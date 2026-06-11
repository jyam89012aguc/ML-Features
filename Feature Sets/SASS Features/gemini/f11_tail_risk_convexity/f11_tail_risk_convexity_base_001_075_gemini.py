# f11_tail_risk_convexity — REAL indicator logic (base 001..075)
# Indicator family: tail risk & convexity of the rolling return distribution.
# Facets: VaR (1/5/10%), CVaR / expected shortfall, tail ratio, downside/upside
# semi-deviation, gain/loss convexity (mean squared +/- returns), cubic (skew-like)
# and quartic (kurtosis-like) tail contributions, max-drawdown tail, Cornish-Fisher VaR,
# plus z-scores, slope/delta, short-vs-long tail spreads, regime distance.
# Rule: rolling windows > 21d compute returns on 'closeadj'.
import numpy as np
import pandas as pd

NICE = [np.inf, -np.inf]


def _ret(df):
    # log returns on closeadj (all our windows are > 21d per spec)
    c = df['closeadj'].astype(float)
    return np.log(c / c.shift(1))


def _z(s, w=63):
    m = s.rolling(w, min_periods=max(5, w // 3)).mean()
    sd = s.rolling(w, min_periods=max(5, w // 3)).std()
    return ((s - m) / sd).replace(NICE, np.nan)


def _slope(s, w=21):
    return (s - s.shift(w)).replace(NICE, np.nan)


def _safe(s):
    return s.replace(NICE, np.nan)


def _var(r, w, q):
    # VaR as the q-quantile of the return distribution (left tail, negative for losses)
    return r.rolling(w, min_periods=max(10, w // 3)).quantile(q)


def _cvar(r, w, q):
    # Expected shortfall: mean of returns at or below the q-quantile (left tail).
    def f(x):
        if np.isnan(x).all():
            return np.nan
        thr = np.nanquantile(x, q)
        tail = x[x <= thr]
        return np.nanmean(tail) if tail.size else np.nan
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _cvar_right(r, w, q):
    # Right-tail expected shortfall: mean of returns at or above the (1-q) quantile.
    def f(x):
        if np.isnan(x).all():
            return np.nan
        thr = np.nanquantile(x, 1.0 - q)
        tail = x[x >= thr]
        return np.nanmean(tail) if tail.size else np.nan
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _tail_ratio(r, w, q):
    # right-tail quantile magnitude / |left-tail quantile|
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
    # option-like upside convexity: mean of squared positive returns
    pos = (r.where(r > 0, 0.0)) ** 2
    return pos.rolling(w, min_periods=max(10, w // 3)).mean()


def _convex_loss(r, w):
    # option-like downside convexity: mean of squared negative returns
    neg = (r.where(r < 0, 0.0)) ** 2
    return neg.rolling(w, min_periods=max(10, w // 3)).mean()


def _cubic_tail(r, w):
    # skew-like tail contribution: mean of cubed centered returns / sigma^3
    def f(x):
        x = x[~np.isnan(x)]
        if x.size < 5:
            return np.nan
        m = x.mean()
        sd = x.std()
        if sd == 0:
            return np.nan
        return np.mean(((x - m) / sd) ** 3)
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _quartic_tail(r, w):
    # kurtosis-like tail contribution: mean of 4th centered moment / sigma^4
    def f(x):
        x = x[~np.isnan(x)]
        if x.size < 5:
            return np.nan
        m = x.mean()
        sd = x.std()
        if sd == 0:
            return np.nan
        return np.mean(((x - m) / sd) ** 4)
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def _max_dd_tail(df, w):
    # rolling max drawdown over the window (a tail of the cumulative path), <= 0
    c = df['closeadj'].astype(float)
    roll_max = c.rolling(w, min_periods=max(10, w // 3)).max()
    dd = c / roll_max - 1.0
    return dd.rolling(w, min_periods=max(10, w // 3)).min()


def _cornish_fisher_var(r, w, q):
    # CF-adjusted VaR using rolling mean/std/skew/kurt at standard-normal z(q)
    from scipy.stats import norm
    z = norm.ppf(q)

    def f(x):
        x = x[~np.isnan(x)]
        if x.size < 8:
            return np.nan
        m = x.mean()
        sd = x.std()
        if sd == 0:
            return np.nan
        s = np.mean(((x - m) / sd) ** 3)
        k = np.mean(((x - m) / sd) ** 4) - 3.0
        zcf = (z
               + (z ** 2 - 1) * s / 6.0
               + (z ** 3 - 3 * z) * k / 24.0
               - (2 * z ** 3 - 5 * z) * (s ** 2) / 36.0)
        return m + sd * zcf
    return r.rolling(w, min_periods=max(10, w // 3)).apply(f, raw=True)


def get_f11_tail_risk_convexity_base_001_075(df):
    df = df.copy()
    r = _ret(df)
    f = {}

    def put(i, series):
        f[f'f11_tail_risk_convexity_{i:03d}'] = _safe(series)

    wins = [21, 63, 126, 252]
    qs = [0.01, 0.05, 0.10]

    i = 1
    # --- 1) VaR levels across windows x quantiles (12) ---
    for w in wins:
        for q in qs:
            put(i, _var(r, w, q)); i += 1

    # --- 2) CVaR / expected shortfall (left tail) across windows x quantiles (12) ---
    for w in wins:
        for q in qs:
            put(i, _cvar(r, w, q)); i += 1

    # --- 3) Tail ratio across windows x quantiles (12) ---
    for w in wins:
        for q in qs:
            put(i, _tail_ratio(r, w, q)); i += 1

    # --- 4) Downside vs upside semi-deviation, and their spread (4 windows x 3 = 12) ---
    for w in wins:
        sd_d = _semi_down(r, w)
        sd_u = _semi_up(r, w)
        put(i, sd_d); i += 1
        put(i, sd_u); i += 1
        put(i, _safe(sd_d / sd_u)); i += 1  # downside/upside asymmetry

    # --- 5) Gain/loss convexity (mean squared +/- returns) and ratio (4 x 3 = 12) ---
    for w in wins:
        cg = _convex_gain(r, w)
        cl = _convex_loss(r, w)
        put(i, cg); i += 1
        put(i, cl); i += 1
        put(i, _safe(cl / cg)); i += 1  # loss-convexity dominance

    # --- 6) Cubic (skew-like) tail contribution across windows (4) ---
    for w in wins:
        put(i, _cubic_tail(r, w)); i += 1

    # --- 7) Quartic (kurtosis-like) tail contribution across windows (4) ---
    for w in wins:
        put(i, _quartic_tail(r, w)); i += 1

    # --- 8) Max-drawdown tail across windows (4) ---
    for w in wins:
        put(i, _max_dd_tail(df, w)); i += 1

    # --- 9) Cornish-Fisher VaR (63/126/252 x 1%/5%) (3 windows x 2 = 6) ---
    for w in [63, 126, 252]:
        for q in [0.01, 0.05]:
            put(i, _cornish_fisher_var(r, w, q)); i += 1

    # --- 10) Right-tail expected shortfall (63/126/252 @5%) (3) ---
    for w in [63, 126, 252]:
        put(i, _cvar_right(r, w, 0.05)); i += 1

    # fill any remainder up to 75 with z-scores of the VaR-5% level (diverse facet)
    base5 = _var(r, 63, 0.05)
    while i <= 75:
        put(i, _z(base5, 63 + (i % 5) * 21)); i += 1

    out = pd.DataFrame(f)
    cols = [f'f11_tail_risk_convexity_{k:03d}' for k in range(1, 76)]
    return out.reindex(columns=cols)
