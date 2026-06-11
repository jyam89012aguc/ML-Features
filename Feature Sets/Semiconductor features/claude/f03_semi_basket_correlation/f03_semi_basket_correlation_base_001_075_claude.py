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
def _f03_own_ret(s):
    return s.pct_change()


def _f03_roll_corr(own_r, bas_r, w):
    return own_r.rolling(w, min_periods=max(2, w // 2)).corr(bas_r)


def _f03_roll_cov(own_r, bas_r, w):
    return own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)

# 21d rolling correlation own vs basket
def f03bc_f03_semi_basket_correlation_corr_21d_base_v001_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling correlation own vs basket
def f03bc_f03_semi_basket_correlation_corr_63d_base_v002_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling correlation own vs basket
def f03bc_f03_semi_basket_correlation_corr_126d_base_v003_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling correlation own vs basket
def f03bc_f03_semi_basket_correlation_corr_252d_base_v004_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling correlation own vs basket
def f03bc_f03_semi_basket_correlation_corr_504d_base_v005_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = _f03_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d decorrelation 1 - corr
def f03bc_f03_semi_basket_correlation_decor_21d_base_v006_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = 1.0 - _f03_roll_corr(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decorrelation 1 - corr
def f03bc_f03_semi_basket_correlation_decor_63d_base_v007_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = 1.0 - _f03_roll_corr(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d decorrelation 1 - corr
def f03bc_f03_semi_basket_correlation_decor_126d_base_v008_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = 1.0 - _f03_roll_corr(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decorrelation 1 - corr
def f03bc_f03_semi_basket_correlation_decor_252d_base_v009_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = 1.0 - _f03_roll_corr(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d decorrelation 1 - corr
def f03bc_f03_semi_basket_correlation_decor_504d_base_v010_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    result = 1.0 - _f03_roll_corr(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrz_21d_base_v011_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = _z(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrz_63d_base_v012_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrz_126d_base_v013_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrz_252d_base_v014_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = _z(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrz_504d_base_v015_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = _z(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrobustz_21d_base_v016_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    med = c.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (c - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrobustz_63d_base_v017_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    med = c.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (c - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrobustz_126d_base_v018_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    med = c.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (c - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrobustz_252d_base_v019_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    med = c.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (c - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrobustz_504d_base_v020_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    med = c.rolling(756, min_periods=max(2, 756 // 2)).median()
    mad = (c - med).abs().rolling(756, min_periods=max(2, 756 // 2)).median()
    result = (c - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation deviation from longer mean
def f03bc_f03_semi_basket_correlation_corrdev_21d_base_v021_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = c - _mean(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation deviation from longer mean
def f03bc_f03_semi_basket_correlation_corrdev_63d_base_v022_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = c - _mean(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation deviation from longer mean
def f03bc_f03_semi_basket_correlation_corrdev_126d_base_v023_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = c - _mean(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation deviation from longer mean
def f03bc_f03_semi_basket_correlation_corrdev_252d_base_v024_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = c - _mean(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation deviation from longer mean
def f03bc_f03_semi_basket_correlation_corrdev_504d_base_v025_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = c - _mean(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of high-correlation days (corr > 0.7)
def f03bc_f03_semi_basket_correlation_corrhi_21d_base_v026_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = (c > 0.7).astype(float).rolling(21, min_periods=max(1, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of high-correlation days (corr > 0.7)
def f03bc_f03_semi_basket_correlation_corrhi_63d_base_v027_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = (c > 0.7).astype(float).rolling(63, min_periods=max(1, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of high-correlation days (corr > 0.7)
def f03bc_f03_semi_basket_correlation_corrhi_126d_base_v028_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = (c > 0.7).astype(float).rolling(126, min_periods=max(1, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-correlation days (corr > 0.7)
def f03bc_f03_semi_basket_correlation_corrhi_252d_base_v029_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = (c > 0.7).astype(float).rolling(252, min_periods=max(1, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of high-correlation days (corr > 0.7)
def f03bc_f03_semi_basket_correlation_corrhi_504d_base_v030_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = (c > 0.7).astype(float).rolling(504, min_periods=max(1, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of high-correlation days
def f03bc_f03_semi_basket_correlation_corrhifrac_21d_base_v031_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = (c > 0.7).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of high-correlation days
def f03bc_f03_semi_basket_correlation_corrhifrac_63d_base_v032_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = (c > 0.7).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of high-correlation days
def f03bc_f03_semi_basket_correlation_corrhifrac_126d_base_v033_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = (c > 0.7).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of high-correlation days
def f03bc_f03_semi_basket_correlation_corrhifrac_252d_base_v034_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = (c > 0.7).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of high-correlation days
def f03bc_f03_semi_basket_correlation_corrhifrac_504d_base_v035_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = (c > 0.7).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of rolling correlation
def f03bc_f03_semi_basket_correlation_corrstd_21d_base_v036_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = _std(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of rolling correlation
def f03bc_f03_semi_basket_correlation_corrstd_63d_base_v037_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = _std(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of rolling correlation
def f03bc_f03_semi_basket_correlation_corrstd_126d_base_v038_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = _std(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of rolling correlation
def f03bc_f03_semi_basket_correlation_corrstd_252d_base_v039_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = _std(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of rolling correlation
def f03bc_f03_semi_basket_correlation_corrstd_504d_base_v040_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = _std(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmax_21d_base_v041_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = _max(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmax_63d_base_v042_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = _max(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmax_126d_base_v043_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = _max(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmax_252d_base_v044_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = _max(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmax_504d_base_v045_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = _max(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmin_21d_base_v046_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = _min(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmin_63d_base_v047_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = _min(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmin_126d_base_v048_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = _min(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmin_252d_base_v049_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = _min(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of rolling correlation
def f03bc_f03_semi_basket_correlation_corrmin_504d_base_v050_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = _min(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrng_21d_base_v051_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = _max(c, 63) - _min(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrng_63d_base_v052_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = _max(c, 126) - _min(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrng_126d_base_v053_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = _max(c, 252) - _min(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrng_252d_base_v054_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = _max(c, 504) - _min(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of rolling correlation
def f03bc_f03_semi_basket_correlation_corrrng_504d_base_v055_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = _max(c, 756) - _min(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation position in rolling range
def f03bc_f03_semi_basket_correlation_corrpos_21d_base_v056_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    lo, hi = _min(c, 63), _max(c, 63)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation position in rolling range
def f03bc_f03_semi_basket_correlation_corrpos_63d_base_v057_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    lo, hi = _min(c, 126), _max(c, 126)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation position in rolling range
def f03bc_f03_semi_basket_correlation_corrpos_126d_base_v058_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    lo, hi = _min(c, 252), _max(c, 252)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation position in rolling range
def f03bc_f03_semi_basket_correlation_corrpos_252d_base_v059_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    lo, hi = _min(c, 504), _max(c, 504)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation position in rolling range
def f03bc_f03_semi_basket_correlation_corrpos_504d_base_v060_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    lo, hi = _min(c, 756), _max(c, 756)
    result = (c - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation drawdown from peak
def f03bc_f03_semi_basket_correlation_corrdd_21d_base_v061_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = c - _max(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation drawdown from peak
def f03bc_f03_semi_basket_correlation_corrdd_63d_base_v062_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = c - _max(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation drawdown from peak
def f03bc_f03_semi_basket_correlation_corrdd_126d_base_v063_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = c - _max(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation drawdown from peak
def f03bc_f03_semi_basket_correlation_corrdd_252d_base_v064_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = c - _max(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation drawdown from peak
def f03bc_f03_semi_basket_correlation_corrdd_504d_base_v065_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = c - _max(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation run-up from trough
def f03bc_f03_semi_basket_correlation_corrupt_21d_base_v066_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = c - _min(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation run-up from trough
def f03bc_f03_semi_basket_correlation_corrupt_63d_base_v067_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = c - _min(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation run-up from trough
def f03bc_f03_semi_basket_correlation_corrupt_126d_base_v068_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = c - _min(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation run-up from trough
def f03bc_f03_semi_basket_correlation_corrupt_252d_base_v069_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = c - _min(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation run-up from trough
def f03bc_f03_semi_basket_correlation_corrupt_504d_base_v070_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = c - _min(c, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of rolling correlation
def f03bc_f03_semi_basket_correlation_correma_5v21_base_v071_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 21)
    result = c.ewm(span=5, adjust=False).mean() - c.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of rolling correlation
def f03bc_f03_semi_basket_correlation_correma_21v63_base_v072_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 63)
    result = c.ewm(span=21, adjust=False).mean() - c.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of rolling correlation
def f03bc_f03_semi_basket_correlation_correma_63v126_base_v073_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 126)
    result = c.ewm(span=63, adjust=False).mean() - c.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of rolling correlation
def f03bc_f03_semi_basket_correlation_correma_126v252_base_v074_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 252)
    result = c.ewm(span=126, adjust=False).mean() - c.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of rolling correlation
def f03bc_f03_semi_basket_correlation_correma_252v504_base_v075_signal(closeadj, semi_basket_closeadj):
    o, b = _f03_own_ret(closeadj), _f03_own_ret(semi_basket_closeadj)
    c = _f03_roll_corr(o, b, 504)
    result = c.ewm(span=252, adjust=False).mean() - c.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


