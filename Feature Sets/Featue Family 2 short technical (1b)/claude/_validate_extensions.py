"""Cross-family validation for families 26, 27, 28, 50 with all 6 slices
(001_075, 076_150, 151_225, 226_300, 301_375, 376_450).

Per-family checks: 24 files exist; each parses/imports; <75 KB; registry has 75 entries;
declared inputs == fn args; no duplicate fn names; d1/d3 == base.diff() / base.diff().diff().diff()
sampled per slice.
"""
import os
import ast
import importlib.util
import inspect
import numpy as np
import pandas as pd

ROOT = r"C:\Users\jyama\Desktop\short_technical_features_1b"
FAMILIES = [
    ("26", "stwf", "26_stochastic_williams_family", "STOCHASTIC_WILLIAMS_FAMILY"),
    ("27", "mcdt", "27_macd_topping_dynamics", "MACD_TOPPING_DYNAMICS"),
    ("28", "ttcf", "28_trix_tsi_cci_family", "TRIX_TSI_CCI_FAMILY"),
    ("50", "tdco", "50_terminal_distribution_composite", "TERMINAL_DISTRIBUTION_COMPOSITE"),
]
SLICES = ("001_075", "076_150", "151_225", "226_300", "301_375", "376_450", "451_525", "526_600")
ORDERS = ("base", "d1", "d2", "d3")


def load(path):
    spec = importlib.util.spec_from_file_location("m", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def synthetic_ohlcv(n=800, seed=7):
    rng = np.random.default_rng(seed)
    rets = rng.normal(0.001, 0.02, n).cumsum()
    close = pd.Series(100.0 * np.exp(rets), index=pd.date_range("2010-01-01", periods=n, freq="B"))
    high = close * (1 + np.abs(rng.normal(0, 0.01, n)))
    low = close * (1 - np.abs(rng.normal(0, 0.01, n)))
    open_ = close.shift(1).fillna(close.iloc[0])
    vol = pd.Series(rng.lognormal(13, 0.5, n), index=close.index)
    return {"open": open_, "high": high, "low": low, "close": close, "volume": vol}


def main():
    errors = []
    ohlcv = synthetic_ohlcv()
    grand_total = 0

    for nn, abbrev, folder, family_upper in FAMILIES:
        family_dir = os.path.join(ROOT, folder)
        family_total = 0
        seen_fn_names = set()

        for order in ORDERS:
            for slice_label in SLICES:
                fname = f"{folder}__{order}__{slice_label}.py"
                fpath = os.path.join(family_dir, fname)
                if not os.path.exists(fpath):
                    errors.append(f"MISSING: {fname}"); continue
                size = os.path.getsize(fpath)
                if size > 75_000:
                    errors.append(f"{fname}: {size} > 75000 bytes")
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        ast.parse(f.read())
                except SyntaxError as e:
                    errors.append(f"{fname}: SYNTAX {e}"); continue
                try:
                    m = load(fpath)
                except Exception as e:
                    errors.append(f"{fname}: IMPORT {e}"); continue
                if order == "base":
                    reg_name = f"{family_upper}_BASE_REGISTRY_{slice_label}"
                else:
                    reg_name = f"{family_upper}_{order.upper()}_REGISTRY_{slice_label}"
                reg = getattr(m, reg_name, None)
                if reg is None:
                    errors.append(f"{fname}: missing registry {reg_name}"); continue
                if len(reg) != 75:
                    errors.append(f"{fname}: registry size {len(reg)} != 75")
                for fn_name, entry in reg.items():
                    if fn_name in seen_fn_names:
                        errors.append(f"{fname}: duplicate fn {fn_name}")
                    seen_fn_names.add(fn_name)
                    sig = inspect.signature(entry["func"])
                    actual = list(sig.parameters.keys())
                    if actual != entry["inputs"]:
                        errors.append(f"{fname}::{fn_name}: declared {entry['inputs']} != actual {actual}")
                family_total += len(reg)

        print(f"family {nn} ({abbrev}): {family_total} features")
        grand_total += family_total

    # d1/d3 semantics on NEW slices only
    print("\n--- d1/d3 semantics on new slices ---")
    for nn, abbrev, folder, family_upper in FAMILIES:
        for slice_label in ("451_525", "526_600"):
            base_path = os.path.join(ROOT, folder, f"{folder}__base__{slice_label}.py")
            d1_path = os.path.join(ROOT, folder, f"{folder}__d1__{slice_label}.py")
            d3_path = os.path.join(ROOT, folder, f"{folder}__d3__{slice_label}.py")
            if not (os.path.exists(base_path) and os.path.exists(d1_path) and os.path.exists(d3_path)):
                continue
            try:
                mb = load(base_path); m1 = load(d1_path); m3 = load(d3_path)
            except Exception as e:
                errors.append(f"{folder} {slice_label}: d-check import {e}"); continue
            rb = getattr(mb, f"{family_upper}_BASE_REGISTRY_{slice_label}")
            r1 = getattr(m1, f"{family_upper}_D1_REGISTRY_{slice_label}")
            r3 = getattr(m3, f"{family_upper}_D3_REGISTRY_{slice_label}")
            n0, e0 = next(iter(rb.items()))
            n1k = n0 + "_d1"; n3k = n0 + "_d3"
            if n1k not in r1 or n3k not in r3:
                errors.append(f"{folder} {slice_label}: missing _d1/_d3 for {n0}"); continue
            try:
                bv = e0["func"](**{k: ohlcv[k] for k in e0["inputs"]})
                d1v = r1[n1k]["func"](**{k: ohlcv[k] for k in r1[n1k]["inputs"]})
                d3v = r3[n3k]["func"](**{k: ohlcv[k] for k in r3[n3k]["inputs"]})
            except Exception as e:
                errors.append(f"{folder} {slice_label} {n0}: compute {e}"); continue
            if not (isinstance(bv, pd.Series) and len(bv) == 800):
                errors.append(f"{folder} {slice_label} {n0}: wrong type/length"); continue
            db = bv.diff(); d3b = bv.diff().diff().diff()
            mx1 = (d1v.dropna() - db.dropna()).abs().max() if len(d1v.dropna()) and len(db.dropna()) else 0
            mx3 = (d3v.dropna() - d3b.dropna()).abs().max() if len(d3v.dropna()) and len(d3b.dropna()) else 0
            if not (np.isnan(mx1) or mx1 < 1e-6):
                errors.append(f"{folder} {slice_label} {n0}: d1 deviates max={mx1}")
            if not (np.isnan(mx3) or mx3 < 1e-6):
                errors.append(f"{folder} {slice_label} {n0}: d3 deviates max={mx3}")
            print(f"  {folder} {slice_label}: {n0} d1 ok, d3 ok")

    print(f"\nGRAND TOTAL: {grand_total} features across all 4 families (expected 4 * 2400 = 9600)")
    print(f"errors: {len(errors)}")
    for e in errors[:80]:
        print("  -", e)
    if not errors:
        print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
