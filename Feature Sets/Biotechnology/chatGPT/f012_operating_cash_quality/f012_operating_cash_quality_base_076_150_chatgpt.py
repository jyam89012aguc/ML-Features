"""Family f012 - Operating cash quality versus income (Cash Flow and Burn) | Sharadar tables: SF1 | fields: ncfo, netinc, depamor, sbcomp | base 076-150"""
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
def _operating_cash_quality_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _operating_cash_quality_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _operating_cash_quality_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ncfo/depamor
def ocq_f012_operating_cash_quality_log_per_depamor_504d_base_v076_signal(ncfo, depamor):
    s = _operating_cash_quality_scaled(ncfo, depamor)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfo/sbcomp
def ocq_f012_operating_cash_quality_log_per_sbcomp_252d_base_v077_signal(ncfo, sbcomp):
    s = _operating_cash_quality_scaled(ncfo, sbcomp)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncfo/sbcomp
def ocq_f012_operating_cash_quality_log_per_sbcomp_504d_base_v078_signal(ncfo, sbcomp):
    s = _operating_cash_quality_scaled(ncfo, sbcomp)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ncfo times closeadj
def ocq_f012_operating_cash_quality_ewm_21d_base_v079_signal(ncfo, closeadj):
    result = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ncfo times closeadj
def ocq_f012_operating_cash_quality_ewm_63d_base_v080_signal(ncfo, closeadj):
    result = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ncfo times closeadj
def ocq_f012_operating_cash_quality_ewm_252d_base_v081_signal(ncfo, closeadj):
    result = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ncfo times closeadj
def ocq_f012_operating_cash_quality_med_63d_base_v082_signal(ncfo, closeadj):
    result = ncfo.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ncfo times closeadj
