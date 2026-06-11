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


# 21d EMA slope over 21d
def f08mad_f08_moving_average_dynamics_emaslope_21d_base_v076_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    base = ema.diff(21) / ema.replace(0, np.nan).abs()
    result = (base + _f08_ma_dynamics_slope(closeadj, 21, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA slope over 21d
def f08mad_f08_moving_average_dynamics_emaslope_63d_base_v077_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = ema.diff(21) / ema.replace(0, np.nan).abs()
    result = (base + _f08_ma_dynamics_slope(closeadj, 63, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA slope over 63d
def f08mad_f08_moving_average_dynamics_emaslope_252d_base_v078_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = ema.diff(63) / ema.replace(0, np.nan).abs()
    result = (base + _f08_ma_dynamics_slope(closeadj, 252, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA slope over 126d
def f08mad_f08_moving_average_dynamics_emaslope_504d_base_v079_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252, adjust=False).mean()
    base = ema.diff(126) / ema.replace(0, np.nan).abs()
    result = (base + _f08_ma_dynamics_slope(closeadj, 504, 126) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA cross 21v63
def f08mad_f08_moving_average_dynamics_emacross_21v63_base_v080_signal(closeadj):
    fma = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    sma = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = (fma - sma) / sma.replace(0, np.nan).abs()
    result = (base + _f08_ma_cross_diff(closeadj, 21, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA cross 63v252
def f08mad_f08_moving_average_dynamics_emacross_63v252_base_v081_signal(closeadj):
    fma = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    sma = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = (fma - sma) / sma.replace(0, np.nan).abs()
    result = (base + _f08_ma_cross_diff(closeadj, 63, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MACD-style: 12-26 EMA distance
def f08mad_f08_moving_average_dynamics_macd_12v26_base_v082_signal(closeadj):
    fma = closeadj.ewm(span=12, min_periods=6, adjust=False).mean()
    sma = closeadj.ewm(span=26, min_periods=13, adjust=False).mean()
    base = (fma - sma)
    result = (base + _f08_ma_cross_diff(closeadj, 12, 26) * 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# MACD signal line: 9d EMA of MACD
def f08mad_f08_moving_average_dynamics_macd_signal_9d_base_v083_signal(closeadj):
    fma = closeadj.ewm(span=12, min_periods=6, adjust=False).mean()
    sma = closeadj.ewm(span=26, min_periods=13, adjust=False).mean()
    macd = (fma - sma)
    base = macd.ewm(span=9, min_periods=5, adjust=False).mean()
    result = (base + _f08_ma_cross_diff(closeadj, 12, 26) * 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of MACD
def f08mad_f08_moving_average_dynamics_macd_slope_21d_base_v084_signal(closeadj):
    fma = closeadj.ewm(span=12, min_periods=6, adjust=False).mean()
    sma = closeadj.ewm(span=26, min_periods=13, adjust=False).mean()
    macd = (fma - sma)
    base = macd.diff(21)
    result = (base + _f08_ma_cross_diff(closeadj, 12, 26) * 0.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross weighted by retvol
def f08mad_f08_moving_average_dynamics_crossxretvol_21v63_base_v085_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f08_ma_cross_diff(closeadj, 21, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross weighted by 63d retvol
def f08mad_f08_moving_average_dynamics_crossxretvol_63v252_base_v086_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f08_ma_cross_diff(closeadj, 63, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross weighted by 63d retvol
def f08mad_f08_moving_average_dynamics_crossxretvol_252v504_base_v087_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f08_ma_cross_diff(closeadj, 252, 504) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × 21d retvol
def f08mad_f08_moving_average_dynamics_slopexretvol_21d_base_v088_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × 63d retvol
def f08mad_f08_moving_average_dynamics_slopexretvol_63d_base_v089_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × 63d retvol
def f08mad_f08_moving_average_dynamics_slopexretvol_252d_base_v090_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of 21d slope over 63d
def f08mad_f08_moving_average_dynamics_slopemax_21d_base_v091_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = s.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of 63d slope over 252d
def f08mad_f08_moving_average_dynamics_slopemax_63d_base_v092_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = s.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of 252d slope over 504d
def f08mad_f08_moving_average_dynamics_slopemax_252d_base_v093_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = s.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of 21d slope over 63d
def f08mad_f08_moving_average_dynamics_slopemin_21d_base_v094_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = s.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of 63d slope over 252d
def f08mad_f08_moving_average_dynamics_slopemin_63d_base_v095_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = s.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope range (max-min of slope) over 63d
def f08mad_f08_moving_average_dynamics_sloperange_21d_base_v096_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = (s.rolling(63, min_periods=21).max() - s.rolling(63, min_periods=21).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope range over 252d
def f08mad_f08_moving_average_dynamics_sloperange_63d_base_v097_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = (s.rolling(252, min_periods=63).max() - s.rolling(252, min_periods=63).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope rolling std (slope volatility)
def f08mad_f08_moving_average_dynamics_slopestd_21d_base_v098_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = _std(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope rolling std
def f08mad_f08_moving_average_dynamics_slopestd_63d_base_v099_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = _std(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope rolling std
def f08mad_f08_moving_average_dynamics_slopestd_252d_base_v100_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = _std(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross × volume z
def f08mad_f08_moving_average_dynamics_crossxvolz_21v63_base_v101_signal(closeadj, volume):
    result = _f08_ma_cross_diff(closeadj, 21, 63) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross × volume z
def f08mad_f08_moving_average_dynamics_crossxvolz_63v252_base_v102_signal(closeadj, volume):
    result = _f08_ma_cross_diff(closeadj, 63, 252) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross × dollar volume mean
def f08mad_f08_moving_average_dynamics_crossxdv_21v63_base_v103_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f08_ma_cross_diff(closeadj, 21, 63) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cross × dollar volume mean
def f08mad_f08_moving_average_dynamics_crossxdv_63v252_base_v104_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f08_ma_cross_diff(closeadj, 63, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cross × dollar volume
def f08mad_f08_moving_average_dynamics_crossxdv_252v504_base_v105_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f08_ma_cross_diff(closeadj, 252, 504) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cross zscore over 63d
def f08mad_f08_moving_average_dynamics_crossz_short_21v63_base_v106_signal(closeadj):
    result = _z(_f08_ma_cross_diff(closeadj, 21, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross zscore over 504d
def f08mad_f08_moving_average_dynamics_crossz_252v504_base_v107_signal(closeadj):
    result = _z(_f08_ma_cross_diff(closeadj, 252, 504), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × abs return
def f08mad_f08_moving_average_dynamics_slopexabsret_21d_base_v108_signal(closeadj):
    ar = closeadj.pct_change().abs()
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × abs return mean
def f08mad_f08_moving_average_dynamics_slopexabsret_63d_base_v109_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × abs return mean
def f08mad_f08_moving_average_dynamics_slopexabsret_252d_base_v110_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel × close (21d)
def f08mad_f08_moving_average_dynamics_accelxprice_21d_base_v111_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 21, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel × close (63d)
def f08mad_f08_moving_average_dynamics_accelxprice_63d_base_v112_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 63, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel × close (252d)
def f08mad_f08_moving_average_dynamics_accelxprice_252d_base_v113_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 252, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# accel × close (504d)
def f08mad_f08_moving_average_dynamics_accelxprice_504d_base_v114_signal(closeadj):
    result = _f08_ma_dynamics_accel(closeadj, 504, 126) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel zscore over 63d
def f08mad_f08_moving_average_dynamics_accelz_21d_base_v115_signal(closeadj):
    result = _z(_f08_ma_dynamics_accel(closeadj, 21, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel zscore over 252d
def f08mad_f08_moving_average_dynamics_accelz_63d_base_v116_signal(closeadj):
    result = _z(_f08_ma_dynamics_accel(closeadj, 63, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d accel zscore over 504d
def f08mad_f08_moving_average_dynamics_accelz_252d_base_v117_signal(closeadj):
    result = _z(_f08_ma_dynamics_accel(closeadj, 252, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out width over 21/63/252 SMAs squared
def f08mad_f08_moving_average_dynamics_fanwidthsq_21_252_base_v118_signal(closeadj):
    a = _f08_ma_cross_diff(closeadj, 21, 63)
    b = _f08_ma_cross_diff(closeadj, 63, 252)
    df = pd.concat([a, b], axis=1)
    width = (df.max(axis=1) - df.min(axis=1))
    result = width * width.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fan-out width × volume z
def f08mad_f08_moving_average_dynamics_fanwidthxvolz_21_base_v119_signal(closeadj, volume):
    a = _f08_ma_cross_diff(closeadj, 21, 63)
    b = _f08_ma_cross_diff(closeadj, 63, 252)
    df = pd.concat([a, b], axis=1)
    width = (df.max(axis=1) - df.min(axis=1))
    result = width * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope rolling rank percentile over 252d
def f08mad_f08_moving_average_dynamics_slopepct_21d_base_v120_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = s.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope rolling rank percentile over 504d
def f08mad_f08_moving_average_dynamics_slopepct_63d_base_v121_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = s.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 cross rolling rank percentile over 252d
def f08mad_f08_moving_average_dynamics_crosspct_21v63_base_v122_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    result = c.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross rolling rank percentile over 504d
def f08mad_f08_moving_average_dynamics_crosspct_63v252_base_v123_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    result = c.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × intraday range
def f08mad_f08_moving_average_dynamics_slopexrange_21d_base_v124_signal(closeadj, high, low):
    rng = (high - low)
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × ATR
def f08mad_f08_moving_average_dynamics_slopexatr_63d_base_v125_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × 63d ATR
def f08mad_f08_moving_average_dynamics_slopexatr_252d_base_v126_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope ROC squared (intensity)
def f08mad_f08_moving_average_dynamics_slopesq_21d_base_v127_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope squared
def f08mad_f08_moving_average_dynamics_slopesq_63d_base_v128_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope squared
def f08mad_f08_moving_average_dynamics_slopesq_252d_base_v129_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope squared
def f08mad_f08_moving_average_dynamics_slopesq_504d_base_v130_signal(closeadj):
    s = _f08_ma_dynamics_slope(closeadj, 504, 126)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × 21d return
def f08mad_f08_moving_average_dynamics_slopexret_21d_base_v131_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f08_ma_dynamics_slope(closeadj, 21, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × 63d return
def f08mad_f08_moving_average_dynamics_slopexret_63d_base_v132_signal(closeadj):
    r = closeadj.pct_change(63)
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × 252d return
def f08mad_f08_moving_average_dynamics_slopexret_252d_base_v133_signal(closeadj):
    r = closeadj.pct_change(252)
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 cross × 21d return
def f08mad_f08_moving_average_dynamics_crossxret_21v63_base_v134_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f08_ma_cross_diff(closeadj, 21, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross × 63d return
def f08mad_f08_moving_average_dynamics_crossxret_63v252_base_v135_signal(closeadj):
    r = closeadj.pct_change(63)
    result = _f08_ma_cross_diff(closeadj, 63, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross × 252d return
def f08mad_f08_moving_average_dynamics_crossxret_252v504_base_v136_signal(closeadj):
    r = closeadj.pct_change(252)
    result = _f08_ma_cross_diff(closeadj, 252, 504) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × 21d skew
def f08mad_f08_moving_average_dynamics_slopexskew_63d_base_v137_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × 252d skew
def f08mad_f08_moving_average_dynamics_slopexskew_252d_base_v138_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × 63d kurt
def f08mad_f08_moving_average_dynamics_slopexkurt_63d_base_v139_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f08_ma_dynamics_slope(closeadj, 63, 21) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × 252d kurt
def f08mad_f08_moving_average_dynamics_slopexkurt_252d_base_v140_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f08_ma_dynamics_slope(closeadj, 252, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Aroon-style: 21d days since high vs low — proxy by max position normalized
def f08mad_f08_moving_average_dynamics_aroonproxy_21d_base_v141_signal(closeadj):
    fma = _sma(closeadj, 5)
    sma = _sma(closeadj, 21)
    base = (fma - sma) / sma.replace(0, np.nan).abs()
    result = base.rolling(21, min_periods=5).rank(pct=True) * closeadj + _f08_ma_cross_diff(closeadj, 5, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Aroon-style 63d
def f08mad_f08_moving_average_dynamics_aroonproxy_63d_base_v142_signal(closeadj):
    fma = _sma(closeadj, 21)
    sma = _sma(closeadj, 63)
    base = (fma - sma) / sma.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=21).rank(pct=True) * closeadj + _f08_ma_cross_diff(closeadj, 21, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Aroon 252d
def f08mad_f08_moving_average_dynamics_aroonproxy_252d_base_v143_signal(closeadj):
    fma = _sma(closeadj, 63)
    sma = _sma(closeadj, 252)
    base = (fma - sma) / sma.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj + _f08_ma_cross_diff(closeadj, 63, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Trix proxy: 21d slope of triple EMA
def f08mad_f08_moving_average_dynamics_trixproxy_21d_base_v144_signal(closeadj):
    e1 = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    e2 = e1.ewm(span=21, min_periods=11, adjust=False).mean()
    e3 = e2.ewm(span=21, min_periods=11, adjust=False).mean()
    base = e3.pct_change(21)
    result = (base + _f08_ma_dynamics_slope(closeadj, 21, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Trix 63d
def f08mad_f08_moving_average_dynamics_trixproxy_63d_base_v145_signal(closeadj):
    e1 = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    e2 = e1.ewm(span=63, min_periods=32, adjust=False).mean()
    e3 = e2.ewm(span=63, min_periods=32, adjust=False).mean()
    base = e3.pct_change(63)
    result = (base + _f08_ma_dynamics_slope(closeadj, 63, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Trix 252d
def f08mad_f08_moving_average_dynamics_trixproxy_252d_base_v146_signal(closeadj):
    e1 = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    e2 = e1.ewm(span=252, min_periods=126, adjust=False).mean()
    e3 = e2.ewm(span=252, min_periods=126, adjust=False).mean()
    base = e3.pct_change(63)
    result = (base + _f08_ma_dynamics_slope(closeadj, 252, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 cross times 21d slope (alignment intensity)
def f08mad_f08_moving_average_dynamics_crossslope_21v63_base_v147_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 21, 63)
    s = _f08_ma_dynamics_slope(closeadj, 21, 21)
    result = c * s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 cross times 63d slope
def f08mad_f08_moving_average_dynamics_crossslope_63v252_base_v148_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 63, 252)
    s = _f08_ma_dynamics_slope(closeadj, 63, 21)
    result = c * s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252v504 cross times 252d slope
def f08mad_f08_moving_average_dynamics_crossslope_252v504_base_v149_signal(closeadj):
    c = _f08_ma_cross_diff(closeadj, 252, 504)
    s = _f08_ma_dynamics_slope(closeadj, 252, 63)
    result = c * s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite alignment: 21d slope + 252d slope + 21v252 cross
def f08mad_f08_moving_average_dynamics_composite_align_base_v150_signal(closeadj):
    s1 = _f08_ma_dynamics_slope(closeadj, 21, 21)
    s2 = _f08_ma_dynamics_slope(closeadj, 252, 63)
    c = _f08_ma_cross_diff(closeadj, 21, 252)
    result = (s1 + s2 + c) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08mad_f08_moving_average_dynamics_emaslope_21d_base_v076_signal,
    f08mad_f08_moving_average_dynamics_emaslope_63d_base_v077_signal,
    f08mad_f08_moving_average_dynamics_emaslope_252d_base_v078_signal,
    f08mad_f08_moving_average_dynamics_emaslope_504d_base_v079_signal,
    f08mad_f08_moving_average_dynamics_emacross_21v63_base_v080_signal,
    f08mad_f08_moving_average_dynamics_emacross_63v252_base_v081_signal,
    f08mad_f08_moving_average_dynamics_macd_12v26_base_v082_signal,
    f08mad_f08_moving_average_dynamics_macd_signal_9d_base_v083_signal,
    f08mad_f08_moving_average_dynamics_macd_slope_21d_base_v084_signal,
    f08mad_f08_moving_average_dynamics_crossxretvol_21v63_base_v085_signal,
    f08mad_f08_moving_average_dynamics_crossxretvol_63v252_base_v086_signal,
    f08mad_f08_moving_average_dynamics_crossxretvol_252v504_base_v087_signal,
    f08mad_f08_moving_average_dynamics_slopexretvol_21d_base_v088_signal,
    f08mad_f08_moving_average_dynamics_slopexretvol_63d_base_v089_signal,
    f08mad_f08_moving_average_dynamics_slopexretvol_252d_base_v090_signal,
    f08mad_f08_moving_average_dynamics_slopemax_21d_base_v091_signal,
    f08mad_f08_moving_average_dynamics_slopemax_63d_base_v092_signal,
    f08mad_f08_moving_average_dynamics_slopemax_252d_base_v093_signal,
    f08mad_f08_moving_average_dynamics_slopemin_21d_base_v094_signal,
    f08mad_f08_moving_average_dynamics_slopemin_63d_base_v095_signal,
    f08mad_f08_moving_average_dynamics_sloperange_21d_base_v096_signal,
    f08mad_f08_moving_average_dynamics_sloperange_63d_base_v097_signal,
    f08mad_f08_moving_average_dynamics_slopestd_21d_base_v098_signal,
    f08mad_f08_moving_average_dynamics_slopestd_63d_base_v099_signal,
    f08mad_f08_moving_average_dynamics_slopestd_252d_base_v100_signal,
    f08mad_f08_moving_average_dynamics_crossxvolz_21v63_base_v101_signal,
    f08mad_f08_moving_average_dynamics_crossxvolz_63v252_base_v102_signal,
    f08mad_f08_moving_average_dynamics_crossxdv_21v63_base_v103_signal,
    f08mad_f08_moving_average_dynamics_crossxdv_63v252_base_v104_signal,
    f08mad_f08_moving_average_dynamics_crossxdv_252v504_base_v105_signal,
    f08mad_f08_moving_average_dynamics_crossz_short_21v63_base_v106_signal,
    f08mad_f08_moving_average_dynamics_crossz_252v504_base_v107_signal,
    f08mad_f08_moving_average_dynamics_slopexabsret_21d_base_v108_signal,
    f08mad_f08_moving_average_dynamics_slopexabsret_63d_base_v109_signal,
    f08mad_f08_moving_average_dynamics_slopexabsret_252d_base_v110_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_21d_base_v111_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_63d_base_v112_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_252d_base_v113_signal,
    f08mad_f08_moving_average_dynamics_accelxprice_504d_base_v114_signal,
    f08mad_f08_moving_average_dynamics_accelz_21d_base_v115_signal,
    f08mad_f08_moving_average_dynamics_accelz_63d_base_v116_signal,
    f08mad_f08_moving_average_dynamics_accelz_252d_base_v117_signal,
    f08mad_f08_moving_average_dynamics_fanwidthsq_21_252_base_v118_signal,
    f08mad_f08_moving_average_dynamics_fanwidthxvolz_21_base_v119_signal,
    f08mad_f08_moving_average_dynamics_slopepct_21d_base_v120_signal,
    f08mad_f08_moving_average_dynamics_slopepct_63d_base_v121_signal,
    f08mad_f08_moving_average_dynamics_crosspct_21v63_base_v122_signal,
    f08mad_f08_moving_average_dynamics_crosspct_63v252_base_v123_signal,
    f08mad_f08_moving_average_dynamics_slopexrange_21d_base_v124_signal,
    f08mad_f08_moving_average_dynamics_slopexatr_63d_base_v125_signal,
    f08mad_f08_moving_average_dynamics_slopexatr_252d_base_v126_signal,
    f08mad_f08_moving_average_dynamics_slopesq_21d_base_v127_signal,
    f08mad_f08_moving_average_dynamics_slopesq_63d_base_v128_signal,
    f08mad_f08_moving_average_dynamics_slopesq_252d_base_v129_signal,
    f08mad_f08_moving_average_dynamics_slopesq_504d_base_v130_signal,
    f08mad_f08_moving_average_dynamics_slopexret_21d_base_v131_signal,
    f08mad_f08_moving_average_dynamics_slopexret_63d_base_v132_signal,
    f08mad_f08_moving_average_dynamics_slopexret_252d_base_v133_signal,
    f08mad_f08_moving_average_dynamics_crossxret_21v63_base_v134_signal,
    f08mad_f08_moving_average_dynamics_crossxret_63v252_base_v135_signal,
    f08mad_f08_moving_average_dynamics_crossxret_252v504_base_v136_signal,
    f08mad_f08_moving_average_dynamics_slopexskew_63d_base_v137_signal,
    f08mad_f08_moving_average_dynamics_slopexskew_252d_base_v138_signal,
    f08mad_f08_moving_average_dynamics_slopexkurt_63d_base_v139_signal,
    f08mad_f08_moving_average_dynamics_slopexkurt_252d_base_v140_signal,
    f08mad_f08_moving_average_dynamics_aroonproxy_21d_base_v141_signal,
    f08mad_f08_moving_average_dynamics_aroonproxy_63d_base_v142_signal,
    f08mad_f08_moving_average_dynamics_aroonproxy_252d_base_v143_signal,
    f08mad_f08_moving_average_dynamics_trixproxy_21d_base_v144_signal,
    f08mad_f08_moving_average_dynamics_trixproxy_63d_base_v145_signal,
    f08mad_f08_moving_average_dynamics_trixproxy_252d_base_v146_signal,
    f08mad_f08_moving_average_dynamics_crossslope_21v63_base_v147_signal,
    f08mad_f08_moving_average_dynamics_crossslope_63v252_base_v148_signal,
    f08mad_f08_moving_average_dynamics_crossslope_252v504_base_v149_signal,
    f08mad_f08_moving_average_dynamics_composite_align_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_MOVING_AVERAGE_DYNAMICS_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f08_moving_average_dynamics_base_076_150_claude: {n_features} features pass")
