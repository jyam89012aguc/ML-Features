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
def _f74_int_eq(intangibles, equity):
    return intangibles / equity.replace(0, np.nan)


# 5d curv of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_curv_v001_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_curv_v002_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_curv_v003_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_curv_v004_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_curv_v005_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_curv_v006_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_curv_v007_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_curv_v008_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_curv_v009_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_curv_v010_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_curv_v011_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_curv_v012_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_curv_v013_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_curv_v014_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_curv_v015_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_curv_v016_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_curv_v017_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_curv_v018_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_curv_v019_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_curv_v020_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_curv_v021_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_curv_v022_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_curv_v023_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_curv_v024_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_curv_v025_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_curv_v026_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_curv_v027_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_curv_v028_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_curv_v029_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_curv_v030_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_curv_v031_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_curv_v032_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_curv_v033_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_curv_v034_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_curv_v035_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_curv_v036_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_curv_v037_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_curv_v038_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_curv_v039_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_curv_v040_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_curv_v041_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_curv_v042_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_curv_v043_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_curv_v044_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_curv_v045_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_curv_v046_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_curv_v047_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_curv_v048_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_curv_v049_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_curv_v050_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_curv_v051_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_curv_v052_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_curv_v053_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_curv_v054_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_curv_v055_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_curv_v056_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_curv_v057_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_curv_v058_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_curv_v059_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_curv_v060_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_curv_v061_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_curv_v062_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_curv_v063_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_curv_v064_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_curv_v065_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_curv_v066_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_curv_v067_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_curv_v068_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_curv_v069_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_curv_v070_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_curv_v071_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_curv_v072_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_curv_v073_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_curv_v074_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_curv_v075_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_curv_v076_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_curv_v077_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_curv_v078_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_curv_v079_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_curv_v080_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_curv_v081_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_curv_v082_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_curv_v083_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_curv_v084_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_curv_v085_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_curv_v086_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_curv_v087_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_curv_v088_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_curv_v089_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_curv_v090_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_curv_v091_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_curv_v092_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_curv_v093_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_curv_v094_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_curv_v095_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_curv_v096_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_curv_v097_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_curv_v098_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_curv_v099_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_curv_v100_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_curv_v101_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_curv_v102_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_curv_v103_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_curv_v104_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_curv_v105_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_curv_v106_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_curv_v107_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_curv_v108_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_curv_v109_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_curv_v110_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_curv_v111_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_curv_v112_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_curv_v113_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_curv_v114_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_curv_v115_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_curv_v116_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_curv_v117_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_curv_v118_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_curv_v119_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_curv_v120_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_curv_v121_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_curv_v122_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_curv_v123_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_curv_v124_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_curv_v125_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_curv_v126_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_curv_v127_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_curv_v128_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_curv_v129_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_curv_v130_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_curv_v131_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_curv_v132_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_curv_v133_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_curv_v134_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_curv_v135_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_curv_v136_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_curv_v137_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_curv_v138_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_curv_v139_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_curv_v140_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_curv_v141_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_curv_v142_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_curv_v143_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_curv_v144_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_curv_v145_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_curv_v146_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_curv_v147_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_curv_v148_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_curv_v149_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_curv_v150_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
