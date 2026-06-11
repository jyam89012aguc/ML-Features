"""Family f42 - Revenue level  (G_Revenue_Growth) | base 076-150"""
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
def _revenue_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _revenue_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _revenue_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of revenue/marketcap
def rvl_f42_revenue_level_log_per_marketcap_504d_base_v076_signal(revenue, marketcap):
    s = _revenue_level_scaled(revenue, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revenue/equity
def rvl_f42_revenue_level_log_per_equity_252d_base_v077_signal(revenue, equity):
    s = _revenue_level_scaled(revenue, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of revenue/equity
def rvl_f42_revenue_level_log_per_equity_504d_base_v078_signal(revenue, equity):
    s = _revenue_level_scaled(revenue, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of revenue times closeadj
def rvl_f42_revenue_level_ewm_21d_base_v079_signal(revenue, closeadj):
    result = revenue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of revenue times closeadj
def rvl_f42_revenue_level_ewm_63d_base_v080_signal(revenue, closeadj):
    result = revenue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of revenue times closeadj
def rvl_f42_revenue_level_ewm_252d_base_v081_signal(revenue, closeadj):
    result = revenue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of revenue times closeadj
def rvl_f42_revenue_level_med_63d_base_v082_signal(revenue, closeadj):
    result = revenue.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of revenue times closeadj
def rvl_f42_revenue_level_med_252d_base_v083_signal(revenue, closeadj):
    result = revenue.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of revenue times closeadj
def rvl_f42_revenue_level_med_504d_base_v084_signal(revenue, closeadj):
    result = revenue.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of revenue
def rvl_f42_revenue_level_skew_252d_base_v085_signal(revenue):
    result = revenue.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of revenue
def rvl_f42_revenue_level_skew_504d_base_v086_signal(revenue):
    result = revenue.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of revenue
def rvl_f42_revenue_level_kurt_252d_base_v087_signal(revenue):
    result = revenue.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of revenue
def rvl_f42_revenue_level_kurt_504d_base_v088_signal(revenue):
    result = revenue.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of revenue times closeadj
def rvl_f42_revenue_level_rank_252d_base_v089_signal(revenue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = revenue.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of revenue times closeadj
def rvl_f42_revenue_level_rank_504d_base_v090_signal(revenue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = revenue.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of revenue times closeadj
def rvl_f42_revenue_level_rank_1008d_base_v091_signal(revenue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = revenue.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of revenue from 63d mean times closeadj
def rvl_f42_revenue_level_devmean_63d_base_v092_signal(revenue, closeadj):
    m = _mean(revenue, 63)
    result = (revenue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of revenue from 252d mean times closeadj
def rvl_f42_revenue_level_devmean_252d_base_v093_signal(revenue, closeadj):
    m = _mean(revenue, 252)
    result = (revenue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of revenue from 504d mean times closeadj
def rvl_f42_revenue_level_devmean_504d_base_v094_signal(revenue, closeadj):
    m = _mean(revenue, 504)
    result = (revenue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of revenue times closeadj
def rvl_f42_revenue_level_logdiff_21d_base_v095_signal(revenue, closeadj):
    lr = _revenue_level_log(revenue)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of revenue times closeadj
def rvl_f42_revenue_level_logdiff_63d_base_v096_signal(revenue, closeadj):
    lr = _revenue_level_log(revenue)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of revenue times closeadj
def rvl_f42_revenue_level_logdiff_252d_base_v097_signal(revenue, closeadj):
    lr = _revenue_level_log(revenue)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of revenue times closeadj
def rvl_f42_revenue_level_range_63d_base_v098_signal(revenue, closeadj):
    hi = revenue.rolling(63, min_periods=max(1, 63//2)).max()
    lo = revenue.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of revenue times closeadj
def rvl_f42_revenue_level_range_252d_base_v099_signal(revenue, closeadj):
    hi = revenue.rolling(252, min_periods=max(1, 252//2)).max()
    lo = revenue.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of revenue times closeadj
def rvl_f42_revenue_level_range_504d_base_v100_signal(revenue, closeadj):
    hi = revenue.rolling(504, min_periods=max(1, 504//2)).max()
    lo = revenue.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 252d mean times closeadj
def rvl_f42_revenue_level_rel_252d_base_v101_signal(revenue, closeadj):
    m = _mean(revenue, 252).replace(0, np.nan)
    result = (revenue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 504d mean times closeadj
def rvl_f42_revenue_level_rel_504d_base_v102_signal(revenue, closeadj):
    m = _mean(revenue, 504).replace(0, np.nan)
    result = (revenue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 1008d mean times closeadj
def rvl_f42_revenue_level_rel_1008d_base_v103_signal(revenue, closeadj):
    m = _mean(revenue, 1008).replace(0, np.nan)
    result = (revenue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revenue/assets 63d mean
def rvl_f42_revenue_level_sqnorm_assets_63d_base_v104_signal(revenue, assets):
    r = _revenue_level_scaled(revenue, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revenue/assets 252d mean
def rvl_f42_revenue_level_sqnorm_assets_252d_base_v105_signal(revenue, assets):
    r = _revenue_level_scaled(revenue, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revenue/marketcap 63d mean
def rvl_f42_revenue_level_sqnorm_marketcap_63d_base_v106_signal(revenue, marketcap):
    r = _revenue_level_scaled(revenue, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revenue/marketcap 252d mean
def rvl_f42_revenue_level_sqnorm_marketcap_252d_base_v107_signal(revenue, marketcap):
    r = _revenue_level_scaled(revenue, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revenue/equity 63d mean
def rvl_f42_revenue_level_sqnorm_equity_63d_base_v108_signal(revenue, equity):
    r = _revenue_level_scaled(revenue, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revenue/equity 252d mean
def rvl_f42_revenue_level_sqnorm_equity_252d_base_v109_signal(revenue, equity):
    r = _revenue_level_scaled(revenue, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of revenue times closeadj
def rvl_f42_revenue_level_infrat_63d_base_v110_signal(revenue, closeadj):
    m = _mean(revenue, 63)
    s = _std(revenue, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of revenue times closeadj
def rvl_f42_revenue_level_infrat_252d_base_v111_signal(revenue, closeadj):
    m = _mean(revenue, 252)
    s = _std(revenue, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of revenue times closeadj
def rvl_f42_revenue_level_infrat_504d_base_v112_signal(revenue, closeadj):
    m = _mean(revenue, 504)
    s = _std(revenue, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of revenue
def rvl_f42_revenue_level_cv_252d_base_v113_signal(revenue):
    m = _mean(revenue, 252).abs().replace(0, np.nan)
    s = _std(revenue, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of revenue
def rvl_f42_revenue_level_cv_504d_base_v114_signal(revenue):
    m = _mean(revenue, 504).abs().replace(0, np.nan)
    s = _std(revenue, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged revenue times closeadj
def rvl_f42_revenue_level_lag_5d_base_v115_signal(revenue, closeadj):
    result = revenue.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged revenue times closeadj
def rvl_f42_revenue_level_lag_21d_base_v116_signal(revenue, closeadj):
    result = revenue.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged revenue times closeadj
def rvl_f42_revenue_level_lag_63d_base_v117_signal(revenue, closeadj):
    result = revenue.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged revenue times closeadj
def rvl_f42_revenue_level_lag_252d_base_v118_signal(revenue, closeadj):
    result = revenue.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(revenue) / mean(assets) x closeadj
def rvl_f42_revenue_level_cumper_assets_252d_base_v119_signal(revenue, assets, closeadj):
    s = revenue.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(revenue) / mean(assets) x closeadj
def rvl_f42_revenue_level_cumper_assets_504d_base_v120_signal(revenue, assets, closeadj):
    s = revenue.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(revenue) / mean(marketcap) x closeadj
def rvl_f42_revenue_level_cumper_marketcap_252d_base_v121_signal(revenue, marketcap, closeadj):
    s = revenue.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(revenue) / mean(marketcap) x closeadj
def rvl_f42_revenue_level_cumper_marketcap_504d_base_v122_signal(revenue, marketcap, closeadj):
    s = revenue.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only revenue times closeadj
def rvl_f42_revenue_level_pos_63d_base_v123_signal(revenue, closeadj):
    pos = revenue.where(revenue > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only revenue times closeadj
def rvl_f42_revenue_level_pos_252d_base_v124_signal(revenue, closeadj):
    pos = revenue.where(revenue > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only revenue times closeadj
def rvl_f42_revenue_level_neg_63d_base_v125_signal(revenue, closeadj):
    neg = revenue.where(revenue < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only revenue times closeadj
def rvl_f42_revenue_level_neg_252d_base_v126_signal(revenue, closeadj):
    neg = revenue.where(revenue < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of revenue times closeadj
def rvl_f42_revenue_level_hl_21d_base_v127_signal(revenue, closeadj):
    result = revenue.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of revenue times closeadj
def rvl_f42_revenue_level_hl_63d_base_v128_signal(revenue, closeadj):
    result = revenue.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of revenue times closeadj
def rvl_f42_revenue_level_hl_252d_base_v129_signal(revenue, closeadj):
    result = revenue.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of revenue
def rvl_f42_revenue_level_z_63d_base_v130_signal(revenue):
    result = _z(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of revenue
def rvl_f42_revenue_level_z_126d_base_v131_signal(revenue):
    result = _z(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of revenue
def rvl_f42_revenue_level_z_1008d_base_v132_signal(revenue):
    result = _z(revenue, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of revenue times closeadj
def rvl_f42_revenue_level_st_lt_252_21d_base_v133_signal(revenue, closeadj):
    sm = _mean(revenue, 21)
    lm = _mean(revenue, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of revenue times closeadj
def rvl_f42_revenue_level_st_lt_252_63d_base_v134_signal(revenue, closeadj):
    sm = _mean(revenue, 63)
    lm = _mean(revenue, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of revenue times closeadj
def rvl_f42_revenue_level_st_lt_504_21d_base_v135_signal(revenue, closeadj):
    sm = _mean(revenue, 21)
    lm = _mean(revenue, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of revenue times closeadj
def rvl_f42_revenue_level_st_lt_504_63d_base_v136_signal(revenue, closeadj):
    sm = _mean(revenue, 63)
    lm = _mean(revenue, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged revenue/assets times closeadj
def rvl_f42_revenue_level_lag_per_assets_21d_base_v137_signal(revenue, assets, closeadj):
    r = _revenue_level_scaled(revenue, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged revenue/assets times closeadj
def rvl_f42_revenue_level_lag_per_assets_63d_base_v138_signal(revenue, assets, closeadj):
    r = _revenue_level_scaled(revenue, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged revenue/assets times closeadj
def rvl_f42_revenue_level_lag_per_assets_252d_base_v139_signal(revenue, assets, closeadj):
    r = _revenue_level_scaled(revenue, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged revenue/marketcap times closeadj
def rvl_f42_revenue_level_lag_per_marketcap_21d_base_v140_signal(revenue, marketcap, closeadj):
    r = _revenue_level_scaled(revenue, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged revenue/marketcap times closeadj
def rvl_f42_revenue_level_lag_per_marketcap_63d_base_v141_signal(revenue, marketcap, closeadj):
    r = _revenue_level_scaled(revenue, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged revenue/marketcap times closeadj
def rvl_f42_revenue_level_lag_per_marketcap_252d_base_v142_signal(revenue, marketcap, closeadj):
    r = _revenue_level_scaled(revenue, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |revenue| times closeadj
def rvl_f42_revenue_level_abssum_63d_base_v143_signal(revenue, closeadj):
    result = revenue.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |revenue| times closeadj
def rvl_f42_revenue_level_abssum_252d_base_v144_signal(revenue, closeadj):
    result = revenue.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |revenue| times closeadj
def rvl_f42_revenue_level_abssum_504d_base_v145_signal(revenue, closeadj):
    result = revenue.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of revenue
def rvl_f42_revenue_level_acf1_252d_base_v146_signal(revenue):
    result = revenue.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of revenue
def rvl_f42_revenue_level_acf1_504d_base_v147_signal(revenue):
    result = revenue.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of revenue
def rvl_f42_revenue_level_posinrange_252d_base_v148_signal(revenue):
    m = _mean(revenue, 252)
    hi = revenue.rolling(252, min_periods=max(1, 252//2)).max()
    lo = revenue.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of revenue
def rvl_f42_revenue_level_posinrange_504d_base_v149_signal(revenue):
    m = _mean(revenue, 504)
    hi = revenue.rolling(504, min_periods=max(1, 504//2)).max()
    lo = revenue.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of revenue times closeadj
def rvl_f42_revenue_level_hl_5d_base_v150_signal(revenue, closeadj):
    result = revenue.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
