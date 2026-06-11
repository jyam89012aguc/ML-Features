"""Family f096 - Holder concentration and turnover (Insiders and Ownership) | Sharadar tables: SF3,SF3A,SF3B | fields: investorname, value, units, calendardate | base 076-150"""
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
def _holder_concentration_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _holder_concentration_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _holder_concentration_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of value/calendardate
def hc_f096_holder_concentration_log_per_calendardate_504d_base_v076_signal(value, calendardate):
    s = _holder_concentration_scaled(value, calendardate)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of value/assets
def hc_f096_holder_concentration_log_per_assets_252d_base_v077_signal(value, assets):
    s = _holder_concentration_scaled(value, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of value/assets
def hc_f096_holder_concentration_log_per_assets_504d_base_v078_signal(value, assets):
    s = _holder_concentration_scaled(value, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of value times closeadj
def hc_f096_holder_concentration_ewm_21d_base_v079_signal(value, closeadj):
    result = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of value times closeadj
def hc_f096_holder_concentration_ewm_63d_base_v080_signal(value, closeadj):
    result = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of value times closeadj
def hc_f096_holder_concentration_ewm_252d_base_v081_signal(value, closeadj):
    result = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of value times closeadj
def hc_f096_holder_concentration_med_63d_base_v082_signal(value, closeadj):
    result = value.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of value times closeadj
def hc_f096_holder_concentration_med_252d_base_v083_signal(value, closeadj):
    result = value.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of value times closeadj
def hc_f096_holder_concentration_med_504d_base_v084_signal(value, closeadj):
    result = value.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of value
def hc_f096_holder_concentration_skew_252d_base_v085_signal(value):
    result = value.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of value
def hc_f096_holder_concentration_skew_504d_base_v086_signal(value):
    result = value.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of value
def hc_f096_holder_concentration_kurt_252d_base_v087_signal(value):
    result = value.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of value
def hc_f096_holder_concentration_kurt_504d_base_v088_signal(value):
    result = value.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of value times closeadj
def hc_f096_holder_concentration_rank_252d_base_v089_signal(value, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = value.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of value times closeadj
def hc_f096_holder_concentration_rank_504d_base_v090_signal(value, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = value.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of value times closeadj
def hc_f096_holder_concentration_rank_1008d_base_v091_signal(value, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = value.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of value from 63d mean times closeadj
def hc_f096_holder_concentration_devmean_63d_base_v092_signal(value, closeadj):
    m = _mean(value, 63)
    result = (value - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of value from 252d mean times closeadj
def hc_f096_holder_concentration_devmean_252d_base_v093_signal(value, closeadj):
    m = _mean(value, 252)
    result = (value - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of value from 504d mean times closeadj
def hc_f096_holder_concentration_devmean_504d_base_v094_signal(value, closeadj):
    m = _mean(value, 504)
    result = (value - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of value times closeadj
def hc_f096_holder_concentration_logdiff_21d_base_v095_signal(value, closeadj):
    lr = _holder_concentration_log(value)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of value times closeadj
def hc_f096_holder_concentration_logdiff_63d_base_v096_signal(value, closeadj):
    lr = _holder_concentration_log(value)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of value times closeadj
def hc_f096_holder_concentration_logdiff_252d_base_v097_signal(value, closeadj):
    lr = _holder_concentration_log(value)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of value times closeadj
def hc_f096_holder_concentration_range_63d_base_v098_signal(value, closeadj):
    hi = value.rolling(63, min_periods=max(1, 63//2)).max()
    lo = value.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of value times closeadj
def hc_f096_holder_concentration_range_252d_base_v099_signal(value, closeadj):
    hi = value.rolling(252, min_periods=max(1, 252//2)).max()
    lo = value.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of value times closeadj
def hc_f096_holder_concentration_range_504d_base_v100_signal(value, closeadj):
    hi = value.rolling(504, min_periods=max(1, 504//2)).max()
    lo = value.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 252d mean times closeadj
def hc_f096_holder_concentration_rel_252d_base_v101_signal(value, closeadj):
    m = _mean(value, 252).replace(0, np.nan)
    result = (value / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 504d mean times closeadj
def hc_f096_holder_concentration_rel_504d_base_v102_signal(value, closeadj):
    m = _mean(value, 504).replace(0, np.nan)
    result = (value / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 1008d mean times closeadj
def hc_f096_holder_concentration_rel_1008d_base_v103_signal(value, closeadj):
    m = _mean(value, 1008).replace(0, np.nan)
    result = (value / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/units 63d mean
def hc_f096_holder_concentration_sqnorm_units_63d_base_v104_signal(value, units):
    r = _holder_concentration_scaled(value, units)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/units 252d mean
def hc_f096_holder_concentration_sqnorm_units_252d_base_v105_signal(value, units):
    r = _holder_concentration_scaled(value, units)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/calendardate 63d mean
def hc_f096_holder_concentration_sqnorm_calendardate_63d_base_v106_signal(value, calendardate):
    r = _holder_concentration_scaled(value, calendardate)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/calendardate 252d mean
def hc_f096_holder_concentration_sqnorm_calendardate_252d_base_v107_signal(value, calendardate):
    r = _holder_concentration_scaled(value, calendardate)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/assets 63d mean
def hc_f096_holder_concentration_sqnorm_assets_63d_base_v108_signal(value, assets):
    r = _holder_concentration_scaled(value, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/assets 252d mean
def hc_f096_holder_concentration_sqnorm_assets_252d_base_v109_signal(value, assets):
    r = _holder_concentration_scaled(value, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of value times closeadj
def hc_f096_holder_concentration_infrat_63d_base_v110_signal(value, closeadj):
    m = _mean(value, 63)
    s = _std(value, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of value times closeadj
def hc_f096_holder_concentration_infrat_252d_base_v111_signal(value, closeadj):
    m = _mean(value, 252)
    s = _std(value, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of value times closeadj
def hc_f096_holder_concentration_infrat_504d_base_v112_signal(value, closeadj):
    m = _mean(value, 504)
    s = _std(value, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of value
def hc_f096_holder_concentration_cv_252d_base_v113_signal(value):
    m = _mean(value, 252).abs().replace(0, np.nan)
    s = _std(value, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of value
def hc_f096_holder_concentration_cv_504d_base_v114_signal(value):
    m = _mean(value, 504).abs().replace(0, np.nan)
    s = _std(value, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged value times closeadj
def hc_f096_holder_concentration_lag_5d_base_v115_signal(value, closeadj):
    result = value.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged value times closeadj
def hc_f096_holder_concentration_lag_21d_base_v116_signal(value, closeadj):
    result = value.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged value times closeadj
def hc_f096_holder_concentration_lag_63d_base_v117_signal(value, closeadj):
    result = value.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged value times closeadj
def hc_f096_holder_concentration_lag_252d_base_v118_signal(value, closeadj):
    result = value.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(value) / mean(units) x closeadj
def hc_f096_holder_concentration_cumper_units_252d_base_v119_signal(value, units, closeadj):
    s = value.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(units, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(value) / mean(units) x closeadj
def hc_f096_holder_concentration_cumper_units_504d_base_v120_signal(value, units, closeadj):
    s = value.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(units, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(value) / mean(calendardate) x closeadj
def hc_f096_holder_concentration_cumper_calendardate_252d_base_v121_signal(value, calendardate, closeadj):
    s = value.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(calendardate, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(value) / mean(calendardate) x closeadj
def hc_f096_holder_concentration_cumper_calendardate_504d_base_v122_signal(value, calendardate, closeadj):
    s = value.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(calendardate, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only value times closeadj
def hc_f096_holder_concentration_pos_63d_base_v123_signal(value, closeadj):
    pos = value.where(value > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only value times closeadj
def hc_f096_holder_concentration_pos_252d_base_v124_signal(value, closeadj):
    pos = value.where(value > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only value times closeadj
def hc_f096_holder_concentration_neg_63d_base_v125_signal(value, closeadj):
    neg = value.where(value < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only value times closeadj
def hc_f096_holder_concentration_neg_252d_base_v126_signal(value, closeadj):
    neg = value.where(value < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of value times closeadj
def hc_f096_holder_concentration_hl_21d_base_v127_signal(value, closeadj):
    result = value.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of value times closeadj
def hc_f096_holder_concentration_hl_63d_base_v128_signal(value, closeadj):
    result = value.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of value times closeadj
def hc_f096_holder_concentration_hl_252d_base_v129_signal(value, closeadj):
    result = value.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of value
def hc_f096_holder_concentration_z_63d_base_v130_signal(value):
    result = _z(value, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of value
def hc_f096_holder_concentration_z_126d_base_v131_signal(value):
    result = _z(value, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of value
def hc_f096_holder_concentration_z_1008d_base_v132_signal(value):
    result = _z(value, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of value times closeadj
def hc_f096_holder_concentration_st_lt_252_21d_base_v133_signal(value, closeadj):
    sm = _mean(value, 21)
    lm = _mean(value, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of value times closeadj
def hc_f096_holder_concentration_st_lt_252_63d_base_v134_signal(value, closeadj):
    sm = _mean(value, 63)
    lm = _mean(value, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of value times closeadj
def hc_f096_holder_concentration_st_lt_504_21d_base_v135_signal(value, closeadj):
    sm = _mean(value, 21)
    lm = _mean(value, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of value times closeadj
def hc_f096_holder_concentration_st_lt_504_63d_base_v136_signal(value, closeadj):
    sm = _mean(value, 63)
    lm = _mean(value, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged value/units times closeadj
def hc_f096_holder_concentration_lag_per_units_21d_base_v137_signal(value, units, closeadj):
    r = _holder_concentration_scaled(value, units)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged value/units times closeadj
def hc_f096_holder_concentration_lag_per_units_63d_base_v138_signal(value, units, closeadj):
    r = _holder_concentration_scaled(value, units)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged value/units times closeadj
def hc_f096_holder_concentration_lag_per_units_252d_base_v139_signal(value, units, closeadj):
    r = _holder_concentration_scaled(value, units)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged value/calendardate times closeadj
def hc_f096_holder_concentration_lag_per_calendardate_21d_base_v140_signal(value, calendardate, closeadj):
    r = _holder_concentration_scaled(value, calendardate)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged value/calendardate times closeadj
def hc_f096_holder_concentration_lag_per_calendardate_63d_base_v141_signal(value, calendardate, closeadj):
    r = _holder_concentration_scaled(value, calendardate)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged value/calendardate times closeadj
def hc_f096_holder_concentration_lag_per_calendardate_252d_base_v142_signal(value, calendardate, closeadj):
    r = _holder_concentration_scaled(value, calendardate)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |value| times closeadj
def hc_f096_holder_concentration_abssum_63d_base_v143_signal(value, closeadj):
    result = value.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |value| times closeadj
def hc_f096_holder_concentration_abssum_252d_base_v144_signal(value, closeadj):
    result = value.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |value| times closeadj
def hc_f096_holder_concentration_abssum_504d_base_v145_signal(value, closeadj):
    result = value.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of value
def hc_f096_holder_concentration_acf1_252d_base_v146_signal(value):
    result = value.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of value
def hc_f096_holder_concentration_acf1_504d_base_v147_signal(value):
    result = value.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of value
def hc_f096_holder_concentration_posinrange_252d_base_v148_signal(value):
    m = _mean(value, 252)
    hi = value.rolling(252, min_periods=max(1, 252//2)).max()
    lo = value.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of value
def hc_f096_holder_concentration_posinrange_504d_base_v149_signal(value):
    m = _mean(value, 504)
    hi = value.rolling(504, min_periods=max(1, 504//2)).max()
    lo = value.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of value times closeadj
def hc_f096_holder_concentration_hl_5d_base_v150_signal(value, closeadj):
    result = value.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
