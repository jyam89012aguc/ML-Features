"""Family f072 - Cash-adjusted valuation (Valuation Multiples) | Sharadar tables: SF1,DAILY | fields: marketcap, ev, cashneq, investments, debt | base 076-150"""
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
def _cash_adjusted_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_adjusted_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_adjusted_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of marketcap/cashneq
def cav_f072_cash_adjusted_valuation_log_per_cashneq_504d_base_v076_signal(marketcap, cashneq):
    s = _cash_adjusted_valuation_scaled(marketcap, cashneq)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/investments
def cav_f072_cash_adjusted_valuation_log_per_investments_252d_base_v077_signal(marketcap, investments):
    s = _cash_adjusted_valuation_scaled(marketcap, investments)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of marketcap/investments
def cav_f072_cash_adjusted_valuation_log_per_investments_504d_base_v078_signal(marketcap, investments):
    s = _cash_adjusted_valuation_scaled(marketcap, investments)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_ewm_21d_base_v079_signal(marketcap, closeadj):
    result = marketcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_ewm_63d_base_v080_signal(marketcap, closeadj):
    result = marketcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_ewm_252d_base_v081_signal(marketcap, closeadj):
    result = marketcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_med_63d_base_v082_signal(marketcap, closeadj):
    result = marketcap.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_med_252d_base_v083_signal(marketcap, closeadj):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_med_504d_base_v084_signal(marketcap, closeadj):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of marketcap
