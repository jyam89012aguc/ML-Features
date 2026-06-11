"""
Drawdown Velocity — 2nd Derivatives
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

def dvel_drv2_001_log_velocity_21d_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_001_log_velocity_21d_accel"""
    v = np.log(close).diff(5) / 5.0
    return v.diff(5)

def dvel_drv2_002_drawdown_velocity_252d_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_002_drawdown_velocity_252d_accel"""
    h = close.rolling(252).max()
    dd = (close - h) / h
    dsh = close.rolling(252).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)
    v = _safe_div(dd, dsh)
    return v.diff(5)

def dvel_drv2_003_terminal_velocity_10d_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_003_terminal_velocity_10d_accel"""
    v = _rolling_slope(np.log(close), 10)
    return v.diff(5)

def dvel_drv2_004_sigma_velocity_21d_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_004_sigma_velocity_21d_accel"""
    ret = np.log(close).diff(21)
    vol = close.pct_change().rolling(21).std() * np.sqrt(21)
    v = _safe_div(ret, vol)
    return v.diff(5)

def dvel_drv2_005_volume_weighted_velocity_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dvel_drv2_005_volume_weighted_velocity_accel"""
    v = np.log(close).diff(5)
    v_norm = _safe_div(volume, volume.rolling(21).mean())
    wv = (v * v_norm).rolling(21).mean()
    return wv.diff(5)

