"""
Drawdown Velocity — 3rd Derivatives
Domain: speed and momentum of decline
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

def dvel_drv3_001_log_velocity_21d_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_001_log_velocity_21d_jerk"""
    v = np.log(close).diff(5) / 5.0
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_002_drawdown_velocity_252d_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_002_drawdown_velocity_252d_jerk"""
    h = close.rolling(252).max()
    dd = (close - h) / h
    dsh = close.rolling(252).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)
    v = _safe_div(dd, dsh)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_003_terminal_velocity_10d_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_003_terminal_velocity_10d_jerk"""
    v = _rolling_slope(np.log(close), 10)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_004_sigma_velocity_21d_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_004_sigma_velocity_21d_jerk"""
    ret = np.log(close).diff(21)
    vol = close.pct_change().rolling(21).std() * np.sqrt(21)
    v = _safe_div(ret, vol)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_005_volume_weighted_velocity_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dvel_drv3_005_volume_weighted_velocity_jerk"""
    v = np.log(close).diff(5)
    v_norm = _safe_div(volume, volume.rolling(21).mean())
    wv = (v * v_norm).rolling(21).mean()
    accel = wv.diff(5)
    return accel.diff(5)

def dvel_drv3_006_mktcap_velocity_63d_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dvel_drv3_006_mktcap_velocity_63d_jerk"""
    mc = close * sharesbas
    v = np.log(mc).diff(21)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_007_velocity_persistence_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_007_velocity_persistence_jerk"""
    v5 = np.log(close).diff(5)
    per = (v5 < 0).rolling(63).mean()
    accel = per.diff(5)
    return accel.diff(5)

def dvel_drv3_008_velocity_skewness_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_008_velocity_skewness_jerk"""
    v5 = np.log(close).diff(5)
    skew = v5.rolling(63).skew()
    accel = skew.diff(5)
    return accel.diff(5)

def dvel_drv3_009_velocity_oscillation_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_009_velocity_oscillation_jerk"""
    v5 = np.log(close).diff(5)
    osc = _safe_div(v5.rolling(63).std(), v5.rolling(63).mean().abs())
    accel = osc.diff(5)
    return accel.diff(5)

def dvel_drv3_010_ema_velocity_21d_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_010_ema_velocity_21d_jerk"""
    ema = close.ewm(span=21).mean()
    v = np.log(ema).diff(5)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_011_velocity_to_atr_ratio_jerk(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dvel_drv3_011_velocity_to_atr_ratio_jerk"""
    v = np.log(close).diff(21).abs()
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(63).mean() / close.rolling(63).mean()
    ratio = _safe_div(v, atr)
    accel = ratio.diff(5)
    return accel.diff(5)

