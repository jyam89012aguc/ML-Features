"""
Drawdown Shape — 3rd Derivatives
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

def dsh_drv3_001_drawdown_slope_252d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_001_drawdown_slope_252d_jerk"""
    h = _rolling_max(close, 252)
    dd = (close - h) / h
    slope = _rolling_slope(dd, 252)
    vel = slope.diff(5)
    return vel.diff(5)

def dsh_drv3_002_drawdown_area_ratio_63d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_002_drawdown_area_ratio_63d_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    area = dd.rolling(63).sum().abs()
    max_dd = dd.rolling(63).min().abs()
    ratio = _safe_div(area, 0.5 * max_dd * 63)
    vel = ratio.diff(5)
    return vel.diff(5)

def dsh_drv3_003_drawdown_concavity_index_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_003_drawdown_concavity_index_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    idx = _safe_div(dd.rolling(63).mean(), dd.rolling(63).min())
    vel = idx.diff(5)
    return vel.diff(5)

def dsh_drv3_004_drawdown_rsq_63d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_004_drawdown_rsq_63d_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _rsq(y):
        if len(y) < 2: return np.nan
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = dd.rolling(63).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)

def dsh_drv3_005_drawdown_curvature_63d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_005_drawdown_curvature_63d_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _poly2(y):
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = dd.rolling(63).apply(_poly2, raw=True)
    vel = curv.diff(5)
    return vel.diff(5)

def dsh_drv3_006_drawdown_v_shape_score_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_006_drawdown_v_shape_score_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _vscore(y):
        mid = len(y) // 2
        s1 = linregress(np.arange(mid), y[:mid]).slope
        s2 = linregress(np.arange(mid), y[mid:]).slope
        return s2 - s1
    v = dd.rolling(63).apply(_vscore, raw=True)
    vel = v.diff(5)
    return vel.diff(5)

def dsh_drv3_007_waterfall_verticality_63d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_007_waterfall_verticality_63d_jerk"""
    ret = close.pct_change()
    max_drop = ret.rolling(63).min().abs()
    avg_drop = ret.rolling(63).mean().abs()
    vert = _safe_div(max_drop, avg_drop)
    vel = vert.diff(5)
    return vel.diff(5)

def dsh_drv3_008_drawdown_skewness_63d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_008_drawdown_skewness_63d_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    vel = dd.rolling(63).skew().diff(5)
    return vel.diff(5)

def dsh_drv3_009_drawdown_symmetry_ratio_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_009_drawdown_symmetry_ratio_jerk"""
    h = _rolling_max(close, 63)
    in_dd = close < h
    ret = close.pct_change()
    up = ((ret > 0) & in_dd).rolling(63).sum()
    down = ((ret < 0) & in_dd).rolling(63).sum()
    sym = _safe_div(down, up)
    vel = sym.diff(5)
    return vel.diff(5)

