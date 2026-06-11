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


# 21d rolling correlation own vs basket
def f15cb_f15_semi_correlation_breakdown_corr_21d_base_v001_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation own vs basket
def f15cb_f15_semi_correlation_breakdown_corr_63d_base_v002_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation own vs basket
def f15cb_f15_semi_correlation_breakdown_corr_126d_base_v003_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation own vs basket
def f15cb_f15_semi_correlation_breakdown_corr_252d_base_v004_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation own vs basket
def f15cb_f15_semi_correlation_breakdown_corr_504d_base_v005_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr minus 63d corr (breakdown spread)
def f15cb_f15_semi_correlation_breakdown_corrspread_21v63_base_v006_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_corr_diff(o, b, 21, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d corr minus 126d corr (breakdown spread)
def f15cb_f15_semi_correlation_breakdown_corrspread_21v126_base_v007_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_corr_diff(o, b, 21, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr minus 126d corr (breakdown spread)
def f15cb_f15_semi_correlation_breakdown_corrspread_63v126_base_v008_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_corr_diff(o, b, 63, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d corr minus 252d corr (breakdown spread)
def f15cb_f15_semi_correlation_breakdown_corrspread_63v252_base_v009_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_corr_diff(o, b, 63, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d corr minus 252d corr (breakdown spread)
def f15cb_f15_semi_correlation_breakdown_corrspread_126v252_base_v010_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    result = _f15_corr_diff(o, b, 126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of correlation
def f15cb_f15_semi_correlation_breakdown_corrz_21d_base_v011_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = _z(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of correlation
def f15cb_f15_semi_correlation_breakdown_corrz_63d_base_v012_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = _z(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of correlation
def f15cb_f15_semi_correlation_breakdown_corrz_126d_base_v013_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of correlation
def f15cb_f15_semi_correlation_breakdown_corrz_252d_base_v014_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of correlation
def f15cb_f15_semi_correlation_breakdown_corrz_504d_base_v015_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = _z(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of correlation
def f15cb_f15_semi_correlation_breakdown_corrrz_21d_base_v016_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    med = c.rolling(21, min_periods=11).median()
    mad = (c - med).abs().rolling(21, min_periods=11).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of correlation
def f15cb_f15_semi_correlation_breakdown_corrrz_63d_base_v017_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    med = c.rolling(63, min_periods=32).median()
    mad = (c - med).abs().rolling(63, min_periods=32).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of correlation
def f15cb_f15_semi_correlation_breakdown_corrrz_126d_base_v018_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    med = c.rolling(126, min_periods=63).median()
    mad = (c - med).abs().rolling(126, min_periods=63).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of correlation
def f15cb_f15_semi_correlation_breakdown_corrrz_252d_base_v019_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    med = c.rolling(252, min_periods=126).median()
    mad = (c - med).abs().rolling(252, min_periods=126).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of correlation
def f15cb_f15_semi_correlation_breakdown_corrrz_504d_base_v020_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    med = c.rolling(504, min_periods=252).median()
    mad = (c - med).abs().rolling(504, min_periods=252).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation drop (corr - corr.shift(w))
def f15cb_f15_semi_correlation_breakdown_corrdrop_21d_base_v021_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c - c.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation drop (corr - corr.shift(w))
def f15cb_f15_semi_correlation_breakdown_corrdrop_63d_base_v022_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = c - c.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation drop (corr - corr.shift(w))
def f15cb_f15_semi_correlation_breakdown_corrdrop_126d_base_v023_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = c - c.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation drop (corr - corr.shift(w))
def f15cb_f15_semi_correlation_breakdown_corrdrop_252d_base_v024_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = c - c.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation drop (corr - corr.shift(w))
def f15cb_f15_semi_correlation_breakdown_corrdrop_504d_base_v025_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = c - c.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation drawdown from rolling peak
def f15cb_f15_semi_correlation_breakdown_corrdd_21d_base_v026_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c - _max(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation drawdown from rolling peak
def f15cb_f15_semi_correlation_breakdown_corrdd_63d_base_v027_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = c - _max(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation drawdown from rolling peak
def f15cb_f15_semi_correlation_breakdown_corrdd_126d_base_v028_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = c - _max(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation drawdown from rolling peak
def f15cb_f15_semi_correlation_breakdown_corrdd_252d_base_v029_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = c - _max(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation drawdown from rolling peak
def f15cb_f15_semi_correlation_breakdown_corrdd_504d_base_v030_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = c - _max(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation run-up above rolling trough
def f15cb_f15_semi_correlation_breakdown_corrup_21d_base_v031_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = c - _min(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation run-up above rolling trough
def f15cb_f15_semi_correlation_breakdown_corrup_63d_base_v032_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = c - _min(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation run-up above rolling trough
def f15cb_f15_semi_correlation_breakdown_corrup_126d_base_v033_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = c - _min(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation run-up above rolling trough
def f15cb_f15_semi_correlation_breakdown_corrup_252d_base_v034_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = c - _min(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation run-up above rolling trough
def f15cb_f15_semi_correlation_breakdown_corrup_504d_base_v035_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = c - _min(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrstd_21d_base_v036_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = _std(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrstd_63d_base_v037_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = _std(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrstd_126d_base_v038_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = _std(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrstd_252d_base_v039_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = _std(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of rolling correlation
def f15cb_f15_semi_correlation_breakdown_corrstd_504d_base_v040_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = _std(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of correlation
def f15cb_f15_semi_correlation_breakdown_corrmax_21d_base_v041_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = _max(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of correlation
def f15cb_f15_semi_correlation_breakdown_corrmax_63d_base_v042_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = _max(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of correlation
def f15cb_f15_semi_correlation_breakdown_corrmax_126d_base_v043_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = _max(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of correlation
def f15cb_f15_semi_correlation_breakdown_corrmax_252d_base_v044_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = _max(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of correlation
def f15cb_f15_semi_correlation_breakdown_corrmax_504d_base_v045_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = _max(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of correlation
def f15cb_f15_semi_correlation_breakdown_corrmin_21d_base_v046_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = _min(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of correlation
def f15cb_f15_semi_correlation_breakdown_corrmin_63d_base_v047_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = _min(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of correlation
def f15cb_f15_semi_correlation_breakdown_corrmin_126d_base_v048_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = _min(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of correlation
def f15cb_f15_semi_correlation_breakdown_corrmin_252d_base_v049_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = _min(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of correlation
def f15cb_f15_semi_correlation_breakdown_corrmin_504d_base_v050_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = _min(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of correlation
def f15cb_f15_semi_correlation_breakdown_corrrng_21d_base_v051_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = _max(c, 21) - _min(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of correlation
def f15cb_f15_semi_correlation_breakdown_corrrng_63d_base_v052_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    result = _max(c, 63) - _min(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of correlation
def f15cb_f15_semi_correlation_breakdown_corrrng_126d_base_v053_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    result = _max(c, 126) - _min(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of correlation
def f15cb_f15_semi_correlation_breakdown_corrrng_252d_base_v054_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    result = _max(c, 252) - _min(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of correlation
def f15cb_f15_semi_correlation_breakdown_corrrng_504d_base_v055_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    result = _max(c, 504) - _min(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of correlation
def f15cb_f15_semi_correlation_breakdown_corrpos_21d_base_v056_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    lo = _min(c, 21)
    hi = _max(c, 21)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of correlation
def f15cb_f15_semi_correlation_breakdown_corrpos_63d_base_v057_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 63)
    lo = _min(c, 63)
    hi = _max(c, 63)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of correlation
def f15cb_f15_semi_correlation_breakdown_corrpos_126d_base_v058_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 126)
    lo = _min(c, 126)
    hi = _max(c, 126)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of correlation
def f15cb_f15_semi_correlation_breakdown_corrpos_252d_base_v059_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 252)
    lo = _min(c, 252)
    hi = _max(c, 252)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of correlation
def f15cb_f15_semi_correlation_breakdown_corrpos_504d_base_v060_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 504)
    lo = _min(c, 504)
    hi = _max(c, 504)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of low-correlation days (corr < 0.3)
def f15cb_f15_semi_correlation_breakdown_lowcorrct_21d_base_v061_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0.3).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of low-correlation days (corr < 0.3)
def f15cb_f15_semi_correlation_breakdown_lowcorrct_63d_base_v062_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0.3).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of low-correlation days (corr < 0.3)
def f15cb_f15_semi_correlation_breakdown_lowcorrct_126d_base_v063_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0.3).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of low-correlation days (corr < 0.3)
def f15cb_f15_semi_correlation_breakdown_lowcorrct_252d_base_v064_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0.3).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of low-correlation days (corr < 0.3)
def f15cb_f15_semi_correlation_breakdown_lowcorrct_504d_base_v065_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0.3).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of negative correlation days
def f15cb_f15_semi_correlation_breakdown_negcorrct_21d_base_v066_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of negative correlation days
def f15cb_f15_semi_correlation_breakdown_negcorrct_63d_base_v067_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of negative correlation days
def f15cb_f15_semi_correlation_breakdown_negcorrct_126d_base_v068_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of negative correlation days
def f15cb_f15_semi_correlation_breakdown_negcorrct_252d_base_v069_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of negative correlation days
def f15cb_f15_semi_correlation_breakdown_negcorrct_504d_base_v070_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    b = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, b, 21)
    result = (c < 0).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# correlation EMA crossover 5v21
def f15cb_f15_semi_correlation_breakdown_correma_5v21_base_v071_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    bret = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, bret, 21)
    result = c.ewm(span=5, adjust=False).mean() - c.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# correlation EMA crossover 21v63
def f15cb_f15_semi_correlation_breakdown_correma_21v63_base_v072_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    bret = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, bret, 63)
    result = c.ewm(span=21, adjust=False).mean() - c.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# correlation EMA crossover 63v126
def f15cb_f15_semi_correlation_breakdown_correma_63v126_base_v073_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    bret = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, bret, 126)
    result = c.ewm(span=63, adjust=False).mean() - c.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# correlation EMA crossover 126v252
def f15cb_f15_semi_correlation_breakdown_correma_126v252_base_v074_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    bret = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, bret, 252)
    result = c.ewm(span=126, adjust=False).mean() - c.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# correlation EMA crossover 252v504
def f15cb_f15_semi_correlation_breakdown_correma_252v504_base_v075_signal(closeadj, semi_basket_closeadj):
    o = _f15_own_ret(closeadj)
    bret = _f15_own_ret(semi_basket_closeadj)
    c = _f15_roll_corr(o, bret, 504)
    result = c.ewm(span=252, adjust=False).mean() - c.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
