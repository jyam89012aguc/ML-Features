"""Family f078 - TTM versus annual consistency (Fundamental Dynamics) | Sharadar tables: SF1 | fields: dimension, revenue, ncfo, netinc, rnd | base 076-150"""
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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _ttm_vs_annual_consistency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ttm_vs_annual_consistency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ttm_vs_annual_consistency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of dimension/ncfo
def tvac_f078_ttm_vs_annual_consistency_log_per_ncfo_504d_base_v076_signal(dimension, ncfo):
    s = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of dimension/netinc
def tvac_f078_ttm_vs_annual_consistency_log_per_netinc_252d_base_v077_signal(dimension, netinc):
    s = _ttm_vs_annual_consistency_scaled(dimension, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of dimension/netinc
def tvac_f078_ttm_vs_annual_consistency_log_per_netinc_504d_base_v078_signal(dimension, netinc):
    s = _ttm_vs_annual_consistency_scaled(dimension, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_ewm_21d_base_v079_signal(dimension, closeadj):
    result = dimension.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_ewm_63d_base_v080_signal(dimension, closeadj):
    result = dimension.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_ewm_252d_base_v081_signal(dimension, closeadj):
    result = dimension.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_med_63d_base_v082_signal(dimension, closeadj):
    result = dimension.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_med_252d_base_v083_signal(dimension, closeadj):
    result = dimension.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_med_504d_base_v084_signal(dimension, closeadj):
    result = dimension.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of dimension
def tvac_f078_ttm_vs_annual_consistency_skew_252d_base_v085_signal(dimension):
    result = dimension.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of dimension
def tvac_f078_ttm_vs_annual_consistency_skew_504d_base_v086_signal(dimension):
    result = dimension.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of dimension
def tvac_f078_ttm_vs_annual_consistency_kurt_252d_base_v087_signal(dimension):
    result = dimension.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of dimension
def tvac_f078_ttm_vs_annual_consistency_kurt_504d_base_v088_signal(dimension):
    result = dimension.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_rank_252d_base_v089_signal(dimension, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = dimension.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_rank_504d_base_v090_signal(dimension, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = dimension.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_rank_1008d_base_v091_signal(dimension, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = dimension.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of dimension from 63d mean times closeadj
def tvac_f078_ttm_vs_annual_consistency_devmean_63d_base_v092_signal(dimension, closeadj):
    m = _mean(dimension, 63)
    result = (dimension - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of dimension from 252d mean times closeadj
def tvac_f078_ttm_vs_annual_consistency_devmean_252d_base_v093_signal(dimension, closeadj):
    m = _mean(dimension, 252)
    result = (dimension - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of dimension from 504d mean times closeadj
def tvac_f078_ttm_vs_annual_consistency_devmean_504d_base_v094_signal(dimension, closeadj):
    m = _mean(dimension, 504)
    result = (dimension - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_logdiff_21d_base_v095_signal(dimension, closeadj):
    lr = _ttm_vs_annual_consistency_log(dimension)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_logdiff_63d_base_v096_signal(dimension, closeadj):
    lr = _ttm_vs_annual_consistency_log(dimension)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_logdiff_252d_base_v097_signal(dimension, closeadj):
    lr = _ttm_vs_annual_consistency_log(dimension)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_range_63d_base_v098_signal(dimension, closeadj):
    hi = dimension.rolling(63, min_periods=max(1, 63//2)).max()
    lo = dimension.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_range_252d_base_v099_signal(dimension, closeadj):
    hi = dimension.rolling(252, min_periods=max(1, 252//2)).max()
    lo = dimension.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_range_504d_base_v100_signal(dimension, closeadj):
    hi = dimension.rolling(504, min_periods=max(1, 504//2)).max()
    lo = dimension.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 252d mean times closeadj
def tvac_f078_ttm_vs_annual_consistency_rel_252d_base_v101_signal(dimension, closeadj):
    m = _mean(dimension, 252).replace(0, np.nan)
    result = (dimension / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 504d mean times closeadj
def tvac_f078_ttm_vs_annual_consistency_rel_504d_base_v102_signal(dimension, closeadj):
    m = _mean(dimension, 504).replace(0, np.nan)
    result = (dimension / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dimension relative to 1008d mean times closeadj
def tvac_f078_ttm_vs_annual_consistency_rel_1008d_base_v103_signal(dimension, closeadj):
    m = _mean(dimension, 1008).replace(0, np.nan)
    result = (dimension / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dimension/revenue 63d mean
def tvac_f078_ttm_vs_annual_consistency_sqnorm_revenue_63d_base_v104_signal(dimension, revenue):
    r = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dimension/revenue 252d mean
def tvac_f078_ttm_vs_annual_consistency_sqnorm_revenue_252d_base_v105_signal(dimension, revenue):
    r = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dimension/ncfo 63d mean
def tvac_f078_ttm_vs_annual_consistency_sqnorm_ncfo_63d_base_v106_signal(dimension, ncfo):
    r = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dimension/ncfo 252d mean
def tvac_f078_ttm_vs_annual_consistency_sqnorm_ncfo_252d_base_v107_signal(dimension, ncfo):
    r = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dimension/netinc 63d mean
def tvac_f078_ttm_vs_annual_consistency_sqnorm_netinc_63d_base_v108_signal(dimension, netinc):
    r = _ttm_vs_annual_consistency_scaled(dimension, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dimension/netinc 252d mean
def tvac_f078_ttm_vs_annual_consistency_sqnorm_netinc_252d_base_v109_signal(dimension, netinc):
    r = _ttm_vs_annual_consistency_scaled(dimension, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_infrat_63d_base_v110_signal(dimension, closeadj):
    m = _mean(dimension, 63)
    s = _std(dimension, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_infrat_252d_base_v111_signal(dimension, closeadj):
    m = _mean(dimension, 252)
    s = _std(dimension, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_infrat_504d_base_v112_signal(dimension, closeadj):
    m = _mean(dimension, 504)
    s = _std(dimension, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of dimension
def tvac_f078_ttm_vs_annual_consistency_cv_252d_base_v113_signal(dimension):
    m = _mean(dimension, 252).abs().replace(0, np.nan)
    s = _std(dimension, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of dimension
def tvac_f078_ttm_vs_annual_consistency_cv_504d_base_v114_signal(dimension):
    m = _mean(dimension, 504).abs().replace(0, np.nan)
    s = _std(dimension, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_5d_base_v115_signal(dimension, closeadj):
    result = dimension.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_21d_base_v116_signal(dimension, closeadj):
    result = dimension.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_63d_base_v117_signal(dimension, closeadj):
    result = dimension.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_252d_base_v118_signal(dimension, closeadj):
    result = dimension.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(dimension) / mean(revenue) x closeadj
def tvac_f078_ttm_vs_annual_consistency_cumper_revenue_252d_base_v119_signal(dimension, revenue, closeadj):
    s = dimension.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(dimension) / mean(revenue) x closeadj
def tvac_f078_ttm_vs_annual_consistency_cumper_revenue_504d_base_v120_signal(dimension, revenue, closeadj):
    s = dimension.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(dimension) / mean(ncfo) x closeadj
def tvac_f078_ttm_vs_annual_consistency_cumper_ncfo_252d_base_v121_signal(dimension, ncfo, closeadj):
    s = dimension.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ncfo, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(dimension) / mean(ncfo) x closeadj
def tvac_f078_ttm_vs_annual_consistency_cumper_ncfo_504d_base_v122_signal(dimension, ncfo, closeadj):
    s = dimension.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ncfo, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_pos_63d_base_v123_signal(dimension, closeadj):
    pos = dimension.where(dimension > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_pos_252d_base_v124_signal(dimension, closeadj):
    pos = dimension.where(dimension > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_neg_63d_base_v125_signal(dimension, closeadj):
    neg = dimension.where(dimension < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_neg_252d_base_v126_signal(dimension, closeadj):
    neg = dimension.where(dimension < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_hl_21d_base_v127_signal(dimension, closeadj):
    result = dimension.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_hl_63d_base_v128_signal(dimension, closeadj):
    result = dimension.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_hl_252d_base_v129_signal(dimension, closeadj):
    result = dimension.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of dimension
def tvac_f078_ttm_vs_annual_consistency_z_63d_base_v130_signal(dimension):
    result = _z(dimension, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of dimension
def tvac_f078_ttm_vs_annual_consistency_z_126d_base_v131_signal(dimension):
    result = _z(dimension, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of dimension
def tvac_f078_ttm_vs_annual_consistency_z_1008d_base_v132_signal(dimension):
    result = _z(dimension, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_st_lt_252_21d_base_v133_signal(dimension, closeadj):
    sm = _mean(dimension, 21)
    lm = _mean(dimension, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_st_lt_252_63d_base_v134_signal(dimension, closeadj):
    sm = _mean(dimension, 63)
    lm = _mean(dimension, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_st_lt_504_21d_base_v135_signal(dimension, closeadj):
    sm = _mean(dimension, 21)
    lm = _mean(dimension, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_st_lt_504_63d_base_v136_signal(dimension, closeadj):
    sm = _mean(dimension, 63)
    lm = _mean(dimension, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged dimension/revenue times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_per_revenue_21d_base_v137_signal(dimension, revenue, closeadj):
    r = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged dimension/revenue times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_per_revenue_63d_base_v138_signal(dimension, revenue, closeadj):
    r = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged dimension/revenue times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_per_revenue_252d_base_v139_signal(dimension, revenue, closeadj):
    r = _ttm_vs_annual_consistency_scaled(dimension, revenue)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged dimension/ncfo times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_per_ncfo_21d_base_v140_signal(dimension, ncfo, closeadj):
    r = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged dimension/ncfo times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_per_ncfo_63d_base_v141_signal(dimension, ncfo, closeadj):
    r = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged dimension/ncfo times closeadj
def tvac_f078_ttm_vs_annual_consistency_lag_per_ncfo_252d_base_v142_signal(dimension, ncfo, closeadj):
    r = _ttm_vs_annual_consistency_scaled(dimension, ncfo)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |dimension| times closeadj
def tvac_f078_ttm_vs_annual_consistency_abssum_63d_base_v143_signal(dimension, closeadj):
    result = dimension.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |dimension| times closeadj
def tvac_f078_ttm_vs_annual_consistency_abssum_252d_base_v144_signal(dimension, closeadj):
    result = dimension.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |dimension| times closeadj
def tvac_f078_ttm_vs_annual_consistency_abssum_504d_base_v145_signal(dimension, closeadj):
    result = dimension.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of dimension
def tvac_f078_ttm_vs_annual_consistency_acf1_252d_base_v146_signal(dimension):
    result = dimension.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of dimension
def tvac_f078_ttm_vs_annual_consistency_acf1_504d_base_v147_signal(dimension):
    result = dimension.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of dimension
def tvac_f078_ttm_vs_annual_consistency_posinrange_252d_base_v148_signal(dimension):
    m = _mean(dimension, 252)
    hi = dimension.rolling(252, min_periods=max(1, 252//2)).max()
    lo = dimension.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of dimension
def tvac_f078_ttm_vs_annual_consistency_posinrange_504d_base_v149_signal(dimension):
    m = _mean(dimension, 504)
    hi = dimension.rolling(504, min_periods=max(1, 504//2)).max()
    lo = dimension.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of dimension times closeadj
def tvac_f078_ttm_vs_annual_consistency_hl_5d_base_v150_signal(dimension, closeadj):
    result = dimension.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
