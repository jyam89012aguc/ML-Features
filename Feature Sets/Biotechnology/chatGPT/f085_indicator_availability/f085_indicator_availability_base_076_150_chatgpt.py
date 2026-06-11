"""Family f085 - Field availability and schema coverage (Security Master and Universe) | Sharadar tables: INDICATORS | fields: table, indicator, title, description | base 076-150"""
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
def _indicator_availability_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _indicator_availability_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _indicator_availability_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of field_coverage/assets
def ia_f085_indicator_availability_log_per_assets_504d_base_v076_signal(field_coverage, assets):
    s = _indicator_availability_scaled(field_coverage, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of field_coverage/marketcap
def ia_f085_indicator_availability_log_per_marketcap_252d_base_v077_signal(field_coverage, marketcap):
    s = _indicator_availability_scaled(field_coverage, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of field_coverage/marketcap
def ia_f085_indicator_availability_log_per_marketcap_504d_base_v078_signal(field_coverage, marketcap):
    s = _indicator_availability_scaled(field_coverage, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of field_coverage times closeadj
def ia_f085_indicator_availability_ewm_21d_base_v079_signal(field_coverage, closeadj):
    result = field_coverage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of field_coverage times closeadj
def ia_f085_indicator_availability_ewm_63d_base_v080_signal(field_coverage, closeadj):
    result = field_coverage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of field_coverage times closeadj
def ia_f085_indicator_availability_ewm_252d_base_v081_signal(field_coverage, closeadj):
    result = field_coverage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of field_coverage times closeadj
def ia_f085_indicator_availability_med_63d_base_v082_signal(field_coverage, closeadj):
    result = field_coverage.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of field_coverage times closeadj
def ia_f085_indicator_availability_med_252d_base_v083_signal(field_coverage, closeadj):
    result = field_coverage.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of field_coverage times closeadj
def ia_f085_indicator_availability_med_504d_base_v084_signal(field_coverage, closeadj):
    result = field_coverage.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of field_coverage
def ia_f085_indicator_availability_skew_252d_base_v085_signal(field_coverage):
    result = field_coverage.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of field_coverage
def ia_f085_indicator_availability_skew_504d_base_v086_signal(field_coverage):
    result = field_coverage.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of field_coverage
def ia_f085_indicator_availability_kurt_252d_base_v087_signal(field_coverage):
    result = field_coverage.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of field_coverage
def ia_f085_indicator_availability_kurt_504d_base_v088_signal(field_coverage):
    result = field_coverage.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of field_coverage times closeadj
def ia_f085_indicator_availability_rank_252d_base_v089_signal(field_coverage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = field_coverage.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of field_coverage times closeadj
def ia_f085_indicator_availability_rank_504d_base_v090_signal(field_coverage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = field_coverage.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of field_coverage times closeadj
def ia_f085_indicator_availability_rank_1008d_base_v091_signal(field_coverage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = field_coverage.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of field_coverage from 63d mean times closeadj
def ia_f085_indicator_availability_devmean_63d_base_v092_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 63)
    result = (field_coverage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of field_coverage from 252d mean times closeadj
def ia_f085_indicator_availability_devmean_252d_base_v093_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 252)
    result = (field_coverage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of field_coverage from 504d mean times closeadj
def ia_f085_indicator_availability_devmean_504d_base_v094_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 504)
    result = (field_coverage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of field_coverage times closeadj
def ia_f085_indicator_availability_logdiff_21d_base_v095_signal(field_coverage, closeadj):
    lr = _indicator_availability_log(field_coverage)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of field_coverage times closeadj
def ia_f085_indicator_availability_logdiff_63d_base_v096_signal(field_coverage, closeadj):
    lr = _indicator_availability_log(field_coverage)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of field_coverage times closeadj
def ia_f085_indicator_availability_logdiff_252d_base_v097_signal(field_coverage, closeadj):
    lr = _indicator_availability_log(field_coverage)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of field_coverage times closeadj
def ia_f085_indicator_availability_range_63d_base_v098_signal(field_coverage, closeadj):
    hi = field_coverage.rolling(63, min_periods=max(1, 63//2)).max()
    lo = field_coverage.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of field_coverage times closeadj
def ia_f085_indicator_availability_range_252d_base_v099_signal(field_coverage, closeadj):
    hi = field_coverage.rolling(252, min_periods=max(1, 252//2)).max()
    lo = field_coverage.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of field_coverage times closeadj
def ia_f085_indicator_availability_range_504d_base_v100_signal(field_coverage, closeadj):
    hi = field_coverage.rolling(504, min_periods=max(1, 504//2)).max()
    lo = field_coverage.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 252d mean times closeadj
def ia_f085_indicator_availability_rel_252d_base_v101_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 252).replace(0, np.nan)
    result = (field_coverage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 504d mean times closeadj
def ia_f085_indicator_availability_rel_504d_base_v102_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 504).replace(0, np.nan)
    result = (field_coverage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 1008d mean times closeadj
def ia_f085_indicator_availability_rel_1008d_base_v103_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 1008).replace(0, np.nan)
    result = (field_coverage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized field_coverage/indicator 63d mean
def ia_f085_indicator_availability_sqnorm_indicator_63d_base_v104_signal(field_coverage, indicator):
    r = _indicator_availability_scaled(field_coverage, indicator)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized field_coverage/indicator 252d mean
def ia_f085_indicator_availability_sqnorm_indicator_252d_base_v105_signal(field_coverage, indicator):
    r = _indicator_availability_scaled(field_coverage, indicator)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized field_coverage/assets 63d mean
def ia_f085_indicator_availability_sqnorm_assets_63d_base_v106_signal(field_coverage, assets):
    r = _indicator_availability_scaled(field_coverage, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized field_coverage/assets 252d mean
def ia_f085_indicator_availability_sqnorm_assets_252d_base_v107_signal(field_coverage, assets):
    r = _indicator_availability_scaled(field_coverage, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized field_coverage/marketcap 63d mean
def ia_f085_indicator_availability_sqnorm_marketcap_63d_base_v108_signal(field_coverage, marketcap):
    r = _indicator_availability_scaled(field_coverage, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized field_coverage/marketcap 252d mean
def ia_f085_indicator_availability_sqnorm_marketcap_252d_base_v109_signal(field_coverage, marketcap):
    r = _indicator_availability_scaled(field_coverage, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of field_coverage times closeadj
def ia_f085_indicator_availability_infrat_63d_base_v110_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 63)
    s = _std(field_coverage, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of field_coverage times closeadj
def ia_f085_indicator_availability_infrat_252d_base_v111_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 252)
    s = _std(field_coverage, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of field_coverage times closeadj
def ia_f085_indicator_availability_infrat_504d_base_v112_signal(field_coverage, closeadj):
    m = _mean(field_coverage, 504)
    s = _std(field_coverage, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of field_coverage
def ia_f085_indicator_availability_cv_252d_base_v113_signal(field_coverage):
    m = _mean(field_coverage, 252).abs().replace(0, np.nan)
    s = _std(field_coverage, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of field_coverage
def ia_f085_indicator_availability_cv_504d_base_v114_signal(field_coverage):
    m = _mean(field_coverage, 504).abs().replace(0, np.nan)
    s = _std(field_coverage, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged field_coverage times closeadj
def ia_f085_indicator_availability_lag_5d_base_v115_signal(field_coverage, closeadj):
    result = field_coverage.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged field_coverage times closeadj
def ia_f085_indicator_availability_lag_21d_base_v116_signal(field_coverage, closeadj):
    result = field_coverage.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged field_coverage times closeadj
def ia_f085_indicator_availability_lag_63d_base_v117_signal(field_coverage, closeadj):
    result = field_coverage.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged field_coverage times closeadj
def ia_f085_indicator_availability_lag_252d_base_v118_signal(field_coverage, closeadj):
    result = field_coverage.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(field_coverage) / mean(indicator) x closeadj
def ia_f085_indicator_availability_cumper_indicator_252d_base_v119_signal(field_coverage, indicator, closeadj):
    s = field_coverage.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(indicator, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(field_coverage) / mean(indicator) x closeadj
def ia_f085_indicator_availability_cumper_indicator_504d_base_v120_signal(field_coverage, indicator, closeadj):
    s = field_coverage.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(indicator, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(field_coverage) / mean(assets) x closeadj
def ia_f085_indicator_availability_cumper_assets_252d_base_v121_signal(field_coverage, assets, closeadj):
    s = field_coverage.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(field_coverage) / mean(assets) x closeadj
def ia_f085_indicator_availability_cumper_assets_504d_base_v122_signal(field_coverage, assets, closeadj):
    s = field_coverage.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only field_coverage times closeadj
def ia_f085_indicator_availability_pos_63d_base_v123_signal(field_coverage, closeadj):
    pos = field_coverage.where(field_coverage > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only field_coverage times closeadj
def ia_f085_indicator_availability_pos_252d_base_v124_signal(field_coverage, closeadj):
    pos = field_coverage.where(field_coverage > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only field_coverage times closeadj
def ia_f085_indicator_availability_neg_63d_base_v125_signal(field_coverage, closeadj):
    neg = field_coverage.where(field_coverage < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only field_coverage times closeadj
def ia_f085_indicator_availability_neg_252d_base_v126_signal(field_coverage, closeadj):
    neg = field_coverage.where(field_coverage < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of field_coverage times closeadj
def ia_f085_indicator_availability_hl_21d_base_v127_signal(field_coverage, closeadj):
    result = field_coverage.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of field_coverage times closeadj
def ia_f085_indicator_availability_hl_63d_base_v128_signal(field_coverage, closeadj):
    result = field_coverage.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of field_coverage times closeadj
def ia_f085_indicator_availability_hl_252d_base_v129_signal(field_coverage, closeadj):
    result = field_coverage.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of field_coverage
def ia_f085_indicator_availability_z_63d_base_v130_signal(field_coverage):
    result = _z(field_coverage, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of field_coverage
def ia_f085_indicator_availability_z_126d_base_v131_signal(field_coverage):
    result = _z(field_coverage, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of field_coverage
def ia_f085_indicator_availability_z_1008d_base_v132_signal(field_coverage):
    result = _z(field_coverage, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of field_coverage times closeadj
def ia_f085_indicator_availability_st_lt_252_21d_base_v133_signal(field_coverage, closeadj):
    sm = _mean(field_coverage, 21)
    lm = _mean(field_coverage, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of field_coverage times closeadj
def ia_f085_indicator_availability_st_lt_252_63d_base_v134_signal(field_coverage, closeadj):
    sm = _mean(field_coverage, 63)
    lm = _mean(field_coverage, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of field_coverage times closeadj
def ia_f085_indicator_availability_st_lt_504_21d_base_v135_signal(field_coverage, closeadj):
    sm = _mean(field_coverage, 21)
    lm = _mean(field_coverage, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of field_coverage times closeadj
def ia_f085_indicator_availability_st_lt_504_63d_base_v136_signal(field_coverage, closeadj):
    sm = _mean(field_coverage, 63)
    lm = _mean(field_coverage, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged field_coverage/indicator times closeadj
def ia_f085_indicator_availability_lag_per_indicator_21d_base_v137_signal(field_coverage, indicator, closeadj):
    r = _indicator_availability_scaled(field_coverage, indicator)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged field_coverage/indicator times closeadj
def ia_f085_indicator_availability_lag_per_indicator_63d_base_v138_signal(field_coverage, indicator, closeadj):
    r = _indicator_availability_scaled(field_coverage, indicator)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged field_coverage/indicator times closeadj
def ia_f085_indicator_availability_lag_per_indicator_252d_base_v139_signal(field_coverage, indicator, closeadj):
    r = _indicator_availability_scaled(field_coverage, indicator)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged field_coverage/assets times closeadj
def ia_f085_indicator_availability_lag_per_assets_21d_base_v140_signal(field_coverage, assets, closeadj):
    r = _indicator_availability_scaled(field_coverage, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged field_coverage/assets times closeadj
def ia_f085_indicator_availability_lag_per_assets_63d_base_v141_signal(field_coverage, assets, closeadj):
    r = _indicator_availability_scaled(field_coverage, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged field_coverage/assets times closeadj
def ia_f085_indicator_availability_lag_per_assets_252d_base_v142_signal(field_coverage, assets, closeadj):
    r = _indicator_availability_scaled(field_coverage, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |field_coverage| times closeadj
def ia_f085_indicator_availability_abssum_63d_base_v143_signal(field_coverage, closeadj):
    result = field_coverage.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |field_coverage| times closeadj
def ia_f085_indicator_availability_abssum_252d_base_v144_signal(field_coverage, closeadj):
    result = field_coverage.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |field_coverage| times closeadj
def ia_f085_indicator_availability_abssum_504d_base_v145_signal(field_coverage, closeadj):
    result = field_coverage.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of field_coverage
def ia_f085_indicator_availability_acf1_252d_base_v146_signal(field_coverage):
    result = field_coverage.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of field_coverage
def ia_f085_indicator_availability_acf1_504d_base_v147_signal(field_coverage):
    result = field_coverage.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of field_coverage
def ia_f085_indicator_availability_posinrange_252d_base_v148_signal(field_coverage):
    m = _mean(field_coverage, 252)
    hi = field_coverage.rolling(252, min_periods=max(1, 252//2)).max()
    lo = field_coverage.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of field_coverage
def ia_f085_indicator_availability_posinrange_504d_base_v149_signal(field_coverage):
    m = _mean(field_coverage, 504)
    hi = field_coverage.rolling(504, min_periods=max(1, 504//2)).max()
    lo = field_coverage.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of field_coverage times closeadj
def ia_f085_indicator_availability_hl_5d_base_v150_signal(field_coverage, closeadj):
    result = field_coverage.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
