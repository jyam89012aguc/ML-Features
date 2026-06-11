"""
preflight.py  --  Run this BEFORE the big compute on any pipeline. It checks every
failure mode we hit in the long debug session and tells you the exact fix. Drop this file
in the pipeline's "Deduplication Scripts" folder (next to compute_postgres_feature_runs.py
and build_postgres_feature_registry.py), edit the CONFIG block, and run:

    python preflight.py

Exit code 0 = all critical checks PASS. Non-zero = at least one FAIL (do not run the big job).
"""
import os, sys, shutil, json, ctypes

# ===================== EDIT THIS PER PIPELINE =====================
CONFIG = {
    # Connection. Use lowercase DB name; no spaces (percent-encode as %20 if unavoidable).
    "DSN": "postgresql://postgres:password@localhost:5432/jason_test_local",
    "REGISTRY_BUILD_ID": 1,
    # Panel parquet the compute reads.
    "PANEL": "winners_controls_10x_panel.parquet",
    "TICKER_COL": "ticker",
    "DATE_COL": "date",
    # Where artifacts will be written (check free space here).
    "ARTIFACT_DIR": r"E:\feature_run_artifacts_10x",
    # Roots that hold the feature .py files (for the discovery / regex check).
    "SOURCE_ROOTS": [
        r"E:\JASON_TO_RUN\Feature Family 2 long (30 Technical Families)\claude",
        r"E:\JASON_TO_RUN\Feature Family 2 long (30 Technical Families)\chatGPT",
        r"E:\JASON_TO_RUN\Feature Family 2 long (30 Technical Families)\gemini",
        r"E:\JASON_TO_RUN\Feature Family 2 long (30 Technical Families)\perplexity",
    ],
}
# =================================================================

PASS, WARN, FAIL = "PASS", "WARN", "FAIL"
results = []
def rec(name, status, msg, fix=""):
    results.append((name, status, msg, fix))
    tag = {"PASS": "[ OK ]", "WARN": "[WARN]", "FAIL": "[FAIL]"}[status]
    print(f"{tag} {name}: {msg}")
    if fix and status != PASS:
        print(f"       FIX: {fix}")


def check_deps():
    missing = []
    for mod in ("psycopg", "pandas", "numpy", "pyarrow", "duckdb", "tqdm"):
        try:
            __import__(mod)
        except Exception:
            missing.append(mod)
    if missing:
        rec("python deps", FAIL, f"missing: {missing}",
            f'"{sys.executable}" -m pip install "psycopg[binary]" duckdb pandas numpy tqdm pyarrow')
    else:
        rec("python deps", PASS, "all importable")
    return not missing


def check_db():
    try:
        import psycopg
    except Exception:
        rec("db connect", FAIL, "psycopg not installed", "install deps first")
        return None
    try:
        conn = psycopg.connect(CONFIG["DSN"], connect_timeout=10)
        with conn.cursor() as c:
            c.execute("SELECT current_database(), current_user")
            db, usr = c.fetchone()
        rec("db connect", PASS, f"connected to {db} as {usr}")
        return conn
    except Exception as e:
        m = str(e).lower()
        fix = "check the DSN."
        if "no pg_hba" in m:
            fix = "Add a pg_hba.conf line on the DB host for this client (host all all <ip>/32 scram-sha-256) and SELECT pg_reload_conf();"
        elif "password authentication failed" in m:
            fix = "Wrong password/user. Verify, or ALTER USER ... WITH PASSWORD."
        elif "does not exist" in m and "database" in m:
            fix = "DB name wrong (Postgres is case-sensitive on connect). Use the EXACT lowercase name; \\l in psql to list."
        elif "unexpected spaces" in m:
            fix = "DSN has spaces. Percent-encode them as %20, or pick a no-space DB name."
        elif "could not translate host" in m or "could not connect" in m:
            fix = "Host unreachable. Check the host/IP and that Postgres listens on it (listen_addresses, firewall)."
        rec("db connect", FAIL, str(e).strip()[:140], fix)
        return None


def check_schema(conn):
    need = ["feature_definition", "feature_version", "feature_run"]
    with conn.cursor() as c:
        c.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        have = {r[0] for r in c.fetchall()}
    miss = [t for t in need if t not in have]
    if miss:
        rec("db schema", FAIL, f"missing tables: {miss}",
            "Registry not built in this DB. Run build_postgres_feature_registry.py --init-schema first.")
    else:
        rec("db schema", PASS, "registry tables present")
    return not miss


