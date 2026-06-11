"""Build helper: emit the 2nd (slope) and 3rd (jerk) derivative files for f22.
Fully-expanded defs (no runtime factories). Deleted by exact filename after use.
"""

HEADER = '''import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _dlog(s, k):
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(k).replace(0, np.nan))


# ===== f22 operating-leverage primitives =====
def _f22ol_dol(opinc, revenue, k):
    gr = revenue.pct_change(k)
    go = opinc.pct_change(k)
    return go / gr.replace(0, np.nan)


def _f22ol_dol_ebit(ebit, revenue, k):
    gr = revenue.pct_change(k)
    ge = ebit.pct_change(k)
    return ge / gr.replace(0, np.nan)


def _f22ol_incmargin(opinc, revenue, k):
    do = opinc - opinc.shift(k)
    dr = revenue - revenue.shift(k)
    return do / dr.replace(0, np.nan)


def _f22ol_incgm(gp, revenue, k):
    dg = gp - gp.shift(k)
    dr = revenue - revenue.shift(k)
    return dg / dr.replace(0, np.nan)


def _f22ol_spread_op(opinc, revenue, k):
    return _dlog(opinc, k) - _dlog(revenue, k)


def _f22ol_spread_gp(gp, revenue, k):
    return _dlog(gp, k) - _dlog(revenue, k)


def _f22ol_spread_ebit(ebit, revenue, k):
    return _dlog(ebit, k) - _dlog(revenue, k)


def _f22ol_opexscale(opex, revenue, k):
    r = opex / revenue.replace(0, np.nan)
    return -(r - r.shift(k))


def _f22ol_gpscale(gp, revenue, k):
    r = gp / revenue.replace(0, np.nan)
    return r - r.shift(k)


def _f22ol_fixedabsorb(opinc, opex, k):
    do = opinc - opinc.shift(k)
    dx = opex - opex.shift(k)
    return do / dx.replace(0, np.nan)


def _f22ol_opexelas(opex, revenue, k):
    return _dlog(opex, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpelas(gp, revenue, k):
    return _dlog(gp, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_ebitelas(ebit, revenue, k):
    return _dlog(ebit, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpopxlev(gp, opex, k):
    return _dlog(gp, k) / _dlog(opex, k).replace(0, np.nan)


def _f22ol_flowthru(gp, opinc, k):
    do = opinc - opinc.shift(k)
    dg = gp - gp.shift(k)
    return do / dg.replace(0, np.nan)


def _f22ol_breakeven_rev(opex, gp, revenue, k):
    cm = (gp / revenue.replace(0, np.nan)).rolling(k, min_periods=max(2, k // 2)).mean()
    be = opex / cm.replace(0, np.nan)
    return (revenue - be) / revenue.replace(0, np.nan)


def _f22ol_dolexc(opinc, revenue, k):
    d = _f22ol_dol(opinc, revenue, k) - 1.0
    return np.sign(d) * (d.abs() ** 0.5)


'''

