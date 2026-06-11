"""
Additional 40 deletes: mean_abs_*_slope in 4 unsigned-signal families.
The slope op (diff/abs.shift) preserves equality when sig >= 0,
so mean == mean_abs in slope tier too.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _apply_deletes import (
    discover_prefix_for_recipe,
    file_by_pattern,
    remove_def_block,
    remove_from_registry_list,
)

ROOT = Path(__file__).parent

UNSIGNED_FAMILIES = {"f17_volatility_regime", "f20_volatility_compression_expansion",
                     "f21_raw_volume_metrics", "f27_volume_regime"}
SLOPE_SLOTS = {5: 14, 10: 29, 15: 44, 21: 59, 42: 74, 63: 89, 84: 104, 126: 119, 252: 134, 504: 149}

deletes = []
for family_dir in sorted(ROOT.iterdir()):
    if not family_dir.is_dir() or family_dir.name not in UNSIGNED_FAMILIES:
        continue
    prefix = discover_prefix_for_recipe(family_dir)
    for w, slot in SLOPE_SLOTS.items():
        name = f"{prefix}_mean_abs_{w}d_slope_v{slot:03d}_signal"
        deletes.append((family_dir, "slope", name))

by_file = {}
for family_dir, pat, fn_name in deletes:
    fpath = file_by_pattern(family_dir, pat)
    by_file.setdefault(fpath, []).append(fn_name)

total = 0
for fpath, names in by_file.items():
    src = fpath.read_text()
    for name in names:
        src = remove_def_block(src, name)
        src = remove_from_registry_list(src, name)
        total += 1
    fpath.write_text(src)
    print(f"  {fpath.relative_to(ROOT)}: removed {len(names)}")
print(f"\nTOTAL DELETES: {total}")
