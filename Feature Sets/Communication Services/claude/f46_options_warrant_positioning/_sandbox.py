"""Local sandbox: pooled real-data corr tester for candidate f46 replacements.
Deleted by exact filename when done. Writes nothing outside this folder.
"""
import sys, inspect
sys.path.insert(0, r"C:\Communication Services\_build")
import numpy as np, pandas as pd
import realdedup as rd

P = rd.panels()


def pooled(funcs):
    parts = []
    for tk, df in P.items():
        cols = {}
        for fn in funcs:
            ps = [p.name for p in inspect.signature(fn).parameters.values()]
            if any(p not in df.columns for p in ps):
                continue
            try:
                cols[fn.__name__] = np.asarray(fn(*[df[p] for p in ps]), dtype="float64")
            except Exception:
                pass
        if cols:
            parts.append(pd.DataFrame(cols))
    out = pd.concat(parts, ignore_index=True).replace([np.inf, -np.inf], np.nan)
    keep = [c for c in out.columns if out[c].notna().sum() > 200 and out[c].std(skipna=True) > 0]
    return out[keep]


def corr_against(cand_funcs, ref_funcs, thr=0.95, same=False):
    """corr of each cand vs each ref on pooled real data."""
    allf = list({f.__name__: f for f in (cand_funcs + ref_funcs)}.values())
    df = pooled(allf)
    res = []
    cn = [f.__name__ for f in cand_funcs if f.__name__ in df.columns]
    rn = [f.__name__ for f in ref_funcs if f.__name__ in df.columns]
    for a in cn:
        for b in rn:
            if same and b <= a:
                continue
            if a == b:
                continue
            x, y = df[a], df[b]
            m = x.notna() & y.notna()
            if m.sum() < 200:
                continue
            c = x[m].corr(y[m])
            if c is not None and np.isfinite(c) and abs(c) > thr:
                res.append((a, b, round(float(c), 4)))
    res.sort(key=lambda t: -abs(t[2]))
    return res


def survives(cand_funcs):
    df = pooled(cand_funcs)
    return [f.__name__ for f in cand_funcs if f.__name__ not in df.columns]
