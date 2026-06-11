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
def _f74_int_eq(intangibles, equity):
    return intangibles / equity.replace(0, np.nan)


# 5d slope of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_slope_v001_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_slope_v002_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_slope_v003_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_slope_v004_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_21d_slope_v005_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_slope_v006_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_slope_v007_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_slope_v008_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_slope_v009_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_63d_slope_v010_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_slope_v011_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_slope_v012_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_slope_v013_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_slope_v014_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_126d_slope_v015_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_slope_v016_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_slope_v017_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_slope_v018_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_slope_v019_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_252d_slope_v020_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_slope_v021_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_slope_v022_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_slope_v023_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_slope_v024_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d intq level
def f74ie_f74_semi_intangibles_to_equity_intq_level_504d_slope_v025_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_slope_v026_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_slope_v027_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_slope_v028_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_slope_v029_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_21d_slope_v030_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_slope_v031_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_slope_v032_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_slope_v033_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_slope_v034_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_63d_slope_v035_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_slope_v036_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_slope_v037_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_slope_v038_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_slope_v039_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_126d_slope_v040_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_slope_v041_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_slope_v042_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_slope_v043_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_slope_v044_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_252d_slope_v045_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_slope_v046_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_slope_v047_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_slope_v048_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_slope_v049_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d intq z
def f74ie_f74_semi_intangibles_to_equity_intq_z_504d_slope_v050_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_slope_v051_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_slope_v052_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_slope_v053_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_slope_v054_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_21d_slope_v055_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_slope_v056_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_slope_v057_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_slope_v058_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_slope_v059_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_63d_slope_v060_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_slope_v061_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_slope_v062_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_slope_v063_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_slope_v064_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_126d_slope_v065_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_slope_v066_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_slope_v067_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_slope_v068_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_slope_v069_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_252d_slope_v070_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_slope_v071_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_slope_v072_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_slope_v073_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_slope_v074_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d intq max
def f74ie_f74_semi_intangibles_to_equity_intq_max_504d_slope_v075_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_slope_v076_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_slope_v077_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_slope_v078_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_slope_v079_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_21d_slope_v080_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_slope_v081_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_slope_v082_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_slope_v083_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_slope_v084_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_63d_slope_v085_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_slope_v086_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_slope_v087_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_slope_v088_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_slope_v089_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_126d_slope_v090_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_slope_v091_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_slope_v092_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_slope_v093_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_slope_v094_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_252d_slope_v095_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_slope_v096_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_slope_v097_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_slope_v098_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_slope_v099_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d intq min
def f74ie_f74_semi_intangibles_to_equity_intq_min_504d_slope_v100_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_slope_v101_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_slope_v102_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_slope_v103_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_slope_v104_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_21d_slope_v105_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_slope_v106_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_slope_v107_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_slope_v108_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_slope_v109_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_63d_slope_v110_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_slope_v111_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_slope_v112_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_slope_v113_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_slope_v114_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_126d_slope_v115_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_slope_v116_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_slope_v117_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_slope_v118_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_slope_v119_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_252d_slope_v120_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_slope_v121_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_slope_v122_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_slope_v123_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_slope_v124_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d intq rng
def f74ie_f74_semi_intangibles_to_equity_intq_rng_504d_slope_v125_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_slope_v126_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_slope_v127_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_slope_v128_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_slope_v129_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_21d_slope_v130_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_slope_v131_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_slope_v132_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_slope_v133_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_slope_v134_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_63d_slope_v135_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_slope_v136_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_slope_v137_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_slope_v138_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_slope_v139_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_126d_slope_v140_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_slope_v141_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_slope_v142_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_slope_v143_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_slope_v144_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_252d_slope_v145_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_slope_v146_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_slope_v147_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_slope_v148_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_slope_v149_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d intq dd
def f74ie_f74_semi_intangibles_to_equity_intq_dd_504d_slope_v150_signal(intangibles, equity, closeadj):
    r = _f74_int_eq(intangibles, equity)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
