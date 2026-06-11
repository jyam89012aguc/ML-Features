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

def _f38_sga_intensity(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f38_sga_revenue_gap(sgna, revenue, w):
    ds = sgna.pct_change(periods=w)
    dr = revenue.pct_change(periods=w)
    return dr - ds


def _f38_sga_leverage(sgna, revenue, w):
    intensity = sgna / revenue.replace(0, np.nan)
    return -intensity.diff(periods=w)




def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d5d_slope_v001_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d10d_slope_v002_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d21d_slope_v003_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d42d_slope_v004_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d63d_slope_v005_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d126d_slope_v006_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d189d_slope_v007_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d252d_slope_v008_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d378d_slope_v009_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanw_5d504d_slope_v010_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d5d_slope_v011_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d10d_slope_v012_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d21d_slope_v013_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d42d_slope_v014_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d63d_slope_v015_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d126d_slope_v016_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d189d_slope_v017_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d252d_slope_v018_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d378d_slope_v019_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intstdw_5d504d_slope_v020_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d5d_slope_v021_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d10d_slope_v022_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d21d_slope_v023_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d42d_slope_v024_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d63d_slope_v025_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d126d_slope_v026_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d189d_slope_v027_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d252d_slope_v028_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d378d_slope_v029_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intzw_5d504d_slope_v030_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _z(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d5d_slope_v031_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d10d_slope_v032_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d21d_slope_v033_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d42d_slope_v034_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d63d_slope_v035_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d126d_slope_v036_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d189d_slope_v037_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d252d_slope_v038_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d378d_slope_v039_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d504d_slope_v040_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = _mean(inner, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d5d_slope_v041_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d10d_slope_v042_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d21d_slope_v043_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d42d_slope_v044_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d63d_slope_v045_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d126d_slope_v046_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d189d_slope_v047_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d252d_slope_v048_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d378d_slope_v049_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intemaxc_5d504d_slope_v050_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d5d_slope_v051_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d10d_slope_v052_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d21d_slope_v053_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d42d_slope_v054_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d63d_slope_v055_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d126d_slope_v056_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d189d_slope_v057_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d252d_slope_v058_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d378d_slope_v059_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d504d_slope_v060_signal(sgna, revenue, closeadj):
    inner = _f38_sga_intensity(sgna, revenue)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapraw_5d_slope_v061_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapxclose_5d_slope_v062_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d5d_slope_v063_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d10d_slope_v064_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d21d_slope_v065_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d42d_slope_v066_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d63d_slope_v067_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d126d_slope_v068_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d189d_slope_v069_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d252d_slope_v070_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d378d_slope_v071_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d504d_slope_v072_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d5d_slope_v073_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d10d_slope_v074_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d21d_slope_v075_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d42d_slope_v076_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d63d_slope_v077_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d126d_slope_v078_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d189d_slope_v079_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d252d_slope_v080_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d378d_slope_v081_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_5d504d_slope_v082_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d5d_slope_v083_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d10d_slope_v084_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d21d_slope_v085_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d42d_slope_v086_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d63d_slope_v087_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d126d_slope_v088_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d189d_slope_v089_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d252d_slope_v090_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d378d_slope_v091_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_5d504d_slope_v092_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _z(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapabsxc_5d_slope_v093_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapsqxc_5d_slope_v094_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner) * (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d5d_slope_v095_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d10d_slope_v096_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d21d_slope_v097_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d42d_slope_v098_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d63d_slope_v099_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d126d_slope_v100_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d189d_slope_v101_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d252d_slope_v102_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d378d_slope_v103_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d504d_slope_v104_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = _mean(inner, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d5d_slope_v105_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d10d_slope_v106_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d21d_slope_v107_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d42d_slope_v108_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d63d_slope_v109_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d126d_slope_v110_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d189d_slope_v111_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d252d_slope_v112_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d378d_slope_v113_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d504d_slope_v114_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d5d_slope_v115_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d10d_slope_v116_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d21d_slope_v117_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d42d_slope_v118_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d63d_slope_v119_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d126d_slope_v120_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d189d_slope_v121_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d252d_slope_v122_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d378d_slope_v123_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d504d_slope_v124_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 5)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapraw_10d_slope_v125_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapxclose_10d_slope_v126_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d5d_slope_v127_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d10d_slope_v128_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d21d_slope_v129_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d42d_slope_v130_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d63d_slope_v131_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d126d_slope_v132_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d189d_slope_v133_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d252d_slope_v134_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d378d_slope_v135_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d504d_slope_v136_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d5d_slope_v137_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d10d_slope_v138_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d21d_slope_v139_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d42d_slope_v140_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d63d_slope_v141_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d126d_slope_v142_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d189d_slope_v143_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d252d_slope_v144_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d378d_slope_v145_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapstdw_10d504d_slope_v146_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_10d5d_slope_v147_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_10d10d_slope_v148_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_10d21d_slope_v149_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f38hsl_f38_healthcare_sga_leverage_gapzw_10d42d_slope_v150_signal(sgna, revenue, closeadj):
    inner = _f38_sga_revenue_gap(sgna, revenue, 10)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d5d_slope_v001_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d10d_slope_v002_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d21d_slope_v003_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d42d_slope_v004_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d63d_slope_v005_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d126d_slope_v006_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d189d_slope_v007_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d252d_slope_v008_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d378d_slope_v009_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanw_5d504d_slope_v010_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d5d_slope_v011_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d10d_slope_v012_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d21d_slope_v013_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d42d_slope_v014_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d63d_slope_v015_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d126d_slope_v016_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d189d_slope_v017_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d252d_slope_v018_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d378d_slope_v019_signal,
    f38hsl_f38_healthcare_sga_leverage_intstdw_5d504d_slope_v020_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d5d_slope_v021_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d10d_slope_v022_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d21d_slope_v023_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d42d_slope_v024_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d63d_slope_v025_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d126d_slope_v026_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d189d_slope_v027_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d252d_slope_v028_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d378d_slope_v029_signal,
    f38hsl_f38_healthcare_sga_leverage_intzw_5d504d_slope_v030_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d5d_slope_v031_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d10d_slope_v032_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d21d_slope_v033_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d42d_slope_v034_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d63d_slope_v035_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d126d_slope_v036_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d189d_slope_v037_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d252d_slope_v038_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d378d_slope_v039_signal,
    f38hsl_f38_healthcare_sga_leverage_intmeanxc_5d504d_slope_v040_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d5d_slope_v041_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d10d_slope_v042_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d21d_slope_v043_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d42d_slope_v044_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d63d_slope_v045_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d126d_slope_v046_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d189d_slope_v047_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d252d_slope_v048_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d378d_slope_v049_signal,
    f38hsl_f38_healthcare_sga_leverage_intemaxc_5d504d_slope_v050_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d5d_slope_v051_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d10d_slope_v052_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d21d_slope_v053_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d42d_slope_v054_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d63d_slope_v055_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d126d_slope_v056_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d189d_slope_v057_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d252d_slope_v058_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d378d_slope_v059_signal,
    f38hsl_f38_healthcare_sga_leverage_intcumsumxc_5d504d_slope_v060_signal,
    f38hsl_f38_healthcare_sga_leverage_gapraw_5d_slope_v061_signal,
    f38hsl_f38_healthcare_sga_leverage_gapxclose_5d_slope_v062_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d5d_slope_v063_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d10d_slope_v064_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d21d_slope_v065_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d42d_slope_v066_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d63d_slope_v067_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d126d_slope_v068_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d189d_slope_v069_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d252d_slope_v070_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d378d_slope_v071_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_5d504d_slope_v072_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d5d_slope_v073_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d10d_slope_v074_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d21d_slope_v075_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d42d_slope_v076_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d63d_slope_v077_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d126d_slope_v078_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d189d_slope_v079_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d252d_slope_v080_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d378d_slope_v081_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_5d504d_slope_v082_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d5d_slope_v083_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d10d_slope_v084_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d21d_slope_v085_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d42d_slope_v086_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d63d_slope_v087_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d126d_slope_v088_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d189d_slope_v089_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d252d_slope_v090_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d378d_slope_v091_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_5d504d_slope_v092_signal,
    f38hsl_f38_healthcare_sga_leverage_gapabsxc_5d_slope_v093_signal,
    f38hsl_f38_healthcare_sga_leverage_gapsqxc_5d_slope_v094_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d5d_slope_v095_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d10d_slope_v096_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d21d_slope_v097_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d42d_slope_v098_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d63d_slope_v099_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d126d_slope_v100_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d189d_slope_v101_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d252d_slope_v102_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d378d_slope_v103_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanxc_5d504d_slope_v104_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d5d_slope_v105_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d10d_slope_v106_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d21d_slope_v107_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d42d_slope_v108_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d63d_slope_v109_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d126d_slope_v110_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d189d_slope_v111_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d252d_slope_v112_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d378d_slope_v113_signal,
    f38hsl_f38_healthcare_sga_leverage_gapemaxc_5d504d_slope_v114_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d5d_slope_v115_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d10d_slope_v116_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d21d_slope_v117_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d42d_slope_v118_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d63d_slope_v119_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d126d_slope_v120_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d189d_slope_v121_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d252d_slope_v122_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d378d_slope_v123_signal,
    f38hsl_f38_healthcare_sga_leverage_gapcumsumxc_5d504d_slope_v124_signal,
    f38hsl_f38_healthcare_sga_leverage_gapraw_10d_slope_v125_signal,
    f38hsl_f38_healthcare_sga_leverage_gapxclose_10d_slope_v126_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d5d_slope_v127_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d10d_slope_v128_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d21d_slope_v129_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d42d_slope_v130_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d63d_slope_v131_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d126d_slope_v132_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d189d_slope_v133_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d252d_slope_v134_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d378d_slope_v135_signal,
    f38hsl_f38_healthcare_sga_leverage_gapmeanw_10d504d_slope_v136_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d5d_slope_v137_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d10d_slope_v138_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d21d_slope_v139_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d42d_slope_v140_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d63d_slope_v141_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d126d_slope_v142_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d189d_slope_v143_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d252d_slope_v144_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d378d_slope_v145_signal,
    f38hsl_f38_healthcare_sga_leverage_gapstdw_10d504d_slope_v146_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_10d5d_slope_v147_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_10d10d_slope_v148_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_10d21d_slope_v149_signal,
    f38hsl_f38_healthcare_sga_leverage_gapzw_10d42d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F38_HEALTHCARE_SGA_LEVERAGE_REGISTRY_SLOPE_001_150 = REGISTRY



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
    domain_primitives = ("_f38_sga_intensity", "_f38_sga_revenue_gap", "_f38_sga_leverage")
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
    print(f"OK f38_healthcare_sga_leverage_2nd_derivatives_001_150_claude: {n_features} features pass")
