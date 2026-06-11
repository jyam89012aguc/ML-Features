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

def _f40_margin_expansion(grossmargin, w):
    return grossmargin.diff(periods=w)


def _f40_margin_compound(ebitdamargin, w):
    avg = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return avg.diff(periods=w) * avg


def _f40_expansion_quality(grossmargin, ebitdamargin, w):
    dg = grossmargin.diff(periods=w)
    de = ebitdamargin.diff(periods=w)
    return dg * de




def f40hme_f40_healthcare_margin_expansion_expraw_5d_slope_v001_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expxclose_5d_slope_v002_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d5d_slope_v003_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d10d_slope_v004_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d21d_slope_v005_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d42d_slope_v006_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d63d_slope_v007_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d126d_slope_v008_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d189d_slope_v009_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d252d_slope_v010_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d378d_slope_v011_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_5d504d_slope_v012_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d5d_slope_v013_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d10d_slope_v014_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d21d_slope_v015_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d42d_slope_v016_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d63d_slope_v017_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d126d_slope_v018_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d189d_slope_v019_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d252d_slope_v020_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d378d_slope_v021_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_5d504d_slope_v022_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d5d_slope_v023_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d10d_slope_v024_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d21d_slope_v025_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d42d_slope_v026_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d63d_slope_v027_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d126d_slope_v028_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d189d_slope_v029_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d252d_slope_v030_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d378d_slope_v031_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_5d504d_slope_v032_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _z(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expabsxc_5d_slope_v033_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expsqxc_5d_slope_v034_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner) * (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d5d_slope_v035_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d10d_slope_v036_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d21d_slope_v037_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d42d_slope_v038_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d63d_slope_v039_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d126d_slope_v040_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d189d_slope_v041_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d252d_slope_v042_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d378d_slope_v043_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_5d504d_slope_v044_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = _mean(inner, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d5d_slope_v045_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d10d_slope_v046_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d21d_slope_v047_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d42d_slope_v048_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d63d_slope_v049_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d126d_slope_v050_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d189d_slope_v051_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d252d_slope_v052_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d378d_slope_v053_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_5d504d_slope_v054_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d5d_slope_v055_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d10d_slope_v056_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d21d_slope_v057_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d42d_slope_v058_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d63d_slope_v059_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d126d_slope_v060_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d189d_slope_v061_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d252d_slope_v062_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d378d_slope_v063_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d504d_slope_v064_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 5)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expraw_10d_slope_v065_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expxclose_10d_slope_v066_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d5d_slope_v067_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d10d_slope_v068_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d21d_slope_v069_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d42d_slope_v070_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d63d_slope_v071_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d126d_slope_v072_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d189d_slope_v073_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d252d_slope_v074_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d378d_slope_v075_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_10d504d_slope_v076_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d5d_slope_v077_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d10d_slope_v078_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d21d_slope_v079_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d42d_slope_v080_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d63d_slope_v081_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d126d_slope_v082_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d189d_slope_v083_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d252d_slope_v084_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d378d_slope_v085_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_10d504d_slope_v086_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d5d_slope_v087_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d10d_slope_v088_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d21d_slope_v089_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d42d_slope_v090_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d63d_slope_v091_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d126d_slope_v092_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d189d_slope_v093_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d252d_slope_v094_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d378d_slope_v095_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expzw_10d504d_slope_v096_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _z(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expabsxc_10d_slope_v097_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expsqxc_10d_slope_v098_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner) * (inner).abs() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d5d_slope_v099_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d10d_slope_v100_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d21d_slope_v101_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d42d_slope_v102_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d63d_slope_v103_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d126d_slope_v104_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d189d_slope_v105_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d252d_slope_v106_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d378d_slope_v107_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanxc_10d504d_slope_v108_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = _mean(inner, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d5d_slope_v109_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d10d_slope_v110_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d21d_slope_v111_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d42d_slope_v112_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d63d_slope_v113_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d126d_slope_v114_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d189d_slope_v115_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d252d_slope_v116_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d378d_slope_v117_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expemaxc_10d504d_slope_v118_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d5d_slope_v119_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d10d_slope_v120_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d21d_slope_v121_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d42d_slope_v122_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d63d_slope_v123_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d126d_slope_v124_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d189d_slope_v125_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d252d_slope_v126_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d378d_slope_v127_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d504d_slope_v128_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 10)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expraw_21d_slope_v129_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = (inner)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expxclose_21d_slope_v130_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = (inner) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d5d_slope_v131_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d10d_slope_v132_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d21d_slope_v133_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d42d_slope_v134_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d63d_slope_v135_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d126d_slope_v136_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d189d_slope_v137_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d252d_slope_v138_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d378d_slope_v139_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expmeanw_21d504d_slope_v140_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _mean(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d5d_slope_v141_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 5)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d10d_slope_v142_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 10)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d21d_slope_v143_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d42d_slope_v144_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 42)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d63d_slope_v145_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d126d_slope_v146_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d189d_slope_v147_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 189)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d252d_slope_v148_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d378d_slope_v149_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 378)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f40hme_f40_healthcare_margin_expansion_expstdw_21d504d_slope_v150_signal(grossmargin, closeadj):
    inner = _f40_margin_expansion(grossmargin, 21)
    base = _std(inner, 504)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40hme_f40_healthcare_margin_expansion_expraw_5d_slope_v001_signal,
    f40hme_f40_healthcare_margin_expansion_expxclose_5d_slope_v002_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d5d_slope_v003_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d10d_slope_v004_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d21d_slope_v005_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d42d_slope_v006_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d63d_slope_v007_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d126d_slope_v008_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d189d_slope_v009_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d252d_slope_v010_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d378d_slope_v011_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_5d504d_slope_v012_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d5d_slope_v013_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d10d_slope_v014_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d21d_slope_v015_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d42d_slope_v016_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d63d_slope_v017_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d126d_slope_v018_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d189d_slope_v019_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d252d_slope_v020_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d378d_slope_v021_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_5d504d_slope_v022_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d5d_slope_v023_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d10d_slope_v024_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d21d_slope_v025_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d42d_slope_v026_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d63d_slope_v027_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d126d_slope_v028_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d189d_slope_v029_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d252d_slope_v030_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d378d_slope_v031_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_5d504d_slope_v032_signal,
    f40hme_f40_healthcare_margin_expansion_expabsxc_5d_slope_v033_signal,
    f40hme_f40_healthcare_margin_expansion_expsqxc_5d_slope_v034_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d5d_slope_v035_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d10d_slope_v036_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d21d_slope_v037_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d42d_slope_v038_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d63d_slope_v039_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d126d_slope_v040_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d189d_slope_v041_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d252d_slope_v042_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d378d_slope_v043_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_5d504d_slope_v044_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d5d_slope_v045_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d10d_slope_v046_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d21d_slope_v047_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d42d_slope_v048_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d63d_slope_v049_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d126d_slope_v050_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d189d_slope_v051_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d252d_slope_v052_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d378d_slope_v053_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_5d504d_slope_v054_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d5d_slope_v055_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d10d_slope_v056_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d21d_slope_v057_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d42d_slope_v058_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d63d_slope_v059_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d126d_slope_v060_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d189d_slope_v061_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d252d_slope_v062_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d378d_slope_v063_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_5d504d_slope_v064_signal,
    f40hme_f40_healthcare_margin_expansion_expraw_10d_slope_v065_signal,
    f40hme_f40_healthcare_margin_expansion_expxclose_10d_slope_v066_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d5d_slope_v067_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d10d_slope_v068_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d21d_slope_v069_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d42d_slope_v070_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d63d_slope_v071_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d126d_slope_v072_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d189d_slope_v073_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d252d_slope_v074_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d378d_slope_v075_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_10d504d_slope_v076_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d5d_slope_v077_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d10d_slope_v078_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d21d_slope_v079_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d42d_slope_v080_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d63d_slope_v081_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d126d_slope_v082_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d189d_slope_v083_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d252d_slope_v084_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d378d_slope_v085_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_10d504d_slope_v086_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d5d_slope_v087_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d10d_slope_v088_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d21d_slope_v089_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d42d_slope_v090_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d63d_slope_v091_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d126d_slope_v092_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d189d_slope_v093_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d252d_slope_v094_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d378d_slope_v095_signal,
    f40hme_f40_healthcare_margin_expansion_expzw_10d504d_slope_v096_signal,
    f40hme_f40_healthcare_margin_expansion_expabsxc_10d_slope_v097_signal,
    f40hme_f40_healthcare_margin_expansion_expsqxc_10d_slope_v098_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d5d_slope_v099_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d10d_slope_v100_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d21d_slope_v101_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d42d_slope_v102_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d63d_slope_v103_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d126d_slope_v104_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d189d_slope_v105_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d252d_slope_v106_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d378d_slope_v107_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanxc_10d504d_slope_v108_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d5d_slope_v109_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d10d_slope_v110_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d21d_slope_v111_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d42d_slope_v112_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d63d_slope_v113_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d126d_slope_v114_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d189d_slope_v115_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d252d_slope_v116_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d378d_slope_v117_signal,
    f40hme_f40_healthcare_margin_expansion_expemaxc_10d504d_slope_v118_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d5d_slope_v119_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d10d_slope_v120_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d21d_slope_v121_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d42d_slope_v122_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d63d_slope_v123_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d126d_slope_v124_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d189d_slope_v125_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d252d_slope_v126_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d378d_slope_v127_signal,
    f40hme_f40_healthcare_margin_expansion_expcumsumxc_10d504d_slope_v128_signal,
    f40hme_f40_healthcare_margin_expansion_expraw_21d_slope_v129_signal,
    f40hme_f40_healthcare_margin_expansion_expxclose_21d_slope_v130_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d5d_slope_v131_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d10d_slope_v132_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d21d_slope_v133_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d42d_slope_v134_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d63d_slope_v135_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d126d_slope_v136_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d189d_slope_v137_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d252d_slope_v138_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d378d_slope_v139_signal,
    f40hme_f40_healthcare_margin_expansion_expmeanw_21d504d_slope_v140_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d5d_slope_v141_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d10d_slope_v142_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d21d_slope_v143_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d42d_slope_v144_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d63d_slope_v145_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d126d_slope_v146_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d189d_slope_v147_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d252d_slope_v148_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d378d_slope_v149_signal,
    f40hme_f40_healthcare_margin_expansion_expstdw_21d504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F40_HEALTHCARE_MARGIN_EXPANSION_REGISTRY_SLOPE_001_150 = REGISTRY



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
    domain_primitives = ("_f40_margin_expansion", "_f40_margin_compound", "_f40_expansion_quality")
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
    print(f"OK f40_healthcare_margin_expansion_2nd_derivatives_001_150_claude: {n_features} features pass")
