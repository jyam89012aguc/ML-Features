"""
11_decline_path_entropy — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base entropy/roughness features — captures acceleration of disorder
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature computes a .diff(n) / slope / pct-change of a base entropy concept.
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9
_N_BINS  = 8

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        x = x[~np.isnan(x)]
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        num = ((xi - xi_m) * (x - x.mean())).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den < _EPS:
            return np.nan
        return float(num / den)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Scalar helpers for base-feature recomputation ─────────────────────────────

def _shannon_entropy_raw(x: np.ndarray, n_bins: int = _N_BINS) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    mn, mx = x.min(), x.max()
    if mx - mn < _EPS:
        return 0.0
    bins = np.linspace(mn, mx, n_bins + 1)
    counts, _ = np.histogram(x, bins=bins)
    total = counts.sum()
    if total == 0:
        return np.nan
    probs = counts[counts > 0] / total
    return float(-np.sum(probs * np.log(probs + _EPS)))


def _sign_change_rate_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    signs = np.sign(x)
    changes = np.sum(signs[1:] != signs[:-1])
    return float(changes / (len(x) - 1))


def _turning_point_density_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    tp = 0
    for i in range(1, len(x) - 1):
        if (x[i] > x[i - 1] and x[i] > x[i + 1]) or (x[i] < x[i - 1] and x[i] < x[i + 1]):
            tp += 1
    return float(tp / (len(x) - 2))


def _path_efficiency_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    net = abs(x[-1] - x[0])
    total = np.sum(np.abs(np.diff(x)))
    if total < _EPS:
        return 1.0
    return float(net / total)


def _permutation_entropy_raw(x: np.ndarray, order: int = 3) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < order + 1:
        return np.nan
    from math import factorial
    count = {}
    for i in range(n - order):
        pat = tuple(np.argsort(x[i:i + order]))
        count[pat] = count.get(pat, 0) + 1
    total = sum(count.values())
    if total == 0:
        return np.nan
    probs = np.array(list(count.values())) / total
    max_ent = np.log(factorial(order))
    if max_ent < _EPS:
        return 0.0
    ent = -np.sum(probs * np.log(probs + _EPS))
    return float(ent / max_ent)


def _hurst_rs_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    half = n // 2
    sub = [x[:half], x[half:half * 2]]
    rs_vals = []
    for seg in sub:
        mean_s = seg.mean()
        dev = np.cumsum(seg - mean_s)
        r = dev.max() - dev.min()
        s = seg.std()
        if s < _EPS:
            continue
        rs_vals.append(r / s)
    if len(rs_vals) == 0:
        return np.nan
    rs = np.mean(rs_vals)
    if rs <= 0:
        return np.nan
    return float(np.log(rs) / np.log(half + _EPS))


def _choppiness_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 2:
        return np.nan
    rng = x.max() - x.min()
    atr_sum = np.sum(np.abs(np.diff(x)))
    if rng < _EPS or atr_sum < _EPS:
        return np.nan
    return float(np.log10(atr_sum) - np.log10(rng))


def _neg_fraction_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return np.nan
    return float(np.sum(x < 0) / len(x))


def _fractal_dim_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    def lm(k):
        total = 0.0
        for m_ in range(1, k + 1):
            idxs = np.arange(m_ - 1, n, k)
            if len(idxs) < 2:
                continue
            seg = x[idxs]
            lm_val = np.sum(np.abs(np.diff(seg))) * (n - 1) / (k * len(idxs))
            total += lm_val
        return total / k if k > 0 else np.nan
    l1, l2 = lm(1), lm(2)
    if l1 is None or l2 is None or l1 <= 0 or l2 <= 0:
        return np.nan
    return float(np.log(l1 / l2) / np.log(2.0))


def _autocorr_lag1_raw(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan
    s = pd.Series(x)
    c = s.autocorr(lag=1)
    return float(c) if not np.isnan(c) else np.nan


# ── Helper: recompute base entropy series ─────────────────────────────────────

def _base_entropy_ret_21d(close: pd.Series) -> pd.Series:
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)


def _base_entropy_ret_63d(close: pd.Series) -> pd.Series:
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _shannon_entropy_raw, raw=True)


def _base_sign_change_21d(close: pd.Series) -> pd.Series:
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)


def _base_sign_change_63d(close: pd.Series) -> pd.Series:
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _sign_change_rate_raw, raw=True)


def _base_tp_density_21d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)


def _base_path_eff_21d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)


def _base_perm_entropy_21d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)


def _base_hurst_21d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _hurst_rs_raw, raw=True)


def _base_hurst_63d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _hurst_rs_raw, raw=True)


def _base_choppiness_21d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)


def _base_choppiness_63d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_QTR, min_periods=max(6, _TD_QTR // 2)).apply(
        _choppiness_raw, raw=True)


def _base_fractal_dim_21d(close: pd.Series) -> pd.Series:
    return close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)


def _base_neg_frac_63d(close: pd.Series) -> pd.Series:
    ret = _daily_ret(close)
    return ret.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(
        _neg_fraction_raw, raw=True)


def _base_autocorr_lag1_21d(close: pd.Series) -> pd.Series:
    ret = _daily_ret(close)
    return ret.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _autocorr_lag1_raw, raw=True)


# ── 2nd-Derivative Feature Functions ──────────────────────────────────────────

def dpe_drv2_001_entropy_ret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first-difference of 21-day return Shannon entropy."""
    return _base_entropy_ret_21d(close).diff(5)


