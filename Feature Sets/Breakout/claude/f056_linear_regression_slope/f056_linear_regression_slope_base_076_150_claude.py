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
    return (lp - lp.shift(w)) / float(w)


def _f056_lr_quality(close, w):
    lp = np.log(close.replace(0, np.nan).abs())
    slope = (lp - lp.shift(w)) / float(w)
    sd = lp.rolling(w, min_periods=max(1, w // 2)).std()
    return slope / sd.replace(0, np.nan)


# 21d lr slope × 21d lr slope (longer window product)
def f056lrs_f056_linear_regression_slope_slopeprod_21_63_base_v076_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 21)
    s2 = _f056_lr_slope(closeadj, 63)
    result = s1 * s2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d × 252d slope product × close
def f056lrs_f056_linear_regression_slope_slopeprod_63_252_base_v077_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 63)
    s2 = _f056_lr_slope(closeadj, 252)
    result = s1 * s2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d × 504d slope product × close
def f056lrs_f056_linear_regression_slope_slopeprod_252_504_base_v078_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 252)
    s2 = _f056_lr_slope(closeadj, 504)
    result = s1 * s2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quality × 252d quality product × close
def f056lrs_f056_linear_regression_slope_qualprod_21_252_base_v079_signal(closeadj):
    q1 = _f056_lr_quality(closeadj, 21)
    q2 = _f056_lr_quality(closeadj, 252)
    result = q1 * q2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality × 504d quality product × close
def f056lrs_f056_linear_regression_slope_qualprod_63_504_base_v080_signal(closeadj):
    q1 = _f056_lr_quality(closeadj, 63)
    q2 = _f056_lr_quality(closeadj, 504)
    result = q1 * q2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log price minus 63d log price × close (level dispersion)
