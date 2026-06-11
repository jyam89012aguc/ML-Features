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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f07_ret(s):
    return s.pct_change()


def _f07_abs_dev(o, b):
    return (o - b).abs()


def _f07_logret(s):
    return np.log(s / s.shift(1))

# 21d mean |own-basket| return (own dispersion)
def f07ds_f07_semi_dispersion_owndisp_21d_base_v001_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = _mean(_f07_abs_dev(o, b), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean |own-basket| return (own dispersion)
def f07ds_f07_semi_dispersion_owndisp_63d_base_v002_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = _mean(_f07_abs_dev(o, b), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean |own-basket| return (own dispersion)
def f07ds_f07_semi_dispersion_owndisp_126d_base_v003_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = _mean(_f07_abs_dev(o, b), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean |own-basket| return (own dispersion)
def f07ds_f07_semi_dispersion_owndisp_252d_base_v004_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = _mean(_f07_abs_dev(o, b), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean |own-basket| return (own dispersion)
def f07ds_f07_semi_dispersion_owndisp_504d_base_v005_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = _mean(_f07_abs_dev(o, b), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_21d_base_v006_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _mean(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_63d_base_v007_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _mean(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_126d_base_v008_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _mean(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_252d_base_v009_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _mean(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean basket dispersion
def f07ds_f07_semi_dispersion_basketdisp_504d_base_v010_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _mean(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own dispersion / basket dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_21d_base_v011_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    result = od / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own dispersion / basket dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_63d_base_v012_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    result = od / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own dispersion / basket dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_126d_base_v013_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    result = od / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own dispersion / basket dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_252d_base_v014_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    result = od / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own dispersion / basket dispersion ratio
def f07ds_f07_semi_dispersion_dispratio_504d_base_v015_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    result = od / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of own dispersion
def f07ds_f07_semi_dispersion_owndispz_21d_base_v016_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    result = _z(od, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of own dispersion
def f07ds_f07_semi_dispersion_owndispz_63d_base_v017_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    result = _z(od, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of own dispersion
def f07ds_f07_semi_dispersion_owndispz_126d_base_v018_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    result = _z(od, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of own dispersion
def f07ds_f07_semi_dispersion_owndispz_252d_base_v019_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    result = _z(od, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of own dispersion
def f07ds_f07_semi_dispersion_owndispz_504d_base_v020_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    result = _z(od, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of basket dispersion
def f07ds_f07_semi_dispersion_basketdispz_21d_base_v021_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _z(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of basket dispersion
def f07ds_f07_semi_dispersion_basketdispz_63d_base_v022_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _z(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of basket dispersion
def f07ds_f07_semi_dispersion_basketdispz_126d_base_v023_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _z(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of basket dispersion
def f07ds_f07_semi_dispersion_basketdispz_252d_base_v024_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _z(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of basket dispersion
def f07ds_f07_semi_dispersion_basketdispz_504d_base_v025_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _z(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d excess own dispersion over basket dispersion
def f07ds_f07_semi_dispersion_excessdisp_21d_base_v026_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    result = od - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 63d excess own dispersion over basket dispersion
def f07ds_f07_semi_dispersion_excessdisp_63d_base_v027_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    result = od - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 126d excess own dispersion over basket dispersion
def f07ds_f07_semi_dispersion_excessdisp_126d_base_v028_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    result = od - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 252d excess own dispersion over basket dispersion
def f07ds_f07_semi_dispersion_excessdisp_252d_base_v029_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    result = od - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 504d excess own dispersion over basket dispersion
def f07ds_f07_semi_dispersion_excessdisp_504d_base_v030_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    result = od - bd
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispcnt_21d_base_v031_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispcnt_63d_base_v032_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispcnt_126d_base_v033_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispcnt_252d_base_v034_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispcnt_504d_base_v035_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispfrac_21d_base_v036_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispfrac_63d_base_v037_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispfrac_126d_base_v038_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispfrac_252d_base_v039_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days own-deviation exceeds basket dispersion
def f07ds_f07_semi_dispersion_owndispfrac_504d_base_v040_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = (ad > semi_basket_dispersion).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of own |deviation| (dispersion vol)
def f07ds_f07_semi_dispersion_dispvol_21d_base_v041_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _std(ad, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of own |deviation| (dispersion vol)
def f07ds_f07_semi_dispersion_dispvol_63d_base_v042_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _std(ad, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of own |deviation| (dispersion vol)
def f07ds_f07_semi_dispersion_dispvol_126d_base_v043_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _std(ad, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of own |deviation| (dispersion vol)
def f07ds_f07_semi_dispersion_dispvol_252d_base_v044_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _std(ad, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of own |deviation| (dispersion vol)
def f07ds_f07_semi_dispersion_dispvol_504d_base_v045_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _std(ad, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max own |deviation|
def f07ds_f07_semi_dispersion_dispmax_21d_base_v046_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _max(ad, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max own |deviation|
def f07ds_f07_semi_dispersion_dispmax_63d_base_v047_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _max(ad, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max own |deviation|
def f07ds_f07_semi_dispersion_dispmax_126d_base_v048_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _max(ad, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max own |deviation|
def f07ds_f07_semi_dispersion_dispmax_252d_base_v049_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _max(ad, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max own |deviation|
def f07ds_f07_semi_dispersion_dispmax_504d_base_v050_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _max(ad, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min own |deviation|
def f07ds_f07_semi_dispersion_dispmin_21d_base_v051_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _min(ad, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min own |deviation|
def f07ds_f07_semi_dispersion_dispmin_63d_base_v052_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _min(ad, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min own |deviation|
def f07ds_f07_semi_dispersion_dispmin_126d_base_v053_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _min(ad, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min own |deviation|
def f07ds_f07_semi_dispersion_dispmin_252d_base_v054_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _min(ad, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min own |deviation|
def f07ds_f07_semi_dispersion_dispmin_504d_base_v055_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = _min(ad, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own dispersion position in rolling range
def f07ds_f07_semi_dispersion_disppos_21d_base_v056_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    lo, hi = _min(ad, 21), _max(ad, 21)
    result = (ad - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own dispersion position in rolling range
def f07ds_f07_semi_dispersion_disppos_63d_base_v057_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    lo, hi = _min(ad, 63), _max(ad, 63)
    result = (ad - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own dispersion position in rolling range
def f07ds_f07_semi_dispersion_disppos_126d_base_v058_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    lo, hi = _min(ad, 126), _max(ad, 126)
    result = (ad - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own dispersion position in rolling range
def f07ds_f07_semi_dispersion_disppos_252d_base_v059_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    lo, hi = _min(ad, 252), _max(ad, 252)
    result = (ad - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own dispersion position in rolling range
def f07ds_f07_semi_dispersion_disppos_504d_base_v060_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    lo, hi = _min(ad, 504), _max(ad, 504)
    result = (ad - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of basket dispersion
def f07ds_f07_semi_dispersion_basketdispema_5v21_base_v061_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion.ewm(span=5, adjust=False).mean() - semi_basket_dispersion.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of basket dispersion
def f07ds_f07_semi_dispersion_basketdispema_21v63_base_v062_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion.ewm(span=21, adjust=False).mean() - semi_basket_dispersion.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of basket dispersion
def f07ds_f07_semi_dispersion_basketdispema_63v126_base_v063_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion.ewm(span=63, adjust=False).mean() - semi_basket_dispersion.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of basket dispersion
def f07ds_f07_semi_dispersion_basketdispema_126v252_base_v064_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion.ewm(span=126, adjust=False).mean() - semi_basket_dispersion.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of basket dispersion
def f07ds_f07_semi_dispersion_basketdispema_252v504_base_v065_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion.ewm(span=252, adjust=False).mean() - semi_basket_dispersion.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of own |deviation|
def f07ds_f07_semi_dispersion_owndispema_5v21_base_v066_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = ad.ewm(span=5, adjust=False).mean() - ad.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of own |deviation|
def f07ds_f07_semi_dispersion_owndispema_21v63_base_v067_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = ad.ewm(span=21, adjust=False).mean() - ad.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of own |deviation|
def f07ds_f07_semi_dispersion_owndispema_63v126_base_v068_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = ad.ewm(span=63, adjust=False).mean() - ad.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of own |deviation|
def f07ds_f07_semi_dispersion_owndispema_126v252_base_v069_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = ad.ewm(span=126, adjust=False).mean() - ad.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of own |deviation|
def f07ds_f07_semi_dispersion_owndispema_252v504_base_v070_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    result = ad.ewm(span=252, adjust=False).mean() - ad.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of dispersion ratio
def f07ds_f07_semi_dispersion_dispratioz_21d_base_v071_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 21)
    bd = _mean(semi_basket_dispersion, 21)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of dispersion ratio
def f07ds_f07_semi_dispersion_dispratioz_63d_base_v072_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of dispersion ratio
def f07ds_f07_semi_dispersion_dispratioz_126d_base_v073_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 126)
    bd = _mean(semi_basket_dispersion, 126)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of dispersion ratio
def f07ds_f07_semi_dispersion_dispratioz_252d_base_v074_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of dispersion ratio
def f07ds_f07_semi_dispersion_dispratioz_504d_base_v075_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 504)
    bd = _mean(semi_basket_dispersion, 504)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 756)
    return result.replace([np.inf, -np.inf], np.nan)