def dpe_drv2_002_entropy_ret_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day first-difference of 21-day return Shannon entropy."""
    return _base_entropy_ret_21d(close).diff(_TD_MON)


def dpe_drv2_003_entropy_ret_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first-difference of 63-day return Shannon entropy."""
    return _base_entropy_ret_63d(close).diff(5)


def dpe_drv2_004_entropy_ret_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day first-difference of 63-day return Shannon entropy."""
    return _base_entropy_ret_63d(close).diff(_TD_MON)


def dpe_drv2_005_sign_change_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day sign-change rate (acceleration of choppiness onset)."""
    return _base_sign_change_21d(close).diff(5)


def dpe_drv2_006_sign_change_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day sign-change rate."""
    return _base_sign_change_21d(close).diff(_TD_MON)


def dpe_drv2_007_sign_change_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day sign-change rate."""
    return _base_sign_change_63d(close).diff(_TD_MON)


def dpe_drv2_008_tp_density_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day turning-point density."""
    return _base_tp_density_21d(close).diff(5)


def dpe_drv2_009_tp_density_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day turning-point density."""
    return _base_tp_density_21d(close).diff(_TD_MON)


def dpe_drv2_010_path_eff_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day path efficiency (smoothness change)."""
    return _base_path_eff_21d(close).diff(5)


def dpe_drv2_011_path_eff_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day path efficiency."""
    return _base_path_eff_21d(close).diff(_TD_MON)


def dpe_drv2_012_perm_entropy_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day permutation entropy."""
    return _base_perm_entropy_21d(close).diff(5)


def dpe_drv2_013_perm_entropy_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day permutation entropy."""
    return _base_perm_entropy_21d(close).diff(_TD_MON)


def dpe_drv2_014_hurst_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Hurst R/S estimate."""
    return _base_hurst_21d(close).diff(5)


def dpe_drv2_015_hurst_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Hurst R/S estimate."""
    return _base_hurst_63d(close).diff(_TD_MON)


def dpe_drv2_016_choppiness_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day choppiness index."""
    return _base_choppiness_21d(close).diff(5)


def dpe_drv2_017_choppiness_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day choppiness index."""
    return _base_choppiness_21d(close).diff(_TD_MON)


def dpe_drv2_018_choppiness_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day choppiness index."""
    return _base_choppiness_63d(close).diff(_TD_MON)


def dpe_drv2_019_fractal_dim_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day fractal dimension proxy."""
    return _base_fractal_dim_21d(close).diff(5)


def dpe_drv2_020_fractal_dim_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day fractal dimension proxy."""
    return _base_fractal_dim_21d(close).diff(_TD_MON)


def dpe_drv2_021_neg_frac_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day negative-return fraction."""
    return _base_neg_frac_63d(close).diff(_TD_MON)