def f056lrs_f056_linear_regression_slope_logpdiff_21_63_base_v081_signal(closeadj):
    lp1 = _f056_log_price(closeadj, 21)
    lp2 = _f056_log_price(closeadj, 63)
    result = (lp1 - lp2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log price minus 252d log price × close
def f056lrs_f056_linear_regression_slope_logpdiff_63_252_base_v082_signal(closeadj):
    lp1 = _f056_log_price(closeadj, 63)
    lp2 = _f056_log_price(closeadj, 252)
    result = (lp1 - lp2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log price minus 504d log price × close
def f056lrs_f056_linear_regression_slope_logpdiff_21_504_base_v083_signal(closeadj):
    lp1 = _f056_log_price(closeadj, 21)
    lp2 = _f056_log_price(closeadj, 504)
    result = (lp1 - lp2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log price minus 504d log price × close
def f056lrs_f056_linear_regression_slope_logpdiff_126_504_base_v084_signal(closeadj):
    lp1 = _f056_log_price(closeadj, 126)
    lp2 = _f056_log_price(closeadj, 504)
    result = (lp1 - lp2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope rank (rolling)
def f056lrs_f056_linear_regression_slope_slopepct_21d_base_v085_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    rank = s.rolling(126, min_periods=21).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope rank
def f056lrs_f056_linear_regression_slope_slopepct_63d_base_v086_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    rank = s.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope rank
def f056lrs_f056_linear_regression_slope_slopepct_252d_base_v087_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    rank = s.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope rank
def f056lrs_f056_linear_regression_slope_slopepct_504d_base_v088_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    rank = s.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr quality rank × close
def f056lrs_f056_linear_regression_slope_qualpct_21d_base_v089_signal(closeadj):
    q = _f056_lr_quality(closeadj, 21)
    rank = q.rolling(126, min_periods=21).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr quality rank × close
def f056lrs_f056_linear_regression_slope_qualpct_63d_base_v090_signal(closeadj):
    q = _f056_lr_quality(closeadj, 63)
    rank = q.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr quality rank × close
def f056lrs_f056_linear_regression_slope_qualpct_252d_base_v091_signal(closeadj):
    q = _f056_lr_quality(closeadj, 252)
    rank = q.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr quality rank × close
def f056lrs_f056_linear_regression_slope_qualpct_504d_base_v092_signal(closeadj):
    q = _f056_lr_quality(closeadj, 504)
    rank = q.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lr slope × close × close (square level)
def f056lrs_f056_linear_regression_slope_slopelevelsq_5d_base_v093_signal(closeadj):
    s = _f056_lr_slope(closeadj, 5)
    result = s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d lr slope × close × close
def f056lrs_f056_linear_regression_slope_slopelevelsq_10d_base_v094_signal(closeadj):
    s = _f056_lr_slope(closeadj, 10)
    result = s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d lr slope × close × close
def f056lrs_f056_linear_regression_slope_slopelevelsq_42d_base_v095_signal(closeadj):
    s = _f056_lr_slope(closeadj, 42)
    result = s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d lr slope × close × close
def f056lrs_f056_linear_regression_slope_slopelevelsq_126d_base_v096_signal(closeadj):
    s = _f056_lr_slope(closeadj, 126)
    result = s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d lr slope × close × close
def f056lrs_f056_linear_regression_slope_slopelevelsq_189d_base_v097_signal(closeadj):
    s = _f056_lr_slope(closeadj, 189)
    result = s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d lr slope × close × close
def f056lrs_f056_linear_regression_slope_slopelevelsq_378d_base_v098_signal(closeadj):
    s = _f056_lr_slope(closeadj, 378)
    result = s * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d log price level × close
def f056lrs_f056_linear_regression_slope_logp_5d_base_v099_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d log price level × close
def f056lrs_f056_linear_regression_slope_logp_10d_base_v100_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 189d log price level × close
def f056lrs_f056_linear_regression_slope_logp_189d_base_v101_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 378d log price level × close
def f056lrs_f056_linear_regression_slope_logp_378d_base_v102_signal(closeadj):
    result = _z(_f056_log_price(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lr quality × close
def f056lrs_f056_linear_regression_slope_qual_5d_base_v103_signal(closeadj):
    result = _f056_lr_quality(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d lr quality × close
def f056lrs_f056_linear_regression_slope_qual_10d_base_v104_signal(closeadj):
    result = _f056_lr_quality(closeadj, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d lr quality × close
def f056lrs_f056_linear_regression_slope_qual_189d_base_v105_signal(closeadj):
    result = _f056_lr_quality(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d lr quality × close
def f056lrs_f056_linear_regression_slope_qual_378d_base_v106_signal(closeadj):
    result = _f056_lr_quality(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope sign × _mean(close, 63)
def f056lrs_f056_linear_regression_slope_signxsmamean_21d_base_v107_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = np.sign(s) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope sign × _mean(close, 252)
def f056lrs_f056_linear_regression_slope_signxsmamean_63d_base_v108_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = np.sign(s) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope sign × _mean(close, 504)
def f056lrs_f056_linear_regression_slope_signxsmamean_252d_base_v109_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = np.sign(s) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope sign × _mean(close, 504)
def f056lrs_f056_linear_regression_slope_signxsmamean_504d_base_v110_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = np.sign(s) * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log price level × log price level (variance proxy) × close
def f056lrs_f056_linear_regression_slope_logpvar_21d_base_v111_signal(closeadj):
    lp = _f056_log_price(closeadj, 21)
    lp_long = _f056_log_price(closeadj, 252)
    result = (lp - lp_long) * (lp - lp_long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log price gap squared × close
def f056lrs_f056_linear_regression_slope_logpvar_63d_base_v112_signal(closeadj):
    lp = _f056_log_price(closeadj, 63)
    lp_long = _f056_log_price(closeadj, 252)
    result = (lp - lp_long) * (lp - lp_long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log price gap squared × close
def f056lrs_f056_linear_regression_slope_logpvar_252d_base_v113_signal(closeadj):
    lp = _f056_log_price(closeadj, 252)
    lp_long = _f056_log_price(closeadj, 504)
    result = (lp - lp_long) * (lp - lp_long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log price gap squared × close
def f056lrs_f056_linear_regression_slope_logpvar_504d_base_v114_signal(closeadj):
    lp = _f056_log_price(closeadj, 504)
    lp_long = _f056_log_price(closeadj, 504)
    result = (lp.shift(126) - lp_long) * (lp.shift(126) - lp_long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope * lr quality × close
def f056lrs_f056_linear_regression_slope_slopexqual_21d_base_v115_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    q = _f056_lr_quality(closeadj, 21)
    result = s * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope * lr quality × close
def f056lrs_f056_linear_regression_slope_slopexqual_63d_base_v116_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    q = _f056_lr_quality(closeadj, 63)
    result = s * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope * lr quality × close
def f056lrs_f056_linear_regression_slope_slopexqual_252d_base_v117_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    q = _f056_lr_quality(closeadj, 252)
    result = s * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope * lr quality × close
def f056lrs_f056_linear_regression_slope_slopexqual_504d_base_v118_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    q = _f056_lr_quality(closeadj, 504)
    result = s * q * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope short minus slope long × close (slope divergence)
def f056lrs_f056_linear_regression_slope_slopediv_21_63_base_v119_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 21)
    s2 = _f056_lr_slope(closeadj, 63)
    result = (s1 - s2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope short minus slope long 63 vs 252 × close
def f056lrs_f056_linear_regression_slope_slopediv_63_252_base_v120_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 63)
    s2 = _f056_lr_slope(closeadj, 252)
    result = (s1 - s2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# slope divergence 252-504 × close
def f056lrs_f056_linear_regression_slope_slopediv_252_504_base_v121_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 252)
    s2 = _f056_lr_slope(closeadj, 504)
    result = (s1 - s2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr slope absolute × close
def f056lrs_f056_linear_regression_slope_absslope_21d_base_v122_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr slope absolute × close
def f056lrs_f056_linear_regression_slope_absslope_63d_base_v123_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr slope absolute × close
def f056lrs_f056_linear_regression_slope_absslope_252d_base_v124_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr slope absolute × close
def f056lrs_f056_linear_regression_slope_absslope_504d_base_v125_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = s.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lr quality absolute × close
def f056lrs_f056_linear_regression_slope_absqual_21d_base_v126_signal(closeadj):
    q = _f056_lr_quality(closeadj, 21)
    result = q.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lr quality absolute × close
def f056lrs_f056_linear_regression_slope_absqual_63d_base_v127_signal(closeadj):
    q = _f056_lr_quality(closeadj, 63)
    result = q.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lr quality absolute × close
def f056lrs_f056_linear_regression_slope_absqual_252d_base_v128_signal(closeadj):
    q = _f056_lr_quality(closeadj, 252)
    result = q.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d lr quality absolute × close
def f056lrs_f056_linear_regression_slope_absqual_504d_base_v129_signal(closeadj):
    q = _f056_lr_quality(closeadj, 504)
    result = q.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × close power (cubed level)
def f056lrs_f056_linear_regression_slope_slopecubed_21d_base_v130_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s * (closeadj ** 3) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope × cubed close / 100
def f056lrs_f056_linear_regression_slope_slopecubed_63d_base_v131_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = s * (closeadj ** 3) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope × cubed close / 100
def f056lrs_f056_linear_regression_slope_slopecubed_252d_base_v132_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s * (closeadj ** 3) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope × cubed close / 100
def f056lrs_f056_linear_regression_slope_slopecubed_504d_base_v133_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = s * (closeadj ** 3) / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log price gap (close vs mean) z-score × close
def f056lrs_f056_linear_regression_slope_lpgapz_21d_base_v134_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 21)
    gap = np.log(closeadj.replace(0, np.nan).abs()) - lp_mean
    result = _z(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log price gap z-score × close
def f056lrs_f056_linear_regression_slope_lpgapz_63d_base_v135_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 63)
    gap = np.log(closeadj.replace(0, np.nan).abs()) - lp_mean
    result = _z(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log price gap z-score × close
def f056lrs_f056_linear_regression_slope_lpgapz_252d_base_v136_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 252)
    gap = np.log(closeadj.replace(0, np.nan).abs()) - lp_mean
    result = _z(gap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log price gap z-score × close
def f056lrs_f056_linear_regression_slope_lpgapz_504d_base_v137_signal(closeadj):
    lp_mean = _f056_log_price(closeadj, 504)
    gap = np.log(closeadj.replace(0, np.nan).abs()) - lp_mean
    result = _z(gap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope EMA span 5 × close
def f056lrs_f056_linear_regression_slope_slopeema5_21d_base_v138_signal(closeadj):
    s = _f056_lr_slope(closeadj, 21)
    result = s.ewm(span=5, min_periods=3).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope EMA span 5 × close
def f056lrs_f056_linear_regression_slope_slopeema5_63d_base_v139_signal(closeadj):
    s = _f056_lr_slope(closeadj, 63)
    result = s.ewm(span=5, min_periods=3).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope EMA span 21 × close
def f056lrs_f056_linear_regression_slope_slopeema21_252d_base_v140_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d slope EMA span 21 × close
def f056lrs_f056_linear_regression_slope_slopeema21_504d_base_v141_signal(closeadj):
    s = _f056_lr_slope(closeadj, 504)
    result = s.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quality EMA span 21 × close
def f056lrs_f056_linear_regression_slope_qualema21_21d_base_v142_signal(closeadj):
    q = _f056_lr_quality(closeadj, 21)
    result = q.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality EMA span 63 × close
def f056lrs_f056_linear_regression_slope_qualema63_63d_base_v143_signal(closeadj):
    q = _f056_lr_quality(closeadj, 63)
    result = q.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality EMA span 63 × close
def f056lrs_f056_linear_regression_slope_qualema63_252d_base_v144_signal(closeadj):
    q = _f056_lr_quality(closeadj, 252)
    result = q.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quality EMA span 126 × close
def f056lrs_f056_linear_regression_slope_qualema126_504d_base_v145_signal(closeadj):
    q = _f056_lr_quality(closeadj, 504)
    result = q.ewm(span=126, min_periods=42).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope × close + 252d slope × close (combined)
def f056lrs_f056_linear_regression_slope_slopecombo_21_252_base_v146_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 21)
    s2 = _f056_lr_slope(closeadj, 252)
    result = (s1 + s2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d + 504d combined slope × close
def f056lrs_f056_linear_regression_slope_slopecombo_63_504_base_v147_signal(closeadj):
    s1 = _f056_lr_slope(closeadj, 63)
    s2 = _f056_lr_slope(closeadj, 504)
    result = (s1 + s2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d + 252d quality combined × close
def f056lrs_f056_linear_regression_slope_qualcombo_21_252_base_v148_signal(closeadj):
    q1 = _f056_lr_quality(closeadj, 21)
    q2 = _f056_lr_quality(closeadj, 252)
    result = (q1 + q2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d + 504d quality combined × close
def f056lrs_f056_linear_regression_slope_qualcombo_63_504_base_v149_signal(closeadj):
    q1 = _f056_lr_quality(closeadj, 63)
    q2 = _f056_lr_quality(closeadj, 504)
    result = (q1 + q2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d annualized lr slope × close
def f056lrs_f056_linear_regression_slope_annslope_252d_base_v150_signal(closeadj):
    s = _f056_lr_slope(closeadj, 252)
    result = s * 252.0 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f056lrs_f056_linear_regression_slope_slopeprod_21_63_base_v076_signal,
    f056lrs_f056_linear_regression_slope_slopeprod_63_252_base_v077_signal,
    f056lrs_f056_linear_regression_slope_slopeprod_252_504_base_v078_signal,
    f056lrs_f056_linear_regression_slope_qualprod_21_252_base_v079_signal,
    f056lrs_f056_linear_regression_slope_qualprod_63_504_base_v080_signal,
    f056lrs_f056_linear_regression_slope_logpdiff_21_63_base_v081_signal,
    f056lrs_f056_linear_regression_slope_logpdiff_63_252_base_v082_signal,
    f056lrs_f056_linear_regression_slope_logpdiff_21_504_base_v083_signal,
    f056lrs_f056_linear_regression_slope_logpdiff_126_504_base_v084_signal,
    f056lrs_f056_linear_regression_slope_slopepct_21d_base_v085_signal,
    f056lrs_f056_linear_regression_slope_slopepct_63d_base_v086_signal,
    f056lrs_f056_linear_regression_slope_slopepct_252d_base_v087_signal,
    f056lrs_f056_linear_regression_slope_slopepct_504d_base_v088_signal,
    f056lrs_f056_linear_regression_slope_qualpct_21d_base_v089_signal,
    f056lrs_f056_linear_regression_slope_qualpct_63d_base_v090_signal,
    f056lrs_f056_linear_regression_slope_qualpct_252d_base_v091_signal,
    f056lrs_f056_linear_regression_slope_qualpct_504d_base_v092_signal,
    f056lrs_f056_linear_regression_slope_slopelevelsq_5d_base_v093_signal,
    f056lrs_f056_linear_regression_slope_slopelevelsq_10d_base_v094_signal,
    f056lrs_f056_linear_regression_slope_slopelevelsq_42d_base_v095_signal,
    f056lrs_f056_linear_regression_slope_slopelevelsq_126d_base_v096_signal,
    f056lrs_f056_linear_regression_slope_slopelevelsq_189d_base_v097_signal,
    f056lrs_f056_linear_regression_slope_slopelevelsq_378d_base_v098_signal,
    f056lrs_f056_linear_regression_slope_logp_5d_base_v099_signal,
    f056lrs_f056_linear_regression_slope_logp_10d_base_v100_signal,
    f056lrs_f056_linear_regression_slope_logp_189d_base_v101_signal,
    f056lrs_f056_linear_regression_slope_logp_378d_base_v102_signal,
    f056lrs_f056_linear_regression_slope_qual_5d_base_v103_signal,
    f056lrs_f056_linear_regression_slope_qual_10d_base_v104_signal,
    f056lrs_f056_linear_regression_slope_qual_189d_base_v105_signal,
    f056lrs_f056_linear_regression_slope_qual_378d_base_v106_signal,
    f056lrs_f056_linear_regression_slope_signxsmamean_21d_base_v107_signal,
    f056lrs_f056_linear_regression_slope_signxsmamean_63d_base_v108_signal,
    f056lrs_f056_linear_regression_slope_signxsmamean_252d_base_v109_signal,
    f056lrs_f056_linear_regression_slope_signxsmamean_504d_base_v110_signal,
    f056lrs_f056_linear_regression_slope_logpvar_21d_base_v111_signal,
    f056lrs_f056_linear_regression_slope_logpvar_63d_base_v112_signal,
    f056lrs_f056_linear_regression_slope_logpvar_252d_base_v113_signal,
    f056lrs_f056_linear_regression_slope_logpvar_504d_base_v114_signal,
    f056lrs_f056_linear_regression_slope_slopexqual_21d_base_v115_signal,
    f056lrs_f056_linear_regression_slope_slopexqual_63d_base_v116_signal,
    f056lrs_f056_linear_regression_slope_slopexqual_252d_base_v117_signal,
    f056lrs_f056_linear_regression_slope_slopexqual_504d_base_v118_signal,
    f056lrs_f056_linear_regression_slope_slopediv_21_63_base_v119_signal,
    f056lrs_f056_linear_regression_slope_slopediv_63_252_base_v120_signal,
    f056lrs_f056_linear_regression_slope_slopediv_252_504_base_v121_signal,
    f056lrs_f056_linear_regression_slope_absslope_21d_base_v122_signal,
    f056lrs_f056_linear_regression_slope_absslope_63d_base_v123_signal,
    f056lrs_f056_linear_regression_slope_absslope_252d_base_v124_signal,
    f056lrs_f056_linear_regression_slope_absslope_504d_base_v125_signal,
    f056lrs_f056_linear_regression_slope_absqual_21d_base_v126_signal,
    f056lrs_f056_linear_regression_slope_absqual_63d_base_v127_signal,
    f056lrs_f056_linear_regression_slope_absqual_252d_base_v128_signal,
    f056lrs_f056_linear_regression_slope_absqual_504d_base_v129_signal,
    f056lrs_f056_linear_regression_slope_slopecubed_21d_base_v130_signal,
    f056lrs_f056_linear_regression_slope_slopecubed_63d_base_v131_signal,
    f056lrs_f056_linear_regression_slope_slopecubed_252d_base_v132_signal,
    f056lrs_f056_linear_regression_slope_slopecubed_504d_base_v133_signal,
    f056lrs_f056_linear_regression_slope_lpgapz_21d_base_v134_signal,
    f056lrs_f056_linear_regression_slope_lpgapz_63d_base_v135_signal,
    f056lrs_f056_linear_regression_slope_lpgapz_252d_base_v136_signal,
    f056lrs_f056_linear_regression_slope_lpgapz_504d_base_v137_signal,
    f056lrs_f056_linear_regression_slope_slopeema5_21d_base_v138_signal,
    f056lrs_f056_linear_regression_slope_slopeema5_63d_base_v139_signal,
    f056lrs_f056_linear_regression_slope_slopeema21_252d_base_v140_signal,
    f056lrs_f056_linear_regression_slope_slopeema21_504d_base_v141_signal,
    f056lrs_f056_linear_regression_slope_qualema21_21d_base_v142_signal,
    f056lrs_f056_linear_regression_slope_qualema63_63d_base_v143_signal,
    f056lrs_f056_linear_regression_slope_qualema63_252d_base_v144_signal,
    f056lrs_f056_linear_regression_slope_qualema126_504d_base_v145_signal,
    f056lrs_f056_linear_regression_slope_slopecombo_21_252_base_v146_signal,
    f056lrs_f056_linear_regression_slope_slopecombo_63_504_base_v147_signal,
    f056lrs_f056_linear_regression_slope_qualcombo_21_252_base_v148_signal,
    f056lrs_f056_linear_regression_slope_qualcombo_63_504_base_v149_signal,
    f056lrs_f056_linear_regression_slope_annslope_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F056_LINEAR_REGRESSION_SLOPE_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f056_linear_regression_slope_base_076_150_claude: {n_features} features pass")
