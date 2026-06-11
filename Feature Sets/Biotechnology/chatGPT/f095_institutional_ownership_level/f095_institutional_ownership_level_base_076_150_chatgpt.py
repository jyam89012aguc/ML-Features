"""Family f095 - Institutional ownership level (Insiders and Ownership) | Sharadar tables: SF3 | fields: calendardate, investorname, value, units, price | base 076-150"""
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
def _institutional_ownership_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _institutional_ownership_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _institutional_ownership_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of calendardate/units
def iol_f095_institutional_ownership_level_log_per_units_504d_base_v076_signal(calendardate, units):
    s = _institutional_ownership_level_scaled(calendardate, units)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of calendardate/price
def iol_f095_institutional_ownership_level_log_per_price_252d_base_v077_signal(calendardate, price):
    s = _institutional_ownership_level_scaled(calendardate, price)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of calendardate/price
def iol_f095_institutional_ownership_level_log_per_price_504d_base_v078_signal(calendardate, price):
    s = _institutional_ownership_level_scaled(calendardate, price)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of calendardate times closeadj
def iol_f095_institutional_ownership_level_ewm_21d_base_v079_signal(calendardate, closeadj):
    result = calendardate.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of calendardate times closeadj
def iol_f095_institutional_ownership_level_ewm_63d_base_v080_signal(calendardate, closeadj):
    result = calendardate.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of calendardate times closeadj
def iol_f095_institutional_ownership_level_ewm_252d_base_v081_signal(calendardate, closeadj):
    result = calendardate.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of calendardate times closeadj
def iol_f095_institutional_ownership_level_med_63d_base_v082_signal(calendardate, closeadj):
    result = calendardate.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of calendardate times closeadj
def iol_f095_institutional_ownership_level_med_252d_base_v083_signal(calendardate, closeadj):
    result = calendardate.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of calendardate times closeadj
def iol_f095_institutional_ownership_level_med_504d_base_v084_signal(calendardate, closeadj):
    result = calendardate.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of calendardate
def iol_f095_institutional_ownership_level_skew_252d_base_v085_signal(calendardate):
    result = calendardate.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of calendardate
def iol_f095_institutional_ownership_level_skew_504d_base_v086_signal(calendardate):
    result = calendardate.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of calendardate
def iol_f095_institutional_ownership_level_kurt_252d_base_v087_signal(calendardate):
    result = calendardate.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of calendardate
def iol_f095_institutional_ownership_level_kurt_504d_base_v088_signal(calendardate):
    result = calendardate.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of calendardate times closeadj
