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
def _f056_log_price(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    return lp.rolling(w, min_periods=max(1, w // 2)).mean()


def _f056_lr_slope(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    # slope of log price over w days (per-day log return slope)
    return (lp - lp.shift(w)) / float(w)


def _f056_lr_quality(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    slope = (lp - lp.shift(w)) / float(w)
    sd = lp.rolling(w, min_periods=max(1, w // 2)).std()
    return slope / sd.replace(0, np.nan)


# 21d log-price scaled by close
def f056lrs_f056_linear_regression_slope_logp_21d_base_v001_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d log-price scaled by close
def f056lrs_f056_linear_regression_slope_logp_42d_base_v002_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-price scaled by close
def f056lrs_f056_linear_regression_slope_logp_63d_base_v003_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-price scaled by close
def f056lrs_f056_linear_regression_slope_logp_126d_base_v004_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-price scaled by close
def f056lrs_f056_linear_regression_slope_logp_252d_base_v005_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-price scaled by close
def f056lrs_f056_linear_regression_slope_logp_504d_base_v006_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_5d_base_v007_signal(closeadj):
    result = _f056_lr_slope(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_10d_base_v008_signal(closeadj):
    result = _f056_lr_slope(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_21d_base_v009_signal(closeadj):
    result = _f056_lr_slope(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_42d_base_v010_signal(closeadj):
    result = _f056_lr_slope(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_63d_base_v011_signal(closeadj):
    result = _f056_lr_slope(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_126d_base_v012_signal(closeadj):
    result = _f056_lr_slope(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_189d_base_v013_signal(closeadj):
    result = _f056_lr_slope(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_252d_base_v014_signal(closeadj):
    result = _f056_lr_slope(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_378d_base_v015_signal(closeadj):
    result = _f056_lr_slope(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope scaled by close
def f056lrs_f056_linear_regression_slope_lrslope_504d_base_v016_signal(closeadj):
    result = _f056_lr_slope(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr quality scaled by close
def f056lrs_f056_linear_regression_slope_lrquality_21d_base_v017_signal(closeadj):
    result = _f056_lr_quality(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d lr quality scaled by close
def f056lrs_f056_linear_regression_slope_lrquality_42d_base_v018_signal(closeadj):
    result = _f056_lr_quality(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr quality scaled by close
def f056lrs_f056_linear_regression_slope_lrquality_63d_base_v019_signal(closeadj):
    result = _f056_lr_quality(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lr quality scaled by close
def f056lrs_f056_linear_regression_slope_lrquality_126d_base_v020_signal(closeadj):
    result = _f056_lr_quality(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr quality scaled by close
def f056lrs_f056_linear_regression_slope_lrquality_252d_base_v021_signal(closeadj):
    result = _f056_lr_quality(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr quality scaled by close
def f056lrs_f056_linear_regression_slope_lrquality_504d_base_v022_signal(closeadj):
    result = _f056_lr_quality(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-price minus close (gap)
def f056lrs_f056_linear_regression_slope_logpgap_21d_base_v023_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 21)
    result = (np.log(closeadj.replace(0, np.nan).abs()) - lp_mean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-price minus close (gap)
def f056lrs_f056_linear_regression_slope_logpgap_63d_base_v024_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 63)
    result = (np.log(closeadj.replace(0, np.nan).abs()) - lp_mean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-price minus close (gap)
def f056lrs_f056_linear_regression_slope_logpgap_252d_base_v025_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 252)
    result = (np.log(closeadj.replace(0, np.nan).abs()) - lp_mean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-price minus close (gap)
def f056lrs_f056_linear_regression_slope_logpgap_504d_base_v026_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 504)
    result = (np.log(closeadj.replace(0, np.nan).abs()) - lp_mean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope squared (curvature proxy) × close
def f056lrs_f056_linear_regression_slope_lrslopesq_21d_base_v027_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = (s * s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope squared × close
def f056lrs_f056_linear_regression_slope_lrslopesq_63d_base_v028_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = (s * s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope squared × close
def f056lrs_f056_linear_regression_slope_lrslopesq_252d_base_v029_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = (s * s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope squared × close
def f056lrs_f056_linear_regression_slope_lrslopesq_504d_base_v030_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = (s * s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope sign × close
def f056lrs_f056_linear_regression_slope_lrsign_21d_base_v031_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope sign × close
def f056lrs_f056_linear_regression_slope_lrsign_63d_base_v032_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope sign × close
def f056lrs_f056_linear_regression_slope_lrsign_252d_base_v033_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope sign × close
def f056lrs_f056_linear_regression_slope_lrsign_504d_base_v034_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope z-score × close
def f056lrs_f056_linear_regression_slope_lrslopez_21d_base_v035_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = _z(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope z-score × close
def f056lrs_f056_linear_regression_slope_lrslopez_63d_base_v036_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope z-score × close
def f056lrs_f056_linear_regression_slope_lrslopez_252d_base_v037_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope z-score × close
def f056lrs_f056_linear_regression_slope_lrslopez_504d_base_v038_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr quality z-score × close
def f056lrs_f056_linear_regression_slope_lrqualz_21d_base_v039_signal(closeadj):
    q = _f056_lr_quality(closeadj, 21)
    result = _z(q, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr quality z-score × close
def f056lrs_f056_linear_regression_slope_lrqualz_63d_base_v040_signal(closeadj):
    q = _f056_lr_quality(closeadj, 63)
    result = _z(q, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr quality z-score × close
def f056lrs_f056_linear_regression_slope_lrqualz_252d_base_v041_signal(closeadj):
    q = _f056_lr_quality(closeadj, 252)
    result = _z(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr quality z-score × close
def f056lrs_f056_linear_regression_slope_lrqualz_504d_base_v042_signal(closeadj):
    q = _f056_lr_quality(closeadj, 504)
    result = _z(q, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope EMA × close
def f056lrs_f056_linear_regression_slope_lrslopeema_21d_base_v043_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope EMA × close
def f056lrs_f056_linear_regression_slope_lrslopeema_63d_base_v044_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = s.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope EMA × close
def f056lrs_f056_linear_regression_slope_lrslopeema_252d_base_v045_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope EMA × close
def f056lrs_f056_linear_regression_slope_lrslopeema_504d_base_v046_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = s.ewm(span=126, min_periods=42).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope SMA × close
def f056lrs_f056_linear_regression_slope_lrslopesma_21d_base_v047_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = _mean(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope SMA × close
def f056lrs_f056_linear_regression_slope_lrslopesma_63d_base_v048_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = _mean(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope SMA × close
def f056lrs_f056_linear_regression_slope_lrslopesma_252d_base_v049_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = _mean(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope SMA × close
def f056lrs_f056_linear_regression_slope_lrslopesma_504d_base_v050_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = _mean(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope × log-price level
def f056lrs_f056_linear_regression_slope_slopexlevel_21d_base_v051_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    lp = _f056_log_price(closeadj, 21)
    result = s * lp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope × log-price level
def f056lrs_f056_linear_regression_slope_slopexlevel_63d_base_v052_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    lp = _f056_log_price(closeadj, 63)
    result = s * lp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope × log-price level
def f056lrs_f056_linear_regression_slope_slopexlevel_252d_base_v053_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    lp = _f056_log_price(closeadj, 252)
    result = s * lp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope × log-price level
def f056lrs_f056_linear_regression_slope_slopexlevel_504d_base_v054_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    lp = _f056_log_price(closeadj, 504)
    result = s * lp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope × 252d lr slope ratio × close
def f056lrs_f056_linear_regression_slope_sloperatio_21_252_base_v055_signal(closeadj):
    s_short = _f056_lr_slope(closeadj, 21)
    s_long = _f056_lr_slope(closeadj, 252)
    result = _safe_div(s_short, s_long.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope × 504d lr slope ratio × close
def f056lrs_f056_linear_regression_slope_sloperatio_63_504_base_v056_signal(closeadj):
    s_short = _f056_lr_slope(closeadj, 63)
    s_long = _f056_lr_slope(closeadj, 504)
    result = _safe_div(s_short, s_long.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr quality × 252d lr quality ratio × close
def f056lrs_f056_linear_regression_slope_qualratio_21_252_base_v057_signal(closeadj):
    q_short = _f056_lr_quality(closeadj, 21)
    q_long = _f056_lr_quality(closeadj, 252)
    result = _safe_div(q_short, q_long.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr quality × 504d lr quality ratio × close
def f056lrs_f056_linear_regression_slope_qualratio_63_504_base_v058_signal(closeadj):
    q_short = _f056_lr_quality(closeadj, 63)
    q_long = _f056_lr_quality(closeadj, 504)
    result = _safe_div(q_short, q_long.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope × volume-free intensity (slope × abs slope)
def f056lrs_f056_linear_regression_slope_slopeabsslope_21d_base_v059_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope × abs slope × close
def f056lrs_f056_linear_regression_slope_slopeabsslope_63d_base_v060_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope × abs slope × close
def f056lrs_f056_linear_regression_slope_slopeabsslope_252d_base_v061_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope × abs slope × close
def f056lrs_f056_linear_regression_slope_slopeabsslope_504d_base_v062_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = s * s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr quality × close × close (level-emphasized)
def f056lrs_f056_linear_regression_slope_qualxlevel_21d_base_v063_signal(closeadj):
    q = _f056_lr_quality(closeadj, 21)
    result = q * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr quality × close × close
def f056lrs_f056_linear_regression_slope_qualxlevel_63d_base_v064_signal(closeadj):
    q = _f056_lr_quality(closeadj, 63)
    result = q * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr quality × close × close
def f056lrs_f056_linear_regression_slope_qualxlevel_252d_base_v065_signal(closeadj):
    q = _f056_lr_quality(closeadj, 252)
    result = q * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr quality × close × close
def f056lrs_f056_linear_regression_slope_qualxlevel_504d_base_v066_signal(closeadj):
    q = _f056_lr_quality(closeadj, 504)
    result = q * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope × rolling close mean
def f056lrs_f056_linear_regression_slope_slopexmean_21d_base_v067_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope × rolling close mean
def f056lrs_f056_linear_regression_slope_slopexmean_63d_base_v068_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = s * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope × rolling close mean
def f056lrs_f056_linear_regression_slope_slopexmean_252d_base_v069_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope × rolling close mean
def f056lrs_f056_linear_regression_slope_slopexmean_504d_base_v070_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = s * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-price level squared × close
def f056lrs_f056_linear_regression_slope_logplevel_21d_base_v071_signal(closeadj):
    lp = _f056_log_price(closeadj, 21)
    result = _z(lp * lp, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-price level squared × close
def f056lrs_f056_linear_regression_slope_logplevel_63d_base_v072_signal(closeadj):
    lp = _f056_log_price(closeadj, 63)
    result = _z(lp * lp, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-price level squared × close
def f056lrs_f056_linear_regression_slope_logplevel_252d_base_v073_signal(closeadj):
    lp = _f056_log_price(closeadj, 252)
    result = (lp * lp) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-price level squared × close
def f056lrs_f056_linear_regression_slope_logplevel_504d_base_v074_signal(closeadj):
    lp = _f056_log_price(closeadj, 504)
    result = _z(lp * lp, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d annualized slope × close
def f056lrs_f056_linear_regression_slope_annslope_21d_base_v075_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s * 252.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f056lrs_f056_linear_regression_slope_logp_21d_base_v001_signal,
    f056lrs_f056_linear_regression_slope_logp_42d_base_v002_signal,
    f056lrs_f056_linear_regression_slope_logp_63d_base_v003_signal,
    f056lrs_f056_linear_regression_slope_logp_126d_base_v004_signal,
    f056lrs_f056_linear_regression_slope_logp_252d_base_v005_signal,
    f056lrs_f056_linear_regression_slope_logp_504d_base_v006_signal,
    f056lrs_f056_linear_regression_slope_lrslope_5d_base_v007_signal,
    f056lrs_f056_linear_regression_slope_lrslope_10d_base_v008_signal,
    f056lrs_f056_linear_regression_slope_lrslope_21d_base_v009_signal,
    f056lrs_f056_linear_regression_slope_lrslope_42d_base_v010_signal,
    f056lrs_f056_linear_regression_slope_lrslope_63d_base_v011_signal,
    f056lrs_f056_linear_regression_slope_lrslope_126d_base_v012_signal,
    f056lrs_f056_linear_regression_slope_lrslope_189d_base_v013_signal,
    f056lrs_f056_linear_regression_slope_lrslope_252d_base_v014_signal,
    f056lrs_f056_linear_regression_slope_lrslope_378d_base_v015_signal,
    f056lrs_f056_linear_regression_slope_lrslope_504d_base_v016_signal,
    f056lrs_f056_linear_regression_slope_lrquality_21d_base_v017_signal,
    f056lrs_f056_linear_regression_slope_lrquality_42d_base_v018_signal,
    f056lrs_f056_linear_regression_slope_lrquality_63d_base_v019_signal,
    f056lrs_f056_linear_regression_slope_lrquality_126d_base_v020_signal,
    f056lrs_f056_linear_regression_slope_lrquality_252d_base_v021_signal,
    f056lrs_f056_linear_regression_slope_lrquality_504d_base_v022_signal,
    f056lrs_f056_linear_regression_slope_logpgap_21d_base_v023_signal,
    f056lrs_f056_linear_regression_slope_logpgap_63d_base_v024_signal,
    f056lrs_f056_linear_regression_slope_logpgap_252d_base_v025_signal,
    f056lrs_f056_linear_regression_slope_logpgap_504d_base_v026_signal,
    f056lrs_f056_linear_regression_slope_lrslopesq_21d_base_v027_signal,
    f056lrs_f056_linear_regression_slope_lrslopesq_63d_base_v028_signal,
    f056lrs_f056_linear_regression_slope_lrslopesq_252d_base_v029_signal,
    f056lrs_f056_linear_regression_slope_lrslopesq_504d_base_v030_signal,
    f056lrs_f056_linear_regression_slope_lrsign_21d_base_v031_signal,
    f056lrs_f056_linear_regression_slope_lrsign_63d_base_v032_signal,
    f056lrs_f056_linear_regression_slope_lrsign_252d_base_v033_signal,
    f056lrs_f056_linear_regression_slope_lrsign_504d_base_v034_signal,
    f056lrs_f056_linear_regression_slope_lrslopez_21d_base_v035_signal,
    f056lrs_f056_linear_regression_slope_lrslopez_63d_base_v036_signal,
    f056lrs_f056_linear_regression_slope_lrslopez_252d_base_v037_signal,
    f056lrs_f056_linear_regression_slope_lrslopez_504d_base_v038_signal,
    f056lrs_f056_linear_regression_slope_lrqualz_21d_base_v039_signal,
    f056lrs_f056_linear_regression_slope_lrqualz_63d_base_v040_signal,
    f056lrs_f056_linear_regression_slope_lrqualz_252d_base_v041_signal,
    f056lrs_f056_linear_regression_slope_lrqualz_504d_base_v042_signal,
    f056lrs_f056_linear_regression_slope_lrslopeema_21d_base_v043_signal,
    f056lrs_f056_linear_regression_slope_lrslopeema_63d_base_v044_signal,
    f056lrs_f056_linear_regression_slope_lrslopeema_252d_base_v045_signal,
    f056lrs_f056_linear_regression_slope_lrslopeema_504d_base_v046_signal,
    f056lrs_f056_linear_regression_slope_lrslopesma_21d_base_v047_signal,
    f056lrs_f056_linear_regression_slope_lrslopesma_63d_base_v048_signal,
    f056lrs_f056_linear_regression_slope_lrslopesma_252d_base_v049_signal,
    f056lrs_f056_linear_regression_slope_lrslopesma_504d_base_v050_signal,
    f056lrs_f056_linear_regression_slope_slopexlevel_21d_base_v051_signal,
    f056lrs_f056_linear_regression_slope_slopexlevel_63d_base_v052_signal,
    f056lrs_f056_linear_regression_slope_slopexlevel_252d_base_v053_signal,
    f056lrs_f056_linear_regression_slope_slopexlevel_504d_base_v054_signal,
    f056lrs_f056_linear_regression_slope_sloperatio_21_252_base_v055_signal,
    f056lrs_f056_linear_regression_slope_sloperatio_63_504_base_v056_signal,
    f056lrs_f056_linear_regression_slope_qualratio_21_252_base_v057_signal,
    f056lrs_f056_linear_regression_slope_qualratio_63_504_base_v058_signal,
    f056lrs_f056_linear_regression_slope_slopeabsslope_21d_base_v059_signal,
    f056lrs_f056_linear_regression_slope_slopeabsslope_63d_base_v060_signal,
    f056lrs_f056_linear_regression_slope_slopeabsslope_252d_base_v061_signal,
    f056lrs_f056_linear_regression_slope_slopeabsslope_504d_base_v062_signal,
    f056lrs_f056_linear_regression_slope_qualxlevel_21d_base_v063_signal,
    f056lrs_f056_linear_regression_slope_qualxlevel_63d_base_v064_signal,
    f056lrs_f056_linear_regression_slope_qualxlevel_252d_base_v065_signal,
    f056lrs_f056_linear_regression_slope_qualxlevel_504d_base_v066_signal,
    f056lrs_f056_linear_regression_slope_slopexmean_21d_base_v067_signal,
    f056lrs_f056_linear_regression_slope_slopexmean_63d_base_v068_signal,
    f056lrs_f056_linear_regression_slope_slopexmean_252d_base_v069_signal,
    f056lrs_f056_linear_regression_slope_slopexmean_504d_base_v070_signal,
    f056lrs_f056_linear_regression_slope_logplevel_21d_base_v071_signal,
    f056lrs_f056_linear_regression_slope_logplevel_63d_base_v072_signal,
    f056lrs_f056_linear_regression_slope_logplevel_252d_base_v073_signal,
    f056lrs_f056_linear_regression_slope_logplevel_504d_base_v074_signal,
    f056lrs_f056_linear_regression_slope_annslope_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F056_LINEAR_REGRESSION_SLOPE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f056_log_price", "_f056_lr_slope", "_f056_lr_quality")
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
    print(f"OK f056_linear_regression_slope_base_001_075_claude: {n_features} features pass")