# Each base spec: (tag, params, expr-of-base-series, window). `expr` is python source that
# computes the base series `base` from the parameter Series and window W.
# We diversify across all f22 primitives so derivative families don't collapse.
PRIMS = [
    # tag,            params,                  base_expr (uses W)
    ("dolop",        "opinc, revenue",        "np.tanh(_f22ol_dol(opinc, revenue, {W}) / 5.0)"),
    ("dolebit",      "ebit, revenue",         "np.tanh(_f22ol_dol_ebit(ebit, revenue, {W}) / 5.0)"),
    ("incmop",       "opinc, revenue",        "_f22ol_incmargin(opinc, revenue, {W})"),
    ("incmgp",       "gp, revenue",           "_f22ol_incgm(gp, revenue, {W})"),
    ("sprop",        "opinc, revenue",        "_f22ol_spread_op(opinc, revenue, {W})"),
    ("sprgp",        "gp, revenue",           "_f22ol_spread_gp(gp, revenue, {W})"),
    ("sprebit",      "ebit, revenue",         "_f22ol_spread_ebit(ebit, revenue, {W})"),
    ("opxabs",       "opex, revenue",         "_f22ol_opexscale(opex, revenue, {W})"),
    ("dolampf",      "opinc, revenue",        "(_f22ol_dol(opinc, revenue, 63).abs() > 1.0).astype(float).rolling({W}, min_periods=max(2, {W} // 2)).mean()"),
    ("fixlev",       "opinc, opex",           "np.tanh(_f22ol_fixedabsorb(opinc, opex, {W}) / 3.0)"),
    ("dolexc",       "opinc, revenue",        "_f22ol_dolexc(opinc, revenue, {W})"),
    ("dolopvol",     "opinc, revenue",        "np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0).rolling({W}, min_periods=max(2, {W} // 2)).std()"),
    ("sprdrag",      "gp, opex",              "np.tanh((_dlog(opex, {W}) / _dlog(gp, {W}).replace(0, np.nan) - 1.0) / 2.0)"),
    ("gpopxlev",     "gp, opex",              "np.tanh(_f22ol_gpopxlev(gp, opex, {W}) / 3.0)"),
    ("flowthru",     "gp, opinc",             "np.tanh(_f22ol_flowthru(gp, opinc, {W}) / 3.0)"),
    ("sprlinediv",   "ebit, opinc, revenue",  "(_f22ol_spread_ebit(ebit, revenue, {W}) - _f22ol_spread_op(opinc, revenue, {W}))"),
    ("mosbe",        "opex, gp, revenue",     "_f22ol_breakeven_rev(opex, gp, revenue, {W})"),
    ("opmrg",        "opinc, revenue",        "(opinc / revenue.replace(0, np.nan)).ewm(span=max(5, {W} // 2), min_periods=max(2, {W} // 4)).mean()"),
    ("safetygp",     "gp, opex",              "((gp - opex) / gp.replace(0, np.nan)).ewm(span=max(5, {W} // 2), min_periods=max(2, {W} // 4)).mean()"),
    ("ebitmrg",      "ebit, revenue",         "(ebit / revenue.replace(0, np.nan)).ewm(span=max(5, {W} // 2), min_periods=max(2, {W} // 4)).mean()"),
]

# (window, roc) pairs appropriate to the base window; produce 150 combos.
# We cycle primitives x (window, roc) to get distinct (tag,W,roc) triples.
WIN_ROC = [
    (63, 21), (126, 21), (126, 42), (252, 63), (252, 42), (504, 63), (504, 126),
]


