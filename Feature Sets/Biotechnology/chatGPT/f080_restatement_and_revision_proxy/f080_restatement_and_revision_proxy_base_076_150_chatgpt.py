"""Family f080 - Revision and restatement proxy (Fundamental Dynamics) | Sharadar tables: SF1 | fields: datekey, lastupdated, reportperiod, dimension | base 076-150"""
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
def _restatement_and_revision_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _restatement_and_revision_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _restatement_and_revision_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of revisioncount/dimension
def rarp_f080_restatement_and_revision_proxy_log_per_dimension_504d_base_v076_signal(revisioncount, dimension):
    s = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revisioncount/assets
def rarp_f080_restatement_and_revision_proxy_log_per_assets_252d_base_v077_signal(revisioncount, assets):
    s = _restatement_and_revision_proxy_scaled(revisioncount, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of revisioncount/assets
def rarp_f080_restatement_and_revision_proxy_log_per_assets_504d_base_v078_signal(revisioncount, assets):
    s = _restatement_and_revision_proxy_scaled(revisioncount, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_ewm_21d_base_v079_signal(revisioncount, closeadj):
    result = revisioncount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_ewm_63d_base_v080_signal(revisioncount, closeadj):
    result = revisioncount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_ewm_252d_base_v081_signal(revisioncount, closeadj):
    result = revisioncount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_med_63d_base_v082_signal(revisioncount, closeadj):
    result = revisioncount.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_med_252d_base_v083_signal(revisioncount, closeadj):
    result = revisioncount.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_med_504d_base_v084_signal(revisioncount, closeadj):
    result = revisioncount.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of revisioncount
def rarp_f080_restatement_and_revision_proxy_skew_252d_base_v085_signal(revisioncount):
    result = revisioncount.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of revisioncount
def rarp_f080_restatement_and_revision_proxy_skew_504d_base_v086_signal(revisioncount):
    result = revisioncount.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of revisioncount
def rarp_f080_restatement_and_revision_proxy_kurt_252d_base_v087_signal(revisioncount):
    result = revisioncount.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of revisioncount
def rarp_f080_restatement_and_revision_proxy_kurt_504d_base_v088_signal(revisioncount):
    result = revisioncount.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_rank_252d_base_v089_signal(revisioncount, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = revisioncount.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_rank_504d_base_v090_signal(revisioncount, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = revisioncount.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_rank_1008d_base_v091_signal(revisioncount, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = revisioncount.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of revisioncount from 63d mean times closeadj
def rarp_f080_restatement_and_revision_proxy_devmean_63d_base_v092_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 63)
    result = (revisioncount - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of revisioncount from 252d mean times closeadj
def rarp_f080_restatement_and_revision_proxy_devmean_252d_base_v093_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 252)
    result = (revisioncount - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of revisioncount from 504d mean times closeadj
def rarp_f080_restatement_and_revision_proxy_devmean_504d_base_v094_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 504)
    result = (revisioncount - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_logdiff_21d_base_v095_signal(revisioncount, closeadj):
    lr = _restatement_and_revision_proxy_log(revisioncount)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_logdiff_63d_base_v096_signal(revisioncount, closeadj):
    lr = _restatement_and_revision_proxy_log(revisioncount)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_logdiff_252d_base_v097_signal(revisioncount, closeadj):
    lr = _restatement_and_revision_proxy_log(revisioncount)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_range_63d_base_v098_signal(revisioncount, closeadj):
    hi = revisioncount.rolling(63, min_periods=max(1, 63//2)).max()
    lo = revisioncount.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_range_252d_base_v099_signal(revisioncount, closeadj):
    hi = revisioncount.rolling(252, min_periods=max(1, 252//2)).max()
    lo = revisioncount.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_range_504d_base_v100_signal(revisioncount, closeadj):
    hi = revisioncount.rolling(504, min_periods=max(1, 504//2)).max()
    lo = revisioncount.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 252d mean times closeadj
def rarp_f080_restatement_and_revision_proxy_rel_252d_base_v101_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 252).replace(0, np.nan)
    result = (revisioncount / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 504d mean times closeadj
def rarp_f080_restatement_and_revision_proxy_rel_504d_base_v102_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 504).replace(0, np.nan)
    result = (revisioncount / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 1008d mean times closeadj
def rarp_f080_restatement_and_revision_proxy_rel_1008d_base_v103_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 1008).replace(0, np.nan)
    result = (revisioncount / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revisioncount/datekey 63d mean
def rarp_f080_restatement_and_revision_proxy_sqnorm_datekey_63d_base_v104_signal(revisioncount, datekey):
    r = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revisioncount/datekey 252d mean
def rarp_f080_restatement_and_revision_proxy_sqnorm_datekey_252d_base_v105_signal(revisioncount, datekey):
    r = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revisioncount/dimension 63d mean
def rarp_f080_restatement_and_revision_proxy_sqnorm_dimension_63d_base_v106_signal(revisioncount, dimension):
    r = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revisioncount/dimension 252d mean
def rarp_f080_restatement_and_revision_proxy_sqnorm_dimension_252d_base_v107_signal(revisioncount, dimension):
    r = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revisioncount/assets 63d mean
def rarp_f080_restatement_and_revision_proxy_sqnorm_assets_63d_base_v108_signal(revisioncount, assets):
    r = _restatement_and_revision_proxy_scaled(revisioncount, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized revisioncount/assets 252d mean
def rarp_f080_restatement_and_revision_proxy_sqnorm_assets_252d_base_v109_signal(revisioncount, assets):
    r = _restatement_and_revision_proxy_scaled(revisioncount, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_infrat_63d_base_v110_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 63)
    s = _std(revisioncount, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_infrat_252d_base_v111_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 252)
    s = _std(revisioncount, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_infrat_504d_base_v112_signal(revisioncount, closeadj):
    m = _mean(revisioncount, 504)
    s = _std(revisioncount, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of revisioncount
def rarp_f080_restatement_and_revision_proxy_cv_252d_base_v113_signal(revisioncount):
    m = _mean(revisioncount, 252).abs().replace(0, np.nan)
    s = _std(revisioncount, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of revisioncount
def rarp_f080_restatement_and_revision_proxy_cv_504d_base_v114_signal(revisioncount):
    m = _mean(revisioncount, 504).abs().replace(0, np.nan)
    s = _std(revisioncount, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_5d_base_v115_signal(revisioncount, closeadj):
    result = revisioncount.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_21d_base_v116_signal(revisioncount, closeadj):
    result = revisioncount.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_63d_base_v117_signal(revisioncount, closeadj):
    result = revisioncount.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_252d_base_v118_signal(revisioncount, closeadj):
    result = revisioncount.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(revisioncount) / mean(datekey) x closeadj
def rarp_f080_restatement_and_revision_proxy_cumper_datekey_252d_base_v119_signal(revisioncount, datekey, closeadj):
    s = revisioncount.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(datekey, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(revisioncount) / mean(datekey) x closeadj
def rarp_f080_restatement_and_revision_proxy_cumper_datekey_504d_base_v120_signal(revisioncount, datekey, closeadj):
    s = revisioncount.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(datekey, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(revisioncount) / mean(dimension) x closeadj
def rarp_f080_restatement_and_revision_proxy_cumper_dimension_252d_base_v121_signal(revisioncount, dimension, closeadj):
    s = revisioncount.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(dimension, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(revisioncount) / mean(dimension) x closeadj
def rarp_f080_restatement_and_revision_proxy_cumper_dimension_504d_base_v122_signal(revisioncount, dimension, closeadj):
    s = revisioncount.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(dimension, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_pos_63d_base_v123_signal(revisioncount, closeadj):
    pos = revisioncount.where(revisioncount > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_pos_252d_base_v124_signal(revisioncount, closeadj):
    pos = revisioncount.where(revisioncount > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_neg_63d_base_v125_signal(revisioncount, closeadj):
    neg = revisioncount.where(revisioncount < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_neg_252d_base_v126_signal(revisioncount, closeadj):
    neg = revisioncount.where(revisioncount < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_hl_21d_base_v127_signal(revisioncount, closeadj):
    result = revisioncount.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_hl_63d_base_v128_signal(revisioncount, closeadj):
    result = revisioncount.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_hl_252d_base_v129_signal(revisioncount, closeadj):
    result = revisioncount.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of revisioncount
def rarp_f080_restatement_and_revision_proxy_z_63d_base_v130_signal(revisioncount):
    result = _z(revisioncount, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of revisioncount
def rarp_f080_restatement_and_revision_proxy_z_126d_base_v131_signal(revisioncount):
    result = _z(revisioncount, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of revisioncount
def rarp_f080_restatement_and_revision_proxy_z_1008d_base_v132_signal(revisioncount):
    result = _z(revisioncount, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_st_lt_252_21d_base_v133_signal(revisioncount, closeadj):
    sm = _mean(revisioncount, 21)
    lm = _mean(revisioncount, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_st_lt_252_63d_base_v134_signal(revisioncount, closeadj):
    sm = _mean(revisioncount, 63)
    lm = _mean(revisioncount, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_st_lt_504_21d_base_v135_signal(revisioncount, closeadj):
    sm = _mean(revisioncount, 21)
    lm = _mean(revisioncount, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_st_lt_504_63d_base_v136_signal(revisioncount, closeadj):
    sm = _mean(revisioncount, 63)
    lm = _mean(revisioncount, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged revisioncount/datekey times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_per_datekey_21d_base_v137_signal(revisioncount, datekey, closeadj):
    r = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged revisioncount/datekey times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_per_datekey_63d_base_v138_signal(revisioncount, datekey, closeadj):
    r = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged revisioncount/datekey times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_per_datekey_252d_base_v139_signal(revisioncount, datekey, closeadj):
    r = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged revisioncount/dimension times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_per_dimension_21d_base_v140_signal(revisioncount, dimension, closeadj):
    r = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged revisioncount/dimension times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_per_dimension_63d_base_v141_signal(revisioncount, dimension, closeadj):
    r = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged revisioncount/dimension times closeadj
def rarp_f080_restatement_and_revision_proxy_lag_per_dimension_252d_base_v142_signal(revisioncount, dimension, closeadj):
    r = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |revisioncount| times closeadj
def rarp_f080_restatement_and_revision_proxy_abssum_63d_base_v143_signal(revisioncount, closeadj):
    result = revisioncount.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |revisioncount| times closeadj
def rarp_f080_restatement_and_revision_proxy_abssum_252d_base_v144_signal(revisioncount, closeadj):
    result = revisioncount.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |revisioncount| times closeadj
def rarp_f080_restatement_and_revision_proxy_abssum_504d_base_v145_signal(revisioncount, closeadj):
    result = revisioncount.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of revisioncount
def rarp_f080_restatement_and_revision_proxy_acf1_252d_base_v146_signal(revisioncount):
    result = revisioncount.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of revisioncount
def rarp_f080_restatement_and_revision_proxy_acf1_504d_base_v147_signal(revisioncount):
    result = revisioncount.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of revisioncount
def rarp_f080_restatement_and_revision_proxy_posinrange_252d_base_v148_signal(revisioncount):
    m = _mean(revisioncount, 252)
    hi = revisioncount.rolling(252, min_periods=max(1, 252//2)).max()
    lo = revisioncount.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of revisioncount
def rarp_f080_restatement_and_revision_proxy_posinrange_504d_base_v149_signal(revisioncount):
    m = _mean(revisioncount, 504)
    hi = revisioncount.rolling(504, min_periods=max(1, 504//2)).max()
    lo = revisioncount.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_hl_5d_base_v150_signal(revisioncount, closeadj):
    result = revisioncount.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
