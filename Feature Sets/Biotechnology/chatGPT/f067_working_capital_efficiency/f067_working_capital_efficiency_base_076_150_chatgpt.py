"""Family f067 - Working capital productivity (Returns and Efficiency) | Sharadar tables: SF1 | fields: workingcapital, revenue, assets | base 076-150"""
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
def _working_capital_efficiency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _working_capital_efficiency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _working_capital_efficiency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of workingcapital/assets
def wce_f067_working_capital_efficiency_log_per_assets_504d_base_v076_signal(workingcapital, assets):
    s = _working_capital_efficiency_scaled(workingcapital, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of workingcapital/marketcap
def wce_f067_working_capital_efficiency_log_per_marketcap_252d_base_v077_signal(workingcapital, marketcap):
    s = _working_capital_efficiency_scaled(workingcapital, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of workingcapital/marketcap
def wce_f067_working_capital_efficiency_log_per_marketcap_504d_base_v078_signal(workingcapital, marketcap):
    s = _working_capital_efficiency_scaled(workingcapital, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of workingcapital times closeadj
def wce_f067_working_capital_efficiency_ewm_21d_base_v079_signal(workingcapital, closeadj):
    result = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of workingcapital times closeadj
def wce_f067_working_capital_efficiency_ewm_63d_base_v080_signal(workingcapital, closeadj):
    result = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of workingcapital times closeadj
def wce_f067_working_capital_efficiency_ewm_252d_base_v081_signal(workingcapital, closeadj):
    result = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of workingcapital times closeadj
def wce_f067_working_capital_efficiency_med_63d_base_v082_signal(workingcapital, closeadj):
    result = workingcapital.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of workingcapital times closeadj
def wce_f067_working_capital_efficiency_med_252d_base_v083_signal(workingcapital, closeadj):
    result = workingcapital.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of workingcapital times closeadj
def wce_f067_working_capital_efficiency_med_504d_base_v084_signal(workingcapital, closeadj):
    result = workingcapital.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of workingcapital
def wce_f067_working_capital_efficiency_skew_252d_base_v085_signal(workingcapital):
    result = workingcapital.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of workingcapital
def wce_f067_working_capital_efficiency_skew_504d_base_v086_signal(workingcapital):
    result = workingcapital.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of workingcapital
def wce_f067_working_capital_efficiency_kurt_252d_base_v087_signal(workingcapital):
    result = workingcapital.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of workingcapital
def wce_f067_working_capital_efficiency_kurt_504d_base_v088_signal(workingcapital):
    result = workingcapital.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of workingcapital times closeadj
def wce_f067_working_capital_efficiency_rank_252d_base_v089_signal(workingcapital, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = workingcapital.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of workingcapital times closeadj
def wce_f067_working_capital_efficiency_rank_504d_base_v090_signal(workingcapital, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = workingcapital.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of workingcapital times closeadj
def wce_f067_working_capital_efficiency_rank_1008d_base_v091_signal(workingcapital, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = workingcapital.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of workingcapital from 63d mean times closeadj
def wce_f067_working_capital_efficiency_devmean_63d_base_v092_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 63)
    result = (workingcapital - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of workingcapital from 252d mean times closeadj
def wce_f067_working_capital_efficiency_devmean_252d_base_v093_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 252)
    result = (workingcapital - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of workingcapital from 504d mean times closeadj
def wce_f067_working_capital_efficiency_devmean_504d_base_v094_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 504)
    result = (workingcapital - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of workingcapital times closeadj
def wce_f067_working_capital_efficiency_logdiff_21d_base_v095_signal(workingcapital, closeadj):
    lr = _working_capital_efficiency_log(workingcapital)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of workingcapital times closeadj
def wce_f067_working_capital_efficiency_logdiff_63d_base_v096_signal(workingcapital, closeadj):
    lr = _working_capital_efficiency_log(workingcapital)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of workingcapital times closeadj
def wce_f067_working_capital_efficiency_logdiff_252d_base_v097_signal(workingcapital, closeadj):
    lr = _working_capital_efficiency_log(workingcapital)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of workingcapital times closeadj
def wce_f067_working_capital_efficiency_range_63d_base_v098_signal(workingcapital, closeadj):
    hi = workingcapital.rolling(63, min_periods=max(1, 63//2)).max()
    lo = workingcapital.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of workingcapital times closeadj
def wce_f067_working_capital_efficiency_range_252d_base_v099_signal(workingcapital, closeadj):
    hi = workingcapital.rolling(252, min_periods=max(1, 252//2)).max()
    lo = workingcapital.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of workingcapital times closeadj
def wce_f067_working_capital_efficiency_range_504d_base_v100_signal(workingcapital, closeadj):
    hi = workingcapital.rolling(504, min_periods=max(1, 504//2)).max()
    lo = workingcapital.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 252d mean times closeadj
def wce_f067_working_capital_efficiency_rel_252d_base_v101_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 252).replace(0, np.nan)
    result = (workingcapital / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 504d mean times closeadj
def wce_f067_working_capital_efficiency_rel_504d_base_v102_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 504).replace(0, np.nan)
    result = (workingcapital / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 1008d mean times closeadj
def wce_f067_working_capital_efficiency_rel_1008d_base_v103_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 1008).replace(0, np.nan)
    result = (workingcapital / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized workingcapital/revenue 63d mean
def wce_f067_working_capital_efficiency_sqnorm_revenue_63d_base_v104_signal(workingcapital, revenue):
    r = _working_capital_efficiency_scaled(workingcapital, revenue)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized workingcapital/revenue 252d mean
def wce_f067_working_capital_efficiency_sqnorm_revenue_252d_base_v105_signal(workingcapital, revenue):
    r = _working_capital_efficiency_scaled(workingcapital, revenue)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized workingcapital/assets 63d mean
def wce_f067_working_capital_efficiency_sqnorm_assets_63d_base_v106_signal(workingcapital, assets):
    r = _working_capital_efficiency_scaled(workingcapital, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized workingcapital/assets 252d mean
def wce_f067_working_capital_efficiency_sqnorm_assets_252d_base_v107_signal(workingcapital, assets):
    r = _working_capital_efficiency_scaled(workingcapital, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized workingcapital/marketcap 63d mean
def wce_f067_working_capital_efficiency_sqnorm_marketcap_63d_base_v108_signal(workingcapital, marketcap):
    r = _working_capital_efficiency_scaled(workingcapital, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized workingcapital/marketcap 252d mean
def wce_f067_working_capital_efficiency_sqnorm_marketcap_252d_base_v109_signal(workingcapital, marketcap):
    r = _working_capital_efficiency_scaled(workingcapital, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of workingcapital times closeadj
def wce_f067_working_capital_efficiency_infrat_63d_base_v110_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 63)
    s = _std(workingcapital, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of workingcapital times closeadj
def wce_f067_working_capital_efficiency_infrat_252d_base_v111_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 252)
    s = _std(workingcapital, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of workingcapital times closeadj
def wce_f067_working_capital_efficiency_infrat_504d_base_v112_signal(workingcapital, closeadj):
    m = _mean(workingcapital, 504)
    s = _std(workingcapital, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of workingcapital
def wce_f067_working_capital_efficiency_cv_252d_base_v113_signal(workingcapital):
    m = _mean(workingcapital, 252).abs().replace(0, np.nan)
    s = _std(workingcapital, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of workingcapital
def wce_f067_working_capital_efficiency_cv_504d_base_v114_signal(workingcapital):
    m = _mean(workingcapital, 504).abs().replace(0, np.nan)
    s = _std(workingcapital, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged workingcapital times closeadj
def wce_f067_working_capital_efficiency_lag_5d_base_v115_signal(workingcapital, closeadj):
    result = workingcapital.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged workingcapital times closeadj
def wce_f067_working_capital_efficiency_lag_21d_base_v116_signal(workingcapital, closeadj):
    result = workingcapital.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged workingcapital times closeadj
def wce_f067_working_capital_efficiency_lag_63d_base_v117_signal(workingcapital, closeadj):
    result = workingcapital.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged workingcapital times closeadj
def wce_f067_working_capital_efficiency_lag_252d_base_v118_signal(workingcapital, closeadj):
    result = workingcapital.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(workingcapital) / mean(revenue) x closeadj
def wce_f067_working_capital_efficiency_cumper_revenue_252d_base_v119_signal(workingcapital, revenue, closeadj):
    s = workingcapital.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(workingcapital) / mean(revenue) x closeadj
def wce_f067_working_capital_efficiency_cumper_revenue_504d_base_v120_signal(workingcapital, revenue, closeadj):
    s = workingcapital.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(workingcapital) / mean(assets) x closeadj
def wce_f067_working_capital_efficiency_cumper_assets_252d_base_v121_signal(workingcapital, assets, closeadj):
    s = workingcapital.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(workingcapital) / mean(assets) x closeadj
def wce_f067_working_capital_efficiency_cumper_assets_504d_base_v122_signal(workingcapital, assets, closeadj):
    s = workingcapital.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only workingcapital times closeadj
def wce_f067_working_capital_efficiency_pos_63d_base_v123_signal(workingcapital, closeadj):
    pos = workingcapital.where(workingcapital > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only workingcapital times closeadj
def wce_f067_working_capital_efficiency_pos_252d_base_v124_signal(workingcapital, closeadj):
    pos = workingcapital.where(workingcapital > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only workingcapital times closeadj
def wce_f067_working_capital_efficiency_neg_63d_base_v125_signal(workingcapital, closeadj):
    neg = workingcapital.where(workingcapital < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only workingcapital times closeadj
def wce_f067_working_capital_efficiency_neg_252d_base_v126_signal(workingcapital, closeadj):
    neg = workingcapital.where(workingcapital < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of workingcapital times closeadj
def wce_f067_working_capital_efficiency_hl_21d_base_v127_signal(workingcapital, closeadj):
    result = workingcapital.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of workingcapital times closeadj
def wce_f067_working_capital_efficiency_hl_63d_base_v128_signal(workingcapital, closeadj):
    result = workingcapital.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of workingcapital times closeadj
def wce_f067_working_capital_efficiency_hl_252d_base_v129_signal(workingcapital, closeadj):
    result = workingcapital.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of workingcapital
def wce_f067_working_capital_efficiency_z_63d_base_v130_signal(workingcapital):
    result = _z(workingcapital, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of workingcapital
def wce_f067_working_capital_efficiency_z_126d_base_v131_signal(workingcapital):
    result = _z(workingcapital, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of workingcapital
def wce_f067_working_capital_efficiency_z_1008d_base_v132_signal(workingcapital):
    result = _z(workingcapital, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of workingcapital times closeadj
def wce_f067_working_capital_efficiency_st_lt_252_21d_base_v133_signal(workingcapital, closeadj):
    sm = _mean(workingcapital, 21)
    lm = _mean(workingcapital, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of workingcapital times closeadj
def wce_f067_working_capital_efficiency_st_lt_252_63d_base_v134_signal(workingcapital, closeadj):
    sm = _mean(workingcapital, 63)
    lm = _mean(workingcapital, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of workingcapital times closeadj
def wce_f067_working_capital_efficiency_st_lt_504_21d_base_v135_signal(workingcapital, closeadj):
    sm = _mean(workingcapital, 21)
    lm = _mean(workingcapital, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of workingcapital times closeadj
def wce_f067_working_capital_efficiency_st_lt_504_63d_base_v136_signal(workingcapital, closeadj):
    sm = _mean(workingcapital, 63)
    lm = _mean(workingcapital, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged workingcapital/revenue times closeadj
def wce_f067_working_capital_efficiency_lag_per_revenue_21d_base_v137_signal(workingcapital, revenue, closeadj):
    r = _working_capital_efficiency_scaled(workingcapital, revenue)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged workingcapital/revenue times closeadj
def wce_f067_working_capital_efficiency_lag_per_revenue_63d_base_v138_signal(workingcapital, revenue, closeadj):
    r = _working_capital_efficiency_scaled(workingcapital, revenue)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged workingcapital/revenue times closeadj
def wce_f067_working_capital_efficiency_lag_per_revenue_252d_base_v139_signal(workingcapital, revenue, closeadj):
    r = _working_capital_efficiency_scaled(workingcapital, revenue)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged workingcapital/assets times closeadj
def wce_f067_working_capital_efficiency_lag_per_assets_21d_base_v140_signal(workingcapital, assets, closeadj):
    r = _working_capital_efficiency_scaled(workingcapital, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged workingcapital/assets times closeadj
def wce_f067_working_capital_efficiency_lag_per_assets_63d_base_v141_signal(workingcapital, assets, closeadj):
    r = _working_capital_efficiency_scaled(workingcapital, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged workingcapital/assets times closeadj
def wce_f067_working_capital_efficiency_lag_per_assets_252d_base_v142_signal(workingcapital, assets, closeadj):
    r = _working_capital_efficiency_scaled(workingcapital, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |workingcapital| times closeadj
def wce_f067_working_capital_efficiency_abssum_63d_base_v143_signal(workingcapital, closeadj):
    result = workingcapital.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |workingcapital| times closeadj
def wce_f067_working_capital_efficiency_abssum_252d_base_v144_signal(workingcapital, closeadj):
    result = workingcapital.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |workingcapital| times closeadj
def wce_f067_working_capital_efficiency_abssum_504d_base_v145_signal(workingcapital, closeadj):
    result = workingcapital.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of workingcapital
def wce_f067_working_capital_efficiency_acf1_252d_base_v146_signal(workingcapital):
    result = workingcapital.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of workingcapital
def wce_f067_working_capital_efficiency_acf1_504d_base_v147_signal(workingcapital):
    result = workingcapital.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of workingcapital
def wce_f067_working_capital_efficiency_posinrange_252d_base_v148_signal(workingcapital):
    m = _mean(workingcapital, 252)
    hi = workingcapital.rolling(252, min_periods=max(1, 252//2)).max()
    lo = workingcapital.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of workingcapital
def wce_f067_working_capital_efficiency_posinrange_504d_base_v149_signal(workingcapital):
    m = _mean(workingcapital, 504)
    hi = workingcapital.rolling(504, min_periods=max(1, 504//2)).max()
    lo = workingcapital.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of workingcapital times closeadj
def wce_f067_working_capital_efficiency_hl_5d_base_v150_signal(workingcapital, closeadj):
    result = workingcapital.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
