import ast
import hashlib
import importlib.util
import inspect
import json
import math
import os
import re
import sys
import traceback
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
N = 1800
WARMUP = 900


def series_inputs():
    rng = np.random.default_rng(42)
    idx = pd.RangeIndex(N)
    t = np.arange(N, dtype=float)
    base = 80 + 0.03 * t + rng.normal(0, 0.7, N).cumsum()
    close = pd.Series(np.maximum(base, 2), index=idx)
    open_ = close.shift(1).fillna(close.iloc[0]) * (1 + rng.normal(0, 0.006, N))
    high = pd.concat([open_, close], axis=1).max(axis=1) * (1 + rng.uniform(0, 0.018, N))
    low = pd.concat([open_, close], axis=1).min(axis=1) * (1 - rng.uniform(0, 0.018, N))
    volume = pd.Series(1_000_000 * (1 + 0.25 * np.sin(t / 35) + rng.lognormal(0, 0.25, N)), index=idx)

    data = {
        "open": open_,
        "high": high,
        "low": low,
        "close": close,
        "volume": volume,
    }

    names = [
        "revenue", "netinc", "ncfo", "fcf", "debt", "equity", "assets", "liabilities",
        "opinc", "ebit", "ebitda", "gp", "cor", "opex", "sgna", "rnd", "capex",
        "cashneq", "cashnequsd", "workingcapital", "sharesbas", "shareswa",
        "shareswadil", "marketcap", "ev", "shortinterest", "float_shares",
        "insider_sell_value", "insider_buy_value", "instownpct", "instown_pct",
        "institutionalpct", "put_iv", "call_iv", "put_volume", "call_volume",
        "put_open_interest", "call_open_interest", "borrow_fee", "utilization",
    ]
    for i, name in enumerate(names):
        drift = (i % 7 - 3) * 0.00008
        raw = 50 + (0.02 + drift) * t + rng.normal(0, 0.45 + (i % 5) * 0.05, N).cumsum()
        s = pd.Series(np.maximum(raw, 0.1), index=idx)
        if name in {"netinc", "opinc", "fcf", "ncfo", "capex"}:
            s = pd.Series(raw, index=idx)
        if name == "marketcap":
            s = close * 100_000_000
        if name == "ev":
            s = close * 105_000_000
        if "shares" in name or name in {"float_shares"}:
            s = pd.Series(100_000_000 + rng.normal(0, 30_000, N).cumsum(), index=idx).abs()
        if name in {"put_iv", "call_iv", "borrow_fee", "utilization", "instownpct", "instown_pct", "institutionalpct"}:
            s = pd.Series(np.clip(0.25 + 0.05 * np.sin(t / (20 + i)) + rng.normal(0, 0.02, N), 0.001, 0.95), index=idx)
        data[name] = s
    return data


def normalize_body(fn):
    try:
        src = inspect.getsource(fn)
    except OSError:
        return None
    tree = ast.parse(src)
    node = tree.body[0]
    node.name = "FN"
    node.decorator_list = []
    ast.fix_missing_locations(tree)
    return ast.dump(tree, include_attributes=False)


def value_hash(s):
    arr = np.asarray(pd.Series(s).iloc[WARMUP:], dtype=float)
    if arr.size == 0:
        return None
    arr = np.where(np.isfinite(arr), arr, np.nan)
    if np.all(np.isnan(arr)):
        return "ALL_NAN"
    rounded = np.round(arr, 10)
    return hashlib.sha256(np.nan_to_num(rounded, nan=1.23456789e123).tobytes()).hexdigest()


