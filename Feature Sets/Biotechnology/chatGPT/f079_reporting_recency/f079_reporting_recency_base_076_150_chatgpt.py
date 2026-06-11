"""Family f079 - Financial statement timeliness (Fundamental Dynamics) | Sharadar tables: SF1 | fields: calendardate, reportperiod, datekey, lastupdated | base 076-150"""
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
def _reporting_recency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _reporting_recency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _reporting_recency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of filingage/datekey
def rr_f079_reporting_recency_log_per_datekey_504d_base_v076_signal(filingage, datekey):
    s = _reporting_recency_scaled(filingage, datekey)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of filingage/assets
def rr_f079_reporting_recency_log_per_assets_252d_base_v077_signal(filingage, assets):
    s = _reporting_recency_scaled(filingage, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of filingage/assets
def rr_f079_reporting_recency_log_per_assets_504d_base_v078_signal(filingage, assets):
    s = _reporting_recency_scaled(filingage, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of filingage times closeadj
def rr_f079_reporting_recency_ewm_21d_base_v079_signal(filingage, closeadj):
    result = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of filingage times closeadj
def rr_f079_reporting_recency_ewm_63d_base_v080_signal(filingage, closeadj):
    result = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of filingage times closeadj
def rr_f079_reporting_recency_ewm_252d_base_v081_signal(filingage, closeadj):
    result = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of filingage times closeadj
def rr_f079_reporting_recency_med_63d_base_v082_signal(filingage, closeadj):
    result = filingage.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of filingage times closeadj
def rr_f079_reporting_recency_med_252d_base_v083_signal(filingage, closeadj):
    result = filingage.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of filingage times closeadj
def rr_f079_reporting_recency_med_504d_base_v084_signal(filingage, closeadj):
    result = filingage.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of filingage
def rr_f079_reporting_recency_skew_252d_base_v085_signal(filingage):
    result = filingage.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of filingage
def rr_f079_reporting_recency_skew_504d_base_v086_signal(filingage):
    result = filingage.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of filingage
def rr_f079_reporting_recency_kurt_252d_base_v087_signal(filingage):
    result = filingage.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of filingage
def rr_f079_reporting_recency_kurt_504d_base_v088_signal(filingage):
    result = filingage.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of filingage times closeadj
def rr_f079_reporting_recency_rank_252d_base_v089_signal(filingage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = filingage.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of filingage times closeadj
def rr_f079_reporting_recency_rank_504d_base_v090_signal(filingage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = filingage.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of filingage times closeadj
def rr_f079_reporting_recency_rank_1008d_base_v091_signal(filingage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = filingage.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of filingage from 63d mean times closeadj
def rr_f079_reporting_recency_devmean_63d_base_v092_signal(filingage, closeadj):
    m = _mean(filingage, 63)
    result = (filingage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of filingage from 252d mean times closeadj
def rr_f079_reporting_recency_devmean_252d_base_v093_signal(filingage, closeadj):
    m = _mean(filingage, 252)
    result = (filingage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of filingage from 504d mean times closeadj
def rr_f079_reporting_recency_devmean_504d_base_v094_signal(filingage, closeadj):
    m = _mean(filingage, 504)
    result = (filingage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of filingage times closeadj
def rr_f079_reporting_recency_logdiff_21d_base_v095_signal(filingage, closeadj):
    lr = _reporting_recency_log(filingage)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of filingage times closeadj
def rr_f079_reporting_recency_logdiff_63d_base_v096_signal(filingage, closeadj):
    lr = _reporting_recency_log(filingage)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of filingage times closeadj
def rr_f079_reporting_recency_logdiff_252d_base_v097_signal(filingage, closeadj):
    lr = _reporting_recency_log(filingage)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of filingage times closeadj
def rr_f079_reporting_recency_range_63d_base_v098_signal(filingage, closeadj):
    hi = filingage.rolling(63, min_periods=max(1, 63//2)).max()
    lo = filingage.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of filingage times closeadj
def rr_f079_reporting_recency_range_252d_base_v099_signal(filingage, closeadj):
    hi = filingage.rolling(252, min_periods=max(1, 252//2)).max()
    lo = filingage.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of filingage times closeadj
def rr_f079_reporting_recency_range_504d_base_v100_signal(filingage, closeadj):
    hi = filingage.rolling(504, min_periods=max(1, 504//2)).max()
    lo = filingage.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 252d mean times closeadj
def rr_f079_reporting_recency_rel_252d_base_v101_signal(filingage, closeadj):
    m = _mean(filingage, 252).replace(0, np.nan)
    result = (filingage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 504d mean times closeadj
def rr_f079_reporting_recency_rel_504d_base_v102_signal(filingage, closeadj):
    m = _mean(filingage, 504).replace(0, np.nan)
    result = (filingage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 1008d mean times closeadj
def rr_f079_reporting_recency_rel_1008d_base_v103_signal(filingage, closeadj):
    m = _mean(filingage, 1008).replace(0, np.nan)
    result = (filingage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized filingage/calendardate 63d mean
def rr_f079_reporting_recency_sqnorm_calendardate_63d_base_v104_signal(filingage, calendardate):
    r = _reporting_recency_scaled(filingage, calendardate)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized filingage/calendardate 252d mean
def rr_f079_reporting_recency_sqnorm_calendardate_252d_base_v105_signal(filingage, calendardate):
    r = _reporting_recency_scaled(filingage, calendardate)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized filingage/datekey 63d mean
def rr_f079_reporting_recency_sqnorm_datekey_63d_base_v106_signal(filingage, datekey):
    r = _reporting_recency_scaled(filingage, datekey)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized filingage/datekey 252d mean
def rr_f079_reporting_recency_sqnorm_datekey_252d_base_v107_signal(filingage, datekey):
    r = _reporting_recency_scaled(filingage, datekey)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized filingage/assets 63d mean
def rr_f079_reporting_recency_sqnorm_assets_63d_base_v108_signal(filingage, assets):
    r = _reporting_recency_scaled(filingage, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized filingage/assets 252d mean
def rr_f079_reporting_recency_sqnorm_assets_252d_base_v109_signal(filingage, assets):
    r = _reporting_recency_scaled(filingage, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of filingage times closeadj
def rr_f079_reporting_recency_infrat_63d_base_v110_signal(filingage, closeadj):
    m = _mean(filingage, 63)
    s = _std(filingage, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of filingage times closeadj
def rr_f079_reporting_recency_infrat_252d_base_v111_signal(filingage, closeadj):
    m = _mean(filingage, 252)
    s = _std(filingage, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of filingage times closeadj
def rr_f079_reporting_recency_infrat_504d_base_v112_signal(filingage, closeadj):
    m = _mean(filingage, 504)
    s = _std(filingage, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of filingage
def rr_f079_reporting_recency_cv_252d_base_v113_signal(filingage):
    m = _mean(filingage, 252).abs().replace(0, np.nan)
    s = _std(filingage, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of filingage
def rr_f079_reporting_recency_cv_504d_base_v114_signal(filingage):
    m = _mean(filingage, 504).abs().replace(0, np.nan)
    s = _std(filingage, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged filingage times closeadj
def rr_f079_reporting_recency_lag_5d_base_v115_signal(filingage, closeadj):
    result = filingage.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged filingage times closeadj
def rr_f079_reporting_recency_lag_21d_base_v116_signal(filingage, closeadj):
    result = filingage.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged filingage times closeadj
def rr_f079_reporting_recency_lag_63d_base_v117_signal(filingage, closeadj):
    result = filingage.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged filingage times closeadj
def rr_f079_reporting_recency_lag_252d_base_v118_signal(filingage, closeadj):
    result = filingage.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(filingage) / mean(calendardate) x closeadj
def rr_f079_reporting_recency_cumper_calendardate_252d_base_v119_signal(filingage, calendardate, closeadj):
    s = filingage.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(calendardate, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(filingage) / mean(calendardate) x closeadj
def rr_f079_reporting_recency_cumper_calendardate_504d_base_v120_signal(filingage, calendardate, closeadj):
    s = filingage.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(calendardate, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(filingage) / mean(datekey) x closeadj
def rr_f079_reporting_recency_cumper_datekey_252d_base_v121_signal(filingage, datekey, closeadj):
    s = filingage.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(datekey, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(filingage) / mean(datekey) x closeadj
def rr_f079_reporting_recency_cumper_datekey_504d_base_v122_signal(filingage, datekey, closeadj):
    s = filingage.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(datekey, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only filingage times closeadj
def rr_f079_reporting_recency_pos_63d_base_v123_signal(filingage, closeadj):
    pos = filingage.where(filingage > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only filingage times closeadj
def rr_f079_reporting_recency_pos_252d_base_v124_signal(filingage, closeadj):
    pos = filingage.where(filingage > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only filingage times closeadj
def rr_f079_reporting_recency_neg_63d_base_v125_signal(filingage, closeadj):
    neg = filingage.where(filingage < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only filingage times closeadj
def rr_f079_reporting_recency_neg_252d_base_v126_signal(filingage, closeadj):
    neg = filingage.where(filingage < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of filingage times closeadj
def rr_f079_reporting_recency_hl_21d_base_v127_signal(filingage, closeadj):
    result = filingage.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of filingage times closeadj
def rr_f079_reporting_recency_hl_63d_base_v128_signal(filingage, closeadj):
    result = filingage.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of filingage times closeadj
def rr_f079_reporting_recency_hl_252d_base_v129_signal(filingage, closeadj):
    result = filingage.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of filingage
def rr_f079_reporting_recency_z_63d_base_v130_signal(filingage):
    result = _z(filingage, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of filingage
def rr_f079_reporting_recency_z_126d_base_v131_signal(filingage):
    result = _z(filingage, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of filingage
def rr_f079_reporting_recency_z_1008d_base_v132_signal(filingage):
    result = _z(filingage, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of filingage times closeadj
def rr_f079_reporting_recency_st_lt_252_21d_base_v133_signal(filingage, closeadj):
    sm = _mean(filingage, 21)
    lm = _mean(filingage, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of filingage times closeadj
def rr_f079_reporting_recency_st_lt_252_63d_base_v134_signal(filingage, closeadj):
    sm = _mean(filingage, 63)
    lm = _mean(filingage, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of filingage times closeadj
def rr_f079_reporting_recency_st_lt_504_21d_base_v135_signal(filingage, closeadj):
    sm = _mean(filingage, 21)
    lm = _mean(filingage, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of filingage times closeadj
def rr_f079_reporting_recency_st_lt_504_63d_base_v136_signal(filingage, closeadj):
    sm = _mean(filingage, 63)
    lm = _mean(filingage, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged filingage/calendardate times closeadj
def rr_f079_reporting_recency_lag_per_calendardate_21d_base_v137_signal(filingage, calendardate, closeadj):
    r = _reporting_recency_scaled(filingage, calendardate)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged filingage/calendardate times closeadj
def rr_f079_reporting_recency_lag_per_calendardate_63d_base_v138_signal(filingage, calendardate, closeadj):
    r = _reporting_recency_scaled(filingage, calendardate)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged filingage/calendardate times closeadj
def rr_f079_reporting_recency_lag_per_calendardate_252d_base_v139_signal(filingage, calendardate, closeadj):
    r = _reporting_recency_scaled(filingage, calendardate)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged filingage/datekey times closeadj
def rr_f079_reporting_recency_lag_per_datekey_21d_base_v140_signal(filingage, datekey, closeadj):
    r = _reporting_recency_scaled(filingage, datekey)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged filingage/datekey times closeadj
def rr_f079_reporting_recency_lag_per_datekey_63d_base_v141_signal(filingage, datekey, closeadj):
    r = _reporting_recency_scaled(filingage, datekey)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged filingage/datekey times closeadj
def rr_f079_reporting_recency_lag_per_datekey_252d_base_v142_signal(filingage, datekey, closeadj):
    r = _reporting_recency_scaled(filingage, datekey)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |filingage| times closeadj
def rr_f079_reporting_recency_abssum_63d_base_v143_signal(filingage, closeadj):
    result = filingage.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |filingage| times closeadj
def rr_f079_reporting_recency_abssum_252d_base_v144_signal(filingage, closeadj):
    result = filingage.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |filingage| times closeadj
def rr_f079_reporting_recency_abssum_504d_base_v145_signal(filingage, closeadj):
    result = filingage.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of filingage
def rr_f079_reporting_recency_acf1_252d_base_v146_signal(filingage):
    result = filingage.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of filingage
def rr_f079_reporting_recency_acf1_504d_base_v147_signal(filingage):
    result = filingage.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of filingage
def rr_f079_reporting_recency_posinrange_252d_base_v148_signal(filingage):
    m = _mean(filingage, 252)
    hi = filingage.rolling(252, min_periods=max(1, 252//2)).max()
    lo = filingage.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of filingage
def rr_f079_reporting_recency_posinrange_504d_base_v149_signal(filingage):
    m = _mean(filingage, 504)
    hi = filingage.rolling(504, min_periods=max(1, 504//2)).max()
    lo = filingage.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of filingage times closeadj
def rr_f079_reporting_recency_hl_5d_base_v150_signal(filingage, closeadj):
    result = filingage.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
