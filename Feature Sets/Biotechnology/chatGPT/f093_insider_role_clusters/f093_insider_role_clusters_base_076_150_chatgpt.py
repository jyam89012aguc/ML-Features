"""Family f093 - Insider role and cluster behavior (Insiders and Ownership) | Sharadar tables: SF2 | fields: ownername, officertitle, isdirector, isofficer, transactiondate | base 076-150"""
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
def _insider_role_clusters_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_role_clusters_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_role_clusters_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of isdirector/transactiondate
def irc_f093_insider_role_clusters_log_per_transactiondate_504d_base_v076_signal(isdirector, transactiondate):
    s = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of isdirector/assets
def irc_f093_insider_role_clusters_log_per_assets_252d_base_v077_signal(isdirector, assets):
    s = _insider_role_clusters_scaled(isdirector, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of isdirector/assets
def irc_f093_insider_role_clusters_log_per_assets_504d_base_v078_signal(isdirector, assets):
    s = _insider_role_clusters_scaled(isdirector, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of isdirector times closeadj
def irc_f093_insider_role_clusters_ewm_21d_base_v079_signal(isdirector, closeadj):
    result = isdirector.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of isdirector times closeadj
def irc_f093_insider_role_clusters_ewm_63d_base_v080_signal(isdirector, closeadj):
    result = isdirector.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of isdirector times closeadj
def irc_f093_insider_role_clusters_ewm_252d_base_v081_signal(isdirector, closeadj):
    result = isdirector.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of isdirector times closeadj
def irc_f093_insider_role_clusters_med_63d_base_v082_signal(isdirector, closeadj):
    result = isdirector.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of isdirector times closeadj
def irc_f093_insider_role_clusters_med_252d_base_v083_signal(isdirector, closeadj):
    result = isdirector.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of isdirector times closeadj
def irc_f093_insider_role_clusters_med_504d_base_v084_signal(isdirector, closeadj):
    result = isdirector.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of isdirector
def irc_f093_insider_role_clusters_skew_252d_base_v085_signal(isdirector):
    result = isdirector.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of isdirector
def irc_f093_insider_role_clusters_skew_504d_base_v086_signal(isdirector):
    result = isdirector.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of isdirector
def irc_f093_insider_role_clusters_kurt_252d_base_v087_signal(isdirector):
    result = isdirector.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of isdirector
def irc_f093_insider_role_clusters_kurt_504d_base_v088_signal(isdirector):
    result = isdirector.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of isdirector times closeadj
def irc_f093_insider_role_clusters_rank_252d_base_v089_signal(isdirector, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = isdirector.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of isdirector times closeadj
def irc_f093_insider_role_clusters_rank_504d_base_v090_signal(isdirector, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = isdirector.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of isdirector times closeadj
def irc_f093_insider_role_clusters_rank_1008d_base_v091_signal(isdirector, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = isdirector.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of isdirector from 63d mean times closeadj
def irc_f093_insider_role_clusters_devmean_63d_base_v092_signal(isdirector, closeadj):
    m = _mean(isdirector, 63)
    result = (isdirector - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of isdirector from 252d mean times closeadj
def irc_f093_insider_role_clusters_devmean_252d_base_v093_signal(isdirector, closeadj):
    m = _mean(isdirector, 252)
    result = (isdirector - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of isdirector from 504d mean times closeadj
def irc_f093_insider_role_clusters_devmean_504d_base_v094_signal(isdirector, closeadj):
    m = _mean(isdirector, 504)
    result = (isdirector - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of isdirector times closeadj
def irc_f093_insider_role_clusters_logdiff_21d_base_v095_signal(isdirector, closeadj):
    lr = _insider_role_clusters_log(isdirector)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of isdirector times closeadj
def irc_f093_insider_role_clusters_logdiff_63d_base_v096_signal(isdirector, closeadj):
    lr = _insider_role_clusters_log(isdirector)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of isdirector times closeadj
def irc_f093_insider_role_clusters_logdiff_252d_base_v097_signal(isdirector, closeadj):
    lr = _insider_role_clusters_log(isdirector)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of isdirector times closeadj
def irc_f093_insider_role_clusters_range_63d_base_v098_signal(isdirector, closeadj):
    hi = isdirector.rolling(63, min_periods=max(1, 63//2)).max()
    lo = isdirector.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of isdirector times closeadj
def irc_f093_insider_role_clusters_range_252d_base_v099_signal(isdirector, closeadj):
    hi = isdirector.rolling(252, min_periods=max(1, 252//2)).max()
    lo = isdirector.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of isdirector times closeadj
def irc_f093_insider_role_clusters_range_504d_base_v100_signal(isdirector, closeadj):
    hi = isdirector.rolling(504, min_periods=max(1, 504//2)).max()
    lo = isdirector.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 252d mean times closeadj
def irc_f093_insider_role_clusters_rel_252d_base_v101_signal(isdirector, closeadj):
    m = _mean(isdirector, 252).replace(0, np.nan)
    result = (isdirector / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 504d mean times closeadj
def irc_f093_insider_role_clusters_rel_504d_base_v102_signal(isdirector, closeadj):
    m = _mean(isdirector, 504).replace(0, np.nan)
    result = (isdirector / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 1008d mean times closeadj
def irc_f093_insider_role_clusters_rel_1008d_base_v103_signal(isdirector, closeadj):
    m = _mean(isdirector, 1008).replace(0, np.nan)
    result = (isdirector / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized isdirector/isofficer 63d mean
def irc_f093_insider_role_clusters_sqnorm_isofficer_63d_base_v104_signal(isdirector, isofficer):
    r = _insider_role_clusters_scaled(isdirector, isofficer)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized isdirector/isofficer 252d mean
def irc_f093_insider_role_clusters_sqnorm_isofficer_252d_base_v105_signal(isdirector, isofficer):
    r = _insider_role_clusters_scaled(isdirector, isofficer)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized isdirector/transactiondate 63d mean
def irc_f093_insider_role_clusters_sqnorm_transactiondate_63d_base_v106_signal(isdirector, transactiondate):
    r = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized isdirector/transactiondate 252d mean
def irc_f093_insider_role_clusters_sqnorm_transactiondate_252d_base_v107_signal(isdirector, transactiondate):
    r = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized isdirector/assets 63d mean
def irc_f093_insider_role_clusters_sqnorm_assets_63d_base_v108_signal(isdirector, assets):
    r = _insider_role_clusters_scaled(isdirector, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized isdirector/assets 252d mean
def irc_f093_insider_role_clusters_sqnorm_assets_252d_base_v109_signal(isdirector, assets):
    r = _insider_role_clusters_scaled(isdirector, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of isdirector times closeadj
def irc_f093_insider_role_clusters_infrat_63d_base_v110_signal(isdirector, closeadj):
    m = _mean(isdirector, 63)
    s = _std(isdirector, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of isdirector times closeadj
def irc_f093_insider_role_clusters_infrat_252d_base_v111_signal(isdirector, closeadj):
    m = _mean(isdirector, 252)
    s = _std(isdirector, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of isdirector times closeadj
def irc_f093_insider_role_clusters_infrat_504d_base_v112_signal(isdirector, closeadj):
    m = _mean(isdirector, 504)
    s = _std(isdirector, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of isdirector
def irc_f093_insider_role_clusters_cv_252d_base_v113_signal(isdirector):
    m = _mean(isdirector, 252).abs().replace(0, np.nan)
    s = _std(isdirector, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of isdirector
def irc_f093_insider_role_clusters_cv_504d_base_v114_signal(isdirector):
    m = _mean(isdirector, 504).abs().replace(0, np.nan)
    s = _std(isdirector, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged isdirector times closeadj
def irc_f093_insider_role_clusters_lag_5d_base_v115_signal(isdirector, closeadj):
    result = isdirector.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged isdirector times closeadj
def irc_f093_insider_role_clusters_lag_21d_base_v116_signal(isdirector, closeadj):
    result = isdirector.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged isdirector times closeadj
def irc_f093_insider_role_clusters_lag_63d_base_v117_signal(isdirector, closeadj):
    result = isdirector.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged isdirector times closeadj
def irc_f093_insider_role_clusters_lag_252d_base_v118_signal(isdirector, closeadj):
    result = isdirector.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(isdirector) / mean(isofficer) x closeadj
def irc_f093_insider_role_clusters_cumper_isofficer_252d_base_v119_signal(isdirector, isofficer, closeadj):
    s = isdirector.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(isofficer, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(isdirector) / mean(isofficer) x closeadj
def irc_f093_insider_role_clusters_cumper_isofficer_504d_base_v120_signal(isdirector, isofficer, closeadj):
    s = isdirector.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(isofficer, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(isdirector) / mean(transactiondate) x closeadj
def irc_f093_insider_role_clusters_cumper_transactiondate_252d_base_v121_signal(isdirector, transactiondate, closeadj):
    s = isdirector.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(transactiondate, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(isdirector) / mean(transactiondate) x closeadj
def irc_f093_insider_role_clusters_cumper_transactiondate_504d_base_v122_signal(isdirector, transactiondate, closeadj):
    s = isdirector.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(transactiondate, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only isdirector times closeadj
def irc_f093_insider_role_clusters_pos_63d_base_v123_signal(isdirector, closeadj):
    pos = isdirector.where(isdirector > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only isdirector times closeadj
def irc_f093_insider_role_clusters_pos_252d_base_v124_signal(isdirector, closeadj):
    pos = isdirector.where(isdirector > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only isdirector times closeadj
def irc_f093_insider_role_clusters_neg_63d_base_v125_signal(isdirector, closeadj):
    neg = isdirector.where(isdirector < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only isdirector times closeadj
def irc_f093_insider_role_clusters_neg_252d_base_v126_signal(isdirector, closeadj):
    neg = isdirector.where(isdirector < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of isdirector times closeadj
def irc_f093_insider_role_clusters_hl_21d_base_v127_signal(isdirector, closeadj):
    result = isdirector.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of isdirector times closeadj
def irc_f093_insider_role_clusters_hl_63d_base_v128_signal(isdirector, closeadj):
    result = isdirector.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of isdirector times closeadj
def irc_f093_insider_role_clusters_hl_252d_base_v129_signal(isdirector, closeadj):
    result = isdirector.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of isdirector
def irc_f093_insider_role_clusters_z_63d_base_v130_signal(isdirector):
    result = _z(isdirector, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of isdirector
def irc_f093_insider_role_clusters_z_126d_base_v131_signal(isdirector):
    result = _z(isdirector, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of isdirector
def irc_f093_insider_role_clusters_z_1008d_base_v132_signal(isdirector):
    result = _z(isdirector, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of isdirector times closeadj
def irc_f093_insider_role_clusters_st_lt_252_21d_base_v133_signal(isdirector, closeadj):
    sm = _mean(isdirector, 21)
    lm = _mean(isdirector, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of isdirector times closeadj
def irc_f093_insider_role_clusters_st_lt_252_63d_base_v134_signal(isdirector, closeadj):
    sm = _mean(isdirector, 63)
    lm = _mean(isdirector, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of isdirector times closeadj
def irc_f093_insider_role_clusters_st_lt_504_21d_base_v135_signal(isdirector, closeadj):
    sm = _mean(isdirector, 21)
    lm = _mean(isdirector, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of isdirector times closeadj
def irc_f093_insider_role_clusters_st_lt_504_63d_base_v136_signal(isdirector, closeadj):
    sm = _mean(isdirector, 63)
    lm = _mean(isdirector, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged isdirector/isofficer times closeadj
def irc_f093_insider_role_clusters_lag_per_isofficer_21d_base_v137_signal(isdirector, isofficer, closeadj):
    r = _insider_role_clusters_scaled(isdirector, isofficer)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged isdirector/isofficer times closeadj
def irc_f093_insider_role_clusters_lag_per_isofficer_63d_base_v138_signal(isdirector, isofficer, closeadj):
    r = _insider_role_clusters_scaled(isdirector, isofficer)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged isdirector/isofficer times closeadj
def irc_f093_insider_role_clusters_lag_per_isofficer_252d_base_v139_signal(isdirector, isofficer, closeadj):
    r = _insider_role_clusters_scaled(isdirector, isofficer)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged isdirector/transactiondate times closeadj
def irc_f093_insider_role_clusters_lag_per_transactiondate_21d_base_v140_signal(isdirector, transactiondate, closeadj):
    r = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged isdirector/transactiondate times closeadj
def irc_f093_insider_role_clusters_lag_per_transactiondate_63d_base_v141_signal(isdirector, transactiondate, closeadj):
    r = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged isdirector/transactiondate times closeadj
def irc_f093_insider_role_clusters_lag_per_transactiondate_252d_base_v142_signal(isdirector, transactiondate, closeadj):
    r = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |isdirector| times closeadj
def irc_f093_insider_role_clusters_abssum_63d_base_v143_signal(isdirector, closeadj):
    result = isdirector.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |isdirector| times closeadj
def irc_f093_insider_role_clusters_abssum_252d_base_v144_signal(isdirector, closeadj):
    result = isdirector.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |isdirector| times closeadj
def irc_f093_insider_role_clusters_abssum_504d_base_v145_signal(isdirector, closeadj):
    result = isdirector.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of isdirector
def irc_f093_insider_role_clusters_acf1_252d_base_v146_signal(isdirector):
    result = isdirector.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of isdirector
def irc_f093_insider_role_clusters_acf1_504d_base_v147_signal(isdirector):
    result = isdirector.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of isdirector
def irc_f093_insider_role_clusters_posinrange_252d_base_v148_signal(isdirector):
    m = _mean(isdirector, 252)
    hi = isdirector.rolling(252, min_periods=max(1, 252//2)).max()
    lo = isdirector.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of isdirector
def irc_f093_insider_role_clusters_posinrange_504d_base_v149_signal(isdirector):
    m = _mean(isdirector, 504)
    hi = isdirector.rolling(504, min_periods=max(1, 504//2)).max()
    lo = isdirector.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of isdirector times closeadj
def irc_f093_insider_role_clusters_hl_5d_base_v150_signal(isdirector, closeadj):
    result = isdirector.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
