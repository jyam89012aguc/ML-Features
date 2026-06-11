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

# 21d own vol / basket dispersion
def f07ds_f07_semi_dispersion_volvsdisp_21d_base_v076_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o = _f07_ret(closeadj)
    ov = _std(o, 21)
    bd = _mean(semi_basket_dispersion, 21)
    result = ov / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own vol / basket dispersion
def f07ds_f07_semi_dispersion_volvsdisp_63d_base_v077_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o = _f07_ret(closeadj)
    ov = _std(o, 63)
    bd = _mean(semi_basket_dispersion, 63)
    result = ov / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own vol / basket dispersion
def f07ds_f07_semi_dispersion_volvsdisp_126d_base_v078_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o = _f07_ret(closeadj)
    ov = _std(o, 126)
    bd = _mean(semi_basket_dispersion, 126)
    result = ov / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own vol / basket dispersion
def f07ds_f07_semi_dispersion_volvsdisp_252d_base_v079_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o = _f07_ret(closeadj)
    ov = _std(o, 252)
    bd = _mean(semi_basket_dispersion, 252)
    result = ov / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own vol / basket dispersion
def f07ds_f07_semi_dispersion_volvsdisp_504d_base_v080_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o = _f07_ret(closeadj)
    ov = _std(o, 504)
    bd = _mean(semi_basket_dispersion, 504)
    result = ov / bd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of basket dispersion
