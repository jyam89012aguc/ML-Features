# Deploy: optimized f01–f04 feature files → the 7 machines
*2026-06-01*

## What this is
`deploy_optimized_f01-f04_2026-06-01.zip` (on this Desktop) — the **64 optimized feature files**
(claude/chatGPT/gemini/perplexity × f01–f04 × base/slope/jerk·ranges). These are the only files the
optimization changed (230 vectorized sites; verified bit-identical to the originals on real data).
They are **self-contained** — they need only numpy + pandas (already required). No new dependencies.

The zip preserves the folder structure:
```
claude\f01_moving_average_systems\..._claude.py
chatGPT\f03_trend_strength_metrics\..._chatGPT.py
gemini\...   perplexity\...
```

## Why this matters
On each machine the fleet run computes features by importing these files. With the originals, the
f01–f04 families run ~10–15× slower (the live run is hitting that now). With these, f03/f04 run at
fast-family rates → per-set time drops toward ~5–7 h → 10 sets across 7 machines in <12 h.

## ⚠️ I can only reach THIS desktop (.114)
I don't have network access to the other 6 machines, so I can't push the files there. Distribute the
zip by whatever you already use (shared drive, network copy, or USB), then apply it on each machine.

## Apply on EACH machine (1 minute)
Precondition: the machine already has a copy of the `Feature Family 2 long (30 Technical Families)`
feature tree (same one used to build the registry). If not, copy the whole tree first.

1. Copy `deploy_optimized_f01-f04_2026-06-01.zip` to the machine.
2. **Unzip it INTO the feature-tree root**, overwriting the originals. PowerShell:
   ```powershell
   Expand-Archive -Path "<path>\deploy_optimized_f01-f04_2026-06-01.zip" `
     -DestinationPath "<...>\Feature Family 2 long (30 Technical Families)" -Force
   ```
   (The vendor\family subfolders line up, so files land exactly over the originals.)
3. **Verify** (optional but recommended): compile-check the 64 files —
   ```powershell
   Get-ChildItem "<root>\claude\f0[1-4]_*","<root>\chatGPT\f0[1-4]_*","<root>\gemini\f0[1-4]_*","<root>\perplexity\f0[1-4]_*" -Filter *.py -Recurse |
     ForEach-Object { python -c "import py_compile,sys; py_compile.compile(sys.argv[1],doraise=True)" $_.FullName }
   ```
   No output = all compiled OK.

## Shared-drive shortcut (if all machines mount one network path)
If the 7 machines read the feature tree from ONE shared location, you only need to apply the zip ONCE
to that shared copy — every machine then sees the optimized files. (If each machine has its own local
copy, apply on each.)

## Python deps on each machine (if not already present)
```powershell
python -m pip install "psycopg[binary]" duckdb pandas numpy tqdm pyarrow
```

## After deploy → fleet run
Use MACHINE_WORKER_SIZING_HANDOFF + FEATURE_REMOVAL_HANDOFF: each machine runs its family slice
against the shared Postgres (no --mark-output-duplicates per machine), then run dedup once at the end.
Ask me and I'll generate the exact per-machine commands (worker counts already sized per RAM/cores).

## Note on the currently-running 10× job
It keeps using the ORIGINAL cached code and finishes on its own (~Mon evening). Its outputs are
identical to the optimized code's, so nothing it has computed is wasted — deploying now does not affect it.