def check_build(conn):
    bid = CONFIG["REGISTRY_BUILD_ID"]
    with conn.cursor() as c:
        c.execute("SELECT count(*) FROM feature_definition WHERE registry_build_id=%s", (bid,))
        n = c.fetchone()[0]
    if n == 0:
        rec("registry build", FAIL, f"registry_build_id={bid} has 0 features",
            "Build the registry for this id, or point REGISTRY_BUILD_ID at an existing build (SELECT registry_build_id,count(*) FROM feature_version GROUP BY 1).")
    else:
        rec("registry build", PASS, f"build {bid} has {n} features")
    return n > 0


def check_write_perm(conn):
    # Try a transaction that would insert+rollback, to catch ownership/privilege issues.
    try:
        with conn.cursor() as c:
            c.execute("SELECT has_table_privilege(current_user,'feature_run','INSERT'), has_table_privilege(current_user,'feature_run','UPDATE')")
            ins, upd = c.fetchone()
        if ins and upd:
            rec("write perms", PASS, "can INSERT/UPDATE feature_run")
        else:
            rec("write perms", FAIL, f"INSERT={ins} UPDATE={upd}",
                "Run the build/compute as the table OWNER (often postgres), or: REASSIGN OWNED BY postgres TO <user>; / GRANT.")
        return ins and upd
    except Exception as e:
        rec("write perms", WARN, f"could not check: {e}", "")
        return True


def check_panel():
    p = CONFIG["PANEL"]
    if not os.path.exists(p):
        rec("panel file", FAIL, f"not found: {p}", "Fix the PANEL path (use the absolute path if running from elsewhere).")
        return None
    try:
        import pyarrow.parquet as pq
        import pandas as pd
        pf = pq.ParquetFile(p)
        cols = list(pf.schema_arrow.names)
        rows = pf.metadata.num_rows
        tc, dc = CONFIG["TICKER_COL"], CONFIG["DATE_COL"]
        missing = [c for c in (tc, dc) if c not in cols]
        if missing:
            rec("panel file", FAIL, f"missing id columns {missing} (have: {cols[:8]}...)",
                "Set TICKER_COL/DATE_COL to match the parquet, or pass --ticker-col/--date-col to compute.")
            return rows
        # quick NaN check on close-like column
        price_col = next((x for x in ("close", "closeadj") if x in cols), None)
        nanfrac = None
        if price_col:
            s = pd.read_parquet(p, columns=[price_col])[price_col]
            nanfrac = float(s.isna().mean())
        rec("panel file", PASS, f"{rows:,} rows, {len(cols)} cols, close NaN frac={nanfrac}")
        return rows
    except Exception as e:
        rec("panel file", FAIL, f"unreadable: {e}", "Re-export the parquet; check pyarrow installed.")
        return None


def check_discovery():
    """The silent-drop trap: feature files that the build's is_feature_file() regex rejects."""
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from build_postgres_feature_registry import is_feature_file
        from pathlib import Path
        have_fn = True
    except Exception as e:
        is_feature_file = None
        have_fn = False
    total_py = 0
    matched = 0
    from pathlib import Path
    for root in CONFIG["SOURCE_ROOTS"]:
        if not os.path.isdir(root):
            rec("source root", WARN, f"not a dir: {root}", "Fix SOURCE_ROOTS paths.")
            continue
        for py in Path(root).rglob("*.py"):
            if py.name.startswith("_") or "__pycache__" in str(py):
                continue
            total_py += 1
            if have_fn:
                try:
                    if is_feature_file(py):
                        matched += 1
                except Exception:
                    pass
    if total_py == 0:
        rec("feature discovery", FAIL, "0 .py files under SOURCE_ROOTS", "Fix SOURCE_ROOTS to point at the vendor feature folders.")
        return False
    if not have_fn:
        rec("feature discovery", WARN, f"{total_py} .py files found; could not import is_feature_file to test the filter",
            "Run from the Deduplication Scripts folder so build_postgres_feature_registry.py is importable.")
        return True
    drop = total_py - matched
    if matched == 0:
        rec("feature discovery", FAIL, f"is_feature_file() matched 0 of {total_py} files",
            "The folder/file naming doesn't match the regex in build_postgres_feature_registry.py (is_feature_file). Update the regex prefix (e.g. add your family prefix) OR rename folders. This is the 'silently dropped files' trap.")
        return False
    if drop > total_py * 0.05:
        rec("feature discovery", WARN, f"is_feature_file() matched {matched}/{total_py} ({drop} dropped)",
            "Some files are being silently dropped by the is_feature_file regex. If those dropped files are real features, update the regex prefix in build_postgres_feature_registry.py (~line 517).")
    else:
        rec("feature discovery", PASS, f"is_feature_file() matched {matched}/{total_py} files")
    return True


