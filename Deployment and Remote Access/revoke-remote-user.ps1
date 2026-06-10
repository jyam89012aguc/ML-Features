#requires -RunAsAdministrator
<#
  revoke-remote-user.ps1
  Revokes the remote RDP user on THIS machine. Run on EACH machine.

  Default action is -Disable (reversible lockout): the account stays but can't
  log in. Pass -Remove to delete the account permanently. Idempotent: safe to
  re-run. Use -CheckOnly to inspect without changing anything.

  This does NOT disable RDP or change the lockout policy machine-wide, since
  other local accounts may rely on them. It only touches the remote user.

  Examples:
    .\revoke-remote-user.ps1 -CheckOnly
    .\revoke-remote-user.ps1            # disables 'remoteuser' (reversible)
    .\revoke-remote-user.ps1 -Remove    # deletes 'remoteuser' permanently
#>
[CmdletBinding()]
param(
    [string]$UserName  = "remoteuser",
    [switch]$Remove,      # delete the account instead of just disabling it
    [switch]$CheckOnly    # report current state, make no changes
)

$ErrorActionPreference = 'Stop'

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
    $u = Get-LocalUser -Name $UserName -ErrorAction SilentlyContinue
    $member = $false; $admin = $false
    if ($u) {
        $member = (Get-LocalGroupMember -Group $rdpGroup   -ErrorAction SilentlyContinue).SID.Value -contains $u.SID.Value
        $admin  = (Get-LocalGroupMember -Group $adminGroup -ErrorAction SilentlyContinue).SID.Value -contains $u.SID.Value
    }
    [pscustomobject]@{
        Machine       = $env:COMPUTERNAME
        AccountExists = [bool]$u
        AccountEnabled = if ($u) { [bool]$u.Enabled } else { $false }
        InRdpGroup    = $member
        InAdminGroup  = $admin
    }
}

Write-Host ("`n=== {0} : current state ===" -f $env:COMPUTERNAME)
Get-State | Format-List

if ($CheckOnly) { Write-Host "CheckOnly: no changes made.`n"; return }

$user = Get-LocalUser -Name $UserName -ErrorAction SilentlyContinue
if (-not $user) {
    Write-Host "Account '$UserName' does not exist - nothing to revoke."
    return
}

# Remove from Remote Desktop Users group (idempotent).
$member = (Get-LocalGroupMember -Group $rdpGroup -ErrorAction SilentlyContinue).SID.Value -contains $user.SID.Value
if ($member) {
    Remove-LocalGroupMember -Group $rdpGroup -Member $user
    Write-Host "Removed '$UserName' from Remote Desktop Users."
} else {
    Write-Host "'$UserName' not in Remote Desktop Users - skipping."
}

# Remove from Administrators group (idempotent) - critical: don't leave a
# "revoked" account sitting as a local admin.
$isAdmin = (Get-LocalGroupMember -Group $adminGroup -ErrorAction SilentlyContinue).SID.Value -contains $user.SID.Value
if ($isAdmin) {
    Remove-LocalGroupMember -Group $adminGroup -Member $user
    Write-Host "Removed '$UserName' from Administrators."
} else {
    Write-Host "'$UserName' not in Administrators - skipping."
}

if ($Remove) {
    Remove-LocalUser -Name $UserName
    Write-Host "Deleted account '$UserName' permanently."
} else {
    if ($user.Enabled) {
        Disable-LocalUser -Name $UserName
        Write-Host "Disabled account '$UserName' (reversible: Enable-LocalUser -Name $UserName)."
    } else {
        Write-Host "Account '$UserName' already disabled."
    }
}

Write-Host "`n!! Don't forget: remove the remote user's laptop from the Tailscale admin console too."

Write-Host "`n=== final state ==="
Get-State | Format-List
