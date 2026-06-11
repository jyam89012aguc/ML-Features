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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f02_own_ret(s):
    return s.pct_change()


def _f02_roll_beta(own_r, bas_r, w):
    cov = own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)
    var = bas_r.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)

# 5d curv of 21d rolling beta
def f02bb_f02_semi_basket_beta_beta_21d_curv_v001_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d rolling beta
def f02bb_f02_semi_basket_beta_beta_21d_curv_v002_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d rolling beta
def f02bb_f02_semi_basket_beta_beta_21d_curv_v003_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d rolling beta
def f02bb_f02_semi_basket_beta_beta_21d_curv_v004_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d rolling beta
def f02bb_f02_semi_basket_beta_beta_21d_curv_v005_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d rolling beta
def f02bb_f02_semi_basket_beta_beta_63d_curv_v006_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d rolling beta
def f02bb_f02_semi_basket_beta_beta_63d_curv_v007_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d rolling beta
def f02bb_f02_semi_basket_beta_beta_63d_curv_v008_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d rolling beta
def f02bb_f02_semi_basket_beta_beta_63d_curv_v009_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d rolling beta
def f02bb_f02_semi_basket_beta_beta_63d_curv_v010_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d rolling beta
def f02bb_f02_semi_basket_beta_beta_126d_curv_v011_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d rolling beta
def f02bb_f02_semi_basket_beta_beta_126d_curv_v012_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d rolling beta
def f02bb_f02_semi_basket_beta_beta_126d_curv_v013_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d rolling beta
def f02bb_f02_semi_basket_beta_beta_126d_curv_v014_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d rolling beta
def f02bb_f02_semi_basket_beta_beta_126d_curv_v015_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d rolling beta
def f02bb_f02_semi_basket_beta_beta_252d_curv_v016_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d rolling beta
def f02bb_f02_semi_basket_beta_beta_252d_curv_v017_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d rolling beta
def f02bb_f02_semi_basket_beta_beta_252d_curv_v018_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d rolling beta
def f02bb_f02_semi_basket_beta_beta_252d_curv_v019_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d rolling beta
def f02bb_f02_semi_basket_beta_beta_252d_curv_v020_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d rolling beta
def f02bb_f02_semi_basket_beta_beta_504d_curv_v021_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d rolling beta
def f02bb_f02_semi_basket_beta_beta_504d_curv_v022_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d rolling beta
def f02bb_f02_semi_basket_beta_beta_504d_curv_v023_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d rolling beta
def f02bb_f02_semi_basket_beta_beta_504d_curv_v024_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d rolling beta
def f02bb_f02_semi_basket_beta_beta_504d_curv_v025_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_21d_curv_v026_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21) - 1.0
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_21d_curv_v027_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21) - 1.0
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_21d_curv_v028_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21) - 1.0
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_21d_curv_v029_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21) - 1.0
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_21d_curv_v030_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 21) - 1.0
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_63d_curv_v031_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63) - 1.0
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_63d_curv_v032_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63) - 1.0
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_63d_curv_v033_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63) - 1.0
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_63d_curv_v034_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63) - 1.0
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_63d_curv_v035_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 63) - 1.0
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_126d_curv_v036_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126) - 1.0
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_126d_curv_v037_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126) - 1.0
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_126d_curv_v038_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126) - 1.0
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_126d_curv_v039_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126) - 1.0
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_126d_curv_v040_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 126) - 1.0
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_252d_curv_v041_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252) - 1.0
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_252d_curv_v042_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252) - 1.0
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_252d_curv_v043_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252) - 1.0
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_252d_curv_v044_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252) - 1.0
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_252d_curv_v045_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 252) - 1.0
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_504d_curv_v046_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504) - 1.0
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_504d_curv_v047_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504) - 1.0
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_504d_curv_v048_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504) - 1.0
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_504d_curv_v049_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504) - 1.0
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_504d_curv_v050_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    base = _f02_roll_beta(o, b, 504) - 1.0
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d beta z-score
def f02bb_f02_semi_basket_beta_betaz_21d_curv_v051_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = (beta - beta.rolling(63, min_periods=max(2, 63 // 2)).mean()) / beta.rolling(63, min_periods=max(2, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d beta z-score
def f02bb_f02_semi_basket_beta_betaz_21d_curv_v052_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = (beta - beta.rolling(63, min_periods=max(2, 63 // 2)).mean()) / beta.rolling(63, min_periods=max(2, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d beta z-score
def f02bb_f02_semi_basket_beta_betaz_21d_curv_v053_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = (beta - beta.rolling(63, min_periods=max(2, 63 // 2)).mean()) / beta.rolling(63, min_periods=max(2, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d beta z-score
def f02bb_f02_semi_basket_beta_betaz_21d_curv_v054_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = (beta - beta.rolling(63, min_periods=max(2, 63 // 2)).mean()) / beta.rolling(63, min_periods=max(2, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d beta z-score
def f02bb_f02_semi_basket_beta_betaz_21d_curv_v055_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = (beta - beta.rolling(63, min_periods=max(2, 63 // 2)).mean()) / beta.rolling(63, min_periods=max(2, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d beta z-score
def f02bb_f02_semi_basket_beta_betaz_63d_curv_v056_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = (beta - beta.rolling(126, min_periods=max(2, 126 // 2)).mean()) / beta.rolling(126, min_periods=max(2, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d beta z-score
def f02bb_f02_semi_basket_beta_betaz_63d_curv_v057_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = (beta - beta.rolling(126, min_periods=max(2, 126 // 2)).mean()) / beta.rolling(126, min_periods=max(2, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d beta z-score
def f02bb_f02_semi_basket_beta_betaz_63d_curv_v058_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = (beta - beta.rolling(126, min_periods=max(2, 126 // 2)).mean()) / beta.rolling(126, min_periods=max(2, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d beta z-score
def f02bb_f02_semi_basket_beta_betaz_63d_curv_v059_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = (beta - beta.rolling(126, min_periods=max(2, 126 // 2)).mean()) / beta.rolling(126, min_periods=max(2, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d beta z-score
def f02bb_f02_semi_basket_beta_betaz_63d_curv_v060_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = (beta - beta.rolling(126, min_periods=max(2, 126 // 2)).mean()) / beta.rolling(126, min_periods=max(2, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d beta z-score
def f02bb_f02_semi_basket_beta_betaz_126d_curv_v061_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = (beta - beta.rolling(252, min_periods=max(2, 252 // 2)).mean()) / beta.rolling(252, min_periods=max(2, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d beta z-score
def f02bb_f02_semi_basket_beta_betaz_126d_curv_v062_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = (beta - beta.rolling(252, min_periods=max(2, 252 // 2)).mean()) / beta.rolling(252, min_periods=max(2, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d beta z-score
def f02bb_f02_semi_basket_beta_betaz_126d_curv_v063_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = (beta - beta.rolling(252, min_periods=max(2, 252 // 2)).mean()) / beta.rolling(252, min_periods=max(2, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d beta z-score
def f02bb_f02_semi_basket_beta_betaz_126d_curv_v064_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = (beta - beta.rolling(252, min_periods=max(2, 252 // 2)).mean()) / beta.rolling(252, min_periods=max(2, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d beta z-score
def f02bb_f02_semi_basket_beta_betaz_126d_curv_v065_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = (beta - beta.rolling(252, min_periods=max(2, 252 // 2)).mean()) / beta.rolling(252, min_periods=max(2, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d beta z-score
def f02bb_f02_semi_basket_beta_betaz_252d_curv_v066_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = (beta - beta.rolling(504, min_periods=max(2, 504 // 2)).mean()) / beta.rolling(504, min_periods=max(2, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d beta z-score
def f02bb_f02_semi_basket_beta_betaz_252d_curv_v067_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = (beta - beta.rolling(504, min_periods=max(2, 504 // 2)).mean()) / beta.rolling(504, min_periods=max(2, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d beta z-score
def f02bb_f02_semi_basket_beta_betaz_252d_curv_v068_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = (beta - beta.rolling(504, min_periods=max(2, 504 // 2)).mean()) / beta.rolling(504, min_periods=max(2, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d beta z-score
def f02bb_f02_semi_basket_beta_betaz_252d_curv_v069_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = (beta - beta.rolling(504, min_periods=max(2, 504 // 2)).mean()) / beta.rolling(504, min_periods=max(2, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d beta z-score
def f02bb_f02_semi_basket_beta_betaz_252d_curv_v070_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = (beta - beta.rolling(504, min_periods=max(2, 504 // 2)).mean()) / beta.rolling(504, min_periods=max(2, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d beta z-score
def f02bb_f02_semi_basket_beta_betaz_504d_curv_v071_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = (beta - beta.rolling(756, min_periods=max(2, 756 // 2)).mean()) / beta.rolling(756, min_periods=max(2, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d beta z-score
def f02bb_f02_semi_basket_beta_betaz_504d_curv_v072_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = (beta - beta.rolling(756, min_periods=max(2, 756 // 2)).mean()) / beta.rolling(756, min_periods=max(2, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d beta z-score
def f02bb_f02_semi_basket_beta_betaz_504d_curv_v073_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = (beta - beta.rolling(756, min_periods=max(2, 756 // 2)).mean()) / beta.rolling(756, min_periods=max(2, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d beta z-score
def f02bb_f02_semi_basket_beta_betaz_504d_curv_v074_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = (beta - beta.rolling(756, min_periods=max(2, 756 // 2)).mean()) / beta.rolling(756, min_periods=max(2, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d beta z-score
def f02bb_f02_semi_basket_beta_betaz_504d_curv_v075_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = (beta - beta.rolling(756, min_periods=max(2, 756 // 2)).mean()) / beta.rolling(756, min_periods=max(2, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_21d_curv_v076_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _mean(beta, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_21d_curv_v077_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _mean(beta, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_21d_curv_v078_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _mean(beta, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_21d_curv_v079_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _mean(beta, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_21d_curv_v080_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _mean(beta, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_63d_curv_v081_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _mean(beta, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_63d_curv_v082_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _mean(beta, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_63d_curv_v083_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _mean(beta, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_63d_curv_v084_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _mean(beta, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_63d_curv_v085_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _mean(beta, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_126d_curv_v086_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _mean(beta, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_126d_curv_v087_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _mean(beta, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_126d_curv_v088_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _mean(beta, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_126d_curv_v089_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _mean(beta, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_126d_curv_v090_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _mean(beta, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_252d_curv_v091_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _mean(beta, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_252d_curv_v092_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _mean(beta, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_252d_curv_v093_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _mean(beta, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_252d_curv_v094_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _mean(beta, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_252d_curv_v095_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _mean(beta, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_504d_curv_v096_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _mean(beta, 756)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_504d_curv_v097_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _mean(beta, 756)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_504d_curv_v098_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _mean(beta, 756)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_504d_curv_v099_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _mean(beta, 756)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d beta deviation from longer mean
def f02bb_f02_semi_basket_beta_betadev_504d_curv_v100_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _mean(beta, 756)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_21d_curv_v101_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _max(beta, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_21d_curv_v102_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _max(beta, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_21d_curv_v103_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _max(beta, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_21d_curv_v104_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _max(beta, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_21d_curv_v105_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = beta - _max(beta, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_63d_curv_v106_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _max(beta, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_63d_curv_v107_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _max(beta, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_63d_curv_v108_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _max(beta, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_63d_curv_v109_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _max(beta, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_63d_curv_v110_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = beta - _max(beta, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_126d_curv_v111_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _max(beta, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_126d_curv_v112_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _max(beta, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_126d_curv_v113_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _max(beta, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_126d_curv_v114_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _max(beta, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_126d_curv_v115_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = beta - _max(beta, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_252d_curv_v116_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _max(beta, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_252d_curv_v117_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _max(beta, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_252d_curv_v118_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _max(beta, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_252d_curv_v119_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _max(beta, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_252d_curv_v120_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = beta - _max(beta, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_504d_curv_v121_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _max(beta, 756)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_504d_curv_v122_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _max(beta, 756)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_504d_curv_v123_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _max(beta, 756)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_504d_curv_v124_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _max(beta, 756)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_504d_curv_v125_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = beta - _max(beta, 756)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d beta std
def f02bb_f02_semi_basket_beta_betastd_21d_curv_v126_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = _std(beta, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d beta std
def f02bb_f02_semi_basket_beta_betastd_21d_curv_v127_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = _std(beta, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d beta std
def f02bb_f02_semi_basket_beta_betastd_21d_curv_v128_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = _std(beta, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d beta std
def f02bb_f02_semi_basket_beta_betastd_21d_curv_v129_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = _std(beta, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d beta std
def f02bb_f02_semi_basket_beta_betastd_21d_curv_v130_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    base = _std(beta, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d beta std
def f02bb_f02_semi_basket_beta_betastd_63d_curv_v131_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = _std(beta, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d beta std
def f02bb_f02_semi_basket_beta_betastd_63d_curv_v132_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = _std(beta, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d beta std
def f02bb_f02_semi_basket_beta_betastd_63d_curv_v133_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = _std(beta, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d beta std
def f02bb_f02_semi_basket_beta_betastd_63d_curv_v134_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = _std(beta, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d beta std
def f02bb_f02_semi_basket_beta_betastd_63d_curv_v135_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    base = _std(beta, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d beta std
def f02bb_f02_semi_basket_beta_betastd_126d_curv_v136_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = _std(beta, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d beta std
def f02bb_f02_semi_basket_beta_betastd_126d_curv_v137_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = _std(beta, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d beta std
def f02bb_f02_semi_basket_beta_betastd_126d_curv_v138_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = _std(beta, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d beta std
def f02bb_f02_semi_basket_beta_betastd_126d_curv_v139_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = _std(beta, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d beta std
def f02bb_f02_semi_basket_beta_betastd_126d_curv_v140_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    base = _std(beta, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d beta std
def f02bb_f02_semi_basket_beta_betastd_252d_curv_v141_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = _std(beta, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d beta std
def f02bb_f02_semi_basket_beta_betastd_252d_curv_v142_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = _std(beta, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d beta std
def f02bb_f02_semi_basket_beta_betastd_252d_curv_v143_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = _std(beta, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d beta std
def f02bb_f02_semi_basket_beta_betastd_252d_curv_v144_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = _std(beta, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d beta std
def f02bb_f02_semi_basket_beta_betastd_252d_curv_v145_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    base = _std(beta, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d beta std
def f02bb_f02_semi_basket_beta_betastd_504d_curv_v146_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = _std(beta, 756)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d beta std
def f02bb_f02_semi_basket_beta_betastd_504d_curv_v147_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = _std(beta, 756)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d beta std
def f02bb_f02_semi_basket_beta_betastd_504d_curv_v148_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = _std(beta, 756)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d beta std
def f02bb_f02_semi_basket_beta_betastd_504d_curv_v149_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = _std(beta, 756)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d beta std
def f02bb_f02_semi_basket_beta_betastd_504d_curv_v150_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    base = _std(beta, 756)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


