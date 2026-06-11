import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f83_pfcf(pfcf):
    return pfcf


# 5d slope of 21d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_21d_slope_v001_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_21d_slope_v002_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_21d_slope_v003_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_21d_slope_v004_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_21d_slope_v005_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_63d_slope_v006_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_63d_slope_v007_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_63d_slope_v008_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_63d_slope_v009_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_63d_slope_v010_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_126d_slope_v011_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_126d_slope_v012_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_126d_slope_v013_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_126d_slope_v014_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_126d_slope_v015_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_252d_slope_v016_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_252d_slope_v017_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_252d_slope_v018_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_252d_slope_v019_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_252d_slope_v020_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_504d_slope_v021_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_504d_slope_v022_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_504d_slope_v023_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_504d_slope_v024_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d pfc level
def f83pfc_f83_semi_pfcf_cohort_pfc_level_504d_slope_v025_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_21d_slope_v026_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_21d_slope_v027_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_21d_slope_v028_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_21d_slope_v029_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_21d_slope_v030_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_63d_slope_v031_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_63d_slope_v032_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_63d_slope_v033_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_63d_slope_v034_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_63d_slope_v035_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_126d_slope_v036_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_126d_slope_v037_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_126d_slope_v038_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_126d_slope_v039_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_126d_slope_v040_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_252d_slope_v041_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_252d_slope_v042_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_252d_slope_v043_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_252d_slope_v044_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_252d_slope_v045_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_504d_slope_v046_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_504d_slope_v047_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_504d_slope_v048_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_504d_slope_v049_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d pfc z
def f83pfc_f83_semi_pfcf_cohort_pfc_z_504d_slope_v050_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_21d_slope_v051_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_21d_slope_v052_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_21d_slope_v053_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_21d_slope_v054_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_21d_slope_v055_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_63d_slope_v056_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_63d_slope_v057_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_63d_slope_v058_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_63d_slope_v059_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_63d_slope_v060_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_126d_slope_v061_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_126d_slope_v062_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_126d_slope_v063_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_126d_slope_v064_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_126d_slope_v065_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_252d_slope_v066_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_252d_slope_v067_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_252d_slope_v068_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_252d_slope_v069_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_252d_slope_v070_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_504d_slope_v071_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_504d_slope_v072_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_504d_slope_v073_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_504d_slope_v074_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d pfc max
def f83pfc_f83_semi_pfcf_cohort_pfc_max_504d_slope_v075_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_21d_slope_v076_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_21d_slope_v077_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_21d_slope_v078_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_21d_slope_v079_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_21d_slope_v080_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_63d_slope_v081_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_63d_slope_v082_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_63d_slope_v083_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_63d_slope_v084_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_63d_slope_v085_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_126d_slope_v086_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_126d_slope_v087_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_126d_slope_v088_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_126d_slope_v089_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_126d_slope_v090_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_252d_slope_v091_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_252d_slope_v092_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_252d_slope_v093_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_252d_slope_v094_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_252d_slope_v095_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_504d_slope_v096_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_504d_slope_v097_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_504d_slope_v098_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_504d_slope_v099_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d pfc min
def f83pfc_f83_semi_pfcf_cohort_pfc_min_504d_slope_v100_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_21d_slope_v101_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_21d_slope_v102_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_21d_slope_v103_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_21d_slope_v104_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_21d_slope_v105_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_63d_slope_v106_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_63d_slope_v107_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_63d_slope_v108_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_63d_slope_v109_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_63d_slope_v110_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_126d_slope_v111_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_126d_slope_v112_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_126d_slope_v113_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_126d_slope_v114_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_126d_slope_v115_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_252d_slope_v116_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_252d_slope_v117_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_252d_slope_v118_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_252d_slope_v119_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_252d_slope_v120_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_504d_slope_v121_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_504d_slope_v122_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_504d_slope_v123_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_504d_slope_v124_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d pfc rng
def f83pfc_f83_semi_pfcf_cohort_pfc_rng_504d_slope_v125_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_21d_slope_v126_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_21d_slope_v127_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_21d_slope_v128_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_21d_slope_v129_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_21d_slope_v130_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_63d_slope_v131_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_63d_slope_v132_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_63d_slope_v133_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_63d_slope_v134_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_63d_slope_v135_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_126d_slope_v136_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_126d_slope_v137_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_126d_slope_v138_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_126d_slope_v139_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_126d_slope_v140_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_252d_slope_v141_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_252d_slope_v142_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_252d_slope_v143_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_252d_slope_v144_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_252d_slope_v145_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_504d_slope_v146_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_504d_slope_v147_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_504d_slope_v148_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_504d_slope_v149_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d pfc dd
def f83pfc_f83_semi_pfcf_cohort_pfc_dd_504d_slope_v150_signal(pfcf, closeadj):
    r = _f83_pfcf(pfcf)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
