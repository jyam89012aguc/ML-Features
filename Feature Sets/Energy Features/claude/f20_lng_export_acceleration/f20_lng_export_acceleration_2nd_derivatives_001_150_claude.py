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


# ===== folder domain primitives =====
def _f20_revenue_accel(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.shift(w)


def _f20_export_pulse(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return revenue / m.replace(0, np.nan) - 1.0


def _f20_export_signature(revenue, capex, w):
    rg = revenue.pct_change(periods=w)
    cg = capex.pct_change(periods=w)
    return rg - cg

def f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope5d_slope_v001_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope10d_slope_v002_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope21d_slope_v003_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope42d_slope_v004_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope63d_slope_v005_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope126d_slope_v006_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope5d_slope_v007_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope10d_slope_v008_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope21d_slope_v009_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope42d_slope_v010_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope63d_slope_v011_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope126d_slope_v012_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope5d_slope_v013_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope10d_slope_v014_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope21d_slope_v015_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope42d_slope_v016_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope63d_slope_v017_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope126d_slope_v018_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope5d_slope_v019_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope10d_slope_v020_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope21d_slope_v021_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope42d_slope_v022_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope63d_slope_v023_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope126d_slope_v024_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope5d_slope_v025_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope10d_slope_v026_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope21d_slope_v027_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope42d_slope_v028_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope63d_slope_v029_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope126d_slope_v030_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope5d_slope_v031_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope10d_slope_v032_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope21d_slope_v033_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope42d_slope_v034_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope63d_slope_v035_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope126d_slope_v036_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope5d_slope_v037_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope10d_slope_v038_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope21d_slope_v039_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope42d_slope_v040_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope63d_slope_v041_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope126d_slope_v042_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope5d_slope_v043_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope10d_slope_v044_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope21d_slope_v045_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope42d_slope_v046_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope63d_slope_v047_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope126d_slope_v048_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope5d_slope_v049_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope10d_slope_v050_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope21d_slope_v051_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope42d_slope_v052_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope63d_slope_v053_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope126d_slope_v054_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope5d_slope_v055_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope10d_slope_v056_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope21d_slope_v057_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope42d_slope_v058_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope63d_slope_v059_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope126d_slope_v060_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope10d_slope_v061_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope21d_slope_v062_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope42d_slope_v063_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope63d_slope_v064_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope126d_slope_v065_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope5d_slope_v066_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope10d_slope_v067_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope21d_slope_v068_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope42d_slope_v069_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope63d_slope_v070_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope126d_slope_v071_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope5d_slope_v072_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope10d_slope_v073_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope21d_slope_v074_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope42d_slope_v075_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope63d_slope_v076_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope126d_slope_v077_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope5d_slope_v078_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope10d_slope_v079_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope21d_slope_v080_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope42d_slope_v081_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope63d_slope_v082_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope126d_slope_v083_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope5d_slope_v084_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope10d_slope_v085_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope21d_slope_v086_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope42d_slope_v087_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope63d_slope_v088_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope126d_slope_v089_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope5d_slope_v090_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope10d_slope_v091_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope21d_slope_v092_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope42d_slope_v093_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope63d_slope_v094_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope126d_slope_v095_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * _z(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope5d_slope_v096_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope10d_slope_v097_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope21d_slope_v098_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope42d_slope_v099_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope63d_slope_v100_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope126d_slope_v101_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope5d_slope_v102_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope10d_slope_v103_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope21d_slope_v104_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope42d_slope_v105_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope63d_slope_v106_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope126d_slope_v107_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.pct_change(63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope5d_slope_v108_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope10d_slope_v109_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope21d_slope_v110_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope42d_slope_v111_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope63d_slope_v112_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope126d_slope_v113_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope5d_slope_v114_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope10d_slope_v115_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope21d_slope_v116_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope42d_slope_v117_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope63d_slope_v118_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope126d_slope_v119_signal(revenue, closeadj):
    result = _slope_pct((_f20_revenue_accel(revenue, 5)) * closeadj.ewm(span=21, min_periods=10).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_raraw_5d21dcl_slope5d_slope_v120_signal(revenue, closeadj):
    result = _slope_diff_norm((_f20_revenue_accel(revenue, 5)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope5d_slope_v121_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope10d_slope_v122_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope21d_slope_v123_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope42d_slope_v124_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope63d_slope_v125_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope126d_slope_v126_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope5d_slope_v127_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope10d_slope_v128_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope21d_slope_v129_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope42d_slope_v130_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 5), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope63d_slope_v131_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope126d_slope_v132_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope5d_slope_v133_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope10d_slope_v134_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope21d_slope_v135_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope42d_slope_v136_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope63d_slope_v137_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope126d_slope_v138_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope5d_slope_v139_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 63), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope10d_slope_v140_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope21d_slope_v141_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope42d_slope_v142_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope63d_slope_v143_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope126d_slope_v144_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _mean(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope5d_slope_v145_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _z(closeadj, 21), 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope10d_slope_v146_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _z(closeadj, 21), 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope21d_slope_v147_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _z(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope42d_slope_v148_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _z(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope63d_slope_v149_signal(revenue, closeadj):
    result = _slope_pct(_mean(_f20_revenue_accel(revenue, 5), 5) * _z(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope126d_slope_v150_signal(revenue, closeadj):
    result = _slope_diff_norm(_mean(_f20_revenue_accel(revenue, 5), 5) * _z(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope5d_slope_v001_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope10d_slope_v002_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope21d_slope_v003_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope42d_slope_v004_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope63d_slope_v005_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl_slope126d_slope_v006_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope5d_slope_v007_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope10d_slope_v008_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope21d_slope_v009_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope42d_slope_v010_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope63d_slope_v011_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl5_slope126d_slope_v012_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope5d_slope_v013_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope10d_slope_v014_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope21d_slope_v015_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope42d_slope_v016_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope63d_slope_v017_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl21_slope126d_slope_v018_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope5d_slope_v019_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope10d_slope_v020_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope21d_slope_v021_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope42d_slope_v022_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope63d_slope_v023_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dcl63_slope126d_slope_v024_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope5d_slope_v025_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope10d_slope_v026_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope21d_slope_v027_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope42d_slope_v028_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope63d_slope_v029_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz21_slope126d_slope_v030_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope5d_slope_v031_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope10d_slope_v032_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope21d_slope_v033_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope42d_slope_v034_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope63d_slope_v035_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclz63_slope126d_slope_v036_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope5d_slope_v037_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope10d_slope_v038_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope21d_slope_v039_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope42d_slope_v040_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope63d_slope_v041_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret21_slope126d_slope_v042_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope5d_slope_v043_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope10d_slope_v044_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope21d_slope_v045_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope42d_slope_v046_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope63d_slope_v047_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclret63_slope126d_slope_v048_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope5d_slope_v049_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope10d_slope_v050_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope21d_slope_v051_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope42d_slope_v052_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope63d_slope_v053_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclsqr_slope126d_slope_v054_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope5d_slope_v055_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope10d_slope_v056_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope21d_slope_v057_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope42d_slope_v058_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope63d_slope_v059_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d5dclema21_slope126d_slope_v060_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope10d_slope_v061_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope21d_slope_v062_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope42d_slope_v063_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope63d_slope_v064_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl_slope126d_slope_v065_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope5d_slope_v066_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope10d_slope_v067_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope21d_slope_v068_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope42d_slope_v069_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope63d_slope_v070_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl5_slope126d_slope_v071_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope5d_slope_v072_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope10d_slope_v073_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope21d_slope_v074_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope42d_slope_v075_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope63d_slope_v076_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl21_slope126d_slope_v077_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope5d_slope_v078_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope10d_slope_v079_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope21d_slope_v080_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope42d_slope_v081_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope63d_slope_v082_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dcl63_slope126d_slope_v083_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope5d_slope_v084_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope10d_slope_v085_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope21d_slope_v086_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope42d_slope_v087_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope63d_slope_v088_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz21_slope126d_slope_v089_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope5d_slope_v090_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope10d_slope_v091_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope21d_slope_v092_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope42d_slope_v093_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope63d_slope_v094_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclz63_slope126d_slope_v095_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope5d_slope_v096_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope10d_slope_v097_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope21d_slope_v098_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope42d_slope_v099_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope63d_slope_v100_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret21_slope126d_slope_v101_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope5d_slope_v102_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope10d_slope_v103_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope21d_slope_v104_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope42d_slope_v105_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope63d_slope_v106_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclret63_slope126d_slope_v107_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope5d_slope_v108_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope10d_slope_v109_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope21d_slope_v110_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope42d_slope_v111_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope63d_slope_v112_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclsqr_slope126d_slope_v113_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope5d_slope_v114_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope10d_slope_v115_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope21d_slope_v116_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope42d_slope_v117_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope63d_slope_v118_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d10dclema21_slope126d_slope_v119_signal,
    f20lea_f20_lng_export_acceleration_raraw_5d21dcl_slope5d_slope_v120_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope5d_slope_v121_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope10d_slope_v122_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope21d_slope_v123_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope42d_slope_v124_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope63d_slope_v125_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl_slope126d_slope_v126_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope5d_slope_v127_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope10d_slope_v128_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope21d_slope_v129_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope42d_slope_v130_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope63d_slope_v131_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl5_slope126d_slope_v132_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope5d_slope_v133_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope10d_slope_v134_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope21d_slope_v135_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope42d_slope_v136_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope63d_slope_v137_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl21_slope126d_slope_v138_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope5d_slope_v139_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope10d_slope_v140_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope21d_slope_v141_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope42d_slope_v142_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope63d_slope_v143_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dcl63_slope126d_slope_v144_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope5d_slope_v145_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope10d_slope_v146_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope21d_slope_v147_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope42d_slope_v148_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope63d_slope_v149_signal,
    f20lea_f20_lng_export_acceleration_ramean_5d5dclz21_slope126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_LNG_EXPORT_ACCELERATION_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex,
            "ppnenet": ppnenet, "assets": assets, "deferredrev": deferredrev}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f20_revenue_accel', '_f20_export_pulse', '_f20_export_signature',)
    import hashlib
    seen_bodies = set()
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
        body = "\n".join(l.strip() for l in src.splitlines()
                          if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("def "))
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(h)
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_lng_export_acceleration_slope_001_150_claude: {n_features} features pass")
