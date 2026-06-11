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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


# ===== folder domain primitives =====
def _f07_price_ma(close, w):
    # simple moving average of price over window w
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f07_above_ma_dist(close, w):
    # distance of price above SMA in percent terms
    ma = _f07_price_ma(close, w)
    return (close - ma) / ma.replace(0, np.nan).abs()


def _f07_above_ma_atr(close, high, low, w):
    # distance of price above SMA in ATR units
    ma = _f07_price_ma(close, w)
    atr = (high - low).rolling(21, min_periods=5).mean()
    return (close - ma) / atr.replace(0, np.nan)


# 5d jerk of 5d SMA distance
def f07pma_f07_price_moving_averages_dist_5d_jerk_v001_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 5) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d SMA distance
def f07pma_f07_price_moving_averages_dist_21d_jerk_v002_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d SMA distance
def f07pma_f07_price_moving_averages_dist_21d_jerk_v003_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 63d SMA distance
def f07pma_f07_price_moving_averages_dist_63d_jerk_v004_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d SMA distance
def f07pma_f07_price_moving_averages_dist_63d_jerk_v005_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d SMA distance
def f07pma_f07_price_moving_averages_dist_63d_jerk_v006_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d SMA distance
def f07pma_f07_price_moving_averages_dist_126d_jerk_v007_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d SMA distance
def f07pma_f07_price_moving_averages_dist_126d_jerk_v008_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d SMA distance
def f07pma_f07_price_moving_averages_dist_252d_jerk_v009_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d SMA distance
def f07pma_f07_price_moving_averages_dist_252d_jerk_v010_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d SMA distance
def f07pma_f07_price_moving_averages_dist_504d_jerk_v011_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d SMA distance
def f07pma_f07_price_moving_averages_dist_504d_jerk_v012_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d SMA price level
def f07pma_f07_price_moving_averages_smaprice_21d_jerk_v013_signal(closeadj):
    base = _f07_price_ma(closeadj, 21)
    slope = _slope_pct(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d SMA price level
def f07pma_f07_price_moving_averages_smaprice_63d_jerk_v014_signal(closeadj):
    base = _f07_price_ma(closeadj, 63)
    slope = _slope_pct(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d SMA price level
def f07pma_f07_price_moving_averages_smaprice_126d_jerk_v015_signal(closeadj):
    base = _f07_price_ma(closeadj, 126)
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d SMA price level
def f07pma_f07_price_moving_averages_smaprice_252d_jerk_v016_signal(closeadj):
    base = _f07_price_ma(closeadj, 252)
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d SMA price level
def f07pma_f07_price_moving_averages_smaprice_504d_jerk_v017_signal(closeadj):
    base = _f07_price_ma(closeadj, 504)
    slope = _slope_pct(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ratio price/SMA
def f07pma_f07_price_moving_averages_ratio_21d_jerk_v018_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    base = (closeadj / ma.replace(0, np.nan)) * closeadj
    slope = _slope_pct(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ratio price/SMA
def f07pma_f07_price_moving_averages_ratio_63d_jerk_v019_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    base = (closeadj / ma.replace(0, np.nan)) * closeadj
    slope = _slope_pct(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ratio price/SMA
def f07pma_f07_price_moving_averages_ratio_252d_jerk_v020_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    base = (closeadj / ma.replace(0, np.nan)) * closeadj
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ratio
def f07pma_f07_price_moving_averages_ratio_504d_jerk_v021_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    base = (closeadj / ma.replace(0, np.nan)) * closeadj
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d log-ratio
def f07pma_f07_price_moving_averages_logratio_21d_jerk_v022_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    base = np.log((closeadj / ma.replace(0, np.nan)).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d log-ratio
def f07pma_f07_price_moving_averages_logratio_63d_jerk_v023_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    base = np.log((closeadj / ma.replace(0, np.nan)).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d log-ratio
def f07pma_f07_price_moving_averages_logratio_252d_jerk_v024_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    base = np.log((closeadj / ma.replace(0, np.nan)).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d log-ratio
def f07pma_f07_price_moving_averages_logratio_504d_jerk_v025_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    base = np.log((closeadj / ma.replace(0, np.nan)).replace(0, np.nan)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ATR distance
def f07pma_f07_price_moving_averages_distatr_21d_jerk_v026_signal(closeadj, high, low):
    base = _f07_above_ma_atr(closeadj, high, low, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR distance
def f07pma_f07_price_moving_averages_distatr_63d_jerk_v027_signal(closeadj, high, low):
    base = _f07_above_ma_atr(closeadj, high, low, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d ATR distance
def f07pma_f07_price_moving_averages_distatr_126d_jerk_v028_signal(closeadj, high, low):
    base = _f07_above_ma_atr(closeadj, high, low, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR distance
def f07pma_f07_price_moving_averages_distatr_252d_jerk_v029_signal(closeadj, high, low):
    base = _f07_above_ma_atr(closeadj, high, low, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d ATR distance
def f07pma_f07_price_moving_averages_distatr_504d_jerk_v030_signal(closeadj, high, low):
    base = _f07_above_ma_atr(closeadj, high, low, 504) * closeadj
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (21d - 252d) distance ratio
def f07pma_f07_price_moving_averages_distratio_21v252_jerk_v031_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 21)
    b = _f07_above_ma_dist(closeadj, 252)
    base = (a - b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (63d - 252d) distance diff
def f07pma_f07_price_moving_averages_distdiff_63m252_jerk_v032_signal(closeadj):
    base = (_f07_above_ma_dist(closeadj, 63) - _f07_above_ma_dist(closeadj, 252)) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of (21d - 63d) distance diff
def f07pma_f07_price_moving_averages_distdiff_21m63_jerk_v033_signal(closeadj):
    base = (_f07_above_ma_dist(closeadj, 21) - _f07_above_ma_dist(closeadj, 63)) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (252d - 504d) distance diff
def f07pma_f07_price_moving_averages_distdiff_252m504_jerk_v034_signal(closeadj):
    base = (_f07_above_ma_dist(closeadj, 252) - _f07_above_ma_dist(closeadj, 504)) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance squared
def f07pma_f07_price_moving_averages_distsq_21d_jerk_v035_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d * d.abs() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance squared
def f07pma_f07_price_moving_averages_distsq_63d_jerk_v036_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d * d.abs() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance squared
def f07pma_f07_price_moving_averages_distsq_252d_jerk_v037_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    base = d * d.abs() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d distance squared
def f07pma_f07_price_moving_averages_distsq_504d_jerk_v038_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 504)
    base = d * d.abs() * closeadj
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × price
def f07pma_f07_price_moving_averages_distxprice_21d_jerk_v039_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 21) * closeadj * closeadj
    slope = _slope_pct(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × price
def f07pma_f07_price_moving_averages_distxprice_252d_jerk_v040_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 252) * closeadj * closeadj
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d distance × price
def f07pma_f07_price_moving_averages_distxprice_504d_jerk_v041_signal(closeadj):
    base = _f07_above_ma_dist(closeadj, 504) * closeadj * closeadj
    slope = _slope_pct(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d distance z-score over 63d
def f07pma_f07_price_moving_averages_distz_63d_jerk_v042_signal(closeadj):
    base = _z(_f07_above_ma_dist(closeadj, 21), 63) * closeadj
    slope = _diff(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d distance z-score over 252d
def f07pma_f07_price_moving_averages_distz_252d_jerk_v043_signal(closeadj):
    base = _z(_f07_above_ma_dist(closeadj, 63), 252) * closeadj
    slope = _diff(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance z-score over 504d
def f07pma_f07_price_moving_averages_distz_504d_jerk_v044_signal(closeadj):
    base = _z(_f07_above_ma_dist(closeadj, 252), 504) * closeadj
    slope = _diff(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d-window mean of 21d distance
def f07pma_f07_price_moving_averages_distmean_63d_jerk_v045_signal(closeadj):
    base = _mean(_f07_above_ma_dist(closeadj, 21), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d-window mean of 63d distance
def f07pma_f07_price_moving_averages_distmean_252d_jerk_v046_signal(closeadj):
    base = _mean(_f07_above_ma_dist(closeadj, 63), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance std
def f07pma_f07_price_moving_averages_diststd_63d_jerk_v047_signal(closeadj):
    base = _std(_f07_above_ma_dist(closeadj, 21), 63) * closeadj
    slope = _slope_pct(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance std
def f07pma_f07_price_moving_averages_diststd_252d_jerk_v048_signal(closeadj):
    base = _std(_f07_above_ma_dist(closeadj, 63), 252) * closeadj
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d above-ratio
def f07pma_f07_price_moving_averages_aboveratio_21d_jerk_v049_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 21) > 0).astype(float)
    base = flag.rolling(21, min_periods=5).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d above-ratio
def f07pma_f07_price_moving_averages_aboveratio_63d_jerk_v050_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 63) > 0).astype(float)
    base = flag.rolling(63, min_periods=21).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d above-ratio
def f07pma_f07_price_moving_averages_aboveratio_252d_jerk_v051_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 252) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d above-ratio
def f07pma_f07_price_moving_averages_aboveratio_504d_jerk_v052_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 504) > 0).astype(float)
    base = flag.rolling(504, min_periods=126).mean() * closeadj
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d distance × retvol
def f07pma_f07_price_moving_averages_distxretvol_21d_jerk_v053_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f07_above_ma_dist(closeadj, 21) * rv * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × retvol
def f07pma_f07_price_moving_averages_distxretvol_63d_jerk_v054_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f07_above_ma_dist(closeadj, 63) * rv * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × retvol
def f07pma_f07_price_moving_averages_distxretvol_252d_jerk_v055_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f07_above_ma_dist(closeadj, 252) * rv * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × volume z-score
def f07pma_f07_price_moving_averages_distxvolz_21d_jerk_v056_signal(closeadj, volume):
    base = _f07_above_ma_dist(closeadj, 21) * _z(volume, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × volume z-score
def f07pma_f07_price_moving_averages_distxvolz_63d_jerk_v057_signal(closeadj, volume):
    base = _f07_above_ma_dist(closeadj, 63) * _z(volume, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × dollar volume mean
def f07pma_f07_price_moving_averages_distxdv_252d_jerk_v058_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f07_above_ma_dist(closeadj, 252) * _mean(dv, 21)
    slope = _slope_pct(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d SMA spread
def f07pma_f07_price_moving_averages_spread_21d_jerk_v059_signal(closeadj):
    base = closeadj - _f07_price_ma(closeadj, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d SMA spread
def f07pma_f07_price_moving_averages_spread_63d_jerk_v060_signal(closeadj):
    base = closeadj - _f07_price_ma(closeadj, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d SMA spread
def f07pma_f07_price_moving_averages_spread_126d_jerk_v061_signal(closeadj):
    base = closeadj - _f07_price_ma(closeadj, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d SMA spread
def f07pma_f07_price_moving_averages_spread_252d_jerk_v062_signal(closeadj):
    base = closeadj - _f07_price_ma(closeadj, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d SMA spread
def f07pma_f07_price_moving_averages_spread_504d_jerk_v063_signal(closeadj):
    base = closeadj - _f07_price_ma(closeadj, 504)
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21v63 fan-out
def f07pma_f07_price_moving_averages_fanout_21v63_jerk_v064_signal(closeadj):
    f = _f07_price_ma(closeadj, 21) - _f07_price_ma(closeadj, 63)
    base = f * closeadj / _f07_price_ma(closeadj, 63).replace(0, np.nan)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v126 fan-out
def f07pma_f07_price_moving_averages_fanout_21v126_jerk_v065_signal(closeadj):
    f = _f07_price_ma(closeadj, 21) - _f07_price_ma(closeadj, 126)
    base = f * closeadj / _f07_price_ma(closeadj, 126).replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63v126 fan-out
def f07pma_f07_price_moving_averages_fanout_63v126_jerk_v066_signal(closeadj):
    f = _f07_price_ma(closeadj, 63) - _f07_price_ma(closeadj, 126)
    base = f * closeadj / _f07_price_ma(closeadj, 126).replace(0, np.nan)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 fan-out
def f07pma_f07_price_moving_averages_fanout_63v252_jerk_v067_signal(closeadj):
    f = _f07_price_ma(closeadj, 63) - _f07_price_ma(closeadj, 252)
    base = f * closeadj / _f07_price_ma(closeadj, 252).replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126v252 fan-out
def f07pma_f07_price_moving_averages_fanout_126v252_jerk_v068_signal(closeadj):
    f = _f07_price_ma(closeadj, 126) - _f07_price_ma(closeadj, 252)
    base = f * closeadj / _f07_price_ma(closeadj, 252).replace(0, np.nan)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252v504 fan-out
def f07pma_f07_price_moving_averages_fanout_252v504_jerk_v069_signal(closeadj):
    f = _f07_price_ma(closeadj, 252) - _f07_price_ma(closeadj, 504)
    base = f * closeadj / _f07_price_ma(closeadj, 504).replace(0, np.nan)
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d-window distance max
def f07pma_f07_price_moving_averages_distmax_63d_jerk_v070_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d.rolling(63, min_periods=21).max() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d-window distance min
def f07pma_f07_price_moving_averages_distmin_252d_jerk_v071_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d.rolling(252, min_periods=63).min() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d-window distance sum
def f07pma_f07_price_moving_averages_distsum_63d_jerk_v072_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d.rolling(63, min_periods=21).sum() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d-window distance sum
def f07pma_f07_price_moving_averages_distsum_252d_jerk_v073_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d.rolling(252, min_periods=63).sum() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d distance pct rank
def f07pma_f07_price_moving_averages_distpct_252d_jerk_v074_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d.rolling(252, min_periods=63).rank(pct=True) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d distance pct rank
def f07pma_f07_price_moving_averages_distpct_504d_jerk_v075_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d.rolling(504, min_periods=126).rank(pct=True) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × intraday range
def f07pma_f07_price_moving_averages_distxrange_21d_jerk_v076_signal(closeadj, high, low):
    rng = (high - low)
    base = _f07_above_ma_dist(closeadj, 21) * rng * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × ATR
def f07pma_f07_price_moving_averages_distxatr_63d_jerk_v077_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f07_above_ma_dist(closeadj, 63) * atr * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × ATR
def f07pma_f07_price_moving_averages_distxatr_252d_jerk_v078_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f07_above_ma_dist(closeadj, 252) * atr * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d EMA distance
def f07pma_f07_price_moving_averages_emadist_21d_jerk_v079_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs() * closeadj + _f07_above_ma_dist(closeadj, 21) * 0.0
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EMA distance
def f07pma_f07_price_moving_averages_emadist_63d_jerk_v080_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs() * closeadj + _f07_above_ma_dist(closeadj, 63) * 0.0
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d EMA distance
def f07pma_f07_price_moving_averages_emadist_126d_jerk_v081_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=63, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs() * closeadj + _f07_above_ma_dist(closeadj, 126) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EMA distance
def f07pma_f07_price_moving_averages_emadist_252d_jerk_v082_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs() * closeadj + _f07_above_ma_dist(closeadj, 252) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d EMA distance
def f07pma_f07_price_moving_averages_emadist_504d_jerk_v083_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs() * closeadj + _f07_above_ma_dist(closeadj, 504) * 0.0
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d composite distance
def f07pma_f07_price_moving_averages_distmulti_21d_jerk_v084_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 5)
    b = _f07_above_ma_dist(closeadj, 21)
    base = (a + b) * closeadj * 0.5
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d composite distance
def f07pma_f07_price_moving_averages_distmulti_63d_jerk_v085_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 21)
    b = _f07_above_ma_dist(closeadj, 63)
    base = (a + b) * closeadj * 0.5
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d composite distance
def f07pma_f07_price_moving_averages_distmulti_252d_jerk_v086_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 63)
    b = _f07_above_ma_dist(closeadj, 126)
    c = _f07_above_ma_dist(closeadj, 252)
    base = (a + b + c) * closeadj / 3.0
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d composite distance
def f07pma_f07_price_moving_averages_distmulti_504d_jerk_v087_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 126)
    b = _f07_above_ma_dist(closeadj, 252)
    c = _f07_above_ma_dist(closeadj, 504)
    base = (a + b + c) * closeadj / 3.0
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d SMA slope
def f07pma_f07_price_moving_averages_smaslope_21d_jerk_v088_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    base = (ma - ma.shift(5)) / ma.replace(0, np.nan).abs() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d SMA slope
def f07pma_f07_price_moving_averages_smaslope_63d_jerk_v089_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    base = (ma - ma.shift(21)) / ma.replace(0, np.nan).abs() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d SMA slope
def f07pma_f07_price_moving_averages_smaslope_252d_jerk_v090_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    base = (ma - ma.shift(63)) / ma.replace(0, np.nan).abs() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d SMA slope
def f07pma_f07_price_moving_averages_smaslope_504d_jerk_v091_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    base = (ma - ma.shift(126)) / ma.replace(0, np.nan).abs() * closeadj
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × 5d return
def f07pma_f07_price_moving_averages_distxret_5d_jerk_v092_signal(closeadj):
    r5 = closeadj.pct_change(5)
    base = _f07_above_ma_dist(closeadj, 21) * r5 * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × 21d return
def f07pma_f07_price_moving_averages_distxret_21d_jerk_v093_signal(closeadj):
    r21 = closeadj.pct_change(21)
    base = _f07_above_ma_dist(closeadj, 63) * r21 * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × 63d return
def f07pma_f07_price_moving_averages_distxret_63d_jerk_v094_signal(closeadj):
    r63 = closeadj.pct_change(63)
    base = _f07_above_ma_dist(closeadj, 252) * r63 * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d distance × 252d return
def f07pma_f07_price_moving_averages_distxret_252d_jerk_v095_signal(closeadj):
    r252 = closeadj.pct_change(252)
    base = _f07_above_ma_dist(closeadj, 504) * r252 * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × skewness
def f07pma_f07_price_moving_averages_distxskew_63d_jerk_v096_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f07_above_ma_dist(closeadj, 63) * sk * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × skewness
def f07pma_f07_price_moving_averages_distxskew_252d_jerk_v097_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f07_above_ma_dist(closeadj, 252) * sk * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × kurtosis
def f07pma_f07_price_moving_averages_distxkurt_63d_jerk_v098_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f07_above_ma_dist(closeadj, 63) * kt * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × kurtosis
def f07pma_f07_price_moving_averages_distxkurt_252d_jerk_v099_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f07_above_ma_dist(closeadj, 252) * kt * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of expanding distance
def f07pma_f07_price_moving_averages_distexp_252d_jerk_v100_signal(closeadj):
    ma = closeadj.expanding(min_periods=21).mean()
    base = (closeadj - ma) / ma.replace(0, np.nan).abs() * closeadj + _f07_above_ma_dist(closeadj, 252) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_5d_jerk_v101_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f07_above_ma_dist(closeadj, 5) * dv
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_21d_jerk_v102_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f07_above_ma_dist(closeadj, 21) * dv
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_63d_jerk_v103_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f07_above_ma_dist(closeadj, 63) * dv
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_504d_jerk_v104_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f07_above_ma_dist(closeadj, 504) * dv
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ATR distance × 5d return
def f07pma_f07_price_moving_averages_distatrxret_21d_jerk_v105_signal(closeadj, high, low):
    r = closeadj.pct_change(5)
    base = _f07_above_ma_atr(closeadj, high, low, 21) * r * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR distance × 21d return
def f07pma_f07_price_moving_averages_distatrxret_63d_jerk_v106_signal(closeadj, high, low):
    r = closeadj.pct_change(21)
    base = _f07_above_ma_atr(closeadj, high, low, 63) * r * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d ATR distance × 252d return
def f07pma_f07_price_moving_averages_distatrxret_504d_jerk_v107_signal(closeadj, high, low):
    r = closeadj.pct_change(252)
    base = _f07_above_ma_atr(closeadj, high, low, 504) * r * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d above-run-count
def f07pma_f07_price_moving_averages_aboveruncts_21d_jerk_v108_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 21) > 0).astype(float)
    base = flag.rolling(63, min_periods=21).sum() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d above-run-count
def f07pma_f07_price_moving_averages_aboveruncts_63d_jerk_v109_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 63) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d above-run-count
def f07pma_f07_price_moving_averages_aboveruncts_252d_jerk_v110_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 252) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d above-run-count
def f07pma_f07_price_moving_averages_aboveruncts_504d_jerk_v111_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 504) > 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj
    slope = _slope_diff_norm(base, 126)
    result = _diff(slope, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × overnight gap
def f07pma_f07_price_moving_averages_distxocgap_21d_jerk_v112_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f07_above_ma_dist(closeadj, 21) * gap * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × overnight gap
def f07pma_f07_price_moving_averages_distxocgap_63d_jerk_v113_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f07_above_ma_dist(closeadj, 63) * gap * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × gap z-score
def f07pma_f07_price_moving_averages_distxgapz_252d_jerk_v114_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f07_above_ma_dist(closeadj, 252) * _z(gap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × intraday range
def f07pma_f07_price_moving_averages_distxintraday_21d_jerk_v115_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan).abs()
    base = _f07_above_ma_dist(closeadj, 21) * rng * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × intraday range
def f07pma_f07_price_moving_averages_distxintraday_63d_jerk_v116_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan).abs()
    base = _f07_above_ma_dist(closeadj, 63) * rng * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × intraday range mean
def f07pma_f07_price_moving_averages_distxintraday_252d_jerk_v117_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan).abs()
    base = _f07_above_ma_dist(closeadj, 252) * _mean(rng, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance min over 21d
def f07pma_f07_price_moving_averages_distminw_21d_jerk_v118_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d.rolling(21, min_periods=5).min() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance min
def f07pma_f07_price_moving_averages_distminw_63d_jerk_v119_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d.rolling(63, min_periods=21).min() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance min
def f07pma_f07_price_moving_averages_distminw_252d_jerk_v120_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    base = d.rolling(252, min_periods=63).min() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance max
def f07pma_f07_price_moving_averages_distmaxw_21d_jerk_v121_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d.rolling(21, min_periods=5).max() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance max
def f07pma_f07_price_moving_averages_distmaxw_63d_jerk_v122_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d.rolling(63, min_periods=21).max() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance max
def f07pma_f07_price_moving_averages_distmaxw_252d_jerk_v123_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    base = d.rolling(252, min_periods=63).max() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance range
def f07pma_f07_price_moving_averages_distrange_21d_jerk_v124_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = (d.rolling(21, min_periods=5).max() - d.rolling(21, min_periods=5).min()) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance range
def f07pma_f07_price_moving_averages_distrange_63d_jerk_v125_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = (d.rolling(63, min_periods=21).max() - d.rolling(63, min_periods=21).min()) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance range
def f07pma_f07_price_moving_averages_distrange_252d_jerk_v126_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    base = (d.rolling(252, min_periods=63).max() - d.rolling(252, min_periods=63).min()) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ATR distance × volume z-score
def f07pma_f07_price_moving_averages_distatrxvolz_21d_jerk_v127_signal(closeadj, high, low, volume):
    base = _f07_above_ma_atr(closeadj, high, low, 21) * _z(volume, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR distance × volume z-score
def f07pma_f07_price_moving_averages_distatrxvolz_63d_jerk_v128_signal(closeadj, high, low, volume):
    base = _f07_above_ma_atr(closeadj, high, low, 63) * _z(volume, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR distance × volume z-score
def f07pma_f07_price_moving_averages_distatrxvolz_252d_jerk_v129_signal(closeadj, high, low, volume):
    base = _f07_above_ma_atr(closeadj, high, low, 252) * _z(volume, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × abs return
def f07pma_f07_price_moving_averages_distxabsret_21d_jerk_v130_signal(closeadj):
    ar = closeadj.pct_change().abs()
    base = _f07_above_ma_dist(closeadj, 21) * ar * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × mean abs return
def f07pma_f07_price_moving_averages_distxabsret_63d_jerk_v131_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    base = _f07_above_ma_dist(closeadj, 63) * ar * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × mean abs return
def f07pma_f07_price_moving_averages_distxabsret_252d_jerk_v132_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    base = _f07_above_ma_dist(closeadj, 252) * ar * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d distance × volume change
def f07pma_f07_price_moving_averages_distxvolch_21d_jerk_v133_signal(closeadj, volume):
    vc = volume.pct_change(21)
    base = _f07_above_ma_dist(closeadj, 21) * vc * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × volume change
def f07pma_f07_price_moving_averages_distxvolch_63d_jerk_v134_signal(closeadj, volume):
    vc = volume.pct_change(63)
    base = _f07_above_ma_dist(closeadj, 63) * vc * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × volume change
def f07pma_f07_price_moving_averages_distxvolch_252d_jerk_v135_signal(closeadj, volume):
    vc = volume.pct_change(252)
    base = _f07_above_ma_dist(closeadj, 252) * vc * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d SMA spread × ATR
def f07pma_f07_price_moving_averages_spreadxatr_21d_jerk_v136_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    spread = closeadj - _f07_price_ma(closeadj, 21)
    base = (spread * atr) + _f07_above_ma_dist(closeadj, 21) * 0.0
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d SMA spread × ATR
def f07pma_f07_price_moving_averages_spreadxatr_63d_jerk_v137_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    spread = closeadj - _f07_price_ma(closeadj, 63)
    base = (spread * atr) + _f07_above_ma_dist(closeadj, 63) * 0.0
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d SMA spread × ATR
def f07pma_f07_price_moving_averages_spreadxatr_252d_jerk_v138_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    spread = closeadj - _f07_price_ma(closeadj, 252)
    base = (spread * atr) + _f07_above_ma_dist(closeadj, 252) * 0.0
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d/252d distance ratio
def f07pma_f07_price_moving_averages_distrelratio_21v252_jerk_v139_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 21)
    b = _f07_above_ma_dist(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d/504d distance ratio
def f07pma_f07_price_moving_averages_distrelratio_63v504_jerk_v140_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 63)
    b = _f07_above_ma_dist(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d distance × 21d std
def f07pma_f07_price_moving_averages_distxstd_21d_jerk_v141_signal(closeadj):
    s = _std(closeadj.pct_change(), 21)
    base = _f07_above_ma_dist(closeadj, 21) * s * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance × 63d std
def f07pma_f07_price_moving_averages_distxstd_63d_jerk_v142_signal(closeadj):
    s = _std(closeadj.pct_change(), 63)
    base = _f07_above_ma_dist(closeadj, 63) * s * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × 252d std
def f07pma_f07_price_moving_averages_distxstd_252d_jerk_v143_signal(closeadj):
    s = _std(closeadj.pct_change(), 252)
    base = _f07_above_ma_dist(closeadj, 252) * s * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d distance integral × price
def f07pma_f07_price_moving_averages_distintegxprice_21d_jerk_v144_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    base = d.rolling(63, min_periods=21).sum() * closeadj * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance integral × price
def f07pma_f07_price_moving_averages_distintegxprice_63d_jerk_v145_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    base = d.rolling(252, min_periods=63).sum() * closeadj * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d distance × 252d mean return
def f07pma_f07_price_moving_averages_distxretmean_252d_jerk_v146_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 252)
    base = _f07_above_ma_dist(closeadj, 252) * rmean * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ATR distance × dollar volume
def f07pma_f07_price_moving_averages_distatrxdv_21d_jerk_v147_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f07_above_ma_atr(closeadj, high, low, 21) * dv
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ATR distance × dollar volume
def f07pma_f07_price_moving_averages_distatrxdv_63d_jerk_v148_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f07_above_ma_atr(closeadj, high, low, 63) * dv
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ATR distance × dollar-volume mean
def f07pma_f07_price_moving_averages_distatrxdv_252d_jerk_v149_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    base = _f07_above_ma_atr(closeadj, high, low, 252) * _mean(dv, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (21d-252d) composite × ATR
def f07pma_f07_price_moving_averages_composite_21v252_jerk_v150_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    diff = _f07_above_ma_dist(closeadj, 21) - _f07_above_ma_dist(closeadj, 252)
    base = diff * closeadj * atr
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07pma_f07_price_moving_averages_dist_5d_jerk_v001_signal,
    f07pma_f07_price_moving_averages_dist_21d_jerk_v002_signal,
    f07pma_f07_price_moving_averages_dist_21d_jerk_v003_signal,
    f07pma_f07_price_moving_averages_dist_63d_jerk_v004_signal,
    f07pma_f07_price_moving_averages_dist_63d_jerk_v005_signal,
    f07pma_f07_price_moving_averages_dist_63d_jerk_v006_signal,
    f07pma_f07_price_moving_averages_dist_126d_jerk_v007_signal,
    f07pma_f07_price_moving_averages_dist_126d_jerk_v008_signal,
    f07pma_f07_price_moving_averages_dist_252d_jerk_v009_signal,
    f07pma_f07_price_moving_averages_dist_252d_jerk_v010_signal,
    f07pma_f07_price_moving_averages_dist_504d_jerk_v011_signal,
    f07pma_f07_price_moving_averages_dist_504d_jerk_v012_signal,
    f07pma_f07_price_moving_averages_smaprice_21d_jerk_v013_signal,
    f07pma_f07_price_moving_averages_smaprice_63d_jerk_v014_signal,
    f07pma_f07_price_moving_averages_smaprice_126d_jerk_v015_signal,
    f07pma_f07_price_moving_averages_smaprice_252d_jerk_v016_signal,
    f07pma_f07_price_moving_averages_smaprice_504d_jerk_v017_signal,
    f07pma_f07_price_moving_averages_ratio_21d_jerk_v018_signal,
    f07pma_f07_price_moving_averages_ratio_63d_jerk_v019_signal,
    f07pma_f07_price_moving_averages_ratio_252d_jerk_v020_signal,
    f07pma_f07_price_moving_averages_ratio_504d_jerk_v021_signal,
    f07pma_f07_price_moving_averages_logratio_21d_jerk_v022_signal,
    f07pma_f07_price_moving_averages_logratio_63d_jerk_v023_signal,
    f07pma_f07_price_moving_averages_logratio_252d_jerk_v024_signal,
    f07pma_f07_price_moving_averages_logratio_504d_jerk_v025_signal,
    f07pma_f07_price_moving_averages_distatr_21d_jerk_v026_signal,
    f07pma_f07_price_moving_averages_distatr_63d_jerk_v027_signal,
    f07pma_f07_price_moving_averages_distatr_126d_jerk_v028_signal,
    f07pma_f07_price_moving_averages_distatr_252d_jerk_v029_signal,
    f07pma_f07_price_moving_averages_distatr_504d_jerk_v030_signal,
    f07pma_f07_price_moving_averages_distratio_21v252_jerk_v031_signal,
    f07pma_f07_price_moving_averages_distdiff_63m252_jerk_v032_signal,
    f07pma_f07_price_moving_averages_distdiff_21m63_jerk_v033_signal,
    f07pma_f07_price_moving_averages_distdiff_252m504_jerk_v034_signal,
    f07pma_f07_price_moving_averages_distsq_21d_jerk_v035_signal,
    f07pma_f07_price_moving_averages_distsq_63d_jerk_v036_signal,
    f07pma_f07_price_moving_averages_distsq_252d_jerk_v037_signal,
    f07pma_f07_price_moving_averages_distsq_504d_jerk_v038_signal,
    f07pma_f07_price_moving_averages_distxprice_21d_jerk_v039_signal,
    f07pma_f07_price_moving_averages_distxprice_252d_jerk_v040_signal,
    f07pma_f07_price_moving_averages_distxprice_504d_jerk_v041_signal,
    f07pma_f07_price_moving_averages_distz_63d_jerk_v042_signal,
    f07pma_f07_price_moving_averages_distz_252d_jerk_v043_signal,
    f07pma_f07_price_moving_averages_distz_504d_jerk_v044_signal,
    f07pma_f07_price_moving_averages_distmean_63d_jerk_v045_signal,
    f07pma_f07_price_moving_averages_distmean_252d_jerk_v046_signal,
    f07pma_f07_price_moving_averages_diststd_63d_jerk_v047_signal,
    f07pma_f07_price_moving_averages_diststd_252d_jerk_v048_signal,
    f07pma_f07_price_moving_averages_aboveratio_21d_jerk_v049_signal,
    f07pma_f07_price_moving_averages_aboveratio_63d_jerk_v050_signal,
    f07pma_f07_price_moving_averages_aboveratio_252d_jerk_v051_signal,
    f07pma_f07_price_moving_averages_aboveratio_504d_jerk_v052_signal,
    f07pma_f07_price_moving_averages_distxretvol_21d_jerk_v053_signal,
    f07pma_f07_price_moving_averages_distxretvol_63d_jerk_v054_signal,
    f07pma_f07_price_moving_averages_distxretvol_252d_jerk_v055_signal,
    f07pma_f07_price_moving_averages_distxvolz_21d_jerk_v056_signal,
    f07pma_f07_price_moving_averages_distxvolz_63d_jerk_v057_signal,
    f07pma_f07_price_moving_averages_distxdv_252d_jerk_v058_signal,
    f07pma_f07_price_moving_averages_spread_21d_jerk_v059_signal,
    f07pma_f07_price_moving_averages_spread_63d_jerk_v060_signal,
    f07pma_f07_price_moving_averages_spread_126d_jerk_v061_signal,
    f07pma_f07_price_moving_averages_spread_252d_jerk_v062_signal,
    f07pma_f07_price_moving_averages_spread_504d_jerk_v063_signal,
    f07pma_f07_price_moving_averages_fanout_21v63_jerk_v064_signal,
    f07pma_f07_price_moving_averages_fanout_21v126_jerk_v065_signal,
    f07pma_f07_price_moving_averages_fanout_63v126_jerk_v066_signal,
    f07pma_f07_price_moving_averages_fanout_63v252_jerk_v067_signal,
    f07pma_f07_price_moving_averages_fanout_126v252_jerk_v068_signal,
    f07pma_f07_price_moving_averages_fanout_252v504_jerk_v069_signal,
    f07pma_f07_price_moving_averages_distmax_63d_jerk_v070_signal,
    f07pma_f07_price_moving_averages_distmin_252d_jerk_v071_signal,
    f07pma_f07_price_moving_averages_distsum_63d_jerk_v072_signal,
    f07pma_f07_price_moving_averages_distsum_252d_jerk_v073_signal,
    f07pma_f07_price_moving_averages_distpct_252d_jerk_v074_signal,
    f07pma_f07_price_moving_averages_distpct_504d_jerk_v075_signal,
    f07pma_f07_price_moving_averages_distxrange_21d_jerk_v076_signal,
    f07pma_f07_price_moving_averages_distxatr_63d_jerk_v077_signal,
    f07pma_f07_price_moving_averages_distxatr_252d_jerk_v078_signal,
    f07pma_f07_price_moving_averages_emadist_21d_jerk_v079_signal,
    f07pma_f07_price_moving_averages_emadist_63d_jerk_v080_signal,
    f07pma_f07_price_moving_averages_emadist_126d_jerk_v081_signal,
    f07pma_f07_price_moving_averages_emadist_252d_jerk_v082_signal,
    f07pma_f07_price_moving_averages_emadist_504d_jerk_v083_signal,
    f07pma_f07_price_moving_averages_distmulti_21d_jerk_v084_signal,
    f07pma_f07_price_moving_averages_distmulti_63d_jerk_v085_signal,
    f07pma_f07_price_moving_averages_distmulti_252d_jerk_v086_signal,
    f07pma_f07_price_moving_averages_distmulti_504d_jerk_v087_signal,
    f07pma_f07_price_moving_averages_smaslope_21d_jerk_v088_signal,
    f07pma_f07_price_moving_averages_smaslope_63d_jerk_v089_signal,
    f07pma_f07_price_moving_averages_smaslope_252d_jerk_v090_signal,
    f07pma_f07_price_moving_averages_smaslope_504d_jerk_v091_signal,
    f07pma_f07_price_moving_averages_distxret_5d_jerk_v092_signal,
    f07pma_f07_price_moving_averages_distxret_21d_jerk_v093_signal,
    f07pma_f07_price_moving_averages_distxret_63d_jerk_v094_signal,
    f07pma_f07_price_moving_averages_distxret_252d_jerk_v095_signal,
    f07pma_f07_price_moving_averages_distxskew_63d_jerk_v096_signal,
    f07pma_f07_price_moving_averages_distxskew_252d_jerk_v097_signal,
    f07pma_f07_price_moving_averages_distxkurt_63d_jerk_v098_signal,
    f07pma_f07_price_moving_averages_distxkurt_252d_jerk_v099_signal,
    f07pma_f07_price_moving_averages_distexp_252d_jerk_v100_signal,
    f07pma_f07_price_moving_averages_distxdv_5d_jerk_v101_signal,
    f07pma_f07_price_moving_averages_distxdv_21d_jerk_v102_signal,
    f07pma_f07_price_moving_averages_distxdv_63d_jerk_v103_signal,
    f07pma_f07_price_moving_averages_distxdv_504d_jerk_v104_signal,
    f07pma_f07_price_moving_averages_distatrxret_21d_jerk_v105_signal,
    f07pma_f07_price_moving_averages_distatrxret_63d_jerk_v106_signal,
    f07pma_f07_price_moving_averages_distatrxret_504d_jerk_v107_signal,
    f07pma_f07_price_moving_averages_aboveruncts_21d_jerk_v108_signal,
    f07pma_f07_price_moving_averages_aboveruncts_63d_jerk_v109_signal,
    f07pma_f07_price_moving_averages_aboveruncts_252d_jerk_v110_signal,
    f07pma_f07_price_moving_averages_aboveruncts_504d_jerk_v111_signal,
    f07pma_f07_price_moving_averages_distxocgap_21d_jerk_v112_signal,
    f07pma_f07_price_moving_averages_distxocgap_63d_jerk_v113_signal,
    f07pma_f07_price_moving_averages_distxgapz_252d_jerk_v114_signal,
    f07pma_f07_price_moving_averages_distxintraday_21d_jerk_v115_signal,
    f07pma_f07_price_moving_averages_distxintraday_63d_jerk_v116_signal,
    f07pma_f07_price_moving_averages_distxintraday_252d_jerk_v117_signal,
    f07pma_f07_price_moving_averages_distminw_21d_jerk_v118_signal,
    f07pma_f07_price_moving_averages_distminw_63d_jerk_v119_signal,
    f07pma_f07_price_moving_averages_distminw_252d_jerk_v120_signal,
    f07pma_f07_price_moving_averages_distmaxw_21d_jerk_v121_signal,
    f07pma_f07_price_moving_averages_distmaxw_63d_jerk_v122_signal,
    f07pma_f07_price_moving_averages_distmaxw_252d_jerk_v123_signal,
    f07pma_f07_price_moving_averages_distrange_21d_jerk_v124_signal,
    f07pma_f07_price_moving_averages_distrange_63d_jerk_v125_signal,
    f07pma_f07_price_moving_averages_distrange_252d_jerk_v126_signal,
    f07pma_f07_price_moving_averages_distatrxvolz_21d_jerk_v127_signal,
    f07pma_f07_price_moving_averages_distatrxvolz_63d_jerk_v128_signal,
    f07pma_f07_price_moving_averages_distatrxvolz_252d_jerk_v129_signal,
    f07pma_f07_price_moving_averages_distxabsret_21d_jerk_v130_signal,
    f07pma_f07_price_moving_averages_distxabsret_63d_jerk_v131_signal,
    f07pma_f07_price_moving_averages_distxabsret_252d_jerk_v132_signal,
    f07pma_f07_price_moving_averages_distxvolch_21d_jerk_v133_signal,
    f07pma_f07_price_moving_averages_distxvolch_63d_jerk_v134_signal,
    f07pma_f07_price_moving_averages_distxvolch_252d_jerk_v135_signal,
    f07pma_f07_price_moving_averages_spreadxatr_21d_jerk_v136_signal,
    f07pma_f07_price_moving_averages_spreadxatr_63d_jerk_v137_signal,
    f07pma_f07_price_moving_averages_spreadxatr_252d_jerk_v138_signal,
    f07pma_f07_price_moving_averages_distrelratio_21v252_jerk_v139_signal,
    f07pma_f07_price_moving_averages_distrelratio_63v504_jerk_v140_signal,
    f07pma_f07_price_moving_averages_distxstd_21d_jerk_v141_signal,
    f07pma_f07_price_moving_averages_distxstd_63d_jerk_v142_signal,
    f07pma_f07_price_moving_averages_distxstd_252d_jerk_v143_signal,
    f07pma_f07_price_moving_averages_distintegxprice_21d_jerk_v144_signal,
    f07pma_f07_price_moving_averages_distintegxprice_63d_jerk_v145_signal,
    f07pma_f07_price_moving_averages_distxretmean_252d_jerk_v146_signal,
    f07pma_f07_price_moving_averages_distatrxdv_21d_jerk_v147_signal,
    f07pma_f07_price_moving_averages_distatrxdv_63d_jerk_v148_signal,
    f07pma_f07_price_moving_averages_distatrxdv_252d_jerk_v149_signal,
    f07pma_f07_price_moving_averages_composite_21v252_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_PRICE_MOVING_AVERAGES_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    open_ = closeadj * (1.0 + np.random.normal(0, 0.005, n))
    open_ = pd.Series(open_, name="open")
    close = closeadj.copy()
    close.name = "close"
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "open": open_, "close": close, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f07_price_ma", "_f07_above_ma_dist", "_f07_above_ma_atr")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f07_price_moving_averages_3rd_derivatives_001_150_claude: {n_features} features pass")
