# Pipeline Runbook — run each feature pipeline without the pain
*2026-06-01. Drop this whole `PIPELINE_RUNBOOK` folder's files into each pipeline's
`Deduplication Scripts` folder (next to compute_postgres_feature_registry.py /
compute_postgres_feature_runs.py). Files: `preflight.py`, `run_pipeline.cmd`, `RUNBOOK.md`.*

The rule: **never start the big compute until `preflight.py` prints `0 FAIL` and the smoke test passes.**
That alone prevents 90% of what went wrong last time.

---

## The 6-step procedure for ANY pipeline

### Step 1 — Put the kit in place & set the env
- Copy `preflight.py` + `run_pipeline.cmd` into this pipeline's `Deduplication Scripts` folder.
- Make sure psql is reachable (optional): `[Environment]::SetEnvironmentVariable("PATH",$env:PATH+";C:\Program Files\PostgreSQL\17\bin","User")` then open a NEW terminal.

### Step 2 — Build the registry (only if not built yet)
```
set DATABASE_URL=postgresql://postgres:password@<HOST>:5432/<db_lowercase>
python build_postgres_feature_registry.py --dsn %DATABASE_URL% --init-schema --source-json <sources.json>
```
Run as **postgres** (table owner) to avoid ownership errors. After it finishes, note the
`registry_build_id` (SELECT registry_build_id,count(*) FROM feature_version GROUP BY 1).
**WATCH the build output for**: `no .py files found under ...` or a suspiciously low feature count —
that's the silent-drop regex trap (see Issues #6).

### Step 3 — Edit & run PREFLIGHT  ← the gate
Open `preflight.py`, edit the `CONFIG` block (DSN, REGISTRY_BUILD_ID, PANEL, ARTIFACT_DIR, SOURCE_ROOTS), then:
```
python preflight.py
```
Fix every `[FAIL]` (each prints its FIX). Re-run until `0 FAIL`. Heed `[WARN]`s too.

### Step 4 — SMOKE TEST (end-to-end on 5 features)  ← proves it actually runs
```
python compute_postgres_feature_runs.py --dsn %DATABASE_URL% --input <panel>.parquet ^
  --registry-build-id <id> --data-vendor smoke --data-snapshot-id smoke_test ^
  --universe-id smoke --limit 5 --workers 2 --artifact-dir "%TEMP%\smoke_art"
```
Expect: `eligible_versions` > 0, 5 `feature_computed` lines, `failed: 0`, no Traceback. Then clean up:
```
psql "%DATABASE_URL%" -c "DELETE FROM feature_run WHERE data_snapshot_id='smoke_test';"
```
If the smoke test errors, fix it now — never discover it 40% into a 10-hour run.

### Step 5 — Full compute (resume-safe)
Edit `run_pipeline.cmd` (DSN, panel, build id, snapshot/universe names, workers, artifact dir), then:
```
.\run_pipeline.cmd
```
- `--workers` = the number preflight recommended (min of physical cores and (RAM-5)/per_worker_GB).
- It writes a checkpoint after every feature — if it stops, just run `.\run_pipeline.cmd` again to resume.
- Keep `--mark-output-duplicates` ON for a single-machine run; turn it OFF on per-machine fleet runs and
  run dedup once at the end (see FLEET_RUN_PLAYBOOK).

### Step 6 — After it completes
- Dedup ran automatically (the `--mark-output-duplicates` at the end).
- Sanity: `SELECT count(*) FROM feature_run WHERE data_snapshot_id='<snap>';` ≈ eligible_versions.
- Then feature-removal per FEATURE_REMOVAL_HANDOFF (q0 matrix → bootstrap XGBoost → ~10k features).

---

## KNOWN ISSUES & FIXES (everything that bit us — preflight checks most of these automatically)

| # | Symptom | Cause | Fix | Preflight catches? |
|---|---|---|---|---|
| 1 | `Missing dependency: pip install psycopg[binary]` | deps in a venv, not the python you ran | `"<python>" -m pip install "psycopg[binary]" duckdb pandas numpy tqdm pyarrow` | ✅ deps |
| 2 | `no pg_hba.conf entry for host ...` | DB host doesn't allow this client | On DB host add `host all all <ip-or-/24> scram-sha-256` to pg_hba.conf, `SELECT pg_reload_conf();` | ✅ db connect |
| 3 | `database "Xxx" does not exist` | Postgres is case-sensitive on connect | use the EXACT lowercase DB name (`\l` to list) | ✅ db connect |
| 4 | `password authentication failed` | wrong user/pw | verify, or `ALTER USER u WITH PASSWORD 'p';` | ✅ db connect |
| 5 | `unexpected spaces in "..."` (DSN) | spaces in DSN | percent-encode as `%20`, or use a no-space DB name | ✅ db connect |
| 6 | build warns `no .py files` / low feature count | `is_feature_file()` regex rejects your folder/file prefix (e.g. `technology_`) → files SILENTLY dropped | update the regex prefix in `build_postgres_feature_registry.py` (~line 517), e.g. `^(?:biotech_|technology_)?(?:f?\d{2,3}q?)_` | ✅ feature discovery |
| 7 | `must be owner of table feature_family` | tables owned by another user | run as the owner (postgres), or `REASSIGN OWNED BY postgres TO <user>;` | ✅ write perms |
| 8 | PowerShell: `Missing expression after unary operator '--'` | backtick line-continuation broke on paste | use a single line, or the `.cmd` runner (no continuations) | n/a (use the .cmd) |
| 9 | `argument --dsn: expected one argument` | `$env:DATABASE_URL` empty in a fresh terminal | the `.cmd` sets it internally; or `set DATABASE_URL=...` first | n/a (use the .cmd) |
| 10 | disk fills / `No space left` | each artifact ≈ panel_rows × ~10 B (~26 MB on a 2.6M-row panel); ×50k features = ~1.3 TB | point `--artifact-dir` at a big drive; or shrink the panel; or delete artifacts as you go (DB holds the hashes) | ✅ disk space |
| 11 | run crawls (hours per cluster) | heavy feature families (`rolling().apply`, per-row loops, autocorr) | deploy the OPTIMIZED feature files (`deploy_optimized_ALL_*.zip`); or vectorize per SOLUTION_HANDOFF | profile_heavy.py |
| 12 | machine unresponsive during run | workers oversubscribing cores | lower `--workers`, or set BelowNormal priority: `Get-Process python | %{ $_.PriorityClass='BelowNormal' }` | ✅ sizing |
| 13 | OOM / swapping | too many workers for RAM (each ~1 GB on 2.6M-row panel, ~2.3 GB on 7.4M) | `--workers = min(cores, (RAM-5)/per_worker_GB)` | ✅ sizing |
| 14 | psql not found | not on PATH | full path `"C:\Program Files\PostgreSQL\17\bin\psql.exe"` or add to PATH | n/a |

---

## Files in this kit
- **`preflight.py`** — the gate. Edit CONFIG, run, fix every FAIL. Proven on the `jason_test_local` pipeline (9/9 pass).
- **`run_pipeline.cmd`** — the runner template (sets the env var, runs the full compute). Edit the marked fields.
- **`RUNBOOK.md`** — this file.
- (From the other handoffs on the Desktop: `deploy_optimized_ALL_*.zip` = optimized feature code;
  `MACHINE_WORKER_SIZING_HANDOFF` = worker counts; `SOLUTION_HANDOFF` (in the solutions folder) = the speed fixes;
  `FLEET_RUN_PLAYBOOK` = multi-machine.)
