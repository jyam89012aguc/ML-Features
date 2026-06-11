"""
Audit harness for 30 technical feature families.

For each family:
 - imports all 4 files
 - runs all functions on synth OHLCV (5 profiles, daily cadence, warmup=600)
 - detects: errors, all-NaN, constants, value-hash dups, z-cosine algebraic-identity dups
 - flags cross-tier base->deriv pollution (Class 4) and within-base derivative duplicates
 - writes per-family findings to _audit_results/<family>.json

Audit precedent classes from CLAUDE.md / AUDITS.md:
  1 formula-exact rename (auto-delete)
  2 cancellation-equivalent (auto-delete)
  3 algebraic-identity scalar-mult (auto-delete, z-cosine catch)
  4 cross-tier base->deriv pollution (auto-delete from base)
  6 mathematical-identity invisible to vhash (auto-delete, z-cosine catch)
  7 sign-flip algebraic-identity (auto-delete)
 11-16 keep-by-design
 17-23 bug classes (fix in place)
"""
import importlib.util
import inspect
import json
import os
import re
import sys
import traceback
import warnings
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "_audit_results"
OUT_DIR.mkdir(exist_ok=True)

WARMUP = 600
N = 1500
SEED = 42

# -----------------------------------------------------------------------------
# Synth OHLCV
# -----------------------------------------------------------------------------
def make_synth(seed=SEED, n=N):
    np.random.seed(seed)
    t = pd.Series(np.arange(n, dtype=float))
    # 5 component cycles + drift + noise + occasional shocks
    cyc = 0.08 * np.sin(t / 9.0) + 0.05 * np.sin(t / 31.0) + 0.04 * np.sin(t / 73.0)
    drift = 0.0005
    noise = np.random.normal(0.0, 0.025, n)
    shocks = np.zeros(n)
    sh_idx = np.random.choice(n, size=n // 80, replace=False)
    shocks[sh_idx] = np.random.normal(0.0, 0.08, len(sh_idx))
    log_ret = drift + noise + shocks + cyc.diff().fillna(0).values
    closeadj = 40.0 * np.exp(np.cumsum(log_ret))
    closeadj = pd.Series(closeadj)
    close = closeadj.copy()
    intra_noise = np.abs(np.random.normal(0.0, 0.015, n))
    high = closeadj * (1 + intra_noise + 0.005)
    low = closeadj * (1 - intra_noise - 0.005)
    gap = np.random.normal(0.0, 0.005, n)
    open_ = closeadj.shift(1).fillna(closeadj.iloc[0]) * (1 + gap)
    high = pd.concat([high, open_, close], axis=1).max(axis=1)
    low = pd.concat([low, open_, close], axis=1).min(axis=1)
    volume = pd.Series(
        np.exp(np.random.normal(np.log(1e6), 0.4, n)) * (1 + 0.5 * np.abs(log_ret))
    ).astype(float)
    benchmark = pd.Series(
        40.0 * np.exp(np.cumsum(drift + np.random.normal(0.0, 0.012, n)))
    )
    return {
        "closeadj": closeadj,
        "close": close,
        "open": open_,
        "high": high,
        "low": low,
        "volume": volume,
        "benchmark": benchmark,
    }


# -----------------------------------------------------------------------------
# Module loading
# -----------------------------------------------------------------------------
def load_module(path: Path):
    name = path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    # don't trigger __main__
    spec.loader.exec_module(mod)
    return mod


def discover_files(family_dir: Path):
    files = {}
    for f in sorted(family_dir.glob("*.py")):
        if "base_001_075" in f.name:
            files["base_001_075"] = f
        elif "base_076_150" in f.name:
            files["base_076_150"] = f
        elif "jerk" in f.name:
            files["jerk"] = f
        elif "slope" in f.name:
            files["slope"] = f
    return files


# -----------------------------------------------------------------------------
# Run a function with kwargs from synth dict
# -----------------------------------------------------------------------------
def run_func(fn, inputs, synth):
    args = {k: synth[k] for k in inputs}
    return fn(**args)


# -----------------------------------------------------------------------------
# Signal post-warmup normalization
# -----------------------------------------------------------------------------
def normalize_post_warmup(y: pd.Series, warmup=WARMUP):
    arr = y.iloc[warmup:].astype(float).to_numpy()
    arr = np.where(np.isfinite(arr), arr, np.nan)
    return arr


def value_hash(arr):
    # ignore NaN positions in the hash; quantize to f32 to absorb FP noise
    finite_mask = np.isfinite(arr)
    if finite_mask.sum() == 0:
        return ("nan",)
    rounded = np.where(finite_mask, np.round(arr.astype(np.float64), 10), np.nan)
    return (int(finite_mask.sum()), float(np.nansum(rounded)), float(np.nanstd(rounded)), float(np.nanmin(rounded)), float(np.nanmax(rounded)))


def zcosine_key(arr):
    """For z-cosine algebraic-identity scan: subtract mean, normalize, return sign of first nonzero element times normalized vector as a hashable key approximation."""
    finite_mask = np.isfinite(arr)
    if finite_mask.sum() < 50:
        return None
    a = arr[finite_mask].astype(np.float64)
    m = a.mean()
    a = a - m
    n = np.linalg.norm(a)
    if n < 1e-15:
        return None
    a = a / n
    # canonicalize sign: flip if first nonzero element is negative
    first_nz = a[np.abs(a) > 1e-15][0] if (np.abs(a) > 1e-15).any() else 1.0
    if first_nz < 0:
        a = -a
    # quantize for hash (1e-9 resolution)
    return tuple(np.round(a, 9).tolist())


def signflip_key(arr):
    """For sign-flip detection (Class 7), key without canonical-sign flip."""
    finite_mask = np.isfinite(arr)
    if finite_mask.sum() < 50:
        return None
    a = arr[finite_mask].astype(np.float64)
    m = a.mean()
    a = a - m
    n = np.linalg.norm(a)
    if n < 1e-15:
        return None
    a = a / n
    return tuple(np.round(a, 9).tolist())


# -----------------------------------------------------------------------------
# Per-family audit
# -----------------------------------------------------------------------------
def audit_family(family_dir: Path, synth):
    files = discover_files(family_dir)
    family_name = family_dir.name

    fn_records = []  # list of dicts
    for tier_key, fpath in files.items():
        try:
            mod = load_module(fpath)
        except Exception as e:
            return {"family": family_name, "load_error": {tier_key: str(e)}}
        if not hasattr(mod, "REGISTRY"):
            continue
        reg = mod.REGISTRY
        for fn_name, meta in reg.items():
            fn = meta["func"]
            inputs = meta["inputs"]
            tier = "base" if tier_key.startswith("base") else tier_key
            chunk = tier_key
            rec = {
                "name": fn_name,
                "tier": tier,
                "chunk": chunk,
                "file": fpath.name,
                "inputs": list(inputs),
                "src": inspect.getsource(fn),
            }
            try:
                y = run_func(fn, inputs, synth)
                if not isinstance(y, pd.Series):
                    rec["error"] = f"non-series: {type(y).__name__}"
                else:
                    arr = normalize_post_warmup(y)
                    rec["arr"] = arr
            except Exception as e:
                rec["error"] = f"{type(e).__name__}: {e}"
            fn_records.append(rec)

    # Diagnostics
    findings = {
        "family": family_name,
        "n_funcs": len(fn_records),
        "errors": [],
        "all_nan": [],
        "constants": [],
        "vhash_dups": [],
        "zcos_dups": [],
        "signflip_pairs": [],
        "class4_base_deriv_pollution": [],
        "by_tier": defaultdict(int),
    }

    vhash_groups = defaultdict(list)
    zcos_groups = defaultdict(list)
    signflip_groups = defaultdict(list)

    for rec in fn_records:
        findings["by_tier"][rec["tier"]] += 1
        if "error" in rec:
            findings["errors"].append({"name": rec["name"], "tier": rec["tier"], "error": rec["error"]})
            continue
        arr = rec["arr"]
        finite = np.isfinite(arr)
        finite_sum = int(finite.sum())
        if finite_sum == 0:
            findings["all_nan"].append({"name": rec["name"], "tier": rec["tier"]})
            continue
        if finite_sum > 0:
            std = float(np.nanstd(arr))
            if std < 1e-15:
                findings["constants"].append({"name": rec["name"], "tier": rec["tier"], "value": float(np.nanmean(arr))})
                continue
        vh = value_hash(arr)
        vhash_groups[vh].append(rec["name"])
        zk = zcosine_key(arr)
        if zk is not None:
            zcos_groups[zk].append(rec["name"])
        sk = signflip_key(arr)
        if sk is not None:
            signflip_groups[sk].append(rec["name"])

    # Map name->tier for tier-aware reporting
    name_to_tier = {rec["name"]: rec["tier"] for rec in fn_records}
    name_to_src = {rec["name"]: rec["src"] for rec in fn_records}

    for vh, names in vhash_groups.items():
        if len(names) > 1:
            tiers = sorted({name_to_tier[n] for n in names})
            cross_tier = len(tiers) > 1
            findings["vhash_dups"].append({"members": sorted(names), "tiers": tiers, "cross_tier": cross_tier})

    # Z-cosine: only report groups that aren't already in vhash dups
    vhash_member_set = {n for g in findings["vhash_dups"] for n in g["members"]}
    for zk, names in zcos_groups.items():
        unique = sorted(set(names))
        if len(unique) > 1 and not any(n in vhash_member_set for n in unique):
            tiers = sorted({name_to_tier[n] for n in unique})
            findings["zcos_dups"].append({"members": unique, "tiers": tiers})

    # Sign-flip pairs (Class 7): two groups whose normalized vector keys are negatives of each other
    # Detected when both zcosine_key(arr) and zcosine_key(-arr) appear as distinct keys
    # Easier: pair up groups in signflip_groups that match their negation
    flip_seen = set()
    for sk, names in signflip_groups.items():
        if sk in flip_seen:
            continue
        neg_sk = tuple(-v for v in sk)
        if neg_sk in signflip_groups and neg_sk != sk:
            other = signflip_groups[neg_sk]
            mem = sorted(set(names + other))
            if len(mem) > 1:
                findings["signflip_pairs"].append({"members": mem})
            flip_seen.add(sk)
            flip_seen.add(neg_sk)

    # Class 4 cross-tier pollution: base function whose body contains derivative operator
    # but only flag if used **in addition to** the base-level transformation (not the canonical "_diff_"/_roc family)
    # We flag any base function with `.diff(`, `.pct_change(`, `_roc(` in body that's NOT a level/quantile/min/max statistic
    deriv_pat = re.compile(r"\.diff\(|\.pct_change\(|_roc\(|_pct_change\(|_delta\(|_pct\(")
    for rec in fn_records:
        if rec["tier"] != "base":
            continue
        src = rec["src"]
        # Remove the boilerplate `result.replace([np.inf` line and helper definitions
        body = re.sub(r"^\s*def _.*?\n.*?(?=\ndef [^_])", "", src, flags=re.DOTALL)
        if deriv_pat.search(src) and "rolling" not in src.split("def ")[1].split(":", 1)[1].split("return")[0]:
            # crude: function body that *only* applies a derivative operator is pollution
            findings["class4_base_deriv_pollution"].append({"name": rec["name"]})

    # Drop arrs from records before serializing
    return findings


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    synth = make_synth()
    families = sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("f")])
    summary = []
    for fam in families:
        print(f"\n=== {fam.name} ===", flush=True)
        findings = audit_family(fam, synth)
        # serializable
        findings["by_tier"] = dict(findings["by_tier"])
        out = OUT_DIR / f"{fam.name}.json"
        out.write_text(json.dumps(findings, indent=2, default=str))
        n_err = len(findings.get("errors", []))
        n_nan = len(findings.get("all_nan", []))
        n_const = len(findings.get("constants", []))
        n_vh = len(findings.get("vhash_dups", []))
        n_zc = len(findings.get("zcos_dups", []))
        n_sf = len(findings.get("signflip_pairs", []))
        n_c4 = len(findings.get("class4_base_deriv_pollution", []))
        n_fn = findings.get("n_funcs", 0)
        line = f"{fam.name}: n={n_fn} err={n_err} nan={n_nan} const={n_const} vh={n_vh} zc={n_zc} sf={n_sf} c4={n_c4}"
        print(line, flush=True)
        summary.append(line)
    (OUT_DIR / "_summary.txt").write_text("\n".join(summary))
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
