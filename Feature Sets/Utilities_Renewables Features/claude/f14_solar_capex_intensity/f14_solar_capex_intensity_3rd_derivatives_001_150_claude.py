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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f14_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f14_capex_burn(capex, fcf, w):
    burn = capex - fcf
    return burn.rolling(w, min_periods=max(1, w // 2)).mean()


def _f14_capex_dynamics(capex, revenue, w):
    r = capex / revenue.replace(0, np.nan).abs()
    return r.diff(periods=w) / r.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def f14sci_f14_solar_capex_intensity_intensity_smooth_21_5d_jerk_v001_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_5d_jerk_v002_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_5d_jerk_v003_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_5d_jerk_v004_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_5d_jerk_v005_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_5d_jerk_v006_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_5d_jerk_v007_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_5d_jerk_v008_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_5d_jerk_v009_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_5d_jerk_v010_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_5d_jerk_v011_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_5d_jerk_v012_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_5d_jerk_v013_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_5d_jerk_v014_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_5d_jerk_v015_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_10d_jerk_v016_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_10d_jerk_v017_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_10d_jerk_v018_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_10d_jerk_v019_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_10d_jerk_v020_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_10d_jerk_v021_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_10d_jerk_v022_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_10d_jerk_v023_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_10d_jerk_v024_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_10d_jerk_v025_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_10d_jerk_v026_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_10d_jerk_v027_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_10d_jerk_v028_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_10d_jerk_v029_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_10d_jerk_v030_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_21d_jerk_v031_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_21d_jerk_v032_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_21d_jerk_v033_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_21d_jerk_v034_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_21d_jerk_v035_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_21d_jerk_v036_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_21d_jerk_v037_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_21d_jerk_v038_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_21d_jerk_v039_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_21d_jerk_v040_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_21d_jerk_v041_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_21d_jerk_v042_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_21d_jerk_v043_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_21d_jerk_v044_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_21d_jerk_v045_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_42d_jerk_v046_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_42d_jerk_v047_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_42d_jerk_v048_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_42d_jerk_v049_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_42d_jerk_v050_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_42d_jerk_v051_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_42d_jerk_v052_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_42d_jerk_v053_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_42d_jerk_v054_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_42d_jerk_v055_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_42d_jerk_v056_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_42d_jerk_v057_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_42d_jerk_v058_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_42d_jerk_v059_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_42d_jerk_v060_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_63d_jerk_v061_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_63d_jerk_v062_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_63d_jerk_v063_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_63d_jerk_v064_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_63d_jerk_v065_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_63d_jerk_v066_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_63d_jerk_v067_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_63d_jerk_v068_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_63d_jerk_v069_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_63d_jerk_v070_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_63d_jerk_v071_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_63d_jerk_v072_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_63d_jerk_v073_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_63d_jerk_v074_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_63d_jerk_v075_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_126d_jerk_v076_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_126d_jerk_v077_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_126d_jerk_v078_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_126d_jerk_v079_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_126d_jerk_v080_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_126d_jerk_v081_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_126d_jerk_v082_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_126d_jerk_v083_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_126d_jerk_v084_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_126d_jerk_v085_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_126d_jerk_v086_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_126d_jerk_v087_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_126d_jerk_v088_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_126d_jerk_v089_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_126d_jerk_v090_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_189d_jerk_v091_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_189d_jerk_v092_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_189d_jerk_v093_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_189d_jerk_v094_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_189d_jerk_v095_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_189d_jerk_v096_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_189d_jerk_v097_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_189d_jerk_v098_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_189d_jerk_v099_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_189d_jerk_v100_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_189d_jerk_v101_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_189d_jerk_v102_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_189d_jerk_v103_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_189d_jerk_v104_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_189d_jerk_v105_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_252d_jerk_v106_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_252d_jerk_v107_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_252d_jerk_v108_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_252d_jerk_v109_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_252d_jerk_v110_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_252d_jerk_v111_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_252d_jerk_v112_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_252d_jerk_v113_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_252d_jerk_v114_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_252d_jerk_v115_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_252d_jerk_v116_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_252d_jerk_v117_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_252d_jerk_v118_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_252d_jerk_v119_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_252d_jerk_v120_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_378d_jerk_v121_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_378d_jerk_v122_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_378d_jerk_v123_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_378d_jerk_v124_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_378d_jerk_v125_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_378d_jerk_v126_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_378d_jerk_v127_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_378d_jerk_v128_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_378d_jerk_v129_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_378d_jerk_v130_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_378d_jerk_v131_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_378d_jerk_v132_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_378d_jerk_v133_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_378d_jerk_v134_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_378d_jerk_v135_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_21_504d_jerk_v136_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_21_504d_jerk_v137_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 21) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_21_504d_jerk_v138_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 21) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_21_504d_jerk_v139_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_21_504d_jerk_v140_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 21), 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_63_504d_jerk_v141_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_63_504d_jerk_v142_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_63_504d_jerk_v143_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_63_504d_jerk_v144_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_63_504d_jerk_v145_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 63), 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_smooth_252_504d_jerk_v146_signal(closeadj):
    base = _mean(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_252_504d_jerk_v147_signal(closeadj):
    base = _f14_capex_burn(capex, fcf, 252) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_dyn_252_504d_jerk_v148_signal(closeadj):
    base = _f14_capex_dynamics(capex, revenue, 252) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_intensity_z_252_504d_jerk_v149_signal(closeadj):
    base = _z(_f14_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

def f14sci_f14_solar_capex_intensity_burn_z_252_504d_jerk_v150_signal(closeadj):
    base = _z(_f14_capex_burn(capex, fcf, 252), 63) * closeadj
    result = _jerk(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_5d_jerk_v001_signal,
    f14sci_f14_solar_capex_intensity_burn_21_5d_jerk_v002_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_5d_jerk_v003_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_5d_jerk_v004_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_5d_jerk_v005_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_5d_jerk_v006_signal,
    f14sci_f14_solar_capex_intensity_burn_63_5d_jerk_v007_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_5d_jerk_v008_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_5d_jerk_v009_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_5d_jerk_v010_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_5d_jerk_v011_signal,
    f14sci_f14_solar_capex_intensity_burn_252_5d_jerk_v012_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_5d_jerk_v013_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_5d_jerk_v014_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_5d_jerk_v015_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_10d_jerk_v016_signal,
    f14sci_f14_solar_capex_intensity_burn_21_10d_jerk_v017_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_10d_jerk_v018_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_10d_jerk_v019_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_10d_jerk_v020_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_10d_jerk_v021_signal,
    f14sci_f14_solar_capex_intensity_burn_63_10d_jerk_v022_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_10d_jerk_v023_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_10d_jerk_v024_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_10d_jerk_v025_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_10d_jerk_v026_signal,
    f14sci_f14_solar_capex_intensity_burn_252_10d_jerk_v027_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_10d_jerk_v028_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_10d_jerk_v029_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_10d_jerk_v030_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_21d_jerk_v031_signal,
    f14sci_f14_solar_capex_intensity_burn_21_21d_jerk_v032_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_21d_jerk_v033_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_21d_jerk_v034_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_21d_jerk_v035_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_21d_jerk_v036_signal,
    f14sci_f14_solar_capex_intensity_burn_63_21d_jerk_v037_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_21d_jerk_v038_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_21d_jerk_v039_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_21d_jerk_v040_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_21d_jerk_v041_signal,
    f14sci_f14_solar_capex_intensity_burn_252_21d_jerk_v042_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_21d_jerk_v043_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_21d_jerk_v044_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_21d_jerk_v045_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_42d_jerk_v046_signal,
    f14sci_f14_solar_capex_intensity_burn_21_42d_jerk_v047_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_42d_jerk_v048_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_42d_jerk_v049_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_42d_jerk_v050_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_42d_jerk_v051_signal,
    f14sci_f14_solar_capex_intensity_burn_63_42d_jerk_v052_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_42d_jerk_v053_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_42d_jerk_v054_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_42d_jerk_v055_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_42d_jerk_v056_signal,
    f14sci_f14_solar_capex_intensity_burn_252_42d_jerk_v057_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_42d_jerk_v058_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_42d_jerk_v059_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_42d_jerk_v060_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_63d_jerk_v061_signal,
    f14sci_f14_solar_capex_intensity_burn_21_63d_jerk_v062_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_63d_jerk_v063_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_63d_jerk_v064_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_63d_jerk_v065_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_63d_jerk_v066_signal,
    f14sci_f14_solar_capex_intensity_burn_63_63d_jerk_v067_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_63d_jerk_v068_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_63d_jerk_v069_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_63d_jerk_v070_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_63d_jerk_v071_signal,
    f14sci_f14_solar_capex_intensity_burn_252_63d_jerk_v072_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_63d_jerk_v073_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_63d_jerk_v074_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_63d_jerk_v075_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_126d_jerk_v076_signal,
    f14sci_f14_solar_capex_intensity_burn_21_126d_jerk_v077_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_126d_jerk_v078_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_126d_jerk_v079_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_126d_jerk_v080_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_126d_jerk_v081_signal,
    f14sci_f14_solar_capex_intensity_burn_63_126d_jerk_v082_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_126d_jerk_v083_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_126d_jerk_v084_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_126d_jerk_v085_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_126d_jerk_v086_signal,
    f14sci_f14_solar_capex_intensity_burn_252_126d_jerk_v087_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_126d_jerk_v088_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_126d_jerk_v089_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_126d_jerk_v090_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_189d_jerk_v091_signal,
    f14sci_f14_solar_capex_intensity_burn_21_189d_jerk_v092_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_189d_jerk_v093_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_189d_jerk_v094_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_189d_jerk_v095_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_189d_jerk_v096_signal,
    f14sci_f14_solar_capex_intensity_burn_63_189d_jerk_v097_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_189d_jerk_v098_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_189d_jerk_v099_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_189d_jerk_v100_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_189d_jerk_v101_signal,
    f14sci_f14_solar_capex_intensity_burn_252_189d_jerk_v102_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_189d_jerk_v103_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_189d_jerk_v104_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_189d_jerk_v105_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_252d_jerk_v106_signal,
    f14sci_f14_solar_capex_intensity_burn_21_252d_jerk_v107_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_252d_jerk_v108_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_252d_jerk_v109_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_252d_jerk_v110_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_252d_jerk_v111_signal,
    f14sci_f14_solar_capex_intensity_burn_63_252d_jerk_v112_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_252d_jerk_v113_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_252d_jerk_v114_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_252d_jerk_v115_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_252d_jerk_v116_signal,
    f14sci_f14_solar_capex_intensity_burn_252_252d_jerk_v117_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_252d_jerk_v118_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_252d_jerk_v119_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_252d_jerk_v120_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_378d_jerk_v121_signal,
    f14sci_f14_solar_capex_intensity_burn_21_378d_jerk_v122_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_378d_jerk_v123_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_378d_jerk_v124_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_378d_jerk_v125_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_378d_jerk_v126_signal,
    f14sci_f14_solar_capex_intensity_burn_63_378d_jerk_v127_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_378d_jerk_v128_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_378d_jerk_v129_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_378d_jerk_v130_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_378d_jerk_v131_signal,
    f14sci_f14_solar_capex_intensity_burn_252_378d_jerk_v132_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_378d_jerk_v133_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_378d_jerk_v134_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_378d_jerk_v135_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_21_504d_jerk_v136_signal,
    f14sci_f14_solar_capex_intensity_burn_21_504d_jerk_v137_signal,
    f14sci_f14_solar_capex_intensity_dyn_21_504d_jerk_v138_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_21_504d_jerk_v139_signal,
    f14sci_f14_solar_capex_intensity_burn_z_21_504d_jerk_v140_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_63_504d_jerk_v141_signal,
    f14sci_f14_solar_capex_intensity_burn_63_504d_jerk_v142_signal,
    f14sci_f14_solar_capex_intensity_dyn_63_504d_jerk_v143_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_63_504d_jerk_v144_signal,
    f14sci_f14_solar_capex_intensity_burn_z_63_504d_jerk_v145_signal,
    f14sci_f14_solar_capex_intensity_intensity_smooth_252_504d_jerk_v146_signal,
    f14sci_f14_solar_capex_intensity_burn_252_504d_jerk_v147_signal,
    f14sci_f14_solar_capex_intensity_dyn_252_504d_jerk_v148_signal,
    f14sci_f14_solar_capex_intensity_intensity_z_252_504d_jerk_v149_signal,
    f14sci_f14_solar_capex_intensity_burn_z_252_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_SOLAR_CAPEX_INTENSITY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f14_capex_intensity", "_f14_capex_burn", "_f14_capex_dynamics",)
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
    print(f"OK f14_solar_capex_intensity_3rd_derivatives_001_150_claude: {n_features} features pass")
