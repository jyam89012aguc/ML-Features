"""
04_drawdown_velocity — 2nd Derivatives (25 features)
Domain: acceleration of decline — rate of change of base velocity features.
Captures whether the speed of the fall is itself speeding up or slowing down.
Asset class: US equities | Daily OHLCV only (SEP folder — price/volume inputs only)
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_YEAR = 252
_QTR = 63
_MONTH = 21
_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)

def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    return np.log(s).diff(n)

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()

def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over rolling window of length w."""
    def _slope(y):
        if len(y) < 2:
            return np.nan
        x = np.arange(len(y), dtype=float)
        xm = x - x.mean()
        ym = y - y.mean()
        denom = (xm * xm).sum()
        if denom == 0:
            return np.nan
        return (xm * ym).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)

def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int = 14) -> pd.Series:
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()

# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────
# Each function computes a base velocity concept, then takes its diff/slope
# to yield the acceleration (rate of change) of that velocity.

def dvel_drv2_001_log_vel_1d_accel_5d(close: pd.Series) -> pd.Series:
    """Acceleration of 1-day velocity: 5-day diff of daily log-return."""
    v = _log_ret(close, 1)
    return v.diff(5)

def dvel_drv2_002_log_vel_5d_accel_5d(close: pd.Series) -> pd.Series:
    """Acceleration of 5-day per-day velocity: 5-day diff."""
    v = _log_ret(close, 5) / 5.0
    return v.diff(5)

def dvel_drv2_003_log_vel_21d_accel_5d(close: pd.Series) -> pd.Series:
    """Acceleration of 21-day per-day velocity: 5-day diff."""
    v = _log_ret(close, 21) / 21.0
    return v.diff(5)

def dvel_drv2_004_ols_slope_5d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of OLS-slope-5d: 5-day diff of rolling 5-day slope."""
    v = _rolling_slope(np.log(close), 5)
    return v.diff(5)

def dvel_drv2_005_ols_slope_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of OLS-slope-21d: 5-day diff of rolling 21-day slope."""
    v = _rolling_slope(np.log(close), 21)
    return v.diff(5)

def dvel_drv2_006_worst_5d_drop_accel_21d(close: pd.Series) -> pd.Series:
    """Acceleration of worst-5d-drop-in-21d: is the worst drop getting worse?"""
    v = _log_ret(close, 5).rolling(21, min_periods=5).min()
    return v.diff(5)

def dvel_drv2_007_dd_vel_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of drawdown/days-since-high (21d): is dd velocity increasing?"""
    roll_max = _rolling_max(close, 21)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(21, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    v = _safe_div(dd, days_since + 1)
    return v.diff(5)

def dvel_drv2_008_dd_vel_252d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of drawdown/days-since-high (252d)."""
    roll_max = _rolling_max(close, 252)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(252, min_periods=21).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    v = _safe_div(dd, days_since + 1)
    return v.diff(5)

def dvel_drv2_009_vol_scaled_vel_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of volatility-scaled 21d velocity (Sharpe-speed accel)."""
    r = _log_ret(close, 21)
    vol = _log_ret(close, 1).rolling(21, min_periods=5).std() * np.sqrt(21)
    v = _safe_div(r, vol)
    return v.diff(5)

def dvel_drv2_010_avg_neg_daily_vel_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of mean negative daily velocity (21d): down-day speed trend."""
    dr = _log_ret(close, 1)
    v = dr.where(dr < 0).rolling(21, min_periods=5).mean()
    return v.diff(5)

def dvel_drv2_011_neg_vel_freq_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of negative-return frequency (21d): is down-day rate growing?"""
    dr = _log_ret(close, 1)
    v = (dr < 0).rolling(21, min_periods=5).mean()
    return v.diff(5)

def dvel_drv2_012_neg_vel_freq_63d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of negative-return frequency (63d)."""
    dr = _log_ret(close, 1)
    v = (dr < 0).rolling(63, min_periods=10).mean()
    return v.diff(5)

