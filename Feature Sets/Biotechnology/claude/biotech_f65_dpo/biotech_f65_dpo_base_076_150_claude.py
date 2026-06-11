"""Family f65 - Payables / DPO  (K_WorkingCapital) | base 076-150"""
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
def _dpo_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _dpo_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _dpo_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of payables/marketcap
def dpo_f65_dpo_log_per_marketcap_504d_base_v076_signal(payables, marketcap):
    s = _dpo_scaled(payables, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of payables/equity
def dpo_f65_dpo_log_per_equity_252d_base_v077_signal(payables, equity):
    s = _dpo_scaled(payables, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of payables/equity
def dpo_f65_dpo_log_per_equity_504d_base_v078_signal(payables, equity):
    s = _dpo_scaled(payables, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of payables times closeadj
def dpo_f65_dpo_ewm_21d_base_v079_signal(payables, closeadj):
    result = payables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of payables times closeadj
def dpo_f65_dpo_ewm_63d_base_v080_signal(payables, closeadj):
    result = payables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of payables times closeadj
def dpo_f65_dpo_ewm_252d_base_v081_signal(payables, closeadj):
    result = payables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of payables times closeadj
def dpo_f65_dpo_med_63d_base_v082_signal(payables, closeadj):
    result = payables.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of payables times closeadj
def dpo_f65_dpo_med_252d_base_v083_signal(payables, closeadj):
    result = payables.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of payables times closeadj
def dpo_f65_dpo_med_504d_base_v084_signal(payables, closeadj):
    result = payables.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of payables
def dpo_f65_dpo_skew_252d_base_v085_signal(payables):
    result = payables.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of payables
def dpo_f65_dpo_skew_504d_base_v086_signal(payables):
    result = payables.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of payables
def dpo_f65_dpo_kurt_252d_base_v087_signal(payables):
    result = payables.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of payables
def dpo_f65_dpo_kurt_504d_base_v088_signal(payables):
    result = payables.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of payables times closeadj
def dpo_f65_dpo_rank_252d_base_v089_signal(payables, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = payables.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of payables times closeadj
def dpo_f65_dpo_rank_504d_base_v090_signal(payables, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = payables.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of payables times closeadj
def dpo_f65_dpo_rank_1008d_base_v091_signal(payables, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = payables.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of payables from 63d mean times closeadj
def dpo_f65_dpo_devmean_63d_base_v092_signal(payables, closeadj):
    m = _mean(payables, 63)
    result = (payables - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of payables from 252d mean times closeadj
def dpo_f65_dpo_devmean_252d_base_v093_signal(payables, closeadj):
    m = _mean(payables, 252)
    result = (payables - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of payables from 504d mean times closeadj
def dpo_f65_dpo_devmean_504d_base_v094_signal(payables, closeadj):
    m = _mean(payables, 504)
    result = (payables - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of payables times closeadj
def dpo_f65_dpo_logdiff_21d_base_v095_signal(payables, closeadj):
    lr = _dpo_log(payables)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of payables times closeadj
def dpo_f65_dpo_logdiff_63d_base_v096_signal(payables, closeadj):
    lr = _dpo_log(payables)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of payables times closeadj
def dpo_f65_dpo_logdiff_252d_base_v097_signal(payables, closeadj):
    lr = _dpo_log(payables)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of payables times closeadj
def dpo_f65_dpo_range_63d_base_v098_signal(payables, closeadj):
    hi = payables.rolling(63, min_periods=max(1, 63//2)).max()
    lo = payables.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of payables times closeadj
def dpo_f65_dpo_range_252d_base_v099_signal(payables, closeadj):
    hi = payables.rolling(252, min_periods=max(1, 252//2)).max()
    lo = payables.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of payables times closeadj
def dpo_f65_dpo_range_504d_base_v100_signal(payables, closeadj):
    hi = payables.rolling(504, min_periods=max(1, 504//2)).max()
    lo = payables.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 252d mean times closeadj
def dpo_f65_dpo_rel_252d_base_v101_signal(payables, closeadj):
    m = _mean(payables, 252).replace(0, np.nan)
    result = (payables / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 504d mean times closeadj
def dpo_f65_dpo_rel_504d_base_v102_signal(payables, closeadj):
    m = _mean(payables, 504).replace(0, np.nan)
    result = (payables / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 1008d mean times closeadj
def dpo_f65_dpo_rel_1008d_base_v103_signal(payables, closeadj):
    m = _mean(payables, 1008).replace(0, np.nan)
    result = (payables / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized payables/assets 63d mean
def dpo_f65_dpo_sqnorm_assets_63d_base_v104_signal(payables, assets):
    r = _dpo_scaled(payables, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized payables/assets 252d mean
def dpo_f65_dpo_sqnorm_assets_252d_base_v105_signal(payables, assets):
    r = _dpo_scaled(payables, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized payables/marketcap 63d mean
def dpo_f65_dpo_sqnorm_marketcap_63d_base_v106_signal(payables, marketcap):
    r = _dpo_scaled(payables, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized payables/marketcap 252d mean
def dpo_f65_dpo_sqnorm_marketcap_252d_base_v107_signal(payables, marketcap):
    r = _dpo_scaled(payables, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized payables/equity 63d mean
def dpo_f65_dpo_sqnorm_equity_63d_base_v108_signal(payables, equity):
    r = _dpo_scaled(payables, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized payables/equity 252d mean
def dpo_f65_dpo_sqnorm_equity_252d_base_v109_signal(payables, equity):
    r = _dpo_scaled(payables, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of payables times closeadj
def dpo_f65_dpo_infrat_63d_base_v110_signal(payables, closeadj):
    m = _mean(payables, 63)
    s = _std(payables, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of payables times closeadj
def dpo_f65_dpo_infrat_252d_base_v111_signal(payables, closeadj):
    m = _mean(payables, 252)
    s = _std(payables, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of payables times closeadj
def dpo_f65_dpo_infrat_504d_base_v112_signal(payables, closeadj):
    m = _mean(payables, 504)
    s = _std(payables, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of payables
def dpo_f65_dpo_cv_252d_base_v113_signal(payables):
    m = _mean(payables, 252).abs().replace(0, np.nan)
    s = _std(payables, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of payables
def dpo_f65_dpo_cv_504d_base_v114_signal(payables):
    m = _mean(payables, 504).abs().replace(0, np.nan)
    s = _std(payables, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged payables times closeadj
def dpo_f65_dpo_lag_5d_base_v115_signal(payables, closeadj):
    result = payables.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged payables times closeadj
def dpo_f65_dpo_lag_21d_base_v116_signal(payables, closeadj):
    result = payables.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged payables times closeadj
def dpo_f65_dpo_lag_63d_base_v117_signal(payables, closeadj):
    result = payables.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged payables times closeadj
def dpo_f65_dpo_lag_252d_base_v118_signal(payables, closeadj):
    result = payables.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(payables) / mean(assets) x closeadj
def dpo_f65_dpo_cumper_assets_252d_base_v119_signal(payables, assets, closeadj):
    s = payables.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(payables) / mean(assets) x closeadj
def dpo_f65_dpo_cumper_assets_504d_base_v120_signal(payables, assets, closeadj):
    s = payables.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(payables) / mean(marketcap) x closeadj
def dpo_f65_dpo_cumper_marketcap_252d_base_v121_signal(payables, marketcap, closeadj):
    s = payables.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(payables) / mean(marketcap) x closeadj
def dpo_f65_dpo_cumper_marketcap_504d_base_v122_signal(payables, marketcap, closeadj):
    s = payables.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only payables times closeadj
def dpo_f65_dpo_pos_63d_base_v123_signal(payables, closeadj):
    pos = payables.where(payables > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only payables times closeadj
def dpo_f65_dpo_pos_252d_base_v124_signal(payables, closeadj):
    pos = payables.where(payables > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only payables times closeadj
def dpo_f65_dpo_neg_63d_base_v125_signal(payables, closeadj):
    neg = payables.where(payables < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only payables times closeadj
def dpo_f65_dpo_neg_252d_base_v126_signal(payables, closeadj):
    neg = payables.where(payables < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of payables times closeadj
def dpo_f65_dpo_hl_21d_base_v127_signal(payables, closeadj):
    result = payables.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of payables times closeadj
def dpo_f65_dpo_hl_63d_base_v128_signal(payables, closeadj):
    result = payables.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of payables times closeadj
def dpo_f65_dpo_hl_252d_base_v129_signal(payables, closeadj):
    result = payables.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of payables
def dpo_f65_dpo_z_63d_base_v130_signal(payables):
    result = _z(payables, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of payables
def dpo_f65_dpo_z_126d_base_v131_signal(payables):
    result = _z(payables, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of payables
def dpo_f65_dpo_z_1008d_base_v132_signal(payables):
    result = _z(payables, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of payables times closeadj
def dpo_f65_dpo_st_lt_252_21d_base_v133_signal(payables, closeadj):
    sm = _mean(payables, 21)
    lm = _mean(payables, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of payables times closeadj
def dpo_f65_dpo_st_lt_252_63d_base_v134_signal(payables, closeadj):
    sm = _mean(payables, 63)
    lm = _mean(payables, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of payables times closeadj
def dpo_f65_dpo_st_lt_504_21d_base_v135_signal(payables, closeadj):
    sm = _mean(payables, 21)
    lm = _mean(payables, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of payables times closeadj
def dpo_f65_dpo_st_lt_504_63d_base_v136_signal(payables, closeadj):
    sm = _mean(payables, 63)
    lm = _mean(payables, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged payables/assets times closeadj
def dpo_f65_dpo_lag_per_assets_21d_base_v137_signal(payables, assets, closeadj):
    r = _dpo_scaled(payables, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged payables/assets times closeadj
def dpo_f65_dpo_lag_per_assets_63d_base_v138_signal(payables, assets, closeadj):
    r = _dpo_scaled(payables, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged payables/assets times closeadj
def dpo_f65_dpo_lag_per_assets_252d_base_v139_signal(payables, assets, closeadj):
    r = _dpo_scaled(payables, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged payables/marketcap times closeadj
def dpo_f65_dpo_lag_per_marketcap_21d_base_v140_signal(payables, marketcap, closeadj):
    r = _dpo_scaled(payables, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged payables/marketcap times closeadj
def dpo_f65_dpo_lag_per_marketcap_63d_base_v141_signal(payables, marketcap, closeadj):
    r = _dpo_scaled(payables, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged payables/marketcap times closeadj
def dpo_f65_dpo_lag_per_marketcap_252d_base_v142_signal(payables, marketcap, closeadj):
    r = _dpo_scaled(payables, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |payables| times closeadj
def dpo_f65_dpo_abssum_63d_base_v143_signal(payables, closeadj):
    result = payables.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |payables| times closeadj
def dpo_f65_dpo_abssum_252d_base_v144_signal(payables, closeadj):
    result = payables.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |payables| times closeadj
def dpo_f65_dpo_abssum_504d_base_v145_signal(payables, closeadj):
    result = payables.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of payables
def dpo_f65_dpo_acf1_252d_base_v146_signal(payables):
    result = payables.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of payables
def dpo_f65_dpo_acf1_504d_base_v147_signal(payables):
    result = payables.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of payables
def dpo_f65_dpo_posinrange_252d_base_v148_signal(payables):
    m = _mean(payables, 252)
    hi = payables.rolling(252, min_periods=max(1, 252//2)).max()
    lo = payables.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of payables
def dpo_f65_dpo_posinrange_504d_base_v149_signal(payables):
    m = _mean(payables, 504)
    hi = payables.rolling(504, min_periods=max(1, 504//2)).max()
    lo = payables.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of payables times closeadj
def dpo_f65_dpo_hl_5d_base_v150_signal(payables, closeadj):
    result = payables.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
