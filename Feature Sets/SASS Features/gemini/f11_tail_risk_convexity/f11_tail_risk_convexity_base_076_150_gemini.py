# f11_tail_risk_convexity — REAL indicator logic (base 076..150)
# Second half of the tail-risk & convexity family. Emphasizes transformed facets:
# z-scores of VaR/CVaR/tail-ratio, slope/delta of tail measures, short-vs-long
# tail spreads (e.g. 21d vs 252d VaR), regime/threshold distance, and interactions
# with realized range/volume — all derived from the rolling return distribution.
# Rule: rolling windows > 21d compute returns on 'closeadj'.
import numpy as np
import pandas as pd

NICE = [np.inf, -np.inf]


def _ret(df):
    c = df['closeadj'].astype(float)
    return np.log(c / c.shift(1))


def _safe(s):
    return s.replace(NICE, np.nan)


def _z(s, w=63):
    m = s.rolling(w, min_periods=max(5, w // 3)).mean()
    sd = s.rolling(w, min_periods=max(5, w // 3)).std()
    return _safe((s - m) / sd)


def _slope(s, w=21):
    return _safe(s - s.shift(w))


def _pct_rank(s, w):
    return s.rolling(w, min_periods=max(10, w // 3)).apply(
        lambda x: (x[-1] >= x).mean() if not np.isnan(x[-1]) else np.nan, raw=True)


def _var(r, w, q):
    return r.rolling(w, min_periods=max(10, w // 3)).quantile(q)


def _cvar(r, w, q):
    def f(x):
        if np.isnan(x).all():
            return np.nan
        thr = np.nanquantile(x, q)
        tail = x[x <= thr]
        return np.nanmean(tail) if tail.size else np.nan
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _tail_ratio(r, w, q):
    rt = r.rolling(w, min_periods=max(10, w // 3)).quantile(1.0 - q)
    lt = r.rolling(w, min_periods=max(10, w // 3)).quantile(q)
    return _safe(rt / lt.abs())


def _semi_down(r, w):
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(10, w // 3)).mean())


def _semi_up(r, w):
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(10, w // 3)).mean())


def _convex_gain(r, w):
    return ((r.where(r > 0, 0.0)) ** 2).rolling(w, min_periods=max(10, w // 3)).mean()


def _convex_loss(r, w):
    return ((r.where(r < 0, 0.0)) ** 2).rolling(w, min_periods=max(10, w // 3)).mean()


def _cubic_tail(r, w):
    def f(x):
        x = x[~np.isnan(x)]
        if x.size < 5:
            return np.nan
        m = x.mean(); sd = x.std()
        if sd == 0:
            return np.nan
        return np.mean(((x - m) / sd) ** 3)
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _quartic_tail(r, w):
    def f(x):
        x = x[~np.isnan(x)]
        if x.size < 5:
            return np.nan
        m = x.mean(); sd = x.std()
        if sd == 0:
            return np.nan
        return np.mean(((x - m) / sd) ** 4)
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _max_dd_tail(df, w):
    c = df['closeadj'].astype(float)
    roll_max = c.rolling(w, min_periods=max(10, w // 3)).max()
    dd = c / roll_max - 1.0
    return dd.rolling(w, min_periods=max(10, w // 3)).min()


def get_f11_tail_risk_convexity_base_076_150(df):
    df = df.copy()
    r = _ret(df)
    f = {}

    def put(i, series):
        f[f'f11_tail_risk_convexity_{i:03d}'] = _safe(series)

    wins = [21, 63, 126, 252]
    qs = [0.01, 0.05, 0.10]

    i = 76

    # --- 1) z-scores of VaR across windows x quantiles (12) ---
    for w in wins:
        for q in qs:
            put(i, _z(_var(r, w, q), w)); i += 1

    # --- 2) slope/delta of CVaR across windows x quantiles (12) ---
    for w in wins:
        for q in qs:
            put(i, _slope(_cvar(r, w, q), 21)); i += 1

    # --- 3) z-score of tail ratio across windows x quantiles (12) ---
    for w in wins:
        for q in qs:
            put(i, _z(_tail_ratio(r, w, q), w)); i += 1

    # --- 4) short-vs-long tail spreads (VaR & CVaR at 5%): short - long (8) ---
    for q in [0.05, 0.10]:
        short_var = _var(r, 21, q)
        for lw in [63, 126, 252]:
            put(i, _safe(short_var - _var(r, lw, q))); i += 1
        # one CVaR short-long per q
        put(i, _safe(_cvar(r, 21, q) - _cvar(r, 252, q))); i += 1

    # --- 5) regime / threshold distance: how far current VaR-5% is below its
    #         long-run mean, normalized (a stress-regime distance) (4) ---
    for w in wins:
        v = _var(r, w, 0.05)
        lr = v.rolling(252, min_periods=63).mean()
        lrsd = v.rolling(252, min_periods=63).std()
        put(i, _safe((v - lr) / lrsd)); i += 1

    # --- 6) semi-deviation asymmetry z-scores (4) ---
    for w in wins:
        asym = _safe(_semi_down(r, w) / _semi_up(r, w))
        put(i, _z(asym, w)); i += 1

    # --- 7) convexity dominance slope (loss/gain convexity, delta) (4) ---
    for w in wins:
        dom = _safe(_convex_loss(r, w) / _convex_gain(r, w))
        put(i, _slope(dom, 21)); i += 1

    # --- 8) cubic-tail z-score and quartic-tail z-score (4 + 4 = 8) ---
    for w in wins:
        put(i, _z(_cubic_tail(r, w), w)); i += 1
    for w in wins:
        put(i, _z(_quartic_tail(r, w), w)); i += 1

    # --- 9) max-drawdown-tail slope and short-vs-long spread (4 + 3 = 7) ---
    for w in wins:
        put(i, _slope(_max_dd_tail(df, w), 21)); i += 1
    short_dd = _max_dd_tail(df, 21)
    for lw in [63, 126, 252]:
        put(i, _safe(short_dd - _max_dd_tail(df, lw))); i += 1

    # --- 10) tail-risk x range/volume interactions (fill remainder) ---
    rng = ((df['high'] - df['low']) / df['close'].replace(0, np.nan)).astype(float)
    dvol = (df['closeadj'] * df['volume']).astype(float)
    # CVaR-5% scaled by realized range and by dollar-volume z
    for w in [63, 126, 252]:
        cv = _cvar(r, w, 0.05)
        put(i, _safe(cv * rng.rolling(w, min_periods=max(10, w // 3)).mean())); i += 1
    for w in [63, 126, 252]:
        cv = _cvar(r, w, 0.05)
        put(i, _safe(cv * _z(dvol, w))); i += 1

    # percentile rank of VaR-5% (regime locator) to top up to 150
    base5_63 = _var(r, 63, 0.05)
    extra_w = [63, 126, 252, 126]
    j = 0
    while i <= 150:
        put(i, _pct_rank(base5_63, extra_w[j % len(extra_w)])); j += 1; i += 1

    out = pd.DataFrame(f)
    cols = [f'f11_tail_risk_convexity_{k:03d}' for k in range(76, 151)]
    return out.reindex(columns=cols)
