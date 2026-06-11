"""
14_recovery_failure — 3rd Derivatives
Domain: rate of change of 2nd derivatives — captures exhaustion/inflection of acceleration
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of recovery failure acceleration (jerk)
def rfl_drv3_001_max_bounce_jerk(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    vel = b.diff(5)
    return vel.diff(5)


def rfl_drv3_002_bounce_intensity_jerk(close: pd.Series) -> pd.Series:
    curr_l = _rolling_min(close, 63)
    curr_b = _safe_div(close - curr_l, curr_l)
    mx_b = (curr_b).rolling(252).max()
    ratio = _safe_div(curr_b, mx_b)
    vel = ratio.diff(5)
    return vel.diff(5)


def rfl_drv3_003_bounce_decay_jerk(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = b.rolling(252).apply(_slope, raw=True)
    vel = sl.diff(5)
    return vel.diff(5)


def rfl_drv3_004_count_lower_highs_jerk(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=5)[0]
    peaks = close.iloc[peaks_idx]
    is_lower = (peaks < peaks.shift(1)).astype(int).rolling(63, min_periods=1).sum()
    vel = is_lower.reindex(close.index).ffill().diff(5)
    return vel.diff(5)


def rfl_drv3_005_proximity_to_last_peak_jerk(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=5)[0]
    last_peak = close.iloc[peaks_idx].reindex(close.index).ffill()
    p = _safe_div(close, last_peak)
    vel = p.diff(5)
    return vel.diff(5)


def rfl_drv3_006_bounce_failure_velocity_jerk(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    peak_val = b.rolling(21).max().ffill()
    v = (b - peak_val).diff(5)
    accel = v.diff(5)
    return accel.diff(5)


def rfl_drv3_007_recovery_trap_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = _rolling_min(close, 21)
    b = _safe_div(close - l, l)
    v_norm = _safe_div(volume, volume.rolling(63).mean())
    dur = (close > l * 1.02).astype(int).rolling(21).sum()
    idx = _safe_div(b * v_norm, dur)
    vel = idx.diff(5)
    return vel.diff(5)


def rfl_drv3_008_ma_reclaim_failure_jerk(close: pd.Series) -> pd.Series:
    ma = close.rolling(50).mean()
    crossed = (close > ma) & (close.shift(1) <= ma.shift(1))
    failed = (close < ma) & crossed.shift(3)
    cnt = failed.rolling(63).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def rfl_drv3_009_dead_cat_bounce_jerk(close: pd.Series) -> pd.Series:
    h = close.rolling(63).max()
    l = close.rolling(63).min()
    fall = (h - l) / h
    bounce = (close - l) / l
    score = _safe_div(fall, bounce)
    vel = score.diff(5)
    return vel.diff(5)


def rfl_drv3_010_consecutive_lower_peak_jerk(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=10)[0]
    peaks = close.iloc[peaks_idx]
    is_lower = (peaks < peaks.shift(1)).astype(int)
    streak = is_lower.groupby((is_lower == 0).cumsum()).cumsum()
    vel = streak.reindex(close.index).ffill().diff(5)
    return vel.diff(5)


def rfl_drv3_011_recovery_stalling_jerk(close: pd.Series) -> pd.Series:
    l = close.cummin()
    rec = (close - l) / l
    ma_rec = rec.rolling(21).mean()
    stalled = (rec < ma_rec).astype(int).groupby((rec >= ma_rec).cumsum()).cumsum()
    vel = stalled.diff(5)
    return vel.diff(5)


def rfl_drv3_012_recovery_velocity_decay_jerk(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    v = rf.diff(5)
    score = _safe_div(v, rf.rolling(63).std())
    vel = score.diff(5)
    return vel.diff(5)


def rfl_drv3_013_trough_test_failure_jerk(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 252)
    new_low = (close < l.shift(1)).astype(int).rolling(252).sum()
    bounce = (close > l.shift(1) * 1.05).astype(int).rolling(252).sum()
    ratio = _safe_div(new_low, bounce)
    vel = ratio.diff(5)
    return vel.diff(5)


def rfl_drv3_014_bounce_volume_div_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    in_dd = close < h
    up_v = volume.where((close > close.shift(1)) & in_dd).rolling(63).sum()
    dn_v = volume.where((close < close.shift(1)) & in_dd).rolling(63).sum()
    ratio = _safe_div(up_v, dn_v)
    vel = ratio.diff(5)
    return vel.diff(5)


def rfl_drv3_015_failed_breakout_jerk(close: pd.Series, high: pd.Series) -> pd.Series:
    h21 = high.rolling(21).max().shift(1)
    failed = (high > h21) & (close < h21)
    cnt = failed.rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def rfl_drv3_016_recovery_exhaustion_jerk(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(close == l).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - idx
    score = _safe_div(b, dsl + 1)
    vel = score.diff(5)
    return vel.diff(5)


def rfl_drv3_017_mktcap_lower_high_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    from scipy.signal import argrelextrema
    p_idx = argrelextrema(mc.values, np.greater, order=5)[0]
    is_lower = (mc.iloc[p_idx] < mc.iloc[p_idx].shift(1)).astype(int).rolling(252, min_periods=1).sum()
    vel = is_lower.reindex(close.index).ffill().diff(5)
    return vel.diff(5)


def rfl_drv3_018_fading_bounce_streak_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    h = close.rolling(21).max()
    failing = (ret > 0.01) & (close < h.shift(1))
    streak = failing.astype(int).groupby((failing == 0).cumsum()).cumsum()
    vel = streak.diff(5)
    return vel.diff(5)


def rfl_drv3_019_bounce_amplitude_decay_jerk(close: pd.Series) -> pd.Series:
    rec = _safe_div(close - _rolling_min(close, 21), _rolling_min(close, 21))
    idx = _safe_div(rec, rec.rolling(63).mean())
    vel = idx.diff(5)
    return vel.diff(5)


def rfl_drv3_020_failed_rally_vol_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_weak = volume.where((ret > 0) & (ret < 0.01)).rolling(63).mean()
    v_strong = volume.where(ret >= 0.02).rolling(63).mean()
    ratio = _safe_div(v_weak, v_strong)
    vel = ratio.diff(5)
    return vel.diff(5)


def rfl_drv3_021_recovery_trap_persist_jerk(close: pd.Series) -> pd.Series:
    ma5 = close.rolling(5).mean()
    ma21 = close.rolling(21).mean()
    dur = ((close > ma5) & (close < ma21)).astype(int).rolling(21).sum()
    vel = dur.diff(5)
    return vel.diff(5)


def rfl_drv3_022_bounce_to_new_low_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    b = (ret > 0.05).rolling(252).sum()
    l = (close == close.rolling(252).min()).astype(int).rolling(252).sum()
    ratio = _safe_div(b, l)
    vel = ratio.diff(5)
    return vel.diff(5)


def rfl_drv3_023_terminal_resistance_climax_jerk(close: pd.Series) -> pd.Series:
    lh = rfl_016_count_lower_highs_63d(close)
    b_vol = close.pct_change().where(close.pct_change() > 0).rolling(63).std()
    score = _safe_div(lh, b_vol + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def rfl_drv3_024_ath_drawdown_stalling_jerk(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    v = dd.diff(5).where(dd > 0.20)
    accel = v.diff(5)
    return accel.diff(5)


def rfl_drv3_025_recovery_failure_composite_jerk(close: pd.Series) -> pd.Series:
    score = rfl_075_recovery_failure_final_composite(close)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V14_A_REGISTRY = {
    "rfl_drv3_001_max_bounce_jerk": {"inputs": ["close"], "func": rfl_drv3_001_max_bounce_jerk},
    "rfl_drv3_002_bounce_intensity_jerk": {"inputs": ["close"], "func": rfl_drv3_002_bounce_intensity_jerk},
    "rfl_drv3_003_bounce_decay_jerk": {"inputs": ["close"], "func": rfl_drv3_003_bounce_decay_jerk},
    "rfl_drv3_004_count_lower_highs_jerk": {"inputs": ["close"], "func": rfl_drv3_004_count_lower_highs_jerk},
    "rfl_drv3_005_proximity_to_last_peak_jerk": {"inputs": ["close"], "func": rfl_drv3_005_proximity_to_last_peak_jerk},
    "rfl_drv3_006_bounce_failure_velocity_jerk": {"inputs": ["close"], "func": rfl_drv3_006_bounce_failure_velocity_jerk},
    "rfl_drv3_007_recovery_trap_jerk": {"inputs": ["close", "volume"], "func": rfl_drv3_007_recovery_trap_jerk},
    "rfl_drv3_008_ma_reclaim_failure_jerk": {"inputs": ["close"], "func": rfl_drv3_008_ma_reclaim_failure_jerk},
    "rfl_drv3_009_dead_cat_bounce_jerk": {"inputs": ["close"], "func": rfl_drv3_009_dead_cat_bounce_jerk},
    "rfl_drv3_010_consecutive_lower_peak_jerk": {"inputs": ["close"], "func": rfl_drv3_010_consecutive_lower_peak_jerk},
    "rfl_drv3_011_recovery_stalling_jerk": {"inputs": ["close"], "func": rfl_drv3_011_recovery_stalling_jerk},
    "rfl_drv3_012_recovery_velocity_decay_jerk": {"inputs": ["close"], "func": rfl_drv3_012_recovery_velocity_decay_jerk},
    "rfl_drv3_013_trough_test_failure_jerk": {"inputs": ["close"], "func": rfl_drv3_013_trough_test_failure_jerk},
    "rfl_drv3_014_bounce_volume_div_jerk": {"inputs": ["close", "volume"], "func": rfl_drv3_014_bounce_volume_div_jerk},
    "rfl_drv3_015_failed_breakout_jerk": {"inputs": ["close", "high"], "func": rfl_drv3_015_failed_breakout_jerk},
    "rfl_drv3_016_recovery_exhaustion_jerk": {"inputs": ["close"], "func": rfl_drv3_016_recovery_exhaustion_jerk},
    "rfl_drv3_017_mktcap_lower_high_jerk": {"inputs": ["close", "sharesbas"], "func": rfl_drv3_017_mktcap_lower_high_jerk},
    "rfl_drv3_018_fading_bounce_streak_jerk": {"inputs": ["close"], "func": rfl_drv3_018_fading_bounce_streak_jerk},
    "rfl_drv3_019_bounce_amplitude_decay_jerk": {"inputs": ["close"], "func": rfl_drv3_019_bounce_amplitude_decay_jerk},
    "rfl_drv3_020_failed_rally_vol_jerk": {"inputs": ["close", "volume"], "func": rfl_drv3_020_failed_rally_vol_jerk},
    "rfl_drv3_021_recovery_trap_persist_jerk": {"inputs": ["close"], "func": rfl_drv3_021_recovery_trap_persist_jerk},
    "rfl_drv3_022_bounce_to_new_low_jerk": {"inputs": ["close"], "func": rfl_drv3_022_bounce_to_new_low_jerk},
    "rfl_drv3_023_terminal_resistance_climax_jerk": {"inputs": ["close"], "func": rfl_drv3_023_terminal_resistance_climax_jerk},
    "rfl_drv3_024_ath_drawdown_stalling_jerk": {"inputs": ["close"], "func": rfl_drv3_024_ath_drawdown_stalling_jerk},
    "rfl_drv3_025_recovery_failure_composite_jerk": {"inputs": ["close"], "func": rfl_drv3_025_recovery_failure_composite_jerk},
}