def iol_f095_institutional_ownership_level_rank_252d_base_v089_signal(calendardate, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = calendardate.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of calendardate times closeadj
def iol_f095_institutional_ownership_level_rank_504d_base_v090_signal(calendardate, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = calendardate.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of calendardate times closeadj
def iol_f095_institutional_ownership_level_rank_1008d_base_v091_signal(calendardate, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = calendardate.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of calendardate from 63d mean times closeadj
def iol_f095_institutional_ownership_level_devmean_63d_base_v092_signal(calendardate, closeadj):
    m = _mean(calendardate, 63)
    result = (calendardate - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of calendardate from 252d mean times closeadj
def iol_f095_institutional_ownership_level_devmean_252d_base_v093_signal(calendardate, closeadj):
    m = _mean(calendardate, 252)
    result = (calendardate - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of calendardate from 504d mean times closeadj
def iol_f095_institutional_ownership_level_devmean_504d_base_v094_signal(calendardate, closeadj):
    m = _mean(calendardate, 504)
    result = (calendardate - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of calendardate times closeadj
def iol_f095_institutional_ownership_level_logdiff_21d_base_v095_signal(calendardate, closeadj):
    lr = _institutional_ownership_level_log(calendardate)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of calendardate times closeadj
def iol_f095_institutional_ownership_level_logdiff_63d_base_v096_signal(calendardate, closeadj):
    lr = _institutional_ownership_level_log(calendardate)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of calendardate times closeadj
def iol_f095_institutional_ownership_level_logdiff_252d_base_v097_signal(calendardate, closeadj):
    lr = _institutional_ownership_level_log(calendardate)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of calendardate times closeadj
def iol_f095_institutional_ownership_level_range_63d_base_v098_signal(calendardate, closeadj):
    hi = calendardate.rolling(63, min_periods=max(1, 63//2)).max()
    lo = calendardate.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of calendardate times closeadj
def iol_f095_institutional_ownership_level_range_252d_base_v099_signal(calendardate, closeadj):
    hi = calendardate.rolling(252, min_periods=max(1, 252//2)).max()
    lo = calendardate.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of calendardate times closeadj
def iol_f095_institutional_ownership_level_range_504d_base_v100_signal(calendardate, closeadj):
    hi = calendardate.rolling(504, min_periods=max(1, 504//2)).max()
    lo = calendardate.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 252d mean times closeadj
def iol_f095_institutional_ownership_level_rel_252d_base_v101_signal(calendardate, closeadj):
    m = _mean(calendardate, 252).replace(0, np.nan)
    result = (calendardate / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 504d mean times closeadj
def iol_f095_institutional_ownership_level_rel_504d_base_v102_signal(calendardate, closeadj):
    m = _mean(calendardate, 504).replace(0, np.nan)
    result = (calendardate / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 1008d mean times closeadj
def iol_f095_institutional_ownership_level_rel_1008d_base_v103_signal(calendardate, closeadj):
    m = _mean(calendardate, 1008).replace(0, np.nan)
    result = (calendardate / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized calendardate/value 63d mean
def iol_f095_institutional_ownership_level_sqnorm_value_63d_base_v104_signal(calendardate, value):
    r = _institutional_ownership_level_scaled(calendardate, value)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized calendardate/value 252d mean
def iol_f095_institutional_ownership_level_sqnorm_value_252d_base_v105_signal(calendardate, value):
    r = _institutional_ownership_level_scaled(calendardate, value)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized calendardate/units 63d mean
def iol_f095_institutional_ownership_level_sqnorm_units_63d_base_v106_signal(calendardate, units):
    r = _institutional_ownership_level_scaled(calendardate, units)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized calendardate/units 252d mean
def iol_f095_institutional_ownership_level_sqnorm_units_252d_base_v107_signal(calendardate, units):
    r = _institutional_ownership_level_scaled(calendardate, units)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized calendardate/price 63d mean
def iol_f095_institutional_ownership_level_sqnorm_price_63d_base_v108_signal(calendardate, price):
    r = _institutional_ownership_level_scaled(calendardate, price)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized calendardate/price 252d mean
def iol_f095_institutional_ownership_level_sqnorm_price_252d_base_v109_signal(calendardate, price):
    r = _institutional_ownership_level_scaled(calendardate, price)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of calendardate times closeadj
def iol_f095_institutional_ownership_level_infrat_63d_base_v110_signal(calendardate, closeadj):
    m = _mean(calendardate, 63)
    s = _std(calendardate, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of calendardate times closeadj
def iol_f095_institutional_ownership_level_infrat_252d_base_v111_signal(calendardate, closeadj):
    m = _mean(calendardate, 252)
    s = _std(calendardate, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of calendardate times closeadj
def iol_f095_institutional_ownership_level_infrat_504d_base_v112_signal(calendardate, closeadj):
    m = _mean(calendardate, 504)
    s = _std(calendardate, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of calendardate
def iol_f095_institutional_ownership_level_cv_252d_base_v113_signal(calendardate):
    m = _mean(calendardate, 252).abs().replace(0, np.nan)
    s = _std(calendardate, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of calendardate
def iol_f095_institutional_ownership_level_cv_504d_base_v114_signal(calendardate):
    m = _mean(calendardate, 504).abs().replace(0, np.nan)
    s = _std(calendardate, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged calendardate times closeadj
def iol_f095_institutional_ownership_level_lag_5d_base_v115_signal(calendardate, closeadj):
    result = calendardate.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged calendardate times closeadj
def iol_f095_institutional_ownership_level_lag_21d_base_v116_signal(calendardate, closeadj):
    result = calendardate.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged calendardate times closeadj
def iol_f095_institutional_ownership_level_lag_63d_base_v117_signal(calendardate, closeadj):
    result = calendardate.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged calendardate times closeadj
def iol_f095_institutional_ownership_level_lag_252d_base_v118_signal(calendardate, closeadj):
    result = calendardate.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(calendardate) / mean(value) x closeadj
def iol_f095_institutional_ownership_level_cumper_value_252d_base_v119_signal(calendardate, value, closeadj):
    s = calendardate.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(value, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(calendardate) / mean(value) x closeadj
def iol_f095_institutional_ownership_level_cumper_value_504d_base_v120_signal(calendardate, value, closeadj):
    s = calendardate.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(value, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(calendardate) / mean(units) x closeadj
def iol_f095_institutional_ownership_level_cumper_units_252d_base_v121_signal(calendardate, units, closeadj):
    s = calendardate.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(units, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(calendardate) / mean(units) x closeadj
def iol_f095_institutional_ownership_level_cumper_units_504d_base_v122_signal(calendardate, units, closeadj):
    s = calendardate.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(units, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only calendardate times closeadj
def iol_f095_institutional_ownership_level_pos_63d_base_v123_signal(calendardate, closeadj):
    pos = calendardate.where(calendardate > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only calendardate times closeadj
def iol_f095_institutional_ownership_level_pos_252d_base_v124_signal(calendardate, closeadj):
    pos = calendardate.where(calendardate > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only calendardate times closeadj
def iol_f095_institutional_ownership_level_neg_63d_base_v125_signal(calendardate, closeadj):
    neg = calendardate.where(calendardate < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only calendardate times closeadj
def iol_f095_institutional_ownership_level_neg_252d_base_v126_signal(calendardate, closeadj):
    neg = calendardate.where(calendardate < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of calendardate times closeadj
def iol_f095_institutional_ownership_level_hl_21d_base_v127_signal(calendardate, closeadj):
    result = calendardate.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of calendardate times closeadj
def iol_f095_institutional_ownership_level_hl_63d_base_v128_signal(calendardate, closeadj):
    result = calendardate.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of calendardate times closeadj
def iol_f095_institutional_ownership_level_hl_252d_base_v129_signal(calendardate, closeadj):
    result = calendardate.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of calendardate
def iol_f095_institutional_ownership_level_z_63d_base_v130_signal(calendardate):
    result = _z(calendardate, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of calendardate
def iol_f095_institutional_ownership_level_z_126d_base_v131_signal(calendardate):
    result = _z(calendardate, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of calendardate
def iol_f095_institutional_ownership_level_z_1008d_base_v132_signal(calendardate):
    result = _z(calendardate, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of calendardate times closeadj
def iol_f095_institutional_ownership_level_st_lt_252_21d_base_v133_signal(calendardate, closeadj):
    sm = _mean(calendardate, 21)
    lm = _mean(calendardate, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of calendardate times closeadj
def iol_f095_institutional_ownership_level_st_lt_252_63d_base_v134_signal(calendardate, closeadj):
    sm = _mean(calendardate, 63)
    lm = _mean(calendardate, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of calendardate times closeadj
def iol_f095_institutional_ownership_level_st_lt_504_21d_base_v135_signal(calendardate, closeadj):
    sm = _mean(calendardate, 21)
    lm = _mean(calendardate, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of calendardate times closeadj
def iol_f095_institutional_ownership_level_st_lt_504_63d_base_v136_signal(calendardate, closeadj):
    sm = _mean(calendardate, 63)
    lm = _mean(calendardate, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged calendardate/value times closeadj
def iol_f095_institutional_ownership_level_lag_per_value_21d_base_v137_signal(calendardate, value, closeadj):
    r = _institutional_ownership_level_scaled(calendardate, value)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged calendardate/value times closeadj
def iol_f095_institutional_ownership_level_lag_per_value_63d_base_v138_signal(calendardate, value, closeadj):
    r = _institutional_ownership_level_scaled(calendardate, value)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged calendardate/value times closeadj
def iol_f095_institutional_ownership_level_lag_per_value_252d_base_v139_signal(calendardate, value, closeadj):
    r = _institutional_ownership_level_scaled(calendardate, value)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged calendardate/units times closeadj
def iol_f095_institutional_ownership_level_lag_per_units_21d_base_v140_signal(calendardate, units, closeadj):
    r = _institutional_ownership_level_scaled(calendardate, units)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged calendardate/units times closeadj
def iol_f095_institutional_ownership_level_lag_per_units_63d_base_v141_signal(calendardate, units, closeadj):
    r = _institutional_ownership_level_scaled(calendardate, units)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged calendardate/units times closeadj
def iol_f095_institutional_ownership_level_lag_per_units_252d_base_v142_signal(calendardate, units, closeadj):
    r = _institutional_ownership_level_scaled(calendardate, units)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |calendardate| times closeadj
def iol_f095_institutional_ownership_level_abssum_63d_base_v143_signal(calendardate, closeadj):
    result = calendardate.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |calendardate| times closeadj
def iol_f095_institutional_ownership_level_abssum_252d_base_v144_signal(calendardate, closeadj):
    result = calendardate.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |calendardate| times closeadj
def iol_f095_institutional_ownership_level_abssum_504d_base_v145_signal(calendardate, closeadj):
    result = calendardate.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of calendardate
def iol_f095_institutional_ownership_level_acf1_252d_base_v146_signal(calendardate):
    result = calendardate.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of calendardate
def iol_f095_institutional_ownership_level_acf1_504d_base_v147_signal(calendardate):
    result = calendardate.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of calendardate
def iol_f095_institutional_ownership_level_posinrange_252d_base_v148_signal(calendardate):
    m = _mean(calendardate, 252)
    hi = calendardate.rolling(252, min_periods=max(1, 252//2)).max()
    lo = calendardate.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of calendardate
def iol_f095_institutional_ownership_level_posinrange_504d_base_v149_signal(calendardate):
    m = _mean(calendardate, 504)
    hi = calendardate.rolling(504, min_periods=max(1, 504//2)).max()
    lo = calendardate.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of calendardate times closeadj
def iol_f095_institutional_ownership_level_hl_5d_base_v150_signal(calendardate, closeadj):
    result = calendardate.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
