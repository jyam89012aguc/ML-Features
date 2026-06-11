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

def _f37_gm_floor(grossmargin, w):
    floor = grossmargin.rolling(w, min_periods=max(1, w // 2)).min()
    return (grossmargin - floor)


def _f37_gm_consistency(grossmargin, w):
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    m = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean().abs()
    return 1.0 / (sd / m.replace(0, np.nan)).replace(0, np.nan)


def _f37_gm_quality_score(grossmargin, ebitdamargin, w):
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (gm * em) / sd.replace(0, np.nan)




def f37hgm_f37_healthcare_gross_margin_quality_flrraw_5d_jerk_v001_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrxclose_5d_jerk_v002_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d5d_jerk_v003_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d10d_jerk_v004_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d21d_jerk_v005_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d42d_jerk_v006_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d63d_jerk_v007_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d126d_jerk_v008_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d189d_jerk_v009_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d252d_jerk_v010_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d378d_jerk_v011_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d504d_jerk_v012_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d5d_jerk_v013_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d10d_jerk_v014_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d21d_jerk_v015_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d42d_jerk_v016_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d63d_jerk_v017_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d126d_jerk_v018_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d189d_jerk_v019_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d252d_jerk_v020_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d378d_jerk_v021_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d504d_jerk_v022_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _std(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d5d_jerk_v023_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d10d_jerk_v024_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d21d_jerk_v025_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d42d_jerk_v026_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d63d_jerk_v027_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d126d_jerk_v028_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d189d_jerk_v029_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d252d_jerk_v030_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d378d_jerk_v031_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d504d_jerk_v032_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _z(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrabsxc_5d_jerk_v033_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrsqxc_5d_jerk_v034_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner) * (inner).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d5d_jerk_v035_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d10d_jerk_v036_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d21d_jerk_v037_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d42d_jerk_v038_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d63d_jerk_v039_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d126d_jerk_v040_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d189d_jerk_v041_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d252d_jerk_v042_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d378d_jerk_v043_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d504d_jerk_v044_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = _mean(inner, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d5d_jerk_v045_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d10d_jerk_v046_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d21d_jerk_v047_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d42d_jerk_v048_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d63d_jerk_v049_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d126d_jerk_v050_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d189d_jerk_v051_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d252d_jerk_v052_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d378d_jerk_v053_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d504d_jerk_v054_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d5d_jerk_v055_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d10d_jerk_v056_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d21d_jerk_v057_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d42d_jerk_v058_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d63d_jerk_v059_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d126d_jerk_v060_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d189d_jerk_v061_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d252d_jerk_v062_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d378d_jerk_v063_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d504d_jerk_v064_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 5)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrraw_10d_jerk_v065_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrxclose_10d_jerk_v066_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d5d_jerk_v067_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d10d_jerk_v068_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d21d_jerk_v069_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d42d_jerk_v070_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d63d_jerk_v071_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d126d_jerk_v072_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d189d_jerk_v073_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d252d_jerk_v074_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d378d_jerk_v075_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d504d_jerk_v076_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d5d_jerk_v077_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d10d_jerk_v078_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d21d_jerk_v079_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d42d_jerk_v080_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d63d_jerk_v081_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d126d_jerk_v082_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d189d_jerk_v083_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d252d_jerk_v084_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d378d_jerk_v085_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d504d_jerk_v086_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _std(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d5d_jerk_v087_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d10d_jerk_v088_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d21d_jerk_v089_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d42d_jerk_v090_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d63d_jerk_v091_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d126d_jerk_v092_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d189d_jerk_v093_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d252d_jerk_v094_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d378d_jerk_v095_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d504d_jerk_v096_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _z(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrabsxc_10d_jerk_v097_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrsqxc_10d_jerk_v098_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner) * (inner).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d5d_jerk_v099_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d10d_jerk_v100_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d21d_jerk_v101_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d42d_jerk_v102_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d63d_jerk_v103_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d126d_jerk_v104_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d189d_jerk_v105_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d252d_jerk_v106_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d378d_jerk_v107_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d504d_jerk_v108_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = _mean(inner, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d5d_jerk_v109_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d10d_jerk_v110_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d21d_jerk_v111_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d42d_jerk_v112_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d63d_jerk_v113_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d126d_jerk_v114_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d189d_jerk_v115_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=189, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d252d_jerk_v116_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d378d_jerk_v117_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=378, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d504d_jerk_v118_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).ewm(span=504, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d5d_jerk_v119_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(5, min_periods=max(1,5//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d10d_jerk_v120_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(10, min_periods=max(1,10//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d21d_jerk_v121_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(21, min_periods=max(1,21//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d42d_jerk_v122_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(42, min_periods=max(1,42//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d63d_jerk_v123_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(63, min_periods=max(1,63//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d126d_jerk_v124_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(126, min_periods=max(1,126//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d189d_jerk_v125_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(189, min_periods=max(1,189//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d252d_jerk_v126_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(252, min_periods=max(1,252//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d378d_jerk_v127_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(378, min_periods=max(1,378//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d504d_jerk_v128_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 10)
    base = (inner).rolling(504, min_periods=max(1,504//2)).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrraw_21d_jerk_v129_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = (inner)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrxclose_21d_jerk_v130_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = (inner) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d5d_jerk_v131_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d10d_jerk_v132_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d21d_jerk_v133_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d42d_jerk_v134_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d63d_jerk_v135_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d126d_jerk_v136_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d189d_jerk_v137_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d252d_jerk_v138_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d378d_jerk_v139_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d504d_jerk_v140_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _mean(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d5d_jerk_v141_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 5)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d10d_jerk_v142_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 10)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d21d_jerk_v143_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d42d_jerk_v144_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d63d_jerk_v145_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d126d_jerk_v146_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d189d_jerk_v147_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 189)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d252d_jerk_v148_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d378d_jerk_v149_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 378)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d504d_jerk_v150_signal(grossmargin, closeadj):
    inner = _f37_gm_floor(grossmargin, 21)
    base = _std(inner, 504)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hgm_f37_healthcare_gross_margin_quality_flrraw_5d_jerk_v001_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrxclose_5d_jerk_v002_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d5d_jerk_v003_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d10d_jerk_v004_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d21d_jerk_v005_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d42d_jerk_v006_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d63d_jerk_v007_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d126d_jerk_v008_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d189d_jerk_v009_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d252d_jerk_v010_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d378d_jerk_v011_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_5d504d_jerk_v012_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d5d_jerk_v013_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d10d_jerk_v014_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d21d_jerk_v015_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d42d_jerk_v016_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d63d_jerk_v017_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d126d_jerk_v018_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d189d_jerk_v019_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d252d_jerk_v020_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d378d_jerk_v021_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_5d504d_jerk_v022_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d5d_jerk_v023_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d10d_jerk_v024_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d21d_jerk_v025_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d42d_jerk_v026_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d63d_jerk_v027_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d126d_jerk_v028_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d189d_jerk_v029_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d252d_jerk_v030_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d378d_jerk_v031_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_5d504d_jerk_v032_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrabsxc_5d_jerk_v033_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrsqxc_5d_jerk_v034_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d5d_jerk_v035_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d10d_jerk_v036_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d21d_jerk_v037_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d42d_jerk_v038_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d63d_jerk_v039_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d126d_jerk_v040_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d189d_jerk_v041_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d252d_jerk_v042_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d378d_jerk_v043_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_5d504d_jerk_v044_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d5d_jerk_v045_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d10d_jerk_v046_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d21d_jerk_v047_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d42d_jerk_v048_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d63d_jerk_v049_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d126d_jerk_v050_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d189d_jerk_v051_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d252d_jerk_v052_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d378d_jerk_v053_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_5d504d_jerk_v054_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d5d_jerk_v055_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d10d_jerk_v056_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d21d_jerk_v057_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d42d_jerk_v058_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d63d_jerk_v059_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d126d_jerk_v060_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d189d_jerk_v061_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d252d_jerk_v062_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d378d_jerk_v063_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_5d504d_jerk_v064_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrraw_10d_jerk_v065_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrxclose_10d_jerk_v066_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d5d_jerk_v067_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d10d_jerk_v068_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d21d_jerk_v069_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d42d_jerk_v070_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d63d_jerk_v071_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d126d_jerk_v072_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d189d_jerk_v073_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d252d_jerk_v074_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d378d_jerk_v075_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_10d504d_jerk_v076_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d5d_jerk_v077_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d10d_jerk_v078_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d21d_jerk_v079_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d42d_jerk_v080_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d63d_jerk_v081_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d126d_jerk_v082_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d189d_jerk_v083_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d252d_jerk_v084_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d378d_jerk_v085_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_10d504d_jerk_v086_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d5d_jerk_v087_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d10d_jerk_v088_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d21d_jerk_v089_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d42d_jerk_v090_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d63d_jerk_v091_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d126d_jerk_v092_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d189d_jerk_v093_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d252d_jerk_v094_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d378d_jerk_v095_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrzw_10d504d_jerk_v096_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrabsxc_10d_jerk_v097_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrsqxc_10d_jerk_v098_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d5d_jerk_v099_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d10d_jerk_v100_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d21d_jerk_v101_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d42d_jerk_v102_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d63d_jerk_v103_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d126d_jerk_v104_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d189d_jerk_v105_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d252d_jerk_v106_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d378d_jerk_v107_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanxc_10d504d_jerk_v108_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d5d_jerk_v109_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d10d_jerk_v110_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d21d_jerk_v111_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d42d_jerk_v112_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d63d_jerk_v113_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d126d_jerk_v114_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d189d_jerk_v115_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d252d_jerk_v116_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d378d_jerk_v117_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flremaxc_10d504d_jerk_v118_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d5d_jerk_v119_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d10d_jerk_v120_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d21d_jerk_v121_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d42d_jerk_v122_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d63d_jerk_v123_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d126d_jerk_v124_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d189d_jerk_v125_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d252d_jerk_v126_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d378d_jerk_v127_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrcumsumxc_10d504d_jerk_v128_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrraw_21d_jerk_v129_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrxclose_21d_jerk_v130_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d5d_jerk_v131_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d10d_jerk_v132_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d21d_jerk_v133_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d42d_jerk_v134_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d63d_jerk_v135_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d126d_jerk_v136_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d189d_jerk_v137_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d252d_jerk_v138_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d378d_jerk_v139_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrmeanw_21d504d_jerk_v140_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d5d_jerk_v141_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d10d_jerk_v142_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d21d_jerk_v143_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d42d_jerk_v144_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d63d_jerk_v145_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d126d_jerk_v146_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d189d_jerk_v147_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d252d_jerk_v148_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d378d_jerk_v149_signal,
    f37hgm_f37_healthcare_gross_margin_quality_flrstdw_21d504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}

F37_HEALTHCARE_GROSS_MARGIN_QUALITY_REGISTRY_JERK_001_150 = REGISTRY



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
    domain_primitives = ("_f37_gm_floor", "_f37_gm_consistency", "_f37_gm_quality_score")
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
    print(f"OK f37_healthcare_gross_margin_quality_3rd_derivatives_001_150_claude: {n_features} features pass")