def build(kind):
    # kind: 'slope' (1st derivative) or 'jerk' (2nd derivative)
    assert kind in ("slope", "jerk")
    combos = []
    # ROC is tied to the base window (roc ~ W/3) so the SAME primitive at different windows
    # always uses a different ROC and cannot duplicate.  A small primitive-specific offset
    # (multiples of 7d) then de-aligns economically-adjacent primitives at the SAME window
    # (e.g. incmop vs fixlev), which otherwise co-move on smooth synthetic data.
    def roc_for(W, pi):
        base = max(14, int(round(W / 3.0)))
        off = 7 * (pi % 4)
        roc = base + off
        return min(roc, max(14, W // 2))

    # Slow EMA-of-level primitives only get widely-spaced windows: adjacent mid windows
    # (168/210/252) would smooth into near-identical slopes.  Spiky ratio primitives get
    # the full window grid.
    SLOW = {"opmrg", "safetygp", "ebitmrg", "mosbe"}
    slow_windows = [63, 252, 504]
    fast_windows = [63, 126, 252, 504, 168, 210, 294]
    seen = set()
    for wi, W in enumerate(fast_windows):
        for pi, (tag, params, expr) in enumerate(PRIMS):
            if tag in SLOW and W not in slow_windows:
                continue
            roc = roc_for(W, pi + wi)
            combos.append((tag, params, expr, W, roc))
            seen.add((tag, W))
    # pad to 150 with extra widely-spaced windows on the first (spiky) primitives,
    # never repeating a (tag, window) pair already emitted.
    pad_windows = [378, 336, 441, 315, 462, 588]
    pi = 0
    while len(combos) < 150:
        tag, params, expr = PRIMS[pi % 8]
        for W in pad_windows:
            if (tag, W) not in seen:
                roc = roc_for(W, pi + 1)
                combos.append((tag, params, expr, W, roc))
                seen.add((tag, W))
                break
        pi += 1
    combos = combos[:150]
    assert len(combos) == 150, len(combos)

    body = []
    names = []
    for idx, (tag, params, expr, W, roc) in enumerate(combos, start=1):
        v = "v%03d" % idx
        nm = "f22ol_f22_operating_leverage_%s_%dd_%s_%s_signal" % (tag, W, kind, v)
        names.append(nm)
        be = expr.format(W=W)
        if kind == "slope":
            comment = "# %s base, roc %dd (slope = 1st derivative)" % (tag, roc)
            deriv = "    d = base.diff(%d) / float(%d)\n" % (roc, roc)
        else:
            comment = "# %s base, roc %dd (jerk = 2nd derivative)" % (tag, roc)
            deriv = ("    d1 = base.diff(%d) / float(%d)\n"
                     "    d = d1.diff(%d) / float(%d)\n" % (roc, roc, roc, roc))
        fn = (
            "%s\n"
            "def %s(%s):\n"
            "    base = %s\n"
            "%s"
            "    result = d\n"
            "    return result.replace([np.inf, -np.inf], np.nan)\n"
        ) % (comment, nm, params, be, deriv)
        body.append(fn)

    out = [HEADER]
    out.append("\n".join(body))
    out.append("\n\n_FEATURES = [\n")
    for nm in names:
        out.append("    %s,\n" % nm)
    out.append("]\n\n\n")
    out.append(FOOTER % (kind.upper(),))
    return "".join(out), names


FOOTER = '''def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


F22_OPERATING_LEVERAGE_REGISTRY_%s_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp) * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp) * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _margin(seed, lo, hi, rho=0.995):
        g = np.random.default_rng(seed)
        e = g.normal(0, 0.01, n)
        ar = np.zeros(n)
        for t in range(1, n):
            ar[t] = rho * ar[t - 1] + e[t]
        m = (ar - ar.min()) / (ar.max() - ar.min() + 1e-9)
        return pd.Series(lo + (hi - lo) * m, name=None)

    revenue = _fund(1, base=1.2e8, drift=0.035, vol=0.06).rename("revenue")
    opex = _fund(2, base=7.0e7, drift=0.030, vol=0.05).rename("opex")
    gp = (revenue * _margin(10, 0.34, 0.62)).rename("gp")
    opinc = (revenue * _margin(11, -0.16, 0.26)).rename("opinc")
    ebit = (revenue * _margin(12, -0.05, 0.27)).rename("ebit")

    cols = {"closeadj": closeadj, "close": close, "open": openp, "high": high,
            "low": low, "volume": volume, "revenue": revenue, "opex": opex,
            "gp": gp, "opinc": opinc, "ebit": ebit}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume", "revenue", "revenueusd",
             "deferredrev", "gp", "grossmargin", "opinc", "opex", "sgna", "cor", "rnd",
             "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc", "netinccmn", "netmargin",
             "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt",
             "ncfbus", "capex", "depamor", "sharesbas", "shareswa", "shareswadil", "assets",
             "assetsc", "tangibles", "intangibles", "ppnenet", "investments", "inventory",
             "receivables", "payables", "equity", "retearn", "workingcapital", "debt", "debtc",
             "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio", "roic", "roe",
             "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps",
             "de", "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis", "marketcap", "ev",
             "evebit", "evebitda", "pe", "pb", "ps", "shrholders", "shrvalue", "shrunits",
             "totalvalue", "percentoftotal", "fndholders", "undholders", "prfholders",
             "dbtholders", "putholders", "putvalue", "cllholders", "cllvalue", "wntholders",
             "wntvalue", "dbtvalue"}
    FUND = {"revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
            "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
            "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
            "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
            "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
            "investments", "inventory", "receivables", "payables", "equity", "retearn",
            "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
            "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
            "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
            "payoutratio", "prefdivis"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        inp = meta["inputs"]
        assert set(inp) <= ALLOW, "%%s inputs not in allowlist: %%s" %% (name, inp)
        assert len(set(inp) & FUND) >= 1, "%%s has no fundamental column" %% name
        fn = meta["func"]
        args = [cols[c] for c in inp]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%%s nunique=%%d" %% (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%%d/%%d" %% (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %%s vs %%s = %%.4f" %% (ni, nj, c)

    print("OK __FNAME__: %%d features pass" %% n_features)
'''


if __name__ == "__main__":
    for kind, fname, token in [
        ("slope", "f22_operating_leverage_2nd_derivatives_001_150_claude.py", "SLOPE"),
        ("jerk", "f22_operating_leverage_3rd_derivatives_001_150_claude.py", "JERK"),
    ]:
        src, names = build(kind)
        src = src.replace("__FNAME__", fname[:-3])
        with open(fname, "w") as f:
            f.write(src)
        print("wrote", fname, len(names), "features", len(src), "bytes")
