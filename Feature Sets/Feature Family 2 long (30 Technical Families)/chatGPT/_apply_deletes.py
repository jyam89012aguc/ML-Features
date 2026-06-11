"""
Apply 383 auto-deletes from the audit:
 - 300 Pattern A: pctdelta_{W}d_base_v00X (every family, every window 5/10/15/21/42/63/84/126/252/504)
 - 80  Pattern B: mean_abs_{W}d_{base,jerk}_v0NN in f17/f20/f21/f27
 - 3   Pattern C: f23 delta_5d_{slope,jerk} sibling dups; f26 level_5d_jerk sibling

For each delete:
 1. Remove the def block + leading comment.
 2. Remove the symbol from the REGISTRY function-name list.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent

# --------------------------------------------------------------------------
# Build delete list
# --------------------------------------------------------------------------

WINDOWS = [5, 10, 15, 21, 42, 63, 84, 126, 252, 504]
PCTDELTA_BASE_SLOTS_001_075 = {5: 6, 10: 21, 15: 36, 21: 51, 42: 66}
PCTDELTA_BASE_SLOTS_076_150 = {63: 81, 84: 96, 126: 111, 252: 126, 504: 141}
MEAN_ABS_BASE_SLOTS_001_075 = {5: 14, 10: 29, 15: 44, 21: 59, 42: 74}
MEAN_ABS_BASE_SLOTS_076_150 = {63: 89, 84: 104, 126: 119, 252: 134, 504: 149}
# jerk slots correspond to the same recipe layout (1..150). Same for slope.
MEAN_ABS_JERK_SLOTS = {5: 14, 10: 29, 15: 44, 21: 59, 42: 74, 63: 89, 84: 104, 126: 119, 252: 134, 504: 149}
MEAN_ABS_SLOPE_SLOTS = MEAN_ABS_JERK_SLOTS

# Pattern A: pctdelta_X_base in every family (10 per family)
UNSIGNED_FAMILIES = {"f17_volatility_regime", "f20_volatility_compression_expansion",
                     "f21_raw_volume_metrics", "f27_volume_regime"}

# Per-family prefix mapping derived from inspecting the registry function names.
# Function name template: <PREFIX>_<RECIPE>_<W>d_<TIER>_v<NNN>_signal
# Read prefix dynamically from the source file by grepping a function def.
def discover_prefix_for_recipe(family_dir: Path):
    """Find the function-name prefix (e.g. 'f01ma_f01_moving_average_systems_ma') by
    locating a base v001 def in the base_001_075 file."""
    base_001 = next(family_dir.glob("*base_001_075*.py"))
    src = base_001.read_text()
    m = re.search(r"def\s+(\S+?)_level_5d_base_v001_signal\(", src)
    if not m:
        # try other v001 naming variants (some families might use different recipe at v001)
        m = re.search(r"def\s+(\S+?)_(?:level|first)_5d_base_v001_signal\(", src)
    if not m:
        raise RuntimeError(f"prefix not found in {base_001}")
    return m.group(1)

def make_delete_list():
    """Return list of (family_dir, file_basename_pattern, fn_name)."""
    deletes = []
    for family_dir in sorted(ROOT.iterdir()):
        if not family_dir.is_dir() or not family_dir.name.startswith("f"):
            continue
        fam = family_dir.name
        prefix = discover_prefix_for_recipe(family_dir)
        # Pattern A — pctdelta_X_base
        for w, slot in PCTDELTA_BASE_SLOTS_001_075.items():
            name = f"{prefix}_pctdelta_{w}d_base_v{slot:03d}_signal"
            deletes.append((family_dir, "base_001_075", name))
        for w, slot in PCTDELTA_BASE_SLOTS_076_150.items():
            name = f"{prefix}_pctdelta_{w}d_base_v{slot:03d}_signal"
            deletes.append((family_dir, "base_076_150", name))

        # Pattern B — mean_abs in unsigned families
        if fam in UNSIGNED_FAMILIES:
            for w, slot in MEAN_ABS_BASE_SLOTS_001_075.items():
                name = f"{prefix}_mean_abs_{w}d_base_v{slot:03d}_signal"
                deletes.append((family_dir, "base_001_075", name))
            for w, slot in MEAN_ABS_BASE_SLOTS_076_150.items():
                name = f"{prefix}_mean_abs_{w}d_base_v{slot:03d}_signal"
                deletes.append((family_dir, "base_076_150", name))
            # jerk file holds slots 1..150
            for w, slot in MEAN_ABS_JERK_SLOTS.items():
                name = f"{prefix}_mean_abs_{w}d_jerk_v{slot:03d}_signal"
                deletes.append((family_dir, "jerk", name))
            # slope file: mean == mean_abs also holds when sig >= 0 (slope op preserves equality)
            for w, slot in MEAN_ABS_SLOPE_SLOTS.items():
                name = f"{prefix}_mean_abs_{w}d_slope_v{slot:03d}_signal"
                deletes.append((family_dir, "slope", name))

        # Pattern C — three specific z-cos dups
        if fam == "f23_on_balance_volume_family":
            deletes.append((family_dir, "slope", f"{prefix}_pctdelta_5d_slope_v006_signal"))
            deletes.append((family_dir, "jerk", f"{prefix}_pctdelta_5d_jerk_v006_signal"))
        if fam == "f26_accumulation_distribution":
            deletes.append((family_dir, "jerk", f"{prefix}_pctdelta_5d_jerk_v006_signal"))
    return deletes


# --------------------------------------------------------------------------
# Surgical edits
# --------------------------------------------------------------------------

def remove_def_block(src: str, fn_name: str) -> str:
    """Remove the function definition block + any preceding single-line `# ...` comment."""
    # Match optional preceding comment then `def fn_name(...): ... return result.replace(...)`
    pat = re.compile(
        r"(?:^# [^\n]*\n)?^def\s+" + re.escape(fn_name) + r"\(.*?\n(?:[^\n]*\n)+?\s*return [^\n]*\n",
        flags=re.MULTILINE,
    )
    new_src, n = pat.subn("", src, count=1)
    if n == 0:
        raise RuntimeError(f"def block for {fn_name} not found")
    # also drop trailing blank line if it created a double blank
    new_src = re.sub(r"\n\n\n+", "\n\n", new_src)
    return new_src


def remove_from_registry_list(src: str, fn_name: str) -> str:
    """Remove ', fn_name' / 'fn_name, ' from the REGISTRY list-of-functions."""
    # Two variants: leading ', name' or 'name, '
    variants = [
        re.compile(r",\s*" + re.escape(fn_name) + r"\b"),
        re.compile(re.escape(fn_name) + r"\s*,\s*"),
        re.compile(re.escape(fn_name) + r"\b"),
    ]
    for pat in variants:
        new_src, n = pat.subn("", src, count=1)
        if n > 0:
            return new_src
    raise RuntimeError(f"registry entry for {fn_name} not found")


def file_by_pattern(family_dir: Path, pat: str) -> Path:
    matches = list(family_dir.glob(f"*{pat}*.py"))
    if len(matches) != 1:
        raise RuntimeError(f"ambiguous: {pat} in {family_dir} -> {matches}")
    return matches[0]


def apply_deletes():
    deletes = make_delete_list()
    # Group by file so we can do all edits on one file then write
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


if __name__ == "__main__":
    apply_deletes()
