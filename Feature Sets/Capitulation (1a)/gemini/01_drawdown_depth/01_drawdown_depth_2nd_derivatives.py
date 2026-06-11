"""
Drawdown Depth — 2nd Derivatives
Domain: magnitude of decline vs trailing highs
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

def dd_drv2_001_drawdown_252d_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_001_drawdown_252d_velocity"""
    # 5-day change in 252d drawdown
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    return dd.diff(5)

def dd_drv2_002_drawdown_ath_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_002_drawdown_ath_velocity"""
    h = close.expanding().max()
    dd = _safe_div(close - h, h)
    return dd.diff(5)

def dd_drv2_003_drawdown_sigma_252d_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_003_drawdown_sigma_252d_chg"""
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    std = close.rolling(252).std() / close.rolling(252).mean()
    dd_sigma = _safe_div(dd, std)
    return dd_sigma.diff(5)

def dd_drv2_004_drawdown_log_ath_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_004_drawdown_log_ath_velocity"""
    h = close.expanding().max()
    log_dd = np.log(close) - np.log(h)
    return log_dd.diff(5)

def dd_drv2_005_drawdown_intensity_252d_accel(close: pd.Series) -> pd.Series:
    """dd_drv2_005_drawdown_intensity_252d_accel"""
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    mdd = dd.rolling(252).min()
    intensity = _safe_div(dd, mdd)
    return intensity.diff(5)

def dd_drv2_006_low_to_high_ratio_252d_chg(close: pd.Series, low: pd.Series) -> pd.Series:
    """dd_drv2_006_low_to_high_ratio_252d_chg"""
    h = _rolling_max(close, 252)
    ratio = _safe_div(low, h)
    return ratio.diff(5)

def dd_drv2_007_drawdown_from_sma_200_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_007_drawdown_from_sma_200_velocity"""
    ma = _rolling_mean(close, 200)
    dd = _safe_div(close - ma, ma)
    return dd.diff(5)

def dd_drv2_008_mktcap_drawdown_252d_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_drv2_008_mktcap_drawdown_252d_velocity"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    dd = _safe_div(mc - h, h)
    return dd.diff(5)

def dd_drv2_009_drawdown_atr_ratio_252d_chg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """dd_drv2_009_drawdown_atr_ratio_252d_chg"""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _rolling_mean(tr, 252)
    h = _rolling_max(close, 252)
    ratio = _safe_div(close - h, atr)
    return ratio.diff(5)

def dd_drv2_010_drawdown_to_range_ratio_252d_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_010_drawdown_to_range_ratio_252d_chg"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    ratio = _safe_div(close - h, h - l)
    return ratio.diff(5)

def dd_drv2_011_drawdown_zscore_252d_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_011_drawdown_zscore_252d_velocity"""
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    z = (dd - dd.rolling(252).mean()) / dd.rolling(252).std()
    return z.diff(5)

def dd_drv2_012_drawdown_weighted_volume_252d_chg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """dd_drv2_012_drawdown_weighted_volume_252d_chg"""
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    v_norm = _safe_div(volume, _rolling_mean(volume, 252))
    w_dd = dd * v_norm
    return w_dd.diff(5)

def dd_drv2_013_drawdown_log_spread_ath_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_013_drawdown_log_spread_ath_velocity"""
    h = close.expanding().max()
    spread = np.log(h) - np.log(close)
    return spread.diff(5)

def dd_drv2_014_drawdown_area_63d_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_014_drawdown_area_63d_velocity"""
    h = _rolling_max(close, 63)
    dd = _safe_div(close - h, h)
    area = dd.rolling(63).sum()
    return area.diff(5)

def dd_drv2_015_drawdown_convexity_63d_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_015_drawdown_convexity_63d_chg"""
    h = _rolling_max(close, 63)
    dd = _safe_div(close - h, h)
    area = dd.rolling(63).sum()
    max_dd = dd.rolling(63).min()
    convexity = _safe_div(area, max_dd * 63.0)
    return convexity.diff(5)

def dd_drv2_016_drawdown_entropy_252d_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_016_drawdown_entropy_252d_chg"""
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    entropy = dd.diff(1).rolling(252).std()
    return entropy.diff(5)

def dd_drv2_017_drawdown_recovery_ratio_252d_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_017_drawdown_recovery_ratio_252d_chg"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    ratio = _safe_div(close - l, h - l)
    return ratio.diff(5)

def dd_drv2_018_drawdown_from_prev_year_high_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_018_drawdown_from_prev_year_high_velocity"""
    h = _rolling_max(close.shift(252), 252)
    dd = _safe_div(close - h, h)
    return dd.diff(5)

def dd_drv2_019_drawdown_from_ema_200_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_019_drawdown_from_ema_200_velocity"""
    ma = close.ewm(span=200).mean()
    dd = _safe_div(close - ma, ma)
    return dd.diff(5)

def dd_drv2_020_drawdown_harmonic_mean_ratio_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_020_drawdown_harmonic_mean_ratio_chg"""
    h = _rolling_max(close, 252)
    harmonic_h = _safe_div(1.0, _rolling_mean(_safe_div(1.0, h), 252))
    ratio = _safe_div(close, harmonic_h)
    return ratio.diff(5)

def dd_drv2_021_drawdown_quadratic_mean_ratio_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_021_drawdown_quadratic_mean_ratio_chg"""
    h = _rolling_max(close, 252)
    quad_h = np.sqrt(_rolling_mean(h**2, 252))
    ratio = _safe_div(close, quad_h)
    return ratio.diff(5)

def dd_drv2_022_mktcap_drawdown_ath_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """dd_drv2_022_mktcap_drawdown_ath_velocity"""
    mc = close * sharesbas
    h = mc.expanding().max()
    dd = _safe_div(mc - h, h)
    return dd.diff(5)

def dd_drv2_023_drawdown_sigma_ath_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_023_drawdown_sigma_ath_chg"""
    h = close.expanding().max()
    dd = _safe_div(close - h, h)
    std = close.expanding().std() / close.expanding().mean()
    dd_sigma = _safe_div(dd, std)
    return dd_sigma.diff(5)

