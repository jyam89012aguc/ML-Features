"""Family f092 - Insider transaction net flow (Insiders and Ownership) | Sharadar tables: SF2 | fields: transactioncode, transactionshares, transactionvalue, transactionpricepershare | base 076-150"""
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
def _insider_transaction_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_transaction_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_transaction_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of transactioncode/transactionvalue
def itf_f092_insider_transaction_flow_log_per_transactionvalue_504d_base_v076_signal(transactioncode, transactionvalue):
    s = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of transactioncode/transactionpricepershare
def itf_f092_insider_transaction_flow_log_per_transactionprice_252d_base_v077_signal(transactioncode, transactionpricepershare):
    s = _insider_transaction_flow_scaled(transactioncode, transactionpricepershare)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of transactioncode/transactionpricepershare
def itf_f092_insider_transaction_flow_log_per_transactionprice_504d_base_v078_signal(transactioncode, transactionpricepershare):
    s = _insider_transaction_flow_scaled(transactioncode, transactionpricepershare)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of transactioncode times closeadj
def itf_f092_insider_transaction_flow_ewm_21d_base_v079_signal(transactioncode, closeadj):
    result = transactioncode.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of transactioncode times closeadj
def itf_f092_insider_transaction_flow_ewm_63d_base_v080_signal(transactioncode, closeadj):
    result = transactioncode.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of transactioncode times closeadj
def itf_f092_insider_transaction_flow_ewm_252d_base_v081_signal(transactioncode, closeadj):
    result = transactioncode.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of transactioncode times closeadj
def itf_f092_insider_transaction_flow_med_63d_base_v082_signal(transactioncode, closeadj):
    result = transactioncode.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of transactioncode times closeadj
def itf_f092_insider_transaction_flow_med_252d_base_v083_signal(transactioncode, closeadj):
    result = transactioncode.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of transactioncode times closeadj
def itf_f092_insider_transaction_flow_med_504d_base_v084_signal(transactioncode, closeadj):
    result = transactioncode.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of transactioncode
def itf_f092_insider_transaction_flow_skew_252d_base_v085_signal(transactioncode):
    result = transactioncode.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of transactioncode
def itf_f092_insider_transaction_flow_skew_504d_base_v086_signal(transactioncode):
    result = transactioncode.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of transactioncode
def itf_f092_insider_transaction_flow_kurt_252d_base_v087_signal(transactioncode):
    result = transactioncode.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of transactioncode
def itf_f092_insider_transaction_flow_kurt_504d_base_v088_signal(transactioncode):
    result = transactioncode.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of transactioncode times closeadj
