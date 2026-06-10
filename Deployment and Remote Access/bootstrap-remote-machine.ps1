#requires -RunAsAdministrator
<#
  bootstrap-remote-machine.ps1
  One-shot per-machine bootstrap for the remote-access deployment. Run ELEVATED
  on EACH of the other machines. It:
    1. Installs Tailscale (silent) if not already present.
    2. Signs the machine into your tailnet (auth key, or browser fallback).
    3. Creates the local RDP user, enables Remote Desktop + NLA, opens the
       firewall, adds the user to Remote Desktop Users (+ Administrators),
       and sets the account-lockout policy.
    4. Reports the final state, including this machine's Tailscale IP.

  Idempotent: safe to re-run. Existing account password is left unchanged
  unless you pass -ResetPassword. Tailscale is not reinstalled if present, and
  login is skipped if the machine is already authenticated.

  Examples:
    .\bootstrap-remote-machine.ps1                       # prompts for auth key + password
    .\bootstrap-remote-machine.ps1 -AuthKey tskey-auth-XXXX
    .\bootstrap-remote-machine.ps1 -CheckOnly            # inspect only, no changes
#>
[CmdletBinding()]
param(
    [string]$UserName      = "remoteuser",
    [string]$FullName      = "Remote User",
    [string]$AuthKey       = "",         # Tailscale reusable auth key. Blank => prompt, then browser fallback.
    [string]$Tag           = "tag:rdp-host",  # Tailscale ACL tag applied to this machine (must exist in tagOwners)
    [bool]  $Administrator = $true,      # add user to local Administrators (deployment default: ON)
    [switch]$ResetPassword,              # force-set password even if the account exists
    [switch]$CheckOnly                   # report current state, make no changes
)

# --- To bake in an auth key instead of prompting, uncomment and set this line:
# $AuthKey = "tskey-auth-XXXXXXXXXXXX"

$ErrorActionPreference = 'Stop'

$TS_KEY  = 'HKLM:\System\CurrentControlSet\Control\Terminal Server'
$RDP_KEY = 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp'
$TS_EXE  = "C:\Program Files\Tailscale\tailscale.exe"

function Test-Admin {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    (New-Object Security.Principal.WindowsPrincipal $id).IsInRole(
        [Security.Principal.WindowsBuiltInRole]::Administrator)
}
if (-not (Test-Admin)) { Write-Error "Run this in an ELEVATED (Administrator) PowerShell window."; return }

# Groups via well-known SID (locale-independent).
$rdpGroup   = Get-LocalGroup -SID 'S-1-5-32-555'   # Remote Desktop Users
$adminGroup = Get-LocalGroup -SID 'S-1-5-32-544'   # Administrators

function Find-Tailscale {
    if (Test-Path $TS_EXE) { return $TS_EXE }
    $c = Get-Command tailscale.exe -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    return $null
}

function Get-State {
    $u   = Get-LocalUser -Name $UserName -ErrorAction SilentlyContinue
    $rdp = (Get-ItemProperty $TS_KEY  -Name fDenyTSConnections -ErrorAction SilentlyContinue).fDenyTSConnections -eq 0
    $nla = (Get-ItemProperty $RDP_KEY -Name UserAuthentication -ErrorAction SilentlyContinue).UserAuthentication -eq 1
    $member = $false; $admin = $false
    if ($u) {
        $member = (Get-LocalGroupMember -Group $rdpGroup   -ErrorAction SilentlyContinue).SID.Value -contains $u.SID.Value
        $admin  = (Get-LocalGroupMember -Group $adminGroup -ErrorAction SilentlyContinue).SID.Value -contains $u.SID.Value
    }
    $ts = Find-Tailscale; $tsip = $null; $tsstate = $null
    if ($ts) {
        try { $tsip = (& $ts ip -4 2>$null | Select-Object -First 1) } catch {}
        try { $tsstate = (& $ts status --json 2>$null | ConvertFrom-Json).BackendState } catch {}
    }
    [pscustomobject]@{
        Machine = $env:COMPUTERNAME; AccountExists = [bool]$u; InRdpGroup = $member
        InAdminGroup = $admin; RdpEnabled = [bool]$rdp; NlaRequired = [bool]$nla
        TailscaleInstalled = [bool]$ts; TailscaleState = $tsstate; TailscaleIP = $tsip
    }
}

Write-Host ("`n=== {0} : current state ===" -f $env:COMPUTERNAME)
Get-State | Format-List

