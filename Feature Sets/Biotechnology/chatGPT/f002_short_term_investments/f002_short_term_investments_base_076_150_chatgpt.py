"""Family f002 - SF1 liquid securities buffer (Liquidity and Runway) | Sharadar tables: SF1 | fields: investmentsc, investments, cashneq, assets | base 076-150"""
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
def _short_term_investments_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _short_term_investments_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _short_term_investments_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of investmentsc/cashneq
def sti_f002_short_term_investments_log_per_cashneq_504d_base_v076_signal(investmentsc, cashneq):
    s = _short_term_investments_scaled(investmentsc, cashneq)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of investmentsc/assets
def sti_f002_short_term_investments_log_per_assets_252d_base_v077_signal(investmentsc, assets):
    s = _short_term_investments_scaled(investmentsc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of investmentsc/assets
def sti_f002_short_term_investments_log_per_assets_504d_base_v078_signal(investmentsc, assets):
    s = _short_term_investments_scaled(investmentsc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of investmentsc times closeadj
def sti_f002_short_term_investments_ewm_21d_base_v079_signal(investmentsc, closeadj):
    result = investmentsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of investmentsc times closeadj
def sti_f002_short_term_investments_ewm_63d_base_v080_signal(investmentsc, closeadj):
    result = investmentsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of investmentsc times closeadj
def sti_f002_short_term_investments_ewm_252d_base_v081_signal(investmentsc, closeadj):
    result = investmentsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of investmentsc times closeadj
def sti_f002_short_term_investments_med_63d_base_v082_signal(investmentsc, closeadj):
    result = investmentsc.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of investmentsc times closeadj
def sti_f002_short_term_investments_med_252d_base_v083_signal(investmentsc, closeadj):
    result = investmentsc.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of investmentsc times closeadj
def sti_f002_short_term_investments_med_504d_base_v084_signal(investmentsc, closeadj):
    result = investmentsc.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of investmentsc
def sti_f002_short_term_investments_skew_252d_base_v085_signal(investmentsc):
    result = investmentsc.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of investmentsc
def sti_f002_short_term_investments_skew_504d_base_v086_signal(investmentsc):
    result = investmentsc.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of investmentsc
def sti_f002_short_term_investments_kurt_252d_base_v087_signal(investmentsc):
    result = investmentsc.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of investmentsc
def sti_f002_short_term_investments_kurt_504d_base_v088_signal(investmentsc):
    result = investmentsc.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of investmentsc times closeadj
def sti_f002_short_term_investments_rank_252d_base_v089_signal(investmentsc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = investmentsc.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of investmentsc times closeadj
def sti_f002_short_term_investments_rank_504d_base_v090_signal(investmentsc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = investmentsc.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of investmentsc times closeadj
def sti_f002_short_term_investments_rank_1008d_base_v091_signal(investmentsc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = investmentsc.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of investmentsc from 63d mean times closeadj
def sti_f002_short_term_investments_devmean_63d_base_v092_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 63)
    result = (investmentsc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of investmentsc from 252d mean times closeadj
def sti_f002_short_term_investments_devmean_252d_base_v093_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 252)
    result = (investmentsc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of investmentsc from 504d mean times closeadj
def sti_f002_short_term_investments_devmean_504d_base_v094_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 504)
    result = (investmentsc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of investmentsc times closeadj
def sti_f002_short_term_investments_logdiff_21d_base_v095_signal(investmentsc, closeadj):
    lr = _short_term_investments_log(investmentsc)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of investmentsc times closeadj
def sti_f002_short_term_investments_logdiff_63d_base_v096_signal(investmentsc, closeadj):
    lr = _short_term_investments_log(investmentsc)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of investmentsc times closeadj
def sti_f002_short_term_investments_logdiff_252d_base_v097_signal(investmentsc, closeadj):
    lr = _short_term_investments_log(investmentsc)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of investmentsc times closeadj
def sti_f002_short_term_investments_range_63d_base_v098_signal(investmentsc, closeadj):
    hi = investmentsc.rolling(63, min_periods=max(1, 63//2)).max()
    lo = investmentsc.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of investmentsc times closeadj
def sti_f002_short_term_investments_range_252d_base_v099_signal(investmentsc, closeadj):
    hi = investmentsc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = investmentsc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of investmentsc times closeadj
def sti_f002_short_term_investments_range_504d_base_v100_signal(investmentsc, closeadj):
    hi = investmentsc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = investmentsc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# investmentsc relative to 252d mean times closeadj
def sti_f002_short_term_investments_rel_252d_base_v101_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 252).replace(0, np.nan)
    result = (investmentsc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# investmentsc relative to 504d mean times closeadj
def sti_f002_short_term_investments_rel_504d_base_v102_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 504).replace(0, np.nan)
    result = (investmentsc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# investmentsc relative to 1008d mean times closeadj
def sti_f002_short_term_investments_rel_1008d_base_v103_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 1008).replace(0, np.nan)
    result = (investmentsc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized investmentsc/investments 63d mean
def sti_f002_short_term_investments_sqnorm_investments_63d_base_v104_signal(investmentsc, investments):
    r = _short_term_investments_scaled(investmentsc, investments)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized investmentsc/investments 252d mean
def sti_f002_short_term_investments_sqnorm_investments_252d_base_v105_signal(investmentsc, investments):
    r = _short_term_investments_scaled(investmentsc, investments)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized investmentsc/cashneq 63d mean
def sti_f002_short_term_investments_sqnorm_cashneq_63d_base_v106_signal(investmentsc, cashneq):
    r = _short_term_investments_scaled(investmentsc, cashneq)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized investmentsc/cashneq 252d mean
def sti_f002_short_term_investments_sqnorm_cashneq_252d_base_v107_signal(investmentsc, cashneq):
    r = _short_term_investments_scaled(investmentsc, cashneq)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized investmentsc/assets 63d mean
def sti_f002_short_term_investments_sqnorm_assets_63d_base_v108_signal(investmentsc, assets):
    r = _short_term_investments_scaled(investmentsc, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized investmentsc/assets 252d mean
def sti_f002_short_term_investments_sqnorm_assets_252d_base_v109_signal(investmentsc, assets):
    r = _short_term_investments_scaled(investmentsc, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of investmentsc times closeadj
def sti_f002_short_term_investments_infrat_63d_base_v110_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 63)
    s = _std(investmentsc, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of investmentsc times closeadj
def sti_f002_short_term_investments_infrat_252d_base_v111_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 252)
    s = _std(investmentsc, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of investmentsc times closeadj
def sti_f002_short_term_investments_infrat_504d_base_v112_signal(investmentsc, closeadj):
    m = _mean(investmentsc, 504)
    s = _std(investmentsc, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of investmentsc
def sti_f002_short_term_investments_cv_252d_base_v113_signal(investmentsc):
    m = _mean(investmentsc, 252).abs().replace(0, np.nan)
    s = _std(investmentsc, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of investmentsc
def sti_f002_short_term_investments_cv_504d_base_v114_signal(investmentsc):
    m = _mean(investmentsc, 504).abs().replace(0, np.nan)
    s = _std(investmentsc, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged investmentsc times closeadj
def sti_f002_short_term_investments_lag_5d_base_v115_signal(investmentsc, closeadj):
    result = investmentsc.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged investmentsc times closeadj
def sti_f002_short_term_investments_lag_21d_base_v116_signal(investmentsc, closeadj):
    result = investmentsc.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged investmentsc times closeadj
def sti_f002_short_term_investments_lag_63d_base_v117_signal(investmentsc, closeadj):
    result = investmentsc.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged investmentsc times closeadj
def sti_f002_short_term_investments_lag_252d_base_v118_signal(investmentsc, closeadj):
    result = investmentsc.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(investmentsc) / mean(investments) x closeadj
def sti_f002_short_term_investments_cumper_investments_252d_base_v119_signal(investmentsc, investments, closeadj):
    s = investmentsc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(investments, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(investmentsc) / mean(investments) x closeadj
def sti_f002_short_term_investments_cumper_investments_504d_base_v120_signal(investmentsc, investments, closeadj):
    s = investmentsc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(investments, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(investmentsc) / mean(cashneq) x closeadj
def sti_f002_short_term_investments_cumper_cashneq_252d_base_v121_signal(investmentsc, cashneq, closeadj):
    s = investmentsc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(cashneq, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(investmentsc) / mean(cashneq) x closeadj
def sti_f002_short_term_investments_cumper_cashneq_504d_base_v122_signal(investmentsc, cashneq, closeadj):
    s = investmentsc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(cashneq, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only investmentsc times closeadj
def sti_f002_short_term_investments_pos_63d_base_v123_signal(investmentsc, closeadj):
    pos = investmentsc.where(investmentsc > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only investmentsc times closeadj
def sti_f002_short_term_investments_pos_252d_base_v124_signal(investmentsc, closeadj):
    pos = investmentsc.where(investmentsc > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only investmentsc times closeadj
def sti_f002_short_term_investments_neg_63d_base_v125_signal(investmentsc, closeadj):
    neg = investmentsc.where(investmentsc < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only investmentsc times closeadj
def sti_f002_short_term_investments_neg_252d_base_v126_signal(investmentsc, closeadj):
    neg = investmentsc.where(investmentsc < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of investmentsc times closeadj
def sti_f002_short_term_investments_hl_21d_base_v127_signal(investmentsc, closeadj):
    result = investmentsc.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of investmentsc times closeadj
def sti_f002_short_term_investments_hl_63d_base_v128_signal(investmentsc, closeadj):
    result = investmentsc.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of investmentsc times closeadj
def sti_f002_short_term_investments_hl_252d_base_v129_signal(investmentsc, closeadj):
    result = investmentsc.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of investmentsc
def sti_f002_short_term_investments_z_63d_base_v130_signal(investmentsc):
    result = _z(investmentsc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of investmentsc
def sti_f002_short_term_investments_z_126d_base_v131_signal(investmentsc):
    result = _z(investmentsc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of investmentsc
def sti_f002_short_term_investments_z_1008d_base_v132_signal(investmentsc):
    result = _z(investmentsc, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of investmentsc times closeadj
def sti_f002_short_term_investments_st_lt_252_21d_base_v133_signal(investmentsc, closeadj):
    sm = _mean(investmentsc, 21)
    lm = _mean(investmentsc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of investmentsc times closeadj
def sti_f002_short_term_investments_st_lt_252_63d_base_v134_signal(investmentsc, closeadj):
    sm = _mean(investmentsc, 63)
    lm = _mean(investmentsc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of investmentsc times closeadj
def sti_f002_short_term_investments_st_lt_504_21d_base_v135_signal(investmentsc, closeadj):
    sm = _mean(investmentsc, 21)
    lm = _mean(investmentsc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of investmentsc times closeadj
def sti_f002_short_term_investments_st_lt_504_63d_base_v136_signal(investmentsc, closeadj):
    sm = _mean(investmentsc, 63)
    lm = _mean(investmentsc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged investmentsc/investments times closeadj
def sti_f002_short_term_investments_lag_per_investments_21d_base_v137_signal(investmentsc, investments, closeadj):
    r = _short_term_investments_scaled(investmentsc, investments)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged investmentsc/investments times closeadj
def sti_f002_short_term_investments_lag_per_investments_63d_base_v138_signal(investmentsc, investments, closeadj):
    r = _short_term_investments_scaled(investmentsc, investments)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged investmentsc/investments times closeadj
def sti_f002_short_term_investments_lag_per_investments_252d_base_v139_signal(investmentsc, investments, closeadj):
    r = _short_term_investments_scaled(investmentsc, investments)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged investmentsc/cashneq times closeadj
def sti_f002_short_term_investments_lag_per_cashneq_21d_base_v140_signal(investmentsc, cashneq, closeadj):
    r = _short_term_investments_scaled(investmentsc, cashneq)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged investmentsc/cashneq times closeadj
def sti_f002_short_term_investments_lag_per_cashneq_63d_base_v141_signal(investmentsc, cashneq, closeadj):
    r = _short_term_investments_scaled(investmentsc, cashneq)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged investmentsc/cashneq times closeadj
def sti_f002_short_term_investments_lag_per_cashneq_252d_base_v142_signal(investmentsc, cashneq, closeadj):
    r = _short_term_investments_scaled(investmentsc, cashneq)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |investmentsc| times closeadj
def sti_f002_short_term_investments_abssum_63d_base_v143_signal(investmentsc, closeadj):
    result = investmentsc.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |investmentsc| times closeadj
def sti_f002_short_term_investments_abssum_252d_base_v144_signal(investmentsc, closeadj):
    result = investmentsc.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |investmentsc| times closeadj
def sti_f002_short_term_investments_abssum_504d_base_v145_signal(investmentsc, closeadj):
    result = investmentsc.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of investmentsc
def sti_f002_short_term_investments_acf1_252d_base_v146_signal(investmentsc):
    result = investmentsc.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of investmentsc
def sti_f002_short_term_investments_acf1_504d_base_v147_signal(investmentsc):
    result = investmentsc.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of investmentsc
def sti_f002_short_term_investments_posinrange_252d_base_v148_signal(investmentsc):
    m = _mean(investmentsc, 252)
    hi = investmentsc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = investmentsc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of investmentsc
def sti_f002_short_term_investments_posinrange_504d_base_v149_signal(investmentsc):
    m = _mean(investmentsc, 504)
    hi = investmentsc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = investmentsc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of investmentsc times closeadj
def sti_f002_short_term_investments_hl_5d_base_v150_signal(investmentsc, closeadj):
    result = investmentsc.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
