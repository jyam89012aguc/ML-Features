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


def _sma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f08_ma_dynamics_slope(close, w, lag):
    # rate of change of SMA over lag, normalized by SMA level
    ma = _sma(close, w)
    return ma.diff(lag) / ma.replace(0, np.nan).abs()


def _f08_ma_cross_diff(close, fast, slow):
    # difference between fast and slow SMAs scaled by slow SMA
    fma = _sma(close, fast)
    sma = _sma(close, slow)
    return (fma - sma) / sma.replace(0, np.nan).abs()


def _f08_ma_dynamics_accel(close, w, lag):
    # acceleration of SMA: 2nd diff over lag
    ma = _sma(close, w)
    return ma.diff(lag).diff(lag) / ma.replace(0, np.nan).abs()


# 5d SMA slope over 5d
def f08mad_f08_moving_average_dynamics_slope_5d_base_v001_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 5, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA slope over 5d
def f08mad_f08_moving_average_dynamics_slope_21d5_base_v002_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 21, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA slope over 21d
def f08mad_f08_moving_average_dynamics_slope_21d21_base_v003_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA slope over 21d
def f08mad_f08_moving_average_dynamics_slope_63d21_base_v004_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA slope over 63d
def f08mad_f08_moving_average_dynamics_slope_63d63_base_v005_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 63, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SMA slope over 21d
def f08mad_f08_moving_average_dynamics_slope_126d21_base_v006_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 126, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SMA slope over 63d
def f08mad_f08_moving_average_dynamics_slope_126d63_base_v007_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 126, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA slope over 21d
def f08mad_f08_moving_average_dynamics_slope_252d21_base_v008_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 252, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA slope over 63d
def f08mad_f08_moving_average_dynamics_slope_252d63_base_v009_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA slope over 126d
def f08mad_f08_moving_average_dynamics_slope_252d126_base_v010_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 252, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA slope over 63d
def f08mad_f08_moving_average_dynamics_slope_504d63_base_v011_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 504, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA slope over 126d
def f08mad_f08_moving_average_dynamics_slope_504d126_base_v012_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 504, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA slope over 252d
def f08mad_f08_moving_average_dynamics_slope_504d252_base_v013_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 504, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d/21d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_5v21_base_v014_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 5, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/63d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_21v63_base_v015_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 21, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/126d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_21v126_base_v016_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 21, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_21v252_base_v017_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 21, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/126d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_63v126_base_v018_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 63, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_63v252_base_v019_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 63, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d/252d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_126v252_base_v020_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 126, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d/504d MA cross divergence
def f08mad_f08_moving_average_dynamics_cross_252v504_base_v021_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 252, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA acceleration over 21d
def f08mad_f08_moving_average_dynamics_accel_21d_base_v022_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 21, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA acceleration over 21d
def f08mad_f08_moving_average_dynamics_accel_63d_base_v023_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 63, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d SMA acceleration over 63d
def f08mad_f08_moving_average_dynamics_accel_126d_base_v024_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 126, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA acceleration over 63d
def f08mad_f08_moving_average_dynamics_accel_252d_base_v025_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 252, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA acceleration over 126d
def f08mad_f08_moving_average_dynamics_accel_504d_base_v026_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 504, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d SMA slope over 63d
def f08mad_f08_moving_average_dynamics_slopez_21d_base_v027_signal(closeadj):
    result = _z(_f08_ma_dynamics_slope(closeadj, 21, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d SMA slope over 252d
def f08mad_f08_moving_average_dynamics_slopez_63d_base_v028_signal(closeadj):
    result = _z(_f08_ma_dynamics_slope(closeadj, 63, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 252d SMA slope over 504d
def f08mad_f08_moving_average_dynamics_slopez_252d_base_v029_signal(closeadj):
    result = _z(_f08_ma_dynamics_slope(closeadj, 252, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21v63 cross over 252d
def f08mad_f08_moving_average_dynamics_crossz_21v63_base_v030_signal(closeadj):
    result = _z(_f08_ma_cross_diff(closeadj, 21, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63v252 cross over 504d
def f08mad_f08_moving_average_dynamics_crossz_63v252_base_v031_signal(closeadj):
    result = _z(_f08_ma_cross_diff(closeadj, 63, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA slope × close (continuous slope)
def f08mad_f08_moving_average_dynamics_slopexprice_21d_base_v032_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA slope × close
def f08mad_f08_moving_average_dynamics_slopexprice_63d_base_v033_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA slope × close
def f08mad_f08_moving_average_dynamics_slopexprice_252d_base_v034_signal(closeadj):
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out width (max-min of MA distances) over 5/21/63/252
def f08mad_f08_moving_average_dynamics_fanwidth_5_252_base_v035_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 5, 21)
    b = _f08_ma_cross_diff(closeadj, 21, 63)
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    df = pd.concat([a, b, c], axis=1)
    result = (df.max(axis=1) - df.min(axis=1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out width over 21/63/126/252
def f08mad_f08_moving_average_dynamics_fanwidth_21_252_base_v036_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 21, 63)
    b = _f08_ma_cross_diff(closeadj, 63, 126)
    c = _f08_ma_cross_diff(closeadj, 126, 252)
    df = pd.concat([a, b, c], axis=1)
    result = (df.max(axis=1) - df.min(axis=1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out width over 63/126/252/504
def f08mad_f08_moving_average_dynamics_fanwidth_63_504_base_v037_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 63, 126)
    b = _f08_ma_cross_diff(closeadj, 126, 252)
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    df = pd.concat([a, b, c], axis=1)
    result = (df.max(axis=1) - df.min(axis=1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 cross squared (intensity)
def f08mad_f08_moving_average_dynamics_crosssq_21v63_base_v038_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = c * c.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_63v252_base_v039_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = c * c.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126v252 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_126v252_base_v040_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 126, 252)
    result = c * c.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_252v504_base_v041_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    result = c * c.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21v63 cross
def f08mad_f08_moving_average_dynamics_crossroc_21v63_base_v042_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = c.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63v252 cross
def f08mad_f08_moving_average_dynamics_crossroc_63v252_base_v043_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = c.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of 21v63 cross
def f08mad_f08_moving_average_dynamics_crossmean_21v63_base_v044_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = _mean(c, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 63v252 cross
def f08mad_f08_moving_average_dynamics_crossmean_63v252_base_v045_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = _mean(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling std of 21v63 cross (cross-volatility)
def f08mad_f08_moving_average_dynamics_crossstd_21v63_base_v046_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = _std(c, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of 63v252 cross
def f08mad_f08_moving_average_dynamics_crossstd_63v252_base_v047_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = _std(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × volume z (price-volume momentum)
def f08mad_f08_moving_average_dynamics_slopexvolz_252d_base_v048_signal(closeadj, volume):
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × volume z
def f08mad_f08_moving_average_dynamics_slopexvolz_21d_base_v049_signal(closeadj, volume):
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × dollar volume mean
def f08mad_f08_moving_average_dynamics_slopexdv_63d_base_v050_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × 21d dollar volume mean
def f08mad_f08_moving_average_dynamics_slopexdv_252d_base_v051_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d MA over 21d, normalized by ATR
def f08mad_f08_moving_average_dynamics_slopenormatr_21d_base_v052_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * closeadj / atr.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d MA over 21d, normalized by ATR
def f08mad_f08_moving_average_dynamics_slopenormatr_63d_base_v053_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * closeadj / atr.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d MA over 63d, normalized by 63d ATR
def f08mad_f08_moving_average_dynamics_slopenormatr_252d_base_v054_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * closeadj / atr.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 cross weighted by close
def f08mad_f08_moving_average_dynamics_crossxprice_21v63_base_v055_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 21, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross weighted by close
def f08mad_f08_moving_average_dynamics_crossxprice_63v252_base_v056_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 63, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross weighted by close
def f08mad_f08_moving_average_dynamics_crossxprice_252v504_base_v057_signal(closeadj):
    result = _f08_ma_cross_diff(closeadj, 252, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d MA × cross 21v63 (alignment)
def f08mad_f08_moving_average_dynamics_slopexcross_21_base_v058_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = s * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d MA × cross 63v252
def f08mad_f08_moving_average_dynamics_slopexcross_63_base_v059_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = s * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d MA × cross 252v504
def f08mad_f08_moving_average_dynamics_slopexcross_252_base_v060_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    result = s * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 21d slope over 63d
def f08mad_f08_moving_average_dynamics_slopesum_21d_base_v061_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = s.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 63d slope over 252d
def f08mad_f08_moving_average_dynamics_slopesum_63d_base_v062_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = s.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling sum of 252d slope over 252d
def f08mad_f08_moving_average_dynamics_slopesum_252d_base_v063_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = s.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days with 21d slope > 0 over 63d (trend strength)
def f08mad_f08_moving_average_dynamics_slopepos_21d_base_v064_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    flag = (s > 0).astype(float)
    result = flag.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days with 63d slope > 0 over 252d
def f08mad_f08_moving_average_dynamics_slopepos_63d_base_v065_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    flag = (s > 0).astype(float)
    result = flag.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# count of days with 252d slope > 0 over 504d
def f08mad_f08_moving_average_dynamics_slopepos_252d_base_v066_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    flag = (s > 0).astype(float)
    result = flag.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 cross convergence speed (abs slope of cross)
def f08mad_f08_moving_average_dynamics_crossroctotal_21v63_base_v067_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = c.diff(21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross convergence speed
def f08mad_f08_moving_average_dynamics_crossroctotal_63v252_base_v068_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = c.diff(63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross convergence speed
def f08mad_f08_moving_average_dynamics_crossroctotal_252v504_base_v069_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    result = c.diff(252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × 252d slope (long-short alignment)
def f08mad_f08_moving_average_dynamics_slopealign_21x252_base_v070_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 21, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = sa * sb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × 252d slope
def f08mad_f08_moving_average_dynamics_slopealign_63x252_base_v071_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 63, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = sa * sb * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope minus 252d slope (short-long divergence)
def f08mad_f08_moving_average_dynamics_slopediff_21m252_base_v072_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 21, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = (sa - sb) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope minus 252d slope
def f08mad_f08_moving_average_dynamics_slopediff_63m252_base_v073_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 63, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = (sa - sb) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope ratio to 63d slope
def f08mad_f08_moving_average_dynamics_sloperatio_21v63_base_v074_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 21, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 63, 21).replace(0, np.nan)
    result = (sa / sb) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope ratio to 252d slope
def f08mad_f08_moving_average_dynamics_sloperatio_63v252_base_v075_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 63, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63).replace(0, np.nan)
    result = (sa / sb) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08mad_f08_moving_average_dynamics_slope_5d_base_v001_signal,
    f08mad_f08_moving_average_dynamics_slope_21d5_base_v002_signal,
    f08mad_f08_moving_average_dynamics_slope_21d21_base_v003_signal,
    f08mad_f08_moving_average_dynamics_slope_63d21_base_v004_signal,
    f08mad_f08_moving_average_dynamics_slope_63d63_base_v005_signal,
    f08mad_f08_moving_average_dynamics_slope_126d21_base_v006_signal,
    f08mad_f08_moving_average_dynamics_slope_126d63_base_v007_signal,
    f08mad_f08_moving_average_dynamics_slope_252d21_base_v008_signal,
    f08mad_f08_moving_average_dynamics_slope_252d63_base_v009_signal,
    f08mad_f08_moving_average_dynamics_slope_252d126_base_v010_signal,
    f08mad_f08_moving_average_dynamics_slope_504d63_base_v011_signal,
    f08mad_f08_moving_average_dynamics_slope_504d126_base_v012_signal,
    f08mad_f08_moving_average_dynamics_slope_504d252_base_v013_signal,
    f08mad_f08_moving_average_dynamics_cross_5v21_base_v014_signal,
    f08mad_f08_moving_average_dynamics_cross_21v63_base_v015_signal,
    f08mad_f08_moving_average_dynamics_cross_21v126_base_v016_signal,
    f08mad_f08_moving_average_dynamics_cross_21v252_base_v017_signal,
    f08mad_f08_moving_average_dynamics_cross_63v126_base_v018_signal,
    f08mad_f08_moving_average_dynamics_cross_63v252_base_v019_signal,
    f08mad_f08_moving_average_dynamics_cross_126v252_base_v020_signal,
    f08mad_f08_moving_average_dynamics_cross_252v504_base_v021_signal,
    f08mad_f08_moving_average_dynamics_accel_21d_base_v022_signal,
    f08mad_f08_moving_average_dynamics_accel_63d_base_v023_signal,
    f08mad_f08_moving_average_dynamics_accel_126d_base_v024_signal,
    f08mad_f08_moving_average_dynamics_accel_252d_base_v025_signal,
    f08mad_f08_moving_average_dynamics_accel_504d_base_v026_signal,
    f08mad_f08_moving_average_dynamics_slopez_21d_base_v027_signal,
    f08mad_f08_moving_average_dynamics_slopez_63d_base_v028_signal,
    f08mad_f08_moving_average_dynamics_slopez_252d_base_v029_signal,
    f08mad_f08_moving_average_dynamics_crossz_21v63_base_v030_signal,
    f08mad_f08_moving_average_dynamics_crossz_63v252_base_v031_signal,
    f08mad_f08_moving_average_dynamics_slopexprice_21d_base_v032_signal,
    f08mad_f08_moving_average_dynamics_slopexprice_63d_base_v033_signal,
    f08mad_f08_moving_average_dynamics_slopexprice_252d_base_v034_signal,
    f08mad_f08_moving_average_dynamics_fanwidth_5_252_base_v035_signal,
    f08mad_f08_moving_average_dynamics_fanwidth_21_252_base_v036_signal,
    f08mad_f08_moving_average_dynamics_fanwidth_63_504_base_v037_signal,
    f08mad_f08_moving_average_dynamics_crosssq_21v63_base_v038_signal,
    f08mad_f08_moving_average_dynamics_crosssq_63v252_base_v039_signal,
    f08mad_f08_moving_average_dynamics_crosssq_126v252_base_v040_signal,
    f08mad_f08_moving_average_dynamics_crosssq_252v504_base_v041_signal,
    f08mad_f08_moving_average_dynamics_crossroc_21v63_base_v042_signal,
    f08mad_f08_moving_average_dynamics_crossroc_63v252_base_v043_signal,
    f08mad_f08_moving_average_dynamics_crossmean_21v63_base_v044_signal,
    f08mad_f08_moving_average_dynamics_crossmean_63v252_base_v045_signal,
    f08mad_f08_moving_average_dynamics_crossstd_21v63_base_v046_signal,
    f08mad_f08_moving_average_dynamics_crossstd_63v252_base_v047_signal,
    f08mad_f08_moving_average_dynamics_slopexvolz_252d_base_v048_signal,
    f08mad_f08_moving_average_dynamics_slopexvolz_21d_base_v049_signal,
    f08mad_f08_moving_average_dynamics_slopexdv_63d_base_v050_signal,
    f08mad_f08_moving_average_dynamics_slopexdv_252d_base_v051_signal,
    f08mad_f08_moving_average_dynamics_slopenormatr_21d_base_v052_signal,
    f08mad_f08_moving_average_dynamics_slopenormatr_63d_base_v053_signal,
    f08mad_f08_moving_average_dynamics_slopenormatr_252d_base_v054_signal,
    f08mad_f08_moving_average_dynamics_crossxprice_21v63_base_v055_signal,
    f08mad_f08_moving_average_dynamics_crossxprice_63v252_base_v056_signal,
    f08mad_f08_moving_average_dynamics_crossxprice_252v504_base_v057_signal,
    f08mad_f08_moving_average_dynamics_slopexcross_21_base_v058_signal,
    f08mad_f08_moving_average_dynamics_slopexcross_63_base_v059_signal,
    f08mad_f08_moving_average_dynamics_slopexcross_252_base_v060_signal,
    f08mad_f08_moving_average_dynamics_slopesum_21d_base_v061_signal,
    f08mad_f08_moving_average_dynamics_slopesum_63d_base_v062_signal,
    f08mad_f08_moving_average_dynamics_slopesum_252d_base_v063_signal,
    f08mad_f08_moving_average_dynamics_slopepos_21d_base_v064_signal,
    f08mad_f08_moving_average_dynamics_slopepos_63d_base_v065_signal,
    f08mad_f08_moving_average_dynamics_slopepos_252d_base_v066_signal,
    f08mad_f08_moving_average_dynamics_crossroctotal_21v63_base_v067_signal,
    f08mad_f08_moving_average_dynamics_crossroctotal_63v252_base_v068_signal,
    f08mad_f08_moving_average_dynamics_crossroctotal_252v504_base_v069_signal,
    f08mad_f08_moving_average_dynamics_slopealign_21x252_base_v070_signal,
    f08mad_f08_moving_average_dynamics_slopealign_63x252_base_v071_signal,
    f08mad_f08_moving_average_dynamics_slopediff_21m252_base_v072_signal,
    f08mad_f08_moving_average_dynamics_slopediff_63m252_base_v073_signal,
    f08mad_f08_moving_average_dynamics_sloperatio_21v63_base_v074_signal,
    f08mad_f08_moving_average_dynamics_sloperatio_63v252_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_MOVING_AVERAGE_DYNAMICS_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f08_ma_dynamics_slope", "_f08_ma_cross_diff", "_f08_ma_dynamics_accel")
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
    print(f"OK f08_moving_average_dynamics_base_001_075_claude: {n_features} features pass")
