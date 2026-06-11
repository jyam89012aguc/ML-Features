import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====

def _f12_capex_acceleration(capex, w):
    g = capex.pct_change(periods=w)
    return g - g.shift(w)


def _f12_revenue_capex_dynamics(revenue, capex, w):
    rg = revenue.pct_change(periods=w)
    cg = capex.pct_change(periods=w)
    return rg * cg


def _f12_rollout_signature(capex, revenue, w):
    cg = capex.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    cap_acc = cg - cg.shift(w)
    return cap_acc + rg


# ===== features =====

def f12rov_f12_rollout_velocity_cap_w5_5d_slope_v001_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w5_10d_slope_v002_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w5_21d_slope_v003_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w5_42d_slope_v004_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w5_63d_slope_v005_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w10_5d_slope_v006_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w10_10d_slope_v007_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w10_21d_slope_v008_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w10_42d_slope_v009_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w10_63d_slope_v010_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w21_5d_slope_v011_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w21_10d_slope_v012_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w21_21d_slope_v013_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w21_42d_slope_v014_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w21_63d_slope_v015_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w42_5d_slope_v016_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w42_10d_slope_v017_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w42_21d_slope_v018_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w42_42d_slope_v019_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w42_63d_slope_v020_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w63_5d_slope_v021_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w63_10d_slope_v022_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w63_21d_slope_v023_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w63_42d_slope_v024_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w63_63d_slope_v025_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w126_5d_slope_v026_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w126_10d_slope_v027_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w126_21d_slope_v028_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w126_42d_slope_v029_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w126_63d_slope_v030_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w189_5d_slope_v031_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w189_10d_slope_v032_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w189_21d_slope_v033_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w189_42d_slope_v034_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w189_63d_slope_v035_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w252_5d_slope_v036_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w252_10d_slope_v037_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w252_21d_slope_v038_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w252_42d_slope_v039_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w252_63d_slope_v040_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w378_5d_slope_v041_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w378_10d_slope_v042_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w378_21d_slope_v043_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w378_42d_slope_v044_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w378_63d_slope_v045_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w504_5d_slope_v046_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w504_10d_slope_v047_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w504_21d_slope_v048_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w504_42d_slope_v049_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_cap_w504_63d_slope_v050_signal(capex, closeadj):
    result = _slope_diff_norm(_f12_capex_acceleration(capex, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w5_5d_slope_v051_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w5_10d_slope_v052_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w5_21d_slope_v053_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w5_42d_slope_v054_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w5_63d_slope_v055_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w10_5d_slope_v056_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w10_10d_slope_v057_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w10_21d_slope_v058_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w10_42d_slope_v059_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w10_63d_slope_v060_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w21_5d_slope_v061_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w21_10d_slope_v062_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w21_21d_slope_v063_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w21_42d_slope_v064_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w21_63d_slope_v065_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w42_5d_slope_v066_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w42_10d_slope_v067_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w42_21d_slope_v068_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w42_42d_slope_v069_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w42_63d_slope_v070_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w63_5d_slope_v071_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w63_10d_slope_v072_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w63_21d_slope_v073_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w63_42d_slope_v074_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w63_63d_slope_v075_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w126_5d_slope_v076_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w126_10d_slope_v077_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w126_21d_slope_v078_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w126_42d_slope_v079_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w126_63d_slope_v080_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w189_5d_slope_v081_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w189_10d_slope_v082_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w189_21d_slope_v083_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w189_42d_slope_v084_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w189_63d_slope_v085_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w252_5d_slope_v086_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w252_10d_slope_v087_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w252_21d_slope_v088_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w252_42d_slope_v089_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w252_63d_slope_v090_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w378_5d_slope_v091_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w378_10d_slope_v092_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w378_21d_slope_v093_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w378_42d_slope_v094_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w378_63d_slope_v095_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w504_5d_slope_v096_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w504_10d_slope_v097_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w504_21d_slope_v098_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w504_42d_slope_v099_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_rcd_w504_63d_slope_v100_signal(revenue, capex, closeadj):
    result = _slope_diff_norm(_f12_revenue_capex_dynamics(revenue, capex, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w5_5d_slope_v101_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w5_10d_slope_v102_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w5_21d_slope_v103_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w5_42d_slope_v104_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w5_63d_slope_v105_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w10_5d_slope_v106_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w10_10d_slope_v107_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w10_21d_slope_v108_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w10_42d_slope_v109_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w10_63d_slope_v110_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w21_5d_slope_v111_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w21_10d_slope_v112_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w21_21d_slope_v113_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w21_42d_slope_v114_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w21_63d_slope_v115_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w42_5d_slope_v116_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w42_10d_slope_v117_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w42_21d_slope_v118_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w42_42d_slope_v119_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w42_63d_slope_v120_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w63_5d_slope_v121_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w63_10d_slope_v122_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w63_21d_slope_v123_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w63_42d_slope_v124_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w63_63d_slope_v125_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w126_5d_slope_v126_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w126_10d_slope_v127_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w126_21d_slope_v128_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w126_42d_slope_v129_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w126_63d_slope_v130_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w189_5d_slope_v131_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w189_10d_slope_v132_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w189_21d_slope_v133_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w189_42d_slope_v134_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w189_63d_slope_v135_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w252_5d_slope_v136_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w252_10d_slope_v137_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w252_21d_slope_v138_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w252_42d_slope_v139_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w252_63d_slope_v140_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w378_5d_slope_v141_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w378_10d_slope_v142_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w378_21d_slope_v143_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w378_42d_slope_v144_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w378_63d_slope_v145_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w504_5d_slope_v146_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w504_10d_slope_v147_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w504_21d_slope_v148_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w504_42d_slope_v149_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f12rov_f12_rollout_velocity_sig_w504_63d_slope_v150_signal(capex, revenue, closeadj):
    result = _slope_diff_norm(_f12_rollout_signature(capex, revenue, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f12rov_f12_rollout_velocity_cap_w5_5d_slope_v001_signal,
    f12rov_f12_rollout_velocity_cap_w5_10d_slope_v002_signal,
    f12rov_f12_rollout_velocity_cap_w5_21d_slope_v003_signal,
    f12rov_f12_rollout_velocity_cap_w5_42d_slope_v004_signal,
    f12rov_f12_rollout_velocity_cap_w5_63d_slope_v005_signal,
    f12rov_f12_rollout_velocity_cap_w10_5d_slope_v006_signal,
    f12rov_f12_rollout_velocity_cap_w10_10d_slope_v007_signal,
    f12rov_f12_rollout_velocity_cap_w10_21d_slope_v008_signal,
    f12rov_f12_rollout_velocity_cap_w10_42d_slope_v009_signal,
    f12rov_f12_rollout_velocity_cap_w10_63d_slope_v010_signal,
    f12rov_f12_rollout_velocity_cap_w21_5d_slope_v011_signal,
    f12rov_f12_rollout_velocity_cap_w21_10d_slope_v012_signal,
    f12rov_f12_rollout_velocity_cap_w21_21d_slope_v013_signal,
    f12rov_f12_rollout_velocity_cap_w21_42d_slope_v014_signal,
    f12rov_f12_rollout_velocity_cap_w21_63d_slope_v015_signal,
    f12rov_f12_rollout_velocity_cap_w42_5d_slope_v016_signal,
    f12rov_f12_rollout_velocity_cap_w42_10d_slope_v017_signal,
    f12rov_f12_rollout_velocity_cap_w42_21d_slope_v018_signal,
    f12rov_f12_rollout_velocity_cap_w42_42d_slope_v019_signal,
    f12rov_f12_rollout_velocity_cap_w42_63d_slope_v020_signal,
    f12rov_f12_rollout_velocity_cap_w63_5d_slope_v021_signal,
    f12rov_f12_rollout_velocity_cap_w63_10d_slope_v022_signal,
    f12rov_f12_rollout_velocity_cap_w63_21d_slope_v023_signal,
    f12rov_f12_rollout_velocity_cap_w63_42d_slope_v024_signal,
    f12rov_f12_rollout_velocity_cap_w63_63d_slope_v025_signal,
    f12rov_f12_rollout_velocity_cap_w126_5d_slope_v026_signal,
    f12rov_f12_rollout_velocity_cap_w126_10d_slope_v027_signal,
    f12rov_f12_rollout_velocity_cap_w126_21d_slope_v028_signal,
    f12rov_f12_rollout_velocity_cap_w126_42d_slope_v029_signal,
    f12rov_f12_rollout_velocity_cap_w126_63d_slope_v030_signal,
    f12rov_f12_rollout_velocity_cap_w189_5d_slope_v031_signal,
    f12rov_f12_rollout_velocity_cap_w189_10d_slope_v032_signal,
    f12rov_f12_rollout_velocity_cap_w189_21d_slope_v033_signal,
    f12rov_f12_rollout_velocity_cap_w189_42d_slope_v034_signal,
    f12rov_f12_rollout_velocity_cap_w189_63d_slope_v035_signal,
    f12rov_f12_rollout_velocity_cap_w252_5d_slope_v036_signal,
    f12rov_f12_rollout_velocity_cap_w252_10d_slope_v037_signal,
    f12rov_f12_rollout_velocity_cap_w252_21d_slope_v038_signal,
    f12rov_f12_rollout_velocity_cap_w252_42d_slope_v039_signal,
    f12rov_f12_rollout_velocity_cap_w252_63d_slope_v040_signal,
    f12rov_f12_rollout_velocity_cap_w378_5d_slope_v041_signal,
    f12rov_f12_rollout_velocity_cap_w378_10d_slope_v042_signal,
    f12rov_f12_rollout_velocity_cap_w378_21d_slope_v043_signal,
    f12rov_f12_rollout_velocity_cap_w378_42d_slope_v044_signal,
    f12rov_f12_rollout_velocity_cap_w378_63d_slope_v045_signal,
    f12rov_f12_rollout_velocity_cap_w504_5d_slope_v046_signal,
    f12rov_f12_rollout_velocity_cap_w504_10d_slope_v047_signal,
    f12rov_f12_rollout_velocity_cap_w504_21d_slope_v048_signal,
    f12rov_f12_rollout_velocity_cap_w504_42d_slope_v049_signal,
    f12rov_f12_rollout_velocity_cap_w504_63d_slope_v050_signal,
    f12rov_f12_rollout_velocity_rcd_w5_5d_slope_v051_signal,
    f12rov_f12_rollout_velocity_rcd_w5_10d_slope_v052_signal,
    f12rov_f12_rollout_velocity_rcd_w5_21d_slope_v053_signal,
    f12rov_f12_rollout_velocity_rcd_w5_42d_slope_v054_signal,
    f12rov_f12_rollout_velocity_rcd_w5_63d_slope_v055_signal,
    f12rov_f12_rollout_velocity_rcd_w10_5d_slope_v056_signal,
    f12rov_f12_rollout_velocity_rcd_w10_10d_slope_v057_signal,
    f12rov_f12_rollout_velocity_rcd_w10_21d_slope_v058_signal,
    f12rov_f12_rollout_velocity_rcd_w10_42d_slope_v059_signal,
    f12rov_f12_rollout_velocity_rcd_w10_63d_slope_v060_signal,
    f12rov_f12_rollout_velocity_rcd_w21_5d_slope_v061_signal,
    f12rov_f12_rollout_velocity_rcd_w21_10d_slope_v062_signal,
    f12rov_f12_rollout_velocity_rcd_w21_21d_slope_v063_signal,
    f12rov_f12_rollout_velocity_rcd_w21_42d_slope_v064_signal,
    f12rov_f12_rollout_velocity_rcd_w21_63d_slope_v065_signal,
    f12rov_f12_rollout_velocity_rcd_w42_5d_slope_v066_signal,
    f12rov_f12_rollout_velocity_rcd_w42_10d_slope_v067_signal,
    f12rov_f12_rollout_velocity_rcd_w42_21d_slope_v068_signal,
    f12rov_f12_rollout_velocity_rcd_w42_42d_slope_v069_signal,
    f12rov_f12_rollout_velocity_rcd_w42_63d_slope_v070_signal,
    f12rov_f12_rollout_velocity_rcd_w63_5d_slope_v071_signal,
    f12rov_f12_rollout_velocity_rcd_w63_10d_slope_v072_signal,
    f12rov_f12_rollout_velocity_rcd_w63_21d_slope_v073_signal,
    f12rov_f12_rollout_velocity_rcd_w63_42d_slope_v074_signal,
    f12rov_f12_rollout_velocity_rcd_w63_63d_slope_v075_signal,
    f12rov_f12_rollout_velocity_rcd_w126_5d_slope_v076_signal,
    f12rov_f12_rollout_velocity_rcd_w126_10d_slope_v077_signal,
    f12rov_f12_rollout_velocity_rcd_w126_21d_slope_v078_signal,
    f12rov_f12_rollout_velocity_rcd_w126_42d_slope_v079_signal,
    f12rov_f12_rollout_velocity_rcd_w126_63d_slope_v080_signal,
    f12rov_f12_rollout_velocity_rcd_w189_5d_slope_v081_signal,
    f12rov_f12_rollout_velocity_rcd_w189_10d_slope_v082_signal,
    f12rov_f12_rollout_velocity_rcd_w189_21d_slope_v083_signal,
    f12rov_f12_rollout_velocity_rcd_w189_42d_slope_v084_signal,
    f12rov_f12_rollout_velocity_rcd_w189_63d_slope_v085_signal,
    f12rov_f12_rollout_velocity_rcd_w252_5d_slope_v086_signal,
    f12rov_f12_rollout_velocity_rcd_w252_10d_slope_v087_signal,
    f12rov_f12_rollout_velocity_rcd_w252_21d_slope_v088_signal,
    f12rov_f12_rollout_velocity_rcd_w252_42d_slope_v089_signal,
    f12rov_f12_rollout_velocity_rcd_w252_63d_slope_v090_signal,
    f12rov_f12_rollout_velocity_rcd_w378_5d_slope_v091_signal,
    f12rov_f12_rollout_velocity_rcd_w378_10d_slope_v092_signal,
    f12rov_f12_rollout_velocity_rcd_w378_21d_slope_v093_signal,
    f12rov_f12_rollout_velocity_rcd_w378_42d_slope_v094_signal,
    f12rov_f12_rollout_velocity_rcd_w378_63d_slope_v095_signal,
    f12rov_f12_rollout_velocity_rcd_w504_5d_slope_v096_signal,
    f12rov_f12_rollout_velocity_rcd_w504_10d_slope_v097_signal,
    f12rov_f12_rollout_velocity_rcd_w504_21d_slope_v098_signal,
    f12rov_f12_rollout_velocity_rcd_w504_42d_slope_v099_signal,
    f12rov_f12_rollout_velocity_rcd_w504_63d_slope_v100_signal,
    f12rov_f12_rollout_velocity_sig_w5_5d_slope_v101_signal,
    f12rov_f12_rollout_velocity_sig_w5_10d_slope_v102_signal,
    f12rov_f12_rollout_velocity_sig_w5_21d_slope_v103_signal,
    f12rov_f12_rollout_velocity_sig_w5_42d_slope_v104_signal,
    f12rov_f12_rollout_velocity_sig_w5_63d_slope_v105_signal,
    f12rov_f12_rollout_velocity_sig_w10_5d_slope_v106_signal,
    f12rov_f12_rollout_velocity_sig_w10_10d_slope_v107_signal,
    f12rov_f12_rollout_velocity_sig_w10_21d_slope_v108_signal,
    f12rov_f12_rollout_velocity_sig_w10_42d_slope_v109_signal,
    f12rov_f12_rollout_velocity_sig_w10_63d_slope_v110_signal,
    f12rov_f12_rollout_velocity_sig_w21_5d_slope_v111_signal,
    f12rov_f12_rollout_velocity_sig_w21_10d_slope_v112_signal,
    f12rov_f12_rollout_velocity_sig_w21_21d_slope_v113_signal,
    f12rov_f12_rollout_velocity_sig_w21_42d_slope_v114_signal,
    f12rov_f12_rollout_velocity_sig_w21_63d_slope_v115_signal,
    f12rov_f12_rollout_velocity_sig_w42_5d_slope_v116_signal,
    f12rov_f12_rollout_velocity_sig_w42_10d_slope_v117_signal,
    f12rov_f12_rollout_velocity_sig_w42_21d_slope_v118_signal,
    f12rov_f12_rollout_velocity_sig_w42_42d_slope_v119_signal,
    f12rov_f12_rollout_velocity_sig_w42_63d_slope_v120_signal,
    f12rov_f12_rollout_velocity_sig_w63_5d_slope_v121_signal,
    f12rov_f12_rollout_velocity_sig_w63_10d_slope_v122_signal,
    f12rov_f12_rollout_velocity_sig_w63_21d_slope_v123_signal,
    f12rov_f12_rollout_velocity_sig_w63_42d_slope_v124_signal,
    f12rov_f12_rollout_velocity_sig_w63_63d_slope_v125_signal,
    f12rov_f12_rollout_velocity_sig_w126_5d_slope_v126_signal,
    f12rov_f12_rollout_velocity_sig_w126_10d_slope_v127_signal,
    f12rov_f12_rollout_velocity_sig_w126_21d_slope_v128_signal,
    f12rov_f12_rollout_velocity_sig_w126_42d_slope_v129_signal,
    f12rov_f12_rollout_velocity_sig_w126_63d_slope_v130_signal,
    f12rov_f12_rollout_velocity_sig_w189_5d_slope_v131_signal,
    f12rov_f12_rollout_velocity_sig_w189_10d_slope_v132_signal,
    f12rov_f12_rollout_velocity_sig_w189_21d_slope_v133_signal,
    f12rov_f12_rollout_velocity_sig_w189_42d_slope_v134_signal,
    f12rov_f12_rollout_velocity_sig_w189_63d_slope_v135_signal,
    f12rov_f12_rollout_velocity_sig_w252_5d_slope_v136_signal,
    f12rov_f12_rollout_velocity_sig_w252_10d_slope_v137_signal,
    f12rov_f12_rollout_velocity_sig_w252_21d_slope_v138_signal,
    f12rov_f12_rollout_velocity_sig_w252_42d_slope_v139_signal,
    f12rov_f12_rollout_velocity_sig_w252_63d_slope_v140_signal,
    f12rov_f12_rollout_velocity_sig_w378_5d_slope_v141_signal,
    f12rov_f12_rollout_velocity_sig_w378_10d_slope_v142_signal,
    f12rov_f12_rollout_velocity_sig_w378_21d_slope_v143_signal,
    f12rov_f12_rollout_velocity_sig_w378_42d_slope_v144_signal,
    f12rov_f12_rollout_velocity_sig_w378_63d_slope_v145_signal,
    f12rov_f12_rollout_velocity_sig_w504_5d_slope_v146_signal,
    f12rov_f12_rollout_velocity_sig_w504_10d_slope_v147_signal,
    f12rov_f12_rollout_velocity_sig_w504_21d_slope_v148_signal,
    f12rov_f12_rollout_velocity_sig_w504_42d_slope_v149_signal,
    f12rov_f12_rollout_velocity_sig_w504_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_ROLLOUT_VELOCITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex,
        "assets": assets, "ppnenet": ppnenet,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f12_capex_acceleration", "_f12_revenue_capex_dynamics", "_f12_rollout_signature")
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
    print(f"OK f12_rollout_velocity_2nd_derivatives_001_150_claude: {n_features} features pass")
