"""Structural schema audit for capitulation feature folders.
Checks each folder against the build schema WITHOUT executing feature code:
  - folder exists; exactly 4 files with the canonical names
  - each file: ast.parse OK, < 75 KB
  - exactly one *_REGISTRY_* dict, correctly named for the folder
  - registry entry counts exactly 75 / 75 / 25 / 25
  - every registry "func" reference is a function defined in the same file
Usage: python _audit.py [LO] [HI]   (default 1 50)
"""
import ast
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LO = int(sys.argv[1]) if len(sys.argv) > 1 else 1
HI = int(sys.argv[2]) if len(sys.argv) > 2 else 50

SUFFIXES = ["base_001_075", "base_076_150", "2nd_derivatives", "3rd_derivatives"]
EXP_COUNT = {"base_001_075": 75, "base_076_150": 75,
             "2nd_derivatives": 25, "3rd_derivatives": 25,
             "extended_001_075": 75}
REG_SUFFIX = {"base_001_075": "REGISTRY_001_075",
              "base_076_150": "REGISTRY_076_150",
              "2nd_derivatives": "REGISTRY_2ND_DERIVATIVES",
              "3rd_derivatives": "REGISTRY_3RD_DERIVATIVES",
              "extended_001_075": "EXTENDED_REGISTRY_001_075"}

folders = {}
for d in os.listdir(ROOT):
    if os.path.isdir(os.path.join(ROOT, d)):
        head = d.split("_")[0]
        if head.isdigit():
            folders[int(head)] = d

clean, gappy = [], []
for fnum in range(LO, HI + 1):
    folder = folders.get(fnum)
    if folder is None:
        gappy.append((fnum, None, [f"folder {fnum:02d}_* does not exist"]))
        continue
    reg_prefix = "_".join(folder.split("_")[1:]).upper()
    fdir = os.path.join(ROOT, folder)
    fg = []
    suffixes = list(SUFFIXES)
    if os.path.exists(os.path.join(fdir, f"{folder}_extended_001_075.py")):
        suffixes.append("extended_001_075")
    for suf in suffixes:
        fname = f"{folder}_{suf}.py"
        path = os.path.join(fdir, fname)
        if not os.path.exists(path):
            fg.append(f"missing file: {fname}")
            continue
        src = open(path, encoding="utf-8").read()
        kb = len(src.encode("utf-8")) / 1024
        if kb >= 75:
            fg.append(f"{fname}: {kb:.1f} KB (>= 75 KB limit)")
        try:
            tree = ast.parse(src)
        except SyntaxError as e:
            fg.append(f"{fname}: ast.parse FAILED — {e}")
            continue
        funcs = {n.name for n in ast.walk(tree)
                 if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        regs = []
        for node in tree.body:
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                for t in node.targets:
                    if isinstance(t, ast.Name) and "REGISTRY" in t.id:
                        regs.append((t.id, node.value))
        if len(regs) != 1:
            fg.append(f"{fname}: {len(regs)} REGISTRY dicts {[n for n, _ in regs]}")
            continue
        rname, rdict = regs[0]
        expect = f"{reg_prefix}_{REG_SUFFIX[suf]}"
        if rname != expect:
            fg.append(f"{fname}: registry '{rname}', expected '{expect}'")
        if len(rdict.keys) != EXP_COUNT[suf]:
            fg.append(f"{fname}: {len(rdict.keys)} entries, expected {EXP_COUNT[suf]}")
        undef = []
        for v in rdict.values:
            if not isinstance(v, ast.Dict):
                continue
            for ik, iv in zip(v.keys, v.values):
                if isinstance(ik, ast.Constant) and ik.value == "func":
                    if isinstance(iv, ast.Name) and iv.id not in funcs:
                        undef.append(iv.id)
                    elif not isinstance(iv, ast.Name):
                        undef.append(type(iv).__name__)
        if undef:
            fg.append(f"{fname}: {len(undef)} registry func ref(s) not defined "
                      f"in file: {sorted(set(undef))[:6]}")
    (gappy if fg else clean).append((fnum, folder, fg))

print(f"Structural schema audit — folders {LO:02d}-{HI:02d}")
print("=" * 64)
print(f"CLEAN: {len(clean)} / {HI - LO + 1}")
for fnum, folder, _ in clean:
    print(f"  ok   {folder}")
print()
if gappy:
    print(f"GAPS: {len(gappy)} folder(s)")
    for fnum, folder, fg in gappy:
        print(f"  [{fnum:02d}] {folder or '(missing)'}")
        for g in fg:
            print(f"       - {g}")
else:
    print("No structural gaps — every folder conforms to the schema.")
