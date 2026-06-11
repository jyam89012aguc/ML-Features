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


def _jerk(base, w):
    return base.diff(w).diff(w) / base.abs().replace(0, np.nan)


# 5d jerk of 5d SMA slope
def f08mad_f08_moving_average_dynamics_slope_5d_jerk_v001_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 5, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d/5d SMA slope
def f08mad_f08_moving_average_dynamics_slope_21d5_jerk_v002_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 21, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d/21d slope
def f08mad_f08_moving_average_dynamics_slope_21d21_jerk_v003_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d/21d slope
def f08mad_f08_moving_average_dynamics_slope_63d21_jerk_v004_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d/63d slope
def f08mad_f08_moving_average_dynamics_slope_63d63_jerk_v005_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 63, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d/21d slope
def f08mad_f08_moving_average_dynamics_slope_126d21_jerk_v006_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 126, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d/63d slope
def f08mad_f08_moving_average_dynamics_slope_126d63_jerk_v007_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 126, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d/21d slope
def f08mad_f08_moving_average_dynamics_slope_252d21_jerk_v008_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 252, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d/63d slope
def f08mad_f08_moving_average_dynamics_slope_252d63_jerk_v009_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d/126d slope
def f08mad_f08_moving_average_dynamics_slope_252d126_jerk_v010_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 252, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d/63d slope
def f08mad_f08_moving_average_dynamics_slope_504d63_jerk_v011_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 504, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d/126d slope
def f08mad_f08_moving_average_dynamics_slope_504d126_jerk_v012_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 504, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d/252d slope
def f08mad_f08_moving_average_dynamics_slope_504d252_jerk_v013_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 504, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5v21 cross
def f08mad_f08_moving_average_dynamics_cross_5v21_jerk_v014_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 5, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 cross
def f08mad_f08_moving_average_dynamics_cross_21v63_jerk_v015_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 21, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v126 cross
def f08mad_f08_moving_average_dynamics_cross_21v126_jerk_v016_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 21, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v252 cross
def f08mad_f08_moving_average_dynamics_cross_21v252_jerk_v017_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 21, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v126 cross
def f08mad_f08_moving_average_dynamics_cross_63v126_jerk_v018_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 63, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 cross
def f08mad_f08_moving_average_dynamics_cross_63v252_jerk_v019_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 63, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126v252 cross
def f08mad_f08_moving_average_dynamics_cross_126v252_jerk_v020_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 126, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252v504 cross
def f08mad_f08_moving_average_dynamics_cross_252v504_jerk_v021_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 252, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d MA accel
def f08mad_f08_moving_average_dynamics_accel_21d_jerk_v022_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 21, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d MA accel
def f08mad_f08_moving_average_dynamics_accel_63d_jerk_v023_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 63, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d MA accel
def f08mad_f08_moving_average_dynamics_accel_126d_jerk_v024_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 126, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d MA accel
def f08mad_f08_moving_average_dynamics_accel_252d_jerk_v025_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 252, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d MA accel
def f08mad_f08_moving_average_dynamics_accel_504d_jerk_v026_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 504, 126) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope-zscore
def f08mad_f08_moving_average_dynamics_slopez_21d_jerk_v027_signal(closeadj):
    base = _z(_f08_ma_dynamics_slope(closeadj, 21, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope-zscore
def f08mad_f08_moving_average_dynamics_slopez_63d_jerk_v028_signal(closeadj):
    base = _z(_f08_ma_dynamics_slope(closeadj, 63, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope-zscore
def f08mad_f08_moving_average_dynamics_slopez_252d_jerk_v029_signal(closeadj):
    base = _z(_f08_ma_dynamics_slope(closeadj, 252, 63), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 cross zscore
def f08mad_f08_moving_average_dynamics_crossz_21v63_jerk_v030_signal(closeadj):
    base = _z(_f08_ma_cross_diff(closeadj, 21, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 cross zscore
def f08mad_f08_moving_average_dynamics_crossz_63v252_jerk_v031_signal(closeadj):
    base = _z(_f08_ma_cross_diff(closeadj, 63, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope×price (21d)
def f08mad_f08_moving_average_dynamics_slopexprice_21d_jerk_v032_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope×price (63d)
def f08mad_f08_moving_average_dynamics_slopexprice_63d_jerk_v033_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope×price (252d)
def f08mad_f08_moving_average_dynamics_slopexprice_252d_jerk_v034_signal(closeadj):
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of fan-width (5/21/63/252)
def f08mad_f08_moving_average_dynamics_fanwidth_5_252_jerk_v035_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 5, 21)
    b = _f08_ma_cross_diff(closeadj, 21, 63)
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    df = pd.concat([a, b, c], axis=1)
    base = (df.max(axis=1) - df.min(axis=1)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of fan-width 21_252
def f08mad_f08_moving_average_dynamics_fanwidth_21_252_jerk_v036_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 21, 63)
    b = _f08_ma_cross_diff(closeadj, 63, 126)
    c = _f08_ma_cross_diff(closeadj, 126, 252)
    df = pd.concat([a, b, c], axis=1)
    base = (df.max(axis=1) - df.min(axis=1)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of fan-width 63_504
def f08mad_f08_moving_average_dynamics_fanwidth_63_504_jerk_v037_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 63, 126)
    b = _f08_ma_cross_diff(closeadj, 126, 252)
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    df = pd.concat([a, b, c], axis=1)
    base = (df.max(axis=1) - df.min(axis=1)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_21v63_jerk_v038_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = c * c.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_63v252_jerk_v039_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = c * c.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126v252 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_126v252_jerk_v040_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 126, 252)
    base = c * c.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252v504 cross squared
def f08mad_f08_moving_average_dynamics_crosssq_252v504_jerk_v041_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    base = c * c.abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 cross-roc
def f08mad_f08_moving_average_dynamics_crossroc_21v63_jerk_v042_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = c.diff(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 cross-roc
def f08mad_f08_moving_average_dynamics_crossroc_63v252_jerk_v043_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = c.diff(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 cross mean
def f08mad_f08_moving_average_dynamics_crossmean_21v63_jerk_v044_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = _mean(c, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 cross mean
def f08mad_f08_moving_average_dynamics_crossmean_63v252_jerk_v045_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = _mean(c, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21v63 cross std
def f08mad_f08_moving_average_dynamics_crossstd_21v63_jerk_v046_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = _std(c, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63v252 cross std
def f08mad_f08_moving_average_dynamics_crossstd_63v252_jerk_v047_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = _std(c, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × volume z
def f08mad_f08_moving_average_dynamics_slopexvolz_252d_jerk_v048_signal(closeadj, volume):
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * _z(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope × volume z
def f08mad_f08_moving_average_dynamics_slopexvolz_21d_jerk_v049_signal(closeadj, volume):
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * _z(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope × dollar volume
def f08mad_f08_moving_average_dynamics_slopexdv_63d_jerk_v050_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope × dollar volume
def f08mad_f08_moving_average_dynamics_slopexdv_252d_jerk_v051_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope norm by ATR
def f08mad_f08_moving_average_dynamics_slopenormatr_21d_jerk_v052_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * closeadj / atr.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d slope norm by ATR
def f08mad_f08_moving_average_dynamics_slopenormatr_63d_jerk_v053_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * closeadj / atr.replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope norm by ATR
def f08mad_f08_moving_average_dynamics_slopenormatr_252d_jerk_v054_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * closeadj / atr.replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross 21v63 × price
def f08mad_f08_moving_average_dynamics_crossxprice_21v63_jerk_v055_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 21, 63) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross 63v252 × price
def f08mad_f08_moving_average_dynamics_crossxprice_63v252_jerk_v056_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 63, 252) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cross 252v504 × price
def f08mad_f08_moving_average_dynamics_crossxprice_252v504_jerk_v057_signal(closeadj):
    base = _f08_ma_cross_diff(closeadj, 252, 504) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × cross (21)
def f08mad_f08_moving_average_dynamics_slopexcross_21_jerk_v058_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = s * c * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × cross (63)
def f08mad_f08_moving_average_dynamics_slopexcross_63_jerk_v059_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = s * c * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × cross (252)
def f08mad_f08_moving_average_dynamics_slopexcross_252_jerk_v060_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    base = s * c * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope-sum
def f08mad_f08_moving_average_dynamics_slopesum_21d_jerk_v061_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = s.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope-sum
def f08mad_f08_moving_average_dynamics_slopesum_63d_jerk_v062_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = s.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope-sum
def f08mad_f08_moving_average_dynamics_slopesum_252d_jerk_v063_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = s.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope-pos ratio
def f08mad_f08_moving_average_dynamics_slopepos_21d_jerk_v064_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    flag = (s > 0).astype(float)
    base = flag.rolling(63, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope-pos ratio
def f08mad_f08_moving_average_dynamics_slopepos_63d_jerk_v065_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    flag = (s > 0).astype(float)
    base = flag.rolling(252, min_periods=63).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d slope-pos ratio
def f08mad_f08_moving_average_dynamics_slopepos_252d_jerk_v066_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    flag = (s > 0).astype(float)
    base = flag.rolling(504, min_periods=126).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross-roc abs (21v63)
def f08mad_f08_moving_average_dynamics_crossroctotal_21v63_jerk_v067_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = c.diff(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross-roc abs (63v252)
def f08mad_f08_moving_average_dynamics_crossroctotal_63v252_jerk_v068_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = c.diff(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d jerk of cross-roc abs (252v504)
def f08mad_f08_moving_average_dynamics_crossroctotal_252v504_jerk_v069_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    base = c.diff(252).abs() * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope-align 21x252
def f08mad_f08_moving_average_dynamics_slopealign_21x252_jerk_v070_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 21, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = sa * sb * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope-align 63x252
def f08mad_f08_moving_average_dynamics_slopealign_63x252_jerk_v071_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 63, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = sa * sb * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope-diff 21m252
def f08mad_f08_moving_average_dynamics_slopediff_21m252_jerk_v072_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 21, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = (sa - sb) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope-diff 63m252
def f08mad_f08_moving_average_dynamics_slopediff_63m252_jerk_v073_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 63, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = (sa - sb) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope-ratio 21v63
def f08mad_f08_moving_average_dynamics_sloperatio_21v63_jerk_v074_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 21, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 63, 21).replace(0, np.nan)
    base = (sa / sb) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope-ratio 63v252
def f08mad_f08_moving_average_dynamics_sloperatio_63v252_jerk_v075_signal(closeadj):
    sa = _f08_ma_dynamics_slope(closeadj, 63, 21)
    sb = _f08_ma_dynamics_slope(closeadj, 252, 63).replace(0, np.nan)
    base = (sa / sb) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EMA-slope 21d
def f08mad_f08_moving_average_dynamics_emaslope_21d_jerk_v076_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    base = ema.diff(21) / ema.replace(0, np.nan).abs() * closeadj + _f08_ma_dynamics_slope(closeadj, 21, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EMA-slope 63d
def f08mad_f08_moving_average_dynamics_emaslope_63d_jerk_v077_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = ema.diff(21) / ema.replace(0, np.nan).abs() * closeadj + _f08_ma_dynamics_slope(closeadj, 63, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EMA-slope 252d
def f08mad_f08_moving_average_dynamics_emaslope_252d_jerk_v078_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = ema.diff(63) / ema.replace(0, np.nan).abs() * closeadj + _f08_ma_dynamics_slope(closeadj, 252, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of EMA-slope 504d
def f08mad_f08_moving_average_dynamics_emaslope_504d_jerk_v079_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252, adjust=False).mean()
    base = ema.diff(126) / ema.replace(0, np.nan).abs() * closeadj + _f08_ma_dynamics_slope(closeadj, 504, 126) * 0.0
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EMA-cross 21v63
def f08mad_f08_moving_average_dynamics_emacross_21v63_jerk_v080_signal(closeadj):
    fma = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    sma = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = (fma - sma) / sma.replace(0, np.nan).abs() * closeadj + _f08_ma_cross_diff(closeadj, 21, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EMA-cross 63v252
def f08mad_f08_moving_average_dynamics_emacross_63v252_jerk_v081_signal(closeadj):
    fma = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    sma = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = (fma - sma) / sma.replace(0, np.nan).abs() * closeadj + _f08_ma_cross_diff(closeadj, 63, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of MACD 12v26
def f08mad_f08_moving_average_dynamics_macd_12v26_jerk_v082_signal(closeadj):
    fma = closeadj.ewm(span=12, min_periods=6, adjust=False).mean()
    sma = closeadj.ewm(span=26, min_periods=13, adjust=False).mean()
    base = (fma - sma) + _f08_ma_cross_diff(closeadj, 12, 26) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of MACD signal line
def f08mad_f08_moving_average_dynamics_macd_signal_9d_jerk_v083_signal(closeadj):
    fma = closeadj.ewm(span=12, min_periods=6, adjust=False).mean()
    sma = closeadj.ewm(span=26, min_periods=13, adjust=False).mean()
    macd = (fma - sma)
    base = macd.ewm(span=9, min_periods=5, adjust=False).mean() + _f08_ma_cross_diff(closeadj, 12, 26) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of MACD slope 21d
def f08mad_f08_moving_average_dynamics_macd_slope_21d_jerk_v084_signal(closeadj):
    fma = closeadj.ewm(span=12, min_periods=6, adjust=False).mean()
    sma = closeadj.ewm(span=26, min_periods=13, adjust=False).mean()
    macd = (fma - sma)
    base = macd.diff(21) + _f08_ma_cross_diff(closeadj, 12, 26) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross × retvol (21v63)
def f08mad_f08_moving_average_dynamics_crossxretvol_21v63_jerk_v085_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f08_ma_cross_diff(closeadj, 21, 63) * rv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross × retvol (63v252)
def f08mad_f08_moving_average_dynamics_crossxretvol_63v252_jerk_v086_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f08_ma_cross_diff(closeadj, 63, 252) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cross × retvol (252v504)
def f08mad_f08_moving_average_dynamics_crossxretvol_252v504_jerk_v087_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f08_ma_cross_diff(closeadj, 252, 504) * rv * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × retvol (21d)
def f08mad_f08_moving_average_dynamics_slopexretvol_21d_jerk_v088_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * rv * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × retvol (63d)
def f08mad_f08_moving_average_dynamics_slopexretvol_63d_jerk_v089_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × retvol (252d)
def f08mad_f08_moving_average_dynamics_slopexretvol_252d_jerk_v090_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * rv * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope max
def f08mad_f08_moving_average_dynamics_slopemax_21d_jerk_v091_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = s.rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope max
def f08mad_f08_moving_average_dynamics_slopemax_63d_jerk_v092_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = s.rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d slope max
def f08mad_f08_moving_average_dynamics_slopemax_252d_jerk_v093_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = s.rolling(504, min_periods=126).max() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope min
def f08mad_f08_moving_average_dynamics_slopemin_21d_jerk_v094_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = s.rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope min
def f08mad_f08_moving_average_dynamics_slopemin_63d_jerk_v095_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = s.rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope-range
def f08mad_f08_moving_average_dynamics_sloperange_21d_jerk_v096_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = (s.rolling(63, min_periods=21).max() - s.rolling(63, min_periods=21).min()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope-range
def f08mad_f08_moving_average_dynamics_sloperange_63d_jerk_v097_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = (s.rolling(252, min_periods=63).max() - s.rolling(252, min_periods=63).min()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d slope-std
def f08mad_f08_moving_average_dynamics_slopestd_21d_jerk_v098_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = _std(s, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d slope-std
def f08mad_f08_moving_average_dynamics_slopestd_63d_jerk_v099_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = _std(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d slope-std
def f08mad_f08_moving_average_dynamics_slopestd_252d_jerk_v100_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = _std(s, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of cross 21v63 × volume z
def f08mad_f08_moving_average_dynamics_crossxvolz_21v63_jerk_v101_signal(closeadj, volume):
    base = _f08_ma_cross_diff(closeadj, 21, 63) * _z(volume, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross 63v252 × volume z
def f08mad_f08_moving_average_dynamics_crossxvolz_63v252_jerk_v102_signal(closeadj, volume):
    base = _f08_ma_cross_diff(closeadj, 63, 252) * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross 21v63 × dollar volume
def f08mad_f08_moving_average_dynamics_crossxdv_21v63_jerk_v103_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f08_ma_cross_diff(closeadj, 21, 63) * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross 63v252 × dollar volume
def f08mad_f08_moving_average_dynamics_crossxdv_63v252_jerk_v104_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f08_ma_cross_diff(closeadj, 63, 252) * _mean(dv, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cross 252v504 × dollar volume
def f08mad_f08_moving_average_dynamics_crossxdv_252v504_jerk_v105_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f08_ma_cross_diff(closeadj, 252, 504) * _mean(dv, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross 21v63 zscore
def f08mad_f08_moving_average_dynamics_crossz_short_21v63_jerk_v106_signal(closeadj):
    base = _z(_f08_ma_cross_diff(closeadj, 21, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross 252v504 zscore
def f08mad_f08_moving_average_dynamics_crossz_252v504_jerk_v107_signal(closeadj):
    base = _z(_f08_ma_cross_diff(closeadj, 252, 504), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × abs ret (21d)
def f08mad_f08_moving_average_dynamics_slopexabsret_21d_jerk_v108_signal(closeadj):
    ar = closeadj.pct_change().abs()
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * ar * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × abs ret (63d)
def f08mad_f08_moving_average_dynamics_slopexabsret_63d_jerk_v109_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * ar * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × abs ret (252d)
def f08mad_f08_moving_average_dynamics_slopexabsret_252d_jerk_v110_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * ar * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × price (21)
def f08mad_f08_moving_average_dynamics_accelxprice_21d_jerk_v111_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 21, 21) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel × price (63)
def f08mad_f08_moving_average_dynamics_accelxprice_63d_jerk_v112_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 63, 21) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel × price (252)
def f08mad_f08_moving_average_dynamics_accelxprice_252d_jerk_v113_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 252, 63) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accel × price (504)
def f08mad_f08_moving_average_dynamics_accelxprice_504d_jerk_v114_signal(closeadj):
    base = _f08_ma_dynamics_accel(closeadj, 504, 126) * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of accel z-score (21)
def f08mad_f08_moving_average_dynamics_accelz_21d_jerk_v115_signal(closeadj):
    base = _z(_f08_ma_dynamics_accel(closeadj, 21, 21), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel z-score (63)
def f08mad_f08_moving_average_dynamics_accelz_63d_jerk_v116_signal(closeadj):
    base = _z(_f08_ma_dynamics_accel(closeadj, 63, 21), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accel z-score (252)
def f08mad_f08_moving_average_dynamics_accelz_252d_jerk_v117_signal(closeadj):
    base = _z(_f08_ma_dynamics_accel(closeadj, 252, 63), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of fan-width squared
def f08mad_f08_moving_average_dynamics_fanwidthsq_21_252_jerk_v118_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 21, 63)
    b = _f08_ma_cross_diff(closeadj, 63, 252)
    df = pd.concat([a, b], axis=1)
    width = (df.max(axis=1) - df.min(axis=1))
    base = width * width.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of fan-width × volume z
def f08mad_f08_moving_average_dynamics_fanwidthxvolz_21_jerk_v119_signal(closeadj, volume):
    a = _f08_ma_cross_diff(closeadj, 21, 63)
    b = _f08_ma_cross_diff(closeadj, 63, 252)
    df = pd.concat([a, b], axis=1)
    width = (df.max(axis=1) - df.min(axis=1))
    base = width * _z(volume, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope-pct rank (21)
def f08mad_f08_moving_average_dynamics_slopepct_21d_jerk_v120_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = s.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope-pct rank (63)
def f08mad_f08_moving_average_dynamics_slopepct_63d_jerk_v121_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = s.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross-pct rank (21v63)
def f08mad_f08_moving_average_dynamics_crosspct_21v63_jerk_v122_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    base = c.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross-pct rank (63v252)
def f08mad_f08_moving_average_dynamics_crosspct_63v252_jerk_v123_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    base = c.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × range (21d)
def f08mad_f08_moving_average_dynamics_slopexrange_21d_jerk_v124_signal(closeadj, high, low):
    rng = (high - low)
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * rng * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × ATR (63d)
def f08mad_f08_moving_average_dynamics_slopexatr_63d_jerk_v125_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * atr * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × ATR (252d)
def f08mad_f08_moving_average_dynamics_slopexatr_252d_jerk_v126_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * atr * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope-squared (21d)
def f08mad_f08_moving_average_dynamics_slopesq_21d_jerk_v127_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = s * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope-squared (63d)
def f08mad_f08_moving_average_dynamics_slopesq_63d_jerk_v128_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = s * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope-squared (252d)
def f08mad_f08_moving_average_dynamics_slopesq_252d_jerk_v129_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = s * s.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of slope-squared (504d)
def f08mad_f08_moving_average_dynamics_slopesq_504d_jerk_v130_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 504, 126)
    base = s * s.abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × ret (21d)
def f08mad_f08_moving_average_dynamics_slopexret_21d_jerk_v131_signal(closeadj):
    r = closeadj.pct_change(21)
    base = _f08_ma_dynamics_slope(closeadj, 21, 21) * r * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × ret (63d)
def f08mad_f08_moving_average_dynamics_slopexret_63d_jerk_v132_signal(closeadj):
    r = closeadj.pct_change(63)
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × ret (252d)
def f08mad_f08_moving_average_dynamics_slopexret_252d_jerk_v133_signal(closeadj):
    r = closeadj.pct_change(252)
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross × ret (21v63)
def f08mad_f08_moving_average_dynamics_crossxret_21v63_jerk_v134_signal(closeadj):
    r = closeadj.pct_change(21)
    base = _f08_ma_cross_diff(closeadj, 21, 63) * r * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross × ret (63v252)
def f08mad_f08_moving_average_dynamics_crossxret_63v252_jerk_v135_signal(closeadj):
    r = closeadj.pct_change(63)
    base = _f08_ma_cross_diff(closeadj, 63, 252) * r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cross × ret (252v504)
def f08mad_f08_moving_average_dynamics_crossxret_252v504_jerk_v136_signal(closeadj):
    r = closeadj.pct_change(252)
    base = _f08_ma_cross_diff(closeadj, 252, 504) * r * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × skew (63d)
def f08mad_f08_moving_average_dynamics_slopexskew_63d_jerk_v137_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * sk * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × skew (252d)
def f08mad_f08_moving_average_dynamics_slopexskew_252d_jerk_v138_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * sk * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of slope × kurt (63d)
def f08mad_f08_moving_average_dynamics_slopexkurt_63d_jerk_v139_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f08_ma_dynamics_slope(closeadj, 63, 21) * kt * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of slope × kurt (252d)
def f08mad_f08_moving_average_dynamics_slopexkurt_252d_jerk_v140_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f08_ma_dynamics_slope(closeadj, 252, 63) * kt * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of Aroon proxy (21d)
def f08mad_f08_moving_average_dynamics_aroonproxy_21d_jerk_v141_signal(closeadj):
    fma = _sma(closeadj, 5)
    sma = _sma(closeadj, 21)
    inner = (fma - sma) / sma.replace(0, np.nan).abs()
    base = inner.rolling(21, min_periods=5).rank(pct=True) * closeadj + _f08_ma_cross_diff(closeadj, 5, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of Aroon proxy (63d)
def f08mad_f08_moving_average_dynamics_aroonproxy_63d_jerk_v142_signal(closeadj):
    fma = _sma(closeadj, 21)
    sma = _sma(closeadj, 63)
    inner = (fma - sma) / sma.replace(0, np.nan).abs()
    base = inner.rolling(63, min_periods=21).rank(pct=True) * closeadj + _f08_ma_cross_diff(closeadj, 21, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of Aroon proxy (252d)
def f08mad_f08_moving_average_dynamics_aroonproxy_252d_jerk_v143_signal(closeadj):
    fma = _sma(closeadj, 63)
    sma = _sma(closeadj, 252)
    inner = (fma - sma) / sma.replace(0, np.nan).abs()
    base = inner.rolling(252, min_periods=63).rank(pct=True) * closeadj + _f08_ma_cross_diff(closeadj, 63, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of Trix proxy (21d)
def f08mad_f08_moving_average_dynamics_trixproxy_21d_jerk_v144_signal(closeadj):
    e1 = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    e2 = e1.ewm(span=21, min_periods=11, adjust=False).mean()
    e3 = e2.ewm(span=21, min_periods=11, adjust=False).mean()
    base = e3.pct_change(21) * closeadj + _f08_ma_dynamics_slope(closeadj, 21, 21) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of Trix proxy (63d)
def f08mad_f08_moving_average_dynamics_trixproxy_63d_jerk_v145_signal(closeadj):
    e1 = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    e2 = e1.ewm(span=63, min_periods=32, adjust=False).mean()
    e3 = e2.ewm(span=63, min_periods=32, adjust=False).mean()
    base = e3.pct_change(63) * closeadj + _f08_ma_dynamics_slope(closeadj, 63, 21) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of Trix proxy (252d)
def f08mad_f08_moving_average_dynamics_trixproxy_252d_jerk_v146_signal(closeadj):
    e1 = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    e2 = e1.ewm(span=252, min_periods=126, adjust=False).mean()
    e3 = e2.ewm(span=252, min_periods=126, adjust=False).mean()
    base = e3.pct_change(63) * closeadj + _f08_ma_dynamics_slope(closeadj, 252, 63) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of cross × slope (21v63)
def f08mad_f08_moving_average_dynamics_crossslope_21v63_jerk_v147_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    base = c * s * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cross × slope (63v252)
def f08mad_f08_moving_average_dynamics_crossslope_63v252_jerk_v148_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    base = c * s * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of cross × slope (252v504)
def f08mad_f08_moving_average_dynamics_crossslope_252v504_jerk_v149_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    base = c * s * closeadj * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of composite alignment
def f08mad_f08_moving_average_dynamics_composite_align_jerk_v150_signal(closeadj):
    s1 = _f08_ma_dynamics_slope(closeadj, 21, 21)
    s2 = _f08_ma_dynamics_slope(closeadj, 252, 63)
    c = _f08_ma_cross_diff(closeadj, 21, 252)
    base = (s1 + s2 + c) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08mad_f08_moving_average_dynamics_slope_5d_jerk_v001_signal,
    f08mad_f08_moving_average_dynamics_slope_21d5_jerk_v002_signal,
    f08mad_f08_moving_average_dynamics_slope_21d21_jerk_v003_signal,
    f08mad_f08_moving_average_dynamics_slope_63d21_jerk_v004_signal,
    f08mad_f08_moving_average_dynamics_slope_63d63_jerk_v005_signal,
    f08mad_f08_moving_average_dynamics_slope_126d21_jerk_v006_signal,
    f08mad_f08_moving_average_dynamics_slope_126d63_jerk_v007_signal,
    f08mad_f08_moving_average_dynamics_slope_252d21_jerk_v008_signal,
    f08mad_f08_moving_average_dynamics_slope_252d63_jerk_v009_signal,
    f08mad_f08_moving_average_dynamics_slope_252d126_jerk_v010_signal,
    f08mad_f08_moving_average_dynamics_slope_504d63_jerk_v011_signal,
    f08mad_f08_moving_average_dynamics_slope_504d126_jerk_v012_signal,
    f08mad_f08_moving_average_dynamics_slope_504d252_jerk_v013_signal,
    f08mad_f08_moving_average_dynamics_cross_5v21_jerk_v014_signal,
    f08mad_f08_moving_average_dynamics_cross_21v63_jerk_v015_signal,
    f08mad_f08_moving_average_dynamics_cross_21v126_jerk_v016_signal,
    f08mad_f08_moving_average_dynamics_cross_21v252_jerk_v017_signal,
    f08mad_f08_moving_average_dynamics_cross_63v126_jerk_v018_signal,
    f08mad_f08_moving_average_dynamics_cross_63v252_jerk_v019_signal,
    f08mad_f08_moving_average_dynamics_cross_126v252_jerk_v020_signal,
    f08mad_f08_moving_average_dynamics_cross_252v504_jerk_v021_signal,
    f08mad_f08_moving_average_dynamics_accel_21d_jerk_v022_signal,
    f08mad_f08_moving_average_dynamics_accel_63d_jerk_v023_signal,
    f08mad_f08_moving_average_dynamics_accel_126d_jerk_v024_signal,
    f08mad_f08_moving_average_dynamics_accel_252d_jerk_v025_signal,
    f08mad_f08_moving_average_dynamics_accel_504d_jerk_v026_signal,
    f08mad_f08_moving_average_dynamics_slopez_21d_jerk_v027_signal,
    f08mad_f08_moving_average_dynamics_slopez_63d_jerk_v028_signal,
    f08mad_f08_moving_average_dynamics_slopez_252d_jerk_v029_signal,
    f08mad_f08_moving_average_dynamics_crossz_21v63_jerk_v030_signal,
    f08mad_f08_moving_average_dynamics_crossz_63v252_jerk_v031_signal,
    f08mad_f08_moving_average_dynamics_slopexprice_21d_jerk_v032_signal,
    f08mad_f08_moving_average_dynamics_slopexprice_63d_jerk_v033_signal,
    f08mad_f08_moving_average_dynamics_slopexprice_252d_jerk_v034_signal,
    f08mad_f08_moving_average_dynamics_fanwidth_5_252_jerk_v035_signal,
    f08mad_f08_moving_average_dynamics_fanwidth_21_252_jerk_v036_signal,
    f08mad_f08_moving_average_dynamics_fanwidth_63_504_jerk_v037_signal,
    f08mad_f08_moving_average_dynamics_crosssq_21v63_jerk_v038_signal,
    f08mad_f08_moving_average_dynamics_crosssq_63v252_jerk_v039_signal,
    f08mad_f08_moving_average_dynamics_crosssq_126v252_jerk_v040_signal,
    f08mad_f08_moving_average_dynamics_crosssq_252v504_jerk_v041_signal,
    f08mad_f08_moving_average_dynamics_crossroc_21v63_jerk_v042_signal,
    f08mad_f08_moving_average_dynamics_crossroc_63v252_jerk_v043_signal,
    f08mad_f08_moving_average_dynamics_crossmean_21v63_jerk_v044_signal,
    f08mad_f08_moving_average_dynamics_crossmean_63v252_jerk_v045_signal,
    f08mad_f08_moving_average_dynamics_crossstd_21v63_jerk_v046_signal,
    f08mad_f08_moving_average_dynamics_crossstd_63v252_jerk_v047_signal,
    f08mad_f08_moving_average_dynamics_slopexvolz_252d_jerk_v048_signal,
    f08mad_f08_moving_average_dynamics_slopexvolz_21d_jerk_v049_signal,
    f08mad_f08_moving_average_dynamics_slopexdv_63d_jerk_v050_signal,
    f08mad_f08_moving_average_dynamics_slopexdv_252d_jerk_v051_signal,
    f08mad_f08_moving_average_dynamics_slopenormatr_21d_jerk_v052_signal,
    f08mad_f08_moving_average_dynamics_slopenormatr_63d_jerk_v053_signal,
    f08mad_f08_moving_average_dynamics_slopenormatr_252d_jerk_v054_signal,
    f08mad_f08_moving_average_dynamics_crossxprice_21v63_jerk_v055_signal,
    f08mad_f08_moving_average_dynamics_crossxprice_63v252_jerk_v056_signal,
    f08mad_f08_moving_average_dynamics_crossxprice_252v504_jerk_v057_signal,
    f08mad_f08_moving_average_dynamics_slopexcross_21_jerk_v058_signal,
    f08mad_f08_moving_average_dynamics_slopexcross_63_jerk_v059_signal,
    f08mad_f08_moving_average_dynamics_slopexcross_252_jerk_v060_signal,
    f08mad_f08_moving_average_dynamics_slopesum_21d_jerk_v061_signal,
    f08mad_f08_moving_average_dynamics_slopesum_63d_jerk_v062_signal,
    f08mad_f08_moving_average_dynamics_slopesum_252d_jerk_v063_signal,
    f08mad_f08_moving_average_dynamics_slopepos_21d_jerk_v064_signal,
    f08mad_f08_moving_average_dynamics_slopepos_63d_jerk_v065_signal,
    f08mad_f08_moving_average_dynamics_slopepos_252d_jerk_v066_signal,
    f08mad_f08_moving_average_dynamics_crossroctotal_21v63_jerk_v067_signal,
    f08mad_f08_moving_average_dynamics_crossroctotal_63v252_jerk_v068_signal,
    f08mad_f08_moving_average_dynamics_crossroctotal_252v504_jerk_v069_signal,
    f08mad_f08_moving_average_dynamics_slopealign_21x252_jerk_v070_signal,
    f08mad_f08_moving_average_dynamics_slopealign_63x252_jerk_v071_signal,
    f08mad_f08_moving_average_dynamics_slopediff_21m252_jerk_v072_signal,
    f08mad_f08_moving_average_dynamics_slopediff_63m252_jerk_v073_signal,
    f08mad_f08_moving_average_dynamics_sloperatio_21v63_jerk_v074_signal,
    f08mad_f08_moving_average_dynamics_sloperatio_63v252_jerk_v075_signal,
    f08mad_f08_moving_average_dynamics_emaslope_21d_jerk_v076_signal,
    f08mad_f08_moving_average_dynamics_emaslope_63d_jerk_v077_signal,
    f08mad_f08_moving_average_dynamics_emaslope_252d_jerk_v078_signal,
    f08mad_f08_moving_average_dynamics_emaslope_504d_jerk_v079_signal,
    f08mad_f08_moving_average_dynamics_emacross_21v63_jerk_v080_signal,
    f08mad_f08_moving_average_dynamics_emacross_63v252_jerk_v081_signal,
    f08mad_f08_moving_average_dynamics_macd_12v26_jerk_v082_signal,
    f08mad_f08_moving_average_dynamics_macd_signal_9d_jerk_v083_signal,
    f08mad_f08_moving_average_dynamics_macd_slope_21d_jerk_v084_signal,
    f08mad_f08_moving_average_dynamics_crossxretvol_21v63_jerk_v085_signal,
    f08mad_f08_moving_average_dynamics_crossxretvol_63v252_jerk_v086_signal,
    f08mad_f08_moving_average_dynamics_crossxretvol_252v504_jerk_v087_signal,
    f08mad_f08_moving_average_dynamics_slopexretvol_21d_jerk_v088_signal,
    f08mad_f08_moving_average_dynamics_slopexretvol_63d_jerk_v089_signal,
    f08mad_f08_moving_average_dynamics_slopexretvol_252d_jerk_v090_signal,
    f08mad_f08_moving_average_dynamics_slopemax_21d_jerk_v091_signal,
    f08mad_f08_moving_average_dynamics_slopemax_63d_jerk_v092_signal,
    f08mad_f08_moving_average_dynamics_slopemax_252d_jerk_v093_signal,
    f08mad_f08_moving_average_dynamics_slopemin_21d_jerk_v094_signal,
    f08mad_f08_moving_average_dynamics_slopemin_63d_jerk_v095_signal,
    f08mad_f08_moving_average_dynamics_sloperange_21d_jerk_v096_signal,
    f08mad_f08_moving_average_dynamics_sloperange_63d_jerk_v097_signal,
    f08mad_f08_moving_average_dynamics_slopestd_21d_jerk_v098_signal,
    f08mad_f08_moving_average_dynamics_slopestd_63d_jerk_v099_signal,
    f08mad_f08_moving_average_dynamics_slopestd_252d_jerk_v100_signal,
    f08mad_f08_moving_average_dynamics_crossxvolz_21v63_jerk_v101_signal,
    f08mad_f08_moving_average_dynamics_crossxvolz_63v252_jerk_v102_signal,
    f08mad_f08_moving_average_dynamics_crossxdv_21v63_jerk_v103_signal,
    f08mad_f08_moving_average_dynamics_crossxdv_63v252_jerk_v104_signal,
    f08mad_f08_moving_average_dynamics_crossxdv_252v504_jerk_v105_signal,
    f08mad_f08_moving_average_dynamics_crossz_short_21v63_jerk_v106_signal,
    f08mad_f08_moving_average_dynamics_crossz_252v504_jerk_v107_signal,
    f08mad_f08_moving_average_dynamics_slopexabsret_21d_jerk_v108_signal,
    f08mad_f08_moving_average_dynamics_slopexabsret_63d_jerk_v109_signal,
    f08mad_f08_moving_average_dynamics_slopexabsret_252d_jerk_v110_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_21d_jerk_v111_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_63d_jerk_v112_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_252d_jerk_v113_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_504d_jerk_v114_signal,
    f08mad_f08_moving_average_dynamics_accelz_21d_jerk_v115_signal,
    f08mad_f08_moving_average_dynamics_accelz_63d_jerk_v116_signal,
    f08mad_f08_moving_average_dynamics_accelz_252d_jerk_v117_signal,
    f08mad_f08_moving_average_dynamics_fanwidthsq_21_252_jerk_v118_signal,
    f08mad_f08_moving_average_dynamics_fanwidthxvolz_21_jerk_v119_signal,
    f08mad_f08_moving_average_dynamics_slopepct_21d_jerk_v120_signal,
    f08mad_f08_moving_average_dynamics_slopepct_63d_jerk_v121_signal,
    f08mad_f08_moving_average_dynamics_crosspct_21v63_jerk_v122_signal,
    f08mad_f08_moving_average_dynamics_crosspct_63v252_jerk_v123_signal,
    f08mad_f08_moving_average_dynamics_slopexrange_21d_jerk_v124_signal,
    f08mad_f08_moving_average_dynamics_slopexatr_63d_jerk_v125_signal,
    f08mad_f08_moving_average_dynamics_slopexatr_252d_jerk_v126_signal,
    f08mad_f08_moving_average_dynamics_slopesq_21d_jerk_v127_signal,
    f08mad_f08_moving_average_dynamics_slopesq_63d_jerk_v128_signal,
    f08mad_f08_moving_average_dynamics_slopesq_252d_jerk_v129_signal,
    f08mad_f08_moving_average_dynamics_slopesq_504d_jerk_v130_signal,
    f08mad_f08_moving_average_dynamics_slopexret_21d_jerk_v131_signal,
    f08mad_f08_moving_average_dynamics_slopexret_63d_jerk_v132_signal,
    f08mad_f08_moving_average_dynamics_slopexret_252d_jerk_v133_signal,
    f08mad_f08_moving_average_dynamics_crossxret_21v63_jerk_v134_signal,
    f08mad_f08_moving_average_dynamics_crossxret_63v252_jerk_v135_signal,
    f08mad_f08_moving_average_dynamics_crossxret_252v504_jerk_v136_signal,
    f08mad_f08_moving_average_dynamics_slopexskew_63d_jerk_v137_signal,
    f08mad_f08_moving_average_dynamics_slopexskew_252d_jerk_v138_signal,
    f08mad_f08_moving_average_dynamics_slopexkurt_63d_jerk_v139_signal,
    f08mad_f08_moving_average_dynamics_slopexkurt_252d_jerk_v140_signal,
    f08mad_f08_moving_average_dynamics_aroonproxy_21d_jerk_v141_signal,
    f08mad_f08_moving_average_dynamics_aroonproxy_63d_jerk_v142_signal,
    f08mad_f08_moving_average_dynamics_aroonproxy_252d_jerk_v143_signal,
    f08mad_f08_moving_average_dynamics_trixproxy_21d_jerk_v144_signal,
    f08mad_f08_moving_average_dynamics_trixproxy_63d_jerk_v145_signal,
    f08mad_f08_moving_average_dynamics_trixproxy_252d_jerk_v146_signal,
    f08mad_f08_moving_average_dynamics_crossslope_21v63_jerk_v147_signal,
    f08mad_f08_moving_average_dynamics_crossslope_63v252_jerk_v148_signal,
    f08mad_f08_moving_average_dynamics_crossslope_252v504_jerk_v149_signal,
    f08mad_f08_moving_average_dynamics_composite_align_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_MOVING_AVERAGE_DYNAMICS_REGISTRY_JERK = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f08_moving_average_dynamics_3rd_derivatives_001_150_claude: {n_features} features pass")
