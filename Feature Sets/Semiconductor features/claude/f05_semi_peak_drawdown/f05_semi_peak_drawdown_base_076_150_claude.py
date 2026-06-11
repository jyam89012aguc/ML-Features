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
def _f05_dd(c, w):
    peak = c.rolling(w, min_periods=max(1, w // 2)).max()
    return (c - peak) / peak.replace(0, np.nan)


def _f05_runup(c, w):
    trough = c.rolling(w, min_periods=max(1, w // 2)).min()
    return (c - trough) / trough.replace(0, np.nan)


def _f05_log_dd(c, w):
    peak = c.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(c.replace(0, np.nan) / peak.replace(0, np.nan))

# 21d average drawdown
def f05pd_f05_semi_peak_drawdown_avgdd_21d_base_v076_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = _mean(d, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d average drawdown
def f05pd_f05_semi_peak_drawdown_avgdd_63d_base_v077_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = _mean(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d average drawdown
def f05pd_f05_semi_peak_drawdown_avgdd_126d_base_v078_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = _mean(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d average drawdown
def f05pd_f05_semi_peak_drawdown_avgdd_252d_base_v079_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d average drawdown
def f05pd_f05_semi_peak_drawdown_avgdd_504d_base_v080_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = _mean(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max drawdown (most negative)
def f05pd_f05_semi_peak_drawdown_maxdd_21d_base_v081_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = _min(d, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max drawdown (most negative)
def f05pd_f05_semi_peak_drawdown_maxdd_63d_base_v082_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = _min(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max drawdown (most negative)
def f05pd_f05_semi_peak_drawdown_maxdd_126d_base_v083_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = _min(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max drawdown (most negative)
def f05pd_f05_semi_peak_drawdown_maxdd_252d_base_v084_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = _min(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max drawdown (most negative)
def f05pd_f05_semi_peak_drawdown_maxdd_504d_base_v085_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = _min(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of drawdown
def f05pd_f05_semi_peak_drawdown_ddstd_21d_base_v086_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = _std(d, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of drawdown
def f05pd_f05_semi_peak_drawdown_ddstd_63d_base_v087_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = _std(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of drawdown
def f05pd_f05_semi_peak_drawdown_ddstd_126d_base_v088_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = _std(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of drawdown
def f05pd_f05_semi_peak_drawdown_ddstd_252d_base_v089_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = _std(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of drawdown
def f05pd_f05_semi_peak_drawdown_ddstd_504d_base_v090_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = _std(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst single-day return
def f05pd_f05_semi_peak_drawdown_worstday_21d_base_v091_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _min(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst single-day return
def f05pd_f05_semi_peak_drawdown_worstday_63d_base_v092_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _min(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d worst single-day return
def f05pd_f05_semi_peak_drawdown_worstday_126d_base_v093_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _min(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst single-day return
def f05pd_f05_semi_peak_drawdown_worstday_252d_base_v094_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _min(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst single-day return
def f05pd_f05_semi_peak_drawdown_worstday_504d_base_v095_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _min(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d best single-day return
def f05pd_f05_semi_peak_drawdown_bestday_21d_base_v096_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _max(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d best single-day return
def f05pd_f05_semi_peak_drawdown_bestday_63d_base_v097_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _max(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d best single-day return
def f05pd_f05_semi_peak_drawdown_bestday_126d_base_v098_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _max(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d best single-day return
def f05pd_f05_semi_peak_drawdown_bestday_252d_base_v099_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _max(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d best single-day return
def f05pd_f05_semi_peak_drawdown_bestday_504d_base_v100_signal(closeadj, high, low):
    r = closeadj.pct_change()
    result = _max(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d downside deviation (std of negative returns)
def f05pd_f05_semi_peak_drawdown_downsidedev_21d_base_v101_signal(closeadj, high, low):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = _std(neg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d downside deviation (std of negative returns)
def f05pd_f05_semi_peak_drawdown_downsidedev_63d_base_v102_signal(closeadj, high, low):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = _std(neg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d downside deviation (std of negative returns)
def f05pd_f05_semi_peak_drawdown_downsidedev_126d_base_v103_signal(closeadj, high, low):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = _std(neg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d downside deviation (std of negative returns)
def f05pd_f05_semi_peak_drawdown_downsidedev_252d_base_v104_signal(closeadj, high, low):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = _std(neg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d downside deviation (std of negative returns)
def f05pd_f05_semi_peak_drawdown_downsidedev_504d_base_v105_signal(closeadj, high, low):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    result = _std(neg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d upside deviation (std of positive returns)
def f05pd_f05_semi_peak_drawdown_upsidedev_21d_base_v106_signal(closeadj, high, low):
    r = closeadj.pct_change()
    pos = r.where(r > 0)
    result = _std(pos, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d upside deviation (std of positive returns)
def f05pd_f05_semi_peak_drawdown_upsidedev_63d_base_v107_signal(closeadj, high, low):
    r = closeadj.pct_change()
    pos = r.where(r > 0)
    result = _std(pos, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d upside deviation (std of positive returns)
def f05pd_f05_semi_peak_drawdown_upsidedev_126d_base_v108_signal(closeadj, high, low):
    r = closeadj.pct_change()
    pos = r.where(r > 0)
    result = _std(pos, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d upside deviation (std of positive returns)
def f05pd_f05_semi_peak_drawdown_upsidedev_252d_base_v109_signal(closeadj, high, low):
    r = closeadj.pct_change()
    pos = r.where(r > 0)
    result = _std(pos, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d upside deviation (std of positive returns)
def f05pd_f05_semi_peak_drawdown_upsidedev_504d_base_v110_signal(closeadj, high, low):
    r = closeadj.pct_change()
    pos = r.where(r > 0)
    result = _std(pos, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Calmar proxy: avg ret / |max drawdown|
def f05pd_f05_semi_peak_drawdown_calmar_21d_base_v111_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 21)
    mdd = _min(d, 21).abs()
    result = _mean(r, 21) / mdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Calmar proxy: avg ret / |max drawdown|
def f05pd_f05_semi_peak_drawdown_calmar_63d_base_v112_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 63)
    mdd = _min(d, 63).abs()
    result = _mean(r, 63) / mdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Calmar proxy: avg ret / |max drawdown|
def f05pd_f05_semi_peak_drawdown_calmar_126d_base_v113_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 126)
    mdd = _min(d, 126).abs()
    result = _mean(r, 126) / mdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Calmar proxy: avg ret / |max drawdown|
def f05pd_f05_semi_peak_drawdown_calmar_252d_base_v114_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 252)
    mdd = _min(d, 252).abs()
    result = _mean(r, 252) / mdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Calmar proxy: avg ret / |max drawdown|
def f05pd_f05_semi_peak_drawdown_calmar_504d_base_v115_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 504)
    mdd = _min(d, 504).abs()
    result = _mean(r, 504) / mdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ulcer index (RMS of drawdown)
def f05pd_f05_semi_peak_drawdown_ulcer_21d_base_v116_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ulcer index (RMS of drawdown)
def f05pd_f05_semi_peak_drawdown_ulcer_63d_base_v117_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ulcer index (RMS of drawdown)
def f05pd_f05_semi_peak_drawdown_ulcer_126d_base_v118_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ulcer index (RMS of drawdown)
def f05pd_f05_semi_peak_drawdown_ulcer_252d_base_v119_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ulcer index (RMS of drawdown)
def f05pd_f05_semi_peak_drawdown_ulcer_504d_base_v120_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pain ratio: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_painratio_21d_base_v121_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 21)
    ulc = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    result = _mean(r, 21) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pain ratio: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_painratio_63d_base_v122_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 63)
    ulc = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    result = _mean(r, 63) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pain ratio: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_painratio_126d_base_v123_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 126)
    ulc = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    result = _mean(r, 126) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pain ratio: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_painratio_252d_base_v124_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 252)
    ulc = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    result = _mean(r, 252) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pain ratio: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_painratio_504d_base_v125_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 504)
    ulc = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    result = _mean(r, 504) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean (high-close)/close
def f05pd_f05_semi_peak_drawdown_highclosegap_21d_base_v126_signal(closeadj, high, low):
    gap = (high - closeadj) / closeadj.replace(0, np.nan)
    result = _mean(gap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean (high-close)/close
def f05pd_f05_semi_peak_drawdown_highclosegap_63d_base_v127_signal(closeadj, high, low):
    gap = (high - closeadj) / closeadj.replace(0, np.nan)
    result = _mean(gap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean (high-close)/close
def f05pd_f05_semi_peak_drawdown_highclosegap_126d_base_v128_signal(closeadj, high, low):
    gap = (high - closeadj) / closeadj.replace(0, np.nan)
    result = _mean(gap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean (high-close)/close
def f05pd_f05_semi_peak_drawdown_highclosegap_252d_base_v129_signal(closeadj, high, low):
    gap = (high - closeadj) / closeadj.replace(0, np.nan)
    result = _mean(gap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean (high-close)/close
def f05pd_f05_semi_peak_drawdown_highclosegap_504d_base_v130_signal(closeadj, high, low):
    gap = (high - closeadj) / closeadj.replace(0, np.nan)
    result = _mean(gap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean (close-low)/close
def f05pd_f05_semi_peak_drawdown_closelowgap_21d_base_v131_signal(closeadj, high, low):
    gap = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _mean(gap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean (close-low)/close
def f05pd_f05_semi_peak_drawdown_closelowgap_63d_base_v132_signal(closeadj, high, low):
    gap = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _mean(gap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean (close-low)/close
def f05pd_f05_semi_peak_drawdown_closelowgap_126d_base_v133_signal(closeadj, high, low):
    gap = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _mean(gap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean (close-low)/close
def f05pd_f05_semi_peak_drawdown_closelowgap_252d_base_v134_signal(closeadj, high, low):
    gap = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _mean(gap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean (close-low)/close
def f05pd_f05_semi_peak_drawdown_closelowgap_504d_base_v135_signal(closeadj, high, low):
    gap = (closeadj - low) / closeadj.replace(0, np.nan)
    result = _mean(gap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean (high-low)/close
def f05pd_f05_semi_peak_drawdown_hlrange_21d_base_v136_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _mean(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean (high-low)/close
def f05pd_f05_semi_peak_drawdown_hlrange_63d_base_v137_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _mean(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean (high-low)/close
def f05pd_f05_semi_peak_drawdown_hlrange_126d_base_v138_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _mean(rng, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean (high-low)/close
def f05pd_f05_semi_peak_drawdown_hlrange_252d_base_v139_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _mean(rng, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean (high-low)/close
def f05pd_f05_semi_peak_drawdown_hlrange_504d_base_v140_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _mean(rng, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown deviation from longer mean
def f05pd_f05_semi_peak_drawdown_dddev_21d_base_v141_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    result = d - _mean(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown deviation from longer mean
def f05pd_f05_semi_peak_drawdown_dddev_63d_base_v142_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    result = d - _mean(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown deviation from longer mean
def f05pd_f05_semi_peak_drawdown_dddev_126d_base_v143_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    result = d - _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown deviation from longer mean
def f05pd_f05_semi_peak_drawdown_dddev_252d_base_v144_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    result = d - _mean(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown deviation from longer mean
def f05pd_f05_semi_peak_drawdown_dddev_504d_base_v145_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    result = d - _mean(d, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of drawdown
def f05pd_f05_semi_peak_drawdown_ddcomposite_short_base_v146_signal(closeadj, high, low):
    d21 = _f05_dd(closeadj, 21)
    d63 = _f05_dd(closeadj, 63)
    d126 = _f05_dd(closeadj, 126)
    result = _z(d21, 63) + _z(d63, 126) + _z(d126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of drawdown
def f05pd_f05_semi_peak_drawdown_ddcomposite_long_base_v147_signal(closeadj, high, low):
    d63 = _f05_dd(closeadj, 63)
    d126 = _f05_dd(closeadj, 126)
    d252 = _f05_dd(closeadj, 252)
    result = _z(d63, 126) + _z(d126, 252) + _z(d252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown regime divergence (short vs long EMA cross sign)
def f05pd_f05_semi_peak_drawdown_ddregime_divergence_base_v148_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    short = np.sign(d.ewm(span=21, adjust=False).mean() - d.ewm(span=63, adjust=False).mean())
    long = np.sign(d.ewm(span=126, adjust=False).mean() - d.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=d.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown quality: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_ddquality_63d_base_v149_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 63)
    ulc = (d ** 2).rolling(63, min_periods=32).mean() ** 0.5
    result = _mean(r, 63) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown quality: avg ret / ulcer
def f05pd_f05_semi_peak_drawdown_ddquality_252d_base_v150_signal(closeadj, high, low):
    r = closeadj.pct_change()
    d = _f05_dd(closeadj, 252)
    ulc = (d ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = _mean(r, 252) / ulc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


