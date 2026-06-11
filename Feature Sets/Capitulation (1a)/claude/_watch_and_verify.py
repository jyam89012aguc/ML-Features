"""Wait until the feature tree stops changing, then run _verify.py once.

Quietness is detected by content, not timestamps: snapshot every feature .py
file's (size, mtime); when two consecutive snapshots 90s apart are identical
the build is considered finished. This is robust to clock skew / future
mtimes written by the build process.
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
POLL = 120         # seconds between snapshots
STABLE_NEEDED = 5  # consecutive identical snapshots required (=10 min quiet)
MAX_WAIT = 6 * 3600


def snapshot():
    snap = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if "__pycache__" in dirpath:
            continue
        for fn in filenames:
            if not fn.endswith(".py"):
                continue
            if fn.startswith(("_verify", "_watch", "_audit", "_gapcheck",
                              "_quality_review", "_smoke")):
                continue
            p = os.path.join(dirpath, fn)
            try:
                st = os.stat(p)
                snap[p] = (st.st_size, st.st_mtime)
            except OSError:
                pass
    return snap


def log(msg):
    print(f"{time.strftime('%H:%M:%S')}  {msg}", flush=True)


start = time.time()
prev = snapshot()
log(f"initial snapshot: {len(prev)} feature .py files")
stable = 0
while stable < STABLE_NEEDED:
    if time.time() - start > MAX_WAIT:
        log("MAX_WAIT exceeded - giving up on quiet detection, verifying anyway")
        break
    time.sleep(POLL)
    cur = snapshot()
    if cur == prev:
        stable += 1
        log(f"no change ({len(cur)} files) - stable {stable}/{STABLE_NEEDED}")
    else:
        added = len(set(cur) - set(prev))
        removed = len(set(prev) - set(cur))
        changed = sum(1 for k in set(cur) & set(prev) if cur[k] != prev[k])
        stable = 0
        log(f"changed: +{added} -{removed} ~{changed}  (total {len(cur)})")
    prev = cur

log(f"TREE SETTLED at {len(prev)} feature .py files - running verification")
for d in os.listdir(ROOT):
    pc = os.path.join(ROOT, d, "__pycache__")
    if os.path.isdir(pc):
        for f in os.listdir(pc):
            try:
                os.remove(os.path.join(pc, f))
            except OSError:
                pass
with open(os.path.join(ROOT, "_vchk.txt"), "w", encoding="utf-8") as out:
    rc = subprocess.run([sys.executable, os.path.join(ROOT, "_verify.py")],
                        stdout=out, stderr=subprocess.STDOUT).returncode
log(f"verification complete, exit={rc}, report written to _vchk.txt")
