"""Family f93 - Accumulation vs distribution  (P_Institutional_SF3) | base 076-150"""
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
def _accumulation_distribution_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _accumulation_distribution_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _accumulation_distribution_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of units/marketcap
def acd_f93_accumulation_distribution_log_per_marketcap_504d_base_v076_signal(units, marketcap):
    s = _accumulation_distribution_scaled(units, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of units/equity
def acd_f93_accumulation_distribution_log_per_equity_252d_base_v077_signal(units, equity):
    s = _accumulation_distribution_scaled(units, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of units/equity
def acd_f93_accumulation_distribution_log_per_equity_504d_base_v078_signal(units, equity):
    s = _accumulation_distribution_scaled(units, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of units times closeadj
def acd_f93_accumulation_distribution_ewm_21d_base_v079_signal(units, closeadj):
    result = units.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of units times closeadj
def acd_f93_accumulation_distribution_ewm_63d_base_v080_signal(units, closeadj):
    result = units.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of units times closeadj
def acd_f93_accumulation_distribution_ewm_252d_base_v081_signal(units, closeadj):
    result = units.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of units times closeadj
def acd_f93_accumulation_distribution_med_63d_base_v082_signal(units, closeadj):
    result = units.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of units times closeadj
def acd_f93_accumulation_distribution_med_252d_base_v083_signal(units, closeadj):
    result = units.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of units times closeadj
def acd_f93_accumulation_distribution_med_504d_base_v084_signal(units, closeadj):
    result = units.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of units
def acd_f93_accumulation_distribution_skew_252d_base_v085_signal(units):
    result = units.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of units
def acd_f93_accumulation_distribution_skew_504d_base_v086_signal(units):
    result = units.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of units
def acd_f93_accumulation_distribution_kurt_252d_base_v087_signal(units):
    result = units.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of units
def acd_f93_accumulation_distribution_kurt_504d_base_v088_signal(units):
    result = units.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of units times closeadj
def acd_f93_accumulation_distribution_rank_252d_base_v089_signal(units, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = units.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of units times closeadj
def acd_f93_accumulation_distribution_rank_504d_base_v090_signal(units, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = units.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of units times closeadj
def acd_f93_accumulation_distribution_rank_1008d_base_v091_signal(units, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = units.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of units from 63d mean times closeadj
def acd_f93_accumulation_distribution_devmean_63d_base_v092_signal(units, closeadj):
    m = _mean(units, 63)
    result = (units - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of units from 252d mean times closeadj
def acd_f93_accumulation_distribution_devmean_252d_base_v093_signal(units, closeadj):
    m = _mean(units, 252)
    result = (units - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of units from 504d mean times closeadj
def acd_f93_accumulation_distribution_devmean_504d_base_v094_signal(units, closeadj):
    m = _mean(units, 504)
    result = (units - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of units times closeadj
def acd_f93_accumulation_distribution_logdiff_21d_base_v095_signal(units, closeadj):
    lr = _accumulation_distribution_log(units)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of units times closeadj
def acd_f93_accumulation_distribution_logdiff_63d_base_v096_signal(units, closeadj):
    lr = _accumulation_distribution_log(units)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of units times closeadj
def acd_f93_accumulation_distribution_logdiff_252d_base_v097_signal(units, closeadj):
    lr = _accumulation_distribution_log(units)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of units times closeadj
def acd_f93_accumulation_distribution_range_63d_base_v098_signal(units, closeadj):
    hi = units.rolling(63, min_periods=max(1, 63//2)).max()
    lo = units.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of units times closeadj
def acd_f93_accumulation_distribution_range_252d_base_v099_signal(units, closeadj):
    hi = units.rolling(252, min_periods=max(1, 252//2)).max()
    lo = units.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of units times closeadj
def acd_f93_accumulation_distribution_range_504d_base_v100_signal(units, closeadj):
    hi = units.rolling(504, min_periods=max(1, 504//2)).max()
    lo = units.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 252d mean times closeadj
def acd_f93_accumulation_distribution_rel_252d_base_v101_signal(units, closeadj):
    m = _mean(units, 252).replace(0, np.nan)
    result = (units / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 504d mean times closeadj
def acd_f93_accumulation_distribution_rel_504d_base_v102_signal(units, closeadj):
    m = _mean(units, 504).replace(0, np.nan)
    result = (units / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 1008d mean times closeadj
def acd_f93_accumulation_distribution_rel_1008d_base_v103_signal(units, closeadj):
    m = _mean(units, 1008).replace(0, np.nan)
    result = (units / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized units/assets 63d mean
def acd_f93_accumulation_distribution_sqnorm_assets_63d_base_v104_signal(units, assets):
    r = _accumulation_distribution_scaled(units, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized units/assets 252d mean
def acd_f93_accumulation_distribution_sqnorm_assets_252d_base_v105_signal(units, assets):
    r = _accumulation_distribution_scaled(units, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized units/marketcap 63d mean
def acd_f93_accumulation_distribution_sqnorm_marketcap_63d_base_v106_signal(units, marketcap):
    r = _accumulation_distribution_scaled(units, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized units/marketcap 252d mean
def acd_f93_accumulation_distribution_sqnorm_marketcap_252d_base_v107_signal(units, marketcap):
    r = _accumulation_distribution_scaled(units, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized units/equity 63d mean
def acd_f93_accumulation_distribution_sqnorm_equity_63d_base_v108_signal(units, equity):
    r = _accumulation_distribution_scaled(units, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized units/equity 252d mean
def acd_f93_accumulation_distribution_sqnorm_equity_252d_base_v109_signal(units, equity):
    r = _accumulation_distribution_scaled(units, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of units times closeadj
def acd_f93_accumulation_distribution_infrat_63d_base_v110_signal(units, closeadj):
    m = _mean(units, 63)
    s = _std(units, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of units times closeadj
def acd_f93_accumulation_distribution_infrat_252d_base_v111_signal(units, closeadj):
    m = _mean(units, 252)
    s = _std(units, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of units times closeadj
def acd_f93_accumulation_distribution_infrat_504d_base_v112_signal(units, closeadj):
    m = _mean(units, 504)
    s = _std(units, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of units
def acd_f93_accumulation_distribution_cv_252d_base_v113_signal(units):
    m = _mean(units, 252).abs().replace(0, np.nan)
    s = _std(units, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of units
def acd_f93_accumulation_distribution_cv_504d_base_v114_signal(units):
    m = _mean(units, 504).abs().replace(0, np.nan)
    s = _std(units, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged units times closeadj
def acd_f93_accumulation_distribution_lag_5d_base_v115_signal(units, closeadj):
    result = units.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged units times closeadj
def acd_f93_accumulation_distribution_lag_21d_base_v116_signal(units, closeadj):
    result = units.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged units times closeadj
def acd_f93_accumulation_distribution_lag_63d_base_v117_signal(units, closeadj):
    result = units.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged units times closeadj
def acd_f93_accumulation_distribution_lag_252d_base_v118_signal(units, closeadj):
    result = units.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(units) / mean(assets) x closeadj
def acd_f93_accumulation_distribution_cumper_assets_252d_base_v119_signal(units, assets, closeadj):
    s = units.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(units) / mean(assets) x closeadj
def acd_f93_accumulation_distribution_cumper_assets_504d_base_v120_signal(units, assets, closeadj):
    s = units.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(units) / mean(marketcap) x closeadj
def acd_f93_accumulation_distribution_cumper_marketcap_252d_base_v121_signal(units, marketcap, closeadj):
    s = units.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(units) / mean(marketcap) x closeadj
def acd_f93_accumulation_distribution_cumper_marketcap_504d_base_v122_signal(units, marketcap, closeadj):
    s = units.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only units times closeadj
def acd_f93_accumulation_distribution_pos_63d_base_v123_signal(units, closeadj):
    pos = units.where(units > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only units times closeadj
def acd_f93_accumulation_distribution_pos_252d_base_v124_signal(units, closeadj):
    pos = units.where(units > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only units times closeadj
def acd_f93_accumulation_distribution_neg_63d_base_v125_signal(units, closeadj):
    neg = units.where(units < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only units times closeadj
def acd_f93_accumulation_distribution_neg_252d_base_v126_signal(units, closeadj):
    neg = units.where(units < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of units times closeadj
def acd_f93_accumulation_distribution_hl_21d_base_v127_signal(units, closeadj):
    result = units.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of units times closeadj
def acd_f93_accumulation_distribution_hl_63d_base_v128_signal(units, closeadj):
    result = units.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of units times closeadj
def acd_f93_accumulation_distribution_hl_252d_base_v129_signal(units, closeadj):
    result = units.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of units
def acd_f93_accumulation_distribution_z_63d_base_v130_signal(units):
    result = _z(units, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of units
def acd_f93_accumulation_distribution_z_126d_base_v131_signal(units):
    result = _z(units, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of units
def acd_f93_accumulation_distribution_z_1008d_base_v132_signal(units):
    result = _z(units, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of units times closeadj
def acd_f93_accumulation_distribution_st_lt_252_21d_base_v133_signal(units, closeadj):
    sm = _mean(units, 21)
    lm = _mean(units, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of units times closeadj
def acd_f93_accumulation_distribution_st_lt_252_63d_base_v134_signal(units, closeadj):
    sm = _mean(units, 63)
    lm = _mean(units, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of units times closeadj
def acd_f93_accumulation_distribution_st_lt_504_21d_base_v135_signal(units, closeadj):
    sm = _mean(units, 21)
    lm = _mean(units, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of units times closeadj
def acd_f93_accumulation_distribution_st_lt_504_63d_base_v136_signal(units, closeadj):
    sm = _mean(units, 63)
    lm = _mean(units, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged units/assets times closeadj
def acd_f93_accumulation_distribution_lag_per_assets_21d_base_v137_signal(units, assets, closeadj):
    r = _accumulation_distribution_scaled(units, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged units/assets times closeadj
def acd_f93_accumulation_distribution_lag_per_assets_63d_base_v138_signal(units, assets, closeadj):
    r = _accumulation_distribution_scaled(units, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged units/assets times closeadj
def acd_f93_accumulation_distribution_lag_per_assets_252d_base_v139_signal(units, assets, closeadj):
    r = _accumulation_distribution_scaled(units, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged units/marketcap times closeadj
def acd_f93_accumulation_distribution_lag_per_marketcap_21d_base_v140_signal(units, marketcap, closeadj):
    r = _accumulation_distribution_scaled(units, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged units/marketcap times closeadj
def acd_f93_accumulation_distribution_lag_per_marketcap_63d_base_v141_signal(units, marketcap, closeadj):
    r = _accumulation_distribution_scaled(units, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged units/marketcap times closeadj
def acd_f93_accumulation_distribution_lag_per_marketcap_252d_base_v142_signal(units, marketcap, closeadj):
    r = _accumulation_distribution_scaled(units, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |units| times closeadj
def acd_f93_accumulation_distribution_abssum_63d_base_v143_signal(units, closeadj):
    result = units.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |units| times closeadj
def acd_f93_accumulation_distribution_abssum_252d_base_v144_signal(units, closeadj):
    result = units.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |units| times closeadj
def acd_f93_accumulation_distribution_abssum_504d_base_v145_signal(units, closeadj):
    result = units.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of units
def acd_f93_accumulation_distribution_acf1_252d_base_v146_signal(units):
    result = units.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of units
def acd_f93_accumulation_distribution_acf1_504d_base_v147_signal(units):
    result = units.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of units
def acd_f93_accumulation_distribution_posinrange_252d_base_v148_signal(units):
    m = _mean(units, 252)
    hi = units.rolling(252, min_periods=max(1, 252//2)).max()
    lo = units.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of units
def acd_f93_accumulation_distribution_posinrange_504d_base_v149_signal(units):
    m = _mean(units, 504)
    hi = units.rolling(504, min_periods=max(1, 504//2)).max()
    lo = units.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of units times closeadj
def acd_f93_accumulation_distribution_hl_5d_base_v150_signal(units, closeadj):
    result = units.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