def dpe_drv2_022_autocorr_lag1_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day lag-1 return autocorrelation."""
    return _base_autocorr_lag1_21d(close).diff(5)


def dpe_drv2_023_entropy_ret_21d_slope_10d(close: pd.Series) -> pd.Series:
    """10-day OLS slope of 21-day return Shannon entropy."""
    ent = _base_entropy_ret_21d(close)
    return _linslope(ent, 10)


def dpe_drv2_024_sign_change_21d_slope_10d(close: pd.Series) -> pd.Series:
    """10-day OLS slope of 21-day sign-change rate."""
    sc = _base_sign_change_21d(close)
    return _linslope(sc, 10)


def dpe_drv2_025_path_eff_21d_slope_10d(close: pd.Series) -> pd.Series:
    """10-day OLS slope of 21-day path efficiency."""
    pe = _base_path_eff_21d(close)
    return _linslope(pe, 10)


# ── Registry ───────────────────────────────────────────────────────────────────

DECLINE_PATH_ENTROPY_REGISTRY_2ND_DERIVATIVES = {
    "dpe_drv2_001_entropy_ret_21d_5d_diff":     {"inputs": ["close"], "func": dpe_drv2_001_entropy_ret_21d_5d_diff},
    "dpe_drv2_002_entropy_ret_21d_21d_diff":    {"inputs": ["close"], "func": dpe_drv2_002_entropy_ret_21d_21d_diff},
    "dpe_drv2_003_entropy_ret_63d_5d_diff":     {"inputs": ["close"], "func": dpe_drv2_003_entropy_ret_63d_5d_diff},
    "dpe_drv2_004_entropy_ret_63d_21d_diff":    {"inputs": ["close"], "func": dpe_drv2_004_entropy_ret_63d_21d_diff},
    "dpe_drv2_005_sign_change_21d_5d_diff":     {"inputs": ["close"], "func": dpe_drv2_005_sign_change_21d_5d_diff},
    "dpe_drv2_006_sign_change_21d_21d_diff":    {"inputs": ["close"], "func": dpe_drv2_006_sign_change_21d_21d_diff},
    "dpe_drv2_007_sign_change_63d_21d_diff":    {"inputs": ["close"], "func": dpe_drv2_007_sign_change_63d_21d_diff},
    "dpe_drv2_008_tp_density_21d_5d_diff":      {"inputs": ["close"], "func": dpe_drv2_008_tp_density_21d_5d_diff},
    "dpe_drv2_009_tp_density_21d_21d_diff":     {"inputs": ["close"], "func": dpe_drv2_009_tp_density_21d_21d_diff},
    "dpe_drv2_010_path_eff_21d_5d_diff":        {"inputs": ["close"], "func": dpe_drv2_010_path_eff_21d_5d_diff},
    "dpe_drv2_011_path_eff_21d_21d_diff":       {"inputs": ["close"], "func": dpe_drv2_011_path_eff_21d_21d_diff},
    "dpe_drv2_012_perm_entropy_21d_5d_diff":    {"inputs": ["close"], "func": dpe_drv2_012_perm_entropy_21d_5d_diff},
    "dpe_drv2_013_perm_entropy_21d_21d_diff":   {"inputs": ["close"], "func": dpe_drv2_013_perm_entropy_21d_21d_diff},
    "dpe_drv2_014_hurst_21d_5d_diff":           {"inputs": ["close"], "func": dpe_drv2_014_hurst_21d_5d_diff},
    "dpe_drv2_015_hurst_63d_21d_diff":          {"inputs": ["close"], "func": dpe_drv2_015_hurst_63d_21d_diff},
    "dpe_drv2_016_choppiness_21d_5d_diff":      {"inputs": ["close"], "func": dpe_drv2_016_choppiness_21d_5d_diff},
    "dpe_drv2_017_choppiness_21d_21d_diff":     {"inputs": ["close"], "func": dpe_drv2_017_choppiness_21d_21d_diff},
    "dpe_drv2_018_choppiness_63d_21d_diff":     {"inputs": ["close"], "func": dpe_drv2_018_choppiness_63d_21d_diff},
    "dpe_drv2_019_fractal_dim_21d_5d_diff":     {"inputs": ["close"], "func": dpe_drv2_019_fractal_dim_21d_5d_diff},
    "dpe_drv2_020_fractal_dim_21d_21d_diff":    {"inputs": ["close"], "func": dpe_drv2_020_fractal_dim_21d_21d_diff},
    "dpe_drv2_021_neg_frac_63d_21d_diff":       {"inputs": ["close"], "func": dpe_drv2_021_neg_frac_63d_21d_diff},
    "dpe_drv2_022_autocorr_lag1_21d_5d_diff":   {"inputs": ["close"], "func": dpe_drv2_022_autocorr_lag1_21d_5d_diff},
    "dpe_drv2_023_entropy_ret_21d_slope_10d":   {"inputs": ["close"], "func": dpe_drv2_023_entropy_ret_21d_slope_10d},
    "dpe_drv2_024_sign_change_21d_slope_10d":   {"inputs": ["close"], "func": dpe_drv2_024_sign_change_21d_slope_10d},
    "dpe_drv2_025_path_eff_21d_slope_10d":      {"inputs": ["close"], "func": dpe_drv2_025_path_eff_21d_slope_10d},
}
