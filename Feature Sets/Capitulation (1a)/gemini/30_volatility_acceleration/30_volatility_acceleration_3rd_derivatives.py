"""
30_volatility_acceleration — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volatility acceleration acceleration (jerk)
def vtac_drv3_001_vol_accel_5d_jerk(close: pd.Series) -> pd.Series:
    # Rate of change of volatility acceleration velocity
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    vel = a.diff(5)
    return vel.diff(5)


def vtac_drv3_002_vol_accel_zscore_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 5)
    z = (a - a.rolling(252).mean()) / (a.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vtac_drv3_003_vol_breakaway_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a5 = _calculate_accel(v, 5).abs()
    a21 = _calculate_accel(v, 21).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = _safe_div(a5, a21) * dd
    vel = idx.diff(5)
    return vel.diff(5)


def vtac_drv3_004_vol_accel_climax_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    val = a * dd
    vel = val.diff(5)
    return vel.diff(5)


def vtac_drv3_005_mktcap_vol_accel_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    a = _calculate_accel(v, 21)
    vel = a.diff(5)
    return vel.diff(5)


def vtac_drv3_006_vol_accel_regime_shift_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a21 = _calculate_accel(v, 5).rolling(21).mean()
    a252 = _calculate_accel(v, 5).rolling(252).mean().abs()
    rsi = _safe_div(a21, a252)
    vel = rsi.diff(5)
    return vel.diff(5)


def vtac_drv3_007_vol_accel_oscillator_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    a21 = a.rolling(21).mean()
    a63 = a.rolling(63).mean()
    osc = _safe_div(a21, a63) - 1.0
    vel = osc.diff(5)
    return vel.diff(5)


def vtac_drv3_008_vol_accel_stability_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = a.rolling(63).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def vsk_drv3_009_vol_accel_reversal_jerk(close: pd.Series, low: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    score = a * _safe_div(close, low + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vtac_drv3_010_vix_proxy_accel_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    a = _calculate_accel(ratio, 5)
    vel = a.diff(5)
    return vel.diff(5)


def vtac_drv3_011_joint_range_vol_accel_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r = (high - low) / (close + _EPS)
    ra = _calculate_accel(r, 21)
    va = _calculate_accel(np.log(close / close.shift(1)).rolling(21).std(), 21)
    spr = ra - va
    vel = spr.diff(5)
    return vel.diff(5)


def vtac_drv3_012_vol_accel_per_dd_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5).abs()
    pv = np.log(close).diff(21).abs()
    ratio = _safe_div(va, pv + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vtac_drv3_013_mktcap_vol_accel_zscore_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    mv = np.log(mc / mc.shift(1)).rolling(21).std()
    ma = _calculate_accel(mv, 21)
    z = (ma - ma.rolling(252).mean()) / (ma.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vtac_drv3_014_vol_accel_volatility_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 1)
    v_a = a.rolling(63).std()
    vel = v_a.diff(5)
    return vel.diff(5)


def vtac_drv3_015_vol_accel_skewness_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    vel = a.rolling(252).skew().diff(5)
    return vel.diff(5)


def vsk_drv3_016_vol_accel_decay_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1))
    a5 = _calculate_accel(v.rolling(5).std(), 5)
    a21 = _calculate_accel(v.rolling(21).std(), 21)
    vel = (a5 - a21).diff(5)
    return vel.diff(5)


def vtac_drv3_017_vol_energy_density_accel_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    ed = (v**2) * v_rat
    a = _calculate_accel(ed, 21)
    vel = a.diff(5)
    return vel.diff(5)


def vtac_drv3_018_consecutive_vol_accel_streak_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    is_high = (a > a.rolling(252).median()).astype(int)
    dur = is_high.groupby((is_high == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vtac_drv3_019_vva_climax_jerk(close: pd.Series, low: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5)
    vva = va.diff(5)
    score = vva * _safe_div(close, low)
    vel = score.diff(5)
    return vel.diff(5)


def vtac_drv3_020_vol_accel_norm_depth_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    va = _calculate_accel(v, 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / (h + _EPS)
    ratio = _safe_div(va, dd + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vtac_drv3_021_vol_accel_regime_break_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    brk = _calculate_accel(v, 5) - _calculate_accel(v, 63)
    vel = brk.diff(5)
    return vel.diff(5)


def vtac_drv3_022_cumulative_vol_accel_energy_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    energy = a.cumsum() / (a.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vtr_drv3_023_vol_accel_final_climax_jerk(close: pd.Series) -> pd.Series:
    score = vtac_150_vol_accel_final_climax_index(close)
    vel = score.diff(5)
    return vel.diff(5)


def vtac_drv3_024_vol_accel_at_ath_low_jerk(close: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    v = np.log(close / close.shift(1)).rolling(5).std()
    a = _calculate_accel(v, 5)
    val = a.where(is_low).ffill()
    vel = val.diff(5)
    return vel.diff(5)


def vtac_drv3_025_vol_accel_composite_jerk(close: pd.Series) -> pd.Series:
    score = vtac_075_vol_acceleration_final_composite(close)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V30_A_REGISTRY = {
    "vtac_drv3_001_vol_accel_5d_jerk": {"inputs": ["close"], "func": vtac_drv3_001_vol_accel_5d_jerk},
    "vtac_drv3_002_vol_accel_zscore_jerk": {"inputs": ["close"], "func": vtac_drv3_002_vol_accel_zscore_jerk},
    "vtac_drv3_003_vol_breakaway_jerk": {"inputs": ["close"], "func": vtac_drv3_003_vol_breakaway_jerk},
    "vtac_drv3_004_vol_accel_climax_jerk": {"inputs": ["close"], "func": vtac_drv3_004_vol_accel_climax_jerk},
    "vtac_drv3_005_mktcap_vol_accel_jerk": {"inputs": ["close", "sharesbas"], "func": vtac_drv3_005_mktcap_vol_accel_jerk},
    "vtac_drv3_006_vol_accel_regime_shift_jerk": {"inputs": ["close"], "func": vtac_drv3_006_vol_accel_regime_shift_jerk},
    "vtac_drv3_007_vol_accel_oscillator_jerk": {"inputs": ["close"], "func": vtac_drv3_007_vol_accel_oscillator_jerk},
    "vtac_drv3_008_vol_accel_stability_jerk": {"inputs": ["close"], "func": vtac_drv3_008_vol_accel_stability_jerk},
    "vsk_drv3_009_vol_accel_reversal_jerk": {"inputs": ["close", "low"], "func": vsk_drv3_009_vol_accel_reversal_jerk},
    "vtac_drv3_010_vix_proxy_accel_jerk": {"inputs": ["close"], "func": vtac_drv3_010_vix_proxy_accel_jerk},
    "vtac_drv3_011_joint_range_vol_accel_jerk": {"inputs": ["high", "low", "close"], "func": vtac_drv3_011_joint_range_vol_accel_jerk},
    "vtac_drv3_012_vol_accel_per_dd_jerk": {"inputs": ["close"], "func": vtac_drv3_012_vol_accel_per_dd_jerk},
    "vtac_drv3_013_mktcap_vol_accel_zscore_jerk": {"inputs": ["close", "sharesbas"], "func": vtac_drv3_013_mktcap_vol_accel_zscore_jerk},
    "vtac_drv3_014_vol_accel_volatility_jerk": {"inputs": ["close"], "func": vtac_drv3_014_vol_accel_volatility_jerk},
    "vtac_drv3_015_vol_accel_skewness_jerk": {"inputs": ["close"], "func": vtac_drv3_015_vol_accel_skewness_jerk},
    "vsk_drv3_016_vol_accel_decay_jerk": {"inputs": ["close"], "func": vsk_drv3_016_vol_accel_decay_jerk},
    "vtac_drv3_017_vol_energy_density_accel_jerk": {"inputs": ["close", "volume"], "func": vtac_drv3_017_vol_energy_density_accel_jerk},
    "vtac_drv3_018_consecutive_vol_accel_streak_jerk": {"inputs": ["close"], "func": vtac_drv3_018_consecutive_vol_accel_streak_jerk},
    "vtac_drv3_019_vva_climax_jerk": {"inputs": ["close", "low"], "func": vtac_drv3_019_vva_climax_jerk},
    "vtac_drv3_020_vol_accel_norm_depth_jerk": {"inputs": ["close"], "func": vtac_drv3_020_vol_accel_norm_depth_jerk},
    "vtac_drv3_021_vol_accel_regime_break_jerk": {"inputs": ["close"], "func": vtac_drv3_021_vol_accel_regime_break_jerk},
    "vtac_drv3_022_cumulative_vol_accel_energy_jerk": {"inputs": ["close"], "func": vtac_drv3_022_cumulative_vol_accel_energy_jerk},
    "vtr_drv3_023_vol_accel_final_climax_jerk": {"inputs": ["close"], "func": vtr_drv3_023_vol_accel_final_climax_jerk},
    "vtac_drv3_024_vol_accel_at_ath_low_jerk": {"inputs": ["close"], "func": vtac_drv3_024_vol_accel_at_ath_low_jerk},
    "vtac_drv3_025_vol_accel_composite_jerk": {"inputs": ["close"], "func": vtac_drv3_025_vol_accel_composite_jerk},
}