def f07ds_f07_semi_dispersion_basketdispstd_21d_base_v081_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _std(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of basket dispersion
def f07ds_f07_semi_dispersion_basketdispstd_63d_base_v082_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _std(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of basket dispersion
def f07ds_f07_semi_dispersion_basketdispstd_126d_base_v083_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _std(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of basket dispersion
def f07ds_f07_semi_dispersion_basketdispstd_252d_base_v084_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _std(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of basket dispersion
def f07ds_f07_semi_dispersion_basketdispstd_504d_base_v085_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _std(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprobustz_21d_base_v086_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    med = semi_basket_dispersion.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (semi_basket_dispersion - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    result = (semi_basket_dispersion - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprobustz_63d_base_v087_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    med = semi_basket_dispersion.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (semi_basket_dispersion - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    result = (semi_basket_dispersion - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprobustz_126d_base_v088_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    med = semi_basket_dispersion.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (semi_basket_dispersion - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    result = (semi_basket_dispersion - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprobustz_252d_base_v089_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    med = semi_basket_dispersion.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (semi_basket_dispersion - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    result = (semi_basket_dispersion - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprobustz_504d_base_v090_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    med = semi_basket_dispersion.rolling(756, min_periods=max(2, 756 // 2)).median()
    mad = (semi_basket_dispersion - med).abs().rolling(756, min_periods=max(2, 756 // 2)).median()
    result = (semi_basket_dispersion - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max basket dispersion
def f07ds_f07_semi_dispersion_basketdispmax_21d_base_v091_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max basket dispersion
def f07ds_f07_semi_dispersion_basketdispmax_63d_base_v092_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max basket dispersion
def f07ds_f07_semi_dispersion_basketdispmax_126d_base_v093_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max basket dispersion
def f07ds_f07_semi_dispersion_basketdispmax_252d_base_v094_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max basket dispersion
def f07ds_f07_semi_dispersion_basketdispmax_504d_base_v095_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min basket dispersion
def f07ds_f07_semi_dispersion_basketdispmin_21d_base_v096_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _min(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min basket dispersion
def f07ds_f07_semi_dispersion_basketdispmin_63d_base_v097_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _min(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min basket dispersion
def f07ds_f07_semi_dispersion_basketdispmin_126d_base_v098_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _min(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min basket dispersion
def f07ds_f07_semi_dispersion_basketdispmin_252d_base_v099_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _min(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min basket dispersion
def f07ds_f07_semi_dispersion_basketdispmin_504d_base_v100_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _min(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprng_21d_base_v101_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 21) - _min(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprng_63d_base_v102_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 63) - _min(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprng_126d_base_v103_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 126) - _min(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprng_252d_base_v104_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 252) - _min(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of basket dispersion
def f07ds_f07_semi_dispersion_basketdisprng_504d_base_v105_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = _max(semi_basket_dispersion, 504) - _min(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basket dispersion position in range
def f07ds_f07_semi_dispersion_basketdisppos_21d_base_v106_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    lo, hi = _min(semi_basket_dispersion, 21), _max(semi_basket_dispersion, 21)
    result = (semi_basket_dispersion - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basket dispersion position in range
def f07ds_f07_semi_dispersion_basketdisppos_63d_base_v107_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    lo, hi = _min(semi_basket_dispersion, 63), _max(semi_basket_dispersion, 63)
    result = (semi_basket_dispersion - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basket dispersion position in range
def f07ds_f07_semi_dispersion_basketdisppos_126d_base_v108_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    lo, hi = _min(semi_basket_dispersion, 126), _max(semi_basket_dispersion, 126)
    result = (semi_basket_dispersion - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basket dispersion position in range
def f07ds_f07_semi_dispersion_basketdisppos_252d_base_v109_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    lo, hi = _min(semi_basket_dispersion, 252), _max(semi_basket_dispersion, 252)
    result = (semi_basket_dispersion - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basket dispersion position in range
def f07ds_f07_semi_dispersion_basketdisppos_504d_base_v110_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    lo, hi = _min(semi_basket_dispersion, 504), _max(semi_basket_dispersion, 504)
    result = (semi_basket_dispersion - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basket dispersion drop from peak
def f07ds_f07_semi_dispersion_basketdispdd_21d_base_v111_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - _max(semi_basket_dispersion, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basket dispersion drop from peak
def f07ds_f07_semi_dispersion_basketdispdd_63d_base_v112_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - _max(semi_basket_dispersion, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basket dispersion drop from peak
def f07ds_f07_semi_dispersion_basketdispdd_126d_base_v113_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - _max(semi_basket_dispersion, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basket dispersion drop from peak
def f07ds_f07_semi_dispersion_basketdispdd_252d_base_v114_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - _max(semi_basket_dispersion, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basket dispersion drop from peak
def f07ds_f07_semi_dispersion_basketdispdd_504d_base_v115_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - _max(semi_basket_dispersion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own dispersion on basket-up days
def f07ds_f07_semi_dispersion_owndispcondup_21d_base_v116_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b > 0)
    result = _mean(ad, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own dispersion on basket-up days
def f07ds_f07_semi_dispersion_owndispcondup_63d_base_v117_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b > 0)
    result = _mean(ad, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own dispersion on basket-up days
def f07ds_f07_semi_dispersion_owndispcondup_126d_base_v118_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b > 0)
    result = _mean(ad, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own dispersion on basket-up days
def f07ds_f07_semi_dispersion_owndispcondup_252d_base_v119_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b > 0)
    result = _mean(ad, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own dispersion on basket-up days
def f07ds_f07_semi_dispersion_owndispcondup_504d_base_v120_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b > 0)
    result = _mean(ad, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own dispersion on basket-down days
def f07ds_f07_semi_dispersion_owndispconddn_21d_base_v121_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b < 0)
    result = _mean(ad, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own dispersion on basket-down days
def f07ds_f07_semi_dispersion_owndispconddn_63d_base_v122_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b < 0)
    result = _mean(ad, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own dispersion on basket-down days
def f07ds_f07_semi_dispersion_owndispconddn_126d_base_v123_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b < 0)
    result = _mean(ad, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own dispersion on basket-down days
def f07ds_f07_semi_dispersion_owndispconddn_252d_base_v124_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b < 0)
    result = _mean(ad, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own dispersion on basket-down days
def f07ds_f07_semi_dispersion_owndispconddn_504d_base_v125_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b).where(b < 0)
    result = _mean(ad, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own dispersion asymmetry (up - down)
def f07ds_f07_semi_dispersion_dispasym_21d_base_v126_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    du = _mean(ad.where(b > 0), 21)
    dd = _mean(ad.where(b < 0), 21)
    result = du - dd
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own dispersion asymmetry (up - down)
def f07ds_f07_semi_dispersion_dispasym_63d_base_v127_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    du = _mean(ad.where(b > 0), 63)
    dd = _mean(ad.where(b < 0), 63)
    result = du - dd
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own dispersion asymmetry (up - down)
def f07ds_f07_semi_dispersion_dispasym_126d_base_v128_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    du = _mean(ad.where(b > 0), 126)
    dd = _mean(ad.where(b < 0), 126)
    result = du - dd
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own dispersion asymmetry (up - down)
def f07ds_f07_semi_dispersion_dispasym_252d_base_v129_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    du = _mean(ad.where(b > 0), 252)
    dd = _mean(ad.where(b < 0), 252)
    result = du - dd
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own dispersion asymmetry (up - down)
def f07ds_f07_semi_dispersion_dispasym_504d_base_v130_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    du = _mean(ad.where(b > 0), 504)
    dd = _mean(ad.where(b < 0), 504)
    result = du - dd
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed (own-basket) cumulative dispersion
def f07ds_f07_semi_dispersion_signeddispcum_21d_base_v131_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = (o - b).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed (own-basket) cumulative dispersion
def f07ds_f07_semi_dispersion_signeddispcum_63d_base_v132_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = (o - b).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed (own-basket) cumulative dispersion
def f07ds_f07_semi_dispersion_signeddispcum_126d_base_v133_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = (o - b).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed (own-basket) cumulative dispersion
def f07ds_f07_semi_dispersion_signeddispcum_252d_base_v134_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = (o - b).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed (own-basket) cumulative dispersion
def f07ds_f07_semi_dispersion_signeddispcum_504d_base_v135_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    result = (o - b).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basket dispersion expansion (level - 21d shift)
def f07ds_f07_semi_dispersion_dispexp_21d_base_v136_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - semi_basket_dispersion.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basket dispersion expansion (level - 63d shift)
def f07ds_f07_semi_dispersion_dispexp_63d_base_v137_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - semi_basket_dispersion.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d basket dispersion expansion (level - 126d shift)
def f07ds_f07_semi_dispersion_dispexp_126d_base_v138_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - semi_basket_dispersion.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basket dispersion expansion (level - 252d shift)
def f07ds_f07_semi_dispersion_dispexp_252d_base_v139_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - semi_basket_dispersion.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d basket dispersion expansion (level - 504d shift)
def f07ds_f07_semi_dispersion_dispexp_504d_base_v140_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    result = semi_basket_dispersion - semi_basket_dispersion.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own dispersion x basket return vol
def f07ds_f07_semi_dispersion_dispxvol_21d_base_v141_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od = _mean(ad, 21)
    bv = _std(b, 21)
    result = od * bv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own dispersion x basket return vol
def f07ds_f07_semi_dispersion_dispxvol_63d_base_v142_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od = _mean(ad, 63)
    bv = _std(b, 63)
    result = od * bv
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own dispersion x basket return vol
def f07ds_f07_semi_dispersion_dispxvol_126d_base_v143_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od = _mean(ad, 126)
    bv = _std(b, 126)
    result = od * bv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own dispersion x basket return vol
def f07ds_f07_semi_dispersion_dispxvol_252d_base_v144_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od = _mean(ad, 252)
    bv = _std(b, 252)
    result = od * bv
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own dispersion x basket return vol
def f07ds_f07_semi_dispersion_dispxvol_504d_base_v145_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od = _mean(ad, 504)
    bv = _std(b, 504)
    result = od * bv
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of own dispersion
def f07ds_f07_semi_dispersion_dispcomposite_short_base_v146_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od21 = _mean(ad, 21)
    od63 = _mean(ad, 63)
    od126 = _mean(ad, 126)
    result = _z(od21, 63) + _z(od63, 126) + _z(od126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of own dispersion
def f07ds_f07_semi_dispersion_dispcomposite_long_base_v147_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    od63 = _mean(ad, 63)
    od126 = _mean(ad, 126)
    od252 = _mean(ad, 252)
    result = _z(od63, 126) + _z(od126, 252) + _z(od252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion regime divergence: short - long EMA cross sign
def f07ds_f07_semi_dispersion_dispregime_divergence_base_v148_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    ad = _f07_abs_dev(o, b)
    short = np.sign(ad.ewm(span=21, adjust=False).mean() - ad.ewm(span=63, adjust=False).mean())
    long = np.sign(ad.ewm(span=126, adjust=False).mean() - ad.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=ad.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dispersion quality: dispersion ratio z-score
def f07ds_f07_semi_dispersion_dispquality_63d_base_v149_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 63)
    bd = _mean(semi_basket_dispersion, 63)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion quality: dispersion ratio z-score
def f07ds_f07_semi_dispersion_dispquality_252d_base_v150_signal(closeadj, semi_basket_closeadj, semi_basket_dispersion):
    o, b = _f07_ret(closeadj), _f07_ret(semi_basket_closeadj)
    od = _mean(_f07_abs_dev(o, b), 252)
    bd = _mean(semi_basket_dispersion, 252)
    rat = od / bd.replace(0, np.nan)
    result = _z(rat, 504)
    return result.replace([np.inf, -np.inf], np.nan)


