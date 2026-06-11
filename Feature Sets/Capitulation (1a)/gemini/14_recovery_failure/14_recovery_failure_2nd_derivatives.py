"""
14_recovery_failure — 2nd Derivatives
Domain: rate of change of base features — captures acceleration of decline/distress
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

# 25 features capturing acceleration of recovery failure metrics
def rfl_drv2_001_max_bounce_velocity(close: pd.Series) -> pd.Series:
    # Change in max bounce magnitude
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    return b.diff(5)


def rfl_drv2_002_bounce_intensity_velocity(close: pd.Series) -> pd.Series:
    curr_l = _rolling_min(close, 63)
    curr_b = _safe_div(close - curr_l, curr_l)
    mx_b = (curr_b).rolling(252).max()
    ratio = _safe_div(curr_b, mx_b)
    return ratio.diff(5)


def rfl_drv2_003_bounce_decay_velocity(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = b.rolling(252).apply(_slope, raw=True)
    return sl.diff(5)


def rfl_drv2_004_count_lower_highs_velocity(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=5)[0]
    peaks = close.iloc[peaks_idx]
    is_lower = (peaks < peaks.shift(1)).astype(int).rolling(63, min_periods=1).sum()
    return is_lower.reindex(close.index).ffill().diff(5)


def rfl_drv2_005_proximity_to_last_peak_velocity(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=5)[0]
    last_peak = close.iloc[peaks_idx].reindex(close.index).ffill()
    p = _safe_div(close, last_peak)
    return p.diff(5)


def rfl_drv2_006_bounce_failure_velocity_accel(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    peak_val = b.rolling(21).max().ffill()
    v = (b - peak_val).diff(5)
    return v.diff(5)


def rfl_drv2_007_recovery_trap_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = _rolling_min(close, 21)
    b = _safe_div(close - l, l)
    v_norm = _safe_div(volume, volume.rolling(63).mean())
    dur = (close > l * 1.02).astype(int).rolling(21).sum()
    idx = _safe_div(b * v_norm, dur)
    return idx.diff(5)


def rfl_drv2_008_ma_reclaim_failure_velocity(close: pd.Series) -> pd.Series:
    ma = close.rolling(50).mean()
    crossed = (close > ma) & (close.shift(1) <= ma.shift(1))
    failed = (close < ma) & crossed.shift(3)
    cnt = failed.rolling(63).sum()
    return cnt.diff(5)


def rfl_drv2_009_dead_cat_bounce_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(63).max()
    l = close.rolling(63).min()
    fall = (h - l) / h
    bounce = (close - l) / l
    score = _safe_div(fall, bounce)
    return score.diff(5)


def rfl_drv2_010_consecutive_lower_peak_velocity(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    peaks_idx = argrelextrema(close.values, np.greater, order=10)[0]
    peaks = close.iloc[peaks_idx]
    is_lower = (peaks < peaks.shift(1)).astype(int)
    streak = is_lower.groupby((is_lower == 0).cumsum()).cumsum()
    return streak.reindex(close.index).ffill().diff(5)


def rfl_drv2_011_recovery_stalling_velocity(close: pd.Series) -> pd.Series:
    l = close.cummin()
    rec = (close - l) / l
    ma_rec = rec.rolling(21).mean()
    stalled = (rec < ma_rec).astype(int).groupby((rec >= ma_rec).cumsum()).cumsum()
    return stalled.diff(5)


def rfl_drv2_012_recovery_velocity_decay_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    v = rf.diff(5)
    score = _safe_div(v, rf.rolling(63).std())
    return score.diff(5)


def rfl_drv2_013_trough_test_failure_velocity(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 252)
    new_low = (close < l.shift(1)).astype(int).rolling(252).sum()
    bounce = (close > l.shift(1) * 1.05).astype(int).rolling(252).sum()
    ratio = _safe_div(new_low, bounce)
    return ratio.diff(5)


def rfl_drv2_014_bounce_volume_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    in_dd = close < h
    up_v = volume.where((close > close.shift(1)) & in_dd).rolling(63).sum()
    dn_v = volume.where((close < close.shift(1)) & in_dd).rolling(63).sum()
    ratio = _safe_div(up_v, dn_v)
    return ratio.diff(5)


def rfl_drv2_015_failed_breakout_velocity(close: pd.Series, high: pd.Series) -> pd.Series:
    h21 = high.rolling(21).max().shift(1)
    failed = (high > h21) & (close < h21)
    cnt = failed.rolling(252).sum()
    return cnt.diff(5)


def rfl_drv2_016_recovery_exhaustion_velocity(close: pd.Series) -> pd.Series:
    l = _rolling_min(close, 63)
    b = _safe_div(close - l, l)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(close == l).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - idx
    score = _safe_div(b, dsl + 1)
    return score.diff(5)


def rfl_drv2_017_mktcap_lower_high_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    from scipy.signal import argrelextrema
    p_idx = argrelextrema(mc.values, np.greater, order=5)[0]
    is_lower = (mc.iloc[p_idx] < mc.iloc[p_idx].shift(1)).astype(int).rolling(252, min_periods=1).sum()
    return is_lower.reindex(close.index).ffill().diff(5)


def rfl_drv2_018_fading_bounce_streak_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    h = close.rolling(21).max()
    failing = (ret > 0.01) & (close < h.shift(1))
    streak = failing.astype(int).groupby((failing == 0).cumsum()).cumsum()
    return streak.diff(5)


def rfl_drv2_019_bounce_amplitude_decay_velocity(close: pd.Series) -> pd.Series:
    rec = _safe_div(close - _rolling_min(close, 21), _rolling_min(close, 21))
    idx = _safe_div(rec, rec.rolling(63).mean())
    return idx.diff(5)


def rfl_drv2_020_failed_rally_vol_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_weak = volume.where((ret > 0) & (ret < 0.01)).rolling(63).mean()
    v_strong = volume.where(ret >= 0.02).rolling(63).mean()
    ratio = _safe_div(v_weak, v_strong)
    return ratio.diff(5)


def rfl_drv2_021_recovery_trap_persist_velocity(close: pd.Series) -> pd.Series:
    ma5 = close.rolling(5).mean()
    ma21 = close.rolling(21).mean()
    dur = ((close > ma5) & (close < ma21)).astype(int).rolling(21).sum()
    return dur.diff(5)


def rfl_drv2_022_bounce_to_new_low_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    b = (ret > 0.05).rolling(252).sum()
    l = (close == close.rolling(252).min()).astype(int).rolling(252).sum()
    ratio = _safe_div(b, l)
    return ratio.diff(5)


def rfl_drv2_023_terminal_resistance_climax_velocity(close: pd.Series) -> pd.Series:
    lh = rfl_016_count_lower_highs_63d(close)
    b_vol = close.pct_change().where(close.pct_change() > 0).rolling(63).std()
    score = _safe_div(lh, b_vol + _EPS)
    return score.diff(5)


def rfl_drv2_024_ath_drawdown_stalling_accel(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    v = dd.diff(5).where(dd > 0.20)
    return v.diff(5)


def rfl_drv2_025_recovery_failure_composite_velocity(close: pd.Series) -> pd.Series:
    score = rfl_075_recovery_failure_final_composite(close)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V14_V_REGISTRY = {
    "rfl_drv2_001_max_bounce_velocity": {"inputs": ["close"], "func": rfl_drv2_001_max_bounce_velocity},
    "rfl_drv2_002_bounce_intensity_velocity": {"inputs": ["close"], "func": rfl_drv2_002_bounce_intensity_velocity},
    "rfl_drv2_003_bounce_decay_velocity": {"inputs": ["close"], "func": rfl_drv2_003_bounce_decay_velocity},
    "rfl_drv2_004_count_lower_highs_velocity": {"inputs": ["close"], "func": rfl_drv2_004_count_lower_highs_velocity},
    "rfl_drv2_005_proximity_to_last_peak_velocity": {"inputs": ["close"], "func": rfl_drv2_005_proximity_to_last_peak_velocity},
    "rfl_drv2_006_bounce_failure_velocity_accel": {"inputs": ["close"], "func": rfl_drv2_006_bounce_failure_velocity_accel},
    "rfl_drv2_007_recovery_trap_velocity": {"inputs": ["close", "volume"], "func": rfl_drv2_007_recovery_trap_velocity},
    "rfl_drv2_008_ma_reclaim_failure_velocity": {"inputs": ["close"], "func": rfl_drv2_008_ma_reclaim_failure_velocity},
    "rfl_drv2_009_dead_cat_bounce_velocity": {"inputs": ["close"], "func": rfl_drv2_009_dead_cat_bounce_velocity},
    "rfl_drv2_010_consecutive_lower_peak_velocity": {"inputs": ["close"], "func": rfl_drv2_010_consecutive_lower_peak_velocity},
    "rfl_drv2_011_recovery_stalling_velocity": {"inputs": ["close"], "func": rfl_drv2_011_recovery_stalling_velocity},
    "rfl_drv2_012_recovery_velocity_decay_velocity": {"inputs": ["close"], "func": rfl_drv2_012_recovery_velocity_decay_velocity},
    "rfl_drv2_013_trough_test_failure_velocity": {"inputs": ["close"], "func": rfl_drv2_013_trough_test_failure_velocity},
    "rfl_drv2_014_bounce_volume_div_velocity": {"inputs": ["close", "volume"], "func": rfl_drv2_014_bounce_volume_div_velocity},
    "rfl_drv2_015_failed_breakout_velocity": {"inputs": ["close", "high"], "func": rfl_drv2_015_failed_breakout_velocity},
    "rfl_drv2_016_recovery_exhaustion_velocity": {"inputs": ["close"], "func": rfl_drv2_016_recovery_exhaustion_velocity},
    "rfl_drv2_017_mktcap_lower_high_velocity": {"inputs": ["close", "sharesbas"], "func": rfl_drv2_017_mktcap_lower_high_velocity},
    "rfl_drv2_018_fading_bounce_streak_velocity": {"inputs": ["close"], "func": rfl_drv2_018_fading_bounce_streak_velocity},
    "rfl_drv2_019_bounce_amplitude_decay_velocity": {"inputs": ["close"], "func": rfl_drv2_019_bounce_amplitude_decay_velocity},
    "rfl_drv2_020_failed_rally_vol_velocity": {"inputs": ["close", "volume"], "func": rfl_drv2_020_failed_rally_vol_velocity},
    "rfl_drv2_021_recovery_trap_persist_velocity": {"inputs": ["close"], "func": rfl_drv2_021_recovery_trap_persist_velocity},
    "rfl_drv2_022_bounce_to_new_low_velocity": {"inputs": ["close"], "func": rfl_drv2_022_bounce_to_new_low_velocity},
    "rfl_drv2_023_terminal_resistance_climax_velocity": {"inputs": ["close"], "func": rfl_drv2_023_terminal_resistance_climax_velocity},
    "rfl_drv2_024_ath_drawdown_stalling_accel": {"inputs": ["close"], "func": rfl_drv2_024_ath_drawdown_stalling_accel},
    "rfl_drv2_025_recovery_failure_composite_velocity": {"inputs": ["close"], "func": rfl_drv2_025_recovery_failure_composite_velocity},
}
