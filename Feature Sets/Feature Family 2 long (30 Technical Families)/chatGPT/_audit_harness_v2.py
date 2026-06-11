"""
Audit harness v2 — proper z-cosine scan + report.

Improvements over v1:
 - Z-cosine via O(N^2) pairwise dot products (not hash lookup which suffers from
   floating-point quantization edge cases).
 - Reports also include cross-tier vhash/zcos counts.
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
OUT_DIR = ROOT / "_audit_results_v2"
OUT_DIR.mkdir(exist_ok=True)

WARMUP = 600
N = 1500
SEED = 42

ZCOS_THRESHOLD = 1.0 - 1e-10  # near-perfect cosine match (algebraic identity)


def make_synth(seed=SEED, n=N):
    np.random.seed(seed)
    t = pd.Series(np.arange(n, dtype=float))
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


def load_module(path: Path):
    name = path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def discover_files(family_dir: Path):
    files = {}
    for f in sorted(family_dir.glob("*.py")):
        if f.name.startswith("_"):
            continue
        if "base_001_075" in f.name:
            files["base_001_075"] = f
        elif "base_076_150" in f.name:
            files["base_076_150"] = f
        elif "jerk" in f.name:
            files["jerk"] = f
        elif "slope" in f.name:
            files["slope"] = f
    return files


def normalize_post_warmup(y: pd.Series, warmup=WARMUP):
    arr = y.iloc[warmup:].astype(float).to_numpy()
    arr = np.where(np.isfinite(arr), arr, np.nan)
    return arr


def vhash_key(arr):
    finite = np.isfinite(arr)
    if finite.sum() == 0:
        return ("nan",)
    rounded = np.where(finite, np.round(arr.astype(np.float64), 10), np.nan)
    return (int(finite.sum()), float(np.nansum(rounded)), float(np.nanstd(rounded)),
            float(np.nanmin(rounded)), float(np.nanmax(rounded)))


def make_zvec(arr):
    """Return (z-normalized vector, raw vector) restricted to indices finite in `arr`."""
    finite = np.isfinite(arr)
    if finite.sum() < 50:
        return None, None
    a = arr.astype(np.float64).copy()
    a[~finite] = 0.0  # zero out NaN positions so dot products skip them
    mask = finite.astype(np.float64)
    return a, mask


def audit_family(family_dir: Path, synth):
    files = discover_files(family_dir)
    family_name = family_dir.name

    fn_records = []
    for tier_key, fpath in files.items():
        try:
            mod = load_module(fpath)
        except Exception as e:
            return {"family": family_name, "load_error": f"{tier_key}: {e}"}
        if not hasattr(mod, "REGISTRY"):
            continue
        reg = mod.REGISTRY
        for fn_name, meta in reg.items():
            fn = meta["func"]
            inputs = meta["inputs"]
            tier = "base" if tier_key.startswith("base") else tier_key
            rec = {
                "name": fn_name,
                "tier": tier,
                "chunk": tier_key,
                "file": fpath.name,
                "inputs": list(inputs),
                "src": inspect.getsource(fn),
            }
            try:
                args = {k: synth[k] for k in inputs}
                y = fn(**args)
                if not isinstance(y, pd.Series):
                    rec["error"] = f"non-series: {type(y).__name__}"
                else:
                    arr = normalize_post_warmup(y)
                    rec["arr"] = arr
            except Exception as e:
                rec["error"] = f"{type(e).__name__}: {e}"
            fn_records.append(rec)

    findings = {
        "family": family_name,
        "n_funcs": len(fn_records),
        "by_tier": defaultdict(int),
        "errors": [],
        "all_nan": [],
        "constants": [],
        "vhash_dups": [],
        "zcos_dups": [],
        "signflip_pairs": [],
        "class4_candidates": [],
    }

    # First pass: errors, all-NaN, constants
    valid_recs = []
    for rec in fn_records:
        findings["by_tier"][rec["tier"]] += 1
        if "error" in rec:
            findings["errors"].append({"name": rec["name"], "tier": rec["tier"], "error": rec["error"]})
            continue
        arr = rec["arr"]
        finite = np.isfinite(arr)
        if finite.sum() == 0:
            findings["all_nan"].append({"name": rec["name"], "tier": rec["tier"]})
            continue
        std = float(np.nanstd(arr))
        if std < 1e-15:
            findings["constants"].append({"name": rec["name"], "tier": rec["tier"], "value": float(np.nanmean(arr))})
            continue
        valid_recs.append(rec)

    # Vhash dups
    vhash_groups = defaultdict(list)
    for rec in valid_recs:
        vhash_groups[vhash_key(rec["arr"])].append(rec)
    vhash_member_set = set()
    for vh, recs in vhash_groups.items():
        if len(recs) > 1:
            names = sorted(r["name"] for r in recs)
            tiers = sorted({r["tier"] for r in recs})
            findings["vhash_dups"].append({"members": names, "tiers": tiers, "cross_tier": len(tiers) > 1})
            for r in recs:
                vhash_member_set.add(r["name"])

    # Z-cosine dups: build z-vectors then pairwise scan
    zrecs = []
    for rec in valid_recs:
        if rec["name"] in vhash_member_set:
            continue
        arr = rec["arr"]
        finite = np.isfinite(arr)
        if finite.sum() < 100:
            continue
        a = arr.copy()
        a[~finite] = 0.0
        # center on the finite-valued samples
        mean = arr[finite].mean()
        a[finite] -= mean
        norm = np.linalg.norm(a)
        if norm < 1e-15:
            continue
        a /= norm
        zrecs.append({"name": rec["name"], "tier": rec["tier"], "z": a, "finite": finite})

    # O(N^2) pairwise scan — N around ~430 per family, so manageable
    parent = {i: i for i in range(len(zrecs))}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj

    Z = np.stack([r["z"] for r in zrecs]) if zrecs else np.zeros((0, 1))
    if len(zrecs) > 0:
        sim = Z @ Z.T
        # cosine in {-1, +1}; for sign-flip detection
        for i in range(len(zrecs)):
            for j in range(i + 1, len(zrecs)):
                s = sim[i, j]
                if s > ZCOS_THRESHOLD:
                    union(i, j)

    # Aggregate z-cos groups
    groups = defaultdict(list)
    for i in range(len(zrecs)):
        groups[find(i)].append(i)
    for g, idxs in groups.items():
        if len(idxs) > 1:
            members = sorted(zrecs[i]["name"] for i in idxs)
            tiers = sorted({zrecs[i]["tier"] for i in idxs})
            findings["zcos_dups"].append({"members": members, "tiers": tiers, "cross_tier": len(tiers) > 1})

    # Sign-flip detection: pair i,j where sim[i,j] < -ZCOS_THRESHOLD
    if len(zrecs) > 0:
        flip_pairs = []
        for i in range(len(zrecs)):
            for j in range(i + 1, len(zrecs)):
                if sim[i, j] < -ZCOS_THRESHOLD:
                    flip_pairs.append(sorted([zrecs[i]["name"], zrecs[j]["name"]]))
        # dedup
        seen = set()
        for pair in flip_pairs:
            key = tuple(pair)
            if key not in seen:
                seen.add(key)
                findings["signflip_pairs"].append({"members": list(pair)})

    # Class 4 candidates: any base function whose name contains "_delta_", "_pctdelta_", "_vol_adj_delta_"
    # (these recipes are derivative operators on the family's signal)
    deriv_suffixes = ("_delta_", "_pctdelta_", "_vol_adj_delta_")
    for rec in fn_records:
        if rec["tier"] != "base":
            continue
        name_low = rec["name"].lower()
        for suf in deriv_suffixes:
            if suf in name_low:
                findings["class4_candidates"].append({"name": rec["name"], "recipe": suf.strip("_")})
                break

    findings["by_tier"] = dict(findings["by_tier"])
    return findings


def main():
    synth = make_synth()
    families = sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("f")])
    summary = []
    for fam in families:
        print(f"\n=== {fam.name} ===", flush=True)
        findings = audit_family(fam, synth)
        out = OUT_DIR / f"{fam.name}.json"
        out.write_text(json.dumps(findings, indent=2, default=str))
        n_err = len(findings.get("errors", []))
        n_nan = len(findings.get("all_nan", []))
        n_const = len(findings.get("constants", []))
        n_vh = len(findings.get("vhash_dups", []))
        n_zc = len(findings.get("zcos_dups", []))
        n_sf = len(findings.get("signflip_pairs", []))
        n_c4 = len(findings.get("class4_candidates", []))
        n_fn = findings.get("n_funcs", 0)
        line = f"{fam.name}: n={n_fn} err={n_err} nan={n_nan} const={n_const} vh={n_vh} zc={n_zc} sf={n_sf} c4_cand={n_c4}"
        print(line, flush=True)
        summary.append(line)
    (OUT_DIR / "_summary.txt").write_text("\n".join(summary))
    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
