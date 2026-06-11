@echo off
REM ============ EDIT THESE 7 LINES PER PIPELINE, then just run:  .\run_pipeline.cmd ============
set "DATABASE_URL=postgresql://postgres:password@localhost:5432/REPLACE_db_lowercase_nospaces"
set "PANEL=REPLACE_panel.parquet"
set "BUILD_ID=1"
set "SNAPSHOT=REPLACE_snapshot_id"
set "UNIVERSE=REPLACE_universe_id"
set "WORKERS=6"
set "ARTIFACT_DIR=E:\REPLACE_artifact_dir_on_a_big_drive"
REM ===========================================================================================
REM Resume-safe: if it stops, just run this file again (it skips finished features via the checkpoint).
REM Single machine: keep --mark-output-duplicates. Fleet/per-machine: REMOVE it and run dedup once at the end.

python compute_postgres_feature_runs.py --dsn %DATABASE_URL% --input "%PANEL%" --registry-build-id %BUILD_ID% --data-vendor silver_duckdb --data-snapshot-id %SNAPSHOT% --universe-id %UNIVERSE% --mark-output-duplicates --workers %WORKERS% --artifact-dir "%ARTIFACT_DIR%" --no-progress-bar --progress-every 50