def itf_f092_insider_transaction_flow_rank_252d_base_v089_signal(transactioncode, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = transactioncode.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of transactioncode times closeadj
def itf_f092_insider_transaction_flow_rank_504d_base_v090_signal(transactioncode, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = transactioncode.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of transactioncode times closeadj
def itf_f092_insider_transaction_flow_rank_1008d_base_v091_signal(transactioncode, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = transactioncode.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of transactioncode from 63d mean times closeadj
def itf_f092_insider_transaction_flow_devmean_63d_base_v092_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 63)
    result = (transactioncode - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of transactioncode from 252d mean times closeadj
def itf_f092_insider_transaction_flow_devmean_252d_base_v093_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 252)
    result = (transactioncode - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of transactioncode from 504d mean times closeadj
def itf_f092_insider_transaction_flow_devmean_504d_base_v094_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 504)
    result = (transactioncode - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of transactioncode times closeadj
def itf_f092_insider_transaction_flow_logdiff_21d_base_v095_signal(transactioncode, closeadj):
    lr = _insider_transaction_flow_log(transactioncode)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of transactioncode times closeadj
def itf_f092_insider_transaction_flow_logdiff_63d_base_v096_signal(transactioncode, closeadj):
    lr = _insider_transaction_flow_log(transactioncode)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of transactioncode times closeadj
def itf_f092_insider_transaction_flow_logdiff_252d_base_v097_signal(transactioncode, closeadj):
    lr = _insider_transaction_flow_log(transactioncode)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of transactioncode times closeadj
def itf_f092_insider_transaction_flow_range_63d_base_v098_signal(transactioncode, closeadj):
    hi = transactioncode.rolling(63, min_periods=max(1, 63//2)).max()
    lo = transactioncode.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of transactioncode times closeadj
def itf_f092_insider_transaction_flow_range_252d_base_v099_signal(transactioncode, closeadj):
    hi = transactioncode.rolling(252, min_periods=max(1, 252//2)).max()
    lo = transactioncode.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of transactioncode times closeadj
def itf_f092_insider_transaction_flow_range_504d_base_v100_signal(transactioncode, closeadj):
    hi = transactioncode.rolling(504, min_periods=max(1, 504//2)).max()
    lo = transactioncode.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 252d mean times closeadj
def itf_f092_insider_transaction_flow_rel_252d_base_v101_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 252).replace(0, np.nan)
    result = (transactioncode / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 504d mean times closeadj
def itf_f092_insider_transaction_flow_rel_504d_base_v102_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 504).replace(0, np.nan)
    result = (transactioncode / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 1008d mean times closeadj
def itf_f092_insider_transaction_flow_rel_1008d_base_v103_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 1008).replace(0, np.nan)
    result = (transactioncode / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactioncode/transactionshares 63d mean
def itf_f092_insider_transaction_flow_sqnorm_transactionshares_63d_base_v104_signal(transactioncode, transactionshares):
    r = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactioncode/transactionshares 252d mean
def itf_f092_insider_transaction_flow_sqnorm_transactionshares_252d_base_v105_signal(transactioncode, transactionshares):
    r = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactioncode/transactionvalue 63d mean
def itf_f092_insider_transaction_flow_sqnorm_transactionvalue_63d_base_v106_signal(transactioncode, transactionvalue):
    r = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactioncode/transactionvalue 252d mean
def itf_f092_insider_transaction_flow_sqnorm_transactionvalue_252d_base_v107_signal(transactioncode, transactionvalue):
    r = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactioncode/transactionpricepershare 63d mean
def itf_f092_insider_transaction_flow_sqnorm_transactionprice_63d_base_v108_signal(transactioncode, transactionpricepershare):
    r = _insider_transaction_flow_scaled(transactioncode, transactionpricepershare)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactioncode/transactionpricepershare 252d mean
def itf_f092_insider_transaction_flow_sqnorm_transactionprice_252d_base_v109_signal(transactioncode, transactionpricepershare):
    r = _insider_transaction_flow_scaled(transactioncode, transactionpricepershare)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of transactioncode times closeadj
def itf_f092_insider_transaction_flow_infrat_63d_base_v110_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 63)
    s = _std(transactioncode, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of transactioncode times closeadj
def itf_f092_insider_transaction_flow_infrat_252d_base_v111_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 252)
    s = _std(transactioncode, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of transactioncode times closeadj
def itf_f092_insider_transaction_flow_infrat_504d_base_v112_signal(transactioncode, closeadj):
    m = _mean(transactioncode, 504)
    s = _std(transactioncode, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of transactioncode
def itf_f092_insider_transaction_flow_cv_252d_base_v113_signal(transactioncode):
    m = _mean(transactioncode, 252).abs().replace(0, np.nan)
    s = _std(transactioncode, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of transactioncode
def itf_f092_insider_transaction_flow_cv_504d_base_v114_signal(transactioncode):
    m = _mean(transactioncode, 504).abs().replace(0, np.nan)
    s = _std(transactioncode, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged transactioncode times closeadj
def itf_f092_insider_transaction_flow_lag_5d_base_v115_signal(transactioncode, closeadj):
    result = transactioncode.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged transactioncode times closeadj
def itf_f092_insider_transaction_flow_lag_21d_base_v116_signal(transactioncode, closeadj):
    result = transactioncode.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged transactioncode times closeadj
def itf_f092_insider_transaction_flow_lag_63d_base_v117_signal(transactioncode, closeadj):
    result = transactioncode.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged transactioncode times closeadj
def itf_f092_insider_transaction_flow_lag_252d_base_v118_signal(transactioncode, closeadj):
    result = transactioncode.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(transactioncode) / mean(transactionshares) x closeadj
def itf_f092_insider_transaction_flow_cumper_transactionshares_252d_base_v119_signal(transactioncode, transactionshares, closeadj):
    s = transactioncode.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(transactionshares, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(transactioncode) / mean(transactionshares) x closeadj
def itf_f092_insider_transaction_flow_cumper_transactionshares_504d_base_v120_signal(transactioncode, transactionshares, closeadj):
    s = transactioncode.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(transactionshares, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(transactioncode) / mean(transactionvalue) x closeadj
def itf_f092_insider_transaction_flow_cumper_transactionvalue_252d_base_v121_signal(transactioncode, transactionvalue, closeadj):
    s = transactioncode.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(transactionvalue, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(transactioncode) / mean(transactionvalue) x closeadj
def itf_f092_insider_transaction_flow_cumper_transactionvalue_504d_base_v122_signal(transactioncode, transactionvalue, closeadj):
    s = transactioncode.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(transactionvalue, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only transactioncode times closeadj
def itf_f092_insider_transaction_flow_pos_63d_base_v123_signal(transactioncode, closeadj):
    pos = transactioncode.where(transactioncode > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only transactioncode times closeadj
def itf_f092_insider_transaction_flow_pos_252d_base_v124_signal(transactioncode, closeadj):
    pos = transactioncode.where(transactioncode > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only transactioncode times closeadj
def itf_f092_insider_transaction_flow_neg_63d_base_v125_signal(transactioncode, closeadj):
    neg = transactioncode.where(transactioncode < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only transactioncode times closeadj
def itf_f092_insider_transaction_flow_neg_252d_base_v126_signal(transactioncode, closeadj):
    neg = transactioncode.where(transactioncode < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of transactioncode times closeadj
def itf_f092_insider_transaction_flow_hl_21d_base_v127_signal(transactioncode, closeadj):
    result = transactioncode.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of transactioncode times closeadj
def itf_f092_insider_transaction_flow_hl_63d_base_v128_signal(transactioncode, closeadj):
    result = transactioncode.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of transactioncode times closeadj
def itf_f092_insider_transaction_flow_hl_252d_base_v129_signal(transactioncode, closeadj):
    result = transactioncode.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of transactioncode
def itf_f092_insider_transaction_flow_z_63d_base_v130_signal(transactioncode):
    result = _z(transactioncode, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of transactioncode
def itf_f092_insider_transaction_flow_z_126d_base_v131_signal(transactioncode):
    result = _z(transactioncode, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of transactioncode
def itf_f092_insider_transaction_flow_z_1008d_base_v132_signal(transactioncode):
    result = _z(transactioncode, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of transactioncode times closeadj
def itf_f092_insider_transaction_flow_st_lt_252_21d_base_v133_signal(transactioncode, closeadj):
    sm = _mean(transactioncode, 21)
    lm = _mean(transactioncode, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of transactioncode times closeadj
def itf_f092_insider_transaction_flow_st_lt_252_63d_base_v134_signal(transactioncode, closeadj):
    sm = _mean(transactioncode, 63)
    lm = _mean(transactioncode, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of transactioncode times closeadj
def itf_f092_insider_transaction_flow_st_lt_504_21d_base_v135_signal(transactioncode, closeadj):
    sm = _mean(transactioncode, 21)
    lm = _mean(transactioncode, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of transactioncode times closeadj
def itf_f092_insider_transaction_flow_st_lt_504_63d_base_v136_signal(transactioncode, closeadj):
    sm = _mean(transactioncode, 63)
    lm = _mean(transactioncode, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged transactioncode/transactionshares times closeadj
def itf_f092_insider_transaction_flow_lag_per_transactionshares_21d_base_v137_signal(transactioncode, transactionshares, closeadj):
    r = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged transactioncode/transactionshares times closeadj
def itf_f092_insider_transaction_flow_lag_per_transactionshares_63d_base_v138_signal(transactioncode, transactionshares, closeadj):
    r = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged transactioncode/transactionshares times closeadj
def itf_f092_insider_transaction_flow_lag_per_transactionshares_252d_base_v139_signal(transactioncode, transactionshares, closeadj):
    r = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged transactioncode/transactionvalue times closeadj
def itf_f092_insider_transaction_flow_lag_per_transactionvalue_21d_base_v140_signal(transactioncode, transactionvalue, closeadj):
    r = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged transactioncode/transactionvalue times closeadj
def itf_f092_insider_transaction_flow_lag_per_transactionvalue_63d_base_v141_signal(transactioncode, transactionvalue, closeadj):
    r = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged transactioncode/transactionvalue times closeadj
def itf_f092_insider_transaction_flow_lag_per_transactionvalue_252d_base_v142_signal(transactioncode, transactionvalue, closeadj):
    r = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |transactioncode| times closeadj
def itf_f092_insider_transaction_flow_abssum_63d_base_v143_signal(transactioncode, closeadj):
    result = transactioncode.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |transactioncode| times closeadj
def itf_f092_insider_transaction_flow_abssum_252d_base_v144_signal(transactioncode, closeadj):
    result = transactioncode.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |transactioncode| times closeadj
def itf_f092_insider_transaction_flow_abssum_504d_base_v145_signal(transactioncode, closeadj):
    result = transactioncode.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of transactioncode
def itf_f092_insider_transaction_flow_acf1_252d_base_v146_signal(transactioncode):
    result = transactioncode.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of transactioncode
def itf_f092_insider_transaction_flow_acf1_504d_base_v147_signal(transactioncode):
    result = transactioncode.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of transactioncode
def itf_f092_insider_transaction_flow_posinrange_252d_base_v148_signal(transactioncode):
    m = _mean(transactioncode, 252)
    hi = transactioncode.rolling(252, min_periods=max(1, 252//2)).max()
    lo = transactioncode.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of transactioncode
def itf_f092_insider_transaction_flow_posinrange_504d_base_v149_signal(transactioncode):
    m = _mean(transactioncode, 504)
    hi = transactioncode.rolling(504, min_periods=max(1, 504//2)).max()
    lo = transactioncode.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of transactioncode times closeadj
def itf_f092_insider_transaction_flow_hl_5d_base_v150_signal(transactioncode, closeadj):
    result = transactioncode.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
