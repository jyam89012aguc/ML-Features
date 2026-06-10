#requires -RunAsAdministrator
<#
  setup-remote-user.ps1
  Creates one local RDP user, enables Remote Desktop with NLA, sets account
  lockout policy, and reports the Tailscale IP. Run on EACH machine.

  Idempotent: safe to re-run. Will NOT change an existing account's password
  unless you pass -ResetPassword. Use -CheckOnly to inspect without changing.

  Pass -Administrator to also add the user to the local Administrators group
  (full control of the box, not just remote-desktop login). FOR THIS DEPLOYMENT,
  pass -Administrator on every machine so all 5 match.

  Examples:
    .\setup-remote-user.ps1 -CheckOnly
    .\setup-remote-user.ps1 -UserName remoteuser -FullName "Remote User" -Administrator
    .\setup-remote-user.ps1 -UserName remoteuser -ResetPassword
#>
[CmdletBinding()]
param(
    [string]$UserName     = "remoteuser",
    [string]$FullName     = "Remote User",
    [switch]$ResetPassword,   # force-set password even if the account exists
    [switch]$Administrator,   # also add the user to the local Administrators group
    [switch]$CheckOnly        # report current state, make no changes
)

$ErrorActionPreference = 'Stop'

$TS_KEY  = 'HKLM:\System\CurrentControlSet\Control\Terminal Server'
$RDP_KEY = 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp'

function Test-Admin {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    (New-Object Security.Principal.WindowsPrincipal $id).IsInRole(
        [Security.Principal.WindowsBuiltInRole]::Administrator)
}
if (-not (Test-Admin)) { Write-Error "Run this in an ELEVATED (Administrator) PowerShell window."; return }

# Groups via well-known SID (locale-independent).
$rdpGroup   = Get-LocalGroup -SID 'S-1-5-32-555'   # Remote Desktop Users
$adminGroup = Get-LocalGroup -SID 'S-1-5-32-544'   # Administrators

function Get-State {
    $u   = Get-LocalUser -Name $UserName -ErrorAction SilentlyContinue
    $rdp = (Get-ItemProperty $TS_KEY  -Name fDenyTSConnections -ErrorAction SilentlyContinue).fDenyTSConnections -eq 0
    $nla = (Get-ItemProperty $RDP_KEY -Name UserAuthentication -ErrorAction SilentlyContinue).UserAuthentication -eq 1
    $member = $false; $admin = $false
    if ($u) {
        $member = (Get-LocalGroupMember -Group $rdpGroup   -ErrorAction SilentlyContinue).SID.Value -contains $u.SID.Value
        $admin  = (Get-LocalGroupMember -Group $adminGroup -ErrorAction SilentlyContinue).SID.Value -contains $u.SID.Value
    }
    $tsip = $null
    $ts = Get-Command tailscale.exe -ErrorAction SilentlyContinue
    if ($ts) { try { $tsip = (& tailscale ip -4 2>$null | Select-Object -First 1) } catch {} }
    [pscustomobject]@{
        Machine = $env:COMPUTERNAME; AccountExists = [bool]$u; InRdpGroup = $member
        InAdminGroup = $admin; RdpEnabled = [bool]$rdp; NlaRequired = [bool]$nla
        TailscaleInstalled = [bool]$ts; TailscaleIP = $tsip
    }
}

Write-Host ("`n=== {0} : current state ===" -f $env:COMPUTERNAME)
Get-State | Format-List

if ($CheckOnly) { Write-Host "CheckOnly: no changes made.`n"; return }

# --- account ---
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

# --- local Administrators (only with -Administrator; idempotent) ---
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

# --- Tailscale ---
$final = Get-State
if (-not $final.TailscaleInstalled) {
    Write-Host "`n!! Tailscale NOT installed. Install from https://tailscale.com/download and sign into your tailnet."
} else {
    Write-Host ("`nTailscale IP for this machine: {0}" -f $final.TailscaleIP)
}

Write-Host "`n=== final state ==="
$final | Format-List
