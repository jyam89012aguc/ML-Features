"""Family f26 - Deferred revenue as funding  (D_Capital_Debt) | base 076-150"""
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
def _deferred_revenue_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _deferred_revenue_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _deferred_revenue_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of deferredrev/marketcap
def dr_f26_deferred_revenue_log_per_marketcap_504d_base_v076_signal(deferredrev, marketcap):
    s = _deferred_revenue_scaled(deferredrev, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of deferredrev/equity
def dr_f26_deferred_revenue_log_per_equity_252d_base_v077_signal(deferredrev, equity):
    s = _deferred_revenue_scaled(deferredrev, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of deferredrev/equity
def dr_f26_deferred_revenue_log_per_equity_504d_base_v078_signal(deferredrev, equity):
    s = _deferred_revenue_scaled(deferredrev, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of deferredrev times closeadj
def dr_f26_deferred_revenue_ewm_21d_base_v079_signal(deferredrev, closeadj):
    result = deferredrev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of deferredrev times closeadj
def dr_f26_deferred_revenue_ewm_63d_base_v080_signal(deferredrev, closeadj):
    result = deferredrev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of deferredrev times closeadj
def dr_f26_deferred_revenue_ewm_252d_base_v081_signal(deferredrev, closeadj):
    result = deferredrev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of deferredrev times closeadj
def dr_f26_deferred_revenue_med_63d_base_v082_signal(deferredrev, closeadj):
    result = deferredrev.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of deferredrev times closeadj
def dr_f26_deferred_revenue_med_252d_base_v083_signal(deferredrev, closeadj):
    result = deferredrev.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of deferredrev times closeadj
def dr_f26_deferred_revenue_med_504d_base_v084_signal(deferredrev, closeadj):
    result = deferredrev.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of deferredrev
def dr_f26_deferred_revenue_skew_252d_base_v085_signal(deferredrev):
    result = deferredrev.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of deferredrev
def dr_f26_deferred_revenue_skew_504d_base_v086_signal(deferredrev):
    result = deferredrev.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of deferredrev
def dr_f26_deferred_revenue_kurt_252d_base_v087_signal(deferredrev):
    result = deferredrev.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of deferredrev
def dr_f26_deferred_revenue_kurt_504d_base_v088_signal(deferredrev):
    result = deferredrev.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of deferredrev times closeadj
def dr_f26_deferred_revenue_rank_252d_base_v089_signal(deferredrev, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = deferredrev.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of deferredrev times closeadj
def dr_f26_deferred_revenue_rank_504d_base_v090_signal(deferredrev, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = deferredrev.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of deferredrev times closeadj
def dr_f26_deferred_revenue_rank_1008d_base_v091_signal(deferredrev, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = deferredrev.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of deferredrev from 63d mean times closeadj
def dr_f26_deferred_revenue_devmean_63d_base_v092_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 63)
    result = (deferredrev - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of deferredrev from 252d mean times closeadj
def dr_f26_deferred_revenue_devmean_252d_base_v093_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 252)
    result = (deferredrev - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of deferredrev from 504d mean times closeadj
def dr_f26_deferred_revenue_devmean_504d_base_v094_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 504)
    result = (deferredrev - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of deferredrev times closeadj
def dr_f26_deferred_revenue_logdiff_21d_base_v095_signal(deferredrev, closeadj):
    lr = _deferred_revenue_log(deferredrev)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of deferredrev times closeadj
def dr_f26_deferred_revenue_logdiff_63d_base_v096_signal(deferredrev, closeadj):
    lr = _deferred_revenue_log(deferredrev)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of deferredrev times closeadj
def dr_f26_deferred_revenue_logdiff_252d_base_v097_signal(deferredrev, closeadj):
    lr = _deferred_revenue_log(deferredrev)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of deferredrev times closeadj
def dr_f26_deferred_revenue_range_63d_base_v098_signal(deferredrev, closeadj):
    hi = deferredrev.rolling(63, min_periods=max(1, 63//2)).max()
    lo = deferredrev.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of deferredrev times closeadj
def dr_f26_deferred_revenue_range_252d_base_v099_signal(deferredrev, closeadj):
    hi = deferredrev.rolling(252, min_periods=max(1, 252//2)).max()
    lo = deferredrev.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of deferredrev times closeadj
def dr_f26_deferred_revenue_range_504d_base_v100_signal(deferredrev, closeadj):
    hi = deferredrev.rolling(504, min_periods=max(1, 504//2)).max()
    lo = deferredrev.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 252d mean times closeadj
def dr_f26_deferred_revenue_rel_252d_base_v101_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 252).replace(0, np.nan)
    result = (deferredrev / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 504d mean times closeadj
def dr_f26_deferred_revenue_rel_504d_base_v102_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 504).replace(0, np.nan)
    result = (deferredrev / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 1008d mean times closeadj
def dr_f26_deferred_revenue_rel_1008d_base_v103_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 1008).replace(0, np.nan)
    result = (deferredrev / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized deferredrev/assets 63d mean
def dr_f26_deferred_revenue_sqnorm_assets_63d_base_v104_signal(deferredrev, assets):
    r = _deferred_revenue_scaled(deferredrev, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized deferredrev/assets 252d mean
def dr_f26_deferred_revenue_sqnorm_assets_252d_base_v105_signal(deferredrev, assets):
    r = _deferred_revenue_scaled(deferredrev, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized deferredrev/marketcap 63d mean
def dr_f26_deferred_revenue_sqnorm_marketcap_63d_base_v106_signal(deferredrev, marketcap):
    r = _deferred_revenue_scaled(deferredrev, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized deferredrev/marketcap 252d mean
def dr_f26_deferred_revenue_sqnorm_marketcap_252d_base_v107_signal(deferredrev, marketcap):
    r = _deferred_revenue_scaled(deferredrev, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized deferredrev/equity 63d mean
def dr_f26_deferred_revenue_sqnorm_equity_63d_base_v108_signal(deferredrev, equity):
    r = _deferred_revenue_scaled(deferredrev, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized deferredrev/equity 252d mean
def dr_f26_deferred_revenue_sqnorm_equity_252d_base_v109_signal(deferredrev, equity):
    r = _deferred_revenue_scaled(deferredrev, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of deferredrev times closeadj
def dr_f26_deferred_revenue_infrat_63d_base_v110_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 63)
    s = _std(deferredrev, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of deferredrev times closeadj
def dr_f26_deferred_revenue_infrat_252d_base_v111_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 252)
    s = _std(deferredrev, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of deferredrev times closeadj
def dr_f26_deferred_revenue_infrat_504d_base_v112_signal(deferredrev, closeadj):
    m = _mean(deferredrev, 504)
    s = _std(deferredrev, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of deferredrev
def dr_f26_deferred_revenue_cv_252d_base_v113_signal(deferredrev):
    m = _mean(deferredrev, 252).abs().replace(0, np.nan)
    s = _std(deferredrev, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of deferredrev
def dr_f26_deferred_revenue_cv_504d_base_v114_signal(deferredrev):
    m = _mean(deferredrev, 504).abs().replace(0, np.nan)
    s = _std(deferredrev, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged deferredrev times closeadj
def dr_f26_deferred_revenue_lag_5d_base_v115_signal(deferredrev, closeadj):
    result = deferredrev.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged deferredrev times closeadj
def dr_f26_deferred_revenue_lag_21d_base_v116_signal(deferredrev, closeadj):
    result = deferredrev.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged deferredrev times closeadj
def dr_f26_deferred_revenue_lag_63d_base_v117_signal(deferredrev, closeadj):
    result = deferredrev.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged deferredrev times closeadj
def dr_f26_deferred_revenue_lag_252d_base_v118_signal(deferredrev, closeadj):
    result = deferredrev.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(deferredrev) / mean(assets) x closeadj
def dr_f26_deferred_revenue_cumper_assets_252d_base_v119_signal(deferredrev, assets, closeadj):
    s = deferredrev.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(deferredrev) / mean(assets) x closeadj
def dr_f26_deferred_revenue_cumper_assets_504d_base_v120_signal(deferredrev, assets, closeadj):
    s = deferredrev.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(deferredrev) / mean(marketcap) x closeadj
def dr_f26_deferred_revenue_cumper_marketcap_252d_base_v121_signal(deferredrev, marketcap, closeadj):
    s = deferredrev.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(deferredrev) / mean(marketcap) x closeadj
def dr_f26_deferred_revenue_cumper_marketcap_504d_base_v122_signal(deferredrev, marketcap, closeadj):
    s = deferredrev.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only deferredrev times closeadj
def dr_f26_deferred_revenue_pos_63d_base_v123_signal(deferredrev, closeadj):
    pos = deferredrev.where(deferredrev > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only deferredrev times closeadj
def dr_f26_deferred_revenue_pos_252d_base_v124_signal(deferredrev, closeadj):
    pos = deferredrev.where(deferredrev > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only deferredrev times closeadj
def dr_f26_deferred_revenue_neg_63d_base_v125_signal(deferredrev, closeadj):
    neg = deferredrev.where(deferredrev < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only deferredrev times closeadj
def dr_f26_deferred_revenue_neg_252d_base_v126_signal(deferredrev, closeadj):
    neg = deferredrev.where(deferredrev < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of deferredrev times closeadj
def dr_f26_deferred_revenue_hl_21d_base_v127_signal(deferredrev, closeadj):
    result = deferredrev.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of deferredrev times closeadj
def dr_f26_deferred_revenue_hl_63d_base_v128_signal(deferredrev, closeadj):
    result = deferredrev.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of deferredrev times closeadj
def dr_f26_deferred_revenue_hl_252d_base_v129_signal(deferredrev, closeadj):
    result = deferredrev.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of deferredrev
def dr_f26_deferred_revenue_z_63d_base_v130_signal(deferredrev):
    result = _z(deferredrev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of deferredrev
def dr_f26_deferred_revenue_z_126d_base_v131_signal(deferredrev):
    result = _z(deferredrev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of deferredrev
def dr_f26_deferred_revenue_z_1008d_base_v132_signal(deferredrev):
    result = _z(deferredrev, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of deferredrev times closeadj
def dr_f26_deferred_revenue_st_lt_252_21d_base_v133_signal(deferredrev, closeadj):
    sm = _mean(deferredrev, 21)
    lm = _mean(deferredrev, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of deferredrev times closeadj
def dr_f26_deferred_revenue_st_lt_252_63d_base_v134_signal(deferredrev, closeadj):
    sm = _mean(deferredrev, 63)
    lm = _mean(deferredrev, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of deferredrev times closeadj
def dr_f26_deferred_revenue_st_lt_504_21d_base_v135_signal(deferredrev, closeadj):
    sm = _mean(deferredrev, 21)
    lm = _mean(deferredrev, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of deferredrev times closeadj
def dr_f26_deferred_revenue_st_lt_504_63d_base_v136_signal(deferredrev, closeadj):
    sm = _mean(deferredrev, 63)
    lm = _mean(deferredrev, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged deferredrev/assets times closeadj
def dr_f26_deferred_revenue_lag_per_assets_21d_base_v137_signal(deferredrev, assets, closeadj):
    r = _deferred_revenue_scaled(deferredrev, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged deferredrev/assets times closeadj
def dr_f26_deferred_revenue_lag_per_assets_63d_base_v138_signal(deferredrev, assets, closeadj):
    r = _deferred_revenue_scaled(deferredrev, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged deferredrev/assets times closeadj
def dr_f26_deferred_revenue_lag_per_assets_252d_base_v139_signal(deferredrev, assets, closeadj):
    r = _deferred_revenue_scaled(deferredrev, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged deferredrev/marketcap times closeadj
def dr_f26_deferred_revenue_lag_per_marketcap_21d_base_v140_signal(deferredrev, marketcap, closeadj):
    r = _deferred_revenue_scaled(deferredrev, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged deferredrev/marketcap times closeadj
def dr_f26_deferred_revenue_lag_per_marketcap_63d_base_v141_signal(deferredrev, marketcap, closeadj):
    r = _deferred_revenue_scaled(deferredrev, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged deferredrev/marketcap times closeadj
def dr_f26_deferred_revenue_lag_per_marketcap_252d_base_v142_signal(deferredrev, marketcap, closeadj):
    r = _deferred_revenue_scaled(deferredrev, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |deferredrev| times closeadj
def dr_f26_deferred_revenue_abssum_63d_base_v143_signal(deferredrev, closeadj):
    result = deferredrev.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |deferredrev| times closeadj
def dr_f26_deferred_revenue_abssum_252d_base_v144_signal(deferredrev, closeadj):
    result = deferredrev.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |deferredrev| times closeadj
def dr_f26_deferred_revenue_abssum_504d_base_v145_signal(deferredrev, closeadj):
    result = deferredrev.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of deferredrev
def dr_f26_deferred_revenue_acf1_252d_base_v146_signal(deferredrev):
    result = deferredrev.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of deferredrev
def dr_f26_deferred_revenue_acf1_504d_base_v147_signal(deferredrev):
    result = deferredrev.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of deferredrev
def dr_f26_deferred_revenue_posinrange_252d_base_v148_signal(deferredrev):
    m = _mean(deferredrev, 252)
    hi = deferredrev.rolling(252, min_periods=max(1, 252//2)).max()
    lo = deferredrev.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of deferredrev
def dr_f26_deferred_revenue_posinrange_504d_base_v149_signal(deferredrev):
    m = _mean(deferredrev, 504)
    hi = deferredrev.rolling(504, min_periods=max(1, 504//2)).max()
    lo = deferredrev.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of deferredrev times closeadj
def dr_f26_deferred_revenue_hl_5d_base_v150_signal(deferredrev, closeadj):
    result = deferredrev.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
