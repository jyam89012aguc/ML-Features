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
def _f02_own_ret(s):
    return s.pct_change()


def _f02_roll_beta(own_r, bas_r, w):
    cov = own_r.rolling(w, min_periods=max(2, w // 2)).cov(bas_r)
    var = bas_r.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f02_roll_alpha(own_r, bas_r, w):
    beta = _f02_roll_beta(own_r, bas_r, w)
    return _mean(own_r, w) - beta * _mean(bas_r, w)


# 21d rolling beta vs semi basket
def f02bb_f02_semi_basket_beta_beta_21d_base_v001_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta vs semi basket
def f02bb_f02_semi_basket_beta_beta_63d_base_v002_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta vs semi basket
def f02bb_f02_semi_basket_beta_beta_126d_base_v003_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta vs semi basket
def f02bb_f02_semi_basket_beta_beta_252d_base_v004_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta vs semi basket
def f02bb_f02_semi_basket_beta_beta_504d_base_v005_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta minus 1 (over/under-basket beta)
def f02bb_f02_semi_basket_beta_betam1_21d_base_v006_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 21) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_63d_base_v007_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 63) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_126d_base_v008_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 126) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_252d_base_v009_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 252) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta minus 1
def f02bb_f02_semi_basket_beta_betam1_504d_base_v010_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    result = _f02_roll_beta(o, b, 504) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of rolling beta
def f02bb_f02_semi_basket_beta_betaz_21d_base_v011_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = _z(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of rolling beta
def f02bb_f02_semi_basket_beta_betaz_63d_base_v012_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = _z(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of rolling beta
def f02bb_f02_semi_basket_beta_betaz_126d_base_v013_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = _z(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of rolling beta
def f02bb_f02_semi_basket_beta_betaz_252d_base_v014_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = _z(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of rolling beta
def f02bb_f02_semi_basket_beta_betaz_504d_base_v015_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = _z(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of rolling beta
def f02bb_f02_semi_basket_beta_betarobustz_21d_base_v016_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    med = beta.rolling(63, min_periods=32).median()
    mad = (beta - med).abs().rolling(63, min_periods=32).median()
    result = (beta - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of rolling beta
def f02bb_f02_semi_basket_beta_betarobustz_63d_base_v017_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    med = beta.rolling(126, min_periods=63).median()
    mad = (beta - med).abs().rolling(126, min_periods=63).median()
    result = (beta - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of rolling beta
def f02bb_f02_semi_basket_beta_betarobustz_126d_base_v018_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    med = beta.rolling(252, min_periods=126).median()
    mad = (beta - med).abs().rolling(252, min_periods=126).median()
    result = (beta - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of rolling beta
def f02bb_f02_semi_basket_beta_betarobustz_252d_base_v019_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    med = beta.rolling(504, min_periods=252).median()
    mad = (beta - med).abs().rolling(504, min_periods=252).median()
    result = (beta - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of rolling beta
def f02bb_f02_semi_basket_beta_betarobustz_504d_base_v020_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    med = beta.rolling(756, min_periods=378).median()
    mad = (beta - med).abs().rolling(756, min_periods=378).median()
    result = (beta - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta vs its 63d mean (deviation)
def f02bb_f02_semi_basket_beta_betadev_21d_base_v021_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta - _mean(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta vs its 126d mean
def f02bb_f02_semi_basket_beta_betadev_63d_base_v022_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta - _mean(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta vs its 252d mean
def f02bb_f02_semi_basket_beta_betadev_126d_base_v023_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta - _mean(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta vs its 504d mean
def f02bb_f02_semi_basket_beta_betadev_252d_base_v024_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta - _mean(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta vs its 756d mean
def f02bb_f02_semi_basket_beta_betadev_504d_base_v025_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta - _mean(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of high-beta days (beta > 1)
def f02bb_f02_semi_basket_beta_betahi_21d_base_v026_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = (beta > 1.0).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of high-beta days
def f02bb_f02_semi_basket_beta_betahi_63d_base_v027_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = (beta > 1.0).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of high-beta days
def f02bb_f02_semi_basket_beta_betahi_126d_base_v028_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = (beta > 1.0).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-beta days
def f02bb_f02_semi_basket_beta_betahi_252d_base_v029_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = (beta > 1.0).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of high-beta days
def f02bb_f02_semi_basket_beta_betahi_504d_base_v030_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = (beta > 1.0).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of high-beta days (beta>1)
def f02bb_f02_semi_basket_beta_betahifrac_21d_base_v031_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = (beta > 1.0).astype(float).rolling(21, min_periods=11).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of high-beta days
def f02bb_f02_semi_basket_beta_betahifrac_63d_base_v032_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = (beta > 1.0).astype(float).rolling(63, min_periods=32).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of high-beta days
def f02bb_f02_semi_basket_beta_betahifrac_126d_base_v033_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = (beta > 1.0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of high-beta days
def f02bb_f02_semi_basket_beta_betahifrac_252d_base_v034_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = (beta > 1.0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of high-beta days
def f02bb_f02_semi_basket_beta_betahifrac_504d_base_v035_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = (beta > 1.0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of rolling beta (beta instability)
def f02bb_f02_semi_basket_beta_betastd_21d_base_v036_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = _std(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of rolling beta
def f02bb_f02_semi_basket_beta_betastd_63d_base_v037_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = _std(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of rolling beta
def f02bb_f02_semi_basket_beta_betastd_126d_base_v038_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = _std(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of rolling beta
def f02bb_f02_semi_basket_beta_betastd_252d_base_v039_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = _std(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of rolling beta
def f02bb_f02_semi_basket_beta_betastd_504d_base_v040_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = _std(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of rolling beta
def f02bb_f02_semi_basket_beta_betamax_21d_base_v041_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = _max(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of rolling beta
def f02bb_f02_semi_basket_beta_betamax_63d_base_v042_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = _max(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of rolling beta
def f02bb_f02_semi_basket_beta_betamax_126d_base_v043_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = _max(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of rolling beta
def f02bb_f02_semi_basket_beta_betamax_252d_base_v044_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = _max(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of rolling beta
def f02bb_f02_semi_basket_beta_betamax_504d_base_v045_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = _max(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of rolling beta
def f02bb_f02_semi_basket_beta_betamin_21d_base_v046_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = _min(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of rolling beta
def f02bb_f02_semi_basket_beta_betamin_63d_base_v047_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = _min(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of rolling beta
def f02bb_f02_semi_basket_beta_betamin_126d_base_v048_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = _min(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of rolling beta
def f02bb_f02_semi_basket_beta_betamin_252d_base_v049_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = _min(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of rolling beta
def f02bb_f02_semi_basket_beta_betamin_504d_base_v050_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = _min(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of rolling beta
def f02bb_f02_semi_basket_beta_betarng_21d_base_v051_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = _max(beta, 63) - _min(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of rolling beta
def f02bb_f02_semi_basket_beta_betarng_63d_base_v052_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = _max(beta, 126) - _min(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of rolling beta
def f02bb_f02_semi_basket_beta_betarng_126d_base_v053_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = _max(beta, 252) - _min(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of rolling beta
def f02bb_f02_semi_basket_beta_betarng_252d_base_v054_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = _max(beta, 504) - _min(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of rolling beta
def f02bb_f02_semi_basket_beta_betarng_504d_base_v055_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = _max(beta, 756) - _min(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta position in rolling range
def f02bb_f02_semi_basket_beta_betapos_21d_base_v056_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    lo, hi = _min(beta, 63), _max(beta, 63)
    result = (beta - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta position in rolling range
def f02bb_f02_semi_basket_beta_betapos_63d_base_v057_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    lo, hi = _min(beta, 126), _max(beta, 126)
    result = (beta - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta position in rolling range
def f02bb_f02_semi_basket_beta_betapos_126d_base_v058_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    lo, hi = _min(beta, 252), _max(beta, 252)
    result = (beta - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta position in rolling range
def f02bb_f02_semi_basket_beta_betapos_252d_base_v059_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    lo, hi = _min(beta, 504), _max(beta, 504)
    result = (beta - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta position in rolling range
def f02bb_f02_semi_basket_beta_betapos_504d_base_v060_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    lo, hi = _min(beta, 756), _max(beta, 756)
    result = (beta - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_21d_base_v061_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta - _max(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_63d_base_v062_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta - _max(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_126d_base_v063_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta - _max(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_252d_base_v064_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta - _max(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta drawdown from peak
def f02bb_f02_semi_basket_beta_betadd_504d_base_v065_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta - _max(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta run-up from trough
def f02bb_f02_semi_basket_beta_betaup_21d_base_v066_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta - _min(beta, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta run-up from trough
def f02bb_f02_semi_basket_beta_betaup_63d_base_v067_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta - _min(beta, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta run-up from trough
def f02bb_f02_semi_basket_beta_betaup_126d_base_v068_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta - _min(beta, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta run-up from trough
def f02bb_f02_semi_basket_beta_betaup_252d_base_v069_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta - _min(beta, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta run-up from trough
def f02bb_f02_semi_basket_beta_betaup_504d_base_v070_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta - _min(beta, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 5v21 EMA crossover of rolling beta
def f02bb_f02_semi_basket_beta_betaema_5v21_base_v071_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 21)
    result = beta.ewm(span=5, adjust=False).mean() - beta.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 EMA crossover of rolling beta
def f02bb_f02_semi_basket_beta_betaema_21v63_base_v072_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 63)
    result = beta.ewm(span=21, adjust=False).mean() - beta.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63v126 EMA crossover of rolling beta
def f02bb_f02_semi_basket_beta_betaema_63v126_base_v073_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 126)
    result = beta.ewm(span=63, adjust=False).mean() - beta.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 EMA crossover of rolling beta
def f02bb_f02_semi_basket_beta_betaema_126v252_base_v074_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 252)
    result = beta.ewm(span=126, adjust=False).mean() - beta.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 EMA crossover of rolling beta
def f02bb_f02_semi_basket_beta_betaema_252v504_base_v075_signal(closeadj, semi_basket_closeadj):
    o, b = _f02_own_ret(closeadj), _f02_own_ret(semi_basket_closeadj)
    beta = _f02_roll_beta(o, b, 504)
    result = beta.ewm(span=252, adjust=False).mean() - beta.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
