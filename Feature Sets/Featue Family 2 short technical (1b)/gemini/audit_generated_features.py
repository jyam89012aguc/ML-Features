import argparse
import ast
import hashlib
import importlib.util
import inspect
import json
import math
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
N_ROWS = 1500
WARMUP = 500


def discover_files(folder_filter=None):
    files = sorted(p for p in ROOT.rglob("*.py") if p.name != Path(__file__).name)
    if folder_filter:
        wanted = set(folder_filter)
        files = [p for p in files if p.relative_to(ROOT).parts[0] in wanted]
    return files


def ast_functions(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    tree = ast.parse(text, filename=str(path))
    funcs = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            funcs.append(node.name)
    return funcs


def load_module(path, ordinal):
    mod_name = f"_audit_mod_{ordinal}_{hashlib.sha1(str(path).encode()).hexdigest()[:10]}"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def make_inputs(names):
    rng = np.random.default_rng(12345)
    idx = pd.date_range("2015-01-01", periods=N_ROWS, freq="B")
    base_ret = rng.normal(0.0003, 0.018, N_ROWS)
    close = pd.Series(100.0 * np.exp(np.cumsum(base_ret)), index=idx)
    spread = pd.Series(rng.uniform(0.002, 0.035, N_ROWS), index=idx)
    high = close * (1.0 + spread)
    low = close * (1.0 - spread * rng.uniform(0.7, 1.3, N_ROWS))
    open_ = close.shift(1).fillna(close.iloc[0]) * (1.0 + rng.normal(0, 0.006, N_ROWS))
    volume = pd.Series(rng.lognormal(14, 0.45, N_ROWS), index=idx)

    data = {
        "open": open_,
        "high": high,
        "low": low,
        "close": close,
        "volume": volume,
    }
    for i, name in enumerate(sorted(names)):
        if name in data:
            continue
        lname = name.lower()
        local = np.random.default_rng(2000 + i)
        if "return" in lname or lname in {"ret", "returns"}:
            data[name] = pd.Series(local.normal(0.0002, 0.02, N_ROWS), index=idx)
        elif "flag" in lname or lname.startswith("is_"):
            data[name] = pd.Series(local.random(N_ROWS) > 0.8, index=idx).astype(float)
        else:
            drift = local.normal(0.00015, 0.01, N_ROWS)
            level = 50.0 + (i % 17) * 7.0
            s = pd.Series(level * np.exp(np.cumsum(drift)), index=idx)
            if any(k in lname for k in ("debt", "liab", "capex", "intexp", "cor", "opex", "sgna")):
                s = s * 0.35
            if any(k in lname for k in ("netinc", "fcf", "ncfo", "opinc", "ebit")):
                sign = np.where(np.sin(np.linspace(0, 10, N_ROWS) + i) > -0.75, 1.0, -1.0)
                s = s * 0.12 * sign
            data[name] = s
    return data


def finite_vector(value):
    if isinstance(value, pd.DataFrame):
        if value.shape[1] == 1:
            value = value.iloc[:, 0]
        else:
            return None, "dataframe_output"
    if not isinstance(value, pd.Series):
        try:
            value = pd.Series(value)
        except Exception:
            return None, "non_series_output"
    arr = pd.to_numeric(value, errors="coerce").to_numpy(dtype=float)
    if arr.shape[0] != N_ROWS:
        return arr, "misaligned_length"
    return arr, None


def output_hash(arr):
    sub = arr[WARMUP:]
    rounded = np.round(np.where(np.isfinite(sub), sub, np.nan), 10)
    return hashlib.sha256(rounded.tobytes()).hexdigest()


def normalized(arr):
    sub = arr[WARMUP:]
    mask = np.isfinite(sub)
    if mask.sum() < 50:
        return None
    x = sub[mask]
    sd = x.std()
    if not np.isfinite(sd) or sd < 1e-12:
        return None
    z = (x - x.mean()) / sd
    return mask, z


def ratio_stats(a, b):
    aa = a[WARMUP:]
    bb = b[WARMUP:]
    mask = np.isfinite(aa) & np.isfinite(bb) & (np.abs(bb) > 1e-12)
    if mask.sum() < 50:
        return None
    r = aa[mask] / bb[mask]
    m = float(np.nanmean(r))
    sd = float(np.nanstd(r))
    rel = sd / max(abs(m), 1e-12)
    return m, sd, rel, int(mask.sum())


def audit(folder_filter=None, dynamic=True, scalar_scan=True, out_path=None):
    files = discover_files(folder_filter)
    parse_errors = []
    import_errors = []
    functions = []
    all_inputs = set()

    for i, path in enumerate(files):
        rel = str(path.relative_to(ROOT))
        try:
            fn_names = ast_functions(path)
        except Exception as exc:
            parse_errors.append({"file": rel, "error": repr(exc)})
            continue
        try:
            module = load_module(path, i)
        except Exception as exc:
            import_errors.append({"file": rel, "error": repr(exc)})
            continue
        for name in fn_names:
            fn = getattr(module, name, None)
            if not callable(fn):
                continue
            try:
                sig = inspect.signature(fn)
                params = list(sig.parameters)
            except Exception as exc:
                functions.append({"file": rel, "name": name, "signature_error": repr(exc)})
                continue
            all_inputs.update(params)
            functions.append({"file": rel, "folder": rel.split("\\")[0], "name": name, "fn": fn, "inputs": params})

    if not dynamic:
        return {
            "files": len(files),
            "parse_errors": parse_errors,
            "import_errors": import_errors,
            "functions_discovered": len(functions),
            "inputs": sorted(all_inputs),
        }

    data = make_inputs(all_inputs)
    errors = []
    all_nan = []
    constants = []
    shape_issues = []
    outputs_by_folder = defaultdict(list)
    timings = []

    for n_done, item in enumerate(functions, 1):
        if "fn" not in item:
            continue
        args = {p: data[p] for p in item["inputs"] if p in data}
        label = f"{item['file']}::{item['name']}"
        t0 = time.perf_counter()
        try:
            value = item["fn"](**args)
            elapsed = time.perf_counter() - t0
            arr, issue = finite_vector(value)
        except Exception as exc:
            elapsed = time.perf_counter() - t0
            errors.append({"feature": label, "error": repr(exc)})
            timings.append((elapsed, label))
            continue
        timings.append((elapsed, label))
        if issue:
            shape_issues.append({"feature": label, "issue": issue, "length": None if arr is None else len(arr)})
            continue
        sub = arr[WARMUP:]
        finite = np.isfinite(sub)
        if finite.sum() == 0:
            all_nan.append(label)
            continue
        sd = float(np.nanstd(sub[finite]))
        if sd < 1e-12:
            constants.append({"feature": label, "value": float(np.nanmean(sub[finite]))})
        outputs_by_folder[item["folder"]].append((label, arr, output_hash(arr)))
        if out_path and n_done % 1000 == 0:
            partial = {
                "files": len(files),
                "functions_discovered": len(functions),
                "runtime_errors": errors,
                "shape_issues": shape_issues,
                "all_nan": all_nan,
                "constants": constants,
                "slowest": [
                    {"seconds": round(sec, 4), "feature": label}
                    for sec, label in sorted(timings, reverse=True)[:20]
                ],
                "partial": True,
                "functions_attempted": n_done,
            }
            Path(out_path).write_text(json.dumps(partial, indent=2), encoding="utf-8")

    dup_groups = []
    scalar_mult = []
    for folder, rows in outputs_by_folder.items():
        by_hash = defaultdict(list)
        for label, arr, h in rows:
            by_hash[h].append(label)
        for labels in by_hash.values():
            if len(labels) > 1:
                dup_groups.append({"folder": folder, "features": labels})

        if not scalar_scan:
            continue
        # Scalar-multiple scan within each folder. Use exact z-correlation on common finite rows.
        vectors = []
        for label, arr, h in rows:
            n = normalized(arr)
            if n is not None:
                vectors.append((label, arr, n))
        for i in range(len(vectors)):
            li, ai, (mi, zi) = vectors[i]
            for j in range(i + 1, len(vectors)):
                lj, aj, (mj, zj) = vectors[j]
                common = mi & mj
                if common.sum() < 100:
                    continue
                xi = ai[WARMUP:][common]
                xj = aj[WARMUP:][common]
                xi = (xi - xi.mean()) / xi.std()
                xj = (xj - xj.mean()) / xj.std()
                corr = float(np.dot(xi, xj) / len(xi))
                if abs(corr) > 0.999999999:
                    rs = ratio_stats(ai, aj)
                    if rs and rs[2] < 1e-10 and not math.isclose(abs(rs[0]), 1.0, rel_tol=1e-10, abs_tol=1e-10):
                        scalar_mult.append({
                            "folder": folder,
                            "a": li,
                            "b": lj,
                            "ratio_mean": rs[0],
                            "ratio_std_rel": rs[2],
                            "n": rs[3],
                        })

    summary = {
        "files": len(files),
        "parse_errors": parse_errors,
        "import_errors": import_errors,
        "functions_discovered": len(functions),
        "inputs": sorted(all_inputs),
        "runtime_errors": errors,
        "shape_issues": shape_issues,
        "all_nan": all_nan,
        "constants": constants,
        "duplicate_groups": dup_groups,
        "scalar_multiple_candidates": scalar_mult,
        "slowest": [
            {"seconds": round(sec, 4), "feature": label}
            for sec, label in sorted(timings, reverse=True)[:50]
        ],
    }
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--static-only", action="store_true")
    parser.add_argument("--no-scalar", action="store_true")
    parser.add_argument("--folder", action="append", default=[])
    parser.add_argument("--out", default="AUDIT_GENERATED_FEATURES_REPORT.json")
    args = parser.parse_args()
    started = time.perf_counter()
    out_path = ROOT / args.out
    result = audit(
        folder_filter=args.folder or None,
        dynamic=not args.static_only,
        scalar_scan=not args.no_scalar,
        out_path=out_path,
    )
    result["elapsed_seconds"] = round(time.perf_counter() - started, 3)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({
        "report": str(out_path),
        "elapsed_seconds": result["elapsed_seconds"],
        "files": result["files"],
        "functions": result["functions_discovered"],
        "parse_errors": len(result["parse_errors"]),
        "import_errors": len(result["import_errors"]),
        "runtime_errors": len(result.get("runtime_errors", [])),
        "shape_issues": len(result.get("shape_issues", [])),
        "all_nan": len(result.get("all_nan", [])),
        "constants": len(result.get("constants", [])),
        "duplicate_groups": len(result.get("duplicate_groups", [])),
        "scalar_multiple_candidates": len(result.get("scalar_multiple_candidates", [])),
    }, indent=2))
