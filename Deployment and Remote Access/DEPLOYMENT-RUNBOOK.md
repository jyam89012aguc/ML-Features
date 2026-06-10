# Remote-Desktop Deployment — Single Source of Truth

> **This file replaces and supersedes the three older, conflicting handoffs:**
> `CHAT-HANDOFF.md`, `HANDOFF 3.md`, and `REMOTE-ACCESS-HANDOFF 1 1.md`.
> Those described two incompatible plans (one ACL-locked-to-owner, one flat/no-ACL).
> **Delete them** once you've swapped this in, so there's no ambiguity.

Last updated: 2026-06-03

---

## The plan in one paragraph

**6 Windows 11 Pro machines**, each reachable by **RDP tunneled inside Tailscale**
(no public 3389 exposure). Each machine has one local **admin** account `remoteuser`,
with NLA, the firewall opened, and a brute-force lockout. A Tailscale **ACL** locks
RDP so that only two identities can connect: **you** (the tailnet owner) and **one
separate remote user** (a different person, invited onto your tailnet).

| Role | Tailscale login |
|---|---|
| **Owner / admin** (deploys + can RDP) | `jason.yamaguchi@gmail.com` |
| **Remote user** (separate person, can RDP) | `jko.respeto@gmail.com` |

> ⚠️ The remote user is a **separate person** (`jko.respeto@gmail.com`) who is
> **already a member of this tailnet** (they own `desktop-v012psj` and a MacBook here).
> So no invite is needed — they only have to be **listed in `group:rdp-admins`** (done
> in the ACL) and sign into Tailscale on whatever device they'll RDP from.

---

## Files in this folder (`C:\Users\<you>\Downloads\`)

| File | Purpose |
|---|---|
| `bootstrap-remote-machine.ps1` | **One-shot per-machine setup.** Installs Tailscale, signs in (tagged `tag:rdp-host`, unattended), creates `remoteuser` admin, enables RDP+NLA+firewall, sets lockout. Idempotent. Run ELEVATED on each machine. **No edits needed.** |
| `tailnet-acl.hujson` | Tailnet ACL. Restricts RDP/3389 on `tag:rdp-host` machines to `group:rdp-admins` only. Paste into the admin console once. **Edit: put the remote user's email in place of the placeholder.** |
| `revoke-remote-user.ps1` | Disables/removes `remoteuser` on a machine. Run per machine to off-board. |
| `setup-remote-user 1.ps1` | Original RDP-only script (no Tailscale). Superseded by bootstrap; kept for reference. |
| `DEPLOYMENT-RUNBOOK.md` | This file — the only handoff to follow. |

---

## Current status (2026-06-10)

| # | Machine | Tailscale IP | State |
|---|---|---|---|
| 1 | **TY5600** (`ty560032gb`) | `100.91.222.30` | ✅ Online, RDP serving, `remoteuser` admin, unattended on, **strong password set 2026-06-03** (stored in your password manager). ✅ now **tagged** `tag:rdp-host` (confirmed in `tailscale status` 2026-06-10). |
| 2 | **backuppc** (`backuppc12gb`) | `100.68.191.6` | Online on tailnet (signed in as you, **not** tagged `tag:rdp-host`). Re-run bootstrap `-CheckOnly` to confirm RDP/account state, then apply the tag. |
| 3 | **SEVENSIX0032GB** (`sevensix0032gb`) | `100.92.65.80` | ✅ Done 2026-06-10. Tailscale signed in + **tagged** `tag:rdp-host`, online; `remoteuser` admin + Remote Desktop Users; RDP enabled, NLA required, firewall open; lockout 5/15. ⚠️ password is literal `password` — harden before relying on it. |
| 4 | — | — | Not started |
| 5 | — | — | Not started |
| 6 | — | — | Not started |

> `desktop-v012psj` and `jahrens-macbook-pro` belong to the **remote user**
> (`jko.respeto@gmail.com`) — these are the devices they connect FROM. Do **not** tag
> them as `tag:rdp-host` hosts; they are clients, not deployment targets.

---

## Do these in order

### Step 1 — Apply the ACL (do this FIRST)
The `tag:rdp-host` tag must exist before any machine can advertise it. `tailnet-acl.hujson`
is already filled in — `group:rdp-admins` = you + `jko.respeto@gmail.com`, `tagOwners`
= you only (the remote user does NOT own tags).
1. Admin console → https://login.tailscale.com/admin/acls/file → paste the whole file.
   ⚠️ **Saving REPLACES your entire policy.** `jko.respeto@gmail.com` already has
   devices on this tailnet — this default-deny policy will limit ALL of them to just
   RDP/3389 on the tagged hosts. If they currently rely on other tailnet access, add
   rules for it before saving.
2. Save.

