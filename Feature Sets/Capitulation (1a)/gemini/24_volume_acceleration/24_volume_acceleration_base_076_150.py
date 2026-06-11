"""
24_volume_acceleration — Base Features 076–150
Domain: second derivative of volume, breakaway flush
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Distribution of Volume Acceleration
def vacc_076_accel_volatility_63d(volume: pd.Series) -> pd.Series:
    # Std dev of daily acceleration values
    a = _calculate_accel(volume, 1)
    return a.rolling(63).std() / _rolling_mean(volume, 252)


def vacc_077_accel_zscore_ath(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    return (a - a.expanding().mean()) / (a.expanding().std() + _EPS)


# 091-105: Climax Acceleration Timing and Ranks
def vacc_091_days_since_peak_accel_252d(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5).abs()
    idx = a.rolling(252).apply(np.argmax, raw=True)
    return 252 - 1 - idx


def vacc_092_count_accel_spikes_63d(volume: pd.Series) -> pd.Series:
    # Number of days with acceleration > 2.5 standard deviations
    a = _calculate_accel(volume, 5)
    threshold = a.rolling(252).mean() + 2.5 * a.rolling(252).std()
    return (a > threshold).rolling(63).sum()


# 106-125: Specialized Flow Accelerators
def vacc_106_normalized_volume_force_accel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Accel of (Price Change * Volume)
    fi = close.diff(1) * volume
    return _calculate_accel(fi, 21) / (fi.rolling(63).std() + _EPS)


def vacc_107_volume_accel_at_new_ath_low(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volume acceleration on the day of an absolute multi-year low
    l = close.cummin()
    is_low = (close == l)
    a = _calculate_accel(volume, 5)
    return a.where(is_low).ffill()


# 126-140: Multi-Horizon Acceleration Oscillators
def vacc_126_accel_spread_short_long(volume: pd.Series) -> pd.Series:
    a_s = _calculate_accel(volume, 5)
    a_l = _calculate_accel(volume, 63)
    return a_s - a_l


def vacc_127_accel_to_climax_ratio_63d(volume: pd.Series) -> pd.Series:
    # Current accel / Max volume spike ratio in window
    a = _calculate_accel(volume, 5).abs()
    v_rat = _safe_div(volume, _rolling_median(volume, 252)).rolling(63).max()
    return _safe_div(a, v_rat)


# 141-150: Final Volume Acceleration composites
def vacc_141_acceleration_exhaustion_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Volume Accel) / (Price Velocity) -> looking for volume speeding up without price
    va = _calculate_accel(volume, 5).abs()
    pv = np.log(close).diff(5).abs()
    return _safe_div(va, pv + _EPS)


def vacc_142_energy_density_acceleration_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Change in (Volume^2 / Price Volatility)
    ev = _safe_div(volume**2, close.pct_change().rolling(21).std())
    return _calculate_accel(ev, 21)


def vacc_143_consecutive_down_accel_days(volume: pd.Series) -> pd.Series:
    # Consecutive days where volume acceleration is negative (slowing down)
    a = _calculate_accel(volume, 5)
    is_neg = (a < 0).astype(int)
    return is_neg.groupby((is_neg == 0).cumsum()).cumsum()


def vacc_144_volume_accel_reversal_climax(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    # (Volume Accel Change) * (Close from Low)
    va = _calculate_accel(volume, 5)
    vva = va.diff(5)
    c_low = _safe_div(close, low)
    return vva * c_low


def vacc_145_mktcap_accel_per_turnover_accel(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ma = _calculate_accel(mc, 21)
    ta = _calculate_accel(_safe_div(volume, sharesbas), 21)
    return _safe_div(ma, ta + _EPS)


def vacc_146_years_since_max_accel_ath(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5).abs()
    idx = a.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(volume)), index=volume.index) - idx) / 252.0


def vacc_147_volume_accel_regime_break_63d(volume: pd.Series) -> pd.Series:
    # Accel(5d) - Accel(63d)
    return _calculate_accel(volume, 5) - _calculate_accel(volume, 63)


def vacc_148_consecutive_days_accel_gt_median(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    med = a.rolling(252).median()
    is_high = (a > med).astype(int)
    return is_high.groupby((is_high == 0).cumsum()).cumsum()


def vacc_149_cumulative_accel_energy_ath(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    return a.cumsum() / (a.abs().cumsum() + _EPS)


def vacc_150_volume_accel_final_climax_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Volume Accel) * (1 - Recovery Fraction) * (Drawdown Depth)
    va = _calculate_accel(volume, 5).abs()
    l = close.rolling(252).min()
    h = close.rolling(252).max()
    rf = _safe_div(close - l, h - l)
    dd = (h - close) / h
    return va * (1.0 - rf) * dd


# ── Registry ──────────────────────────────────────────────────────────────────

V24_REGISTRY = {
    "vacc_076_accel_volatility_63d": {"inputs": ["volume"], "func": vacc_076_accel_volatility_63d},
    "vacc_077_accel_zscore_ath": {"inputs": ["volume"], "func": vacc_077_accel_zscore_ath},
    "vacc_091_days_since_peak_accel_252d": {"inputs": ["volume"], "func": vacc_091_days_since_peak_accel_252d},
    "vacc_092_count_accel_spikes_63d": {"inputs": ["volume"], "func": vacc_092_count_accel_spikes_63d},
    "vacc_106_normalized_volume_force_accel_63d": {"inputs": ["close", "volume"], "func": vacc_106_normalized_volume_force_accel_63d},
    "vacc_107_volume_accel_at_new_ath_low": {"inputs": ["close", "volume"], "func": vacc_107_volume_accel_at_new_ath_low},
    "vacc_126_accel_spread_short_long": {"inputs": ["volume"], "func": vacc_126_accel_spread_short_long},
    "vacc_127_accel_to_climax_ratio_63d": {"inputs": ["volume"], "func": vacc_127_accel_to_climax_ratio_63d},
    "vacc_141_acceleration_exhaustion_score_21d": {"inputs": ["close", "volume"], "func": vacc_141_acceleration_exhaustion_score_21d},
    "vacc_142_energy_density_acceleration_63d": {"inputs": ["close", "volume"], "func": vacc_142_energy_density_acceleration_63d},
    "vacc_143_consecutive_down_accel_days": {"inputs": ["volume"], "func": vacc_143_consecutive_down_accel_days},
    "vacc_144_volume_accel_reversal_climax": {"inputs": ["close", "volume", "low"], "func": vacc_144_volume_accel_reversal_climax},
    "vacc_145_mktcap_per_turnover_accel": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_145_mktcap_accel_per_turnover_accel},
    "vacc_146_years_since_max_accel_ath": {"inputs": ["volume"], "func": vacc_146_years_since_max_accel_ath},
    "vacc_147_volume_accel_regime_break_63d": {"inputs": ["volume"], "func": vacc_147_volume_accel_regime_break_63d},
    "vacc_148_consecutive_days_accel_gt_median": {"inputs": ["volume"], "func": vacc_148_consecutive_days_accel_gt_median},
    "vacc_149_cumulative_accel_energy_ath": {"inputs": ["volume"], "func": vacc_149_cumulative_accel_energy_ath},
    "vacc_150_volume_accel_final_climax_index": {"inputs": ["close", "volume"], "func": vacc_150_volume_accel_final_climax_index},
}
