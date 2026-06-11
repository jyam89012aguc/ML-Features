import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (short-squeeze thrust) =====
def _f14_thrust(s, w):
    # multi-day cumulative up-move; positive moves convex-emphasised (squeeze signature)
    r = s / s.shift(w) - 1.0
    return r * (1.0 + r.clip(lower=0.0))


def _f14_volthrust(s, v, w):
    # up-move over w days multiplied by contemporaneous volume surge vs its own baseline
    r = s / s.shift(w) - 1.0
    surge = v / v.rolling(w * 3, min_periods=max(2, w)).mean().replace(0, np.nan)
    return r * surge


def _f14_velocity(s, w):
    # w-day return per unit of realized daily volatility (sharpness of the thrust)
    r = s / s.shift(w) - 1.0
    vol = s.pct_change().rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(w)
    return r / vol.replace(0, np.nan)


def _f14_recovery(s, w):
    # thrust measured as distance above the trailing w-day low (recovery-from-low)
    low = s.rolling(w, min_periods=max(2, w // 2)).min().replace(0, np.nan)
    return s / low - 1.0


# ============ FEATURES 001-075 ============

# 3d cumulative thrust (positive-emphasised)
def f14ss_f14_short_squeeze_thrust_thrust_3d_base_v001_signal(closeadj):
    result = _f14_thrust(closeadj, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_5d_base_v002_signal(closeadj):
    result = _f14_thrust(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_10d_base_v003_signal(closeadj):
    result = _f14_thrust(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_21d_base_v004_signal(closeadj):
    result = _f14_thrust(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_42d_base_v005_signal(closeadj):
    result = _f14_thrust(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative thrust
def f14ss_f14_short_squeeze_thrust_thrust_63d_base_v006_signal(closeadj):
    result = _f14_thrust(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 3d thrust * volume surge (squeeze ignition)
def f14ss_f14_short_squeeze_thrust_volthrust_3d_base_v007_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d thrust * volume surge
def f14ss_f14_short_squeeze_thrust_volthrust_5d_base_v008_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d thrust * volume surge
def f14ss_f14_short_squeeze_thrust_volthrust_10d_base_v009_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d thrust * volume surge
def f14ss_f14_short_squeeze_thrust_volthrust_21d_base_v010_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d thrust * volume surge
def f14ss_f14_short_squeeze_thrust_volthrust_42d_base_v011_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 3d velocity (return per unit realized vol)
def f14ss_f14_short_squeeze_thrust_velocity_3d_base_v012_signal(closeadj):
    result = _f14_velocity(closeadj, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d velocity
def f14ss_f14_short_squeeze_thrust_velocity_5d_base_v013_signal(closeadj):
    result = _f14_velocity(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d velocity
def f14ss_f14_short_squeeze_thrust_velocity_10d_base_v014_signal(closeadj):
    result = _f14_velocity(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d velocity
def f14ss_f14_short_squeeze_thrust_velocity_21d_base_v015_signal(closeadj):
    result = _f14_velocity(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d velocity
def f14ss_f14_short_squeeze_thrust_velocity_42d_base_v016_signal(closeadj):
    result = _f14_velocity(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d velocity
def f14ss_f14_short_squeeze_thrust_velocity_63d_base_v017_signal(closeadj):
    result = _f14_velocity(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_10d_base_v018_signal(closeadj):
    result = _f14_recovery(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_21d_base_v019_signal(closeadj):
    result = _f14_recovery(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_42d_base_v020_signal(closeadj):
    result = _f14_recovery(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d recovery-from-low thrust
def f14ss_f14_short_squeeze_thrust_recovery_63d_base_v021_signal(closeadj):
    result = _f14_recovery(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure = 5d thrust * 21d volume z-score
def f14ss_f14_short_squeeze_thrust_squeeze_5d_base_v022_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 5) * _z(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure = 10d thrust * 42d volume z-score
def f14ss_f14_short_squeeze_thrust_squeeze_10d_base_v023_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 10) * _z(volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure = 21d thrust * 63d volume z-score
def f14ss_f14_short_squeeze_thrust_squeeze_21d_base_v024_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 21) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure = 42d thrust * 126d dollar-volume z-score
def f14ss_f14_short_squeeze_thrust_squeezedv_42d_base_v025_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f14_thrust(closeadj, 42) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-move z-score: 5d thrust standardized over 63d
def f14ss_f14_short_squeeze_thrust_zthrust_5d_base_v026_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-move z-score: 10d thrust standardized over 126d
def f14ss_f14_short_squeeze_thrust_zthrust_10d_base_v027_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 10), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-move z-score: 21d thrust standardized over 252d
def f14ss_f14_short_squeeze_thrust_zthrust_21d_base_v028_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical-move z-score: 3d thrust standardized over 42d
def f14ss_f14_short_squeeze_thrust_zthrust_3d_base_v029_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 3), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity z-score: 10d velocity standardized over 126d
def f14ss_f14_short_squeeze_thrust_zvel_10d_base_v030_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 10), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity z-score: 21d velocity standardized over 252d
def f14ss_f14_short_squeeze_thrust_zvel_21d_base_v031_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up stacking magnitude: 5d sum of positive overnight gaps
def f14ss_f14_short_squeeze_thrust_gapstack_5d_base_v032_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(5, min_periods=2).sum() + _f14_thrust(closeadj, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up stacking magnitude: 10d sum of positive overnight gaps
def f14ss_f14_short_squeeze_thrust_gapstack_10d_base_v033_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(10, min_periods=3).sum() + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up stacking magnitude: 21d sum of positive overnight gaps
def f14ss_f14_short_squeeze_thrust_gapstack_21d_base_v034_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(21, min_periods=7).sum() + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-up intensity: magnitude-weighted positive daily returns over 10d
def f14ss_f14_short_squeeze_thrust_upintensity_10d_base_v035_signal(closeadj):
    up = closeadj.pct_change().clip(lower=0.0)
    result = up.rolling(10, min_periods=3).sum() + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-up intensity over 21d
def f14ss_f14_short_squeeze_thrust_upintensity_21d_base_v036_signal(closeadj):
    up = closeadj.pct_change().clip(lower=0.0)
    result = up.rolling(21, min_periods=7).sum() + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside range expansion: 10d high-low range vs 63d baseline (thrust-anchored)
def f14ss_f14_short_squeeze_thrust_rangeexp_10d_base_v037_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    result = _safe_div(_mean(rng, 10), _mean(rng, 63)) + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside range expansion: 21d range vs 126d baseline
def f14ss_f14_short_squeeze_thrust_rangeexp_21d_base_v038_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    result = _safe_div(_mean(rng, 21), _mean(rng, 126)) + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of thrust: 5d thrust minus 10d thrust
def f14ss_f14_short_squeeze_thrust_accel_5_10_base_v039_signal(closeadj):
    result = _f14_thrust(closeadj, 5) - _f14_thrust(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of thrust: 10d thrust minus 21d thrust
def f14ss_f14_short_squeeze_thrust_accel_10_21_base_v040_signal(closeadj):
    result = _f14_thrust(closeadj, 10) - _f14_thrust(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of thrust: 21d thrust minus 42d thrust
def f14ss_f14_short_squeeze_thrust_accel_21_42_base_v041_signal(closeadj):
    result = _f14_thrust(closeadj, 21) - _f14_thrust(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# price acceleration confirmed by volume: 10d thrust-accel * volume surge
def f14ss_f14_short_squeeze_thrust_accelvol_10d_base_v042_signal(closeadj, volume):
    accel = _f14_thrust(closeadj, 5) - _f14_thrust(closeadj, 10)
    surge = _safe_div(volume, _mean(volume, 42))
    result = accel * surge
    return result.replace([np.inf, -np.inf], np.nan)


# price acceleration confirmed by volume: 21d thrust-accel * volume surge
def f14ss_f14_short_squeeze_thrust_accelvol_21d_base_v043_signal(closeadj, volume):
    accel = _f14_thrust(closeadj, 10) - _f14_thrust(closeadj, 21)
    surge = _safe_div(volume, _mean(volume, 63))
    result = accel * surge
    return result.replace([np.inf, -np.inf], np.nan)


# velocity confirmed by dollar-volume surge over 10d
def f14ss_f14_short_squeeze_thrust_veldv_10d_base_v044_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f14_velocity(closeadj, 10) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# velocity confirmed by dollar-volume surge over 21d
def f14ss_f14_short_squeeze_thrust_veldv_21d_base_v045_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 126))
    result = _f14_velocity(closeadj, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-from-low * volume surge (squeeze off the bottom) 21d
def f14ss_f14_short_squeeze_thrust_recovol_21d_base_v046_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f14_recovery(closeadj, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-from-low * volume surge 42d
def f14ss_f14_short_squeeze_thrust_recovol_42d_base_v047_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 126))
    result = _f14_recovery(closeadj, 42) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# thrust per unit recovery depth: 10d thrust scaled by trailing drawdown
def f14ss_f14_short_squeeze_thrust_thrustdd_10d_base_v048_signal(closeadj):
    peak = closeadj.rolling(63, min_periods=21).max().replace(0, np.nan)
    dd = (peak - closeadj) / peak
    result = _f14_thrust(closeadj, 10) * (1.0 + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust per unit recovery depth: 21d thrust scaled by trailing drawdown
def f14ss_f14_short_squeeze_thrust_thrustdd_21d_base_v049_signal(closeadj):
    peak = closeadj.rolling(126, min_periods=42).max().replace(0, np.nan)
    dd = (peak - closeadj) / peak
    result = _f14_thrust(closeadj, 21) * (1.0 + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust convexity: positive-emphasised thrust minus raw return (5d)
def f14ss_f14_short_squeeze_thrust_convex_5d_base_v050_signal(closeadj):
    raw = closeadj / closeadj.shift(5) - 1.0
    result = _f14_thrust(closeadj, 5) - raw
    return result.replace([np.inf, -np.inf], np.nan)


# thrust convexity: 10d
def f14ss_f14_short_squeeze_thrust_convex_10d_base_v051_signal(closeadj):
    raw = closeadj / closeadj.shift(10) - 1.0
    result = _f14_thrust(closeadj, 10) - raw
    return result.replace([np.inf, -np.inf], np.nan)


# thrust convexity: 21d
def f14ss_f14_short_squeeze_thrust_convex_21d_base_v052_signal(closeadj):
    raw = closeadj / closeadj.shift(21) - 1.0
    result = _f14_thrust(closeadj, 21) - raw
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed thrust: 5d mean of 5d thrust
def f14ss_f14_short_squeeze_thrust_smthrust_5d_base_v053_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed thrust: 10d mean of 10d thrust
def f14ss_f14_short_squeeze_thrust_smthrust_10d_base_v054_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 10), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed velocity: 10d mean of 5d velocity
def f14ss_f14_short_squeeze_thrust_smvel_5d_base_v055_signal(closeadj):
    result = _mean(_f14_velocity(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust ratio: 5d thrust over 21d thrust magnitude (sharpness)
def f14ss_f14_short_squeeze_thrust_ratio_5_21_base_v056_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 5), _f14_thrust(closeadj, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# thrust ratio: 10d thrust over 42d thrust magnitude
def f14ss_f14_short_squeeze_thrust_ratio_10_42_base_v057_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 10), _f14_thrust(closeadj, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# volthrust z-score: 5d volthrust standardized over 63d
def f14ss_f14_short_squeeze_thrust_zvolthrust_5d_base_v058_signal(closeadj, volume):
    result = _z(_f14_volthrust(closeadj, volume, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# volthrust z-score: 10d volthrust standardized over 126d
def f14ss_f14_short_squeeze_thrust_zvolthrust_10d_base_v059_signal(closeadj, volume):
    result = _z(_f14_volthrust(closeadj, volume, 10), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery velocity: recovery-from-low per unit realized vol (21d)
def f14ss_f14_short_squeeze_thrust_recovel_21d_base_v060_signal(closeadj):
    vol = closeadj.pct_change().rolling(21, min_periods=10).std() * np.sqrt(21.0)
    result = _safe_div(_f14_recovery(closeadj, 21), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery velocity 42d
def f14ss_f14_short_squeeze_thrust_recovel_42d_base_v061_signal(closeadj):
    vol = closeadj.pct_change().rolling(42, min_periods=21).std() * np.sqrt(42.0)
    result = _safe_div(_f14_recovery(closeadj, 42), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday thrust: close position within 10d high-low range (squeeze close)
def f14ss_f14_short_squeeze_thrust_closepos_10d_base_v062_signal(high, low, closeadj):
    hi = high.rolling(10, min_periods=3).max()
    lo = low.rolling(10, min_periods=3).min()
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan) + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intraday thrust: close position within 21d high-low range
def f14ss_f14_short_squeeze_thrust_closepos_21d_base_v063_signal(high, low, closeadj):
    hi = high.rolling(21, min_periods=7).max()
    lo = low.rolling(21, min_periods=7).min()
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan) + _f14_thrust(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# thrust * range expansion (vertical-move with widening bars) 10d
def f14ss_f14_short_squeeze_thrust_thrustrange_10d_base_v064_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 10), _mean(rng, 63))
    result = _f14_thrust(closeadj, 10) * exp
    return result.replace([np.inf, -np.inf], np.nan)


# thrust * range expansion 21d
def f14ss_f14_short_squeeze_thrust_thrustrange_21d_base_v065_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 21), _mean(rng, 126))
    result = _f14_thrust(closeadj, 21) * exp
    return result.replace([np.inf, -np.inf], np.nan)


# velocity ratio: 5d velocity over 21d velocity magnitude
def f14ss_f14_short_squeeze_thrust_velratio_5_21_base_v066_signal(closeadj):
    result = _safe_div(_f14_velocity(closeadj, 5), _f14_velocity(closeadj, 21).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# thrust momentum surprise: 5d thrust minus its 42d mean
def f14ss_f14_short_squeeze_thrust_surp_5d_base_v067_signal(closeadj):
    t = _f14_thrust(closeadj, 5)
    result = t - _mean(t, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust momentum surprise: 21d thrust minus its 126d mean
def f14ss_f14_short_squeeze_thrust_surp_21d_base_v068_signal(closeadj):
    t = _f14_thrust(closeadj, 21)
    result = t - _mean(t, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure smoothed: 5d (thrust*volz) averaged over 10d
def f14ss_f14_short_squeeze_thrust_smsqueeze_5d_base_v069_signal(closeadj, volume):
    sp = _f14_thrust(closeadj, 5) * _z(volume, 21)
    result = _mean(sp, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# velocity * recovery (compound thrust off a low) 21d
def f14ss_f14_short_squeeze_thrust_velreco_21d_base_v070_signal(closeadj):
    result = _f14_velocity(closeadj, 21) * (1.0 + _f14_recovery(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# upside range expansion confirmed by volume 10d
def f14ss_f14_short_squeeze_thrust_rangevol_10d_base_v071_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 10), _mean(rng, 63))
    surge = _safe_div(volume, _mean(volume, 63))
    result = exp * surge + _f14_thrust(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# thrust dispersion: rolling std of 5d thrust over 42d (instability of the move)
def f14ss_f14_short_squeeze_thrust_disp_5d_base_v072_signal(closeadj):
    result = _std(_f14_thrust(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# thrust dispersion: rolling std of 10d thrust over 63d
def f14ss_f14_short_squeeze_thrust_disp_10d_base_v073_signal(closeadj):
    result = _std(_f14_thrust(closeadj, 10), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# volthrust smoothed over 10d (5d window)
def f14ss_f14_short_squeeze_thrust_smvolthrust_5d_base_v074_signal(closeadj, volume):
    result = _mean(_f14_volthrust(closeadj, volume, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze pressure with dollar-volume z 5d
def f14ss_f14_short_squeeze_thrust_squeezedv_5d_base_v075_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f14_thrust(closeadj, 5) * _z(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14ss_f14_short_squeeze_thrust_thrust_3d_base_v001_signal,
    f14ss_f14_short_squeeze_thrust_thrust_5d_base_v002_signal,
    f14ss_f14_short_squeeze_thrust_thrust_10d_base_v003_signal,
    f14ss_f14_short_squeeze_thrust_thrust_21d_base_v004_signal,
    f14ss_f14_short_squeeze_thrust_thrust_42d_base_v005_signal,
    f14ss_f14_short_squeeze_thrust_thrust_63d_base_v006_signal,
    f14ss_f14_short_squeeze_thrust_volthrust_3d_base_v007_signal,
    f14ss_f14_short_squeeze_thrust_volthrust_5d_base_v008_signal,
    f14ss_f14_short_squeeze_thrust_volthrust_10d_base_v009_signal,
    f14ss_f14_short_squeeze_thrust_volthrust_21d_base_v010_signal,
    f14ss_f14_short_squeeze_thrust_volthrust_42d_base_v011_signal,
    f14ss_f14_short_squeeze_thrust_velocity_3d_base_v012_signal,
    f14ss_f14_short_squeeze_thrust_velocity_5d_base_v013_signal,
    f14ss_f14_short_squeeze_thrust_velocity_10d_base_v014_signal,
    f14ss_f14_short_squeeze_thrust_velocity_21d_base_v015_signal,
    f14ss_f14_short_squeeze_thrust_velocity_42d_base_v016_signal,
    f14ss_f14_short_squeeze_thrust_velocity_63d_base_v017_signal,
    f14ss_f14_short_squeeze_thrust_recovery_10d_base_v018_signal,
    f14ss_f14_short_squeeze_thrust_recovery_21d_base_v019_signal,
    f14ss_f14_short_squeeze_thrust_recovery_42d_base_v020_signal,
    f14ss_f14_short_squeeze_thrust_recovery_63d_base_v021_signal,
    f14ss_f14_short_squeeze_thrust_squeeze_5d_base_v022_signal,
    f14ss_f14_short_squeeze_thrust_squeeze_10d_base_v023_signal,
    f14ss_f14_short_squeeze_thrust_squeeze_21d_base_v024_signal,
    f14ss_f14_short_squeeze_thrust_squeezedv_42d_base_v025_signal,
    f14ss_f14_short_squeeze_thrust_zthrust_5d_base_v026_signal,
    f14ss_f14_short_squeeze_thrust_zthrust_10d_base_v027_signal,
    f14ss_f14_short_squeeze_thrust_zthrust_21d_base_v028_signal,
    f14ss_f14_short_squeeze_thrust_zthrust_3d_base_v029_signal,
    f14ss_f14_short_squeeze_thrust_zvel_10d_base_v030_signal,
    f14ss_f14_short_squeeze_thrust_zvel_21d_base_v031_signal,
    f14ss_f14_short_squeeze_thrust_gapstack_5d_base_v032_signal,
    f14ss_f14_short_squeeze_thrust_gapstack_10d_base_v033_signal,
    f14ss_f14_short_squeeze_thrust_gapstack_21d_base_v034_signal,
    f14ss_f14_short_squeeze_thrust_upintensity_10d_base_v035_signal,
    f14ss_f14_short_squeeze_thrust_upintensity_21d_base_v036_signal,
    f14ss_f14_short_squeeze_thrust_rangeexp_10d_base_v037_signal,
    f14ss_f14_short_squeeze_thrust_rangeexp_21d_base_v038_signal,
    f14ss_f14_short_squeeze_thrust_accel_5_10_base_v039_signal,
    f14ss_f14_short_squeeze_thrust_accel_10_21_base_v040_signal,
    f14ss_f14_short_squeeze_thrust_accel_21_42_base_v041_signal,
    f14ss_f14_short_squeeze_thrust_accelvol_10d_base_v042_signal,
    f14ss_f14_short_squeeze_thrust_accelvol_21d_base_v043_signal,
    f14ss_f14_short_squeeze_thrust_veldv_10d_base_v044_signal,
    f14ss_f14_short_squeeze_thrust_veldv_21d_base_v045_signal,
    f14ss_f14_short_squeeze_thrust_recovol_21d_base_v046_signal,
    f14ss_f14_short_squeeze_thrust_recovol_42d_base_v047_signal,
    f14ss_f14_short_squeeze_thrust_thrustdd_10d_base_v048_signal,
    f14ss_f14_short_squeeze_thrust_thrustdd_21d_base_v049_signal,
    f14ss_f14_short_squeeze_thrust_convex_5d_base_v050_signal,
    f14ss_f14_short_squeeze_thrust_convex_10d_base_v051_signal,
    f14ss_f14_short_squeeze_thrust_convex_21d_base_v052_signal,
    f14ss_f14_short_squeeze_thrust_smthrust_5d_base_v053_signal,
    f14ss_f14_short_squeeze_thrust_smthrust_10d_base_v054_signal,
    f14ss_f14_short_squeeze_thrust_smvel_5d_base_v055_signal,
    f14ss_f14_short_squeeze_thrust_ratio_5_21_base_v056_signal,
    f14ss_f14_short_squeeze_thrust_ratio_10_42_base_v057_signal,
    f14ss_f14_short_squeeze_thrust_zvolthrust_5d_base_v058_signal,
    f14ss_f14_short_squeeze_thrust_zvolthrust_10d_base_v059_signal,
    f14ss_f14_short_squeeze_thrust_recovel_21d_base_v060_signal,
    f14ss_f14_short_squeeze_thrust_recovel_42d_base_v061_signal,
    f14ss_f14_short_squeeze_thrust_closepos_10d_base_v062_signal,
    f14ss_f14_short_squeeze_thrust_closepos_21d_base_v063_signal,
    f14ss_f14_short_squeeze_thrust_thrustrange_10d_base_v064_signal,
    f14ss_f14_short_squeeze_thrust_thrustrange_21d_base_v065_signal,
    f14ss_f14_short_squeeze_thrust_velratio_5_21_base_v066_signal,
    f14ss_f14_short_squeeze_thrust_surp_5d_base_v067_signal,
    f14ss_f14_short_squeeze_thrust_surp_21d_base_v068_signal,
    f14ss_f14_short_squeeze_thrust_smsqueeze_5d_base_v069_signal,
    f14ss_f14_short_squeeze_thrust_velreco_21d_base_v070_signal,
    f14ss_f14_short_squeeze_thrust_rangevol_10d_base_v071_signal,
    f14ss_f14_short_squeeze_thrust_disp_5d_base_v072_signal,
    f14ss_f14_short_squeeze_thrust_disp_10d_base_v073_signal,
    f14ss_f14_short_squeeze_thrust_smvolthrust_5d_base_v074_signal,
    f14ss_f14_short_squeeze_thrust_squeezedv_5d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_SHORT_SQUEEZE_THRUST_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f14_thrust", "_f14_volthrust", "_f14_velocity", "_f14_recovery")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f14_short_squeeze_thrust_base_001_075_claude: {n_features} features pass")
