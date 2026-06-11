"""
Drawdown Shape — 2nd Derivatives
Domain: shape and convexity of decline
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def dsh_drv2_001_drawdown_slope_252d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_001_drawdown_slope_252d_velocity"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    slope = _rolling_slope(dd, 252)
    return slope.diff(5)

def dsh_drv2_002_drawdown_area_ratio_63d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_002_drawdown_area_ratio_63d_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    area = dd.rolling(63).sum().abs()
    max_dd = dd.rolling(63).min().abs()
    ratio = _safe_div(area, 0.5 * max_dd * 63)
    return ratio.diff(5)

def dsh_drv2_003_drawdown_concavity_index_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_003_drawdown_concavity_index_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    idx = _safe_div(dd.rolling(63).mean(), dd.rolling(63).min())
    return idx.diff(5)

def dsh_drv2_004_drawdown_rsq_63d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_004_drawdown_rsq_63d_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _rsq(y):
        if len(y) < 2: return np.nan
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = dd.rolling(63).apply(_rsq, raw=True)
    return r2.diff(5)

def dsh_drv2_005_drawdown_curvature_63d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_005_drawdown_curvature_63d_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _poly2(y):
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = dd.rolling(63).apply(_poly2, raw=True)
    return curv.diff(5)

def dsh_drv2_006_drawdown_v_shape_score_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_006_drawdown_v_shape_score_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _vscore(y):
        mid = len(y) // 2
        s1 = linregress(np.arange(mid), y[:mid]).slope
        s2 = linregress(np.arange(mid), y[mid:]).slope
        return s2 - s1
    v = dd.rolling(63).apply(_vscore, raw=True)
    return v.diff(5)

def dsh_drv2_007_waterfall_verticality_63d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_007_waterfall_verticality_63d_velocity"""
    ret = close.pct_change()
    max_drop = ret.rolling(63).min().abs()
    avg_drop = ret.rolling(63).mean().abs()
    vert = _safe_div(max_drop, avg_drop)
    return vert.diff(5)

def dsh_drv2_008_drawdown_skewness_63d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_008_drawdown_skewness_63d_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    return dd.rolling(63).skew().diff(5)

def dsh_drv2_009_drawdown_symmetry_ratio_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_009_drawdown_symmetry_ratio_velocity"""
    h = _rolling_max(close, 63)
    in_dd = close < h
    ret = close.pct_change()
    up = ((ret > 0) & in_dd).rolling(63).sum()
    down = ((ret < 0) & in_dd).rolling(63).sum()
    sym = _safe_div(down, up)
    return sym.diff(5)

def dsh_drv2_010_drawdown_jaggedness_21d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_010_drawdown_jaggedness_21d_velocity"""
    h = _rolling_max(close, 21)
    dd = (close - h) / h
    path_len = dd.diff().abs().rolling(21).sum()
    net_depth = dd.diff(21).abs()
    jag = _safe_div(path_len, net_depth)
    return jag.diff(5)

def dsh_drv2_011_drawdown_entropy_63d_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_011_drawdown_entropy_63d_velocity"""
    ret = close.pct_change()
    def _entropy(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
    ent = ret.rolling(63).apply(_entropy, raw=True)
    return ent.diff(5)

def dsh_drv2_012_mktcap_drawdown_slope_63d_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dsh_drv2_012_mktcap_drawdown_slope_63d_velocity"""
    mc = close * sharesbas
    h = _rolling_max(mc, 63)
    dd = (mc - h) / h
    slope = _rolling_slope(dd, 63)
    return slope.diff(5)