def dvel_drv2_013_vwap_vel_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 21d VWAP velocity: is VWAP falling faster?"""
    vwap = _safe_div(
        (close * volume).rolling(21, min_periods=5).sum(),
        volume.rolling(21, min_periods=5).sum())
    v = _log_ret(vwap, 5) / 5.0
    return v.diff(5)

def dvel_drv2_014_ema10_slope_accel(close: pd.Series) -> pd.Series:
    """Acceleration of EMA(10) slope: short-term smooth descent accelerating?"""
    v = _log_ret(close.ewm(span=10, adjust=False).mean(), 5) / 5.0
    return v.diff(5)

def dvel_drv2_015_ema50_slope_accel(close: pd.Series) -> pd.Series:
    """Acceleration of EMA(50) slope."""
    v = _log_ret(close.ewm(span=50, adjust=False).mean(), 10) / 10.0
    return v.diff(5)

def dvel_drv2_016_vel_zscore_5d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of 5d velocity z-score (is it becoming more extreme?)."""
    v_raw = _log_ret(close, 5)
    v = _safe_div(v_raw - _rolling_mean(v_raw, 252),
                  _rolling_std(v_raw, 252))
    return v.diff(5)

def dvel_drv2_017_atr_norm_vel_21d_accel(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Acceleration of ATR-normalized 21d velocity."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    atr21 = tr.rolling(21, min_periods=5).mean()
    v = _safe_div(close - close.shift(21), atr21)
    return v.diff(5)

def dvel_drv2_018_down_vol_ratio_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of down-vol / up-vol ratio (21d): selling pressure trend."""
    dr = _log_ret(close, 1)
    down_vol = volume.where(dr < 0, 0).rolling(21, min_periods=5).sum()
    up_vol = volume.where(dr > 0, 0).rolling(21, min_periods=5).sum()
    v = _safe_div(down_vol, up_vol)
    return v.diff(5)

def dvel_drv2_019_vel_spread_5_vs_21_accel(close: pd.Series) -> pd.Series:
    """Acceleration of velocity spread (5d minus 21d): is short term worsening vs medium?"""
    v = _log_ret(close, 5) / 5.0 - _log_ret(close, 21) / 21.0
    return v.diff(5)

def dvel_drv2_020_crash_speed_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of crash speed score (21d worst-5d / vol): panic deepening?"""
    worst5 = _log_ret(close, 5).rolling(21, min_periods=5).min()
    vol63 = _rolling_std(_log_ret(close, 1), 63) * np.sqrt(5)
    v = _safe_div(worst5, vol63)
    return v.diff(5)

def dvel_drv2_021_vel_slope_of_vel_slope_21d(close: pd.Series) -> pd.Series:
    """2nd derivative directly: slope of the OLS-slope-5d series over 21d."""
    v = _rolling_slope(np.log(close), 5)
    return _rolling_slope(v, 21)

def dvel_drv2_022_neg_vel_share_accel_21d(close: pd.Series) -> pd.Series:
    """Acceleration of negative velocity share (21d): is downward thrust growing?"""
    dr = _log_ret(close, 1)
    neg_sum = dr.where(dr < 0, 0).rolling(21, min_periods=5).sum().abs()
    tot_sum = dr.abs().rolling(21, min_periods=5).sum()
    v = _safe_div(neg_sum, tot_sum)
    return v.diff(5)

def dvel_drv2_023_vel_pct_rank_accel_252d(close: pd.Series) -> pd.Series:
    """Acceleration of 21d velocity percentile rank: rank falling faster?"""
    v = _log_ret(close, 21).rolling(252, min_periods=42).rank(pct=True)
    return v.diff(5)

def dvel_drv2_024_rolling_mdd_rate_accel_63d(close: pd.Series) -> pd.Series:
    """Acceleration of rolling 63d max-drawdown-rate."""
    def _mdd_rate(x):
        cum_max = np.maximum.accumulate(x)
        dd = (x - cum_max) / cum_max
        mdd = dd.min()
        if mdd == 0:
            return 0.0
        trough_idx = np.argmin(dd)
        peak_idx = np.argmax(x[:trough_idx + 1]) if trough_idx > 0 else 0
        duration = trough_idx - peak_idx
        return mdd / (duration + 1)
    v = close.rolling(63, min_periods=10).apply(_mdd_rate, raw=True)
    return v.diff(5)

def dvel_drv2_025_ath_dd_vel_accel(close: pd.Series) -> pd.Series:
    """Acceleration of ATH-drawdown velocity: is the ATH fall speeding up?"""
    ath = close.cummax()
    dd = _safe_div(close - ath, ath)
    is_high = (close >= ath)
    idx_arr = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_ath_idx = idx_arr.where(is_high).ffill().fillna(0)
    days_since = idx_arr - last_ath_idx
    v = _safe_div(dd, days_since + 1)
    return v.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────
DRAWDOWN_VELOCITY_REGISTRY_2ND_DERIVATIVES = {
    "dvel_drv2_001_log_vel_1d_accel_5d": {"inputs": ["close"], "func": dvel_drv2_001_log_vel_1d_accel_5d},
    "dvel_drv2_002_log_vel_5d_accel_5d": {"inputs": ["close"], "func": dvel_drv2_002_log_vel_5d_accel_5d},
    "dvel_drv2_003_log_vel_21d_accel_5d": {"inputs": ["close"], "func": dvel_drv2_003_log_vel_21d_accel_5d},
    "dvel_drv2_004_ols_slope_5d_accel": {"inputs": ["close"], "func": dvel_drv2_004_ols_slope_5d_accel},
    "dvel_drv2_005_ols_slope_21d_accel": {"inputs": ["close"], "func": dvel_drv2_005_ols_slope_21d_accel},
    "dvel_drv2_006_worst_5d_drop_accel_21d": {"inputs": ["close"], "func": dvel_drv2_006_worst_5d_drop_accel_21d},
    "dvel_drv2_007_dd_vel_21d_accel": {"inputs": ["close"], "func": dvel_drv2_007_dd_vel_21d_accel},
    "dvel_drv2_008_dd_vel_252d_accel": {"inputs": ["close"], "func": dvel_drv2_008_dd_vel_252d_accel},
    "dvel_drv2_009_vol_scaled_vel_21d_accel": {"inputs": ["close"], "func": dvel_drv2_009_vol_scaled_vel_21d_accel},
    "dvel_drv2_010_avg_neg_daily_vel_21d_accel": {"inputs": ["close"], "func": dvel_drv2_010_avg_neg_daily_vel_21d_accel},
    "dvel_drv2_011_neg_vel_freq_21d_accel": {"inputs": ["close"], "func": dvel_drv2_011_neg_vel_freq_21d_accel},
    "dvel_drv2_012_neg_vel_freq_63d_accel": {"inputs": ["close"], "func": dvel_drv2_012_neg_vel_freq_63d_accel},
    "dvel_drv2_013_vwap_vel_accel_21d": {"inputs": ["close", "volume"], "func": dvel_drv2_013_vwap_vel_accel_21d},
    "dvel_drv2_014_ema10_slope_accel": {"inputs": ["close"], "func": dvel_drv2_014_ema10_slope_accel},
    "dvel_drv2_015_ema50_slope_accel": {"inputs": ["close"], "func": dvel_drv2_015_ema50_slope_accel},
    "dvel_drv2_016_vel_zscore_5d_accel": {"inputs": ["close"], "func": dvel_drv2_016_vel_zscore_5d_accel},
    "dvel_drv2_017_atr_norm_vel_21d_accel": {"inputs": ["close", "high", "low"], "func": dvel_drv2_017_atr_norm_vel_21d_accel},
    "dvel_drv2_018_down_vol_ratio_accel": {"inputs": ["close", "volume"], "func": dvel_drv2_018_down_vol_ratio_accel},
    "dvel_drv2_019_vel_spread_5_vs_21_accel": {"inputs": ["close"], "func": dvel_drv2_019_vel_spread_5_vs_21_accel},
    "dvel_drv2_020_crash_speed_score_accel": {"inputs": ["close"], "func": dvel_drv2_020_crash_speed_score_accel},
    "dvel_drv2_021_vel_slope_of_vel_slope_21d": {"inputs": ["close"], "func": dvel_drv2_021_vel_slope_of_vel_slope_21d},
    "dvel_drv2_022_neg_vel_share_accel_21d": {"inputs": ["close"], "func": dvel_drv2_022_neg_vel_share_accel_21d},
    "dvel_drv2_023_vel_pct_rank_accel_252d": {"inputs": ["close"], "func": dvel_drv2_023_vel_pct_rank_accel_252d},
    "dvel_drv2_024_rolling_mdd_rate_accel_63d": {"inputs": ["close"], "func": dvel_drv2_024_rolling_mdd_rate_accel_63d},
    "dvel_drv2_025_ath_dd_vel_accel": {"inputs": ["close"], "func": dvel_drv2_025_ath_dd_vel_accel},
}