### Step 2 — Confirm the remote user is on the tailnet (already done)
`jko.respeto@gmail.com` is **already a member** of this tailnet (their devices
`desktop-v012psj` / `jahrens-macbook-pro` already appear in `tailscale status`), so
**no invite is needed**. Just make sure whatever device they'll RDP from has Tailscale
installed and is signed in as `jko.respeto@gmail.com`. Step 1's ACL is what actually
grants them RDP access.

### Step 3 — (Optional) Generate a reusable auth key
Skip if you'll use browser login per machine.
1. Admin console → **Settings → Keys** → **Generate auth key**.
2. Reusable: on. Short expiry. Optionally attach tag `tag:rdp-host`.
3. Copy the `tskey-auth-...`. Treat as a secret; let it expire after all machines join.

### Step 4 — Finish TY5600 (this PC) — just needs the tag
TY5600 is already signed in and serving RDP; it only lacks the tag. After Step 1:
```powershell
& "C:\Program Files\Tailscale\tailscale.exe" up `
    --reset --unattended --accept-routes `
    --advertise-tags=tag:rdp-host --hostname=TY5600
```
Then verify it shows `tag:rdp-host` and still has IP `100.91.222.30`:
```powershell
& "C:\Program Files\Tailscale\tailscale.exe" status
```

### Step 5 — Bootstrap machines 2–6
Copy `bootstrap-remote-machine.ps1` onto each machine. In an **elevated** PowerShell:
```powershell
# browser login (press Enter at the auth-key prompt to use the browser):
.\bootstrap-remote-machine.ps1

# or unattended with the key from Step 3:
.\bootstrap-remote-machine.ps1 -AuthKey tskey-auth-XXXXXXXX
```
It installs Tailscale (unattended + `tag:rdp-host`), creates `remoteuser` admin,
enables RDP/NLA/firewall, sets the lockout, and prints the machine's Tailscale IP.
**Set a STRONG password at the prompt** (use the same one on all machines if you want
one credential everywhere). Record each machine's `100.x` IP in the table above.

### Step 6 — Verify every machine
```powershell
.\bootstrap-remote-machine.ps1 -CheckOnly
```
Target state on all 6: `AccountExists / InRdpGroup / InAdminGroup / RdpEnabled /
NlaRequired = True`, `TailscaleState = Running`, and a `TailscaleIP`.

---

## How the REMOTE USER connects (give them this section)

1. On the device you'll connect from, install **Tailscale** and **sign in as
   `jko.respeto@gmail.com`** (the account already on this tailnet). Confirm it shows
   connected.
2. Open **Remote Desktop Connection** (Start → type `mstsc`).
3. In **Computer**, enter the target machine's Tailscale IP (e.g. `100.91.222.30`).
4. **Connect** → username **`remoteuser`** → the password → accept the certificate.
5. To reach a different machine, repeat with that machine's `100.x` IP.

The ACL denies RDP to anyone who is not in `group:rdp-admins`.

---

## Off-boarding / revoking the remote user
1. Remove their device + user from the **Tailscale admin console** (Users / Machines).
2. Remove their email from `group:rdp-admins` in the ACL and re-save.
3. Optionally, on each machine: `.\revoke-remote-user.ps1` (disable) or `-Remove` (delete)
   to retire the `remoteuser` account itself.

---

## Hardening / don't-skip
- **Change TY5600's password** off the literal `password`:
  ```powershell
  Set-LocalUser -Name remoteuser -Password (Read-Host "New password" -AsSecureString)
  ```
  Set a strong password on the other machines at the Step 5 prompt.
- **Let any auth key expire / delete it** once all 6 machines are joined.
- Keep RDP **tailnet-only** — never expose 3389 to the public internet/LAN.
- One `remoteuser` credential opens all 6 machines; rotating it means resetting on all 6
  (`-ResetPassword`), and revoking means disabling/removing it on all 6.
- **Single session per machine:** RDP-ing into a box evicts whoever is on its console.
- Consider enabling **device approval** and **key expiry** for the 6 hosts.

---

## Key facts to carry forward
- Tailnet owner login is **`jason.yamaguchi@gmail.com`** — NOT `jasopenny@yahoo.com`
  (that email appeared in the old handoffs and is not on this tailnet).
- The remote user is **`jko.respeto@gmail.com`** — a separate person who is already a
  tailnet member, authorized purely by being in `group:rdp-admins` (no invite needed).
  This is the difference the old files got wrong.
- The ACL is **tailnet-wide**: one save covers all 6 machines. It is NOT edited per machine.
- `bootstrap-remote-machine.ps1` needs **no edits** — it's parameterized and idempotent.
- Unattended mode (`ForceDaemon`) keeps each host connected for all logins / before
  login — required for RDP to work when no one is at the console.
