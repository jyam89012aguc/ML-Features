"""Family f94 - Capital-structure actions  (Q_Actions_Events) | base 076-150"""
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
def _capital_actions_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capital_actions_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capital_actions_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of actionvalue/marketcap
def ca_f94_capital_actions_log_per_marketcap_504d_base_v076_signal(actionvalue, marketcap):
    s = _capital_actions_scaled(actionvalue, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of actionvalue/equity
def ca_f94_capital_actions_log_per_equity_252d_base_v077_signal(actionvalue, equity):
    s = _capital_actions_scaled(actionvalue, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of actionvalue/equity
def ca_f94_capital_actions_log_per_equity_504d_base_v078_signal(actionvalue, equity):
    s = _capital_actions_scaled(actionvalue, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of actionvalue times closeadj
def ca_f94_capital_actions_ewm_21d_base_v079_signal(actionvalue, closeadj):
    result = actionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of actionvalue times closeadj
def ca_f94_capital_actions_ewm_63d_base_v080_signal(actionvalue, closeadj):
    result = actionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of actionvalue times closeadj
def ca_f94_capital_actions_ewm_252d_base_v081_signal(actionvalue, closeadj):
    result = actionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of actionvalue times closeadj
def ca_f94_capital_actions_med_63d_base_v082_signal(actionvalue, closeadj):
    result = actionvalue.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of actionvalue times closeadj
def ca_f94_capital_actions_med_252d_base_v083_signal(actionvalue, closeadj):
    result = actionvalue.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of actionvalue times closeadj
def ca_f94_capital_actions_med_504d_base_v084_signal(actionvalue, closeadj):
    result = actionvalue.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of actionvalue
def ca_f94_capital_actions_skew_252d_base_v085_signal(actionvalue):
    result = actionvalue.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of actionvalue
def ca_f94_capital_actions_skew_504d_base_v086_signal(actionvalue):
    result = actionvalue.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of actionvalue
def ca_f94_capital_actions_kurt_252d_base_v087_signal(actionvalue):
    result = actionvalue.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of actionvalue
def ca_f94_capital_actions_kurt_504d_base_v088_signal(actionvalue):
    result = actionvalue.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of actionvalue times closeadj
def ca_f94_capital_actions_rank_252d_base_v089_signal(actionvalue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = actionvalue.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of actionvalue times closeadj
def ca_f94_capital_actions_rank_504d_base_v090_signal(actionvalue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = actionvalue.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of actionvalue times closeadj
def ca_f94_capital_actions_rank_1008d_base_v091_signal(actionvalue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = actionvalue.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of actionvalue from 63d mean times closeadj
def ca_f94_capital_actions_devmean_63d_base_v092_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 63)
    result = (actionvalue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of actionvalue from 252d mean times closeadj
def ca_f94_capital_actions_devmean_252d_base_v093_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 252)
    result = (actionvalue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of actionvalue from 504d mean times closeadj
def ca_f94_capital_actions_devmean_504d_base_v094_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 504)
    result = (actionvalue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of actionvalue times closeadj
def ca_f94_capital_actions_logdiff_21d_base_v095_signal(actionvalue, closeadj):
    lr = _capital_actions_log(actionvalue)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of actionvalue times closeadj
def ca_f94_capital_actions_logdiff_63d_base_v096_signal(actionvalue, closeadj):
    lr = _capital_actions_log(actionvalue)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of actionvalue times closeadj
def ca_f94_capital_actions_logdiff_252d_base_v097_signal(actionvalue, closeadj):
    lr = _capital_actions_log(actionvalue)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of actionvalue times closeadj
def ca_f94_capital_actions_range_63d_base_v098_signal(actionvalue, closeadj):
    hi = actionvalue.rolling(63, min_periods=max(1, 63//2)).max()
    lo = actionvalue.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of actionvalue times closeadj
def ca_f94_capital_actions_range_252d_base_v099_signal(actionvalue, closeadj):
    hi = actionvalue.rolling(252, min_periods=max(1, 252//2)).max()
    lo = actionvalue.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of actionvalue times closeadj
def ca_f94_capital_actions_range_504d_base_v100_signal(actionvalue, closeadj):
    hi = actionvalue.rolling(504, min_periods=max(1, 504//2)).max()
    lo = actionvalue.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 252d mean times closeadj
def ca_f94_capital_actions_rel_252d_base_v101_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 252).replace(0, np.nan)
    result = (actionvalue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 504d mean times closeadj
def ca_f94_capital_actions_rel_504d_base_v102_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 504).replace(0, np.nan)
    result = (actionvalue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 1008d mean times closeadj
def ca_f94_capital_actions_rel_1008d_base_v103_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 1008).replace(0, np.nan)
    result = (actionvalue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized actionvalue/assets 63d mean
def ca_f94_capital_actions_sqnorm_assets_63d_base_v104_signal(actionvalue, assets):
    r = _capital_actions_scaled(actionvalue, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized actionvalue/assets 252d mean
def ca_f94_capital_actions_sqnorm_assets_252d_base_v105_signal(actionvalue, assets):
    r = _capital_actions_scaled(actionvalue, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized actionvalue/marketcap 63d mean
def ca_f94_capital_actions_sqnorm_marketcap_63d_base_v106_signal(actionvalue, marketcap):
    r = _capital_actions_scaled(actionvalue, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized actionvalue/marketcap 252d mean
def ca_f94_capital_actions_sqnorm_marketcap_252d_base_v107_signal(actionvalue, marketcap):
    r = _capital_actions_scaled(actionvalue, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized actionvalue/equity 63d mean
def ca_f94_capital_actions_sqnorm_equity_63d_base_v108_signal(actionvalue, equity):
    r = _capital_actions_scaled(actionvalue, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized actionvalue/equity 252d mean
def ca_f94_capital_actions_sqnorm_equity_252d_base_v109_signal(actionvalue, equity):
    r = _capital_actions_scaled(actionvalue, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of actionvalue times closeadj
def ca_f94_capital_actions_infrat_63d_base_v110_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 63)
    s = _std(actionvalue, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of actionvalue times closeadj
def ca_f94_capital_actions_infrat_252d_base_v111_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 252)
    s = _std(actionvalue, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of actionvalue times closeadj
def ca_f94_capital_actions_infrat_504d_base_v112_signal(actionvalue, closeadj):
    m = _mean(actionvalue, 504)
    s = _std(actionvalue, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of actionvalue
def ca_f94_capital_actions_cv_252d_base_v113_signal(actionvalue):
    m = _mean(actionvalue, 252).abs().replace(0, np.nan)
    s = _std(actionvalue, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of actionvalue
def ca_f94_capital_actions_cv_504d_base_v114_signal(actionvalue):
    m = _mean(actionvalue, 504).abs().replace(0, np.nan)
    s = _std(actionvalue, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged actionvalue times closeadj
def ca_f94_capital_actions_lag_5d_base_v115_signal(actionvalue, closeadj):
    result = actionvalue.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged actionvalue times closeadj
def ca_f94_capital_actions_lag_21d_base_v116_signal(actionvalue, closeadj):
    result = actionvalue.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged actionvalue times closeadj
def ca_f94_capital_actions_lag_63d_base_v117_signal(actionvalue, closeadj):
    result = actionvalue.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged actionvalue times closeadj
def ca_f94_capital_actions_lag_252d_base_v118_signal(actionvalue, closeadj):
    result = actionvalue.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(actionvalue) / mean(assets) x closeadj
def ca_f94_capital_actions_cumper_assets_252d_base_v119_signal(actionvalue, assets, closeadj):
    s = actionvalue.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(actionvalue) / mean(assets) x closeadj
def ca_f94_capital_actions_cumper_assets_504d_base_v120_signal(actionvalue, assets, closeadj):
    s = actionvalue.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(actionvalue) / mean(marketcap) x closeadj
def ca_f94_capital_actions_cumper_marketcap_252d_base_v121_signal(actionvalue, marketcap, closeadj):
    s = actionvalue.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(actionvalue) / mean(marketcap) x closeadj
def ca_f94_capital_actions_cumper_marketcap_504d_base_v122_signal(actionvalue, marketcap, closeadj):
    s = actionvalue.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only actionvalue times closeadj
def ca_f94_capital_actions_pos_63d_base_v123_signal(actionvalue, closeadj):
    pos = actionvalue.where(actionvalue > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only actionvalue times closeadj
def ca_f94_capital_actions_pos_252d_base_v124_signal(actionvalue, closeadj):
    pos = actionvalue.where(actionvalue > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only actionvalue times closeadj
def ca_f94_capital_actions_neg_63d_base_v125_signal(actionvalue, closeadj):
    neg = actionvalue.where(actionvalue < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only actionvalue times closeadj
def ca_f94_capital_actions_neg_252d_base_v126_signal(actionvalue, closeadj):
    neg = actionvalue.where(actionvalue < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of actionvalue times closeadj
def ca_f94_capital_actions_hl_21d_base_v127_signal(actionvalue, closeadj):
    result = actionvalue.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of actionvalue times closeadj
def ca_f94_capital_actions_hl_63d_base_v128_signal(actionvalue, closeadj):
    result = actionvalue.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of actionvalue times closeadj
def ca_f94_capital_actions_hl_252d_base_v129_signal(actionvalue, closeadj):
    result = actionvalue.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of actionvalue
def ca_f94_capital_actions_z_63d_base_v130_signal(actionvalue):
    result = _z(actionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of actionvalue
def ca_f94_capital_actions_z_126d_base_v131_signal(actionvalue):
    result = _z(actionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of actionvalue
def ca_f94_capital_actions_z_1008d_base_v132_signal(actionvalue):
    result = _z(actionvalue, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of actionvalue times closeadj
def ca_f94_capital_actions_st_lt_252_21d_base_v133_signal(actionvalue, closeadj):
    sm = _mean(actionvalue, 21)
    lm = _mean(actionvalue, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of actionvalue times closeadj
def ca_f94_capital_actions_st_lt_252_63d_base_v134_signal(actionvalue, closeadj):
    sm = _mean(actionvalue, 63)
    lm = _mean(actionvalue, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of actionvalue times closeadj
def ca_f94_capital_actions_st_lt_504_21d_base_v135_signal(actionvalue, closeadj):
    sm = _mean(actionvalue, 21)
    lm = _mean(actionvalue, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of actionvalue times closeadj
def ca_f94_capital_actions_st_lt_504_63d_base_v136_signal(actionvalue, closeadj):
    sm = _mean(actionvalue, 63)
    lm = _mean(actionvalue, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged actionvalue/assets times closeadj
def ca_f94_capital_actions_lag_per_assets_21d_base_v137_signal(actionvalue, assets, closeadj):
    r = _capital_actions_scaled(actionvalue, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged actionvalue/assets times closeadj
def ca_f94_capital_actions_lag_per_assets_63d_base_v138_signal(actionvalue, assets, closeadj):
    r = _capital_actions_scaled(actionvalue, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged actionvalue/assets times closeadj
def ca_f94_capital_actions_lag_per_assets_252d_base_v139_signal(actionvalue, assets, closeadj):
    r = _capital_actions_scaled(actionvalue, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged actionvalue/marketcap times closeadj
def ca_f94_capital_actions_lag_per_marketcap_21d_base_v140_signal(actionvalue, marketcap, closeadj):
    r = _capital_actions_scaled(actionvalue, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged actionvalue/marketcap times closeadj
def ca_f94_capital_actions_lag_per_marketcap_63d_base_v141_signal(actionvalue, marketcap, closeadj):
    r = _capital_actions_scaled(actionvalue, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged actionvalue/marketcap times closeadj
def ca_f94_capital_actions_lag_per_marketcap_252d_base_v142_signal(actionvalue, marketcap, closeadj):
    r = _capital_actions_scaled(actionvalue, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |actionvalue| times closeadj
def ca_f94_capital_actions_abssum_63d_base_v143_signal(actionvalue, closeadj):
    result = actionvalue.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |actionvalue| times closeadj
def ca_f94_capital_actions_abssum_252d_base_v144_signal(actionvalue, closeadj):
    result = actionvalue.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |actionvalue| times closeadj
def ca_f94_capital_actions_abssum_504d_base_v145_signal(actionvalue, closeadj):
    result = actionvalue.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of actionvalue
def ca_f94_capital_actions_acf1_252d_base_v146_signal(actionvalue):
    result = actionvalue.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of actionvalue
def ca_f94_capital_actions_acf1_504d_base_v147_signal(actionvalue):
    result = actionvalue.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of actionvalue
def ca_f94_capital_actions_posinrange_252d_base_v148_signal(actionvalue):
    m = _mean(actionvalue, 252)
    hi = actionvalue.rolling(252, min_periods=max(1, 252//2)).max()
    lo = actionvalue.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of actionvalue
def ca_f94_capital_actions_posinrange_504d_base_v149_signal(actionvalue):
    m = _mean(actionvalue, 504)
    hi = actionvalue.rolling(504, min_periods=max(1, 504//2)).max()
    lo = actionvalue.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of actionvalue times closeadj
def ca_f94_capital_actions_hl_5d_base_v150_signal(actionvalue, closeadj):
    result = actionvalue.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
