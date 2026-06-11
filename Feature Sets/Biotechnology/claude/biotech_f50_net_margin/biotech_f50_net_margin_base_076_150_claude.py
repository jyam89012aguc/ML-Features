"""Family f50 - Net margin  (H_Margins) | base 076-150"""
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
def _net_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of netmargin/marketcap
def nm_f50_net_margin_log_per_marketcap_504d_base_v076_signal(netmargin, marketcap):
    s = _net_margin_scaled(netmargin, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of netmargin/equity
def nm_f50_net_margin_log_per_equity_252d_base_v077_signal(netmargin, equity):
    s = _net_margin_scaled(netmargin, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of netmargin/equity
def nm_f50_net_margin_log_per_equity_504d_base_v078_signal(netmargin, equity):
    s = _net_margin_scaled(netmargin, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of netmargin times closeadj
def nm_f50_net_margin_ewm_21d_base_v079_signal(netmargin, closeadj):
    result = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of netmargin times closeadj
def nm_f50_net_margin_ewm_63d_base_v080_signal(netmargin, closeadj):
    result = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of netmargin times closeadj
def nm_f50_net_margin_ewm_252d_base_v081_signal(netmargin, closeadj):
    result = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of netmargin times closeadj
def nm_f50_net_margin_med_63d_base_v082_signal(netmargin, closeadj):
    result = netmargin.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of netmargin times closeadj
def nm_f50_net_margin_med_252d_base_v083_signal(netmargin, closeadj):
    result = netmargin.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of netmargin times closeadj
def nm_f50_net_margin_med_504d_base_v084_signal(netmargin, closeadj):
    result = netmargin.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of netmargin
def nm_f50_net_margin_skew_252d_base_v085_signal(netmargin):
    result = netmargin.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of netmargin
def nm_f50_net_margin_skew_504d_base_v086_signal(netmargin):
    result = netmargin.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of netmargin
def nm_f50_net_margin_kurt_252d_base_v087_signal(netmargin):
    result = netmargin.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of netmargin
def nm_f50_net_margin_kurt_504d_base_v088_signal(netmargin):
    result = netmargin.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of netmargin times closeadj
def nm_f50_net_margin_rank_252d_base_v089_signal(netmargin, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = netmargin.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of netmargin times closeadj
def nm_f50_net_margin_rank_504d_base_v090_signal(netmargin, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = netmargin.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of netmargin times closeadj
def nm_f50_net_margin_rank_1008d_base_v091_signal(netmargin, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = netmargin.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of netmargin from 63d mean times closeadj
def nm_f50_net_margin_devmean_63d_base_v092_signal(netmargin, closeadj):
    m = _mean(netmargin, 63)
    result = (netmargin - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of netmargin from 252d mean times closeadj
def nm_f50_net_margin_devmean_252d_base_v093_signal(netmargin, closeadj):
    m = _mean(netmargin, 252)
    result = (netmargin - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of netmargin from 504d mean times closeadj
def nm_f50_net_margin_devmean_504d_base_v094_signal(netmargin, closeadj):
    m = _mean(netmargin, 504)
    result = (netmargin - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of netmargin times closeadj
def nm_f50_net_margin_logdiff_21d_base_v095_signal(netmargin, closeadj):
    lr = _net_margin_log(netmargin)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of netmargin times closeadj
def nm_f50_net_margin_logdiff_63d_base_v096_signal(netmargin, closeadj):
    lr = _net_margin_log(netmargin)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of netmargin times closeadj
def nm_f50_net_margin_logdiff_252d_base_v097_signal(netmargin, closeadj):
    lr = _net_margin_log(netmargin)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of netmargin times closeadj
def nm_f50_net_margin_range_63d_base_v098_signal(netmargin, closeadj):
    hi = netmargin.rolling(63, min_periods=max(1, 63//2)).max()
    lo = netmargin.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of netmargin times closeadj
def nm_f50_net_margin_range_252d_base_v099_signal(netmargin, closeadj):
    hi = netmargin.rolling(252, min_periods=max(1, 252//2)).max()
    lo = netmargin.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of netmargin times closeadj
def nm_f50_net_margin_range_504d_base_v100_signal(netmargin, closeadj):
    hi = netmargin.rolling(504, min_periods=max(1, 504//2)).max()
    lo = netmargin.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 252d mean times closeadj
def nm_f50_net_margin_rel_252d_base_v101_signal(netmargin, closeadj):
    m = _mean(netmargin, 252).replace(0, np.nan)
    result = (netmargin / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 504d mean times closeadj
def nm_f50_net_margin_rel_504d_base_v102_signal(netmargin, closeadj):
    m = _mean(netmargin, 504).replace(0, np.nan)
    result = (netmargin / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 1008d mean times closeadj
def nm_f50_net_margin_rel_1008d_base_v103_signal(netmargin, closeadj):
    m = _mean(netmargin, 1008).replace(0, np.nan)
    result = (netmargin / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netmargin/assets 63d mean
def nm_f50_net_margin_sqnorm_assets_63d_base_v104_signal(netmargin, assets):
    r = _net_margin_scaled(netmargin, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netmargin/assets 252d mean
def nm_f50_net_margin_sqnorm_assets_252d_base_v105_signal(netmargin, assets):
    r = _net_margin_scaled(netmargin, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netmargin/marketcap 63d mean
def nm_f50_net_margin_sqnorm_marketcap_63d_base_v106_signal(netmargin, marketcap):
    r = _net_margin_scaled(netmargin, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netmargin/marketcap 252d mean
def nm_f50_net_margin_sqnorm_marketcap_252d_base_v107_signal(netmargin, marketcap):
    r = _net_margin_scaled(netmargin, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netmargin/equity 63d mean
def nm_f50_net_margin_sqnorm_equity_63d_base_v108_signal(netmargin, equity):
    r = _net_margin_scaled(netmargin, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netmargin/equity 252d mean
def nm_f50_net_margin_sqnorm_equity_252d_base_v109_signal(netmargin, equity):
    r = _net_margin_scaled(netmargin, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of netmargin times closeadj
def nm_f50_net_margin_infrat_63d_base_v110_signal(netmargin, closeadj):
    m = _mean(netmargin, 63)
    s = _std(netmargin, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of netmargin times closeadj
def nm_f50_net_margin_infrat_252d_base_v111_signal(netmargin, closeadj):
    m = _mean(netmargin, 252)
    s = _std(netmargin, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of netmargin times closeadj
def nm_f50_net_margin_infrat_504d_base_v112_signal(netmargin, closeadj):
    m = _mean(netmargin, 504)
    s = _std(netmargin, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of netmargin
def nm_f50_net_margin_cv_252d_base_v113_signal(netmargin):
    m = _mean(netmargin, 252).abs().replace(0, np.nan)
    s = _std(netmargin, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of netmargin
def nm_f50_net_margin_cv_504d_base_v114_signal(netmargin):
    m = _mean(netmargin, 504).abs().replace(0, np.nan)
    s = _std(netmargin, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged netmargin times closeadj
def nm_f50_net_margin_lag_5d_base_v115_signal(netmargin, closeadj):
    result = netmargin.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged netmargin times closeadj
def nm_f50_net_margin_lag_21d_base_v116_signal(netmargin, closeadj):
    result = netmargin.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged netmargin times closeadj
def nm_f50_net_margin_lag_63d_base_v117_signal(netmargin, closeadj):
    result = netmargin.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged netmargin times closeadj
def nm_f50_net_margin_lag_252d_base_v118_signal(netmargin, closeadj):
    result = netmargin.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(netmargin) / mean(assets) x closeadj
def nm_f50_net_margin_cumper_assets_252d_base_v119_signal(netmargin, assets, closeadj):
    s = netmargin.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(netmargin) / mean(assets) x closeadj
def nm_f50_net_margin_cumper_assets_504d_base_v120_signal(netmargin, assets, closeadj):
    s = netmargin.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(netmargin) / mean(marketcap) x closeadj
def nm_f50_net_margin_cumper_marketcap_252d_base_v121_signal(netmargin, marketcap, closeadj):
    s = netmargin.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(netmargin) / mean(marketcap) x closeadj
def nm_f50_net_margin_cumper_marketcap_504d_base_v122_signal(netmargin, marketcap, closeadj):
    s = netmargin.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only netmargin times closeadj
def nm_f50_net_margin_pos_63d_base_v123_signal(netmargin, closeadj):
    pos = netmargin.where(netmargin > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only netmargin times closeadj
def nm_f50_net_margin_pos_252d_base_v124_signal(netmargin, closeadj):
    pos = netmargin.where(netmargin > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only netmargin times closeadj
def nm_f50_net_margin_neg_63d_base_v125_signal(netmargin, closeadj):
    neg = netmargin.where(netmargin < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only netmargin times closeadj
def nm_f50_net_margin_neg_252d_base_v126_signal(netmargin, closeadj):
    neg = netmargin.where(netmargin < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of netmargin times closeadj
def nm_f50_net_margin_hl_21d_base_v127_signal(netmargin, closeadj):
    result = netmargin.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of netmargin times closeadj
def nm_f50_net_margin_hl_63d_base_v128_signal(netmargin, closeadj):
    result = netmargin.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of netmargin times closeadj
def nm_f50_net_margin_hl_252d_base_v129_signal(netmargin, closeadj):
    result = netmargin.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of netmargin
def nm_f50_net_margin_z_63d_base_v130_signal(netmargin):
    result = _z(netmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of netmargin
def nm_f50_net_margin_z_126d_base_v131_signal(netmargin):
    result = _z(netmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of netmargin
def nm_f50_net_margin_z_1008d_base_v132_signal(netmargin):
    result = _z(netmargin, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of netmargin times closeadj
def nm_f50_net_margin_st_lt_252_21d_base_v133_signal(netmargin, closeadj):
    sm = _mean(netmargin, 21)
    lm = _mean(netmargin, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of netmargin times closeadj
def nm_f50_net_margin_st_lt_252_63d_base_v134_signal(netmargin, closeadj):
    sm = _mean(netmargin, 63)
    lm = _mean(netmargin, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of netmargin times closeadj
def nm_f50_net_margin_st_lt_504_21d_base_v135_signal(netmargin, closeadj):
    sm = _mean(netmargin, 21)
    lm = _mean(netmargin, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of netmargin times closeadj
def nm_f50_net_margin_st_lt_504_63d_base_v136_signal(netmargin, closeadj):
    sm = _mean(netmargin, 63)
    lm = _mean(netmargin, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged netmargin/assets times closeadj
def nm_f50_net_margin_lag_per_assets_21d_base_v137_signal(netmargin, assets, closeadj):
    r = _net_margin_scaled(netmargin, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged netmargin/assets times closeadj
def nm_f50_net_margin_lag_per_assets_63d_base_v138_signal(netmargin, assets, closeadj):
    r = _net_margin_scaled(netmargin, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged netmargin/assets times closeadj
def nm_f50_net_margin_lag_per_assets_252d_base_v139_signal(netmargin, assets, closeadj):
    r = _net_margin_scaled(netmargin, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged netmargin/marketcap times closeadj
def nm_f50_net_margin_lag_per_marketcap_21d_base_v140_signal(netmargin, marketcap, closeadj):
    r = _net_margin_scaled(netmargin, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged netmargin/marketcap times closeadj
def nm_f50_net_margin_lag_per_marketcap_63d_base_v141_signal(netmargin, marketcap, closeadj):
    r = _net_margin_scaled(netmargin, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged netmargin/marketcap times closeadj
def nm_f50_net_margin_lag_per_marketcap_252d_base_v142_signal(netmargin, marketcap, closeadj):
    r = _net_margin_scaled(netmargin, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |netmargin| times closeadj
def nm_f50_net_margin_abssum_63d_base_v143_signal(netmargin, closeadj):
    result = netmargin.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |netmargin| times closeadj
def nm_f50_net_margin_abssum_252d_base_v144_signal(netmargin, closeadj):
    result = netmargin.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |netmargin| times closeadj
def nm_f50_net_margin_abssum_504d_base_v145_signal(netmargin, closeadj):
    result = netmargin.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of netmargin
def nm_f50_net_margin_acf1_252d_base_v146_signal(netmargin):
    result = netmargin.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of netmargin
def nm_f50_net_margin_acf1_504d_base_v147_signal(netmargin):
    result = netmargin.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of netmargin
def nm_f50_net_margin_posinrange_252d_base_v148_signal(netmargin):
    m = _mean(netmargin, 252)
    hi = netmargin.rolling(252, min_periods=max(1, 252//2)).max()
    lo = netmargin.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of netmargin
def nm_f50_net_margin_posinrange_504d_base_v149_signal(netmargin):
    m = _mean(netmargin, 504)
    hi = netmargin.rolling(504, min_periods=max(1, 504//2)).max()
    lo = netmargin.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of netmargin times closeadj
def nm_f50_net_margin_hl_5d_base_v150_signal(netmargin, closeadj):
    result = netmargin.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