def dvel_drv3_012_terminal_velocity_decay_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_012_terminal_velocity_decay_jerk"""
    score = _rolling_slope(np.log(close), 5) - _rolling_slope(np.log(close), 21)
    accel = score.diff(5)
    return accel.diff(5)

def dvel_drv3_013_velocity_entropy_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_013_velocity_entropy_jerk"""
    v = close.pct_change()
    def _entropy(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
    ent = v.rolling(63).apply(_entropy, raw=True)
    accel = ent.diff(5)
    return accel.diff(5)

def dvel_drv3_014_velocity_gradient_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_014_velocity_gradient_jerk"""
    v = np.log(close).diff(5)
    grad = _rolling_slope(v, 63)
    accel = grad.diff(5)
    return accel.diff(5)

def dvel_drv3_015_harmonic_velocity_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_015_harmonic_velocity_jerk"""
    ret = close.pct_change() + 1.0
    def _harm(y):
        return len(y) / np.sum(1.0 / y) - 1.0
    hv = ret.rolling(63).apply(_harm, raw=True)
    accel = hv.diff(5)
    return accel.diff(5)

def dvel_drv3_016_log_price_rsq_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_016_log_price_rsq_jerk"""
    def _rsq(y):
        if len(y) < 2: return np.nan
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = np.log(close).rolling(63).apply(_rsq, raw=True)
    accel = r2.diff(5)
    return accel.diff(5)

def dvel_drv3_017_velocity_jump_ratio_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_017_velocity_jump_ratio_jerk"""
    v = np.log(close).diff(1).abs()
    ratio = _safe_div(v, v.rolling(21).max())
    accel = ratio.diff(5)
    return accel.diff(5)

def dvel_drv3_018_velocity_at_earnings_surprise_jerk(close: pd.Series, surprise: pd.Series) -> pd.Series:
    """dvel_drv3_018_velocity_at_earnings_surprise_jerk"""
    v = np.log(close).diff(5)
    ves = v.where(surprise.abs() > 0).ffill()
    accel = ves.diff(5)
    return accel.diff(5)

def dvel_drv3_019_mktcap_to_price_velocity_ratio_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dvel_drv3_019_mktcap_to_price_velocity_ratio_jerk"""
    v_p = np.log(close).diff(21)
    v_mc = np.log(close * sharesbas).diff(21)
    ratio = _safe_div(v_mc, v_p)
    accel = ratio.diff(5)
    return accel.diff(5)

def dvel_drv3_020_negative_velocity_intensity_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_020_negative_velocity_intensity_jerk"""
    v = np.log(close).diff(1)
    neg_v = v.where(v < 0)
    intense = neg_v.rolling(21).sum()
    accel = intense.diff(5)
    return accel.diff(5)

def dvel_drv3_021_velocity_climax_score_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_021_velocity_climax_score_jerk"""
    v = np.log(close).diff(5).abs()
    v_norm = _safe_div(v - v.rolling(63).mean(), v.rolling(63).std())
    r = (close.expanding().max() - close.expanding().min()) / close.expanding().max()
    score = v_norm * r
    accel = score.diff(5)
    return accel.diff(5)

def dvel_drv3_022_days_in_high_velocity_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_022_days_in_high_velocity_jerk"""
    v = np.log(close).diff(5).abs()
    threshold = v.rolling(252).mean() + 1.5 * v.rolling(252).std()
    days = (v > threshold).rolling(63).sum()
    accel = days.diff(5)
    return accel.diff(5)

def dvel_drv3_023_velocity_autocorr_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_023_velocity_autocorr_jerk"""
    v5 = np.log(close).diff(5)
    ac = v5.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    accel = ac.diff(5)
    return accel.diff(5)

def dvel_drv3_024_velocity_residual_std_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_024_velocity_residual_std_jerk"""
    def _res_std(y):
        x = np.arange(len(y))
        res = linregress(x, y)
        y_fit = res.intercept + res.slope * x
        return np.std(y - y_fit)
    rs = np.log(close).rolling(63).apply(_res_std, raw=True)
    accel = rs.diff(5)
    return accel.diff(5)

def dvel_drv3_025_velocity_composite_momentum_jerk(close: pd.Series) -> pd.Series:
    """dvel_drv3_025_velocity_composite_momentum_jerk"""
    v5 = np.log(close).diff(5) / 5.0
    v21 = np.log(close).diff(21) / 21.0
    v63 = np.log(close).diff(63) / 63.0
    comp = (0.5 * v5 + 0.3 * v21 + 0.2 * v63)
    accel = comp.diff(5)
    return accel.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V04_A_REGISTRY = {
    "dvel_drv3_001_log_velocity_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_001_log_velocity_21d_jerk},
    "dvel_drv3_002_drawdown_velocity_252d_jerk": {"inputs": ["close"], "func": dvel_drv3_002_drawdown_velocity_252d_jerk},
    "dvel_drv3_003_terminal_velocity_10d_jerk": {"inputs": ["close"], "func": dvel_drv3_003_terminal_velocity_10d_jerk},
    "dvel_drv3_004_sigma_velocity_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_004_sigma_velocity_21d_jerk},
    "dvel_drv3_005_volume_weighted_velocity_jerk": {"inputs": ["close", "volume"], "func": dvel_drv3_005_volume_weighted_velocity_jerk},
    "dvel_drv3_006_mktcap_velocity_63d_jerk": {"inputs": ["close", "sharesbas"], "func": dvel_drv3_006_mktcap_velocity_63d_jerk},
    "dvel_drv3_007_velocity_persistence_jerk": {"inputs": ["close"], "func": dvel_drv3_007_velocity_persistence_jerk},
    "dvel_drv3_008_velocity_skewness_jerk": {"inputs": ["close"], "func": dvel_drv3_008_velocity_skewness_jerk},
    "dvel_drv3_009_velocity_oscillation_jerk": {"inputs": ["close"], "func": dvel_drv3_009_velocity_oscillation_jerk},
    "dvel_drv3_010_ema_velocity_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_010_ema_velocity_21d_jerk},
    "dvel_drv3_011_velocity_to_atr_ratio_jerk": {"inputs": ["close", "high", "low"], "func": dvel_drv3_011_velocity_to_atr_ratio_jerk},
    "dvel_drv3_012_terminal_velocity_decay_jerk": {"inputs": ["close"], "func": dvel_drv3_012_terminal_velocity_decay_jerk},
    "dvel_drv3_013_velocity_entropy_jerk": {"inputs": ["close"], "func": dvel_drv3_013_velocity_entropy_jerk},
    "dvel_drv3_014_velocity_gradient_jerk": {"inputs": ["close"], "func": dvel_drv3_014_velocity_gradient_jerk},
    "dvel_drv3_015_harmonic_velocity_jerk": {"inputs": ["close"], "func": dvel_drv3_015_harmonic_velocity_jerk},
    "dvel_drv3_016_log_price_rsq_jerk": {"inputs": ["close"], "func": dvel_drv3_016_log_price_rsq_jerk},
    "dvel_drv3_017_velocity_jump_ratio_jerk": {"inputs": ["close"], "func": dvel_drv3_017_velocity_jump_ratio_jerk},
    "dvel_drv3_018_velocity_at_earnings_surprise_jerk": {"inputs": ["close", "surprise"], "func": dvel_drv3_018_velocity_at_earnings_surprise_jerk},
    "dvel_drv3_019_mktcap_to_price_velocity_ratio_jerk": {"inputs": ["close", "sharesbas"], "func": dvel_drv3_019_mktcap_to_price_velocity_ratio_jerk},
    "dvel_drv3_020_negative_velocity_intensity_jerk": {"inputs": ["close"], "func": dvel_drv3_020_negative_velocity_intensity_jerk},
    "dvel_drv3_021_velocity_climax_score_jerk": {"inputs": ["close"], "func": dvel_drv3_021_velocity_climax_score_jerk},
    "dvel_drv3_022_days_in_high_velocity_jerk": {"inputs": ["close"], "func": dvel_drv3_022_days_in_high_velocity_jerk},
    "dvel_drv3_023_velocity_autocorr_jerk": {"inputs": ["close"], "func": dvel_drv3_023_velocity_autocorr_jerk},
    "dvel_drv3_024_velocity_residual_std_jerk": {"inputs": ["close"], "func": dvel_drv3_024_velocity_residual_std_jerk},
    "dvel_drv3_025_velocity_composite_momentum_jerk": {"inputs": ["close"], "func": dvel_drv3_025_velocity_composite_momentum_jerk},
}
