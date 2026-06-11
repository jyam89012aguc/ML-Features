"""
24_volume_acceleration — 3rd Derivatives
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


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of volume acceleration acceleration (jerk)
def vacc_drv3_001_volume_accel_5d_jerk(volume: pd.Series) -> pd.Series:
    # Rate of change of volume acceleration velocity
    a = _calculate_accel(volume, 5)
    vel = a.diff(5)
    return vel.diff(5)


def vacc_drv3_002_accel_zscore_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    z = (a - a.rolling(252).mean()) / (a.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vacc_drv3_003_volume_breakaway_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    a5 = _calculate_accel(volume, 5).abs()
    a21 = _calculate_accel(volume, 21).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = _safe_div(a5, a21) * dd
    vel = idx.diff(5)
    return vel.diff(5)


def vacc_drv3_004_accel_climax_intensity_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    val = a * dd
    vel = val.diff(5)
    return vel.diff(5)


def vacc_drv3_005_mktcap_volume_accel_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * np.log(mc + _EPS)
    a = _calculate_accel(cv, 21)
    vel = a.diff(5)
    return vel.diff(5)


def vacc_drv3_006_accel_regime_shift_jerk(volume: pd.Series) -> pd.Series:
    a21 = _calculate_accel(volume, 5).rolling(21).mean()
    a252 = _calculate_accel(volume, 5).rolling(252).mean().abs()
    rsi = _safe_div(a21, a252)
    vel = rsi.diff(5)
    return vel.diff(5)


def vacc_drv3_007_accel_oscillator_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    a21 = a.rolling(21).mean()
    a63 = a.rolling(63).mean()
    osc = _safe_div(a21, a63) - 1.0
    vel = osc.diff(5)
    return vel.diff(5)


def vacc_drv3_008_accel_stability_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = a.rolling(63).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def vacc_drv3_009_accel_reversal_climax_jerk(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    score = a * _safe_div(close, low + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vacc_drv3_010_joint_pv_accel_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    va = _calculate_accel(volume, 21) / (volume.rolling(21).mean() + _EPS)
    pa = _calculate_accel(close, 21) / (close.rolling(21).mean() + _EPS)
    spr = va - pa
    vel = spr.diff(5)
    return vel.diff(5)


def vacc_drv3_011_accel_per_dd_vel_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    va = _calculate_accel(volume, 5).abs()
    pv = np.log(close).diff(21).abs()
    ratio = _safe_div(va, pv + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vacc_drv3_012_mktcap_accel_zscore_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ma = _calculate_accel(mc, 21)
    z = (ma - ma.rolling(252).mean()) / (ma.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vacc_drv3_013_accel_volatility_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 1)
    v = a.rolling(63).std()
    vel = v.diff(5)
    return vel.diff(5)


def vacc_drv3_014_normalized_force_accel_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = close.diff(1) * volume
    a = _calculate_accel(fi, 21)
    vel = a.diff(5)
    return vel.diff(5)


def vacc_drv3_015_accel_skewness_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    vel = a.rolling(252).skew().diff(5)
    return vel.diff(5)


def vacc_drv3_016_accel_decay_jerk(volume: pd.Series) -> pd.Series:
    a5 = _calculate_accel(volume, 5)
    a21 = _calculate_accel(volume, 21)
    vel = (a5 - a21).diff(5)
    return vel.diff(5)


def vacc_drv3_017_energy_density_accel_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ev = _safe_div(volume**2, close.pct_change().rolling(21).std())
    a = _calculate_accel(ev, 21)
    vel = a.diff(5)
    return vel.diff(5)


def vacc_drv3_018_consecutive_down_accel_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    is_neg = (a < 0).astype(int)
    dur = is_neg.groupby((is_neg == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vacc_drv3_019_vva_climax_jerk(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    va = _calculate_accel(volume, 5)
    vva = va.diff(5)
    c_low = _safe_div(close, low)
    vel = (vva * c_low).diff(5)
    return vel.diff(5)


def vacc_drv3_020_mktcap_per_turnover_accel_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ma = _calculate_accel(mc, 21)
    ta = _calculate_accel(_safe_div(volume, sharesbas), 21)
    ratio = _safe_div(ma, ta + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vacc_drv3_021_accel_regime_break_jerk(volume: pd.Series) -> pd.Series:
    v_accel = _calculate_accel(volume, 5) - _calculate_accel(volume, 63)
    vel = v_accel.diff(5)
    return vel.diff(5)


def vacc_drv3_022_cumulative_accel_energy_jerk(volume: pd.Series) -> pd.Series:
    a = _calculate_accel(volume, 5)
    energy = a.cumsum() / (a.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vacc_drv3_023_volume_accel_final_climax_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    score = vacc_150_volume_accel_final_climax_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vacc_drv3_024_accel_at_ath_low_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    a = _calculate_accel(volume, 5)
    val = a.where(is_low).ffill()
    vel = val.diff(5)
    return vel.diff(5)


def vacc_drv3_025_final_accel_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vacc_075_volume_acceleration_final_composite(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V24_A_REGISTRY = {
    "vacc_drv3_001_volume_accel_5d_jerk": {"inputs": ["volume"], "func": vacc_drv3_001_volume_accel_5d_jerk},
    "vacc_drv3_002_accel_zscore_jerk": {"inputs": ["volume"], "func": vacc_drv3_002_accel_zscore_jerk},
    "vacc_drv3_003_volume_breakaway_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_003_volume_breakaway_jerk},
    "vacc_drv3_004_accel_climax_intensity_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_004_accel_climax_intensity_jerk},
    "vacc_drv3_005_mktcap_volume_accel_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_drv3_005_mktcap_volume_accel_jerk},
    "vacc_drv3_006_accel_regime_shift_jerk": {"inputs": ["volume"], "func": vacc_drv3_006_accel_regime_shift_jerk},
    "vacc_drv3_007_accel_oscillator_jerk": {"inputs": ["volume"], "func": vacc_drv3_007_accel_oscillator_jerk},
    "vacc_drv3_008_accel_stability_jerk": {"inputs": ["volume"], "func": vacc_drv3_008_accel_stability_jerk},
    "vacc_drv3_009_accel_reversal_climax_jerk": {"inputs": ["close", "volume", "low"], "func": vacc_drv3_009_accel_reversal_climax_jerk},
    "vacc_drv3_010_joint_pv_accel_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_010_joint_pv_accel_jerk},
    "vacc_drv3_011_accel_per_dd_vel_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_011_accel_per_dd_vel_jerk},
    "vacc_drv3_012_mktcap_accel_zscore_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_drv3_012_mktcap_accel_zscore_jerk},
    "vacc_drv3_013_accel_volatility_jerk": {"inputs": ["volume"], "func": vacc_drv3_013_accel_volatility_jerk},
    "vacc_drv3_014_normalized_force_accel_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_014_normalized_force_accel_jerk},
    "vacc_drv3_015_accel_skewness_jerk": {"inputs": ["volume"], "func": vacc_drv3_015_accel_skewness_jerk},
    "vacc_drv3_016_accel_decay_jerk": {"inputs": ["volume"], "func": vacc_drv3_016_accel_decay_jerk},
    "vacc_drv3_017_energy_density_accel_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_017_energy_density_accel_jerk},
    "vacc_drv3_018_consecutive_down_accel_jerk": {"inputs": ["volume"], "func": vacc_drv3_018_consecutive_down_accel_jerk},
    "vacc_drv3_019_vva_climax_jerk": {"inputs": ["close", "volume", "low"], "func": vacc_drv3_019_vva_climax_jerk},
    "vacc_drv3_020_mktcap_per_turnover_accel_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vacc_drv3_020_mktcap_per_turnover_accel_jerk},
    "vacc_drv3_021_accel_regime_break_jerk": {"inputs": ["volume"], "func": vacc_drv3_021_accel_regime_break_jerk},
    "vacc_drv3_022_cumulative_accel_energy_jerk": {"inputs": ["volume"], "func": vacc_drv3_022_cumulative_accel_energy_jerk},
    "vacc_drv3_023_volume_accel_final_climax_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_023_volume_accel_final_climax_jerk},
    "vacc_drv3_024_accel_at_ath_low_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_024_accel_at_ath_low_jerk},
    "vacc_drv3_025_final_accel_composite_jerk": {"inputs": ["close", "volume"], "func": vacc_drv3_025_final_accel_composite_jerk},
}
