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
def _f71_nd_ebitda(debt, cashneq, ebitda):
    return (debt - cashneq) / ebitda.replace(0, np.nan)


# 5d slope of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_slope_v001_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_slope_v002_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_slope_v003_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_slope_v004_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_slope_v005_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_slope_v006_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_slope_v007_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_slope_v008_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_slope_v009_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_slope_v010_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_slope_v011_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_slope_v012_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_slope_v013_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_slope_v014_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_slope_v015_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_slope_v016_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_slope_v017_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_slope_v018_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_slope_v019_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_slope_v020_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_slope_v021_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_slope_v022_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_slope_v023_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_slope_v024_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_slope_v025_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_slope_v026_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_slope_v027_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_slope_v028_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_slope_v029_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_slope_v030_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_slope_v031_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_slope_v032_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_slope_v033_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_slope_v034_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_slope_v035_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_slope_v036_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_slope_v037_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_slope_v038_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_slope_v039_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_slope_v040_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_slope_v041_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_slope_v042_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_slope_v043_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_slope_v044_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_slope_v045_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_slope_v046_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_slope_v047_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_slope_v048_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_slope_v049_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_slope_v050_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_slope_v051_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_slope_v052_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_slope_v053_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_slope_v054_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_slope_v055_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_slope_v056_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_slope_v057_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_slope_v058_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_slope_v059_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_slope_v060_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_slope_v061_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_slope_v062_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_slope_v063_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_slope_v064_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_slope_v065_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_slope_v066_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_slope_v067_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_slope_v068_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_slope_v069_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_slope_v070_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_slope_v071_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_slope_v072_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_slope_v073_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_slope_v074_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_slope_v075_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_slope_v076_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_slope_v077_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_slope_v078_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_slope_v079_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_slope_v080_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_slope_v081_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_slope_v082_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_slope_v083_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_slope_v084_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_slope_v085_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_slope_v086_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_slope_v087_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_slope_v088_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_slope_v089_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_slope_v090_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_slope_v091_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_slope_v092_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_slope_v093_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_slope_v094_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_slope_v095_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_slope_v096_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_slope_v097_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_slope_v098_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_slope_v099_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_slope_v100_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_slope_v101_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_slope_v102_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_slope_v103_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_slope_v104_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_slope_v105_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_slope_v106_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_slope_v107_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_slope_v108_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_slope_v109_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_slope_v110_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_slope_v111_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_slope_v112_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_slope_v113_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_slope_v114_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_slope_v115_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_slope_v116_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_slope_v117_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_slope_v118_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_slope_v119_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_slope_v120_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_slope_v121_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_slope_v122_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_slope_v123_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_slope_v124_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_slope_v125_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_slope_v126_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_slope_v127_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_slope_v128_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_slope_v129_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_slope_v130_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_slope_v131_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_slope_v132_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_slope_v133_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_slope_v134_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_slope_v135_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_slope_v136_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_slope_v137_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_slope_v138_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_slope_v139_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_slope_v140_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_slope_v141_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_slope_v142_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_slope_v143_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_slope_v144_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_slope_v145_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_slope_v146_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_slope_v147_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_slope_v148_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_slope_v149_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_slope_v150_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
