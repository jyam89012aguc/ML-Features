"""
11_decline_path_entropy — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative entropy features — curvature of disorder trajectory
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Each feature applies .diff / slope / pct-change to 2nd-derivative concepts.
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


# ── Scalar helpers for base recomputation ─────────────────────────────────────

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


# ── Helper: recompute 2nd-derivative series (drv2 layer) ─────────────────────

def _drv2_entropy_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day return entropy."""
    ret = _daily_ret(close)
    e21 = ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)
    return e21.diff(5)


def _drv2_sign_change_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day sign-change rate."""
    ret = _daily_ret(close)
    sc21 = ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)
    return sc21.diff(5)


def _drv2_path_eff_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day path efficiency."""
    pe21 = close.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)
    return pe21.diff(5)


def _drv2_tp_density_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day turning-point density."""
    tp21 = close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _turning_point_density_raw, raw=True)
    return tp21.diff(5)


def _drv2_perm_entropy_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day permutation entropy."""
    pe21 = close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _permutation_entropy_raw, raw=True)
    return pe21.diff(5)


def _drv2_hurst_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day Hurst R/S."""
    h21 = close.rolling(_TD_MON, min_periods=max(8, _TD_MON // 2)).apply(
        _hurst_rs_raw, raw=True)
    return h21.diff(5)


def _drv2_choppiness_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day choppiness."""
    ch21 = close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)
    return ch21.diff(5)


def _drv2_fractal_dim_5d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 5-day diff of 21-day fractal dim."""
    fd21 = close.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).apply(
        _fractal_dim_raw, raw=True)
    return fd21.diff(5)


def _drv2_entropy_21d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 21-day diff of 21-day return entropy."""
    ret = _daily_ret(close)
    e21 = ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)
    return e21.diff(_TD_MON)


def _drv2_sign_change_21d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 21-day diff of 21-day sign-change rate."""
    ret = _daily_ret(close)
    sc21 = ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)
    return sc21.diff(_TD_MON)


def _drv2_choppiness_21d(close: pd.Series) -> pd.Series:
    """2nd-deriv: 21-day diff of 21-day choppiness."""
    ch21 = close.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _choppiness_raw, raw=True)
    return ch21.diff(_TD_MON)


def _drv2_slope_entropy(close: pd.Series) -> pd.Series:
    """2nd-deriv: 10-day OLS slope of 21-day entropy."""
    ret = _daily_ret(close)
    e21 = ret.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _shannon_entropy_raw, raw=True)
    return _linslope(e21, 10)


def _drv2_slope_sign_change(close: pd.Series) -> pd.Series:
    """2nd-deriv: 10-day OLS slope of 21-day sign-change rate."""
    ret = _daily_ret(close)
    sc21 = ret.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _sign_change_rate_raw, raw=True)
    return _linslope(sc21, 10)


def _drv2_slope_path_eff(close: pd.Series) -> pd.Series:
    """2nd-deriv: 10-day OLS slope of 21-day path efficiency."""
    pe21 = close.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        _path_efficiency_raw, raw=True)
    return _linslope(pe21, 10)


# ── 3rd-Derivative Feature Functions ──────────────────────────────────────────

def dpe_drv3_001_entropy_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d entropy) — 2nd discrete derivative of entropy."""
    return _drv2_entropy_5d(close).diff(5)


def dpe_drv3_002_entropy_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of 21d entropy)."""
    return _drv2_entropy_5d(close).diff(_TD_MON)


def dpe_drv3_003_sign_change_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of sign-change rate)."""
    return _drv2_sign_change_5d(close).diff(5)


def dpe_drv3_004_sign_change_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of sign-change rate)."""
    return _drv2_sign_change_5d(close).diff(_TD_MON)


def dpe_drv3_005_path_eff_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of path efficiency)."""
    return _drv2_path_eff_5d(close).diff(5)


def dpe_drv3_006_path_eff_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of path efficiency)."""
    return _drv2_path_eff_5d(close).diff(_TD_MON)


def dpe_drv3_007_tp_density_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of turning-point density)."""
    return _drv2_tp_density_5d(close).diff(5)


def dpe_drv3_008_tp_density_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of turning-point density)."""
    return _drv2_tp_density_5d(close).diff(_TD_MON)


def dpe_drv3_009_perm_entropy_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of permutation entropy)."""
    return _drv2_perm_entropy_5d(close).diff(5)


def dpe_drv3_010_perm_entropy_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of permutation entropy)."""
    return _drv2_perm_entropy_5d(close).diff(_TD_MON)


def dpe_drv3_011_hurst_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of Hurst R/S)."""
    return _drv2_hurst_5d(close).diff(5)


def dpe_drv3_012_hurst_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of Hurst R/S)."""
    return _drv2_hurst_5d(close).diff(_TD_MON)


def dpe_drv3_013_choppiness_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of choppiness)."""
    return _drv2_choppiness_5d(close).diff(5)


def dpe_drv3_014_choppiness_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of choppiness)."""
    return _drv2_choppiness_5d(close).diff(_TD_MON)


def dpe_drv3_015_fractal_dim_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of fractal dimension)."""
    return _drv2_fractal_dim_5d(close).diff(5)


def dpe_drv3_016_fractal_dim_5d_diff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of fractal dimension)."""
    return _drv2_fractal_dim_5d(close).diff(_TD_MON)


def dpe_drv3_017_entropy_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of entropy)."""
    return _drv2_entropy_21d(close).diff(5)


def dpe_drv3_018_sign_change_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of sign-change rate)."""
    return _drv2_sign_change_21d(close).diff(5)


def dpe_drv3_019_choppiness_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of choppiness)."""
    return _drv2_choppiness_21d(close).diff(5)


