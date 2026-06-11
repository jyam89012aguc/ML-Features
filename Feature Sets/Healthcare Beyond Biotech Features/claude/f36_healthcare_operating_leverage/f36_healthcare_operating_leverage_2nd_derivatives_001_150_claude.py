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

def _f36_op_leverage_proxy(ebit, revenue, w):
    em = (ebit / revenue.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()
    eb = ebit.rolling(w, min_periods=max(1, w // 2)).mean()
    rv = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return em * eb / rv.replace(0, np.nan)


def _f36_margin_revenue_beta(ebitdamargin, revenue, w):
    dm = ebitdamargin.diff(periods=w)
    dr = revenue.pct_change(periods=w)
    return dm / dr.replace(0, np.nan)


def _f36_drop_through(ebit, revenue, w):
    deb = ebit.diff(periods=w)
    drv = revenue.diff(periods=w)
    return deb / drv.replace(0, np.nan)




def f36hol_f36_healthcare_operating_leverage_oplraw_5d_slope_v001_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplxclose_5d_slope_v002_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d5d_slope_v003_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d10d_slope_v004_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d21d_slope_v005_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d42d_slope_v006_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d63d_slope_v007_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d126d_slope_v008_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d189d_slope_v009_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d252d_slope_v010_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d378d_slope_v011_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_5d504d_slope_v012_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d5d_slope_v013_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d10d_slope_v014_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d21d_slope_v015_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d42d_slope_v016_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d63d_slope_v017_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d126d_slope_v018_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d189d_slope_v019_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d252d_slope_v020_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d378d_slope_v021_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_5d504d_slope_v022_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d5d_slope_v023_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d10d_slope_v024_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d21d_slope_v025_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d42d_slope_v026_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d63d_slope_v027_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d126d_slope_v028_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d189d_slope_v029_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d252d_slope_v030_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d378d_slope_v031_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_5d504d_slope_v032_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _z(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplabsxc_5d_slope_v033_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplsqxc_5d_slope_v034_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner) * (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d5d_slope_v035_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d10d_slope_v036_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d21d_slope_v037_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d42d_slope_v038_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d63d_slope_v039_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d126d_slope_v040_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d189d_slope_v041_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d252d_slope_v042_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d378d_slope_v043_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d504d_slope_v044_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = _mean(inner, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d5d_slope_v045_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d10d_slope_v046_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d21d_slope_v047_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d42d_slope_v048_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d63d_slope_v049_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d126d_slope_v050_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d189d_slope_v051_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d252d_slope_v052_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d378d_slope_v053_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_5d504d_slope_v054_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d5d_slope_v055_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d10d_slope_v056_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d21d_slope_v057_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d42d_slope_v058_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d63d_slope_v059_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d126d_slope_v060_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d189d_slope_v061_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d252d_slope_v062_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d378d_slope_v063_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d504d_slope_v064_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 5)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplraw_10d_slope_v065_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplxclose_10d_slope_v066_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d5d_slope_v067_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d10d_slope_v068_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d21d_slope_v069_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d42d_slope_v070_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d63d_slope_v071_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d126d_slope_v072_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d189d_slope_v073_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d252d_slope_v074_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d378d_slope_v075_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_10d504d_slope_v076_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d5d_slope_v077_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d10d_slope_v078_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d21d_slope_v079_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d42d_slope_v080_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d63d_slope_v081_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d126d_slope_v082_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d189d_slope_v083_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d252d_slope_v084_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d378d_slope_v085_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_10d504d_slope_v086_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d5d_slope_v087_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d10d_slope_v088_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d21d_slope_v089_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d42d_slope_v090_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d63d_slope_v091_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d126d_slope_v092_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d189d_slope_v093_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d252d_slope_v094_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d378d_slope_v095_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplzw_10d504d_slope_v096_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _z(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplabsxc_10d_slope_v097_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplsqxc_10d_slope_v098_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner) * (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d5d_slope_v099_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d10d_slope_v100_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d21d_slope_v101_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d42d_slope_v102_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d63d_slope_v103_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d126d_slope_v104_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d189d_slope_v105_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d252d_slope_v106_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d378d_slope_v107_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d504d_slope_v108_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = _mean(inner, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d5d_slope_v109_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d10d_slope_v110_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d21d_slope_v111_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d42d_slope_v112_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d63d_slope_v113_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d126d_slope_v114_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d189d_slope_v115_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d252d_slope_v116_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d378d_slope_v117_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplemaxc_10d504d_slope_v118_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d5d_slope_v119_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d10d_slope_v120_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d21d_slope_v121_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d42d_slope_v122_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d63d_slope_v123_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d126d_slope_v124_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d189d_slope_v125_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d252d_slope_v126_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d378d_slope_v127_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d504d_slope_v128_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 10)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplraw_21d_slope_v129_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplxclose_21d_slope_v130_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d5d_slope_v131_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d10d_slope_v132_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d21d_slope_v133_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d42d_slope_v134_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d63d_slope_v135_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d126d_slope_v136_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d189d_slope_v137_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d252d_slope_v138_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d378d_slope_v139_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplmeanw_21d504d_slope_v140_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d5d_slope_v141_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d10d_slope_v142_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d21d_slope_v143_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d42d_slope_v144_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d63d_slope_v145_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d126d_slope_v146_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d189d_slope_v147_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d252d_slope_v148_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d378d_slope_v149_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36hol_f36_healthcare_operating_leverage_oplstdw_21d504d_slope_v150_signal(ebit, revenue, closeadj):
    inner = _f36_op_leverage_proxy(ebit, revenue, 21)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36hol_f36_healthcare_operating_leverage_oplraw_5d_slope_v001_signal,
    f36hol_f36_healthcare_operating_leverage_oplxclose_5d_slope_v002_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d5d_slope_v003_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d10d_slope_v004_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d21d_slope_v005_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d42d_slope_v006_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d63d_slope_v007_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d126d_slope_v008_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d189d_slope_v009_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d252d_slope_v010_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d378d_slope_v011_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_5d504d_slope_v012_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d5d_slope_v013_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d10d_slope_v014_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d21d_slope_v015_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d42d_slope_v016_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d63d_slope_v017_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d126d_slope_v018_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d189d_slope_v019_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d252d_slope_v020_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d378d_slope_v021_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_5d504d_slope_v022_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d5d_slope_v023_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d10d_slope_v024_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d21d_slope_v025_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d42d_slope_v026_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d63d_slope_v027_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d126d_slope_v028_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d189d_slope_v029_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d252d_slope_v030_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d378d_slope_v031_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_5d504d_slope_v032_signal,
    f36hol_f36_healthcare_operating_leverage_oplabsxc_5d_slope_v033_signal,
    f36hol_f36_healthcare_operating_leverage_oplsqxc_5d_slope_v034_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d5d_slope_v035_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d10d_slope_v036_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d21d_slope_v037_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d42d_slope_v038_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d63d_slope_v039_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d126d_slope_v040_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d189d_slope_v041_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d252d_slope_v042_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d378d_slope_v043_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_5d504d_slope_v044_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d5d_slope_v045_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d10d_slope_v046_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d21d_slope_v047_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d42d_slope_v048_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d63d_slope_v049_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d126d_slope_v050_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d189d_slope_v051_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d252d_slope_v052_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d378d_slope_v053_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_5d504d_slope_v054_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d5d_slope_v055_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d10d_slope_v056_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d21d_slope_v057_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d42d_slope_v058_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d63d_slope_v059_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d126d_slope_v060_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d189d_slope_v061_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d252d_slope_v062_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d378d_slope_v063_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_5d504d_slope_v064_signal,
    f36hol_f36_healthcare_operating_leverage_oplraw_10d_slope_v065_signal,
    f36hol_f36_healthcare_operating_leverage_oplxclose_10d_slope_v066_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d5d_slope_v067_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d10d_slope_v068_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d21d_slope_v069_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d42d_slope_v070_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d63d_slope_v071_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d126d_slope_v072_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d189d_slope_v073_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d252d_slope_v074_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d378d_slope_v075_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_10d504d_slope_v076_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d5d_slope_v077_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d10d_slope_v078_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d21d_slope_v079_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d42d_slope_v080_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d63d_slope_v081_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d126d_slope_v082_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d189d_slope_v083_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d252d_slope_v084_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d378d_slope_v085_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_10d504d_slope_v086_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d5d_slope_v087_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d10d_slope_v088_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d21d_slope_v089_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d42d_slope_v090_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d63d_slope_v091_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d126d_slope_v092_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d189d_slope_v093_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d252d_slope_v094_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d378d_slope_v095_signal,
    f36hol_f36_healthcare_operating_leverage_oplzw_10d504d_slope_v096_signal,
    f36hol_f36_healthcare_operating_leverage_oplabsxc_10d_slope_v097_signal,
    f36hol_f36_healthcare_operating_leverage_oplsqxc_10d_slope_v098_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d5d_slope_v099_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d10d_slope_v100_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d21d_slope_v101_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d42d_slope_v102_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d63d_slope_v103_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d126d_slope_v104_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d189d_slope_v105_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d252d_slope_v106_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d378d_slope_v107_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanxc_10d504d_slope_v108_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d5d_slope_v109_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d10d_slope_v110_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d21d_slope_v111_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d42d_slope_v112_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d63d_slope_v113_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d126d_slope_v114_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d189d_slope_v115_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d252d_slope_v116_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d378d_slope_v117_signal,
    f36hol_f36_healthcare_operating_leverage_oplemaxc_10d504d_slope_v118_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d5d_slope_v119_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d10d_slope_v120_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d21d_slope_v121_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d42d_slope_v122_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d63d_slope_v123_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d126d_slope_v124_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d189d_slope_v125_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d252d_slope_v126_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d378d_slope_v127_signal,
    f36hol_f36_healthcare_operating_leverage_oplcumsumxc_10d504d_slope_v128_signal,
    f36hol_f36_healthcare_operating_leverage_oplraw_21d_slope_v129_signal,
    f36hol_f36_healthcare_operating_leverage_oplxclose_21d_slope_v130_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d5d_slope_v131_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d10d_slope_v132_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d21d_slope_v133_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d42d_slope_v134_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d63d_slope_v135_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d126d_slope_v136_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d189d_slope_v137_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d252d_slope_v138_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d378d_slope_v139_signal,
    f36hol_f36_healthcare_operating_leverage_oplmeanw_21d504d_slope_v140_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d5d_slope_v141_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d10d_slope_v142_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d21d_slope_v143_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d42d_slope_v144_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d63d_slope_v145_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d126d_slope_v146_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d189d_slope_v147_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d252d_slope_v148_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d378d_slope_v149_signal,
    f36hol_f36_healthcare_operating_leverage_oplstdw_21d504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F36_HEALTHCARE_OPERATING_LEVERAGE_REGISTRY_SLOPE_001_150 = REGISTRY



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
    domain_primitives = ("_f36_op_leverage_proxy", "_f36_margin_revenue_beta", "_f36_drop_through")
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
    print(f"OK f36_healthcare_operating_leverage_2nd_derivatives_001_150_claude: {n_features} features pass")
