"""Family f61 - Asset turnover  (J_Returns_Efficiency) | base 076-150"""
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
def _asset_turnover_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _asset_turnover_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _asset_turnover_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of assetturnover/marketcap
def at_f61_asset_turnover_log_per_marketcap_504d_base_v076_signal(assetturnover, marketcap):
    s = _asset_turnover_scaled(assetturnover, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assetturnover/equity
def at_f61_asset_turnover_log_per_equity_252d_base_v077_signal(assetturnover, equity):
    s = _asset_turnover_scaled(assetturnover, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of assetturnover/equity
def at_f61_asset_turnover_log_per_equity_504d_base_v078_signal(assetturnover, equity):
    s = _asset_turnover_scaled(assetturnover, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of assetturnover times closeadj
def at_f61_asset_turnover_ewm_21d_base_v079_signal(assetturnover, closeadj):
    result = assetturnover.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of assetturnover times closeadj
def at_f61_asset_turnover_ewm_63d_base_v080_signal(assetturnover, closeadj):
    result = assetturnover.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of assetturnover times closeadj
def at_f61_asset_turnover_ewm_252d_base_v081_signal(assetturnover, closeadj):
    result = assetturnover.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of assetturnover times closeadj
def at_f61_asset_turnover_med_63d_base_v082_signal(assetturnover, closeadj):
    result = assetturnover.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of assetturnover times closeadj
def at_f61_asset_turnover_med_252d_base_v083_signal(assetturnover, closeadj):
    result = assetturnover.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of assetturnover times closeadj
def at_f61_asset_turnover_med_504d_base_v084_signal(assetturnover, closeadj):
    result = assetturnover.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of assetturnover
def at_f61_asset_turnover_skew_252d_base_v085_signal(assetturnover):
    result = assetturnover.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of assetturnover
def at_f61_asset_turnover_skew_504d_base_v086_signal(assetturnover):
    result = assetturnover.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of assetturnover
def at_f61_asset_turnover_kurt_252d_base_v087_signal(assetturnover):
    result = assetturnover.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of assetturnover
def at_f61_asset_turnover_kurt_504d_base_v088_signal(assetturnover):
    result = assetturnover.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of assetturnover times closeadj
def at_f61_asset_turnover_rank_252d_base_v089_signal(assetturnover, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assetturnover.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of assetturnover times closeadj
def at_f61_asset_turnover_rank_504d_base_v090_signal(assetturnover, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assetturnover.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of assetturnover times closeadj
def at_f61_asset_turnover_rank_1008d_base_v091_signal(assetturnover, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assetturnover.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assetturnover from 63d mean times closeadj
def at_f61_asset_turnover_devmean_63d_base_v092_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 63)
    result = (assetturnover - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assetturnover from 252d mean times closeadj
def at_f61_asset_turnover_devmean_252d_base_v093_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 252)
    result = (assetturnover - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assetturnover from 504d mean times closeadj
def at_f61_asset_turnover_devmean_504d_base_v094_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 504)
    result = (assetturnover - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of assetturnover times closeadj
def at_f61_asset_turnover_logdiff_21d_base_v095_signal(assetturnover, closeadj):
    lr = _asset_turnover_log(assetturnover)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of assetturnover times closeadj
def at_f61_asset_turnover_logdiff_63d_base_v096_signal(assetturnover, closeadj):
    lr = _asset_turnover_log(assetturnover)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of assetturnover times closeadj
def at_f61_asset_turnover_logdiff_252d_base_v097_signal(assetturnover, closeadj):
    lr = _asset_turnover_log(assetturnover)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of assetturnover times closeadj
def at_f61_asset_turnover_range_63d_base_v098_signal(assetturnover, closeadj):
    hi = assetturnover.rolling(63, min_periods=max(1, 63//2)).max()
    lo = assetturnover.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of assetturnover times closeadj
def at_f61_asset_turnover_range_252d_base_v099_signal(assetturnover, closeadj):
    hi = assetturnover.rolling(252, min_periods=max(1, 252//2)).max()
    lo = assetturnover.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of assetturnover times closeadj
def at_f61_asset_turnover_range_504d_base_v100_signal(assetturnover, closeadj):
    hi = assetturnover.rolling(504, min_periods=max(1, 504//2)).max()
    lo = assetturnover.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 252d mean times closeadj
def at_f61_asset_turnover_rel_252d_base_v101_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 252).replace(0, np.nan)
    result = (assetturnover / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 504d mean times closeadj
def at_f61_asset_turnover_rel_504d_base_v102_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 504).replace(0, np.nan)
    result = (assetturnover / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 1008d mean times closeadj
def at_f61_asset_turnover_rel_1008d_base_v103_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 1008).replace(0, np.nan)
    result = (assetturnover / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetturnover/assets 63d mean
def at_f61_asset_turnover_sqnorm_assets_63d_base_v104_signal(assetturnover, assets):
    r = _asset_turnover_scaled(assetturnover, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetturnover/assets 252d mean
def at_f61_asset_turnover_sqnorm_assets_252d_base_v105_signal(assetturnover, assets):
    r = _asset_turnover_scaled(assetturnover, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetturnover/marketcap 63d mean
def at_f61_asset_turnover_sqnorm_marketcap_63d_base_v106_signal(assetturnover, marketcap):
    r = _asset_turnover_scaled(assetturnover, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetturnover/marketcap 252d mean
def at_f61_asset_turnover_sqnorm_marketcap_252d_base_v107_signal(assetturnover, marketcap):
    r = _asset_turnover_scaled(assetturnover, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetturnover/equity 63d mean
def at_f61_asset_turnover_sqnorm_equity_63d_base_v108_signal(assetturnover, equity):
    r = _asset_turnover_scaled(assetturnover, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetturnover/equity 252d mean
def at_f61_asset_turnover_sqnorm_equity_252d_base_v109_signal(assetturnover, equity):
    r = _asset_turnover_scaled(assetturnover, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of assetturnover times closeadj
def at_f61_asset_turnover_infrat_63d_base_v110_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 63)
    s = _std(assetturnover, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of assetturnover times closeadj
def at_f61_asset_turnover_infrat_252d_base_v111_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 252)
    s = _std(assetturnover, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of assetturnover times closeadj
def at_f61_asset_turnover_infrat_504d_base_v112_signal(assetturnover, closeadj):
    m = _mean(assetturnover, 504)
    s = _std(assetturnover, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of assetturnover
def at_f61_asset_turnover_cv_252d_base_v113_signal(assetturnover):
    m = _mean(assetturnover, 252).abs().replace(0, np.nan)
    s = _std(assetturnover, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of assetturnover
def at_f61_asset_turnover_cv_504d_base_v114_signal(assetturnover):
    m = _mean(assetturnover, 504).abs().replace(0, np.nan)
    s = _std(assetturnover, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged assetturnover times closeadj
def at_f61_asset_turnover_lag_5d_base_v115_signal(assetturnover, closeadj):
    result = assetturnover.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assetturnover times closeadj
def at_f61_asset_turnover_lag_21d_base_v116_signal(assetturnover, closeadj):
    result = assetturnover.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assetturnover times closeadj
def at_f61_asset_turnover_lag_63d_base_v117_signal(assetturnover, closeadj):
    result = assetturnover.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assetturnover times closeadj
def at_f61_asset_turnover_lag_252d_base_v118_signal(assetturnover, closeadj):
    result = assetturnover.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(assetturnover) / mean(assets) x closeadj
def at_f61_asset_turnover_cumper_assets_252d_base_v119_signal(assetturnover, assets, closeadj):
    s = assetturnover.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(assetturnover) / mean(assets) x closeadj
def at_f61_asset_turnover_cumper_assets_504d_base_v120_signal(assetturnover, assets, closeadj):
    s = assetturnover.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(assetturnover) / mean(marketcap) x closeadj
def at_f61_asset_turnover_cumper_marketcap_252d_base_v121_signal(assetturnover, marketcap, closeadj):
    s = assetturnover.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(assetturnover) / mean(marketcap) x closeadj
def at_f61_asset_turnover_cumper_marketcap_504d_base_v122_signal(assetturnover, marketcap, closeadj):
    s = assetturnover.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only assetturnover times closeadj
def at_f61_asset_turnover_pos_63d_base_v123_signal(assetturnover, closeadj):
    pos = assetturnover.where(assetturnover > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only assetturnover times closeadj
def at_f61_asset_turnover_pos_252d_base_v124_signal(assetturnover, closeadj):
    pos = assetturnover.where(assetturnover > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only assetturnover times closeadj
def at_f61_asset_turnover_neg_63d_base_v125_signal(assetturnover, closeadj):
    neg = assetturnover.where(assetturnover < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only assetturnover times closeadj
def at_f61_asset_turnover_neg_252d_base_v126_signal(assetturnover, closeadj):
    neg = assetturnover.where(assetturnover < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of assetturnover times closeadj
def at_f61_asset_turnover_hl_21d_base_v127_signal(assetturnover, closeadj):
    result = assetturnover.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of assetturnover times closeadj
def at_f61_asset_turnover_hl_63d_base_v128_signal(assetturnover, closeadj):
    result = assetturnover.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of assetturnover times closeadj
def at_f61_asset_turnover_hl_252d_base_v129_signal(assetturnover, closeadj):
    result = assetturnover.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of assetturnover
def at_f61_asset_turnover_z_63d_base_v130_signal(assetturnover):
    result = _z(assetturnover, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of assetturnover
def at_f61_asset_turnover_z_126d_base_v131_signal(assetturnover):
    result = _z(assetturnover, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of assetturnover
def at_f61_asset_turnover_z_1008d_base_v132_signal(assetturnover):
    result = _z(assetturnover, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of assetturnover times closeadj
def at_f61_asset_turnover_st_lt_252_21d_base_v133_signal(assetturnover, closeadj):
    sm = _mean(assetturnover, 21)
    lm = _mean(assetturnover, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of assetturnover times closeadj
def at_f61_asset_turnover_st_lt_252_63d_base_v134_signal(assetturnover, closeadj):
    sm = _mean(assetturnover, 63)
    lm = _mean(assetturnover, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of assetturnover times closeadj
def at_f61_asset_turnover_st_lt_504_21d_base_v135_signal(assetturnover, closeadj):
    sm = _mean(assetturnover, 21)
    lm = _mean(assetturnover, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of assetturnover times closeadj
def at_f61_asset_turnover_st_lt_504_63d_base_v136_signal(assetturnover, closeadj):
    sm = _mean(assetturnover, 63)
    lm = _mean(assetturnover, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assetturnover/assets times closeadj
def at_f61_asset_turnover_lag_per_assets_21d_base_v137_signal(assetturnover, assets, closeadj):
    r = _asset_turnover_scaled(assetturnover, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assetturnover/assets times closeadj
def at_f61_asset_turnover_lag_per_assets_63d_base_v138_signal(assetturnover, assets, closeadj):
    r = _asset_turnover_scaled(assetturnover, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assetturnover/assets times closeadj
def at_f61_asset_turnover_lag_per_assets_252d_base_v139_signal(assetturnover, assets, closeadj):
    r = _asset_turnover_scaled(assetturnover, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assetturnover/marketcap times closeadj
def at_f61_asset_turnover_lag_per_marketcap_21d_base_v140_signal(assetturnover, marketcap, closeadj):
    r = _asset_turnover_scaled(assetturnover, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assetturnover/marketcap times closeadj
def at_f61_asset_turnover_lag_per_marketcap_63d_base_v141_signal(assetturnover, marketcap, closeadj):
    r = _asset_turnover_scaled(assetturnover, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assetturnover/marketcap times closeadj
def at_f61_asset_turnover_lag_per_marketcap_252d_base_v142_signal(assetturnover, marketcap, closeadj):
    r = _asset_turnover_scaled(assetturnover, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |assetturnover| times closeadj
def at_f61_asset_turnover_abssum_63d_base_v143_signal(assetturnover, closeadj):
    result = assetturnover.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |assetturnover| times closeadj
def at_f61_asset_turnover_abssum_252d_base_v144_signal(assetturnover, closeadj):
    result = assetturnover.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |assetturnover| times closeadj
def at_f61_asset_turnover_abssum_504d_base_v145_signal(assetturnover, closeadj):
    result = assetturnover.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of assetturnover
def at_f61_asset_turnover_acf1_252d_base_v146_signal(assetturnover):
    result = assetturnover.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of assetturnover
def at_f61_asset_turnover_acf1_504d_base_v147_signal(assetturnover):
    result = assetturnover.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of assetturnover
def at_f61_asset_turnover_posinrange_252d_base_v148_signal(assetturnover):
    m = _mean(assetturnover, 252)
    hi = assetturnover.rolling(252, min_periods=max(1, 252//2)).max()
    lo = assetturnover.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of assetturnover
def at_f61_asset_turnover_posinrange_504d_base_v149_signal(assetturnover):
    m = _mean(assetturnover, 504)
    hi = assetturnover.rolling(504, min_periods=max(1, 504//2)).max()
    lo = assetturnover.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of assetturnover times closeadj
def at_f61_asset_turnover_hl_5d_base_v150_signal(assetturnover, closeadj):
    result = assetturnover.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
