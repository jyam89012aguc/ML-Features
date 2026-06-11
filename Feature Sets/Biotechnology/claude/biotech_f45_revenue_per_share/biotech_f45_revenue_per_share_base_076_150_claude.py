"""Family f45 - Revenue per share  (G_Revenue_Growth) | base 076-150"""
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
def _revenue_per_share_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _revenue_per_share_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _revenue_per_share_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sps/marketcap
def rvp_f45_revenue_per_share_log_per_marketcap_504d_base_v076_signal(sps, marketcap):
    s = _revenue_per_share_scaled(sps, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sps/equity
def rvp_f45_revenue_per_share_log_per_equity_252d_base_v077_signal(sps, equity):
    s = _revenue_per_share_scaled(sps, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sps/equity
def rvp_f45_revenue_per_share_log_per_equity_504d_base_v078_signal(sps, equity):
    s = _revenue_per_share_scaled(sps, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sps times closeadj
def rvp_f45_revenue_per_share_ewm_21d_base_v079_signal(sps, closeadj):
    result = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sps times closeadj
def rvp_f45_revenue_per_share_ewm_63d_base_v080_signal(sps, closeadj):
    result = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sps times closeadj
def rvp_f45_revenue_per_share_ewm_252d_base_v081_signal(sps, closeadj):
    result = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sps times closeadj
def rvp_f45_revenue_per_share_med_63d_base_v082_signal(sps, closeadj):
    result = sps.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sps times closeadj
def rvp_f45_revenue_per_share_med_252d_base_v083_signal(sps, closeadj):
    result = sps.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sps times closeadj
def rvp_f45_revenue_per_share_med_504d_base_v084_signal(sps, closeadj):
    result = sps.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sps
def rvp_f45_revenue_per_share_skew_252d_base_v085_signal(sps):
    result = sps.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sps
def rvp_f45_revenue_per_share_skew_504d_base_v086_signal(sps):
    result = sps.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sps
def rvp_f45_revenue_per_share_kurt_252d_base_v087_signal(sps):
    result = sps.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sps
def rvp_f45_revenue_per_share_kurt_504d_base_v088_signal(sps):
    result = sps.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sps times closeadj
def rvp_f45_revenue_per_share_rank_252d_base_v089_signal(sps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sps.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sps times closeadj
def rvp_f45_revenue_per_share_rank_504d_base_v090_signal(sps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sps.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sps times closeadj
def rvp_f45_revenue_per_share_rank_1008d_base_v091_signal(sps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sps.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sps from 63d mean times closeadj
def rvp_f45_revenue_per_share_devmean_63d_base_v092_signal(sps, closeadj):
    m = _mean(sps, 63)
    result = (sps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sps from 252d mean times closeadj
def rvp_f45_revenue_per_share_devmean_252d_base_v093_signal(sps, closeadj):
    m = _mean(sps, 252)
    result = (sps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sps from 504d mean times closeadj
def rvp_f45_revenue_per_share_devmean_504d_base_v094_signal(sps, closeadj):
    m = _mean(sps, 504)
    result = (sps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sps times closeadj
def rvp_f45_revenue_per_share_logdiff_21d_base_v095_signal(sps, closeadj):
    lr = _revenue_per_share_log(sps)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sps times closeadj
def rvp_f45_revenue_per_share_logdiff_63d_base_v096_signal(sps, closeadj):
    lr = _revenue_per_share_log(sps)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sps times closeadj
def rvp_f45_revenue_per_share_logdiff_252d_base_v097_signal(sps, closeadj):
    lr = _revenue_per_share_log(sps)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sps times closeadj
def rvp_f45_revenue_per_share_range_63d_base_v098_signal(sps, closeadj):
    hi = sps.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sps.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sps times closeadj
def rvp_f45_revenue_per_share_range_252d_base_v099_signal(sps, closeadj):
    hi = sps.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sps.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sps times closeadj
def rvp_f45_revenue_per_share_range_504d_base_v100_signal(sps, closeadj):
    hi = sps.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sps.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 252d mean times closeadj
def rvp_f45_revenue_per_share_rel_252d_base_v101_signal(sps, closeadj):
    m = _mean(sps, 252).replace(0, np.nan)
    result = (sps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 504d mean times closeadj
def rvp_f45_revenue_per_share_rel_504d_base_v102_signal(sps, closeadj):
    m = _mean(sps, 504).replace(0, np.nan)
    result = (sps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 1008d mean times closeadj
def rvp_f45_revenue_per_share_rel_1008d_base_v103_signal(sps, closeadj):
    m = _mean(sps, 1008).replace(0, np.nan)
    result = (sps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sps/assets 63d mean
def rvp_f45_revenue_per_share_sqnorm_assets_63d_base_v104_signal(sps, assets):
    r = _revenue_per_share_scaled(sps, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sps/assets 252d mean
def rvp_f45_revenue_per_share_sqnorm_assets_252d_base_v105_signal(sps, assets):
    r = _revenue_per_share_scaled(sps, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sps/marketcap 63d mean
def rvp_f45_revenue_per_share_sqnorm_marketcap_63d_base_v106_signal(sps, marketcap):
    r = _revenue_per_share_scaled(sps, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sps/marketcap 252d mean
def rvp_f45_revenue_per_share_sqnorm_marketcap_252d_base_v107_signal(sps, marketcap):
    r = _revenue_per_share_scaled(sps, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sps/equity 63d mean
def rvp_f45_revenue_per_share_sqnorm_equity_63d_base_v108_signal(sps, equity):
    r = _revenue_per_share_scaled(sps, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sps/equity 252d mean
def rvp_f45_revenue_per_share_sqnorm_equity_252d_base_v109_signal(sps, equity):
    r = _revenue_per_share_scaled(sps, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sps times closeadj
def rvp_f45_revenue_per_share_infrat_63d_base_v110_signal(sps, closeadj):
    m = _mean(sps, 63)
    s = _std(sps, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sps times closeadj
def rvp_f45_revenue_per_share_infrat_252d_base_v111_signal(sps, closeadj):
    m = _mean(sps, 252)
    s = _std(sps, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sps times closeadj
def rvp_f45_revenue_per_share_infrat_504d_base_v112_signal(sps, closeadj):
    m = _mean(sps, 504)
    s = _std(sps, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sps
def rvp_f45_revenue_per_share_cv_252d_base_v113_signal(sps):
    m = _mean(sps, 252).abs().replace(0, np.nan)
    s = _std(sps, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sps
def rvp_f45_revenue_per_share_cv_504d_base_v114_signal(sps):
    m = _mean(sps, 504).abs().replace(0, np.nan)
    s = _std(sps, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sps times closeadj
def rvp_f45_revenue_per_share_lag_5d_base_v115_signal(sps, closeadj):
    result = sps.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sps times closeadj
def rvp_f45_revenue_per_share_lag_21d_base_v116_signal(sps, closeadj):
    result = sps.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sps times closeadj
def rvp_f45_revenue_per_share_lag_63d_base_v117_signal(sps, closeadj):
    result = sps.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sps times closeadj
def rvp_f45_revenue_per_share_lag_252d_base_v118_signal(sps, closeadj):
    result = sps.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sps) / mean(assets) x closeadj
def rvp_f45_revenue_per_share_cumper_assets_252d_base_v119_signal(sps, assets, closeadj):
    s = sps.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sps) / mean(assets) x closeadj
def rvp_f45_revenue_per_share_cumper_assets_504d_base_v120_signal(sps, assets, closeadj):
    s = sps.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sps) / mean(marketcap) x closeadj
def rvp_f45_revenue_per_share_cumper_marketcap_252d_base_v121_signal(sps, marketcap, closeadj):
    s = sps.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sps) / mean(marketcap) x closeadj
def rvp_f45_revenue_per_share_cumper_marketcap_504d_base_v122_signal(sps, marketcap, closeadj):
    s = sps.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sps times closeadj
def rvp_f45_revenue_per_share_pos_63d_base_v123_signal(sps, closeadj):
    pos = sps.where(sps > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sps times closeadj
def rvp_f45_revenue_per_share_pos_252d_base_v124_signal(sps, closeadj):
    pos = sps.where(sps > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sps times closeadj
def rvp_f45_revenue_per_share_neg_63d_base_v125_signal(sps, closeadj):
    neg = sps.where(sps < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sps times closeadj
def rvp_f45_revenue_per_share_neg_252d_base_v126_signal(sps, closeadj):
    neg = sps.where(sps < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sps times closeadj
def rvp_f45_revenue_per_share_hl_21d_base_v127_signal(sps, closeadj):
    result = sps.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sps times closeadj
def rvp_f45_revenue_per_share_hl_63d_base_v128_signal(sps, closeadj):
    result = sps.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sps times closeadj
def rvp_f45_revenue_per_share_hl_252d_base_v129_signal(sps, closeadj):
    result = sps.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sps
def rvp_f45_revenue_per_share_z_63d_base_v130_signal(sps):
    result = _z(sps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sps
def rvp_f45_revenue_per_share_z_126d_base_v131_signal(sps):
    result = _z(sps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sps
def rvp_f45_revenue_per_share_z_1008d_base_v132_signal(sps):
    result = _z(sps, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sps times closeadj
def rvp_f45_revenue_per_share_st_lt_252_21d_base_v133_signal(sps, closeadj):
    sm = _mean(sps, 21)
    lm = _mean(sps, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sps times closeadj
def rvp_f45_revenue_per_share_st_lt_252_63d_base_v134_signal(sps, closeadj):
    sm = _mean(sps, 63)
    lm = _mean(sps, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sps times closeadj
def rvp_f45_revenue_per_share_st_lt_504_21d_base_v135_signal(sps, closeadj):
    sm = _mean(sps, 21)
    lm = _mean(sps, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sps times closeadj
def rvp_f45_revenue_per_share_st_lt_504_63d_base_v136_signal(sps, closeadj):
    sm = _mean(sps, 63)
    lm = _mean(sps, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sps/assets times closeadj
def rvp_f45_revenue_per_share_lag_per_assets_21d_base_v137_signal(sps, assets, closeadj):
    r = _revenue_per_share_scaled(sps, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sps/assets times closeadj
def rvp_f45_revenue_per_share_lag_per_assets_63d_base_v138_signal(sps, assets, closeadj):
    r = _revenue_per_share_scaled(sps, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sps/assets times closeadj
def rvp_f45_revenue_per_share_lag_per_assets_252d_base_v139_signal(sps, assets, closeadj):
    r = _revenue_per_share_scaled(sps, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sps/marketcap times closeadj
def rvp_f45_revenue_per_share_lag_per_marketcap_21d_base_v140_signal(sps, marketcap, closeadj):
    r = _revenue_per_share_scaled(sps, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sps/marketcap times closeadj
def rvp_f45_revenue_per_share_lag_per_marketcap_63d_base_v141_signal(sps, marketcap, closeadj):
    r = _revenue_per_share_scaled(sps, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sps/marketcap times closeadj
def rvp_f45_revenue_per_share_lag_per_marketcap_252d_base_v142_signal(sps, marketcap, closeadj):
    r = _revenue_per_share_scaled(sps, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sps| times closeadj
def rvp_f45_revenue_per_share_abssum_63d_base_v143_signal(sps, closeadj):
    result = sps.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sps| times closeadj
def rvp_f45_revenue_per_share_abssum_252d_base_v144_signal(sps, closeadj):
    result = sps.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sps| times closeadj
def rvp_f45_revenue_per_share_abssum_504d_base_v145_signal(sps, closeadj):
    result = sps.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sps
def rvp_f45_revenue_per_share_acf1_252d_base_v146_signal(sps):
    result = sps.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sps
def rvp_f45_revenue_per_share_acf1_504d_base_v147_signal(sps):
    result = sps.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sps
def rvp_f45_revenue_per_share_posinrange_252d_base_v148_signal(sps):
    m = _mean(sps, 252)
    hi = sps.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sps.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sps
def rvp_f45_revenue_per_share_posinrange_504d_base_v149_signal(sps):
    m = _mean(sps, 504)
    hi = sps.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sps.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sps times closeadj
def rvp_f45_revenue_per_share_hl_5d_base_v150_signal(sps, closeadj):
    result = sps.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
