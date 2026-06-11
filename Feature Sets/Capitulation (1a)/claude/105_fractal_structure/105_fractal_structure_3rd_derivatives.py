"""
105_fractal_structure — 3rd Derivatives (Features fct_drv3_001-025)
Domain: rate of change of 2nd-derivative fractal features — acceleration of Hurst,
        DFA, Higuchi/Katz FD, autocorrelation, variance-ratio, and roughness velocity.
        Texture acceleration ONLY — not depth or speed of decline.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ─── Scalar fractal helpers ────────────────────────────────────────────────────

def _hurst_rs(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    rs_vals, span_sizes = [], []
    for size in [n // 4, n // 2, n]:
        if size < 4:
            continue
        n_chunks = n // size
        if n_chunks < 1:
            continue
        rs_chunk = []
        for k in range(n_chunks):
            seg = x[k * size: (k + 1) * size]
            if len(seg) < 4:
                continue
            mean_s = seg.mean()
            dev = np.cumsum(seg - mean_s)
            r = dev.max() - dev.min()
            s = seg.std(ddof=1)
            if s < _EPS:
                continue
            rs_chunk.append(r / s)
        if rs_chunk:
            rs_vals.append(np.mean(rs_chunk))
            span_sizes.append(size)
    if len(rs_vals) < 2:
        return np.nan
    log_n = np.log(span_sizes)
    log_rs = np.log(np.maximum(rs_vals, _EPS))
    if log_n[-1] - log_n[0] < _EPS:
        return np.nan
    return float(np.polyfit(log_n, log_rs, 1)[0])


def _dfa_alpha(x: np.ndarray, scales: list) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 16:
        return np.nan
    y = np.cumsum(x - x.mean())
    f_vals, valid_scales = [], []
    for s in scales:
        if s < 4 or s > n // 2:
            continue
        n_seg = n // s
        if n_seg < 2:
            continue
        rms_list = []
        for k in range(n_seg):
            seg = y[k * s: (k + 1) * s]
            xi = np.arange(len(seg), dtype=float)
            coeffs = np.polyfit(xi, seg, 1)
            trend = np.polyval(coeffs, xi)
            rms_list.append(np.sqrt(np.mean((seg - trend) ** 2)))
        f_vals.append(np.mean(rms_list))
        valid_scales.append(s)
    if len(f_vals) < 2:
        return np.nan
    return float(np.polyfit(np.log(valid_scales), np.log(np.maximum(f_vals, _EPS)), 1)[0])


def _higuchi_fd(x: np.ndarray, k_max: int = 4) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    lk, ks = [], []
    for k in range(1, min(k_max + 1, n // 2)):
        Lm = []
        for m in range(1, k + 1):
            idx = np.arange(m - 1, n, k)
            if len(idx) < 2:
                continue
            diff_sum = np.sum(np.abs(np.diff(x[idx])))
            norm = (n - 1) / (((len(idx) - 1) * k) * k + _EPS)
            Lm.append(diff_sum * norm)
        if Lm:
            lk.append(np.mean(Lm))
            ks.append(k)
    if len(ks) < 2:
        return np.nan
    return float(-np.polyfit(np.log(ks), np.log(np.maximum(lk, _EPS)), 1)[0])


def _katz_fd(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    diffs = np.diff(x)
    L = np.sum(np.abs(diffs))
    d = np.max(np.abs(x - x[0]))
    if L < _EPS or d < _EPS:
        return np.nan
    avg_step = L / (n - 1)
    return float(np.log10(n) / (np.log10(d / avg_step) + np.log10(n) + _EPS))


def _autocorr_lag1(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 4:
        return np.nan
    xm = x - x.mean()
    denom = np.sum(xm ** 2)
    if denom < _EPS:
        return np.nan
    return float(np.dot(xm[:-1], xm[1:]) / denom)


def _variance_ratio(x: np.ndarray, q: int = 5) -> float:
    x = x[~np.isnan(x)]
    n = len(x)
    if n < q + 4:
        return np.nan
    var1 = np.var(x, ddof=1)
    if var1 < _EPS:
        return np.nan
    agg = np.array([x[i:i + q].sum() for i in range(n - q + 1)])
    varq = np.var(agg, ddof=1)
    return float(varq / (q * var1 + _EPS))


def _rolling_hurst_rs(close: pd.Series, w: int) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _hurst_rs(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_dfa(close: pd.Series, w: int, scales: list) -> pd.Series:
    lr = np.log(close / close.shift(1))
    sc = scales
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _dfa_alpha(np.asarray(x, dtype=float), sc), raw=True
    )


def _rolling_higuchi(close: pd.Series, w: int) -> pd.Series:
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _higuchi_fd(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_katz(close: pd.Series, w: int) -> pd.Series:
    lp = np.log(close.clip(lower=_EPS))
    return lp.rolling(w, min_periods=w // 2).apply(
        lambda x: _katz_fd(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_autocorr1(close: pd.Series, w: int) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _autocorr_lag1(np.asarray(x, dtype=float)), raw=True
    )


def _rolling_vr(close: pd.Series, w: int, q: int) -> pd.Series:
    lr = np.log(close / close.shift(1))
    return lr.rolling(w, min_periods=w // 2).apply(
        lambda x: _variance_ratio(np.asarray(x, dtype=float), q), raw=True
    )


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def fct_drv3_001_hurst_rs_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d R/S Hurst (acceleration of Hurst velocity)."""
    vel = _rolling_hurst_rs(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_002_hurst_rs_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63d R/S Hurst (jerk in monthly Hurst)."""
    vel21 = _rolling_hurst_rs(close, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fct_drv3_003_dfa_alpha_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d DFA alpha (acceleration of DFA velocity)."""
    vel = _rolling_dfa(close, _TD_QTR, [4, 8, 16]).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_004_dfa_alpha_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day DFA velocity (jerk in monthly DFA change)."""
    vel21 = _rolling_dfa(close, _TD_QTR, [4, 8, 16]).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fct_drv3_005_higuchi_fd_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d Higuchi FD (acceleration of roughness velocity)."""
    vel = _rolling_higuchi(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_006_higuchi_fd_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63d Higuchi FD."""
    vel21 = _rolling_higuchi(close, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fct_drv3_007_katz_fd_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d Katz FD (acceleration of Katz roughness velocity)."""
    vel = _rolling_katz(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_008_autocorr_lag1_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d autocorrelation (acceleration of texture change)."""
    vel = _rolling_autocorr1(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_009_variance_ratio_5_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of VR(5,63d) (acceleration of variance-ratio change)."""
    vel = _rolling_vr(close, _TD_QTR, 5).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_010_variance_ratio_5_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day VR(5,63d) velocity."""
    vel21 = _rolling_vr(close, _TD_QTR, 5).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fct_drv3_011_logret_roughness_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d log-return roughness (roughness acceleration)."""
    lr = np.log(close / close.shift(1))
    r21 = lr.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    vel = r21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_012_logret_roughness_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d log-return roughness."""
    lr = np.log(close / close.shift(1))
    r63 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()
    vel = r63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_013_hurst_rs_63d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d OLS slope of the 63d R/S Hurst series."""
    slope = _linslope(_rolling_hurst_rs(close, _TD_QTR), _TD_MON)
    return slope.diff(_TD_WEEK)


def fct_drv3_014_dfa_alpha_63d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d OLS slope of the 63d DFA alpha series."""
    slope = _linslope(_rolling_dfa(close, _TD_QTR, [4, 8, 16]), _TD_MON)
    return slope.diff(_TD_WEEK)


def fct_drv3_015_higuchi_fd_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d Higuchi FD (acceleration of short-window roughness)."""
    vel = _rolling_higuchi(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_016_autocorr_lag1_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d lag-1 autocorrelation."""
    vel = _rolling_autocorr1(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_017_hurst_rs_dfa_spread_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (R/S Hurst minus DFA alpha) spread over 63d."""
    spread = _rolling_hurst_rs(close, _TD_QTR) - _rolling_dfa(close, _TD_QTR, [4, 8, 16])
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_018_katz_fd_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63d Katz FD."""
    vel21 = _rolling_katz(close, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fct_drv3_019_hurst_rs_63d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 63d R/S Hurst."""
    vel = _rolling_hurst_rs(close, _TD_QTR).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def fct_drv3_020_dfa_alpha_63d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 63d DFA alpha."""
    vel = _rolling_dfa(close, _TD_QTR, [4, 8, 16]).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def fct_drv3_021_variance_ratio_5_63d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of VR(5,63d)."""
    vel = _rolling_vr(close, _TD_QTR, 5).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def fct_drv3_022_autocorr_lag1_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63d autocorrelation."""
    vel21 = _rolling_autocorr1(close, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def fct_drv3_023_roughness_ratio_21d_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of the 21d/63d roughness ratio."""
    lr = np.log(close / close.shift(1))
    r21 = lr.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    r63 = lr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()
    ratio = r21 / r63.replace(0, np.nan)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_024_hurst_rs_126d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126d R/S Hurst (acceleration of medium-window Hurst)."""
    vel = _rolling_hurst_rs(close, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def fct_drv3_025_hurst_rs_63d_depth_below05_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d R/S Hurst depth below 0.5 (anti-persistence jerk)."""
    depth = (0.5 - _rolling_hurst_rs(close, _TD_QTR)).clip(lower=0.0)
    vel = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

FRACTAL_STRUCTURE_REGISTRY_3RD_DERIVATIVES = {
    "fct_drv3_001_hurst_rs_63d_5d_diff_5d_diff":           {"inputs": ["close"], "func": fct_drv3_001_hurst_rs_63d_5d_diff_5d_diff},
    "fct_drv3_002_hurst_rs_63d_21d_diff_5d_diff":          {"inputs": ["close"], "func": fct_drv3_002_hurst_rs_63d_21d_diff_5d_diff},
    "fct_drv3_003_dfa_alpha_63d_5d_diff_5d_diff":          {"inputs": ["close"], "func": fct_drv3_003_dfa_alpha_63d_5d_diff_5d_diff},
    "fct_drv3_004_dfa_alpha_63d_21d_diff_5d_diff":         {"inputs": ["close"], "func": fct_drv3_004_dfa_alpha_63d_21d_diff_5d_diff},
    "fct_drv3_005_higuchi_fd_63d_5d_diff_5d_diff":         {"inputs": ["close"], "func": fct_drv3_005_higuchi_fd_63d_5d_diff_5d_diff},
    "fct_drv3_006_higuchi_fd_63d_21d_diff_5d_diff":        {"inputs": ["close"], "func": fct_drv3_006_higuchi_fd_63d_21d_diff_5d_diff},
    "fct_drv3_007_katz_fd_63d_5d_diff_5d_diff":            {"inputs": ["close"], "func": fct_drv3_007_katz_fd_63d_5d_diff_5d_diff},
    "fct_drv3_008_autocorr_lag1_63d_5d_diff_5d_diff":      {"inputs": ["close"], "func": fct_drv3_008_autocorr_lag1_63d_5d_diff_5d_diff},
    "fct_drv3_009_variance_ratio_5_63d_5d_diff_5d_diff":   {"inputs": ["close"], "func": fct_drv3_009_variance_ratio_5_63d_5d_diff_5d_diff},
    "fct_drv3_010_variance_ratio_5_63d_21d_diff_5d_diff":  {"inputs": ["close"], "func": fct_drv3_010_variance_ratio_5_63d_21d_diff_5d_diff},
    "fct_drv3_011_logret_roughness_21d_5d_diff_5d_diff":   {"inputs": ["close"], "func": fct_drv3_011_logret_roughness_21d_5d_diff_5d_diff},
    "fct_drv3_012_logret_roughness_63d_5d_diff_5d_diff":   {"inputs": ["close"], "func": fct_drv3_012_logret_roughness_63d_5d_diff_5d_diff},
    "fct_drv3_013_hurst_rs_63d_slope_21d_5d_diff":         {"inputs": ["close"], "func": fct_drv3_013_hurst_rs_63d_slope_21d_5d_diff},
    "fct_drv3_014_dfa_alpha_63d_slope_21d_5d_diff":        {"inputs": ["close"], "func": fct_drv3_014_dfa_alpha_63d_slope_21d_5d_diff},
    "fct_drv3_015_higuchi_fd_21d_5d_diff_5d_diff":         {"inputs": ["close"], "func": fct_drv3_015_higuchi_fd_21d_5d_diff_5d_diff},
    "fct_drv3_016_autocorr_lag1_21d_5d_diff_5d_diff":      {"inputs": ["close"], "func": fct_drv3_016_autocorr_lag1_21d_5d_diff_5d_diff},
    "fct_drv3_017_hurst_rs_dfa_spread_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": fct_drv3_017_hurst_rs_dfa_spread_63d_5d_diff_5d_diff},
    "fct_drv3_018_katz_fd_63d_21d_diff_5d_diff":           {"inputs": ["close"], "func": fct_drv3_018_katz_fd_63d_21d_diff_5d_diff},
    "fct_drv3_019_hurst_rs_63d_5d_diff_slope_21d":         {"inputs": ["close"], "func": fct_drv3_019_hurst_rs_63d_5d_diff_slope_21d},
    "fct_drv3_020_dfa_alpha_63d_5d_diff_slope_21d":        {"inputs": ["close"], "func": fct_drv3_020_dfa_alpha_63d_5d_diff_slope_21d},
    "fct_drv3_021_variance_ratio_5_63d_5d_diff_slope_21d": {"inputs": ["close"], "func": fct_drv3_021_variance_ratio_5_63d_5d_diff_slope_21d},
    "fct_drv3_022_autocorr_lag1_63d_21d_diff_5d_diff":     {"inputs": ["close"], "func": fct_drv3_022_autocorr_lag1_63d_21d_diff_5d_diff},
    "fct_drv3_023_roughness_ratio_21d_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": fct_drv3_023_roughness_ratio_21d_63d_5d_diff_5d_diff},
    "fct_drv3_024_hurst_rs_126d_5d_diff_5d_diff":          {"inputs": ["close"], "func": fct_drv3_024_hurst_rs_126d_5d_diff_5d_diff},
    "fct_drv3_025_hurst_rs_63d_depth_below05_5d_diff_5d_diff": {"inputs": ["close"], "func": fct_drv3_025_hurst_rs_63d_depth_below05_5d_diff_5d_diff},
}
