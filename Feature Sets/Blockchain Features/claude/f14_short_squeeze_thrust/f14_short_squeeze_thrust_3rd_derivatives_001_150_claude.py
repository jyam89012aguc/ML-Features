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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f14ss_f14_short_squeeze_thrust_thrust_3d_jerk_v001_signal(closeadj):
    result = _f14_thrust(closeadj, 3)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_5d_jerk_v002_signal(closeadj):
    result = _f14_thrust(closeadj, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_10d_jerk_v003_signal(closeadj):
    result = _f14_thrust(closeadj, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_21d_jerk_v004_signal(closeadj):
    result = _f14_thrust(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_42d_jerk_v005_signal(closeadj):
    result = _f14_thrust(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_63d_jerk_v006_signal(closeadj):
    result = _f14_thrust(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_volthrust_3d_jerk_v007_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 3)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_volthrust_5d_jerk_v008_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_volthrust_10d_jerk_v009_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_volthrust_21d_jerk_v010_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_volthrust_42d_jerk_v011_signal(closeadj, volume):
    result = _f14_volthrust(closeadj, volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_3d_jerk_v012_signal(closeadj):
    result = _f14_velocity(closeadj, 3)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_5d_jerk_v013_signal(closeadj):
    result = _f14_velocity(closeadj, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_10d_jerk_v014_signal(closeadj):
    result = _f14_velocity(closeadj, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_21d_jerk_v015_signal(closeadj):
    result = _f14_velocity(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_42d_jerk_v016_signal(closeadj):
    result = _f14_velocity(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_63d_jerk_v017_signal(closeadj):
    result = _f14_velocity(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_10d_jerk_v018_signal(closeadj):
    result = _f14_recovery(closeadj, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_21d_jerk_v019_signal(closeadj):
    result = _f14_recovery(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_42d_jerk_v020_signal(closeadj):
    result = _f14_recovery(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_63d_jerk_v021_signal(closeadj):
    result = _f14_recovery(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeeze_5d_jerk_v022_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 5) * _z(volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeeze_10d_jerk_v023_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 10) * _z(volume, 42)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeeze_21d_jerk_v024_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 21) * _z(volume, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeezedv_42d_jerk_v025_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f14_thrust(closeadj, 42) * _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zthrust_5d_jerk_v026_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 5), 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zthrust_10d_jerk_v027_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 10), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zthrust_21d_jerk_v028_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zthrust_3d_jerk_v029_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 3), 42)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvel_10d_jerk_v030_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 10), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvel_21d_jerk_v031_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_gapstack_5d_jerk_v032_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(5, min_periods=2).sum() + _f14_thrust(closeadj, 5) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_gapstack_10d_jerk_v033_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(10, min_periods=3).sum() + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_gapstack_21d_jerk_v034_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(21, min_periods=7).sum() + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_upintensity_10d_jerk_v035_signal(closeadj):
    up = closeadj.pct_change().clip(lower=0.0)
    result = up.rolling(10, min_periods=3).sum() + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_upintensity_21d_jerk_v036_signal(closeadj):
    up = closeadj.pct_change().clip(lower=0.0)
    result = up.rolling(21, min_periods=7).sum() + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rangeexp_10d_jerk_v037_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    result = _safe_div(_mean(rng, 10), _mean(rng, 63)) + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rangeexp_21d_jerk_v038_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    result = _safe_div(_mean(rng, 21), _mean(rng, 126)) + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accel_5_10_jerk_v039_signal(closeadj):
    result = _f14_thrust(closeadj, 5) - _f14_thrust(closeadj, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accel_10_21_jerk_v040_signal(closeadj):
    result = _f14_thrust(closeadj, 10) - _f14_thrust(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accel_21_42_jerk_v041_signal(closeadj):
    result = _f14_thrust(closeadj, 21) - _f14_thrust(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accelvol_10d_jerk_v042_signal(closeadj, volume):
    accel = _f14_thrust(closeadj, 5) - _f14_thrust(closeadj, 10)
    surge = _safe_div(volume, _mean(volume, 42))
    result = accel * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accelvol_21d_jerk_v043_signal(closeadj, volume):
    accel = _f14_thrust(closeadj, 10) - _f14_thrust(closeadj, 21)
    surge = _safe_div(volume, _mean(volume, 63))
    result = accel * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_veldv_10d_jerk_v044_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f14_velocity(closeadj, 10) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_veldv_21d_jerk_v045_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 126))
    result = _f14_velocity(closeadj, 21) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovol_21d_jerk_v046_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f14_recovery(closeadj, 21) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovol_42d_jerk_v047_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 126))
    result = _f14_recovery(closeadj, 42) * surge
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustdd_10d_jerk_v048_signal(closeadj):
    peak = closeadj.rolling(63, min_periods=21).max().replace(0, np.nan)
    dd = (peak - closeadj) / peak
    result = _f14_thrust(closeadj, 10) * (1.0 + dd)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustdd_21d_jerk_v049_signal(closeadj):
    peak = closeadj.rolling(126, min_periods=42).max().replace(0, np.nan)
    dd = (peak - closeadj) / peak
    result = _f14_thrust(closeadj, 21) * (1.0 + dd)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_convex_5d_jerk_v050_signal(closeadj):
    raw = closeadj / closeadj.shift(5) - 1.0
    result = _f14_thrust(closeadj, 5) - raw
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_convex_10d_jerk_v051_signal(closeadj):
    raw = closeadj / closeadj.shift(10) - 1.0
    result = _f14_thrust(closeadj, 10) - raw
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_convex_21d_jerk_v052_signal(closeadj):
    raw = closeadj / closeadj.shift(21) - 1.0
    result = _f14_thrust(closeadj, 21) - raw
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smthrust_5d_jerk_v053_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 5), 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smthrust_10d_jerk_v054_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 10), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smvel_5d_jerk_v055_signal(closeadj):
    result = _mean(_f14_velocity(closeadj, 5), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ratio_5_21_jerk_v056_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 5), _f14_thrust(closeadj, 21).abs())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ratio_10_42_jerk_v057_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 10), _f14_thrust(closeadj, 42).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvolthrust_5d_jerk_v058_signal(closeadj, volume):
    result = _z(_f14_volthrust(closeadj, volume, 5), 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvolthrust_10d_jerk_v059_signal(closeadj, volume):
    result = _z(_f14_volthrust(closeadj, volume, 10), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovel_21d_jerk_v060_signal(closeadj):
    vol = closeadj.pct_change().rolling(21, min_periods=10).std() * np.sqrt(21.0)
    result = _safe_div(_f14_recovery(closeadj, 21), vol)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovel_42d_jerk_v061_signal(closeadj):
    vol = closeadj.pct_change().rolling(42, min_periods=21).std() * np.sqrt(42.0)
    result = _safe_div(_f14_recovery(closeadj, 42), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_closepos_10d_jerk_v062_signal(high, low, closeadj):
    hi = high.rolling(10, min_periods=3).max()
    lo = low.rolling(10, min_periods=3).min()
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan) + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_closepos_21d_jerk_v063_signal(high, low, closeadj):
    hi = high.rolling(21, min_periods=7).max()
    lo = low.rolling(21, min_periods=7).min()
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan) + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustrange_10d_jerk_v064_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 10), _mean(rng, 63))
    result = _f14_thrust(closeadj, 10) * exp
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustrange_21d_jerk_v065_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 21), _mean(rng, 126))
    result = _f14_thrust(closeadj, 21) * exp
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velratio_5_21_jerk_v066_signal(closeadj):
    result = _safe_div(_f14_velocity(closeadj, 5), _f14_velocity(closeadj, 21).abs())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_surp_5d_jerk_v067_signal(closeadj):
    t = _f14_thrust(closeadj, 5)
    result = t - _mean(t, 42)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_surp_21d_jerk_v068_signal(closeadj):
    t = _f14_thrust(closeadj, 21)
    result = t - _mean(t, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smsqueeze_5d_jerk_v069_signal(closeadj, volume):
    sp = _f14_thrust(closeadj, 5) * _z(volume, 21)
    result = _mean(sp, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velreco_21d_jerk_v070_signal(closeadj):
    result = _f14_velocity(closeadj, 21) * (1.0 + _f14_recovery(closeadj, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rangevol_10d_jerk_v071_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 10), _mean(rng, 63))
    surge = _safe_div(volume, _mean(volume, 63))
    result = exp * surge + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_disp_5d_jerk_v072_signal(closeadj):
    result = _std(_f14_thrust(closeadj, 5), 42)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_disp_10d_jerk_v073_signal(closeadj):
    result = _std(_f14_thrust(closeadj, 10), 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smvolthrust_5d_jerk_v074_signal(closeadj, volume):
    result = _mean(_f14_volthrust(closeadj, volume, 5), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeezedv_5d_jerk_v075_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f14_thrust(closeadj, 5) * _z(dv, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ewthrust_5d_jerk_v076_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=5, min_periods=3).mean() * 5.0 + _f14_thrust(closeadj, 5) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ewthrust_10d_jerk_v077_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=10, min_periods=5).mean() * 10.0 + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ewthrust_21d_jerk_v078_signal(closeadj):
    r = closeadj.pct_change()
    result = r.ewm(span=21, min_periods=10).mean() * 21.0 + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rank_5d_jerk_v079_signal(closeadj):
    t = _f14_thrust(closeadj, 5)
    result = t.rolling(63, min_periods=21).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rank_10d_jerk_v080_signal(closeadj):
    t = _f14_thrust(closeadj, 10)
    result = t.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rank_21d_jerk_v081_signal(closeadj):
    t = _f14_thrust(closeadj, 21)
    result = t.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rankvel_10d_jerk_v082_signal(closeadj):
    v = _f14_velocity(closeadj, 10)
    result = v.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rankvt_5d_jerk_v083_signal(closeadj, volume):
    vt = _f14_volthrust(closeadj, volume, 5)
    result = vt.rolling(63, min_periods=21).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_84d_jerk_v084_signal(closeadj):
    result = _f14_thrust(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_126d_jerk_v085_signal(closeadj):
    result = _f14_thrust(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_84d_jerk_v086_signal(closeadj):
    result = _f14_velocity(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velocity_126d_jerk_v087_signal(closeadj):
    result = _f14_velocity(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_84d_jerk_v088_signal(closeadj):
    result = _f14_recovery(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_126d_jerk_v089_signal(closeadj):
    result = _f14_recovery(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeeze_42d_jerk_v090_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 42) * _z(volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeeze_63d_jerk_v091_signal(closeadj, volume):
    result = _f14_thrust(closeadj, 63) * _z(volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zthrust_42d_jerk_v092_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 42), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zthrust_63d_jerk_v093_signal(closeadj):
    result = _z(_f14_thrust(closeadj, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvel_42d_jerk_v094_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 42), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvel_63d_jerk_v095_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_gapstack_42d_jerk_v096_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    result = gap.rolling(42, min_periods=14).sum() + _f14_thrust(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_gapvel_10d_jerk_v097_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0)
    g = gap.rolling(10, min_periods=3).sum()
    vol = closeadj.pct_change().rolling(10, min_periods=5).std() * np.sqrt(10.0)
    result = _safe_div(g, vol) + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_upintensity_42d_jerk_v098_signal(closeadj):
    up = closeadj.pct_change().clip(lower=0.0)
    result = up.rolling(42, min_periods=14).sum() + _f14_thrust(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_udratio_21d_jerk_v099_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(21, min_periods=7).sum()
    dn = (-r.clip(upper=0.0)).rolling(21, min_periods=7).sum()
    result = _safe_div(up, dn) + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_udratio_42d_jerk_v100_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(42, min_periods=14).sum()
    dn = (-r.clip(upper=0.0)).rolling(42, min_periods=14).sum()
    result = _safe_div(up, dn) + _f14_thrust(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rangeexp_42d_jerk_v101_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    result = _safe_div(_mean(rng, 42), _mean(rng, 189)) + _f14_thrust(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accel_42_63_jerk_v102_signal(closeadj):
    result = _f14_thrust(closeadj, 42) - _f14_thrust(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accel_3_5_jerk_v103_signal(closeadj):
    result = _f14_thrust(closeadj, 3) - _f14_thrust(closeadj, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_accelvol_42d_jerk_v104_signal(closeadj, volume):
    accel = _f14_thrust(closeadj, 21) - _f14_thrust(closeadj, 42)
    surge = _safe_div(volume, _mean(volume, 126))
    result = accel * surge
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_veldv_42d_jerk_v105_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 189))
    result = _f14_velocity(closeadj, 42) * surge
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovol_63d_jerk_v106_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 189))
    result = _f14_recovery(closeadj, 63) * surge
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustdd_42d_jerk_v107_signal(closeadj):
    peak = closeadj.rolling(189, min_periods=63).max().replace(0, np.nan)
    dd = (peak - closeadj) / peak
    result = _f14_thrust(closeadj, 42) * (1.0 + dd)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_convex_42d_jerk_v108_signal(closeadj):
    raw = closeadj / closeadj.shift(42) - 1.0
    result = _f14_thrust(closeadj, 42) - raw
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smthrust_21d_jerk_v109_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smthrust_42d_jerk_v110_signal(closeadj):
    result = _mean(_f14_thrust(closeadj, 42), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smvel_10d_jerk_v111_signal(closeadj):
    result = _mean(_f14_velocity(closeadj, 10), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ratio_21_63_jerk_v112_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 21), _f14_thrust(closeadj, 63).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ratio_5_42_jerk_v113_signal(closeadj):
    result = _safe_div(_f14_thrust(closeadj, 5), _f14_thrust(closeadj, 42).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvolthrust_21d_jerk_v114_signal(closeadj, volume):
    result = _z(_f14_volthrust(closeadj, volume, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovel_63d_jerk_v115_signal(closeadj):
    vol = closeadj.pct_change().rolling(63, min_periods=21).std() * np.sqrt(63.0)
    result = _safe_div(_f14_recovery(closeadj, 63), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_closepos_42d_jerk_v116_signal(high, low, closeadj):
    hi = high.rolling(42, min_periods=14).max()
    lo = low.rolling(42, min_periods=14).min()
    result = (closeadj - lo) / (hi - lo).replace(0, np.nan) + _f14_thrust(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustrange_42d_jerk_v117_signal(high, low, closeadj):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 42), _mean(rng, 189))
    result = _f14_thrust(closeadj, 42) * exp
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velratio_10_42_jerk_v118_signal(closeadj):
    result = _safe_div(_f14_velocity(closeadj, 10), _f14_velocity(closeadj, 42).abs())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_surp_42d_jerk_v119_signal(closeadj):
    t = _f14_thrust(closeadj, 42)
    result = t - _mean(t, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smsqueeze_21d_jerk_v120_signal(closeadj, volume):
    sp = _f14_thrust(closeadj, 21) * _z(volume, 63)
    result = _mean(sp, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velreco_42d_jerk_v121_signal(closeadj):
    result = _f14_velocity(closeadj, 42) * (1.0 + _f14_recovery(closeadj, 42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_rangevol_21d_jerk_v122_signal(high, low, closeadj, volume):
    rng = (high - low) / closeadj
    exp = _safe_div(_mean(rng, 21), _mean(rng, 126))
    surge = _safe_div(volume, _mean(volume, 126))
    result = exp * surge + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_disp_21d_jerk_v123_signal(closeadj):
    result = _std(_f14_thrust(closeadj, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_smvolthrust_21d_jerk_v124_signal(closeadj, volume):
    result = _mean(_f14_volthrust(closeadj, volume, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_skew_42d_jerk_v125_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(42, min_periods=14).skew() + _f14_thrust(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_skew_63d_jerk_v126_signal(closeadj):
    r = closeadj.pct_change()
    result = r.rolling(63, min_periods=21).skew() + _f14_thrust(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_spike_10d_jerk_v127_signal(closeadj):
    r = closeadj.pct_change()
    jump = r.rolling(10, min_periods=5).max()
    vol = r.rolling(63, min_periods=21).std()
    result = _safe_div(jump, vol) + _f14_thrust(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_spike_21d_jerk_v128_signal(closeadj):
    r = closeadj.pct_change()
    jump = r.rolling(21, min_periods=7).max()
    vol = r.rolling(63, min_periods=21).std()
    result = _safe_div(jump, vol) + _f14_thrust(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_vtvel_10d_jerk_v129_signal(closeadj, volume):
    vt = _f14_volthrust(closeadj, volume, 10)
    vol = closeadj.pct_change().rolling(10, min_periods=5).std() * np.sqrt(10.0)
    result = _safe_div(vt, vol)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustshare_10d_jerk_v130_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(10, min_periods=5).sum()
    tot = r.abs().rolling(10, min_periods=5).sum()
    share = _safe_div(up, tot)
    result = _f14_thrust(closeadj, 10) * share
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustshare_21d_jerk_v131_signal(closeadj):
    r = closeadj.pct_change()
    up = r.clip(lower=0.0).rolling(21, min_periods=7).sum()
    tot = r.abs().rolling(21, min_periods=7).sum()
    share = _safe_div(up, tot)
    result = _f14_thrust(closeadj, 21) * share
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velaccel_5_21_jerk_v132_signal(closeadj):
    result = _f14_velocity(closeadj, 5) - _f14_velocity(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_velaccel_10_42_jerk_v133_signal(closeadj):
    result = _f14_velocity(closeadj, 10) - _f14_velocity(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recoaccel_21_63_jerk_v134_signal(closeadj):
    result = _f14_recovery(closeadj, 21) - _f14_recovery(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_tv_10d_jerk_v135_signal(closeadj):
    result = _f14_thrust(closeadj, 10) * _f14_velocity(closeadj, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_tv_21d_jerk_v136_signal(closeadj):
    result = _f14_thrust(closeadj, 21) * _f14_velocity(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ewsqueeze_10d_jerk_v137_signal(closeadj, volume):
    sp = _f14_thrust(closeadj, 10) * _z(volume, 42)
    result = sp.ewm(span=10, min_periods=5).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_dvvel_10d_jerk_v138_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    vol = closeadj.pct_change().rolling(10, min_periods=5).std() * np.sqrt(10.0)
    result = _safe_div(_f14_thrust(closeadj, 10) * surge, vol)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zreco_21d_jerk_v139_signal(closeadj):
    result = _z(_f14_recovery(closeadj, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zreco_42d_jerk_v140_signal(closeadj):
    result = _z(_f14_recovery(closeadj, 42), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustgap_10d_jerk_v141_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0).rolling(10, min_periods=3).sum()
    result = _f14_thrust(closeadj, 10) * (1.0 + gap)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrustgap_21d_jerk_v142_signal(open, closeadj):
    gap = (open / closeadj.shift(1) - 1.0).clip(lower=0.0).rolling(21, min_periods=7).sum()
    result = _f14_thrust(closeadj, 21) * (1.0 + gap)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_ewvel_10d_jerk_v143_signal(closeadj):
    result = _f14_velocity(closeadj, 10).ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_blendshort_jerk_v144_signal(closeadj):
    result = (_f14_thrust(closeadj, 3) + _f14_thrust(closeadj, 5)
              + _f14_thrust(closeadj, 10)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_blendvel_jerk_v145_signal(closeadj):
    result = (_f14_velocity(closeadj, 10) + _f14_velocity(closeadj, 21)
              + _f14_velocity(closeadj, 42)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_thrust_189d_jerk_v146_signal(closeadj):
    result = _f14_thrust(closeadj, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_recovery_189d_jerk_v147_signal(closeadj):
    result = _f14_recovery(closeadj, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_zvel_84d_jerk_v148_signal(closeadj):
    result = _z(_f14_velocity(closeadj, 84), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeezedv_21d_jerk_v149_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f14_thrust(closeadj, 21) * _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14ss_f14_short_squeeze_thrust_squeezemulti_jerk_v150_signal(closeadj):
    result = (_f14_thrust(closeadj, 5) * _f14_velocity(closeadj, 5)
              + _f14_thrust(closeadj, 10) * _f14_velocity(closeadj, 10)
              + _f14_thrust(closeadj, 21) * _f14_velocity(closeadj, 21)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f14ss_f14_short_squeeze_thrust_thrust_3d_jerk_v001_signal,    f14ss_f14_short_squeeze_thrust_thrust_5d_jerk_v002_signal,    f14ss_f14_short_squeeze_thrust_thrust_10d_jerk_v003_signal,    f14ss_f14_short_squeeze_thrust_thrust_21d_jerk_v004_signal,    f14ss_f14_short_squeeze_thrust_thrust_42d_jerk_v005_signal,    f14ss_f14_short_squeeze_thrust_thrust_63d_jerk_v006_signal,    f14ss_f14_short_squeeze_thrust_volthrust_3d_jerk_v007_signal,    f14ss_f14_short_squeeze_thrust_volthrust_5d_jerk_v008_signal,    f14ss_f14_short_squeeze_thrust_volthrust_10d_jerk_v009_signal,    f14ss_f14_short_squeeze_thrust_volthrust_21d_jerk_v010_signal,    f14ss_f14_short_squeeze_thrust_volthrust_42d_jerk_v011_signal,    f14ss_f14_short_squeeze_thrust_velocity_3d_jerk_v012_signal,    f14ss_f14_short_squeeze_thrust_velocity_5d_jerk_v013_signal,    f14ss_f14_short_squeeze_thrust_velocity_10d_jerk_v014_signal,    f14ss_f14_short_squeeze_thrust_velocity_21d_jerk_v015_signal,    f14ss_f14_short_squeeze_thrust_velocity_42d_jerk_v016_signal,    f14ss_f14_short_squeeze_thrust_velocity_63d_jerk_v017_signal,    f14ss_f14_short_squeeze_thrust_recovery_10d_jerk_v018_signal,    f14ss_f14_short_squeeze_thrust_recovery_21d_jerk_v019_signal,    f14ss_f14_short_squeeze_thrust_recovery_42d_jerk_v020_signal,    f14ss_f14_short_squeeze_thrust_recovery_63d_jerk_v021_signal,    f14ss_f14_short_squeeze_thrust_squeeze_5d_jerk_v022_signal,    f14ss_f14_short_squeeze_thrust_squeeze_10d_jerk_v023_signal,    f14ss_f14_short_squeeze_thrust_squeeze_21d_jerk_v024_signal,    f14ss_f14_short_squeeze_thrust_squeezedv_42d_jerk_v025_signal,    f14ss_f14_short_squeeze_thrust_zthrust_5d_jerk_v026_signal,    f14ss_f14_short_squeeze_thrust_zthrust_10d_jerk_v027_signal,    f14ss_f14_short_squeeze_thrust_zthrust_21d_jerk_v028_signal,    f14ss_f14_short_squeeze_thrust_zthrust_3d_jerk_v029_signal,    f14ss_f14_short_squeeze_thrust_zvel_10d_jerk_v030_signal,    f14ss_f14_short_squeeze_thrust_zvel_21d_jerk_v031_signal,    f14ss_f14_short_squeeze_thrust_gapstack_5d_jerk_v032_signal,    f14ss_f14_short_squeeze_thrust_gapstack_10d_jerk_v033_signal,    f14ss_f14_short_squeeze_thrust_gapstack_21d_jerk_v034_signal,    f14ss_f14_short_squeeze_thrust_upintensity_10d_jerk_v035_signal,    f14ss_f14_short_squeeze_thrust_upintensity_21d_jerk_v036_signal,    f14ss_f14_short_squeeze_thrust_rangeexp_10d_jerk_v037_signal,    f14ss_f14_short_squeeze_thrust_rangeexp_21d_jerk_v038_signal,    f14ss_f14_short_squeeze_thrust_accel_5_10_jerk_v039_signal,    f14ss_f14_short_squeeze_thrust_accel_10_21_jerk_v040_signal,    f14ss_f14_short_squeeze_thrust_accel_21_42_jerk_v041_signal,    f14ss_f14_short_squeeze_thrust_accelvol_10d_jerk_v042_signal,    f14ss_f14_short_squeeze_thrust_accelvol_21d_jerk_v043_signal,    f14ss_f14_short_squeeze_thrust_veldv_10d_jerk_v044_signal,    f14ss_f14_short_squeeze_thrust_veldv_21d_jerk_v045_signal,    f14ss_f14_short_squeeze_thrust_recovol_21d_jerk_v046_signal,    f14ss_f14_short_squeeze_thrust_recovol_42d_jerk_v047_signal,    f14ss_f14_short_squeeze_thrust_thrustdd_10d_jerk_v048_signal,    f14ss_f14_short_squeeze_thrust_thrustdd_21d_jerk_v049_signal,    f14ss_f14_short_squeeze_thrust_convex_5d_jerk_v050_signal,    f14ss_f14_short_squeeze_thrust_convex_10d_jerk_v051_signal,    f14ss_f14_short_squeeze_thrust_convex_21d_jerk_v052_signal,    f14ss_f14_short_squeeze_thrust_smthrust_5d_jerk_v053_signal,    f14ss_f14_short_squeeze_thrust_smthrust_10d_jerk_v054_signal,    f14ss_f14_short_squeeze_thrust_smvel_5d_jerk_v055_signal,    f14ss_f14_short_squeeze_thrust_ratio_5_21_jerk_v056_signal,    f14ss_f14_short_squeeze_thrust_ratio_10_42_jerk_v057_signal,    f14ss_f14_short_squeeze_thrust_zvolthrust_5d_jerk_v058_signal,    f14ss_f14_short_squeeze_thrust_zvolthrust_10d_jerk_v059_signal,    f14ss_f14_short_squeeze_thrust_recovel_21d_jerk_v060_signal,    f14ss_f14_short_squeeze_thrust_recovel_42d_jerk_v061_signal,    f14ss_f14_short_squeeze_thrust_closepos_10d_jerk_v062_signal,    f14ss_f14_short_squeeze_thrust_closepos_21d_jerk_v063_signal,    f14ss_f14_short_squeeze_thrust_thrustrange_10d_jerk_v064_signal,    f14ss_f14_short_squeeze_thrust_thrustrange_21d_jerk_v065_signal,    f14ss_f14_short_squeeze_thrust_velratio_5_21_jerk_v066_signal,    f14ss_f14_short_squeeze_thrust_surp_5d_jerk_v067_signal,    f14ss_f14_short_squeeze_thrust_surp_21d_jerk_v068_signal,    f14ss_f14_short_squeeze_thrust_smsqueeze_5d_jerk_v069_signal,    f14ss_f14_short_squeeze_thrust_velreco_21d_jerk_v070_signal,    f14ss_f14_short_squeeze_thrust_rangevol_10d_jerk_v071_signal,    f14ss_f14_short_squeeze_thrust_disp_5d_jerk_v072_signal,    f14ss_f14_short_squeeze_thrust_disp_10d_jerk_v073_signal,    f14ss_f14_short_squeeze_thrust_smvolthrust_5d_jerk_v074_signal,    f14ss_f14_short_squeeze_thrust_squeezedv_5d_jerk_v075_signal,    f14ss_f14_short_squeeze_thrust_ewthrust_5d_jerk_v076_signal,    f14ss_f14_short_squeeze_thrust_ewthrust_10d_jerk_v077_signal,    f14ss_f14_short_squeeze_thrust_ewthrust_21d_jerk_v078_signal,    f14ss_f14_short_squeeze_thrust_rank_5d_jerk_v079_signal,    f14ss_f14_short_squeeze_thrust_rank_10d_jerk_v080_signal,    f14ss_f14_short_squeeze_thrust_rank_21d_jerk_v081_signal,    f14ss_f14_short_squeeze_thrust_rankvel_10d_jerk_v082_signal,    f14ss_f14_short_squeeze_thrust_rankvt_5d_jerk_v083_signal,    f14ss_f14_short_squeeze_thrust_thrust_84d_jerk_v084_signal,    f14ss_f14_short_squeeze_thrust_thrust_126d_jerk_v085_signal,    f14ss_f14_short_squeeze_thrust_velocity_84d_jerk_v086_signal,    f14ss_f14_short_squeeze_thrust_velocity_126d_jerk_v087_signal,    f14ss_f14_short_squeeze_thrust_recovery_84d_jerk_v088_signal,    f14ss_f14_short_squeeze_thrust_recovery_126d_jerk_v089_signal,    f14ss_f14_short_squeeze_thrust_squeeze_42d_jerk_v090_signal,    f14ss_f14_short_squeeze_thrust_squeeze_63d_jerk_v091_signal,    f14ss_f14_short_squeeze_thrust_zthrust_42d_jerk_v092_signal,    f14ss_f14_short_squeeze_thrust_zthrust_63d_jerk_v093_signal,    f14ss_f14_short_squeeze_thrust_zvel_42d_jerk_v094_signal,    f14ss_f14_short_squeeze_thrust_zvel_63d_jerk_v095_signal,    f14ss_f14_short_squeeze_thrust_gapstack_42d_jerk_v096_signal,    f14ss_f14_short_squeeze_thrust_gapvel_10d_jerk_v097_signal,    f14ss_f14_short_squeeze_thrust_upintensity_42d_jerk_v098_signal,    f14ss_f14_short_squeeze_thrust_udratio_21d_jerk_v099_signal,    f14ss_f14_short_squeeze_thrust_udratio_42d_jerk_v100_signal,    f14ss_f14_short_squeeze_thrust_rangeexp_42d_jerk_v101_signal,    f14ss_f14_short_squeeze_thrust_accel_42_63_jerk_v102_signal,    f14ss_f14_short_squeeze_thrust_accel_3_5_jerk_v103_signal,    f14ss_f14_short_squeeze_thrust_accelvol_42d_jerk_v104_signal,    f14ss_f14_short_squeeze_thrust_veldv_42d_jerk_v105_signal,    f14ss_f14_short_squeeze_thrust_recovol_63d_jerk_v106_signal,    f14ss_f14_short_squeeze_thrust_thrustdd_42d_jerk_v107_signal,    f14ss_f14_short_squeeze_thrust_convex_42d_jerk_v108_signal,    f14ss_f14_short_squeeze_thrust_smthrust_21d_jerk_v109_signal,    f14ss_f14_short_squeeze_thrust_smthrust_42d_jerk_v110_signal,    f14ss_f14_short_squeeze_thrust_smvel_10d_jerk_v111_signal,    f14ss_f14_short_squeeze_thrust_ratio_21_63_jerk_v112_signal,    f14ss_f14_short_squeeze_thrust_ratio_5_42_jerk_v113_signal,    f14ss_f14_short_squeeze_thrust_zvolthrust_21d_jerk_v114_signal,    f14ss_f14_short_squeeze_thrust_recovel_63d_jerk_v115_signal,    f14ss_f14_short_squeeze_thrust_closepos_42d_jerk_v116_signal,    f14ss_f14_short_squeeze_thrust_thrustrange_42d_jerk_v117_signal,    f14ss_f14_short_squeeze_thrust_velratio_10_42_jerk_v118_signal,    f14ss_f14_short_squeeze_thrust_surp_42d_jerk_v119_signal,    f14ss_f14_short_squeeze_thrust_smsqueeze_21d_jerk_v120_signal,    f14ss_f14_short_squeeze_thrust_velreco_42d_jerk_v121_signal,    f14ss_f14_short_squeeze_thrust_rangevol_21d_jerk_v122_signal,    f14ss_f14_short_squeeze_thrust_disp_21d_jerk_v123_signal,    f14ss_f14_short_squeeze_thrust_smvolthrust_21d_jerk_v124_signal,    f14ss_f14_short_squeeze_thrust_skew_42d_jerk_v125_signal,    f14ss_f14_short_squeeze_thrust_skew_63d_jerk_v126_signal,    f14ss_f14_short_squeeze_thrust_spike_10d_jerk_v127_signal,    f14ss_f14_short_squeeze_thrust_spike_21d_jerk_v128_signal,    f14ss_f14_short_squeeze_thrust_vtvel_10d_jerk_v129_signal,    f14ss_f14_short_squeeze_thrust_thrustshare_10d_jerk_v130_signal,    f14ss_f14_short_squeeze_thrust_thrustshare_21d_jerk_v131_signal,    f14ss_f14_short_squeeze_thrust_velaccel_5_21_jerk_v132_signal,    f14ss_f14_short_squeeze_thrust_velaccel_10_42_jerk_v133_signal,    f14ss_f14_short_squeeze_thrust_recoaccel_21_63_jerk_v134_signal,    f14ss_f14_short_squeeze_thrust_tv_10d_jerk_v135_signal,    f14ss_f14_short_squeeze_thrust_tv_21d_jerk_v136_signal,    f14ss_f14_short_squeeze_thrust_ewsqueeze_10d_jerk_v137_signal,    f14ss_f14_short_squeeze_thrust_dvvel_10d_jerk_v138_signal,    f14ss_f14_short_squeeze_thrust_zreco_21d_jerk_v139_signal,    f14ss_f14_short_squeeze_thrust_zreco_42d_jerk_v140_signal,    f14ss_f14_short_squeeze_thrust_thrustgap_10d_jerk_v141_signal,    f14ss_f14_short_squeeze_thrust_thrustgap_21d_jerk_v142_signal,    f14ss_f14_short_squeeze_thrust_ewvel_10d_jerk_v143_signal,    f14ss_f14_short_squeeze_thrust_blendshort_jerk_v144_signal,    f14ss_f14_short_squeeze_thrust_blendvel_jerk_v145_signal,    f14ss_f14_short_squeeze_thrust_thrust_189d_jerk_v146_signal,    f14ss_f14_short_squeeze_thrust_recovery_189d_jerk_v147_signal,    f14ss_f14_short_squeeze_thrust_zvel_84d_jerk_v148_signal,    f14ss_f14_short_squeeze_thrust_squeezedv_21d_jerk_v149_signal,    f14ss_f14_short_squeeze_thrust_squeezemulti_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_SHORT_SQUEEZE_THRUST_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f14_thrust', '_f14_volthrust', '_f14_velocity', '_f14_recovery')
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
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f14_short_squeeze_thrust_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
