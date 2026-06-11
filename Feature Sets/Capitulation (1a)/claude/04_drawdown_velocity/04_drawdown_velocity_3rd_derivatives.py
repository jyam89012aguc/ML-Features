"""
04_drawdown_velocity — 3rd Derivatives (25 features)
Domain: jerk / exhaustion of acceleration — rate of change of the 2nd derivative.
Captures inflection points in velocity acceleration: is the acceleration itself fading
(velocity exhaustion / capitulation climax signals)?
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

# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each function recomputes the relevant 2nd-derivative concept, then takes
# ANOTHER diff/slope to yield the jerk (3rd derivative).

def dvel_drv3_001_log_vel_1d_jerk_5d(close: pd.Series) -> pd.Series:
    """Jerk of 1d velocity: third diff of daily log-return (5-day steps)."""
    v1 = _log_ret(close, 1)
    accel = v1.diff(5)
    return accel.diff(5)

def dvel_drv3_002_log_vel_5d_jerk_5d(close: pd.Series) -> pd.Series:
    """Jerk of 5d per-day velocity."""
    v = _log_ret(close, 5) / 5.0
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_003_ols_slope_5d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of OLS-slope-5d: is the slope acceleration exhausting?"""
    v = _rolling_slope(np.log(close), 5)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_004_ols_slope_21d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of OLS-slope-21d."""
    v = _rolling_slope(np.log(close), 21)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_005_worst_5d_drop_jerk_21d(close: pd.Series) -> pd.Series:
    """Jerk of worst-5d-drop-in-21d: is crash speed acceleration itself fading?"""
    v = _log_ret(close, 5).rolling(21, min_periods=5).min()
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_006_dd_vel_21d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of drawdown/days-since-high (21d) acceleration."""
    roll_max = _rolling_max(close, 21)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(21, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    v = _safe_div(dd, days_since + 1)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_007_vol_scaled_vel_21d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of volatility-scaled 21d velocity."""
    r = _log_ret(close, 21)
    vol = _log_ret(close, 1).rolling(21, min_periods=5).std() * np.sqrt(21)
    v = _safe_div(r, vol)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_008_avg_neg_vel_21d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of mean negative daily velocity (21d)."""
    dr = _log_ret(close, 1)
    v = dr.where(dr < 0).rolling(21, min_periods=5).mean()
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_009_neg_vel_freq_21d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of negative-return frequency (21d): is frequency-acceleration stabilizing?"""
    dr = _log_ret(close, 1)
    v = (dr < 0).rolling(21, min_periods=5).mean()
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_010_neg_vel_freq_63d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of negative-return frequency (63d)."""
    dr = _log_ret(close, 1)
    v = (dr < 0).rolling(63, min_periods=10).mean()
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_011_vwap_vel_jerk_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jerk of VWAP velocity (21d): is VWAP decline acceleration fading?"""
    vwap = _safe_div(
        (close * volume).rolling(21, min_periods=5).sum(),
        volume.rolling(21, min_periods=5).sum())
    v = _log_ret(vwap, 5) / 5.0
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_012_ema10_slope_jerk(close: pd.Series) -> pd.Series:
    """Jerk of EMA(10) slope acceleration."""
    v = _log_ret(close.ewm(span=10, adjust=False).mean(), 5) / 5.0
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_013_vel_zscore_5d_jerk(close: pd.Series) -> pd.Series:
    """Jerk of 5d velocity z-score: is the z-score acceleration reversing?"""
    v_raw = _log_ret(close, 5)
    v = _safe_div(v_raw - _rolling_mean(v_raw, 252), _rolling_std(v_raw, 252))
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_014_atr_norm_vel_21d_jerk(
        close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Jerk of ATR-normalized 21d velocity."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    atr21 = tr.rolling(21, min_periods=5).mean()
    v = _safe_div(close - close.shift(21), atr21)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_015_down_vol_ratio_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Jerk of down-vol/up-vol ratio (21d): is selling pressure trend decelerating?"""
    dr = _log_ret(close, 1)
    down_vol = volume.where(dr < 0, 0).rolling(21, min_periods=5).sum()
    up_vol = volume.where(dr > 0, 0).rolling(21, min_periods=5).sum()
    v = _safe_div(down_vol, up_vol)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_016_vel_spread_5_vs_21_jerk(close: pd.Series) -> pd.Series:
    """Jerk of velocity-spread (5d minus 21d): is the spread acceleration flipping?"""
    v = _log_ret(close, 5) / 5.0 - _log_ret(close, 21) / 21.0
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_017_crash_speed_jerk(close: pd.Series) -> pd.Series:
    """Jerk of crash speed score (21d worst-5d / vol)."""
    worst5 = _log_ret(close, 5).rolling(21, min_periods=5).min()
    vol63 = _rolling_std(_log_ret(close, 1), 63) * np.sqrt(5)
    v = _safe_div(worst5, vol63)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_018_vel_slope_jerk_21d(close: pd.Series) -> pd.Series:
    """Jerk via slope-of-slope-of-slope: 3rd OLS slope of log-price (5d base)."""
    v = _rolling_slope(np.log(close), 5)
    accel_slope = _rolling_slope(v, 21)
    return _rolling_slope(accel_slope, 10)

def dvel_drv3_019_neg_vel_share_jerk_21d(close: pd.Series) -> pd.Series:
    """Jerk of negative velocity share (21d)."""
    dr = _log_ret(close, 1)
    neg_sum = dr.where(dr < 0, 0).rolling(21, min_periods=5).sum().abs()
    tot_sum = dr.abs().rolling(21, min_periods=5).sum()
    v = _safe_div(neg_sum, tot_sum)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_020_vel_pct_rank_jerk_252d(close: pd.Series) -> pd.Series:
    """Jerk of 21d velocity percentile rank (252d)."""
    v = _log_ret(close, 21).rolling(252, min_periods=42).rank(pct=True)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_021_rolling_mdd_rate_jerk_63d(close: pd.Series) -> pd.Series:
    """Jerk of rolling 63d MDD rate."""
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
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_022_ath_dd_vel_jerk(close: pd.Series) -> pd.Series:
    """Jerk of ATH-drawdown velocity."""
    ath = close.cummax()
    dd = _safe_div(close - ath, ath)
    is_high = (close >= ath)
    idx_arr = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_ath_idx = idx_arr.where(is_high).ffill().fillna(0)
    days_since = idx_arr - last_ath_idx
    v = _safe_div(dd, days_since + 1)
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_023_log_vel_21d_jerk_slope(close: pd.Series) -> pd.Series:
    """Jerk of 21d per-day velocity via OLS slope of its 5d-diff series."""
    v = _log_ret(close, 21) / 21.0
    accel = v.diff(5)
    return _rolling_slope(accel, 21)

def dvel_drv3_024_neg_vel_intensity_jerk_21d(close: pd.Series) -> pd.Series:
    """Jerk of sum-of-negative-daily-velocity (21d)."""
    dr = _log_ret(close, 1)
    v = dr.where(dr < 0, 0).rolling(21, min_periods=5).sum()
    accel = v.diff(5)
    return accel.diff(5)

def dvel_drv3_025_composite_jerk_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite jerk: mean of z-scored jerks from 1d-vel, freq-21d, and crash-speed."""
    # jerk of 1d velocity
    v1 = _log_ret(close, 1)
    j1 = v1.diff(5).diff(5)
    # jerk of neg-freq-21d
    dr = _log_ret(close, 1)
    vf = (dr < 0).rolling(21, min_periods=5).mean()
    jf = vf.diff(5).diff(5)
    # jerk of crash speed
    worst5 = _log_ret(close, 5).rolling(21, min_periods=5).min()
    vol63 = _rolling_std(_log_ret(close, 1), 63) * np.sqrt(5)
    vc = _safe_div(worst5, vol63)
    jc = vc.diff(5).diff(5)
    def _zs(s):
        return _safe_div(s - _rolling_mean(s, 252), _rolling_std(s, 252))
    return (_zs(j1) + _zs(jf) + _zs(jc)) / 3.0

# ── Registry ──────────────────────────────────────────────────────────────────
DRAWDOWN_VELOCITY_REGISTRY_3RD_DERIVATIVES = {
    "dvel_drv3_001_log_vel_1d_jerk_5d": {"inputs": ["close"], "func": dvel_drv3_001_log_vel_1d_jerk_5d},
    "dvel_drv3_002_log_vel_5d_jerk_5d": {"inputs": ["close"], "func": dvel_drv3_002_log_vel_5d_jerk_5d},
    "dvel_drv3_003_ols_slope_5d_jerk": {"inputs": ["close"], "func": dvel_drv3_003_ols_slope_5d_jerk},
    "dvel_drv3_004_ols_slope_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_004_ols_slope_21d_jerk},
    "dvel_drv3_005_worst_5d_drop_jerk_21d": {"inputs": ["close"], "func": dvel_drv3_005_worst_5d_drop_jerk_21d},
    "dvel_drv3_006_dd_vel_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_006_dd_vel_21d_jerk},
    "dvel_drv3_007_vol_scaled_vel_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_007_vol_scaled_vel_21d_jerk},
    "dvel_drv3_008_avg_neg_vel_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_008_avg_neg_vel_21d_jerk},
    "dvel_drv3_009_neg_vel_freq_21d_jerk": {"inputs": ["close"], "func": dvel_drv3_009_neg_vel_freq_21d_jerk},
    "dvel_drv3_010_neg_vel_freq_63d_jerk": {"inputs": ["close"], "func": dvel_drv3_010_neg_vel_freq_63d_jerk},
    "dvel_drv3_011_vwap_vel_jerk_21d": {"inputs": ["close", "volume"], "func": dvel_drv3_011_vwap_vel_jerk_21d},
    "dvel_drv3_012_ema10_slope_jerk": {"inputs": ["close"], "func": dvel_drv3_012_ema10_slope_jerk},
    "dvel_drv3_013_vel_zscore_5d_jerk": {"inputs": ["close"], "func": dvel_drv3_013_vel_zscore_5d_jerk},
    "dvel_drv3_014_atr_norm_vel_21d_jerk": {"inputs": ["close", "high", "low"], "func": dvel_drv3_014_atr_norm_vel_21d_jerk},
    "dvel_drv3_015_down_vol_ratio_jerk": {"inputs": ["close", "volume"], "func": dvel_drv3_015_down_vol_ratio_jerk},
    "dvel_drv3_016_vel_spread_5_vs_21_jerk": {"inputs": ["close"], "func": dvel_drv3_016_vel_spread_5_vs_21_jerk},
    "dvel_drv3_017_crash_speed_jerk": {"inputs": ["close"], "func": dvel_drv3_017_crash_speed_jerk},
    "dvel_drv3_018_vel_slope_jerk_21d": {"inputs": ["close"], "func": dvel_drv3_018_vel_slope_jerk_21d},
    "dvel_drv3_019_neg_vel_share_jerk_21d": {"inputs": ["close"], "func": dvel_drv3_019_neg_vel_share_jerk_21d},
    "dvel_drv3_020_vel_pct_rank_jerk_252d": {"inputs": ["close"], "func": dvel_drv3_020_vel_pct_rank_jerk_252d},
    "dvel_drv3_021_rolling_mdd_rate_jerk_63d": {"inputs": ["close"], "func": dvel_drv3_021_rolling_mdd_rate_jerk_63d},
    "dvel_drv3_022_ath_dd_vel_jerk": {"inputs": ["close"], "func": dvel_drv3_022_ath_dd_vel_jerk},
    "dvel_drv3_023_log_vel_21d_jerk_slope": {"inputs": ["close"], "func": dvel_drv3_023_log_vel_21d_jerk_slope},
    "dvel_drv3_024_neg_vel_intensity_jerk_21d": {"inputs": ["close"], "func": dvel_drv3_024_neg_vel_intensity_jerk_21d},
    "dvel_drv3_025_composite_jerk_score": {"inputs": ["close", "volume"], "func": dvel_drv3_025_composite_jerk_score},
}