def dpe_drv3_020_slope_entropy_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (10-day OLS slope of entropy)."""
    return _drv2_slope_entropy(close).diff(5)


def dpe_drv3_021_slope_entropy_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (10-day OLS slope of entropy)."""
    return _drv2_slope_entropy(close).diff(_TD_MON)


def dpe_drv3_022_slope_sign_change_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (10-day OLS slope of sign-change rate)."""
    return _drv2_slope_sign_change(close).diff(5)


def dpe_drv3_023_slope_sign_change_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (10-day OLS slope of sign-change rate)."""
    return _drv2_slope_sign_change(close).diff(_TD_MON)


def dpe_drv3_024_slope_path_eff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (10-day OLS slope of path efficiency)."""
    return _drv2_slope_path_eff(close).diff(5)


def dpe_drv3_025_slope_path_eff_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of (10-day OLS slope of path efficiency)."""
    return _drv2_slope_path_eff(close).diff(_TD_MON)


# ── Registry ───────────────────────────────────────────────────────────────────

DECLINE_PATH_ENTROPY_REGISTRY_3RD_DERIVATIVES = {
    "dpe_drv3_001_entropy_5d_diff_5d_diff":         {"inputs": ["close"], "func": dpe_drv3_001_entropy_5d_diff_5d_diff},
    "dpe_drv3_002_entropy_5d_diff_21d_diff":         {"inputs": ["close"], "func": dpe_drv3_002_entropy_5d_diff_21d_diff},
    "dpe_drv3_003_sign_change_5d_diff_5d_diff":      {"inputs": ["close"], "func": dpe_drv3_003_sign_change_5d_diff_5d_diff},
    "dpe_drv3_004_sign_change_5d_diff_21d_diff":     {"inputs": ["close"], "func": dpe_drv3_004_sign_change_5d_diff_21d_diff},
    "dpe_drv3_005_path_eff_5d_diff_5d_diff":         {"inputs": ["close"], "func": dpe_drv3_005_path_eff_5d_diff_5d_diff},
    "dpe_drv3_006_path_eff_5d_diff_21d_diff":        {"inputs": ["close"], "func": dpe_drv3_006_path_eff_5d_diff_21d_diff},
    "dpe_drv3_007_tp_density_5d_diff_5d_diff":       {"inputs": ["close"], "func": dpe_drv3_007_tp_density_5d_diff_5d_diff},
    "dpe_drv3_008_tp_density_5d_diff_21d_diff":      {"inputs": ["close"], "func": dpe_drv3_008_tp_density_5d_diff_21d_diff},
    "dpe_drv3_009_perm_entropy_5d_diff_5d_diff":     {"inputs": ["close"], "func": dpe_drv3_009_perm_entropy_5d_diff_5d_diff},
    "dpe_drv3_010_perm_entropy_5d_diff_21d_diff":    {"inputs": ["close"], "func": dpe_drv3_010_perm_entropy_5d_diff_21d_diff},
    "dpe_drv3_011_hurst_5d_diff_5d_diff":            {"inputs": ["close"], "func": dpe_drv3_011_hurst_5d_diff_5d_diff},
    "dpe_drv3_012_hurst_5d_diff_21d_diff":           {"inputs": ["close"], "func": dpe_drv3_012_hurst_5d_diff_21d_diff},
    "dpe_drv3_013_choppiness_5d_diff_5d_diff":       {"inputs": ["close"], "func": dpe_drv3_013_choppiness_5d_diff_5d_diff},
    "dpe_drv3_014_choppiness_5d_diff_21d_diff":      {"inputs": ["close"], "func": dpe_drv3_014_choppiness_5d_diff_21d_diff},
    "dpe_drv3_015_fractal_dim_5d_diff_5d_diff":      {"inputs": ["close"], "func": dpe_drv3_015_fractal_dim_5d_diff_5d_diff},
    "dpe_drv3_016_fractal_dim_5d_diff_21d_diff":     {"inputs": ["close"], "func": dpe_drv3_016_fractal_dim_5d_diff_21d_diff},
    "dpe_drv3_017_entropy_21d_diff_5d_diff":         {"inputs": ["close"], "func": dpe_drv3_017_entropy_21d_diff_5d_diff},
    "dpe_drv3_018_sign_change_21d_diff_5d_diff":     {"inputs": ["close"], "func": dpe_drv3_018_sign_change_21d_diff_5d_diff},
    "dpe_drv3_019_choppiness_21d_diff_5d_diff":      {"inputs": ["close"], "func": dpe_drv3_019_choppiness_21d_diff_5d_diff},
    "dpe_drv3_020_slope_entropy_5d_diff":            {"inputs": ["close"], "func": dpe_drv3_020_slope_entropy_5d_diff},
    "dpe_drv3_021_slope_entropy_21d_diff":           {"inputs": ["close"], "func": dpe_drv3_021_slope_entropy_21d_diff},
    "dpe_drv3_022_slope_sign_change_5d_diff":        {"inputs": ["close"], "func": dpe_drv3_022_slope_sign_change_5d_diff},
    "dpe_drv3_023_slope_sign_change_21d_diff":       {"inputs": ["close"], "func": dpe_drv3_023_slope_sign_change_21d_diff},
    "dpe_drv3_024_slope_path_eff_5d_diff":           {"inputs": ["close"], "func": dpe_drv3_024_slope_path_eff_5d_diff},
    "dpe_drv3_025_slope_path_eff_21d_diff":          {"inputs": ["close"], "func": dpe_drv3_025_slope_path_eff_21d_diff},
}
