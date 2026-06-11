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


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


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


# 5d curv of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_curv_v001_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_curv_v002_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_curv_v003_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_curv_v004_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_21d_curv_v005_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_curv_v006_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_curv_v007_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_curv_v008_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_curv_v009_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_63d_curv_v010_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_curv_v011_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_curv_v012_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_curv_v013_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_curv_v014_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_126d_curv_v015_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_curv_v016_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_curv_v017_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_curv_v018_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_curv_v019_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_252d_curv_v020_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_curv_v021_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_curv_v022_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_curv_v023_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_curv_v024_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d curr level
def f77cr_f77_semi_current_ratio_dynamics_curr_level_504d_curv_v025_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_curv_v026_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_curv_v027_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_curv_v028_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_curv_v029_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_21d_curv_v030_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_curv_v031_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_curv_v032_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_curv_v033_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_curv_v034_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_63d_curv_v035_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_curv_v036_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_curv_v037_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_curv_v038_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_curv_v039_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_126d_curv_v040_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_curv_v041_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_curv_v042_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_curv_v043_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_curv_v044_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_252d_curv_v045_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_curv_v046_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_curv_v047_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_curv_v048_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_curv_v049_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d curr z
def f77cr_f77_semi_current_ratio_dynamics_curr_z_504d_curv_v050_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_curv_v051_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_curv_v052_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_curv_v053_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_curv_v054_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_21d_curv_v055_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_curv_v056_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_curv_v057_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_curv_v058_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_curv_v059_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_63d_curv_v060_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_curv_v061_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_curv_v062_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_curv_v063_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_curv_v064_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_126d_curv_v065_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_curv_v066_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_curv_v067_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_curv_v068_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_curv_v069_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_252d_curv_v070_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_curv_v071_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_curv_v072_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_curv_v073_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_curv_v074_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d curr max
def f77cr_f77_semi_current_ratio_dynamics_curr_max_504d_curv_v075_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_curv_v076_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_curv_v077_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_curv_v078_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_curv_v079_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_21d_curv_v080_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_curv_v081_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_curv_v082_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_curv_v083_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_curv_v084_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_63d_curv_v085_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_curv_v086_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_curv_v087_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_curv_v088_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_curv_v089_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_126d_curv_v090_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_curv_v091_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_curv_v092_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_curv_v093_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_curv_v094_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_252d_curv_v095_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_curv_v096_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_curv_v097_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_curv_v098_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_curv_v099_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d curr min
def f77cr_f77_semi_current_ratio_dynamics_curr_min_504d_curv_v100_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_curv_v101_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_curv_v102_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_curv_v103_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_curv_v104_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_21d_curv_v105_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_curv_v106_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_curv_v107_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_curv_v108_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_curv_v109_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_63d_curv_v110_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_curv_v111_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_curv_v112_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_curv_v113_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_curv_v114_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_126d_curv_v115_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_curv_v116_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_curv_v117_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_curv_v118_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_curv_v119_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_252d_curv_v120_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_curv_v121_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_curv_v122_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_curv_v123_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_curv_v124_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d curr rng
def f77cr_f77_semi_current_ratio_dynamics_curr_rng_504d_curv_v125_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_curv_v126_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_curv_v127_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_curv_v128_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_curv_v129_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_21d_curv_v130_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_curv_v131_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_curv_v132_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_curv_v133_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_curv_v134_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_63d_curv_v135_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_curv_v136_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_curv_v137_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_curv_v138_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_curv_v139_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_126d_curv_v140_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_curv_v141_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_curv_v142_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_curv_v143_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_curv_v144_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_252d_curv_v145_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_curv_v146_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_curv_v147_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_curv_v148_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_curv_v149_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d curr dd
def f77cr_f77_semi_current_ratio_dynamics_curr_dd_504d_curv_v150_signal(assetsc, liabilitiesc, closeadj):
    r = _f77_cr(assetsc, liabilitiesc)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