def dsh_drv3_010_drawdown_jaggedness_21d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_010_drawdown_jaggedness_21d_jerk"""
    h = _rolling_max(close, 21)
    dd = (close - h) / h
    path_len = dd.diff().abs().rolling(21).sum()
    net_depth = dd.diff(21).abs()
    jag = _safe_div(path_len, net_depth)
    vel = jag.diff(5)
    return vel.diff(5)

def dsh_drv3_011_drawdown_entropy_63d_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_011_drawdown_entropy_63d_jerk"""
    ret = close.pct_change()
    def _entropy(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
    ent = ret.rolling(63).apply(_entropy, raw=True)
    vel = ent.diff(5)
    return vel.diff(5)

def dsh_drv3_012_mktcap_drawdown_slope_63d_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dsh_drv3_012_mktcap_drawdown_slope_63d_jerk"""
    mc = close * sharesbas
    h = _rolling_max(mc, 63)
    dd = (mc - h) / h
    slope = _rolling_slope(dd, 63)
    vel = slope.diff(5)
    return vel.diff(5)

def dsh_drv3_013_drawdown_log_decay_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_013_drawdown_log_decay_jerk"""
    h = _rolling_max(close, 63)
    dd = (h - close) / h + 0.01
    def _decay(y):
        return linregress(np.arange(len(y)), np.log(y)).slope
    dec = dd.rolling(63).apply(_decay, raw=True)
    vel = dec.diff(5)
    return vel.diff(5)

def dsh_drv3_014_drawdown_rounded_top_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_014_drawdown_rounded_top_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _top(y):
        coeffs = np.polyfit(np.arange(len(y)), y, 2)
        return -coeffs[0] if coeffs[0] < 0 else 0
    top = dd.rolling(63).apply(_top, raw=True)
    vel = top.diff(5)
    return vel.diff(5)

def dsh_drv3_015_drawdown_terminal_slope_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_015_drawdown_terminal_slope_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    slope = _rolling_slope(dd, 10)
    vel = slope.diff(5)
    return vel.diff(5)

def dsh_drv3_016_drawdown_hump_score_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_016_drawdown_hump_score_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _hump(y):
        lin = np.linspace(y[0], y[-1], len(y))
        return np.mean(y - lin)
    hump = dd.rolling(63).apply(_hump, raw=True)
    vel = hump.diff(5)
    return vel.diff(5)

def dsh_drv3_017_drawdown_bow_factor_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_017_drawdown_bow_factor_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    bow = dd.rolling(63).median() - dd.rolling(63).mean()
    vel = bow.diff(5)
    return vel.diff(5)

def dsh_drv3_018_drawdown_vol_ratio_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_018_drawdown_vol_ratio_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _vol_ratio(y):
        mid = len(y) // 2
        return _safe_div(pd.Series(np.std(y[mid:])), pd.Series(np.std(y[:mid]))).iloc[0]
    vr = dd.rolling(63).apply(_vol_ratio, raw=True)
    vel = vr.diff(5)
    return vel.diff(5)

def dsh_drv3_019_drawdown_max_residual_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_019_drawdown_max_residual_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _max_res(y):
        res = linregress(np.arange(len(y)), y)
        y_fit = res.intercept + res.slope * np.arange(len(y))
        return np.max(np.abs(y - y_fit))
    mr = dd.rolling(63).apply(_max_res, raw=True)
    vel = mr.diff(5)
    return vel.diff(5)

def dsh_drv3_020_drawdown_step_verticality_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_020_drawdown_step_verticality_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    diff = dd.diff()
    vertical = diff.where(diff < diff.rolling(63).mean() - 1*diff.rolling(63).std())
    sv = vertical.rolling(63).mean()
    vel = sv.diff(5)
    return vel.diff(5)

def dsh_drv3_021_drawdown_autocorr_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_021_drawdown_autocorr_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    ac = dd.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    vel = ac.diff(5)
    return vel.diff(5)

def dsh_drv3_022_drawdown_parabolic_accel_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_022_drawdown_parabolic_accel_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _para(y):
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    pa = dd.rolling(63).apply(_para, raw=True)
    vel = pa.diff(5)
    return vel.diff(5)

def dsh_drv3_023_drawdown_shape_complexity_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_023_drawdown_shape_complexity_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _stderr(y):
        return linregress(np.arange(len(y)), y).stderr
    def _rsq(y):
        return linregress(np.arange(len(y)), y).rvalue**2
    se = dd.rolling(63).apply(_stderr, raw=True)
    r2 = dd.rolling(63).apply(_rsq, raw=True)
    comp = se * (1.0 - r2)
    vel = comp.diff(5)
    return vel.diff(5)

def dsh_drv3_024_drawdown_acceleration_of_slope_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_024_drawdown_acceleration_of_slope_jerk"""
    slope = _rolling_slope((close - _rolling_max(close, 21)) / _rolling_max(close, 21), 21)
    accel = slope.diff(5)
    return accel.diff(5)

def dsh_drv3_025_drawdown_velocity_inflection_jerk(close: pd.Series) -> pd.Series:
    """dsh_drv3_025_drawdown_velocity_inflection_jerk"""
    h = _rolling_max(close, 63)
    dd = (close - h) / h
    def _inflection(y):
        coeffs = np.polyfit(np.arange(len(y)), y, 2)
        return np.sign(coeffs[0])
    inf = dd.rolling(63).apply(_inflection, raw=True)
    vel = inf.diff(5)
    return vel.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V03_A_REGISTRY = {
    "dsh_drv3_001_drawdown_slope_252d_jerk": {"inputs": ["close"], "func": dsh_drv3_001_drawdown_slope_252d_jerk},
    "dsh_drv3_002_drawdown_area_ratio_63d_jerk": {"inputs": ["close"], "func": dsh_drv3_002_drawdown_area_ratio_63d_jerk},
    "dsh_drv3_003_drawdown_concavity_index_jerk": {"inputs": ["close"], "func": dsh_drv3_003_drawdown_concavity_index_jerk},
    "dsh_drv3_004_drawdown_rsq_63d_jerk": {"inputs": ["close"], "func": dsh_drv3_004_drawdown_rsq_63d_jerk},
    "dsh_drv3_005_drawdown_curvature_63d_jerk": {"inputs": ["close"], "func": dsh_drv3_005_drawdown_curvature_63d_jerk},
    "dsh_drv3_006_drawdown_v_shape_score_jerk": {"inputs": ["close"], "func": dsh_drv3_006_drawdown_v_shape_score_jerk},
    "dsh_drv3_007_waterfall_verticality_63d_jerk": {"inputs": ["close"], "func": dsh_drv3_007_waterfall_verticality_63d_jerk},
    "dsh_drv3_008_drawdown_skewness_63d_jerk": {"inputs": ["close"], "func": dsh_drv3_008_drawdown_skewness_63d_jerk},
    "dsh_drv3_009_drawdown_symmetry_ratio_jerk": {"inputs": ["close"], "func": dsh_drv3_009_drawdown_symmetry_ratio_jerk},
    "dsh_drv3_010_drawdown_jaggedness_21d_jerk": {"inputs": ["close"], "func": dsh_drv3_010_drawdown_jaggedness_21d_jerk},
    "dsh_drv3_011_drawdown_entropy_63d_jerk": {"inputs": ["close"], "func": dsh_drv3_011_drawdown_entropy_63d_jerk},
    "dsh_drv3_012_mktcap_drawdown_slope_63d_jerk": {"inputs": ["close", "sharesbas"], "func": dsh_drv3_012_mktcap_drawdown_slope_63d_jerk},
    "dsh_drv3_013_drawdown_log_decay_jerk": {"inputs": ["close"], "func": dsh_drv3_013_drawdown_log_decay_jerk},
    "dsh_drv3_014_drawdown_rounded_top_jerk": {"inputs": ["close"], "func": dsh_drv3_014_drawdown_rounded_top_jerk},
    "dsh_drv3_015_drawdown_terminal_slope_jerk": {"inputs": ["close"], "func": dsh_drv3_015_drawdown_terminal_slope_jerk},
    "dsh_drv3_016_drawdown_hump_score_jerk": {"inputs": ["close"], "func": dsh_drv3_016_drawdown_hump_score_jerk},
    "dsh_drv3_017_drawdown_bow_factor_jerk": {"inputs": ["close"], "func": dsh_drv3_017_drawdown_bow_factor_jerk},
    "dsh_drv3_018_drawdown_vol_ratio_jerk": {"inputs": ["close"], "func": dsh_drv3_018_drawdown_vol_ratio_jerk},
    "dsh_drv3_019_drawdown_max_residual_jerk": {"inputs": ["close"], "func": dsh_drv3_019_drawdown_max_residual_jerk},
    "dsh_drv3_020_drawdown_step_verticality_jerk": {"inputs": ["close"], "func": dsh_drv3_020_drawdown_step_verticality_jerk},
    "dsh_drv3_021_drawdown_autocorr_jerk": {"inputs": ["close"], "func": dsh_drv3_021_drawdown_autocorr_jerk},
    "dsh_drv3_022_drawdown_parabolic_accel_jerk": {"inputs": ["close"], "func": dsh_drv3_022_drawdown_parabolic_accel_jerk},
    "dsh_drv3_023_drawdown_shape_complexity_jerk": {"inputs": ["close"], "func": dsh_drv3_023_drawdown_shape_complexity_jerk},
    "dsh_drv3_024_drawdown_acceleration_of_slope_jerk": {"inputs": ["close"], "func": dsh_drv3_024_drawdown_acceleration_of_slope_jerk},
    "dsh_drv3_025_drawdown_velocity_inflection_jerk": {"inputs": ["close"], "func": dsh_drv3_025_drawdown_velocity_inflection_jerk},
}