if ($CheckOnly) { Write-Host "CheckOnly: no changes made.`n"; return }

# ===================== Tailscale =====================
$ts = Find-Tailscale
if (-not $ts) {
    Write-Host "`nInstalling Tailscale ..."
    $msi = Join-Path $env:TEMP "tailscale-setup.msi"
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest "https://pkgs.tailscale.com/stable/tailscale-setup-latest-amd64.msi" -OutFile $msi -UseBasicParsing
    $p = Start-Process msiexec.exe -ArgumentList "/i `"$msi`" /quiet /norestart TS_UNATTENDEDMODE=always" -Wait -PassThru
    if ($p.ExitCode -ne 0) { Write-Error "Tailscale MSI install failed (exit $($p.ExitCode))." }
    $ts = $TS_EXE
    Write-Host "Tailscale installed."
} else {
    Write-Host "Tailscale already installed."
}

$state = (& $ts status --json 2>$null | ConvertFrom-Json).BackendState
if ($state -ne 'Running') {
    if (-not $AuthKey) {
        $AuthKey = Read-Host "Paste Tailscale auth key (or press Enter for browser login)"
    }
    if ($AuthKey) {
        Write-Host "Bringing Tailscale up with auth key (tag: $Tag) ..."
        & $ts up --authkey $AuthKey --advertise-tags=$Tag --hostname $env:COMPUTERNAME --accept-routes
    } else {
        Write-Host "No key given - starting browser login (tag: $Tag). Watch for the login URL below:"
        & $ts up --advertise-tags=$Tag --hostname $env:COMPUTERNAME --accept-routes
    }
} else {
    Write-Host "Tailscale already signed in."
}

# ===================== Local RDP user =====================
$user = Get-LocalUser -Name $UserName -ErrorAction SilentlyContinue
if (-not $user) {
    $pw = Read-Host "Set password for '$UserName'" -AsSecureString
    New-LocalUser -Name $UserName -FullName $FullName -Description "Remote RDP user" `
                  -Password $pw -PasswordNeverExpires -AccountNeverExpires | Out-Null
    Write-Host "Created account '$UserName'."
    $user = Get-LocalUser -Name $UserName
}
elseif ($ResetPassword) {
    $pw = Read-Host "Reset password for existing '$UserName'" -AsSecureString
    Set-LocalUser -Name $UserName -Password $pw -PasswordNeverExpires $true
    Write-Host "Password reset for '$UserName'."
}
else {
    Write-Host "Account '$UserName' already exists - password left unchanged (use -ResetPassword to force)."
}

# --- group membership (idempotent) ---
$member = (Get-LocalGroupMember -Group $rdpGroup -ErrorAction SilentlyContinue).SID.Value -contains $user.SID.Value
if (-not $member) {
    Add-LocalGroupMember -Group $rdpGroup -Member $user
    Write-Host "Added '$UserName' to Remote Desktop Users."
} else {
    Write-Host "'$UserName' already in Remote Desktop Users."
}

# --- local Administrators (idempotent) ---
if ($Administrator) {
    $isAdmin = (Get-LocalGroupMember -Group $adminGroup -ErrorAction SilentlyContinue).SID.Value -contains $user.SID.Value
    if (-not $isAdmin) {
        Add-LocalGroupMember -Group $adminGroup -Member $user
        Write-Host "Added '$UserName' to Administrators (full control of this machine)."
    } else {
        Write-Host "'$UserName' already in Administrators."
    }
}

# --- enable RDP + require NLA + open firewall ---
Set-ItemProperty $TS_KEY  -Name fDenyTSConnections -Value 0
Set-ItemProperty $RDP_KEY -Name UserAuthentication -Value 1
Enable-NetFirewallRule -Group "@FirewallAPI.dll,-28752"   # locale-independent "Remote Desktop" group
Write-Host "RDP enabled with NLA required; firewall rule on."

# --- machine-wide account lockout (brute-force protection) ---
net accounts /lockoutthreshold:5 /lockoutduration:15 /lockoutwindow:15 | Out-Null
Write-Host "Lockout policy set: 5 attempts, 15-min lockout."

# ===================== Report =====================
Write-Host "`n=== final state ==="
$final = Get-State
$final | Format-List
if (-not $final.TailscaleIP) {
    Write-Host "!! No Tailscale IP yet. If a browser login URL appeared above, finish sign-in, then re-run with -CheckOnly."
} else {
    Write-Host ("RDP target for this machine:  {0}  (user: {1})" -f $final.TailscaleIP, $UserName)
}
