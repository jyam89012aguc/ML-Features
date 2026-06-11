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
def _f15_own_ret(s):
    return s.pct_change()


def _f15_roll_corr(o, b, w):
    return o.rolling(w, min_periods=max(2, w // 2)).corr(b)


def _f15_corr_diff(o, b, short_w, long_w):
    cs = o.rolling(short_w, min_periods=max(2, short_w // 2)).corr(b)
    cl = o.rolling(long_w, min_periods=max(2, long_w // 2)).corr(b)
    return cs - cl


# 21d Fisher-z transform of correlation
def f15cb_f15_semi_correlation_breakdown_fisherz_21d_base_v076_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    c = c.clip(-0.9999, 0.9999)
    result = 0.5 * np.log((1 + c) / (1 - c))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Fisher-z transform of correlation
def f15cb_f15_semi_correlation_breakdown_fisherz_63d_base_v077_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    c = c.clip(-0.9999, 0.9999)
    result = 0.5 * np.log((1 + c) / (1 - c))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Fisher-z transform of correlation
def f15cb_f15_semi_correlation_breakdown_fisherz_126d_base_v078_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    c = c.clip(-0.9999, 0.9999)
    result = 0.5 * np.log((1 + c) / (1 - c))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Fisher-z transform of correlation
def f15cb_f15_semi_correlation_breakdown_fisherz_252d_base_v079_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    c = c.clip(-0.9999, 0.9999)
    result = 0.5 * np.log((1 + c) / (1 - c))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Fisher-z transform of correlation
def f15cb_f15_semi_correlation_breakdown_fisherz_504d_base_v080_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    c = c.clip(-0.9999, 0.9999)
    result = 0.5 * np.log((1 + c) / (1 - c))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in Fisher-z correlation over 21d
def f15cb_f15_semi_correlation_breakdown_fisherzdiff_21d_base_v081_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21).clip(-0.9999, 0.9999)
    fz = 0.5 * np.log((1 + c) / (1 - c))
    result = fz - fz.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in Fisher-z correlation over 63d
def f15cb_f15_semi_correlation_breakdown_fisherzdiff_63d_base_v082_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63).clip(-0.9999, 0.9999)
    fz = 0.5 * np.log((1 + c) / (1 - c))
    result = fz - fz.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in Fisher-z correlation over 126d
def f15cb_f15_semi_correlation_breakdown_fisherzdiff_126d_base_v083_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126).clip(-0.9999, 0.9999)
    fz = 0.5 * np.log((1 + c) / (1 - c))
    result = fz - fz.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in Fisher-z correlation over 252d
def f15cb_f15_semi_correlation_breakdown_fisherzdiff_252d_base_v084_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252).clip(-0.9999, 0.9999)
    fz = 0.5 * np.log((1 + c) / (1 - c))
    result = fz - fz.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in Fisher-z correlation over 504d
def f15cb_f15_semi_correlation_breakdown_fisherzdiff_504d_base_v085_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504).clip(-0.9999, 0.9999)
    fz = 0.5 * np.log((1 + c) / (1 - c))
    result = fz - fz.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation conditional on basket-down days
def f15cb_f15_semi_correlation_breakdown_corrconddn_21d_base_v086_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    od = o.where(b < 0)
    bd = b.where(b < 0)
    result = od.rolling(21, min_periods=10).corr(bd)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation conditional on basket-down days
def f15cb_f15_semi_correlation_breakdown_corrconddn_63d_base_v087_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    od = o.where(b < 0)
    bd = b.where(b < 0)
    result = od.rolling(63, min_periods=31).corr(bd)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation conditional on basket-down days
def f15cb_f15_semi_correlation_breakdown_corrconddn_126d_base_v088_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    od = o.where(b < 0)
    bd = b.where(b < 0)
    result = od.rolling(126, min_periods=63).corr(bd)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation conditional on basket-down days
def f15cb_f15_semi_correlation_breakdown_corrconddn_252d_base_v089_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    od = o.where(b < 0)
    bd = b.where(b < 0)
    result = od.rolling(252, min_periods=126).corr(bd)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation conditional on basket-down days
def f15cb_f15_semi_correlation_breakdown_corrconddn_504d_base_v090_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    od = o.where(b < 0)
    bd = b.where(b < 0)
    result = od.rolling(504, min_periods=252).corr(bd)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation conditional on basket-up days
def f15cb_f15_semi_correlation_breakdown_corrcondup_21d_base_v091_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    ou = o.where(b > 0)
    bu = b.where(b > 0)
    result = ou.rolling(21, min_periods=10).corr(bu)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation conditional on basket-up days
def f15cb_f15_semi_correlation_breakdown_corrcondup_63d_base_v092_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    ou = o.where(b > 0)
    bu = b.where(b > 0)
    result = ou.rolling(63, min_periods=31).corr(bu)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation conditional on basket-up days
def f15cb_f15_semi_correlation_breakdown_corrcondup_126d_base_v093_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    ou = o.where(b > 0)
    bu = b.where(b > 0)
    result = ou.rolling(126, min_periods=63).corr(bu)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation conditional on basket-up days
def f15cb_f15_semi_correlation_breakdown_corrcondup_252d_base_v094_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    ou = o.where(b > 0)
    bu = b.where(b > 0)
    result = ou.rolling(252, min_periods=126).corr(bu)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation conditional on basket-up days
def f15cb_f15_semi_correlation_breakdown_corrcondup_504d_base_v095_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    ou = o.where(b > 0)
    bu = b.where(b > 0)
    result = ou.rolling(504, min_periods=252).corr(bu)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asymmetric correlation (down minus up)
def f15cb_f15_semi_correlation_breakdown_asymcorr_21d_base_v096_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    cd = o.where(b < 0).rolling(21, min_periods=10).corr(b.where(b < 0))
    cu = o.where(b > 0).rolling(21, min_periods=10).corr(b.where(b > 0))
    result = cd - cu
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asymmetric correlation (down minus up)
def f15cb_f15_semi_correlation_breakdown_asymcorr_63d_base_v097_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    cd = o.where(b < 0).rolling(63, min_periods=31).corr(b.where(b < 0))
    cu = o.where(b > 0).rolling(63, min_periods=31).corr(b.where(b > 0))
    result = cd - cu
    return result.replace([np.inf, -np.inf], np.nan)


# 126d asymmetric correlation (down minus up)
def f15cb_f15_semi_correlation_breakdown_asymcorr_126d_base_v098_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    cd = o.where(b < 0).rolling(126, min_periods=63).corr(b.where(b < 0))
    cu = o.where(b > 0).rolling(126, min_periods=63).corr(b.where(b > 0))
    result = cd - cu
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asymmetric correlation (down minus up)
def f15cb_f15_semi_correlation_breakdown_asymcorr_252d_base_v099_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    cd = o.where(b < 0).rolling(252, min_periods=126).corr(b.where(b < 0))
    cu = o.where(b > 0).rolling(252, min_periods=126).corr(b.where(b > 0))
    result = cd - cu
    return result.replace([np.inf, -np.inf], np.nan)


# 504d asymmetric correlation (down minus up)
def f15cb_f15_semi_correlation_breakdown_asymcorr_504d_base_v100_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    cd = o.where(b < 0).rolling(504, min_periods=252).corr(b.where(b < 0))
    cu = o.where(b > 0).rolling(504, min_periods=252).corr(b.where(b > 0))
    result = cd - cu
    return result.replace([np.inf, -np.inf], np.nan)


# 21d decoupling level (1 - correlation)
def f15cb_f15_semi_correlation_breakdown_decoup_21d_base_v101_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = 1.0 - _f15_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decoupling level (1 - correlation)
def f15cb_f15_semi_correlation_breakdown_decoup_63d_base_v102_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = 1.0 - _f15_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d decoupling level (1 - correlation)
def f15cb_f15_semi_correlation_breakdown_decoup_126d_base_v103_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = 1.0 - _f15_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decoupling level (1 - correlation)
def f15cb_f15_semi_correlation_breakdown_decoup_252d_base_v104_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = 1.0 - _f15_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d decoupling level (1 - correlation)
def f15cb_f15_semi_correlation_breakdown_decoup_504d_base_v105_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = 1.0 - _f15_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative correlation change (regime drift)
def f15cb_f15_semi_correlation_breakdown_corrchgcum_21d_base_v106_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c - c.shift(1)
    result = d.rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative correlation change (regime drift)
def f15cb_f15_semi_correlation_breakdown_corrchgcum_63d_base_v107_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c - c.shift(1)
    result = d.rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative correlation change (regime drift)
def f15cb_f15_semi_correlation_breakdown_corrchgcum_126d_base_v108_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c - c.shift(1)
    result = d.rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative correlation change (regime drift)
def f15cb_f15_semi_correlation_breakdown_corrchgcum_252d_base_v109_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c - c.shift(1)
    result = d.rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative correlation change (regime drift)
def f15cb_f15_semi_correlation_breakdown_corrchgcum_504d_base_v110_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c - c.shift(1)
    result = d.rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d info ratio of correlation changes
def f15cb_f15_semi_correlation_breakdown_corrchgir_21d_base_v111_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c.diff()
    result = _mean(d, 21) / _std(d, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d info ratio of correlation changes
def f15cb_f15_semi_correlation_breakdown_corrchgir_63d_base_v112_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c.diff()
    result = _mean(d, 63) / _std(d, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d info ratio of correlation changes
def f15cb_f15_semi_correlation_breakdown_corrchgir_126d_base_v113_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c.diff()
    result = _mean(d, 126) / _std(d, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d info ratio of correlation changes
def f15cb_f15_semi_correlation_breakdown_corrchgir_252d_base_v114_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c.diff()
    result = _mean(d, 252) / _std(d, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d info ratio of correlation changes
def f15cb_f15_semi_correlation_breakdown_corrchgir_504d_base_v115_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    d = c.diff()
    result = _mean(d, 504) / _std(d, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrskew_21d_base_v116_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrskew_63d_base_v117_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrskew_126d_base_v118_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrskew_252d_base_v119_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrskew_504d_base_v120_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrkurt_21d_base_v121_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrkurt_63d_base_v122_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrkurt_126d_base_v123_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrkurt_252d_base_v124_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrkurt_504d_base_v125_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Spearman-style rank correlation
def f15cb_f15_semi_correlation_breakdown_spcorr_21d_base_v126_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj).rolling(21, min_periods=10).rank(pct=True)
    b = _f15_own_ret(semi_basket_closeadj).rolling(21, min_periods=10).rank(pct=True)
    result = o.rolling(21, min_periods=10).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Spearman-style rank correlation
def f15cb_f15_semi_correlation_breakdown_spcorr_63d_base_v127_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj).rolling(63, min_periods=31).rank(pct=True)
    b = _f15_own_ret(semi_basket_closeadj).rolling(63, min_periods=31).rank(pct=True)
    result = o.rolling(63, min_periods=31).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Spearman-style rank correlation
def f15cb_f15_semi_correlation_breakdown_spcorr_126d_base_v128_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj).rolling(126, min_periods=63).rank(pct=True)
    b = _f15_own_ret(semi_basket_closeadj).rolling(126, min_periods=63).rank(pct=True)
    result = o.rolling(126, min_periods=63).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Spearman-style rank correlation
def f15cb_f15_semi_correlation_breakdown_spcorr_252d_base_v129_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj).rolling(252, min_periods=126).rank(pct=True)
    b = _f15_own_ret(semi_basket_closeadj).rolling(252, min_periods=126).rank(pct=True)
    result = o.rolling(252, min_periods=126).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Spearman-style rank correlation
def f15cb_f15_semi_correlation_breakdown_spcorr_504d_base_v130_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj).rolling(504, min_periods=252).rank(pct=True)
    b = _f15_own_ret(semi_basket_closeadj).rolling(504, min_periods=252).rank(pct=True)
    result = o.rolling(504, min_periods=252).corr(b)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation of own with lag-1 basket (lead-lag)
def f15cb_f15_semi_correlation_breakdown_corrlag1_21d_base_v131_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = o.rolling(21, min_periods=10).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation of own with lag-1 basket (lead-lag)
def f15cb_f15_semi_correlation_breakdown_corrlag1_63d_base_v132_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = o.rolling(63, min_periods=31).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation of own with lag-1 basket (lead-lag)
def f15cb_f15_semi_correlation_breakdown_corrlag1_126d_base_v133_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = o.rolling(126, min_periods=63).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation of own with lag-1 basket (lead-lag)
def f15cb_f15_semi_correlation_breakdown_corrlag1_252d_base_v134_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = o.rolling(252, min_periods=126).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation of own with lag-1 basket (lead-lag)
def f15cb_f15_semi_correlation_breakdown_corrlag1_504d_base_v135_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = o.rolling(504, min_periods=252).corr(b.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of weak-correlation days (|corr| < 0.5)
def f15cb_f15_semi_correlation_breakdown_weakcorrct_21d_base_v136_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c.abs() < 0.5).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of weak-correlation days (|corr| < 0.5)
def f15cb_f15_semi_correlation_breakdown_weakcorrct_63d_base_v137_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c.abs() < 0.5).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of weak-correlation days (|corr| < 0.5)
def f15cb_f15_semi_correlation_breakdown_weakcorrct_126d_base_v138_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c.abs() < 0.5).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of weak-correlation days (|corr| < 0.5)
def f15cb_f15_semi_correlation_breakdown_weakcorrct_252d_base_v139_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c.abs() < 0.5).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of weak-correlation days (|corr| < 0.5)
def f15cb_f15_semi_correlation_breakdown_weakcorrct_504d_base_v140_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c.abs() < 0.5).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# correlation composite short (z21+z63+z126)
def f15cb_f15_semi_correlation_breakdown_corrcompshort_63d_base_v141_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c21 = _f15_roll_corr(o, b, 21)
    c63 = _f15_roll_corr(o, b, 63)
    c126 = _f15_roll_corr(o, b, 126)
    result = _z(c21, 21) + _z(c63, 63) + _z(c126, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation composite long (z63+z126+z252)
def f15cb_f15_semi_correlation_breakdown_corrcomplong_252d_base_v142_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c63 = _f15_roll_corr(o, b, 63)
    c126 = _f15_roll_corr(o, b, 126)
    c252 = _f15_roll_corr(o, b, 252)
    result = _z(c63, 63) + _z(c126, 126) + _z(c252, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation regime divergence
def f15cb_f15_semi_correlation_breakdown_corrregdiv_63d_base_v143_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    short = np.sign(c.ewm(span=21, adjust=False).mean() - c.ewm(span=63, adjust=False).mean())
    long = np.sign(c.ewm(span=126, adjust=False).mean() - c.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=c.index)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation breakdown quality 63d
def f15cb_f15_semi_correlation_breakdown_breakdownquality63_63d_base_v144_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    d = c - c.shift(21)
    ir = _mean(d, 63) / _std(d, 63).replace(0, np.nan)
    sev = (d < -0.1).astype(float).rolling(63, min_periods=32).mean()
    result = -ir * sev
    return result.replace([np.inf, -np.inf], np.nan)


# correlation breakdown quality 252d
def f15cb_f15_semi_correlation_breakdown_breakdownquality252_252d_base_v145_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    d = c - c.shift(63)
    ir = _mean(d, 252) / _std(d, 252).replace(0, np.nan)
    sev = (d < -0.1).astype(float).rolling(252, min_periods=126).mean()
    result = -ir * sev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max correlation drawdown magnitude
def f15cb_f15_semi_correlation_breakdown_corrmaxdd_21d_base_v146_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    dd = c - _max(c, 21)
    result = _min(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max correlation drawdown magnitude
def f15cb_f15_semi_correlation_breakdown_corrmaxdd_63d_base_v147_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    dd = c - _max(c, 63)
    result = _min(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max correlation drawdown magnitude
def f15cb_f15_semi_correlation_breakdown_corrmaxdd_126d_base_v148_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    dd = c - _max(c, 126)
    result = _min(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max correlation drawdown magnitude
def f15cb_f15_semi_correlation_breakdown_corrmaxdd_252d_base_v149_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    dd = c - _max(c, 252)
    result = _min(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max correlation drawdown magnitude
def f15cb_f15_semi_correlation_breakdown_corrmaxdd_504d_base_v150_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    dd = c - _max(c, 504)
    result = _min(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)