def check_disk(panel_rows, conn):
    drv = os.path.splitdrive(os.path.abspath(CONFIG["ARTIFACT_DIR"]))[0] or "C:"
    try:
        free = shutil.disk_usage(os.path.splitdrive(os.path.abspath(CONFIG["ARTIFACT_DIR"]))[0] + "\\").free
    except Exception:
        free = shutil.disk_usage(".").free
    nfeat = None
    if conn is not None:
        with conn.cursor() as c:
            c.execute("SELECT count(*) FROM feature_definition WHERE registry_build_id=%s", (CONFIG["REGISTRY_BUILD_ID"],))
            nfeat = c.fetchone()[0]
    if not panel_rows or not nfeat:
        rec("disk space", WARN, "can't estimate (missing panel rows or feature count)", "")
        return True
    # Each artifact ~ panel_rows * ~10 bytes (ticker+date+float64 parquet, measured: ~24 MB on a
    # 2.6M-row panel, ~68 MB on a 7.4M-row panel => ~9.2 B/row). Use 10 as a slightly safe figure.
    bytes_per_artifact = panel_rows * 10
    est_total = bytes_per_artifact * nfeat
    free_gb, est_gb = free / 1e9, est_total / 1e9
    msg = f"artifacts est ~{est_gb:.0f} GB ({nfeat} feat x ~{bytes_per_artifact/1e6:.0f} MB), free on {drv} ~{free_gb:.0f} GB"
    if est_total > free * 0.9:
        rec("disk space", FAIL, msg,
            "Not enough room. Options: point --artifact-dir at a bigger drive; shrink the panel (fewer tickers); or treat artifacts as throwaway (the DB holds the hashes) and delete as you go.")
        return False
    rec("disk space", PASS, msg)
    return True


def sizing():
    cores = os.cpu_count() or 4
    ram_gb = None
    try:
        class MS(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                        ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                        ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
        ms = MS(); ms.dwLength = ctypes.sizeof(MS)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(ms))
        ram_gb = ms.ullTotalPhys / 1e9
    except Exception:
        pass
    phys = max(1, cores // 2)  # logical->physical guess for typical HT
    per_worker = 1.0  # GB on a ~2.6M-row panel; ~2.3 on a 7.4M-row panel
    if ram_gb:
        ram_cap = int((ram_gb - 5) / per_worker)
        rec_workers = max(1, min(phys, ram_cap))
        rec("sizing", PASS, f"{cores} logical (~{phys} physical), {ram_gb:.0f} GB RAM -> recommend --workers {rec_workers}",
            "RAM-bound if the panel is large (per worker ~2.3 GB on a 7.4M-row panel) -> lower workers.")
    else:
        rec("sizing", WARN, f"{cores} logical cores -> --workers ~{phys}; couldn't read RAM", "")


def main():
    print("=== PIPELINE PREFLIGHT ===\n")
    ok = True
    ok &= check_deps()
    conn = check_db()
    panel_rows = None
    if conn is not None:
        if not check_schema(conn): ok = False
        if not check_build(conn): ok = False
        check_write_perm(conn)
    else:
        ok = False
    panel_rows = check_panel()
    if panel_rows is None: ok = False
    if not check_discovery(): ok = False
    check_disk(panel_rows, conn)
    sizing()
    fails = [r for r in results if r[1] == FAIL]
    warns = [r for r in results if r[1] == WARN]
    print("\n=== SUMMARY ===")
    print(f"  {len(fails)} FAIL, {len(warns)} WARN, {len(results)-len(fails)-len(warns)} PASS")
    if fails:
        print("  DO NOT run the big job until the FAILs are fixed:")
        for n, _, m, fx in fails:
            print(f"   - {n}: {m}\n       FIX: {fx}")
    else:
        print("  All critical checks passed. Recommended: run the smoke test next (see RUNBOOK.md).")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
