"""Family f074 - Dividend and payout valuation (Valuation Multiples) | Sharadar tables: SF1 | fields: dps, ncfdiv, payoutratio, value | base 076-150"""
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
def _dividend_and_payout_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _dividend_and_payout_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _dividend_and_payout_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of dps/payoutratio
def dpv_f074_dividend_and_payout_valuation_log_per_payoutratio_504d_base_v076_signal(dps, payoutratio):
    s = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of dps/value
def dpv_f074_dividend_and_payout_valuation_log_per_value_252d_base_v077_signal(dps, value):
    s = _dividend_and_payout_valuation_scaled(dps, value)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of dps/value
def dpv_f074_dividend_and_payout_valuation_log_per_value_504d_base_v078_signal(dps, value):
    s = _dividend_and_payout_valuation_scaled(dps, value)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_ewm_21d_base_v079_signal(dps, closeadj):
    result = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_ewm_63d_base_v080_signal(dps, closeadj):
    result = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_ewm_252d_base_v081_signal(dps, closeadj):
    result = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_med_63d_base_v082_signal(dps, closeadj):
    result = dps.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_med_252d_base_v083_signal(dps, closeadj):
    result = dps.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_med_504d_base_v084_signal(dps, closeadj):
    result = dps.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of dps
def dpv_f074_dividend_and_payout_valuation_skew_252d_base_v085_signal(dps):
    result = dps.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of dps
def dpv_f074_dividend_and_payout_valuation_skew_504d_base_v086_signal(dps):
    result = dps.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of dps
def dpv_f074_dividend_and_payout_valuation_kurt_252d_base_v087_signal(dps):
    result = dps.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of dps
