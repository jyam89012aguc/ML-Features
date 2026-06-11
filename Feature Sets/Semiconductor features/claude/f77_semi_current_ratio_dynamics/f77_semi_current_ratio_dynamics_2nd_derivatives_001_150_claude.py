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
def _f77_cr(assetsc, liabilitiesc):
    return assetsc / liabilitiesc.replace(0, np.nan)


# 5d slope of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_slope_v001_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_slope_v002_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_slope_v003_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_slope_v004_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_slope_v005_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_slope_v006_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_slope_v007_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_slope_v008_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_slope_v009_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_slope_v010_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_slope_v011_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_slope_v012_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_slope_v013_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_slope_v014_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_slope_v015_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_slope_v016_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_slope_v017_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_slope_v018_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_slope_v019_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_slope_v020_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_slope_v021_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_slope_v022_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_slope_v023_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_slope_v024_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_slope_v025_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_slope_v026_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_slope_v027_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_slope_v028_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_slope_v029_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_slope_v030_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_slope_v031_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_slope_v032_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_slope_v033_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_slope_v034_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_slope_v035_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_slope_v036_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_slope_v037_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_slope_v038_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_slope_v039_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_slope_v040_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_slope_v041_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_slope_v042_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_slope_v043_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_slope_v044_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_slope_v045_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_slope_v046_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_slope_v047_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_slope_v048_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_slope_v049_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_slope_v050_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_slope_v051_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_slope_v052_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_slope_v053_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_slope_v054_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_slope_v055_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_slope_v056_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_slope_v057_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_slope_v058_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_slope_v059_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_slope_v060_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_slope_v061_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_slope_v062_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_slope_v063_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_slope_v064_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_slope_v065_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_slope_v066_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_slope_v067_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_slope_v068_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_slope_v069_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_slope_v070_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_slope_v071_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_slope_v072_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_slope_v073_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_slope_v074_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_slope_v075_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_slope_v076_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_slope_v077_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_slope_v078_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_slope_v079_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_slope_v080_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_slope_v081_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_slope_v082_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_slope_v083_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_slope_v084_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_slope_v085_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_slope_v086_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_slope_v087_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_slope_v088_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_slope_v089_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_slope_v090_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_slope_v091_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_slope_v092_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_slope_v093_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_slope_v094_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_slope_v095_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_slope_v096_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_slope_v097_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_slope_v098_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_slope_v099_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_slope_v100_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_slope_v101_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_slope_v102_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_slope_v103_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_slope_v104_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_slope_v105_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_slope_v106_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_slope_v107_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_slope_v108_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_slope_v109_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_slope_v110_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_slope_v111_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_slope_v112_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_slope_v113_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_slope_v114_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_slope_v115_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_slope_v116_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_slope_v117_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_slope_v118_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_slope_v119_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_slope_v120_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_slope_v121_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_slope_v122_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_slope_v123_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_slope_v124_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_slope_v125_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_slope_v126_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_slope_v127_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_slope_v128_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_slope_v129_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_slope_v130_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_slope_v131_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_slope_v132_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_slope_v133_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_slope_v134_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_slope_v135_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_slope_v136_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_slope_v137_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_slope_v138_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_slope_v139_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_slope_v140_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_slope_v141_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_slope_v142_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_slope_v143_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_slope_v144_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_slope_v145_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_slope_v146_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_slope_v147_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_slope_v148_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_slope_v149_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_slope_v150_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
