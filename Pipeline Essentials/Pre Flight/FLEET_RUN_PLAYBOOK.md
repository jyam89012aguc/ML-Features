# Fleet Run Playbook
*2026-06-01 — companion to MACHINE_WORKER_SIZING_HANDOFF + SOLUTION_HANDOFF*

Optimization is COMPLETE (4 waves, ~680 sites vectorized, 0 outputs broken — verified bit-identical
where required and within 1e-12 tolerance for the autocorr/OLS class). Deploy package:
**`deploy_optimized_ALL_2026-06-01.zip`** (488 .py files, all vendors f01–f30).

This machine (.114) keeps running **set 1** (`jason_test_local`) on the full optimized code.

---

## What I CANNOT do (needs you)
- I only have shell access to **.114**. Launching on the other 6 machines is manual.
- `pg_hba.conf` is permission-locked — **you** must open the DB host (step 1).
- I don't have the other **9 sets'** details — I need: each set's **DB name, panel parquet path,
  and whether its registry is built**, plus the **7 machines' IPs + cores/RAM**, to make the
  per-machine commands fully concrete.

---

## Step 0 — On EACH machine (one-time)
1. Apply the optimized code: copy `deploy_optimized_ALL_2026-06-01.zip` over and
   `Expand-Archive <zip> -DestinationPath "<...>\Feature Family 2 long (30 Technical Families)" -Force`.
2. Python deps: `python -m pip install "psycopg[binary]" duckdb pandas numpy tqdm pyarrow`.
3. Each machine needs a local copy of the panel parquet for the set(s) it will run.

## Step 1 — Open the DB host (.114), YOU run as admin
Edit `E:\postgre\data\pg_hba.conf`, add under the IPv4 section:
```
host    all    all    192.168.68.0/24    scram-sha-256
```
Then reload (psql as postgres):  `SELECT pg_reload_conf();`
Test from another machine:  `psql -h 192.168.68.114 -U postgres -d jason_test_local`

## Step 2 — Assign work
**Model (recommended): one machine = whole set(s).** Each machine computes a full set independently
against the shared DB on .114. Simple, no cross-machine coordination.
- 10 sets ÷ 7 machines → 3 machines take 2 sets, 4 take 1. The **8-core laptops** (5825U) take 2.
- Per-set time on optimized code ≈ ~6–9 h on a 6-core (the rank-corr tail in f14/f17/f24/f25 remains).
  So a machine with 2 sets ≈ ~12–18 h; with the laptops on the doubles and family-splitting the slowest
  set, the whole fleet lands ~12–14 h. (If you need strict <12 h, split the 2–3 slowest sets by family
  across idle machines once they finish their first — see Model B in SOLUTION/handoff.)

**Worker count per machine** (from MACHINE_WORKER_SIZING_HANDOFF):
`workers = min(physical_cores, floor((RAM_GB − 5) / per_worker_GB))`, per_worker ≈ 1 GB (10× panel) / 2.3 GB (full panel).
- Desktop 6c/64 GB (also DB host): **6**.  5825U 8c/16 GB: **8** (10× panel) / 4–5 (full).  16 GB/4c: **4**.

## Step 3 — Per-machine command (one per set that machine owns)
```
set DATABASE_URL=postgresql://postgres:password@192.168.68.114:5432/<SET_DB>
python compute_postgres_feature_runs.py --dsn %DATABASE_URL% ^
  --input <SET_PANEL>.parquet --registry-build-id <BUILD_ID> ^
  --data-vendor silver_duckdb --data-snapshot-id <SET_SNAPSHOT> ^
  --universe-id <SET_UNIVERSE> --workers <N> --artifact-dir "<local fast drive>"
```
- **Do NOT pass `--mark-output-duplicates` on the per-machine runs** (it must see all features at once).
- Artifacts go to each machine's **local** drive (they're throwaway after hashing — the DB holds the dedup data).
- **Resume-safe:** re-running the same command resumes from that machine's local checkpoint.

## Step 4 — Dedup, ONCE per set, after that set's compute is fully done
On any one machine, for each completed set:
```
python compute_postgres_feature_runs.py --dsn postgresql://postgres:password@192.168.68.114:5432/<SET_DB> ^
  --input <SET_PANEL>.parquet --registry-build-id <BUILD_ID> --data-vendor silver_duckdb ^
  --data-snapshot-id <SET_SNAPSHOT> --universe-id <SET_UNIVERSE> --mark-output-duplicates --limit 1
```
(Uses DB hashes, not artifacts — so artifacts can already be deleted.)

## Step 5 — Then feature-removal (per FEATURE_REMOVAL_HANDOFF)
Per set: build the q0 training matrix → bootstrap/walk-forward XGBoost → keep ~10k independent features.

---

## Set 1 (this machine) — concrete, already running
DB `jason_test_local`, build 1, panel `winners_controls_10x_panel.parquet`, snapshot `snapshot_10x_db_long30`,
universe `db_us_equity_10x_long30`, 10 workers, artifacts `E:\feature_run_artifacts_10x`. ~44% done.

## What I need from you to finish the fleet commands
1. The 9 other sets: **DB name · panel path · registry built? (Y/N) · build id** for each.
2. The 7 machines: **IP · cores · RAM** for each.
Give me those and I'll generate a ready-to-paste command file per machine.
