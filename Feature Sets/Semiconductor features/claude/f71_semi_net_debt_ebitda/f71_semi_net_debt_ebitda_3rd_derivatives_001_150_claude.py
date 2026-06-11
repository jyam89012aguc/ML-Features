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
def _f71_nd_ebitda(debt, cashneq, ebitda):
    return (debt - cashneq) / ebitda.replace(0, np.nan)


# 5d curv of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_curv_v001_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_curv_v002_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_curv_v003_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_curv_v004_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_21d_curv_v005_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_curv_v006_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_curv_v007_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_curv_v008_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_curv_v009_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_63d_curv_v010_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_curv_v011_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_curv_v012_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_curv_v013_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_curv_v014_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_126d_curv_v015_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_curv_v016_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_curv_v017_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_curv_v018_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_curv_v019_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_252d_curv_v020_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_curv_v021_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_curv_v022_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_curv_v023_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_curv_v024_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d nde level
def f71nd_f71_semi_net_debt_ebitda_nde_level_504d_curv_v025_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_curv_v026_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_curv_v027_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_curv_v028_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_curv_v029_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_21d_curv_v030_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_curv_v031_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_curv_v032_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_curv_v033_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_curv_v034_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_63d_curv_v035_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_curv_v036_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_curv_v037_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_curv_v038_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_curv_v039_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_126d_curv_v040_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_curv_v041_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_curv_v042_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_curv_v043_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_curv_v044_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_252d_curv_v045_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_curv_v046_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_curv_v047_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_curv_v048_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_curv_v049_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d nde z
def f71nd_f71_semi_net_debt_ebitda_nde_z_504d_curv_v050_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_curv_v051_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_curv_v052_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_curv_v053_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_curv_v054_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_21d_curv_v055_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_curv_v056_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_curv_v057_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_curv_v058_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_curv_v059_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_63d_curv_v060_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_curv_v061_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_curv_v062_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_curv_v063_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_curv_v064_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_126d_curv_v065_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_curv_v066_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_curv_v067_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_curv_v068_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_curv_v069_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_252d_curv_v070_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_curv_v071_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_curv_v072_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_curv_v073_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_curv_v074_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d nde max
def f71nd_f71_semi_net_debt_ebitda_nde_max_504d_curv_v075_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_curv_v076_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_curv_v077_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_curv_v078_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_curv_v079_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_21d_curv_v080_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_curv_v081_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_curv_v082_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_curv_v083_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_curv_v084_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_63d_curv_v085_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_curv_v086_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_curv_v087_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_curv_v088_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_curv_v089_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_126d_curv_v090_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_curv_v091_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_curv_v092_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_curv_v093_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_curv_v094_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_252d_curv_v095_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_curv_v096_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_curv_v097_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_curv_v098_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_curv_v099_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d nde min
def f71nd_f71_semi_net_debt_ebitda_nde_min_504d_curv_v100_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_curv_v101_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_curv_v102_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_curv_v103_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_curv_v104_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_21d_curv_v105_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_curv_v106_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_curv_v107_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_curv_v108_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_curv_v109_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_63d_curv_v110_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_curv_v111_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_curv_v112_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_curv_v113_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_curv_v114_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_126d_curv_v115_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_curv_v116_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_curv_v117_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_curv_v118_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_curv_v119_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_252d_curv_v120_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_curv_v121_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_curv_v122_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_curv_v123_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_curv_v124_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d nde rng
def f71nd_f71_semi_net_debt_ebitda_nde_rng_504d_curv_v125_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_curv_v126_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_curv_v127_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_curv_v128_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_curv_v129_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_21d_curv_v130_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_curv_v131_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_curv_v132_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_curv_v133_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_curv_v134_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_63d_curv_v135_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_curv_v136_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_curv_v137_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_curv_v138_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_curv_v139_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_126d_curv_v140_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_curv_v141_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_curv_v142_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_curv_v143_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_curv_v144_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_252d_curv_v145_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_curv_v146_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_curv_v147_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_curv_v148_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_curv_v149_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d nde dd
def f71nd_f71_semi_net_debt_ebitda_nde_dd_504d_curv_v150_signal(debt, cashneq, ebitda, closeadj):
    r = _f71_nd_ebitda(debt, cashneq, ebitda)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
