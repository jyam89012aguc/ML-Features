import importlib.util
import inspect
import json
import pathlib
import re
import traceback

import numpy as np
import pandas as pd

N = 900
root = pathlib.Path(".")
rng = np.random.default_rng(7)
idx = pd.RangeIndex(N)
t = np.arange(N, dtype=float)
close = pd.Series(50 + rng.normal(0, 0.5, N).cumsum() + 0.02 * t, index=idx).abs() + 1
open_ = close.shift(1).fillna(close.iloc[0])
high = pd.concat([open_, close], axis=1).max(axis=1) * 1.01
low = pd.concat([open_, close], axis=1).min(axis=1) * 0.99
base = {
    "open": open_,
    "open_": open_,
    "high": high,
    "low": low,
    "close": close,
    "volume": pd.Series(1_000_000 + rng.normal(0, 20_000, N).cumsum(), index=idx).abs(),
}
for name in [
    "revenue", "netinc", "ncfo", "fcf", "debt", "equity", "assets", "liabilities",
    "opinc", "ebit", "ebitda", "gp", "cor", "opex", "sgna", "rnd", "capex",
    "cashneq", "cashnequsd", "workingcapital", "sharesbas", "shareswa",
    "shareswadil", "marketcap", "ev", "shortinterest", "float_shares",
    "insider_sell_value", "insider_buy_value", "inst_holders", "inst_units",
    "inst_value", "instownpct", "instown_pct", "institutionalpct", "put_iv",
    "call_iv", "put_volume", "call_volume", "put_open_interest",
    "call_open_interest", "borrow_fee", "utilization", "receivables", "inventory",
]:
    vals = 100 + rng.normal(0, 0.7, N).cumsum() + 0.01 * t
    base[name] = pd.Series(vals, index=idx)

errors = []
bad_alignment = []
all_nan = []
checked = 0

for path in sorted(root.glob("*/*.py")):
    spec = importlib.util.spec_from_file_location("smoke_" + re.sub(r"\W+", "_", str(path)), path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:
        errors.append({"file": str(path), "name": "<import>", "error": repr(exc)})
        continue
    funcs = [(n, o) for n, o in vars(mod).items() if callable(o) and re.match(r"^f\d+_", n)]
    # Exercise beginning, middle, and end of each generated file.
    picks = funcs[:3] + funcs[len(funcs)//2:len(funcs)//2+3] + funcs[-3:]
    seen = set()
    for name, fn in picks:
        if name in seen:
            continue
        seen.add(name)
        sig = inspect.signature(fn)
        kwargs = {}
        for param in sig.parameters:
            kwargs[param] = base.get(param, pd.Series(np.nan, index=idx))
        try:
            out = fn(**kwargs)
            checked += 1
            if not isinstance(out, pd.Series):
                out = pd.Series(out)
            if len(out) != N:
                bad_alignment.append({"file": str(path), "name": name, "len": len(out)})
            if out.iloc[N//2:].isna().all():
                all_nan.append({"file": str(path), "name": name})
        except Exception as exc:
            errors.append({"file": str(path), "name": name, "error": repr(exc), "trace": traceback.format_exc(limit=1)})

report = {
    "files": len(list(root.glob("*/*.py"))),
    "checked_functions": checked,
    "errors": errors,
    "bad_alignment": bad_alignment,
    "all_nan": all_nan,
}
(root / "smoke_audit_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items()}, indent=2))