def cav_f072_cash_adjusted_valuation_skew_252d_base_v085_signal(marketcap):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of marketcap
def cav_f072_cash_adjusted_valuation_skew_504d_base_v086_signal(marketcap):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of marketcap
def cav_f072_cash_adjusted_valuation_kurt_252d_base_v087_signal(marketcap):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of marketcap
def cav_f072_cash_adjusted_valuation_kurt_504d_base_v088_signal(marketcap):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_rank_252d_base_v089_signal(marketcap, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_rank_504d_base_v090_signal(marketcap, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_rank_1008d_base_v091_signal(marketcap, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = marketcap.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of marketcap from 63d mean times closeadj
def cav_f072_cash_adjusted_valuation_devmean_63d_base_v092_signal(marketcap, closeadj):
    m = _mean(marketcap, 63)
    result = (marketcap - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of marketcap from 252d mean times closeadj
def cav_f072_cash_adjusted_valuation_devmean_252d_base_v093_signal(marketcap, closeadj):
    m = _mean(marketcap, 252)
    result = (marketcap - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of marketcap from 504d mean times closeadj
def cav_f072_cash_adjusted_valuation_devmean_504d_base_v094_signal(marketcap, closeadj):
    m = _mean(marketcap, 504)
    result = (marketcap - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_logdiff_21d_base_v095_signal(marketcap, closeadj):
    lr = _cash_adjusted_valuation_log(marketcap)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_logdiff_63d_base_v096_signal(marketcap, closeadj):
    lr = _cash_adjusted_valuation_log(marketcap)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_logdiff_252d_base_v097_signal(marketcap, closeadj):
    lr = _cash_adjusted_valuation_log(marketcap)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_range_63d_base_v098_signal(marketcap, closeadj):
    hi = marketcap.rolling(63, min_periods=max(1, 63//2)).max()
    lo = marketcap.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_range_252d_base_v099_signal(marketcap, closeadj):
    hi = marketcap.rolling(252, min_periods=max(1, 252//2)).max()
    lo = marketcap.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_range_504d_base_v100_signal(marketcap, closeadj):
    hi = marketcap.rolling(504, min_periods=max(1, 504//2)).max()
    lo = marketcap.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d mean times closeadj
def cav_f072_cash_adjusted_valuation_rel_252d_base_v101_signal(marketcap, closeadj):
    m = _mean(marketcap, 252).replace(0, np.nan)
    result = (marketcap / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d mean times closeadj
def cav_f072_cash_adjusted_valuation_rel_504d_base_v102_signal(marketcap, closeadj):
    m = _mean(marketcap, 504).replace(0, np.nan)
    result = (marketcap / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 1008d mean times closeadj
def cav_f072_cash_adjusted_valuation_rel_1008d_base_v103_signal(marketcap, closeadj):
    m = _mean(marketcap, 1008).replace(0, np.nan)
    result = (marketcap / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized marketcap/ev 63d mean
def cav_f072_cash_adjusted_valuation_sqnorm_ev_63d_base_v104_signal(marketcap, ev):
    r = _cash_adjusted_valuation_scaled(marketcap, ev)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized marketcap/ev 252d mean
def cav_f072_cash_adjusted_valuation_sqnorm_ev_252d_base_v105_signal(marketcap, ev):
    r = _cash_adjusted_valuation_scaled(marketcap, ev)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized marketcap/cashneq 63d mean
def cav_f072_cash_adjusted_valuation_sqnorm_cashneq_63d_base_v106_signal(marketcap, cashneq):
    r = _cash_adjusted_valuation_scaled(marketcap, cashneq)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized marketcap/cashneq 252d mean
def cav_f072_cash_adjusted_valuation_sqnorm_cashneq_252d_base_v107_signal(marketcap, cashneq):
    r = _cash_adjusted_valuation_scaled(marketcap, cashneq)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized marketcap/investments 63d mean
def cav_f072_cash_adjusted_valuation_sqnorm_investments_63d_base_v108_signal(marketcap, investments):
    r = _cash_adjusted_valuation_scaled(marketcap, investments)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized marketcap/investments 252d mean
def cav_f072_cash_adjusted_valuation_sqnorm_investments_252d_base_v109_signal(marketcap, investments):
    r = _cash_adjusted_valuation_scaled(marketcap, investments)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_infrat_63d_base_v110_signal(marketcap, closeadj):
    m = _mean(marketcap, 63)
    s = _std(marketcap, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_infrat_252d_base_v111_signal(marketcap, closeadj):
    m = _mean(marketcap, 252)
    s = _std(marketcap, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_infrat_504d_base_v112_signal(marketcap, closeadj):
    m = _mean(marketcap, 504)
    s = _std(marketcap, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of marketcap
def cav_f072_cash_adjusted_valuation_cv_252d_base_v113_signal(marketcap):
    m = _mean(marketcap, 252).abs().replace(0, np.nan)
    s = _std(marketcap, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of marketcap
def cav_f072_cash_adjusted_valuation_cv_504d_base_v114_signal(marketcap):
    m = _mean(marketcap, 504).abs().replace(0, np.nan)
    s = _std(marketcap, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged marketcap times closeadj
def cav_f072_cash_adjusted_valuation_lag_5d_base_v115_signal(marketcap, closeadj):
    result = marketcap.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged marketcap times closeadj
def cav_f072_cash_adjusted_valuation_lag_21d_base_v116_signal(marketcap, closeadj):
    result = marketcap.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged marketcap times closeadj
def cav_f072_cash_adjusted_valuation_lag_63d_base_v117_signal(marketcap, closeadj):
    result = marketcap.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged marketcap times closeadj
def cav_f072_cash_adjusted_valuation_lag_252d_base_v118_signal(marketcap, closeadj):
    result = marketcap.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(marketcap) / mean(ev) x closeadj
def cav_f072_cash_adjusted_valuation_cumper_ev_252d_base_v119_signal(marketcap, ev, closeadj):
    s = marketcap.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ev, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(marketcap) / mean(ev) x closeadj
def cav_f072_cash_adjusted_valuation_cumper_ev_504d_base_v120_signal(marketcap, ev, closeadj):
    s = marketcap.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ev, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(marketcap) / mean(cashneq) x closeadj
def cav_f072_cash_adjusted_valuation_cumper_cashneq_252d_base_v121_signal(marketcap, cashneq, closeadj):
    s = marketcap.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(cashneq, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(marketcap) / mean(cashneq) x closeadj
def cav_f072_cash_adjusted_valuation_cumper_cashneq_504d_base_v122_signal(marketcap, cashneq, closeadj):
    s = marketcap.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(cashneq, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only marketcap times closeadj
def cav_f072_cash_adjusted_valuation_pos_63d_base_v123_signal(marketcap, closeadj):
    pos = marketcap.where(marketcap > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only marketcap times closeadj
def cav_f072_cash_adjusted_valuation_pos_252d_base_v124_signal(marketcap, closeadj):
    pos = marketcap.where(marketcap > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only marketcap times closeadj
def cav_f072_cash_adjusted_valuation_neg_63d_base_v125_signal(marketcap, closeadj):
    neg = marketcap.where(marketcap < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only marketcap times closeadj
def cav_f072_cash_adjusted_valuation_neg_252d_base_v126_signal(marketcap, closeadj):
    neg = marketcap.where(marketcap < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_hl_21d_base_v127_signal(marketcap, closeadj):
    result = marketcap.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_hl_63d_base_v128_signal(marketcap, closeadj):
    result = marketcap.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_hl_252d_base_v129_signal(marketcap, closeadj):
    result = marketcap.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of marketcap
def cav_f072_cash_adjusted_valuation_z_63d_base_v130_signal(marketcap):
    result = _z(marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of marketcap
def cav_f072_cash_adjusted_valuation_z_126d_base_v131_signal(marketcap):
    result = _z(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of marketcap
def cav_f072_cash_adjusted_valuation_z_1008d_base_v132_signal(marketcap):
    result = _z(marketcap, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_st_lt_252_21d_base_v133_signal(marketcap, closeadj):
    sm = _mean(marketcap, 21)
    lm = _mean(marketcap, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_st_lt_252_63d_base_v134_signal(marketcap, closeadj):
    sm = _mean(marketcap, 63)
    lm = _mean(marketcap, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_st_lt_504_21d_base_v135_signal(marketcap, closeadj):
    sm = _mean(marketcap, 21)
    lm = _mean(marketcap, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_st_lt_504_63d_base_v136_signal(marketcap, closeadj):
    sm = _mean(marketcap, 63)
    lm = _mean(marketcap, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged marketcap/ev times closeadj
def cav_f072_cash_adjusted_valuation_lag_per_ev_21d_base_v137_signal(marketcap, ev, closeadj):
    r = _cash_adjusted_valuation_scaled(marketcap, ev)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged marketcap/ev times closeadj
def cav_f072_cash_adjusted_valuation_lag_per_ev_63d_base_v138_signal(marketcap, ev, closeadj):
    r = _cash_adjusted_valuation_scaled(marketcap, ev)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged marketcap/ev times closeadj
def cav_f072_cash_adjusted_valuation_lag_per_ev_252d_base_v139_signal(marketcap, ev, closeadj):
    r = _cash_adjusted_valuation_scaled(marketcap, ev)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged marketcap/cashneq times closeadj
def cav_f072_cash_adjusted_valuation_lag_per_cashneq_21d_base_v140_signal(marketcap, cashneq, closeadj):
    r = _cash_adjusted_valuation_scaled(marketcap, cashneq)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged marketcap/cashneq times closeadj
def cav_f072_cash_adjusted_valuation_lag_per_cashneq_63d_base_v141_signal(marketcap, cashneq, closeadj):
    r = _cash_adjusted_valuation_scaled(marketcap, cashneq)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged marketcap/cashneq times closeadj
def cav_f072_cash_adjusted_valuation_lag_per_cashneq_252d_base_v142_signal(marketcap, cashneq, closeadj):
    r = _cash_adjusted_valuation_scaled(marketcap, cashneq)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |marketcap| times closeadj
def cav_f072_cash_adjusted_valuation_abssum_63d_base_v143_signal(marketcap, closeadj):
    result = marketcap.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |marketcap| times closeadj
def cav_f072_cash_adjusted_valuation_abssum_252d_base_v144_signal(marketcap, closeadj):
    result = marketcap.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |marketcap| times closeadj
def cav_f072_cash_adjusted_valuation_abssum_504d_base_v145_signal(marketcap, closeadj):
    result = marketcap.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of marketcap
def cav_f072_cash_adjusted_valuation_acf1_252d_base_v146_signal(marketcap):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of marketcap
def cav_f072_cash_adjusted_valuation_acf1_504d_base_v147_signal(marketcap):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of marketcap
def cav_f072_cash_adjusted_valuation_posinrange_252d_base_v148_signal(marketcap):
    m = _mean(marketcap, 252)
    hi = marketcap.rolling(252, min_periods=max(1, 252//2)).max()
    lo = marketcap.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of marketcap
def cav_f072_cash_adjusted_valuation_posinrange_504d_base_v149_signal(marketcap):
    m = _mean(marketcap, 504)
    hi = marketcap.rolling(504, min_periods=max(1, 504//2)).max()
    lo = marketcap.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of marketcap times closeadj
def cav_f072_cash_adjusted_valuation_hl_5d_base_v150_signal(marketcap, closeadj):
    result = marketcap.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