def dsh_drv2_013_drawdown_log_decay_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_013_drawdown_log_decay_velocity"""
    h = _rolling_max(close, 63)
    dd = (h - close) / h + 0.01
    def _decay(y):
        return linregress(np.arange(len(y)), np.log(y)).slope
    dec = dd.rolling(63).apply(_decay, raw=True)
    return dec.diff(5)

def dsh_drv2_014_drawdown_rounded_top_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_014_drawdown_rounded_top_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _top(y):
        coeffs = np.polyfit(np.arange(len(y)), y, 2)
        return -coeffs[0] if coeffs[0] < 0 else 0
    top = dd.rolling(63).apply(_top, raw=True)
    return top.diff(5)

def dsh_drv2_015_drawdown_terminal_slope_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_015_drawdown_terminal_slope_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    slope = _rolling_slope(dd, 10)
    return slope.diff(5)

def dsh_drv2_016_drawdown_hump_score_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_016_drawdown_hump_score_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _hump(y):
        lin = np.linspace(y[0], y[-1], len(y))
        return np.mean(y - lin)
    hump = dd.rolling(63).apply(_hump, raw=True)
    return hump.diff(5)

def dsh_drv2_017_drawdown_bow_factor_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_017_drawdown_bow_factor_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    bow = dd.rolling(63).median() - dd.rolling(63).mean()
    return bow.diff(5)

def dsh_drv2_018_drawdown_vol_ratio_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_018_drawdown_vol_ratio_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _vol_ratio(y):
        mid = len(y) // 2
        return _safe_div(pd.Series(np.std(y[mid:])), pd.Series(np.std(y[:mid]))).iloc[0]
    vr = dd.rolling(63).apply(_vol_ratio, raw=True)
    return vr.diff(5)

def dsh_drv2_019_drawdown_max_residual_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_019_drawdown_max_residual_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _max_res(y):
        res = linregress(np.arange(len(y)), y)
        y_fit = res.intercept + res.slope * np.arange(len(y))
        return np.max(np.abs(y - y_fit))
    mr = dd.rolling(63).apply(_max_res, raw=True)
    return mr.diff(5)

def dsh_drv2_020_drawdown_step_verticality_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_020_drawdown_step_verticality_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    diff = dd.diff()
    vertical = diff.where(diff < diff.rolling(63).mean() - 1*diff.rolling(63).std())
    sv = vertical.rolling(63).mean()
    return sv.diff(5)

def dsh_drv2_021_drawdown_autocorr_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_021_drawdown_autocorr_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    ac = dd.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(5)

def dsh_drv2_022_drawdown_parabolic_accel_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_022_drawdown_parabolic_accel_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _para(y):
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    pa = dd.rolling(63).apply(_para, raw=True)
    return pa.diff(5)

def dsh_drv2_023_drawdown_shape_complexity_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_023_drawdown_shape_complexity_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _stderr(y):
        return linregress(np.arange(len(y)), y).stderr
    def _rsq(y):
        return linregress(np.arange(len(y)), y).rvalue**2
    se = dd.rolling(63).apply(_stderr, raw=True)
    r2 = dd.rolling(63).apply(_rsq, raw=True)
    jag = dsh_drv2_010_drawdown_jaggedness_21d_velocity(close).cumsum() # proxy for raw jaggedness
    comp = se * (1.0 - r2)
    return comp.diff(5)

def dsh_drv2_024_drawdown_acceleration_of_slope_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_024_drawdown_acceleration_of_slope_velocity"""
    slope = _rolling_slope((close - _rolling_max(close, 21)) / _rolling_max(close, 21), 21)
    accel = slope.diff(5)
    return accel.diff(5)