def dd_drv2_024_drawdown_tail_risk_252d_chg(close: pd.Series) -> pd.Series:
    """dd_drv2_024_drawdown_tail_risk_252d_chg"""
    h = _rolling_max(close, 252)
    dd = _safe_div(close - h, h)
    p5 = dd.rolling(252).quantile(0.05)
    m = dd.rolling(252).mean()
    risk = _safe_div(p5, m)
    return risk.diff(5)

def dd_drv2_025_drawdown_final_depth_metric_velocity(close: pd.Series) -> pd.Series:
    """dd_drv2_025_drawdown_final_depth_metric_velocity"""
    dd21 = _safe_div(close - _rolling_max(close, 21), _rolling_max(close, 21))
    dd63 = _safe_div(close - _rolling_max(close, 63), _rolling_max(close, 63))
    dd252 = _safe_div(close - _rolling_max(close, 252), _rolling_max(close, 252))
    metric = (0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252)
    return metric.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V01_V_REGISTRY = {
    "dd_drv2_001_drawdown_252d_velocity": {"inputs": ["close"], "func": dd_drv2_001_drawdown_252d_velocity},
    "dd_drv2_002_drawdown_ath_velocity": {"inputs": ["close"], "func": dd_drv2_002_drawdown_ath_velocity},
    "dd_drv2_003_drawdown_sigma_252d_chg": {"inputs": ["close"], "func": dd_drv2_003_drawdown_sigma_252d_chg},
    "dd_drv2_004_drawdown_log_ath_velocity": {"inputs": ["close"], "func": dd_drv2_004_drawdown_log_ath_velocity},
    "dd_drv2_005_drawdown_intensity_252d_accel": {"inputs": ["close"], "func": dd_drv2_005_drawdown_intensity_252d_accel},
    "dd_drv2_006_low_to_high_ratio_252d_chg": {"inputs": ["close", "low"], "func": dd_drv2_006_low_to_high_ratio_252d_chg},
    "dd_drv2_007_drawdown_from_sma_200_velocity": {"inputs": ["close"], "func": dd_drv2_007_drawdown_from_sma_200_velocity},
    "dd_drv2_008_mktcap_drawdown_252d_velocity": {"inputs": ["close", "sharesbas"], "func": dd_drv2_008_mktcap_drawdown_252d_velocity},
    "dd_drv2_009_drawdown_atr_ratio_252d_chg": {"inputs": ["close", "high", "low"], "func": dd_drv2_009_drawdown_atr_ratio_252d_chg},
    "dd_drv2_010_drawdown_to_range_ratio_252d_chg": {"inputs": ["close"], "func": dd_drv2_010_drawdown_to_range_ratio_252d_chg},
    "dd_drv2_011_drawdown_zscore_252d_velocity": {"inputs": ["close"], "func": dd_drv2_011_drawdown_zscore_252d_velocity},
    "dd_drv2_012_drawdown_weighted_volume_252d_chg": {"inputs": ["close", "volume"], "func": dd_drv2_012_drawdown_weighted_volume_252d_chg},
    "dd_drv2_013_drawdown_log_spread_ath_velocity": {"inputs": ["close"], "func": dd_drv2_013_drawdown_log_spread_ath_velocity},
    "dd_drv2_014_drawdown_area_63d_velocity": {"inputs": ["close"], "func": dd_drv2_014_drawdown_area_63d_velocity},
    "dd_drv2_015_drawdown_convexity_63d_chg": {"inputs": ["close"], "func": dd_drv2_015_drawdown_convexity_63d_chg},
    "dd_drv2_016_drawdown_entropy_252d_chg": {"inputs": ["close"], "func": dd_drv2_016_drawdown_entropy_252d_chg},
    "dd_drv2_017_drawdown_recovery_ratio_252d_chg": {"inputs": ["close"], "func": dd_drv2_017_drawdown_recovery_ratio_252d_chg},
    "dd_drv2_018_drawdown_from_prev_year_high_velocity": {"inputs": ["close"], "func": dd_drv2_018_drawdown_from_prev_year_high_velocity},
    "dd_drv2_019_drawdown_from_ema_200_velocity": {"inputs": ["close"], "func": dd_drv2_019_drawdown_from_ema_200_velocity},
    "dd_drv2_020_drawdown_harmonic_mean_ratio_chg": {"inputs": ["close"], "func": dd_drv2_020_drawdown_harmonic_mean_ratio_chg},
    "dd_drv2_021_drawdown_quadratic_mean_ratio_chg": {"inputs": ["close"], "func": dd_drv2_021_drawdown_quadratic_mean_ratio_chg},
    "dd_drv2_022_mktcap_drawdown_ath_velocity": {"inputs": ["close", "sharesbas"], "func": dd_drv2_022_mktcap_drawdown_ath_velocity},
    "dd_drv2_023_drawdown_sigma_ath_chg": {"inputs": ["close"], "func": dd_drv2_023_drawdown_sigma_ath_chg},
    "dd_drv2_024_drawdown_tail_risk_252d_chg": {"inputs": ["close"], "func": dd_drv2_024_drawdown_tail_risk_252d_chg},
    "dd_drv2_025_drawdown_final_depth_metric_velocity": {"inputs": ["close"], "func": dd_drv2_025_drawdown_final_depth_metric_velocity},
}