def ocq_f012_operating_cash_quality_med_252d_base_v083_signal(ncfo, closeadj):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ncfo times closeadj
def ocq_f012_operating_cash_quality_med_504d_base_v084_signal(ncfo, closeadj):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ncfo
def ocq_f012_operating_cash_quality_skew_252d_base_v085_signal(ncfo):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ncfo
def ocq_f012_operating_cash_quality_skew_504d_base_v086_signal(ncfo):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ncfo
def ocq_f012_operating_cash_quality_kurt_252d_base_v087_signal(ncfo):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ncfo
def ocq_f012_operating_cash_quality_kurt_504d_base_v088_signal(ncfo):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ncfo times closeadj
def ocq_f012_operating_cash_quality_rank_252d_base_v089_signal(ncfo, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ncfo times closeadj
def ocq_f012_operating_cash_quality_rank_504d_base_v090_signal(ncfo, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ncfo times closeadj
def ocq_f012_operating_cash_quality_rank_1008d_base_v091_signal(ncfo, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfo.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfo from 63d mean times closeadj
def ocq_f012_operating_cash_quality_devmean_63d_base_v092_signal(ncfo, closeadj):
    m = _mean(ncfo, 63)
    result = (ncfo - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfo from 252d mean times closeadj
def ocq_f012_operating_cash_quality_devmean_252d_base_v093_signal(ncfo, closeadj):
    m = _mean(ncfo, 252)
    result = (ncfo - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfo from 504d mean times closeadj
def ocq_f012_operating_cash_quality_devmean_504d_base_v094_signal(ncfo, closeadj):
    m = _mean(ncfo, 504)
    result = (ncfo - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ncfo times closeadj
def ocq_f012_operating_cash_quality_logdiff_21d_base_v095_signal(ncfo, closeadj):
    lr = _operating_cash_quality_log(ncfo)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ncfo times closeadj
def ocq_f012_operating_cash_quality_logdiff_63d_base_v096_signal(ncfo, closeadj):
    lr = _operating_cash_quality_log(ncfo)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ncfo times closeadj
def ocq_f012_operating_cash_quality_logdiff_252d_base_v097_signal(ncfo, closeadj):
    lr = _operating_cash_quality_log(ncfo)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ncfo times closeadj
def ocq_f012_operating_cash_quality_range_63d_base_v098_signal(ncfo, closeadj):
    hi = ncfo.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ncfo.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ncfo times closeadj
def ocq_f012_operating_cash_quality_range_252d_base_v099_signal(ncfo, closeadj):
    hi = ncfo.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncfo.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ncfo times closeadj
def ocq_f012_operating_cash_quality_range_504d_base_v100_signal(ncfo, closeadj):
    hi = ncfo.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncfo.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 252d mean times closeadj
def ocq_f012_operating_cash_quality_rel_252d_base_v101_signal(ncfo, closeadj):
    m = _mean(ncfo, 252).replace(0, np.nan)
    result = (ncfo / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 504d mean times closeadj
def ocq_f012_operating_cash_quality_rel_504d_base_v102_signal(ncfo, closeadj):
    m = _mean(ncfo, 504).replace(0, np.nan)
    result = (ncfo / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 1008d mean times closeadj
def ocq_f012_operating_cash_quality_rel_1008d_base_v103_signal(ncfo, closeadj):
    m = _mean(ncfo, 1008).replace(0, np.nan)
    result = (ncfo / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/netinc 63d mean
def ocq_f012_operating_cash_quality_sqnorm_netinc_63d_base_v104_signal(ncfo, netinc):
    r = _operating_cash_quality_scaled(ncfo, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/netinc 252d mean
def ocq_f012_operating_cash_quality_sqnorm_netinc_252d_base_v105_signal(ncfo, netinc):
    r = _operating_cash_quality_scaled(ncfo, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/depamor 63d mean
def ocq_f012_operating_cash_quality_sqnorm_depamor_63d_base_v106_signal(ncfo, depamor):
    r = _operating_cash_quality_scaled(ncfo, depamor)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/depamor 252d mean
def ocq_f012_operating_cash_quality_sqnorm_depamor_252d_base_v107_signal(ncfo, depamor):
    r = _operating_cash_quality_scaled(ncfo, depamor)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/sbcomp 63d mean
def ocq_f012_operating_cash_quality_sqnorm_sbcomp_63d_base_v108_signal(ncfo, sbcomp):
    r = _operating_cash_quality_scaled(ncfo, sbcomp)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/sbcomp 252d mean
def ocq_f012_operating_cash_quality_sqnorm_sbcomp_252d_base_v109_signal(ncfo, sbcomp):
    r = _operating_cash_quality_scaled(ncfo, sbcomp)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ncfo times closeadj
def ocq_f012_operating_cash_quality_infrat_63d_base_v110_signal(ncfo, closeadj):
    m = _mean(ncfo, 63)
    s = _std(ncfo, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ncfo times closeadj
def ocq_f012_operating_cash_quality_infrat_252d_base_v111_signal(ncfo, closeadj):
    m = _mean(ncfo, 252)
    s = _std(ncfo, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ncfo times closeadj
def ocq_f012_operating_cash_quality_infrat_504d_base_v112_signal(ncfo, closeadj):
    m = _mean(ncfo, 504)
    s = _std(ncfo, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ncfo
def ocq_f012_operating_cash_quality_cv_252d_base_v113_signal(ncfo):
    m = _mean(ncfo, 252).abs().replace(0, np.nan)
    s = _std(ncfo, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ncfo
def ocq_f012_operating_cash_quality_cv_504d_base_v114_signal(ncfo):
    m = _mean(ncfo, 504).abs().replace(0, np.nan)
    s = _std(ncfo, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ncfo times closeadj
def ocq_f012_operating_cash_quality_lag_5d_base_v115_signal(ncfo, closeadj):
    result = ncfo.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfo times closeadj
def ocq_f012_operating_cash_quality_lag_21d_base_v116_signal(ncfo, closeadj):
    result = ncfo.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfo times closeadj
def ocq_f012_operating_cash_quality_lag_63d_base_v117_signal(ncfo, closeadj):
    result = ncfo.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfo times closeadj
def ocq_f012_operating_cash_quality_lag_252d_base_v118_signal(ncfo, closeadj):
    result = ncfo.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncfo) / mean(netinc) x closeadj
def ocq_f012_operating_cash_quality_cumper_netinc_252d_base_v119_signal(ncfo, netinc, closeadj):
    s = ncfo.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncfo) / mean(netinc) x closeadj
def ocq_f012_operating_cash_quality_cumper_netinc_504d_base_v120_signal(ncfo, netinc, closeadj):
    s = ncfo.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncfo) / mean(depamor) x closeadj
def ocq_f012_operating_cash_quality_cumper_depamor_252d_base_v121_signal(ncfo, depamor, closeadj):
    s = ncfo.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(depamor, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncfo) / mean(depamor) x closeadj
def ocq_f012_operating_cash_quality_cumper_depamor_504d_base_v122_signal(ncfo, depamor, closeadj):
    s = ncfo.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(depamor, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ncfo times closeadj
def ocq_f012_operating_cash_quality_pos_63d_base_v123_signal(ncfo, closeadj):
    pos = ncfo.where(ncfo > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ncfo times closeadj
def ocq_f012_operating_cash_quality_pos_252d_base_v124_signal(ncfo, closeadj):
    pos = ncfo.where(ncfo > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ncfo times closeadj
def ocq_f012_operating_cash_quality_neg_63d_base_v125_signal(ncfo, closeadj):
    neg = ncfo.where(ncfo < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ncfo times closeadj
def ocq_f012_operating_cash_quality_neg_252d_base_v126_signal(ncfo, closeadj):
    neg = ncfo.where(ncfo < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ncfo times closeadj
def ocq_f012_operating_cash_quality_hl_21d_base_v127_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ncfo times closeadj
def ocq_f012_operating_cash_quality_hl_63d_base_v128_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ncfo times closeadj
def ocq_f012_operating_cash_quality_hl_252d_base_v129_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ncfo
def ocq_f012_operating_cash_quality_z_63d_base_v130_signal(ncfo):
    result = _z(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ncfo
def ocq_f012_operating_cash_quality_z_126d_base_v131_signal(ncfo):
    result = _z(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ncfo
def ocq_f012_operating_cash_quality_z_1008d_base_v132_signal(ncfo):
    result = _z(ncfo, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ncfo times closeadj
def ocq_f012_operating_cash_quality_st_lt_252_21d_base_v133_signal(ncfo, closeadj):
    sm = _mean(ncfo, 21)
    lm = _mean(ncfo, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ncfo times closeadj
def ocq_f012_operating_cash_quality_st_lt_252_63d_base_v134_signal(ncfo, closeadj):
    sm = _mean(ncfo, 63)
    lm = _mean(ncfo, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ncfo times closeadj
def ocq_f012_operating_cash_quality_st_lt_504_21d_base_v135_signal(ncfo, closeadj):
    sm = _mean(ncfo, 21)
    lm = _mean(ncfo, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ncfo times closeadj
def ocq_f012_operating_cash_quality_st_lt_504_63d_base_v136_signal(ncfo, closeadj):
    sm = _mean(ncfo, 63)
    lm = _mean(ncfo, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfo/netinc times closeadj
def ocq_f012_operating_cash_quality_lag_per_netinc_21d_base_v137_signal(ncfo, netinc, closeadj):
    r = _operating_cash_quality_scaled(ncfo, netinc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfo/netinc times closeadj
def ocq_f012_operating_cash_quality_lag_per_netinc_63d_base_v138_signal(ncfo, netinc, closeadj):
    r = _operating_cash_quality_scaled(ncfo, netinc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfo/netinc times closeadj
def ocq_f012_operating_cash_quality_lag_per_netinc_252d_base_v139_signal(ncfo, netinc, closeadj):
    r = _operating_cash_quality_scaled(ncfo, netinc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfo/depamor times closeadj
def ocq_f012_operating_cash_quality_lag_per_depamor_21d_base_v140_signal(ncfo, depamor, closeadj):
    r = _operating_cash_quality_scaled(ncfo, depamor)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfo/depamor times closeadj
def ocq_f012_operating_cash_quality_lag_per_depamor_63d_base_v141_signal(ncfo, depamor, closeadj):
    r = _operating_cash_quality_scaled(ncfo, depamor)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfo/depamor times closeadj
def ocq_f012_operating_cash_quality_lag_per_depamor_252d_base_v142_signal(ncfo, depamor, closeadj):
    r = _operating_cash_quality_scaled(ncfo, depamor)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ncfo| times closeadj
def ocq_f012_operating_cash_quality_abssum_63d_base_v143_signal(ncfo, closeadj):
    result = ncfo.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ncfo| times closeadj
def ocq_f012_operating_cash_quality_abssum_252d_base_v144_signal(ncfo, closeadj):
    result = ncfo.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ncfo| times closeadj
def ocq_f012_operating_cash_quality_abssum_504d_base_v145_signal(ncfo, closeadj):
    result = ncfo.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ncfo
def ocq_f012_operating_cash_quality_acf1_252d_base_v146_signal(ncfo):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ncfo
def ocq_f012_operating_cash_quality_acf1_504d_base_v147_signal(ncfo):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ncfo
def ocq_f012_operating_cash_quality_posinrange_252d_base_v148_signal(ncfo):
    m = _mean(ncfo, 252)
    hi = ncfo.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncfo.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ncfo
def ocq_f012_operating_cash_quality_posinrange_504d_base_v149_signal(ncfo):
    m = _mean(ncfo, 504)
    hi = ncfo.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncfo.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ncfo times closeadj
def ocq_f012_operating_cash_quality_hl_5d_base_v150_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
