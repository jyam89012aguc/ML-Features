"""
30_volatility_acceleration — 2nd Derivatives
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


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volatility acceleration metrics (jerk proxy)
def vtac_drv2_001_vol_accel_5d_velocity(close: pd.Series) -> pd.Series:
    # Rate of change of 5-day volatility acceleration
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    return a.diff(5)


def vtac_drv2_002_vol_accel_zscore_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 5)
    z = (a - a.rolling(252).mean()) / (a.rolling(252).std() + _EPS)
    return z.diff(5)


def vtac_drv2_003_vol_breakaway_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a5 = _calculate_accel(v, 5).abs()
    a21 = _calculate_accel(v, 21).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = _safe_div(a5, a21) * dd
    return idx.diff(5)


def vtac_drv2_004_vol_accel_climax_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return (a * dd).diff(5)


def vtac_drv2_005_mktcap_vol_accel_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 21)
    return a.diff(5)


def vtac_drv2_006_vol_accel_regime_shift_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a21 = _calculate_accel(v, 5).rolling(21).mean()
    a252 = _calculate_accel(v, 5).rolling(252).mean().abs()
    rsi = _safe_div(a21, a252)
    return rsi.diff(5)


def vtac_drv2_007_vol_accel_oscillator_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    a21 = a.rolling(21).mean()
    a63 = a.rolling(63).mean()
    osc = _safe_div(a21, a63) - 1.0
    return osc.diff(5)


def vtac_drv2_008_vol_accel_stability_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = a.rolling(63).apply(_rsq, raw=True)
    return rs.diff(5)


def vtac_drv2_009_vol_accel_reversal_velocity(close: pd.Series, low: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    score = a * _safe_div(close, low)
    return score.diff(5)


def vtac_drv2_010_vix_proxy_accel_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    a = _calculate_accel(ratio, 5)
    return a.diff(5)


def vtac_drv2_011_joint_range_vol_accel_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r = (high - low) / (close + _EPS)
    ra = _calculate_accel(r, 21)
    va = _calculate_accel(np.log(close / close.shift(1)).rolling(21).std(), 21)
    spr = ra - va
    return spr.diff(5)


def vtac_drv2_012_vol_accel_per_dd_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5).abs()
    pv = np.log(close).diff(21).abs()
    ratio = _safe_div(va, pv + _EPS)
    return ratio.diff(5)


def vtac_drv2_013_mktcap_vol_accel_zscore_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    mv = np.log(mc / mc.shift(1)).rolling(21).std()
    ma = _calculate_accel(mv, 21)
    z = (ma - ma.rolling(252).mean()) / (ma.rolling(252).std() + _EPS)
    return z.diff(5)


def vtac_drv2_014_vol_accel_volatility_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 1)
    v_a = a.rolling(63).std()
    return v_a.diff(5)


def vtac_drv2_015_vol_accel_skewness_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    return a.rolling(252).skew().diff(5)


def vtac_drv2_016_vol_accel_decay_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1))
    a5 = _calculate_accel(v.rolling(5).std(), 5)
    a21 = _calculate_accel(v.rolling(21).std(), 21)
    return (a5 - a21).diff(5)


def vtac_drv2_017_vol_energy_density_accel_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    ed = (v**2) * v_rat
    a = _calculate_accel(ed, 21)
    return a.diff(5)


def vtac_drv2_018_consecutive_vol_accel_streak_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    is_high = (a > a.rolling(252).median()).astype(int)
    dur = is_high.groupby((is_high == 0).cumsum()).cumsum()
    return dur.diff(5)


def vtac_drv2_019_vva_climax_velocity(close: pd.Series, low: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5)
    vva = va.diff(5)
    score = vva * _safe_div(close, low)
    return score.diff(5)


def vtac_drv2_020_vol_accel_norm_depth_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    ratio = _safe_div(va, dd + _EPS)
    return ratio.diff(5)


def vtac_drv2_021_vol_accel_regime_break_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    brk = _calculate_accel(v, 5) - _calculate_accel(v, 63)
    return brk.diff(5)


def vtac_drv2_022_cumulative_vol_accel_energy_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    energy = a.cumsum() / (a.abs().cumsum() + _EPS)
    return energy.diff(5)


def vtac_drv2_023_vol_accel_final_climax_velocity(close: pd.Series) -> pd.Series:
    score = vtac_150_vol_accel_final_climax_index(close)
    return score.diff(5)


def vtac_drv2_024_vol_accel_at_ath_low_velocity(close: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    val = a.where(is_low).ffill()
    return val.diff(5)


def vtac_drv2_025_vol_accel_composite_velocity(close: pd.Series) -> pd.Series:
    score = vtac_075_vol_acceleration_final_composite(close)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V30_V_REGISTRY = {
    "vtac_drv2_001_vol_accel_5d_velocity": {"inputs": ["close"], "func": vtac_drv2_001_vol_accel_5d_velocity},
    "vtac_drv2_002_vol_accel_zscore_velocity": {"inputs": ["close"], "func": vtac_drv2_002_vol_accel_zscore_velocity},
    "vtac_drv2_003_vol_breakaway_velocity": {"inputs": ["close"], "func": vtac_drv2_003_vol_breakaway_velocity},
    "vtac_drv2_004_vol_accel_climax_velocity": {"inputs": ["close"], "func": vtac_drv2_004_vol_accel_climax_velocity},
    "vtac_drv2_005_mktcap_vol_accel_velocity": {"inputs": ["close", "sharesbas"], "func": vtac_drv2_005_mktcap_vol_accel_velocity},
    "vtac_drv2_006_vol_accel_regime_shift_velocity": {"inputs": ["close"], "func": vtac_drv2_006_vol_accel_regime_shift_velocity},
    "vtac_drv2_007_vol_accel_oscillator_velocity": {"inputs": ["close"], "func": vtac_drv2_007_vol_accel_oscillator_velocity},
    "vtac_drv2_008_vol_accel_stability_velocity": {"inputs": ["close"], "func": vtac_drv2_008_vol_accel_stability_velocity},
    "vtac_drv2_009_vol_accel_reversal_velocity": {"inputs": ["close", "low"], "func": vtac_drv2_009_vol_accel_reversal_velocity},
    "vtac_drv2_010_vix_proxy_accel_velocity": {"inputs": ["close"], "func": vtac_drv2_010_vix_proxy_accel_velocity},
    "vtac_drv2_011_joint_range_vol_accel_velocity": {"inputs": ["high", "low", "close"], "func": vtac_drv2_011_joint_range_vol_accel_velocity},
    "vtac_drv2_012_vol_accel_per_dd_velocity": {"inputs": ["close"], "func": vtac_drv2_012_vol_accel_per_dd_velocity},
    "vtac_drv2_013_mktcap_vol_accel_zscore_velocity": {"inputs": ["close", "sharesbas"], "func": vtac_drv2_013_mktcap_vol_accel_zscore_velocity},
    "vtac_drv2_014_vol_accel_volatility_velocity": {"inputs": ["close"], "func": vtac_drv2_014_vol_accel_volatility_velocity},
    "vtac_drv2_015_vol_accel_skewness_velocity": {"inputs": ["close"], "func": vtac_drv2_015_vol_accel_skewness_velocity},
    "vtac_drv2_016_vol_accel_decay_velocity": {"inputs": ["close"], "func": vtac_drv2_016_vol_accel_decay_velocity},
    "vtac_drv2_017_vol_energy_density_accel_velocity": {"inputs": ["close", "volume"], "func": vtac_drv2_017_vol_energy_density_accel_velocity},
    "vtac_drv2_018_consecutive_vol_accel_streak_velocity": {"inputs": ["close"], "func": vtac_drv2_018_consecutive_vol_accel_streak_velocity},
    "vtac_drv2_019_vva_climax_velocity": {"inputs": ["close", "low"], "func": vtac_drv2_019_vva_climax_velocity},
    "vtac_drv2_020_vol_accel_norm_depth_velocity": {"inputs": ["close"], "func": vtac_drv2_020_vol_accel_norm_depth_velocity},
    "vtac_drv2_021_vol_accel_regime_break_velocity": {"inputs": ["close"], "func": vtac_drv2_021_vol_accel_regime_break_velocity},
    "vtac_drv2_022_cumulative_vol_accel_energy_velocity": {"inputs": ["close"], "func": vtac_drv2_022_cumulative_vol_accel_energy_velocity},
    "vtac_drv2_023_vol_accel_final_climax_velocity": {"inputs": ["close"], "func": vtac_drv2_023_vol_accel_final_climax_velocity},
    "vtac_drv2_024_vol_accel_at_ath_low_velocity": {"inputs": ["close"], "func": vtac_drv2_024_vol_accel_at_ath_low_velocity},
    "vtac_drv2_025_vol_accel_composite_velocity": {"inputs": ["close"], "func": vtac_drv2_025_vol_accel_composite_velocity},
}