def dsh_drv2_025_drawdown_velocity_inflection_velocity(close: pd.Series) -> pd.Series:
    """dsh_drv2_025_drawdown_velocity_inflection_velocity"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _inflection(y):
        coeffs = np.polyfit(np.arange(len(y)), y, 2)
        return np.sign(coeffs[0])
    inf = dd.rolling(63).apply(_inflection, raw=True)
    return inf.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V03_V_REGISTRY = {
    "dsh_drv2_001_drawdown_slope_252d_velocity": {"inputs": ["close"], "func": dsh_drv2_001_drawdown_slope_252d_velocity},
    "dsh_drv2_002_drawdown_area_ratio_63d_velocity": {"inputs": ["close"], "func": dsh_drv2_002_drawdown_area_ratio_63d_velocity},
    "dsh_drv2_003_drawdown_concavity_index_velocity": {"inputs": ["close"], "func": dsh_drv2_003_drawdown_concavity_index_velocity},
    "dsh_drv2_004_drawdown_rsq_63d_velocity": {"inputs": ["close"], "func": dsh_drv2_004_drawdown_rsq_63d_velocity},
    "dsh_drv2_005_drawdown_curvature_63d_velocity": {"inputs": ["close"], "func": dsh_drv2_005_drawdown_curvature_63d_velocity},
    "dsh_drv2_006_drawdown_v_shape_score_velocity": {"inputs": ["close"], "func": dsh_drv2_006_drawdown_v_shape_score_velocity},
    "dsh_drv2_007_waterfall_verticality_63d_velocity": {"inputs": ["close"], "func": dsh_drv2_007_waterfall_verticality_63d_velocity},
    "dsh_drv2_008_drawdown_skewness_63d_velocity": {"inputs": ["close"], "func": dsh_drv2_008_drawdown_skewness_63d_velocity},
    "dsh_drv2_009_drawdown_symmetry_ratio_velocity": {"inputs": ["close"], "func": dsh_drv2_009_drawdown_symmetry_ratio_velocity},
    "dsh_drv2_010_drawdown_jaggedness_21d_velocity": {"inputs": ["close"], "func": dsh_drv2_010_drawdown_jaggedness_21d_velocity},
    "dsh_drv2_011_drawdown_entropy_63d_velocity": {"inputs": ["close"], "func": dsh_drv2_011_drawdown_entropy_63d_velocity},
    "dsh_drv2_012_mktcap_drawdown_slope_63d_velocity": {"inputs": ["close", "sharesbas"], "func": dsh_drv2_012_mktcap_drawdown_slope_63d_velocity},
    "dsh_drv2_013_drawdown_log_decay_velocity": {"inputs": ["close"], "func": dsh_drv2_013_drawdown_log_decay_velocity},
    "dsh_drv2_014_drawdown_rounded_top_velocity": {"inputs": ["close"], "func": dsh_drv2_014_drawdown_rounded_top_velocity},
    "dsh_drv2_015_drawdown_terminal_slope_velocity": {"inputs": ["close"], "func": dsh_drv2_015_drawdown_terminal_slope_velocity},
    "dsh_drv2_016_drawdown_hump_score_velocity": {"inputs": ["close"], "func": dsh_drv2_016_drawdown_hump_score_velocity},
    "dsh_drv2_017_drawdown_bow_factor_velocity": {"inputs": ["close"], "func": dsh_drv2_017_drawdown_bow_factor_velocity},
    "dsh_drv2_018_drawdown_vol_ratio_velocity": {"inputs": ["close"], "func": dsh_drv2_018_drawdown_vol_ratio_velocity},
    "dsh_drv2_019_drawdown_max_residual_velocity": {"inputs": ["close"], "func": dsh_drv2_019_drawdown_max_residual_velocity},
    "dsh_drv2_020_drawdown_step_verticality_velocity": {"inputs": ["close"], "func": dsh_drv2_020_drawdown_step_verticality_velocity},
    "dsh_drv2_021_drawdown_autocorr_velocity": {"inputs": ["close"], "func": dsh_drv2_021_drawdown_autocorr_velocity},
    "dsh_drv2_022_drawdown_parabolic_accel_velocity": {"inputs": ["close"], "func": dsh_drv2_022_drawdown_parabolic_accel_velocity},
    "dsh_drv2_023_drawdown_shape_complexity_velocity": {"inputs": ["close"], "func": dsh_drv2_023_drawdown_shape_complexity_velocity},
    "dsh_drv2_024_drawdown_acceleration_of_slope_velocity": {"inputs": ["close"], "func": dsh_drv2_024_drawdown_acceleration_of_slope_velocity},
    "dsh_drv2_025_drawdown_velocity_inflection_velocity": {"inputs": ["close"], "func": dsh_drv2_025_drawdown_velocity_inflection_velocity},
}
