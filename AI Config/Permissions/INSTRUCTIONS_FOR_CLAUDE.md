# Instructions for Claude — install these CLI configs on this machine

You are being asked to install three AI-CLI permission configs from another machine. The configs make each CLI maximally permissive (auto-approve everything) so the user is not repeatedly prompted to confirm actions.

## Files in this folder

| File here | Belongs at | Purpose |
|---|---|---|
| `claude-settings.json` | `<USERHOME>/.claude/settings.json` | Claude Code permissions |
| `gemini-settings.json` | `<USERHOME>/.gemini/settings.json` | Gemini CLI permissions |
| `codex-config.toml`    | `<USERHOME>/.codex/config.toml`    | OpenAI Codex CLI permissions |

`<USERHOME>` is the current user's home folder:
- Windows: `C:\Users\<username>` (i.e. `$env:USERPROFILE`)
- macOS / Linux: `~` (i.e. `$HOME`)

## Before you copy anything — show the user this summary

Tell the user, in plain language:

> "These configs set all three CLIs to **auto-approve every action** — no permission prompts. Specifically:
> - **Claude Code:** allows `PowerShell(*)` (any PowerShell command) plus all Bash/Edit/Write/Read/Glob/Grep. The deny list still blocks `rm -rf`, `git push`, `curl`, `wget`, and writes to `data/` — but only for Bash, not PowerShell equivalents.
> - **Gemini CLI:** `defaultApprovalMode = yolo`, folder-trust disabled, sandbox removed. Env-var redaction is still on (API_KEY, TOKEN, SECRET, PASSWORD, DATABASE_URL).
> - **Codex CLI:** `approval_policy = never`, `sandbox_mode = danger-full-access`. No file or network restrictions.
>
> This is the same trade-off you chose on the original machine: maximum convenience, minimum safety. Want me to proceed?"

If they decline, stop. If they accept, continue below.

## Installation steps

For each of the three destinations:

1. **Check if the target file already exists.** If yes, back it up to `<destination>.backup-<YYYYMMDD>` before overwriting. Do not silently clobber.
2. **Check if the parent folder exists.** If `.claude` / `.gemini` / `.codex` doesn't exist yet, the corresponding CLI has never been run on this machine. Create the folder, then warn the user that they'll need to actually install + login to that CLI before the config takes effect.
3. **Copy the file**, renaming back to its real name:
   - `claude-settings.json` → `settings.json` in `.claude/`
   - `gemini-settings.json` → `settings.json` in `.gemini/`
   - `codex-config.toml` → `config.toml` in `.codex/`

## Codex file — IMPORTANT path cleanup

The `codex-config.toml` file contains ~35 `[projects.'...']` entries with hardcoded paths from the source machine — username `jyama`, specific drive letters (`c:\`, `d:\`, `e:\`), and folders like `Desktop\jahren new features\...`.

These entries are **harmless if left alone** (they just mark folders as trusted; unmatched paths are ignored). But they're stale on a new machine.

Ask the user:
- "Want me to strip the stale `[projects.'...']` entries from the Codex config? They reference paths that don't exist on this machine. Removing them keeps the file clean; leaving them in is harmless."

If yes, delete every `[projects.'...']` block AND its `trust_level = "trusted"` line. Keep `[tui.model_availability_nux]` and `[notice]` blocks and the top two `approval_policy` / `sandbox_mode` lines.

If the username on this machine is different from `jyama` and they want to preserve some of those project entries, do a search/replace on `jyama` → new username AFTER confirming the new paths actually exist.

## Auth — heads up

None of these files include login credentials. After installing, the user needs to re-authenticate each CLI:

- Claude Code: run `claude` and complete `/login`
- Gemini: launch `gemini` — it'll prompt for OAuth on first use
- Codex: run `codex login`

## Platform notes

- **`PowerShell(*)`** in the Claude config is Windows-specific. On macOS/Linux it's a no-op (commands run through bash, which is already covered by the tool-level `Bash` allow). No need to remove it.
- **`[windows] sandbox`** is not in the Codex config because it was removed (would conflict with `danger-full-access`). Nothing to do.
- **Backslash paths** in the Codex deny rules don't apply on macOS/Linux. They're already gone in this config (`codex-handoff` permission profile was removed), so this is moot.

## After installation

1. Tell the user the changes take effect on next CLI restart.
2. Remind them to re-login (see "Auth" above).
3. If you stripped the `[projects.'...']` entries from Codex, tell them they'll get a one-time "trust this folder?" prompt the first time they `cd` into a new project — answering "yes always" re-populates the trust list naturally.