def dvel_drv2_006_mktcap_velocity_63d_accel(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dvel_drv2_006_mktcap_velocity_63d_accel"""
    mc = close * sharesbas
    v = np.log(mc).diff(21)
    return v.diff(5)

def dvel_drv2_007_velocity_persistence_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_007_velocity_persistence_accel"""
    v5 = np.log(close).diff(5)
    per = (v5 < 0).rolling(63).mean()
    return per.diff(5)

def dvel_drv2_008_velocity_skewness_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_008_velocity_skewness_accel"""
    v5 = np.log(close).diff(5)
    skew = v5.rolling(63).skew()
    return skew.diff(5)

def dvel_drv2_009_velocity_oscillation_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_009_velocity_oscillation_accel"""
    v5 = np.log(close).diff(5)
    osc = _safe_div(v5.rolling(63).std(), v5.rolling(63).mean().abs())
    return osc.diff(5)

def dvel_drv2_010_ema_velocity_21d_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_010_ema_velocity_21d_accel"""
    ema = close.ewm(span=21).mean()
    v = np.log(ema).diff(5)
    return v.diff(5)

def dvel_drv2_011_velocity_to_atr_ratio_accel(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dvel_drv2_011_velocity_to_atr_ratio_accel"""
    v = np.log(close).diff(21).abs()
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(63).mean() / close.rolling(63).mean()
    ratio = _safe_div(v, atr)
    return ratio.diff(5)

def dvel_drv2_012_terminal_velocity_decay_velocity(close: pd.Series) -> pd.Series:
    """dvel_drv2_012_terminal_velocity_decay_velocity"""
    score = _rolling_slope(np.log(close), 5) - _rolling_slope(np.log(close), 21)
    return score.diff(5)

def dvel_drv2_013_velocity_entropy_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_013_velocity_entropy_accel"""
    v = close.pct_change()
    def _entropy(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
    ent = v.rolling(63).apply(_entropy, raw=True)
    return ent.diff(5)

def dvel_drv2_014_velocity_gradient_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_014_velocity_gradient_accel"""
    v = np.log(close).diff(5)
    grad = _rolling_slope(v, 63)
    return grad.diff(5)

def dvel_drv2_015_harmonic_velocity_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_015_harmonic_velocity_accel"""
    ret = close.pct_change() + 1.0
    def _harm(y):
        return len(y) / np.sum(1.0 / y) - 1.0
    hv = ret.rolling(63).apply(_harm, raw=True)
    return hv.diff(5)

def dvel_drv2_016_log_price_rsq_velocity(close: pd.Series) -> pd.Series:
    """dvel_drv2_016_log_price_rsq_velocity"""
    def _rsq(y):
        if len(y) < 2: return np.nan
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = np.log(close).rolling(63).apply(_rsq, raw=True)
    return r2.diff(5)

def dvel_drv2_017_velocity_jump_ratio_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_017_velocity_jump_ratio_accel"""
    v = np.log(close).diff(1).abs()
    ratio = _safe_div(v, v.rolling(21).max())
    return ratio.diff(5)

def dvel_drv2_018_velocity_at_earnings_surprise_accel(close: pd.Series, surprise: pd.Series) -> pd.Series:
    """dvel_drv2_018_velocity_at_earnings_surprise_accel"""
    v = np.log(close).diff(5)
    ves = v.where(surprise.abs() > 0).ffill()
    return ves.diff(5)

def dvel_drv2_019_mktcap_to_price_velocity_ratio_accel(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dvel_drv2_019_mktcap_to_price_velocity_ratio_accel"""
    v_p = np.log(close).diff(21)
    v_mc = np.log(close * sharesbas).diff(21)
    ratio = _safe_div(v_mc, v_p)
    return ratio.diff(5)

def dvel_drv2_020_negative_velocity_intensity_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_020_negative_velocity_intensity_accel"""
    v = np.log(close).diff(1)
    neg_v = v.where(v < 0)
    intense = neg_v.rolling(21).sum()
    return intense.diff(5)

def dvel_drv2_021_velocity_climax_score_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_021_velocity_climax_score_accel"""
    v = np.log(close).diff(5).abs()
    v_norm = _safe_div(v - v.rolling(63).mean(), v.rolling(63).std())
    r = (close.expanding().max() - close.expanding().min()) / close.expanding().max()
    score = v_norm * r
    return score.diff(5)

def dvel_drv2_022_days_in_high_velocity_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_022_days_in_high_velocity_accel"""
    v = np.log(close).diff(5).abs()
    threshold = v.rolling(252).mean() + 1.5 * v.rolling(252).std()
    days = (v > threshold).rolling(63).sum()
    return days.diff(5)

def dvel_drv2_023_velocity_autocorr_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_023_velocity_autocorr_accel"""
    v5 = np.log(close).diff(5)
    ac = v5.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(5)

def dvel_drv2_024_velocity_residual_std_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_024_velocity_residual_std_accel"""
    def _res_std(y):
        x = np.arange(len(y))
        res = linregress(x, y)
        y_fit = res.intercept + res.slope * x
        return np.std(y - y_fit)
    rs = np.log(close).rolling(63).apply(_res_std, raw=True)
    return rs.diff(5)

def dvel_drv2_025_velocity_composite_momentum_accel(close: pd.Series) -> pd.Series:
    """dvel_drv2_025_velocity_composite_momentum_accel"""
    v5 = np.log(close).diff(5) / 5.0
    v21 = np.log(close).diff(21) / 21.0
    v63 = np.log(close).diff(63) / 63.0
    comp = (0.5 * v5 + 0.3 * v21 + 0.2 * v63)
    return comp.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V04_V_REGISTRY = {
    "dvel_drv2_001_log_velocity_21d_accel": {"inputs": ["close"], "func": dvel_drv2_001_log_velocity_21d_accel},
    "dvel_drv2_002_drawdown_velocity_252d_accel": {"inputs": ["close"], "func": dvel_drv2_002_drawdown_velocity_252d_accel},
    "dvel_drv2_003_terminal_velocity_10d_accel": {"inputs": ["close"], "func": dvel_drv2_003_terminal_velocity_10d_accel},
    "dvel_drv2_004_sigma_velocity_21d_accel": {"inputs": ["close"], "func": dvel_drv2_004_sigma_velocity_21d_accel},
    "dvel_drv2_005_volume_weighted_velocity_accel": {"inputs": ["close", "volume"], "func": dvel_drv2_005_volume_weighted_velocity_accel},
    "dvel_drv2_006_mktcap_velocity_63d_accel": {"inputs": ["close", "sharesbas"], "func": dvel_drv2_006_mktcap_velocity_63d_accel},
    "dvel_drv2_007_velocity_persistence_accel": {"inputs": ["close"], "func": dvel_drv2_007_velocity_persistence_accel},
    "dvel_drv2_008_velocity_skewness_accel": {"inputs": ["close"], "func": dvel_drv2_008_velocity_skewness_accel},
    "dvel_drv2_009_velocity_oscillation_accel": {"inputs": ["close"], "func": dvel_drv2_009_velocity_oscillation_accel},
    "dvel_drv2_010_ema_velocity_21d_accel": {"inputs": ["close"], "func": dvel_drv2_010_ema_velocity_21d_accel},
    "dvel_drv2_011_velocity_to_atr_ratio_accel": {"inputs": ["close", "high", "low"], "func": dvel_drv2_011_velocity_to_atr_ratio_accel},
    "dvel_drv2_012_terminal_velocity_decay_velocity": {"inputs": ["close"], "func": dvel_drv2_012_terminal_velocity_decay_velocity},
    "dvel_drv2_013_velocity_entropy_accel": {"inputs": ["close"], "func": dvel_drv2_013_velocity_entropy_accel},
    "dvel_drv2_014_velocity_gradient_accel": {"inputs": ["close"], "func": dvel_drv2_014_velocity_gradient_accel},
    "dvel_drv2_015_harmonic_velocity_accel": {"inputs": ["close"], "func": dvel_drv2_015_harmonic_velocity_accel},
    "dvel_drv2_016_log_price_rsq_velocity": {"inputs": ["close"], "func": dvel_drv2_016_log_price_rsq_velocity},
    "dvel_drv2_017_velocity_jump_ratio_accel": {"inputs": ["close"], "func": dvel_drv2_017_velocity_jump_ratio_accel},
    "dvel_drv2_018_velocity_at_earnings_surprise_accel": {"inputs": ["close", "surprise"], "func": dvel_drv2_018_velocity_at_earnings_surprise_accel},
    "dvel_drv2_019_mktcap_to_price_velocity_ratio_accel": {"inputs": ["close", "sharesbas"], "func": dvel_drv2_019_mktcap_to_price_velocity_ratio_accel},
    "dvel_drv2_020_negative_velocity_intensity_accel": {"inputs": ["close"], "func": dvel_drv2_020_negative_velocity_intensity_accel},
    "dvel_drv2_021_velocity_climax_score_accel": {"inputs": ["close"], "func": dvel_drv2_021_velocity_climax_score_accel},
    "dvel_drv2_022_days_in_high_velocity_accel": {"inputs": ["close"], "func": dvel_drv2_022_days_in_high_velocity_accel},
    "dvel_drv2_023_velocity_autocorr_accel": {"inputs": ["close"], "func": dvel_drv2_023_velocity_autocorr_accel},
    "dvel_drv2_024_velocity_residual_std_accel": {"inputs": ["close"], "func": dvel_drv2_024_velocity_residual_std_accel},
    "dvel_drv2_025_velocity_composite_momentum_accel": {"inputs": ["close"], "func": dvel_drv2_025_velocity_composite_momentum_accel},
}
