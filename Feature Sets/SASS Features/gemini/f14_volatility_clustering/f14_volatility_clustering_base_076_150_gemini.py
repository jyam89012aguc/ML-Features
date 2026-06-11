# f14_volatility_clustering — REAL indicator logic (base 076..150)
# Indicator: volatility clustering / ARCH effects (second 75 variants).
# Facets here: vol-of-vol, high-vol streaks, regime distance, EWMA-vol slope,
# GARCH-like decay, squared-return ACF slopes/ratios, vol-ratio z-scores,
# clustering-strength dispersion, and short-vs-long persistence spreads.
# Windows > 21d use 'closeadj' (per spec). Returns are log closeadj returns.
import numpy as np
import pandas as pd

WINDOWS = [21, 63, 126, 252]
LAGS = [1, 2, 3, 5, 10]


def _ret(df):
    c = df['closeadj'].astype(float)
    return np.log(c / c.shift(1))


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _rolling_acf(x, lag, window):
    return _clean(x.rolling(window).corr(x.shift(lag)))


def _ewma_vol(r, span):
    return np.sqrt(r.pow(2).ewm(span=span, min_periods=max(5, span // 3)).mean())


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return _clean((s - m) / sd)


def _roc(s, window):
    return _clean(s / s.shift(window) - 1.0)


def _slope(s, window):
    """Per-step OLS slope of s over a trailing window (vectorised)."""
    n = window
    x = np.arange(n, dtype=float)
    xm = x.mean()
    xden = ((x - xm) ** 2).sum()

    def _fit(arr):
        if np.isnan(arr).any():
            return np.nan
        ym = arr.mean()
        return ((x - xm) * (arr - ym)).sum() / xden

    return _clean(s.rolling(n).apply(_fit, raw=True))


def get_f14_volatility_clustering_base_076_150(df):
    features = {}
    r = _ret(df)
    r2 = r.pow(2)
    ra = r.abs()

    def put(i, series):
        features[f'f14_volatility_clustering_{i:03d}'] = _clean(series)

    i = 76

    # --- Facet L: vol-of-vol (std of trailing realized vol) (4) ---
    # Clustering manifests as a fluctuating volatility level => high vol-of-vol.
    for w in WINDOWS:
        rv = r.rolling(max(5, w // 5)).std()
        put(i, rv.rolling(w).std()); i += 1

    # --- Facet M: vol-of-vol normalized by vol level (coefficient of variation) (4) ---
    for w in WINDOWS:
        rv = r.rolling(max(5, w // 5)).std()
        put(i, _clean(rv.rolling(w).std() / rv.rolling(w).mean())); i += 1

    # --- Facet N: high-vol streak length (4) ---
    # Consecutive days where short-window vol exceeds its trailing median:
    # clustering produces long runs of elevated volatility.
    for w in WINDOWS:
        rv = r.rolling(max(5, w // 5)).std()
        med = rv.rolling(w).median()
        hi = (rv > med).astype(float)
        # streak: cumulative run length of consecutive 1s
        grp = (hi == 0).cumsum()
        streak = hi.groupby(grp).cumsum()
        put(i, streak); i += 1

    # --- Facet O: regime distance — current vol z-score vs long history (4) ---
    # Distance of current vol from its long-run mean in std units (regime gauge).
    for w in WINDOWS:
        rv = r.rolling(max(5, w // 5)).std()
        put(i, _z(rv, w)); i += 1

    # --- Facet P: EWMA-vol slope (trend of volatility) (4) ---
    for w in WINDOWS:
        ev = _ewma_vol(r, span=w)
        put(i, _slope(ev, w)); i += 1

    # --- Facet Q: GARCH-like decay — ratio of lag-2 to lag-1 squared-ACF (4) ---
    # Geometric ACF decay characteristic of GARCH(1,1); ratio ~ persistence.
    for w in WINDOWS:
        a1 = _rolling_acf(r2, 1, w)
        a2 = _rolling_acf(r2, 2, w)
        put(i, _clean(a2 / a1)); i += 1

    # --- Facet R: squared-return ACF decay slope across lags 1,2,3,5,10 (4) ---
    # Fit a line through the ACF-vs-lag profile; steeper => faster decay.
    lag_arr = np.array(LAGS, dtype=float)
    lag_m = lag_arr.mean()
    lag_den = ((lag_arr - lag_m) ** 2).sum()
    for w in WINDOWS:
        acfs = [_rolling_acf(r2, lag, w) for lag in LAGS]
        acf_mat = pd.concat(acfs, axis=1)
        acf_mean = acf_mat.mean(axis=1)
        num = sum((LAGS[k] - lag_m) * (acfs[k] - acf_mean) for k in range(len(LAGS)))
        put(i, _clean(num / lag_den)); i += 1

    # --- Facet S: current/trailing vol ratio z-score (4) ---
    for w in WINDOWS:
        short = r.rolling(max(5, w // 5)).std()
        trail = r.rolling(w).std()
        ratio = _clean(short / trail)
        put(i, _z(ratio, w)); i += 1

    # --- Facet T: clustering strength rate-of-change (4) ---
    # Momentum of the summed squared-return ACF (clustering building/fading).
    for w in WINDOWS:
        strength = sum(_rolling_acf(r2, lag, w) for lag in LAGS)
        put(i, _roc(strength, max(5, w // 5))); i += 1

    # --- Facet U: |return| ACF lag-1 z-score (4) ---
    for w in WINDOWS:
        a1 = _rolling_acf(ra, 1, w)
        put(i, _z(a1, w)); i += 1

    # --- Facet V: EWMA-vol persistence (lag-1 ACF) on ABSOLUTE-return EWMA (4) ---
    for w in WINDOWS:
        eva = np.sqrt(ra.pow(2).ewm(span=w, min_periods=max(5, w // 3)).mean())
        put(i, _rolling_acf(eva, 1, w)); i += 1

    # Counts so far: L4 M4 N4 O4 P4 Q4 R4 S4 T4 U4 V4 = 44 (i now 120).
    # Need 31 more (120..150).

    # --- Facet W: vol ratio (fast EWMA vol / slow EWMA vol) per window (4) ---
    for w in WINDOWS:
        fast = _ewma_vol(r, span=max(5, w // 3))
        slow = _ewma_vol(r, span=w)
        put(i, _clean(fast / slow)); i += 1  # 120..123

    # --- Facet X: half-life of |return| EWMA-vol shocks (4) ---
    for w in WINDOWS:
        eva = np.sqrt(ra.pow(2).ewm(span=w, min_periods=max(5, w // 3)).mean())
        rho = _rolling_acf(eva, 1, w).clip(lower=1e-4, upper=0.9999)
        put(i, _clean(np.log(0.5) / np.log(rho))); i += 1  # 124..127

    # --- Facet Y: squared-return ACF at each lag, fixed mid window=63 (5) ---
    for lag in LAGS:
        put(i, _rolling_acf(r2, lag, 63)); i += 1  # 128..132

    # --- Facet Z: squared-return ACF at each lag, fixed long window=252 (5) ---
    for lag in LAGS:
        put(i, _rolling_acf(r2, lag, 252)); i += 1  # 133..137

    # --- Facet AA: short-vs-long clustering-strength spread (3) ---
    s21 = sum(_rolling_acf(r2, lag, 21) for lag in LAGS)
    s63 = sum(_rolling_acf(r2, lag, 63) for lag in LAGS)
    s126 = sum(_rolling_acf(r2, lag, 126) for lag in LAGS)
    s252 = sum(_rolling_acf(r2, lag, 252) for lag in LAGS)
    put(i, _clean(s21 - s63)); i += 1    # 138
    put(i, _clean(s63 - s126)); i += 1   # 139
    put(i, _clean(s126 - s252)); i += 1  # 140

    # --- Facet AB: vol-persistence spread (EWMA-vol lag1 ACF short vs long) (3) ---
    p21 = _rolling_acf(_ewma_vol(r, 21), 1, 21)
    p63 = _rolling_acf(_ewma_vol(r, 63), 1, 63)
    p126 = _rolling_acf(_ewma_vol(r, 126), 1, 126)
    p252 = _rolling_acf(_ewma_vol(r, 252), 1, 252)
    put(i, _clean(p21 - p63)); i += 1    # 141
    put(i, _clean(p63 - p126)); i += 1   # 142
    put(i, _clean(p126 - p252)); i += 1  # 143

    # --- Facet AC: Ljung-Box-style |return| stat z-score (4) ---
    for w in WINDOWS:
        q = sum(_rolling_acf(ra, lag, w).pow(2) for lag in LAGS) * float(w)
        put(i, _z(q, w)); i += 1  # 144..147

    # --- Facet AD: vol-of-vol of EWMA vol, short/mid/long (3) ---
    put(i, _ewma_vol(r, 21).rolling(63).std()); i += 1    # 148
    put(i, _ewma_vol(r, 63).rolling(126).std()); i += 1   # 149
    put(i, _ewma_vol(r, 126).rolling(252).std()); i += 1  # 150

    out = pd.DataFrame(features)
    cols = [f'f14_volatility_clustering_{k:03d}' for k in range(76, 151)]
    return out[cols]