def is_constant(s):
    arr = np.asarray(pd.Series(s).iloc[WARMUP:], dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size < 50:
        return False, None
    spread = float(np.nanmax(arr) - np.nanmin(arr))
    scale = max(1.0, float(np.nanmedian(np.abs(arr))))
    return spread <= 1e-10 * scale, float(np.nanmedian(arr))


def main():
    sys.path.insert(0, str(ROOT))
    inputs = series_inputs()
    py_files = sorted(p for p in ROOT.glob("*/*.py") if "__pycache__" not in p.parts)
    modules = []
    functions = []
    import_errors = []
    run_errors = []
    constants = []
    all_nan = []
    bad_alignment = []
    body_groups = defaultdict(list)
    value_groups = defaultdict(list)
    lookahead_hits = []
    dropna_hits = []
    scalar_pairs = []

    for path in py_files:
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8", errors="replace")
        if re.search(r"\.shift\(\s*-\d+", text):
            lookahead_hits.append(rel)
        if ".dropna(" in text:
            dropna_hits.append(rel)
        modname = "audit_" + re.sub(r"\W+", "_", rel)
        try:
            spec = importlib.util.spec_from_file_location(modname, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            modules.append(rel)
        except Exception as exc:
            import_errors.append({"file": rel, "error": repr(exc), "trace": traceback.format_exc(limit=2)})
            continue

        for name, obj in list(vars(mod).items()):
            if not (callable(obj) and re.match(r"^f\d+_", name)):
                continue
            sig = inspect.signature(obj)
            args = {}
            for param in sig.parameters.values():
                if param.name in inputs:
                    args[param.name] = inputs[param.name]
                elif param.default is inspect._empty:
                    args[param.name] = pd.Series(np.nan, index=pd.RangeIndex(N))
            rec = {"file": rel, "name": name, "inputs": list(sig.parameters)}
            functions.append(rec)

            body = normalize_body(obj)
            if body:
                body_groups[hashlib.sha256(body.encode()).hexdigest()].append(rec)
            try:
                out = obj(**args)
                if not isinstance(out, pd.Series):
                    out = pd.Series(out)
                if len(out) != N or not out.index.equals(pd.RangeIndex(N)):
                    bad_alignment.append({**rec, "len": len(out), "index_type": type(out.index).__name__})
                vh = value_hash(out)
                value_groups[vh].append(rec)
                if vh == "ALL_NAN":
                    all_nan.append(rec)
                const, val = is_constant(out)
                if const:
                    constants.append({**rec, "value": val})
                rec["_values"] = np.asarray(out.iloc[WARMUP:], dtype=float)
            except Exception as exc:
                run_errors.append({**rec, "error": repr(exc)})

    body_dups = {k: v for k, v in body_groups.items() if len(v) > 1}
    value_dups = {k: v for k, v in value_groups.items() if k not in (None, "ALL_NAN") and len(v) > 1}

    # Scalar multiple scan within each directory/tier-ish file family to avoid a huge global O(N^2).
    by_dir = defaultdict(list)
    for rec in functions:
        if "_values" in rec:
            by_dir[Path(rec["file"]).parts[0]].append(rec)
    for _, recs in by_dir.items():
        for i in range(len(recs)):
            a = recs[i].get("_values")
            if a is None:
                continue
            for j in range(i + 1, len(recs)):
                b = recs[j].get("_values")
                if b is None:
                    continue
                mask = np.isfinite(a) & np.isfinite(b) & (np.abs(b) > 1e-12)
                if mask.sum() < 200:
                    continue
                aa = a[mask]
                bb = b[mask]
                if np.nanstd(aa) < 1e-12 or np.nanstd(bb) < 1e-12:
                    continue
                ratio = aa / bb
                med = np.nanmedian(ratio)
                if not np.isfinite(med) or abs(med) < 1e-12:
                    continue
                rel_std = np.nanstd(ratio) / max(abs(med), 1e-12)
                if rel_std < 1e-10 and abs(med - 1.0) > 1e-8:
                    scalar_pairs.append({"a": {k: recs[i][k] for k in ("file", "name")}, "b": {k: recs[j][k] for k in ("file", "name")}, "ratio": float(med), "rel_std": float(rel_std)})

    for rec in functions:
        rec.pop("_values", None)

    report = {
        "files": len(py_files),
        "imported_files": len(modules),
        "functions": len(functions),
        "import_errors": import_errors,
        "run_errors": run_errors,
        "bad_alignment": bad_alignment,
        "all_nan": all_nan,
        "constants": constants,
        "body_duplicate_groups": list(body_dups.values()),
        "value_duplicate_groups": list(value_dups.values()),
        "scalar_multiple_pairs": scalar_pairs[:500],
        "scalar_multiple_pair_count": len(scalar_pairs),
        "lookahead_files": lookahead_hits,
        "dropna_files": dropna_hits,
    }
    out_path = ROOT / "audit_report.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items() if k != "scalar_multiple_pairs"}, indent=2))
    print(f"report={out_path}")


if __name__ == "__main__":
    main()
