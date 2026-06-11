"""
24_volume_acceleration — 2nd Derivatives
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volume acceleration metrics (jerk proxy)
def vacc_drv2_001_volume_accel_5d_velocity(volume: pd.Series) -> pd.Series:
    # Change in volume acceleration
    a = _calculate_accel(volume, 5)
    return a.diff(5)


def vacc_drv2_002_accel_zscore_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    z = (a - a.rolling(252).mean()) / (a.rolling(252).std() + _EPS)
    return z.diff(5)


def vacc_drv2_003_volume_breakaway_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    a5 = _calculate_accel(volume, 5).abs()
    a21 = _calculate_accel(volume, 21).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = _safe_div(a5, a21) * dd
    return idx.diff(5)


def vacc_drv2_004_accel_climax_intensity_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return (a * dd).diff(5)


def vacc_drv2_005_mktcap_volume_accel_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * np.log(mc + _EPS)
    a = _calculate_accel(cv, 21)
    return a.diff(5)


def vacc_drv2_006_accel_regime_shift_velocity(volume: pd.Series) -> pd.Series:
    a21 = _calculate_accel(volume, 5).rolling(21).mean()
    a252 = _calculate_accel(volume, 5).rolling(252).mean().abs()
    rsi = _safe_div(a21, a252)
    return rsi.diff(5)


def vacc_drv2_007_accel_oscillator_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    a21 = a.rolling(21).mean()
    a63 = a.rolling(63).mean()
    osc = _safe_div(a21, a63) - 1.0
    return osc.diff(5)


def vacc_drv2_008_accel_stability_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = a.rolling(63).apply(_rsq, raw=True)
    return rs.diff(5)


def vacc_drv2_009_accel_reversal_climax_velocity(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    score = a * _safe_div(close, low)
    return score.diff(5)


def vacc_drv2_010_joint_pv_accel_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    va = _calculate_accel(volume, 21) / (volume.rolling(21).mean() + _EPS)
    pa = _calculate_accel(close, 21) / (close.rolling(21).mean() + _EPS)
    spr = va - pa
    return spr.diff(5)


def vacc_drv2_011_accel_per_dd_vel_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    va = _calculate_accel(volume, 5).abs()
    pv = np.log(close).diff(21).abs()
    ratio = _safe_div(va, pv + _EPS)
    return ratio.diff(5)


def vacc_drv2_012_mktcap_accel_zscore_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ma = _calculate_accel(mc, 21)
    z = (ma - ma.rolling(252).mean()) / (ma.rolling(252).std() + _EPS)
    return z.diff(5)


def vacc_drv2_013_accel_volatility_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 1)
    v = a.rolling(63).std()
    return v.diff(5)


def vacc_drv2_014_normalized_force_accel_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = close.diff(1) * volume
    a = _calculate_accel(fi, 21)
    return a.diff(5)


def vacc_drv2_015_accel_skewness_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    return a.rolling(252).skew().diff(5)


def vacc_drv2_016_accel_decay_velocity(volume: pd.Series) -> pd.Series:
    a5 = _calculate_accel(volume, 5)
    a21 = _calculate_accel(volume, 21)
    return (a5 - a21).diff(5)


def vacc_drv2_017_energy_density_accel_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ev = _safe_div(volume**2, close.pct_change().rolling(21).std())
    a = _calculate_accel(ev, 21)
    return a.diff(5)


def vacc_drv2_018_consecutive_down_accel_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    is_neg = (a < 0).astype(int)
    dur = is_neg.groupby((is_neg == 0).cumsum()).cumsum()
    return dur.diff(5)


def vacc_drv2_019_vva_climax_velocity(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    va = _calculate_accel(volume, 5)
    vva = va.diff(5)
    c_low = _safe_div(close, low)
    return (vva * c_low).diff(5)


def vacc_drv2_020_mktcap_per_turnover_accel_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ma = _calculate_accel(mc, 21)
    ta = _calculate_accel(_safe_div(volume, sharesbas), 21)
    ratio = _safe_div(ma, ta + _EPS)
    return ratio.diff(5)


def vacc_drv2_021_accel_regime_break_velocity(volume: pd.Series) -> pd.Series:
    v_accel = _calculate_accel(volume, 5) - _calculate_accel(volume, 63)
    return v_accel.diff(5)


def vacc_drv2_022_cumulative_accel_energy_velocity(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    energy = a.cumsum() / (a.abs().cumsum() + _EPS)
    return energy.diff(5)


def vacc_drv2_023_volume_accel_final_climax_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vacc_150_volume_accel_final_climax_index(close, volume)
    return score.diff(5)


def vacc_drv2_024_accel_at_ath_low_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    a = _calculate_accel(volume, 5)
    val = a.where(is_low).ffill()
    return val.diff(5)


def vacc_drv2_025_final_accel_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vacc_075_volume_acceleration_final_composite(close, volume)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V24_V_REGISTRY = {
    "vacc_drv2_001_volume_accel_5d_velocity": {"inputs": ["volume"], "func": vacc_drv2_001_volume_accel_5d_velocity},
    "vacc_drv2_002_accel_zscore_velocity": {"inputs": ["volume"], "func": vacc_drv2_002_accel_zscore_velocity},
    "vacc_drv2_003_volume_breakaway_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_003_volume_breakaway_velocity},
    "vacc_drv2_004_accel_climax_intensity_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_004_accel_climax_intensity_velocity},
    "vacc_drv2_005_mktcap_volume_accel_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_drv2_005_mktcap_volume_accel_velocity},
    "vacc_drv2_006_accel_regime_shift_velocity": {"inputs": ["volume"], "func": vacc_drv2_006_accel_regime_shift_velocity},
    "vacc_drv2_007_accel_oscillator_velocity": {"inputs": ["volume"], "func": vacc_drv2_007_accel_oscillator_velocity},
    "vacc_drv2_008_accel_stability_velocity": {"inputs": ["volume"], "func": vtr_drv2_008_accel_stability_velocity},
    "vacc_drv2_009_accel_reversal_climax_velocity": {"inputs": ["close", "volume", "low"], "func": vacc_drv2_009_accel_reversal_climax_velocity},
    "vacc_drv2_010_joint_pv_accel_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_010_joint_pv_accel_velocity},
    "vacc_drv2_011_accel_per_dd_vel_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_011_accel_per_dd_vel_velocity},
    "vacc_drv2_012_mktcap_accel_zscore_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_drv2_012_mktcap_accel_zscore_velocity},
    "vacc_drv2_013_accel_volatility_velocity": {"inputs": ["volume"], "func": vacc_drv2_013_accel_volatility_velocity},
    "vacc_drv2_014_normalized_force_accel_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_014_normalized_force_accel_velocity},
    "vacc_drv2_015_accel_skewness_velocity": {"inputs": ["volume"], "func": vacc_drv2_015_accel_skewness_velocity},
    "vacc_drv2_016_accel_decay_velocity": {"inputs": ["volume"], "func": vacc_drv2_016_accel_decay_velocity},
    "vacc_drv2_017_energy_density_accel_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_017_energy_density_accel_velocity},
    "vacc_drv2_018_consecutive_down_accel_velocity": {"inputs": ["volume"], "func": vacc_drv2_018_consecutive_down_accel_velocity},
    "vacc_drv2_019_vva_climax_velocity": {"inputs": ["close", "volume", "low"], "func": vacc_drv2_019_vva_climax_velocity},
    "vacc_drv2_020_mktcap_per_turnover_accel_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_drv2_020_mktcap_per_turnover_accel_velocity},
    "vacc_drv2_021_accel_regime_break_velocity": {"inputs": ["volume"], "func": vacc_drv2_021_accel_regime_break_velocity},
    "vacc_drv2_022_cumulative_accel_energy_velocity": {"inputs": ["volume"], "func": vacc_drv2_022_cumulative_accel_energy_velocity},
    "vacc_drv2_023_volume_accel_final_climax_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_023_volume_accel_final_climax_velocity},
    "vacc_drv2_024_accel_at_ath_low_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_024_accel_at_ath_low_velocity},
    "vacc_drv2_025_final_accel_composite_velocity": {"inputs": ["close", "volume"], "func": vacc_drv2_025_final_accel_composite_velocity},
}
