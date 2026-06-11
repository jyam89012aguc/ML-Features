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
def _f07_ret(s):
    return s.pct_change()


def _f07_abs_dev(o, b):
    return (o - b).abs()


def _f07_logret(s):
    return np.log(s / s.shift(1))

# 5d curv of 21d own dispersion
def f07ds_f07_semi_dispersion_owndisp_21d_curv_v001_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d own dispersion
def f07ds_f07_semi_dispersion_owndisp_21d_curv_v002_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d own dispersion
def f07ds_f07_semi_dispersion_owndisp_21d_curv_v003_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d own dispersion
def f07ds_f07_semi_dispersion_owndisp_21d_curv_v004_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d own dispersion
def f07ds_f07_semi_dispersion_owndisp_21d_curv_v005_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d own dispersion
def f07ds_f07_semi_dispersion_owndisp_63d_curv_v006_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d own dispersion
def f07ds_f07_semi_dispersion_owndisp_63d_curv_v007_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d own dispersion
def f07ds_f07_semi_dispersion_owndisp_63d_curv_v008_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d own dispersion
def f07ds_f07_semi_dispersion_owndisp_63d_curv_v009_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d own dispersion
def f07ds_f07_semi_dispersion_owndisp_63d_curv_v010_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d own dispersion
def f07ds_f07_semi_dispersion_owndisp_126d_curv_v011_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d own dispersion
def f07ds_f07_semi_dispersion_owndisp_126d_curv_v012_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d own dispersion
def f07ds_f07_semi_dispersion_owndisp_126d_curv_v013_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d own dispersion
def f07ds_f07_semi_dispersion_owndisp_126d_curv_v014_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d own dispersion
def f07ds_f07_semi_dispersion_owndisp_126d_curv_v015_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d own dispersion
def f07ds_f07_semi_dispersion_owndisp_252d_curv_v016_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d own dispersion
def f07ds_f07_semi_dispersion_owndisp_252d_curv_v017_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d own dispersion
def f07ds_f07_semi_dispersion_owndisp_252d_curv_v018_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d own dispersion
def f07ds_f07_semi_dispersion_owndisp_252d_curv_v019_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d own dispersion
def f07ds_f07_semi_dispersion_owndisp_252d_curv_v020_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d own dispersion
def f07ds_f07_semi_dispersion_owndisp_504d_curv_v021_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d own dispersion
def f07ds_f07_semi_dispersion_owndisp_504d_curv_v022_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d own dispersion
def f07ds_f07_semi_dispersion_owndisp_504d_curv_v023_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d own dispersion
def f07ds_f07_semi_dispersion_owndisp_504d_curv_v024_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d own dispersion
def f07ds_f07_semi_dispersion_owndisp_504d_curv_v025_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    base = _mean(_f07_abs_dev(o, b), 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_21d_curv_v026_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_21d_curv_v027_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_21d_curv_v028_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_21d_curv_v029_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_21d_curv_v030_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_63d_curv_v031_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_63d_curv_v032_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_63d_curv_v033_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_63d_curv_v034_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_63d_curv_v035_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_126d_curv_v036_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_126d_curv_v037_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_126d_curv_v038_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_126d_curv_v039_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_126d_curv_v040_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_252d_curv_v041_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_252d_curv_v042_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_252d_curv_v043_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_252d_curv_v044_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_252d_curv_v045_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_504d_curv_v046_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_504d_curv_v047_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_504d_curv_v048_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_504d_curv_v049_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_504d_curv_v050_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = _mean(semi_basket_dispersion, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_21d_curv_v051_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_21d_curv_v052_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_21d_curv_v053_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_21d_curv_v054_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_21d_curv_v055_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_63d_curv_v056_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_63d_curv_v057_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_63d_curv_v058_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_63d_curv_v059_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_63d_curv_v060_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_126d_curv_v061_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_126d_curv_v062_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_126d_curv_v063_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_126d_curv_v064_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_126d_curv_v065_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_252d_curv_v066_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_252d_curv_v067_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_252d_curv_v068_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_252d_curv_v069_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_252d_curv_v070_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_504d_curv_v071_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_504d_curv_v072_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_504d_curv_v073_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_504d_curv_v074_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_504d_curv_v075_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od / bd.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_21d_curv_v076_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od - bd
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_21d_curv_v077_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od - bd
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_21d_curv_v078_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od - bd
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_21d_curv_v079_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od - bd
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_21d_curv_v080_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    base = od - bd
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_63d_curv_v081_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od - bd
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_63d_curv_v082_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od - bd
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_63d_curv_v083_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od - bd
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_63d_curv_v084_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od - bd
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_63d_curv_v085_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    base = od - bd
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_126d_curv_v086_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od - bd
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_126d_curv_v087_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od - bd
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_126d_curv_v088_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od - bd
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_126d_curv_v089_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od - bd
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_126d_curv_v090_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    base = od - bd
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_252d_curv_v091_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od - bd
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_252d_curv_v092_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od - bd
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_252d_curv_v093_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od - bd
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_252d_curv_v094_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od - bd
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_252d_curv_v095_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    base = od - bd
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_504d_curv_v096_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od - bd
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_504d_curv_v097_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od - bd
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_504d_curv_v098_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od - bd
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_504d_curv_v099_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od - bd
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d excess dispersion
def f07ds_f07_semi_dispersion_excessdisp_504d_curv_v100_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    base = od - bd
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_21d_curv_v101_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).mean()) / semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_21d_curv_v102_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).mean()) / semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_21d_curv_v103_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).mean()) / semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_21d_curv_v104_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).mean()) / semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_21d_curv_v105_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).mean()) / semi_basket_dispersion.rolling(63, min_periods=max(1, 63 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_63d_curv_v106_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).mean()) / semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_63d_curv_v107_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).mean()) / semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_63d_curv_v108_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).mean()) / semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_63d_curv_v109_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).mean()) / semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_63d_curv_v110_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).mean()) / semi_basket_dispersion.rolling(126, min_periods=max(1, 126 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_126d_curv_v111_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).mean()) / semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_126d_curv_v112_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).mean()) / semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_126d_curv_v113_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).mean()) / semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_126d_curv_v114_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).mean()) / semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_126d_curv_v115_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).mean()) / semi_basket_dispersion.rolling(252, min_periods=max(1, 252 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_252d_curv_v116_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).mean()) / semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_252d_curv_v117_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).mean()) / semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_252d_curv_v118_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).mean()) / semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_252d_curv_v119_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).mean()) / semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_252d_curv_v120_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).mean()) / semi_basket_dispersion.rolling(504, min_periods=max(1, 504 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_504d_curv_v121_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).mean()) / semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_504d_curv_v122_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).mean()) / semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_504d_curv_v123_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).mean()) / semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_504d_curv_v124_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).mean()) / semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d basket dispersion z-score
def f07ds_f07_semi_dispersion_basketdispz_504d_curv_v125_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    base = (semi_basket_dispersion - semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).mean()) / semi_basket_dispersion.rolling(756, min_periods=max(1, 756 // 2)).std().replace(0, np.nan)
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_21d_curv_v126_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_21d_curv_v127_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_21d_curv_v128_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_21d_curv_v129_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_21d_curv_v130_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_63d_curv_v131_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_63d_curv_v132_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_63d_curv_v133_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_63d_curv_v134_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_63d_curv_v135_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_126d_curv_v136_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_126d_curv_v137_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_126d_curv_v138_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_126d_curv_v139_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_126d_curv_v140_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_252d_curv_v141_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_252d_curv_v142_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_252d_curv_v143_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_252d_curv_v144_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_252d_curv_v145_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_504d_curv_v146_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_504d_curv_v147_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_504d_curv_v148_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_504d_curv_v149_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dispersion vol
def f07ds_f07_semi_dispersion_dispvol_504d_curv_v150_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    base = _std(ad, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


