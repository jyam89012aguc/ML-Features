"""Run __main__ self-tests in every file by importing + invoking the embedded asserts."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
fails = []
total = 0
for fam in sorted(ROOT.iterdir()):
    if not fam.is_dir() or not fam.name.startswith("f"):
        continue
    for f in sorted(fam.glob("*.py")):
        total += 1
        r = subprocess.run([sys.executable, str(f)], capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            fails.append((str(f.relative_to(ROOT)), r.stdout[-300:], r.stderr[-300:]))
            print(f"FAIL {f.relative_to(ROOT)}")
        else:
            print(f"OK   {f.relative_to(ROOT)}")
print(f"\n{total - len(fails)}/{total} pass")
if fails:
    for path, out, err in fails:
        print(f"\n--- {path} ---\nSTDOUT: {out}\nSTDERR: {err}")
    sys.exit(1)
