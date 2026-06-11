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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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


# 5d SMA distance from price (percent)
def f07pma_f07_price_moving_averages_dist_5d_base_v001_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance from price (percent)
def f07pma_f07_price_moving_averages_dist_21d_base_v002_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance from price (percent)
def f07pma_f07_price_moving_averages_dist_63d_base_v003_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SMA distance from price (percent)
def f07pma_f07_price_moving_averages_dist_126d_base_v004_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance from price (percent)
def f07pma_f07_price_moving_averages_dist_252d_base_v005_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA distance from price (percent)
def f07pma_f07_price_moving_averages_dist_504d_base_v006_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA price level (continuous)
def f07pma_f07_price_moving_averages_smaprice_21d_base_v007_signal(closeadj):
    result = _f07_price_ma(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA price level (continuous)
def f07pma_f07_price_moving_averages_smaprice_63d_base_v008_signal(closeadj):
    result = _f07_price_ma(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SMA price level (continuous)
def f07pma_f07_price_moving_averages_smaprice_126d_base_v009_signal(closeadj):
    result = _f07_price_ma(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA price level (continuous)
def f07pma_f07_price_moving_averages_smaprice_252d_base_v010_signal(closeadj):
    result = _f07_price_ma(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA price level (continuous)
def f07pma_f07_price_moving_averages_smaprice_504d_base_v011_signal(closeadj):
    result = _f07_price_ma(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to 21d SMA (multiplied by price for variation)
def f07pma_f07_price_moving_averages_ratio_21d_base_v012_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    result = (closeadj / ma.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to 63d SMA
def f07pma_f07_price_moving_averages_ratio_63d_base_v013_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    result = (closeadj / ma.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to 252d SMA
def f07pma_f07_price_moving_averages_ratio_252d_base_v014_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    result = (closeadj / ma.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of price to 504d SMA
def f07pma_f07_price_moving_averages_ratio_504d_base_v015_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    result = (closeadj / ma.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of price to 21d SMA
def f07pma_f07_price_moving_averages_logratio_21d_base_v016_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    r = closeadj / ma.replace(0, np.nan)
    result = np.log(r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of price to 63d SMA
def f07pma_f07_price_moving_averages_logratio_63d_base_v017_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    r = closeadj / ma.replace(0, np.nan)
    result = np.log(r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of price to 252d SMA
def f07pma_f07_price_moving_averages_logratio_252d_base_v018_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    r = closeadj / ma.replace(0, np.nan)
    result = np.log(r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log ratio of price to 504d SMA
def f07pma_f07_price_moving_averages_logratio_504d_base_v019_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    r = closeadj / ma.replace(0, np.nan)
    result = np.log(r.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 21d SMA in ATR units
def f07pma_f07_price_moving_averages_distatr_21d_base_v020_signal(closeadj, high, low):
    result = _f07_above_ma_atr(closeadj, high, low, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 63d SMA in ATR units
def f07pma_f07_price_moving_averages_distatr_63d_base_v021_signal(closeadj, high, low):
    result = _f07_above_ma_atr(closeadj, high, low, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 126d SMA in ATR units
def f07pma_f07_price_moving_averages_distatr_126d_base_v022_signal(closeadj, high, low):
    result = _f07_above_ma_atr(closeadj, high, low, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d SMA in ATR units
def f07pma_f07_price_moving_averages_distatr_252d_base_v023_signal(closeadj, high, low):
    result = _f07_above_ma_atr(closeadj, high, low, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 504d SMA in ATR units
def f07pma_f07_price_moving_averages_distatr_504d_base_v024_signal(closeadj, high, low):
    result = _f07_above_ma_atr(closeadj, high, low, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance scaled by 252d distance
def f07pma_f07_price_moving_averages_distratio_21v252_base_v025_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 21)
    b = _f07_above_ma_dist(closeadj, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance minus 252d SMA distance
def f07pma_f07_price_moving_averages_distdiff_63m252_base_v026_signal(closeadj):
    result = (_f07_above_ma_dist(closeadj, 63) - _f07_above_ma_dist(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance minus 63d SMA distance
def f07pma_f07_price_moving_averages_distdiff_21m63_base_v027_signal(closeadj):
    result = (_f07_above_ma_dist(closeadj, 21) - _f07_above_ma_dist(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance minus 504d SMA distance
def f07pma_f07_price_moving_averages_distdiff_252m504_base_v028_signal(closeadj):
    result = (_f07_above_ma_dist(closeadj, 252) - _f07_above_ma_dist(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d SMA squared (severity)
def f07pma_f07_price_moving_averages_distsq_21d_base_v029_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 63d SMA squared
def f07pma_f07_price_moving_averages_distsq_63d_base_v030_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 252d SMA squared
def f07pma_f07_price_moving_averages_distsq_252d_base_v031_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 504d SMA squared
def f07pma_f07_price_moving_averages_distsq_504d_base_v032_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 504)
    result = d * d.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance times closeadj (price-weighted)
def f07pma_f07_price_moving_averages_distxprice_21d_base_v033_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance times closeadj
def f07pma_f07_price_moving_averages_distxprice_252d_base_v034_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA distance times closeadj
def f07pma_f07_price_moving_averages_distxprice_504d_base_v035_signal(closeadj):
    result = _f07_above_ma_dist(closeadj, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance z-score over 63d
def f07pma_f07_price_moving_averages_distz_63d_base_v036_signal(closeadj):
    result = _z(_f07_above_ma_dist(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance z-score over 252d
def f07pma_f07_price_moving_averages_distz_252d_base_v037_signal(closeadj):
    result = _z(_f07_above_ma_dist(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance z-score over 504d
def f07pma_f07_price_moving_averages_distz_504d_base_v038_signal(closeadj):
    result = _z(_f07_above_ma_dist(closeadj, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 21d distance over 63d
def f07pma_f07_price_moving_averages_distmean_63d_base_v039_signal(closeadj):
    result = _mean(_f07_above_ma_dist(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of 63d distance over 252d
def f07pma_f07_price_moving_averages_distmean_252d_base_v040_signal(closeadj):
    result = _mean(_f07_above_ma_dist(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 21d distance over 63d
def f07pma_f07_price_moving_averages_diststd_63d_base_v041_signal(closeadj):
    result = _std(_f07_above_ma_dist(closeadj, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling std of 63d distance over 252d
def f07pma_f07_price_moving_averages_diststd_252d_base_v042_signal(closeadj):
    result = _std(_f07_above_ma_dist(closeadj, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days above 21d SMA (presence above)
def f07pma_f07_price_moving_averages_aboveratio_21d_base_v043_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 21) > 0).astype(float)
    result = flag.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days above 63d SMA
def f07pma_f07_price_moving_averages_aboveratio_63d_base_v044_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 63) > 0).astype(float)
    result = flag.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days above 252d SMA
def f07pma_f07_price_moving_averages_aboveratio_252d_base_v045_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 252) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days above 504d SMA
def f07pma_f07_price_moving_averages_aboveratio_504d_base_v046_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 504) > 0).astype(float)
    result = flag.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR distance multiplied by sign of return
def f07pma_f07_price_moving_averages_distatrsigned_21d_base_v047_signal(closeadj, high, low):
    r = closeadj.pct_change(21)
    result = _f07_above_ma_atr(closeadj, high, low, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR distance multiplied by 252d return
def f07pma_f07_price_moving_averages_distatrsigned_252d_base_v048_signal(closeadj, high, low):
    r = closeadj.pct_change(252)
    result = _f07_above_ma_atr(closeadj, high, low, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance times rolling vol of returns
def f07pma_f07_price_moving_averages_distxretvol_21d_base_v049_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f07_above_ma_dist(closeadj, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance times rolling vol
def f07pma_f07_price_moving_averages_distxretvol_63d_base_v050_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f07_above_ma_dist(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance times rolling vol
def f07pma_f07_price_moving_averages_distxretvol_252d_base_v051_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f07_above_ma_dist(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance times volume z-score
def f07pma_f07_price_moving_averages_distxvolz_21d_base_v052_signal(closeadj, volume):
    result = _f07_above_ma_dist(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance times volume z-score
def f07pma_f07_price_moving_averages_distxvolz_63d_base_v053_signal(closeadj, volume):
    result = _f07_above_ma_dist(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance times dollar-volume mean
def f07pma_f07_price_moving_averages_distxdv_252d_base_v054_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f07_above_ma_dist(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA-spread between price and 21d SMA in dollars
def f07pma_f07_price_moving_averages_spread_21d_base_v055_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    result = closeadj - ma
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA spread (close - SMA) in dollars
def f07pma_f07_price_moving_averages_spread_63d_base_v056_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    result = closeadj - ma
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SMA spread in dollars
def f07pma_f07_price_moving_averages_spread_126d_base_v057_signal(closeadj):
    ma = _f07_price_ma(closeadj, 126)
    result = closeadj - ma
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA spread in dollars
def f07pma_f07_price_moving_averages_spread_252d_base_v058_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    result = closeadj - ma
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA spread in dollars
def f07pma_f07_price_moving_averages_spread_504d_base_v059_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    result = closeadj - ma
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out: 21d SMA minus 63d SMA scaled by close
def f07pma_f07_price_moving_averages_fanout_21v63_base_v060_signal(closeadj):
    f = _f07_price_ma(closeadj, 21) - _f07_price_ma(closeadj, 63)
    result = f * closeadj / _f07_price_ma(closeadj, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out: 21d minus 126d SMA scaled by close
def f07pma_f07_price_moving_averages_fanout_21v126_base_v061_signal(closeadj):
    f = _f07_price_ma(closeadj, 21) - _f07_price_ma(closeadj, 126)
    result = f * closeadj / _f07_price_ma(closeadj, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out: 63d minus 126d SMA scaled by close
def f07pma_f07_price_moving_averages_fanout_63v126_base_v062_signal(closeadj):
    f = _f07_price_ma(closeadj, 63) - _f07_price_ma(closeadj, 126)
    result = f * closeadj / _f07_price_ma(closeadj, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out: 63d minus 252d SMA scaled by close
def f07pma_f07_price_moving_averages_fanout_63v252_base_v063_signal(closeadj):
    f = _f07_price_ma(closeadj, 63) - _f07_price_ma(closeadj, 252)
    result = f * closeadj / _f07_price_ma(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out: 126d minus 252d SMA scaled by close
def f07pma_f07_price_moving_averages_fanout_126v252_base_v064_signal(closeadj):
    f = _f07_price_ma(closeadj, 126) - _f07_price_ma(closeadj, 252)
    result = f * closeadj / _f07_price_ma(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out: 252d minus 504d SMA scaled by close
def f07pma_f07_price_moving_averages_fanout_252v504_base_v065_signal(closeadj):
    f = _f07_price_ma(closeadj, 252) - _f07_price_ma(closeadj, 504)
    result = f * closeadj / _f07_price_ma(closeadj, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling max of 21d SMA distance over 63d
def f07pma_f07_price_moving_averages_distmax_63d_base_v066_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling min of 63d SMA distance over 252d
def f07pma_f07_price_moving_averages_distmin_252d_base_v067_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 21d SMA distance over 63d (cumulative position)
def f07pma_f07_price_moving_averages_distsum_63d_base_v068_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 63d SMA distance over 252d
def f07pma_f07_price_moving_averages_distsum_252d_base_v069_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance scaled by 504d worst (most-negative) distance
def f07pma_f07_price_moving_averages_distrelhist_504d_base_v070_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    worst = d.rolling(504, min_periods=126).min()
    result = (d / worst.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 21d SMA distance over 252d
def f07pma_f07_price_moving_averages_distpct_252d_base_v071_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 63d SMA distance over 504d
def f07pma_f07_price_moving_averages_distpct_504d_base_v072_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance times daily range
def f07pma_f07_price_moving_averages_distxrange_21d_base_v073_signal(closeadj, high, low):
    rng = (high - low)
    result = _f07_above_ma_dist(closeadj, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance times 21d ATR
def f07pma_f07_price_moving_averages_distxatr_63d_base_v074_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f07_above_ma_dist(closeadj, 63) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance times 63d ATR
def f07pma_f07_price_moving_averages_distxatr_252d_base_v075_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f07_above_ma_dist(closeadj, 252) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07pma_f07_price_moving_averages_dist_5d_base_v001_signal,
    f07pma_f07_price_moving_averages_dist_21d_base_v002_signal,
    f07pma_f07_price_moving_averages_dist_63d_base_v003_signal,
    f07pma_f07_price_moving_averages_dist_126d_base_v004_signal,
    f07pma_f07_price_moving_averages_dist_252d_base_v005_signal,
    f07pma_f07_price_moving_averages_dist_504d_base_v006_signal,
    f07pma_f07_price_moving_averages_smaprice_21d_base_v007_signal,
    f07pma_f07_price_moving_averages_smaprice_63d_base_v008_signal,
    f07pma_f07_price_moving_averages_smaprice_126d_base_v009_signal,
    f07pma_f07_price_moving_averages_smaprice_252d_base_v010_signal,
    f07pma_f07_price_moving_averages_smaprice_504d_base_v011_signal,
    f07pma_f07_price_moving_averages_ratio_21d_base_v012_signal,
    f07pma_f07_price_moving_averages_ratio_63d_base_v013_signal,
    f07pma_f07_price_moving_averages_ratio_252d_base_v014_signal,
    f07pma_f07_price_moving_averages_ratio_504d_base_v015_signal,
    f07pma_f07_price_moving_averages_logratio_21d_base_v016_signal,
    f07pma_f07_price_moving_averages_logratio_63d_base_v017_signal,
    f07pma_f07_price_moving_averages_logratio_252d_base_v018_signal,
    f07pma_f07_price_moving_averages_logratio_504d_base_v019_signal,
    f07pma_f07_price_moving_averages_distatr_21d_base_v020_signal,
    f07pma_f07_price_moving_averages_distatr_63d_base_v021_signal,
    f07pma_f07_price_moving_averages_distatr_126d_base_v022_signal,
    f07pma_f07_price_moving_averages_distatr_252d_base_v023_signal,
    f07pma_f07_price_moving_averages_distatr_504d_base_v024_signal,
    f07pma_f07_price_moving_averages_distratio_21v252_base_v025_signal,
    f07pma_f07_price_moving_averages_distdiff_63m252_base_v026_signal,
    f07pma_f07_price_moving_averages_distdiff_21m63_base_v027_signal,
    f07pma_f07_price_moving_averages_distdiff_252m504_base_v028_signal,
    f07pma_f07_price_moving_averages_distsq_21d_base_v029_signal,
    f07pma_f07_price_moving_averages_distsq_63d_base_v030_signal,
    f07pma_f07_price_moving_averages_distsq_252d_base_v031_signal,
    f07pma_f07_price_moving_averages_distsq_504d_base_v032_signal,
    f07pma_f07_price_moving_averages_distxprice_21d_base_v033_signal,
    f07pma_f07_price_moving_averages_distxprice_252d_base_v034_signal,
    f07pma_f07_price_moving_averages_distxprice_504d_base_v035_signal,
    f07pma_f07_price_moving_averages_distz_63d_base_v036_signal,
    f07pma_f07_price_moving_averages_distz_252d_base_v037_signal,
    f07pma_f07_price_moving_averages_distz_504d_base_v038_signal,
    f07pma_f07_price_moving_averages_distmean_63d_base_v039_signal,
    f07pma_f07_price_moving_averages_distmean_252d_base_v040_signal,
    f07pma_f07_price_moving_averages_diststd_63d_base_v041_signal,
    f07pma_f07_price_moving_averages_diststd_252d_base_v042_signal,
    f07pma_f07_price_moving_averages_aboveratio_21d_base_v043_signal,
    f07pma_f07_price_moving_averages_aboveratio_63d_base_v044_signal,
    f07pma_f07_price_moving_averages_aboveratio_252d_base_v045_signal,
    f07pma_f07_price_moving_averages_aboveratio_504d_base_v046_signal,
    f07pma_f07_price_moving_averages_distatrsigned_21d_base_v047_signal,
    f07pma_f07_price_moving_averages_distatrsigned_252d_base_v048_signal,
    f07pma_f07_price_moving_averages_distxretvol_21d_base_v049_signal,
    f07pma_f07_price_moving_averages_distxretvol_63d_base_v050_signal,
    f07pma_f07_price_moving_averages_distxretvol_252d_base_v051_signal,
    f07pma_f07_price_moving_averages_distxvolz_21d_base_v052_signal,
    f07pma_f07_price_moving_averages_distxvolz_63d_base_v053_signal,
    f07pma_f07_price_moving_averages_distxdv_252d_base_v054_signal,
    f07pma_f07_price_moving_averages_spread_21d_base_v055_signal,
    f07pma_f07_price_moving_averages_spread_63d_base_v056_signal,
    f07pma_f07_price_moving_averages_spread_126d_base_v057_signal,
    f07pma_f07_price_moving_averages_spread_252d_base_v058_signal,
    f07pma_f07_price_moving_averages_spread_504d_base_v059_signal,
    f07pma_f07_price_moving_averages_fanout_21v63_base_v060_signal,
    f07pma_f07_price_moving_averages_fanout_21v126_base_v061_signal,
    f07pma_f07_price_moving_averages_fanout_63v126_base_v062_signal,
    f07pma_f07_price_moving_averages_fanout_63v252_base_v063_signal,
    f07pma_f07_price_moving_averages_fanout_126v252_base_v064_signal,
    f07pma_f07_price_moving_averages_fanout_252v504_base_v065_signal,
    f07pma_f07_price_moving_averages_distmax_63d_base_v066_signal,
    f07pma_f07_price_moving_averages_distmin_252d_base_v067_signal,
    f07pma_f07_price_moving_averages_distsum_63d_base_v068_signal,
    f07pma_f07_price_moving_averages_distsum_252d_base_v069_signal,
    f07pma_f07_price_moving_averages_distrelhist_504d_base_v070_signal,
    f07pma_f07_price_moving_averages_distpct_252d_base_v071_signal,
    f07pma_f07_price_moving_averages_distpct_504d_base_v072_signal,
    f07pma_f07_price_moving_averages_distxrange_21d_base_v073_signal,
    f07pma_f07_price_moving_averages_distxatr_63d_base_v074_signal,
    f07pma_f07_price_moving_averages_distxatr_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_PRICE_MOVING_AVERAGES_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f07_price_moving_averages_base_001_075_claude: {n_features} features pass")
