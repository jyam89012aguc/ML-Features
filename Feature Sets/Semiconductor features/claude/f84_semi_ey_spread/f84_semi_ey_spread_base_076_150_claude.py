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


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


# ===== folder domain primitives =====
def _f84ey_own_ey(pe):
    return 1.0 / pe.replace(0, np.nan)


def _f84ey_spread(pe, sp500_ey_avg):
    return (1.0 / pe.replace(0, np.nan)) - sp500_ey_avg


def _f84ey_ratio(pe, sp500_ey_avg):
    return (1.0 / pe.replace(0, np.nan)) / sp500_ey_avg.replace(0, np.nan)


def _f84ey_log_ratio(pe, sp500_ey_avg):
    own = 1.0 / pe.replace(0, np.nan)
    return np.log(own.abs() / sp500_ey_avg.replace(0, np.nan).abs())


# 21d std of EY spread (spread vol)
def f84ey_f84_semi_ey_spread_spreadstd_21d_base_v076_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _std(sp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of EY spread (spread vol)
def f84ey_f84_semi_ey_spread_spreadstd_63d_base_v077_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _std(sp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of EY spread (spread vol)
def f84ey_f84_semi_ey_spread_spreadstd_126d_base_v078_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _std(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of EY spread (spread vol)
def f84ey_f84_semi_ey_spread_spreadstd_252d_base_v079_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _std(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of EY spread (spread vol)
def f84ey_f84_semi_ey_spread_spreadstd_504d_base_v080_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _std(sp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of EY spread
def f84ey_f84_semi_ey_spread_spreadskew_21d_base_v081_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of EY spread
def f84ey_f84_semi_ey_spread_spreadskew_63d_base_v082_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of EY spread
def f84ey_f84_semi_ey_spread_spreadskew_126d_base_v083_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of EY spread
def f84ey_f84_semi_ey_spread_spreadskew_252d_base_v084_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of EY spread
def f84ey_f84_semi_ey_spread_spreadskew_504d_base_v085_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of EY spread
def f84ey_f84_semi_ey_spread_spreadkurt_21d_base_v086_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of EY spread
def f84ey_f84_semi_ey_spread_spreadkurt_63d_base_v087_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of EY spread
def f84ey_f84_semi_ey_spread_spreadkurt_126d_base_v088_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of EY spread
def f84ey_f84_semi_ey_spread_spreadkurt_252d_base_v089_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of EY spread
def f84ey_f84_semi_ey_spread_spreadkurt_504d_base_v090_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of own_ey level
def f84ey_f84_semi_ey_spread_owneyz_21d_base_v091_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _z(own, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of own_ey level
def f84ey_f84_semi_ey_spread_owneyz_63d_base_v092_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _z(own, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of own_ey level
def f84ey_f84_semi_ey_spread_owneyz_126d_base_v093_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _z(own, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of own_ey level
def f84ey_f84_semi_ey_spread_owneyz_252d_base_v094_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _z(own, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of own_ey level
def f84ey_f84_semi_ey_spread_owneyz_504d_base_v095_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = _z(own, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of sp500_ey_avg level
def f84ey_f84_semi_ey_spread_spxeyz_21d_base_v096_signal(pe, sp500_ey_avg, closeadj):
    result = _z(sp500_ey_avg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of sp500_ey_avg level
def f84ey_f84_semi_ey_spread_spxeyz_63d_base_v097_signal(pe, sp500_ey_avg, closeadj):
    result = _z(sp500_ey_avg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of sp500_ey_avg level
def f84ey_f84_semi_ey_spread_spxeyz_126d_base_v098_signal(pe, sp500_ey_avg, closeadj):
    result = _z(sp500_ey_avg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of sp500_ey_avg level
def f84ey_f84_semi_ey_spread_spxeyz_252d_base_v099_signal(pe, sp500_ey_avg, closeadj):
    result = _z(sp500_ey_avg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of sp500_ey_avg level
def f84ey_f84_semi_ey_spread_spxeyz_504d_base_v100_signal(pe, sp500_ey_avg, closeadj):
    result = _z(sp500_ey_avg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EY spread conditional on SP500 EY rising
def f84ey_f84_semi_ey_spread_condrise_21d_base_v101_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    result = _mean(sp.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EY spread conditional on SP500 EY rising
def f84ey_f84_semi_ey_spread_condrise_63d_base_v102_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    result = _mean(sp.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EY spread conditional on SP500 EY rising
def f84ey_f84_semi_ey_spread_condrise_126d_base_v103_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    result = _mean(sp.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EY spread conditional on SP500 EY rising
def f84ey_f84_semi_ey_spread_condrise_252d_base_v104_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    result = _mean(sp.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EY spread conditional on SP500 EY rising
def f84ey_f84_semi_ey_spread_condrise_504d_base_v105_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() > 0
    result = _mean(sp.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EY spread conditional on SP500 EY falling
def f84ey_f84_semi_ey_spread_condfall_21d_base_v106_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    result = _mean(sp.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EY spread conditional on SP500 EY falling
def f84ey_f84_semi_ey_spread_condfall_63d_base_v107_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    result = _mean(sp.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EY spread conditional on SP500 EY falling
def f84ey_f84_semi_ey_spread_condfall_126d_base_v108_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    result = _mean(sp.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EY spread conditional on SP500 EY falling
def f84ey_f84_semi_ey_spread_condfall_252d_base_v109_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    result = _mean(sp.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EY spread conditional on SP500 EY falling
def f84ey_f84_semi_ey_spread_condfall_504d_base_v110_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    mask = sp500_ey_avg.diff() < 0
    result = _mean(sp.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in EY spread (diff)
def f84ey_f84_semi_ey_spread_spreaddiff_21d_base_v111_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in EY spread (diff)
def f84ey_f84_semi_ey_spread_spreaddiff_63d_base_v112_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in EY spread (diff)
def f84ey_f84_semi_ey_spread_spreaddiff_126d_base_v113_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in EY spread (diff)
def f84ey_f84_semi_ey_spread_spreaddiff_252d_base_v114_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in EY spread (diff)
def f84ey_f84_semi_ey_spread_spreaddiff_504d_base_v115_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sum of positive EY spread (cheaper days magnitude)
def f84ey_f84_semi_ey_spread_spreadpossum_21d_base_v116_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(lower=0).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of positive EY spread
def f84ey_f84_semi_ey_spread_spreadpossum_63d_base_v117_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(lower=0).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sum of positive EY spread
def f84ey_f84_semi_ey_spread_spreadpossum_126d_base_v118_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(lower=0).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of positive EY spread
def f84ey_f84_semi_ey_spread_spreadpossum_252d_base_v119_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(lower=0).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of positive EY spread
def f84ey_f84_semi_ey_spread_spreadpossum_504d_base_v120_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(lower=0).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sum of negative EY spread (expensive days magnitude)
def f84ey_f84_semi_ey_spread_spreadnegsum_21d_base_v121_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(upper=0).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of negative EY spread
def f84ey_f84_semi_ey_spread_spreadnegsum_63d_base_v122_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(upper=0).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sum of negative EY spread
def f84ey_f84_semi_ey_spread_spreadnegsum_126d_base_v123_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(upper=0).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of negative EY spread
def f84ey_f84_semi_ey_spread_spreadnegsum_252d_base_v124_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(upper=0).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of negative EY spread
def f84ey_f84_semi_ey_spread_spreadnegsum_504d_base_v125_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp.clip(upper=0).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EY spread minus its own short EMA (deviation)
def f84ey_f84_semi_ey_spread_spreaddev_21d_base_v126_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EY spread minus its 63d EMA
def f84ey_f84_semi_ey_spread_spreaddev_63d_base_v127_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EY spread minus its 126d EMA
def f84ey_f84_semi_ey_spread_spreaddev_126d_base_v128_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EY spread minus its 252d EMA
def f84ey_f84_semi_ey_spread_spreaddev_252d_base_v129_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EY spread minus its 504d EMA
def f84ey_f84_semi_ey_spread_spreaddev_504d_base_v130_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = sp - sp.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation of own_ey with sp500_ey
def f84ey_f84_semi_ey_spread_corr_21d_base_v131_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = own.rolling(21, min_periods=11).corr(sp500_ey_avg)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation of own_ey with sp500_ey
def f84ey_f84_semi_ey_spread_corr_63d_base_v132_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = own.rolling(63, min_periods=32).corr(sp500_ey_avg)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation of own_ey with sp500_ey
def f84ey_f84_semi_ey_spread_corr_126d_base_v133_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = own.rolling(126, min_periods=63).corr(sp500_ey_avg)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation of own_ey with sp500_ey
def f84ey_f84_semi_ey_spread_corr_252d_base_v134_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = own.rolling(252, min_periods=126).corr(sp500_ey_avg)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation of own_ey with sp500_ey
def f84ey_f84_semi_ey_spread_corr_504d_base_v135_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    result = own.rolling(504, min_periods=252).corr(sp500_ey_avg)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta of own_ey on sp500_ey
def f84ey_f84_semi_ey_spread_beta_21d_base_v136_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(21, min_periods=11).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(21, min_periods=11).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta of own_ey on sp500_ey
def f84ey_f84_semi_ey_spread_beta_63d_base_v137_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(63, min_periods=32).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(63, min_periods=32).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta of own_ey on sp500_ey
def f84ey_f84_semi_ey_spread_beta_126d_base_v138_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(126, min_periods=63).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(126, min_periods=63).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta of own_ey on sp500_ey
def f84ey_f84_semi_ey_spread_beta_252d_base_v139_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(252, min_periods=126).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(252, min_periods=126).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta of own_ey on sp500_ey
def f84ey_f84_semi_ey_spread_beta_504d_base_v140_signal(pe, sp500_ey_avg, closeadj):
    own = _f84ey_own_ey(pe)
    cov = own.rolling(504, min_periods=252).cov(sp500_ey_avg)
    var = sp500_ey_avg.rolling(504, min_periods=252).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z-score sum across short windows (21+63+126)
def f84ey_f84_semi_ey_spread_compshort_base_v141_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 21) + _z(sp, 63) + _z(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z-score sum across long windows (63+126+252)
def f84ey_f84_semi_ey_spread_complong_base_v142_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = _z(sp, 63) + _z(sp, 126) + _z(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# regime divergence: short EMA cross minus long EMA cross of EY spread
def f84ey_f84_semi_ey_spread_regimediv_base_v143_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    short = np.sign(sp.ewm(span=21, adjust=False).mean() - sp.ewm(span=63, adjust=False).mean())
    long = np.sign(sp.ewm(span=126, adjust=False).mean() - sp.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=sp.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EY spread half-life proxy (1 - lag1 autocorr)
def f84ey_f84_semi_ey_spread_halflife_21d_base_v144_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = 1.0 - sp.rolling(21, min_periods=11).corr(sp.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EY spread half-life proxy
def f84ey_f84_semi_ey_spread_halflife_63d_base_v145_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = 1.0 - sp.rolling(63, min_periods=32).corr(sp.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EY spread half-life proxy
def f84ey_f84_semi_ey_spread_halflife_126d_base_v146_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = 1.0 - sp.rolling(126, min_periods=63).corr(sp.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EY spread half-life proxy
def f84ey_f84_semi_ey_spread_halflife_252d_base_v147_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = 1.0 - sp.rolling(252, min_periods=126).corr(sp.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EY spread half-life proxy
def f84ey_f84_semi_ey_spread_halflife_504d_base_v148_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    result = 1.0 - sp.rolling(504, min_periods=252).corr(sp.shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EY spread quality (z * sign of regime)
def f84ey_f84_semi_ey_spread_quality_63d_base_v149_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    z = _z(sp, 63)
    regime = np.sign(sp.ewm(span=21, adjust=False).mean() - sp.ewm(span=63, adjust=False).mean())
    result = z * pd.Series(regime, index=sp.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EY spread quality (z * sign of long regime)
def f84ey_f84_semi_ey_spread_quality_252d_base_v150_signal(pe, sp500_ey_avg, closeadj):
    sp = _f84ey_spread(pe, sp500_ey_avg)
    z = _z(sp, 252)
    regime = np.sign(sp.ewm(span=126, adjust=False).mean() - sp.ewm(span=252, adjust=False).mean())
    result = z * pd.Series(regime, index=sp.index)
    return result.replace([np.inf, -np.inf], np.nan)
