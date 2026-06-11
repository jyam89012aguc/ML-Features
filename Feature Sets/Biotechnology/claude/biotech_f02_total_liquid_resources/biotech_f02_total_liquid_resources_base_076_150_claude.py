"""Family f02 - Total liquid resources  (A_Liquidity_Runway) | base 076-150"""
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
def _total_liquid_resources_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _total_liquid_resources_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _total_liquid_resources_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of cashneq/marketcap
def tlr_f02_total_liquid_resources_log_per_marketcap_504d_base_v076_signal(cashneq, marketcap):
    s = _total_liquid_resources_scaled(cashneq, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of cashneq/equity
def tlr_f02_total_liquid_resources_log_per_equity_252d_base_v077_signal(cashneq, equity):
    s = _total_liquid_resources_scaled(cashneq, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of cashneq/equity
def tlr_f02_total_liquid_resources_log_per_equity_504d_base_v078_signal(cashneq, equity):
    s = _total_liquid_resources_scaled(cashneq, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of cashneq times closeadj
def tlr_f02_total_liquid_resources_ewm_21d_base_v079_signal(cashneq, closeadj):
    result = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of cashneq times closeadj
def tlr_f02_total_liquid_resources_ewm_63d_base_v080_signal(cashneq, closeadj):
    result = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of cashneq times closeadj
def tlr_f02_total_liquid_resources_ewm_252d_base_v081_signal(cashneq, closeadj):
    result = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of cashneq times closeadj
def tlr_f02_total_liquid_resources_med_63d_base_v082_signal(cashneq, closeadj):
    result = cashneq.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of cashneq times closeadj
def tlr_f02_total_liquid_resources_med_252d_base_v083_signal(cashneq, closeadj):
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of cashneq times closeadj
def tlr_f02_total_liquid_resources_med_504d_base_v084_signal(cashneq, closeadj):
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of cashneq
def tlr_f02_total_liquid_resources_skew_252d_base_v085_signal(cashneq):
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of cashneq
def tlr_f02_total_liquid_resources_skew_504d_base_v086_signal(cashneq):
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of cashneq
def tlr_f02_total_liquid_resources_kurt_252d_base_v087_signal(cashneq):
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of cashneq
def tlr_f02_total_liquid_resources_kurt_504d_base_v088_signal(cashneq):
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of cashneq times closeadj
def tlr_f02_total_liquid_resources_rank_252d_base_v089_signal(cashneq, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of cashneq times closeadj
def tlr_f02_total_liquid_resources_rank_504d_base_v090_signal(cashneq, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of cashneq times closeadj
def tlr_f02_total_liquid_resources_rank_1008d_base_v091_signal(cashneq, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = cashneq.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of cashneq from 63d mean times closeadj
def tlr_f02_total_liquid_resources_devmean_63d_base_v092_signal(cashneq, closeadj):
    m = _mean(cashneq, 63)
    result = (cashneq - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of cashneq from 252d mean times closeadj
def tlr_f02_total_liquid_resources_devmean_252d_base_v093_signal(cashneq, closeadj):
    m = _mean(cashneq, 252)
    result = (cashneq - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of cashneq from 504d mean times closeadj
def tlr_f02_total_liquid_resources_devmean_504d_base_v094_signal(cashneq, closeadj):
    m = _mean(cashneq, 504)
    result = (cashneq - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of cashneq times closeadj
def tlr_f02_total_liquid_resources_logdiff_21d_base_v095_signal(cashneq, closeadj):
    lr = _total_liquid_resources_log(cashneq)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of cashneq times closeadj
def tlr_f02_total_liquid_resources_logdiff_63d_base_v096_signal(cashneq, closeadj):
    lr = _total_liquid_resources_log(cashneq)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of cashneq times closeadj
def tlr_f02_total_liquid_resources_logdiff_252d_base_v097_signal(cashneq, closeadj):
    lr = _total_liquid_resources_log(cashneq)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of cashneq times closeadj
def tlr_f02_total_liquid_resources_range_63d_base_v098_signal(cashneq, closeadj):
    hi = cashneq.rolling(63, min_periods=max(1, 63//2)).max()
    lo = cashneq.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of cashneq times closeadj
def tlr_f02_total_liquid_resources_range_252d_base_v099_signal(cashneq, closeadj):
    hi = cashneq.rolling(252, min_periods=max(1, 252//2)).max()
    lo = cashneq.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of cashneq times closeadj
def tlr_f02_total_liquid_resources_range_504d_base_v100_signal(cashneq, closeadj):
    hi = cashneq.rolling(504, min_periods=max(1, 504//2)).max()
    lo = cashneq.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 252d mean times closeadj
def tlr_f02_total_liquid_resources_rel_252d_base_v101_signal(cashneq, closeadj):
    m = _mean(cashneq, 252).replace(0, np.nan)
    result = (cashneq / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 504d mean times closeadj
def tlr_f02_total_liquid_resources_rel_504d_base_v102_signal(cashneq, closeadj):
    m = _mean(cashneq, 504).replace(0, np.nan)
    result = (cashneq / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 1008d mean times closeadj
def tlr_f02_total_liquid_resources_rel_1008d_base_v103_signal(cashneq, closeadj):
    m = _mean(cashneq, 1008).replace(0, np.nan)
    result = (cashneq / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized cashneq/assets 63d mean
def tlr_f02_total_liquid_resources_sqnorm_assets_63d_base_v104_signal(cashneq, assets):
    r = _total_liquid_resources_scaled(cashneq, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized cashneq/assets 252d mean
def tlr_f02_total_liquid_resources_sqnorm_assets_252d_base_v105_signal(cashneq, assets):
    r = _total_liquid_resources_scaled(cashneq, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized cashneq/marketcap 63d mean
def tlr_f02_total_liquid_resources_sqnorm_marketcap_63d_base_v106_signal(cashneq, marketcap):
    r = _total_liquid_resources_scaled(cashneq, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized cashneq/marketcap 252d mean
def tlr_f02_total_liquid_resources_sqnorm_marketcap_252d_base_v107_signal(cashneq, marketcap):
    r = _total_liquid_resources_scaled(cashneq, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized cashneq/equity 63d mean
def tlr_f02_total_liquid_resources_sqnorm_equity_63d_base_v108_signal(cashneq, equity):
    r = _total_liquid_resources_scaled(cashneq, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized cashneq/equity 252d mean
def tlr_f02_total_liquid_resources_sqnorm_equity_252d_base_v109_signal(cashneq, equity):
    r = _total_liquid_resources_scaled(cashneq, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of cashneq times closeadj
def tlr_f02_total_liquid_resources_infrat_63d_base_v110_signal(cashneq, closeadj):
    m = _mean(cashneq, 63)
    s = _std(cashneq, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of cashneq times closeadj
def tlr_f02_total_liquid_resources_infrat_252d_base_v111_signal(cashneq, closeadj):
    m = _mean(cashneq, 252)
    s = _std(cashneq, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of cashneq times closeadj
def tlr_f02_total_liquid_resources_infrat_504d_base_v112_signal(cashneq, closeadj):
    m = _mean(cashneq, 504)
    s = _std(cashneq, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of cashneq
def tlr_f02_total_liquid_resources_cv_252d_base_v113_signal(cashneq):
    m = _mean(cashneq, 252).abs().replace(0, np.nan)
    s = _std(cashneq, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of cashneq
def tlr_f02_total_liquid_resources_cv_504d_base_v114_signal(cashneq):
    m = _mean(cashneq, 504).abs().replace(0, np.nan)
    s = _std(cashneq, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged cashneq times closeadj
def tlr_f02_total_liquid_resources_lag_5d_base_v115_signal(cashneq, closeadj):
    result = cashneq.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged cashneq times closeadj
def tlr_f02_total_liquid_resources_lag_21d_base_v116_signal(cashneq, closeadj):
    result = cashneq.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged cashneq times closeadj
def tlr_f02_total_liquid_resources_lag_63d_base_v117_signal(cashneq, closeadj):
    result = cashneq.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged cashneq times closeadj
def tlr_f02_total_liquid_resources_lag_252d_base_v118_signal(cashneq, closeadj):
    result = cashneq.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(cashneq) / mean(assets) x closeadj
def tlr_f02_total_liquid_resources_cumper_assets_252d_base_v119_signal(cashneq, assets, closeadj):
    s = cashneq.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(cashneq) / mean(assets) x closeadj
def tlr_f02_total_liquid_resources_cumper_assets_504d_base_v120_signal(cashneq, assets, closeadj):
    s = cashneq.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(cashneq) / mean(marketcap) x closeadj
def tlr_f02_total_liquid_resources_cumper_marketcap_252d_base_v121_signal(cashneq, marketcap, closeadj):
    s = cashneq.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(cashneq) / mean(marketcap) x closeadj
def tlr_f02_total_liquid_resources_cumper_marketcap_504d_base_v122_signal(cashneq, marketcap, closeadj):
    s = cashneq.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only cashneq times closeadj
def tlr_f02_total_liquid_resources_pos_63d_base_v123_signal(cashneq, closeadj):
    pos = cashneq.where(cashneq > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only cashneq times closeadj
def tlr_f02_total_liquid_resources_pos_252d_base_v124_signal(cashneq, closeadj):
    pos = cashneq.where(cashneq > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only cashneq times closeadj
def tlr_f02_total_liquid_resources_neg_63d_base_v125_signal(cashneq, closeadj):
    neg = cashneq.where(cashneq < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only cashneq times closeadj
def tlr_f02_total_liquid_resources_neg_252d_base_v126_signal(cashneq, closeadj):
    neg = cashneq.where(cashneq < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of cashneq times closeadj
def tlr_f02_total_liquid_resources_hl_21d_base_v127_signal(cashneq, closeadj):
    result = cashneq.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of cashneq times closeadj
def tlr_f02_total_liquid_resources_hl_63d_base_v128_signal(cashneq, closeadj):
    result = cashneq.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of cashneq times closeadj
def tlr_f02_total_liquid_resources_hl_252d_base_v129_signal(cashneq, closeadj):
    result = cashneq.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of cashneq
def tlr_f02_total_liquid_resources_z_63d_base_v130_signal(cashneq):
    result = _z(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of cashneq
def tlr_f02_total_liquid_resources_z_126d_base_v131_signal(cashneq):
    result = _z(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of cashneq
def tlr_f02_total_liquid_resources_z_1008d_base_v132_signal(cashneq):
    result = _z(cashneq, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of cashneq times closeadj
def tlr_f02_total_liquid_resources_st_lt_252_21d_base_v133_signal(cashneq, closeadj):
    sm = _mean(cashneq, 21)
    lm = _mean(cashneq, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of cashneq times closeadj
def tlr_f02_total_liquid_resources_st_lt_252_63d_base_v134_signal(cashneq, closeadj):
    sm = _mean(cashneq, 63)
    lm = _mean(cashneq, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of cashneq times closeadj
def tlr_f02_total_liquid_resources_st_lt_504_21d_base_v135_signal(cashneq, closeadj):
    sm = _mean(cashneq, 21)
    lm = _mean(cashneq, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of cashneq times closeadj
def tlr_f02_total_liquid_resources_st_lt_504_63d_base_v136_signal(cashneq, closeadj):
    sm = _mean(cashneq, 63)
    lm = _mean(cashneq, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged cashneq/assets times closeadj
def tlr_f02_total_liquid_resources_lag_per_assets_21d_base_v137_signal(cashneq, assets, closeadj):
    r = _total_liquid_resources_scaled(cashneq, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged cashneq/assets times closeadj
def tlr_f02_total_liquid_resources_lag_per_assets_63d_base_v138_signal(cashneq, assets, closeadj):
    r = _total_liquid_resources_scaled(cashneq, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged cashneq/assets times closeadj
def tlr_f02_total_liquid_resources_lag_per_assets_252d_base_v139_signal(cashneq, assets, closeadj):
    r = _total_liquid_resources_scaled(cashneq, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged cashneq/marketcap times closeadj
def tlr_f02_total_liquid_resources_lag_per_marketcap_21d_base_v140_signal(cashneq, marketcap, closeadj):
    r = _total_liquid_resources_scaled(cashneq, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged cashneq/marketcap times closeadj
def tlr_f02_total_liquid_resources_lag_per_marketcap_63d_base_v141_signal(cashneq, marketcap, closeadj):
    r = _total_liquid_resources_scaled(cashneq, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged cashneq/marketcap times closeadj
def tlr_f02_total_liquid_resources_lag_per_marketcap_252d_base_v142_signal(cashneq, marketcap, closeadj):
    r = _total_liquid_resources_scaled(cashneq, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |cashneq| times closeadj
def tlr_f02_total_liquid_resources_abssum_63d_base_v143_signal(cashneq, closeadj):
    result = cashneq.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |cashneq| times closeadj
def tlr_f02_total_liquid_resources_abssum_252d_base_v144_signal(cashneq, closeadj):
    result = cashneq.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |cashneq| times closeadj
def tlr_f02_total_liquid_resources_abssum_504d_base_v145_signal(cashneq, closeadj):
    result = cashneq.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of cashneq
def tlr_f02_total_liquid_resources_acf1_252d_base_v146_signal(cashneq):
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of cashneq
def tlr_f02_total_liquid_resources_acf1_504d_base_v147_signal(cashneq):
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of cashneq
def tlr_f02_total_liquid_resources_posinrange_252d_base_v148_signal(cashneq):
    m = _mean(cashneq, 252)
    hi = cashneq.rolling(252, min_periods=max(1, 252//2)).max()
    lo = cashneq.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of cashneq
def tlr_f02_total_liquid_resources_posinrange_504d_base_v149_signal(cashneq):
    m = _mean(cashneq, 504)
    hi = cashneq.rolling(504, min_periods=max(1, 504//2)).max()
    lo = cashneq.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of cashneq times closeadj
def tlr_f02_total_liquid_resources_hl_5d_base_v150_signal(cashneq, closeadj):
    result = cashneq.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
