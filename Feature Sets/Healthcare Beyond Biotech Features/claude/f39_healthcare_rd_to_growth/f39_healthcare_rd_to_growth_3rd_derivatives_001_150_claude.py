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

def _f39_rd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f39_rd_growth_gap(rnd, revenue, w):
    drd = rnd.pct_change(periods=w)
    drv = revenue.pct_change(periods=w)
    return drv - drd


def _f39_rd_productivity(rnd, revenue, w):
    drv = revenue.diff(periods=w)
    rnd_avg = rnd.rolling(w, min_periods=max(1, w // 2)).mean()
    return drv / rnd_avg.replace(0, np.nan)




def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d5d_jerk_v001_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d10d_jerk_v002_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d21d_jerk_v003_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d42d_jerk_v004_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d63d_jerk_v005_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d126d_jerk_v006_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d189d_jerk_v007_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d252d_jerk_v008_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d378d_jerk_v009_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d504d_jerk_v010_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d5d_jerk_v011_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d10d_jerk_v012_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d21d_jerk_v013_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d42d_jerk_v014_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d63d_jerk_v015_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d126d_jerk_v016_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d189d_jerk_v017_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d252d_jerk_v018_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d378d_jerk_v019_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intstdw_5d504d_jerk_v020_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _std(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d5d_jerk_v021_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d10d_jerk_v022_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d21d_jerk_v023_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d42d_jerk_v024_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d63d_jerk_v025_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d126d_jerk_v026_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d189d_jerk_v027_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d252d_jerk_v028_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d378d_jerk_v029_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intzw_5d504d_jerk_v030_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _z(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d5d_jerk_v031_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d10d_jerk_v032_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d21d_jerk_v033_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d42d_jerk_v034_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d63d_jerk_v035_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d126d_jerk_v036_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d189d_jerk_v037_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d252d_jerk_v038_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d378d_jerk_v039_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d504d_jerk_v040_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = _mean(inner, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d5d_jerk_v041_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d10d_jerk_v042_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d21d_jerk_v043_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d42d_jerk_v044_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d63d_jerk_v045_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d126d_jerk_v046_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d189d_jerk_v047_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d252d_jerk_v048_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d378d_jerk_v049_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d504d_jerk_v050_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d5d_jerk_v051_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d10d_jerk_v052_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d21d_jerk_v053_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d42d_jerk_v054_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d63d_jerk_v055_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d126d_jerk_v056_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d189d_jerk_v057_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d252d_jerk_v058_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d378d_jerk_v059_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d504d_jerk_v060_signal(rnd, revenue, closeadj):
    inner = _f39_rd_intensity(rnd, revenue)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapraw_5d_jerk_v061_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapxclose_5d_jerk_v062_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d5d_jerk_v063_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d10d_jerk_v064_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d21d_jerk_v065_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d42d_jerk_v066_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d63d_jerk_v067_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d126d_jerk_v068_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d189d_jerk_v069_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d252d_jerk_v070_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d378d_jerk_v071_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d504d_jerk_v072_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d5d_jerk_v073_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d10d_jerk_v074_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d21d_jerk_v075_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d42d_jerk_v076_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d63d_jerk_v077_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d126d_jerk_v078_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d189d_jerk_v079_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d252d_jerk_v080_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d378d_jerk_v081_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d504d_jerk_v082_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _std(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d5d_jerk_v083_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d10d_jerk_v084_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d21d_jerk_v085_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d42d_jerk_v086_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d63d_jerk_v087_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d126d_jerk_v088_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d189d_jerk_v089_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d252d_jerk_v090_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d378d_jerk_v091_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_5d504d_jerk_v092_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _z(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapabsxc_5d_jerk_v093_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapsqxc_5d_jerk_v094_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner) * (inner).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d5d_jerk_v095_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d10d_jerk_v096_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d21d_jerk_v097_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d42d_jerk_v098_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d63d_jerk_v099_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d126d_jerk_v100_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d189d_jerk_v101_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d252d_jerk_v102_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d378d_jerk_v103_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d504d_jerk_v104_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = _mean(inner, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d5d_jerk_v105_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d10d_jerk_v106_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d21d_jerk_v107_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d42d_jerk_v108_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d63d_jerk_v109_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d126d_jerk_v110_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d189d_jerk_v111_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d252d_jerk_v112_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d378d_jerk_v113_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d504d_jerk_v114_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d5d_jerk_v115_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d10d_jerk_v116_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d21d_jerk_v117_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d42d_jerk_v118_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d63d_jerk_v119_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d126d_jerk_v120_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d189d_jerk_v121_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d252d_jerk_v122_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d378d_jerk_v123_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d504d_jerk_v124_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 5)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapraw_10d_jerk_v125_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = (inner)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapxclose_10d_jerk_v126_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = (inner) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d5d_jerk_v127_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d10d_jerk_v128_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d21d_jerk_v129_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d42d_jerk_v130_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d63d_jerk_v131_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d126d_jerk_v132_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d189d_jerk_v133_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d252d_jerk_v134_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d378d_jerk_v135_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d504d_jerk_v136_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _mean(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d5d_jerk_v137_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d10d_jerk_v138_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d21d_jerk_v139_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d42d_jerk_v140_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d63d_jerk_v141_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d126d_jerk_v142_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d189d_jerk_v143_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d252d_jerk_v144_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d378d_jerk_v145_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d504d_jerk_v146_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _std(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_10d5d_jerk_v147_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _z(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_10d10d_jerk_v148_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _z(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_10d21d_jerk_v149_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _z(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f39hrg_f39_healthcare_rd_to_growth_gapzw_10d42d_jerk_v150_signal(rnd, revenue, closeadj):
    inner = _f39_rd_growth_gap(rnd, revenue, 10)
    base = _z(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d5d_jerk_v001_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d10d_jerk_v002_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d21d_jerk_v003_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d42d_jerk_v004_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d63d_jerk_v005_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d126d_jerk_v006_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d189d_jerk_v007_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d252d_jerk_v008_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d378d_jerk_v009_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanw_5d504d_jerk_v010_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d5d_jerk_v011_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d10d_jerk_v012_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d21d_jerk_v013_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d42d_jerk_v014_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d63d_jerk_v015_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d126d_jerk_v016_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d189d_jerk_v017_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d252d_jerk_v018_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d378d_jerk_v019_signal,
    f39hrg_f39_healthcare_rd_to_growth_intstdw_5d504d_jerk_v020_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d5d_jerk_v021_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d10d_jerk_v022_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d21d_jerk_v023_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d42d_jerk_v024_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d63d_jerk_v025_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d126d_jerk_v026_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d189d_jerk_v027_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d252d_jerk_v028_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d378d_jerk_v029_signal,
    f39hrg_f39_healthcare_rd_to_growth_intzw_5d504d_jerk_v030_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d5d_jerk_v031_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d10d_jerk_v032_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d21d_jerk_v033_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d42d_jerk_v034_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d63d_jerk_v035_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d126d_jerk_v036_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d189d_jerk_v037_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d252d_jerk_v038_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d378d_jerk_v039_signal,
    f39hrg_f39_healthcare_rd_to_growth_intmeanxc_5d504d_jerk_v040_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d5d_jerk_v041_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d10d_jerk_v042_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d21d_jerk_v043_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d42d_jerk_v044_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d63d_jerk_v045_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d126d_jerk_v046_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d189d_jerk_v047_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d252d_jerk_v048_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d378d_jerk_v049_signal,
    f39hrg_f39_healthcare_rd_to_growth_intemaxc_5d504d_jerk_v050_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d5d_jerk_v051_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d10d_jerk_v052_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d21d_jerk_v053_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d42d_jerk_v054_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d63d_jerk_v055_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d126d_jerk_v056_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d189d_jerk_v057_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d252d_jerk_v058_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d378d_jerk_v059_signal,
    f39hrg_f39_healthcare_rd_to_growth_intcumsumxc_5d504d_jerk_v060_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapraw_5d_jerk_v061_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapxclose_5d_jerk_v062_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d5d_jerk_v063_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d10d_jerk_v064_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d21d_jerk_v065_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d42d_jerk_v066_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d63d_jerk_v067_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d126d_jerk_v068_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d189d_jerk_v069_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d252d_jerk_v070_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d378d_jerk_v071_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_5d504d_jerk_v072_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d5d_jerk_v073_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d10d_jerk_v074_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d21d_jerk_v075_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d42d_jerk_v076_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d63d_jerk_v077_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d126d_jerk_v078_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d189d_jerk_v079_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d252d_jerk_v080_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d378d_jerk_v081_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_5d504d_jerk_v082_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d5d_jerk_v083_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d10d_jerk_v084_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d21d_jerk_v085_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d42d_jerk_v086_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d63d_jerk_v087_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d126d_jerk_v088_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d189d_jerk_v089_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d252d_jerk_v090_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d378d_jerk_v091_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_5d504d_jerk_v092_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapabsxc_5d_jerk_v093_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapsqxc_5d_jerk_v094_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d5d_jerk_v095_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d10d_jerk_v096_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d21d_jerk_v097_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d42d_jerk_v098_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d63d_jerk_v099_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d126d_jerk_v100_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d189d_jerk_v101_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d252d_jerk_v102_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d378d_jerk_v103_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanxc_5d504d_jerk_v104_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d5d_jerk_v105_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d10d_jerk_v106_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d21d_jerk_v107_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d42d_jerk_v108_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d63d_jerk_v109_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d126d_jerk_v110_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d189d_jerk_v111_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d252d_jerk_v112_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d378d_jerk_v113_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapemaxc_5d504d_jerk_v114_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d5d_jerk_v115_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d10d_jerk_v116_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d21d_jerk_v117_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d42d_jerk_v118_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d63d_jerk_v119_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d126d_jerk_v120_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d189d_jerk_v121_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d252d_jerk_v122_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d378d_jerk_v123_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapcumsumxc_5d504d_jerk_v124_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapraw_10d_jerk_v125_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapxclose_10d_jerk_v126_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d5d_jerk_v127_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d10d_jerk_v128_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d21d_jerk_v129_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d42d_jerk_v130_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d63d_jerk_v131_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d126d_jerk_v132_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d189d_jerk_v133_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d252d_jerk_v134_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d378d_jerk_v135_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapmeanw_10d504d_jerk_v136_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d5d_jerk_v137_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d10d_jerk_v138_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d21d_jerk_v139_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d42d_jerk_v140_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d63d_jerk_v141_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d126d_jerk_v142_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d189d_jerk_v143_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d252d_jerk_v144_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d378d_jerk_v145_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapstdw_10d504d_jerk_v146_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_10d5d_jerk_v147_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_10d10d_jerk_v148_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_10d21d_jerk_v149_signal,
    f39hrg_f39_healthcare_rd_to_growth_gapzw_10d42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F39_HEALTHCARE_RD_TO_GROWTH_REGISTRY_JERK_001_150 = REGISTRY



if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit,
        "sgna": sgna, "opex": opex, "rnd": rnd,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f39_rd_intensity", "_f39_rd_growth_gap", "_f39_rd_productivity")
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
    print(f"OK f39_healthcare_rd_to_growth_3rd_derivatives_001_150_claude: {n_features} features pass")