def dpv_f074_dividend_and_payout_valuation_kurt_504d_base_v088_signal(dps):
    result = dps.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_rank_252d_base_v089_signal(dps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = dps.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_rank_504d_base_v090_signal(dps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = dps.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_rank_1008d_base_v091_signal(dps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = dps.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of dps from 63d mean times closeadj
def dpv_f074_dividend_and_payout_valuation_devmean_63d_base_v092_signal(dps, closeadj):
    m = _mean(dps, 63)
    result = (dps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of dps from 252d mean times closeadj
def dpv_f074_dividend_and_payout_valuation_devmean_252d_base_v093_signal(dps, closeadj):
    m = _mean(dps, 252)
    result = (dps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of dps from 504d mean times closeadj
def dpv_f074_dividend_and_payout_valuation_devmean_504d_base_v094_signal(dps, closeadj):
    m = _mean(dps, 504)
    result = (dps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_logdiff_21d_base_v095_signal(dps, closeadj):
    lr = _dividend_and_payout_valuation_log(dps)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_logdiff_63d_base_v096_signal(dps, closeadj):
    lr = _dividend_and_payout_valuation_log(dps)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_logdiff_252d_base_v097_signal(dps, closeadj):
    lr = _dividend_and_payout_valuation_log(dps)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_range_63d_base_v098_signal(dps, closeadj):
    hi = dps.rolling(63, min_periods=max(1, 63//2)).max()
    lo = dps.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_range_252d_base_v099_signal(dps, closeadj):
    hi = dps.rolling(252, min_periods=max(1, 252//2)).max()
    lo = dps.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_range_504d_base_v100_signal(dps, closeadj):
    hi = dps.rolling(504, min_periods=max(1, 504//2)).max()
    lo = dps.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 252d mean times closeadj
def dpv_f074_dividend_and_payout_valuation_rel_252d_base_v101_signal(dps, closeadj):
    m = _mean(dps, 252).replace(0, np.nan)
    result = (dps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 504d mean times closeadj
def dpv_f074_dividend_and_payout_valuation_rel_504d_base_v102_signal(dps, closeadj):
    m = _mean(dps, 504).replace(0, np.nan)
    result = (dps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 1008d mean times closeadj
def dpv_f074_dividend_and_payout_valuation_rel_1008d_base_v103_signal(dps, closeadj):
    m = _mean(dps, 1008).replace(0, np.nan)
    result = (dps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dps/ncfdiv 63d mean
def dpv_f074_dividend_and_payout_valuation_sqnorm_ncfdiv_63d_base_v104_signal(dps, ncfdiv):
    r = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dps/ncfdiv 252d mean
def dpv_f074_dividend_and_payout_valuation_sqnorm_ncfdiv_252d_base_v105_signal(dps, ncfdiv):
    r = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dps/payoutratio 63d mean
def dpv_f074_dividend_and_payout_valuation_sqnorm_payoutratio_63d_base_v106_signal(dps, payoutratio):
    r = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dps/payoutratio 252d mean
def dpv_f074_dividend_and_payout_valuation_sqnorm_payoutratio_252d_base_v107_signal(dps, payoutratio):
    r = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dps/value 63d mean
def dpv_f074_dividend_and_payout_valuation_sqnorm_value_63d_base_v108_signal(dps, value):
    r = _dividend_and_payout_valuation_scaled(dps, value)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized dps/value 252d mean
def dpv_f074_dividend_and_payout_valuation_sqnorm_value_252d_base_v109_signal(dps, value):
    r = _dividend_and_payout_valuation_scaled(dps, value)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_infrat_63d_base_v110_signal(dps, closeadj):
    m = _mean(dps, 63)
    s = _std(dps, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_infrat_252d_base_v111_signal(dps, closeadj):
    m = _mean(dps, 252)
    s = _std(dps, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_infrat_504d_base_v112_signal(dps, closeadj):
    m = _mean(dps, 504)
    s = _std(dps, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of dps
def dpv_f074_dividend_and_payout_valuation_cv_252d_base_v113_signal(dps):
    m = _mean(dps, 252).abs().replace(0, np.nan)
    s = _std(dps, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of dps
def dpv_f074_dividend_and_payout_valuation_cv_504d_base_v114_signal(dps):
    m = _mean(dps, 504).abs().replace(0, np.nan)
    s = _std(dps, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged dps times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_5d_base_v115_signal(dps, closeadj):
    result = dps.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged dps times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_21d_base_v116_signal(dps, closeadj):
    result = dps.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged dps times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_63d_base_v117_signal(dps, closeadj):
    result = dps.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged dps times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_252d_base_v118_signal(dps, closeadj):
    result = dps.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(dps) / mean(ncfdiv) x closeadj
def dpv_f074_dividend_and_payout_valuation_cumper_ncfdiv_252d_base_v119_signal(dps, ncfdiv, closeadj):
    s = dps.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ncfdiv, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(dps) / mean(ncfdiv) x closeadj
def dpv_f074_dividend_and_payout_valuation_cumper_ncfdiv_504d_base_v120_signal(dps, ncfdiv, closeadj):
    s = dps.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ncfdiv, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(dps) / mean(payoutratio) x closeadj
def dpv_f074_dividend_and_payout_valuation_cumper_payoutratio_252d_base_v121_signal(dps, payoutratio, closeadj):
    s = dps.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(payoutratio, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(dps) / mean(payoutratio) x closeadj
def dpv_f074_dividend_and_payout_valuation_cumper_payoutratio_504d_base_v122_signal(dps, payoutratio, closeadj):
    s = dps.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(payoutratio, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only dps times closeadj
def dpv_f074_dividend_and_payout_valuation_pos_63d_base_v123_signal(dps, closeadj):
    pos = dps.where(dps > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only dps times closeadj
def dpv_f074_dividend_and_payout_valuation_pos_252d_base_v124_signal(dps, closeadj):
    pos = dps.where(dps > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only dps times closeadj
def dpv_f074_dividend_and_payout_valuation_neg_63d_base_v125_signal(dps, closeadj):
    neg = dps.where(dps < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only dps times closeadj
def dpv_f074_dividend_and_payout_valuation_neg_252d_base_v126_signal(dps, closeadj):
    neg = dps.where(dps < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_hl_21d_base_v127_signal(dps, closeadj):
    result = dps.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_hl_63d_base_v128_signal(dps, closeadj):
    result = dps.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_hl_252d_base_v129_signal(dps, closeadj):
    result = dps.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of dps
def dpv_f074_dividend_and_payout_valuation_z_63d_base_v130_signal(dps):
    result = _z(dps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of dps
def dpv_f074_dividend_and_payout_valuation_z_126d_base_v131_signal(dps):
    result = _z(dps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of dps
def dpv_f074_dividend_and_payout_valuation_z_1008d_base_v132_signal(dps):
    result = _z(dps, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_st_lt_252_21d_base_v133_signal(dps, closeadj):
    sm = _mean(dps, 21)
    lm = _mean(dps, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_st_lt_252_63d_base_v134_signal(dps, closeadj):
    sm = _mean(dps, 63)
    lm = _mean(dps, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_st_lt_504_21d_base_v135_signal(dps, closeadj):
    sm = _mean(dps, 21)
    lm = _mean(dps, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_st_lt_504_63d_base_v136_signal(dps, closeadj):
    sm = _mean(dps, 63)
    lm = _mean(dps, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged dps/ncfdiv times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_per_ncfdiv_21d_base_v137_signal(dps, ncfdiv, closeadj):
    r = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged dps/ncfdiv times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_per_ncfdiv_63d_base_v138_signal(dps, ncfdiv, closeadj):
    r = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged dps/ncfdiv times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_per_ncfdiv_252d_base_v139_signal(dps, ncfdiv, closeadj):
    r = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged dps/payoutratio times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_per_payoutratio_21d_base_v140_signal(dps, payoutratio, closeadj):
    r = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged dps/payoutratio times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_per_payoutratio_63d_base_v141_signal(dps, payoutratio, closeadj):
    r = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged dps/payoutratio times closeadj
def dpv_f074_dividend_and_payout_valuation_lag_per_payoutratio_252d_base_v142_signal(dps, payoutratio, closeadj):
    r = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |dps| times closeadj
def dpv_f074_dividend_and_payout_valuation_abssum_63d_base_v143_signal(dps, closeadj):
    result = dps.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |dps| times closeadj
def dpv_f074_dividend_and_payout_valuation_abssum_252d_base_v144_signal(dps, closeadj):
    result = dps.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |dps| times closeadj
def dpv_f074_dividend_and_payout_valuation_abssum_504d_base_v145_signal(dps, closeadj):
    result = dps.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of dps
def dpv_f074_dividend_and_payout_valuation_acf1_252d_base_v146_signal(dps):
    result = dps.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of dps
def dpv_f074_dividend_and_payout_valuation_acf1_504d_base_v147_signal(dps):
    result = dps.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of dps
def dpv_f074_dividend_and_payout_valuation_posinrange_252d_base_v148_signal(dps):
    m = _mean(dps, 252)
    hi = dps.rolling(252, min_periods=max(1, 252//2)).max()
    lo = dps.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of dps
def dpv_f074_dividend_and_payout_valuation_posinrange_504d_base_v149_signal(dps):
    m = _mean(dps, 504)
    hi = dps.rolling(504, min_periods=max(1, 504//2)).max()
    lo = dps.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_hl_5d_base_v150_signal(dps, closeadj):
    result = dps.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
