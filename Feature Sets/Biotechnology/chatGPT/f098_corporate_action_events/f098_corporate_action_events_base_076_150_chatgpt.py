"""Family f098 - Corporate actions density and type (Corporate Actions and Events) | Sharadar tables: ACTIONS,SF1,SEP | fields: value, sharesbas, assets, equity, debt | base 076-150"""
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
def _corporate_action_events_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _corporate_action_events_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _corporate_action_events_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of value/assets
def cae_f098_corporate_action_events_log_per_assets_504d_base_v076_signal(value, assets):
    s = _corporate_action_events_scaled(value, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of value/sharesbas
def cae_f098_corporate_action_events_log_per_sharesbas_252d_base_v077_signal(value, sharesbas):
    s = _corporate_action_events_scaled(value, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of value/sharesbas
def cae_f098_corporate_action_events_log_per_sharesbas_504d_base_v078_signal(value, sharesbas):
    s = _corporate_action_events_scaled(value, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of value times closeadj
def cae_f098_corporate_action_events_ewm_21d_base_v079_signal(value, closeadj):
    result = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of value times closeadj
def cae_f098_corporate_action_events_ewm_63d_base_v080_signal(value, closeadj):
    result = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of value times closeadj
def cae_f098_corporate_action_events_ewm_252d_base_v081_signal(value, closeadj):
    result = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of value times closeadj
def cae_f098_corporate_action_events_med_63d_base_v082_signal(value, closeadj):
    result = value.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of value times closeadj
def cae_f098_corporate_action_events_med_252d_base_v083_signal(value, closeadj):
    result = value.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of value times closeadj
def cae_f098_corporate_action_events_med_504d_base_v084_signal(value, closeadj):
    result = value.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of value
def cae_f098_corporate_action_events_skew_252d_base_v085_signal(value):
    result = value.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of value
def cae_f098_corporate_action_events_skew_504d_base_v086_signal(value):
    result = value.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of value
def cae_f098_corporate_action_events_kurt_252d_base_v087_signal(value):
    result = value.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of value
def cae_f098_corporate_action_events_kurt_504d_base_v088_signal(value):
    result = value.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of value times closeadj
def cae_f098_corporate_action_events_rank_252d_base_v089_signal(value, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = value.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of value times closeadj
def cae_f098_corporate_action_events_rank_504d_base_v090_signal(value, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = value.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of value times closeadj
def cae_f098_corporate_action_events_rank_1008d_base_v091_signal(value, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = value.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of value from 63d mean times closeadj
def cae_f098_corporate_action_events_devmean_63d_base_v092_signal(value, closeadj):
    m = _mean(value, 63)
    result = (value - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of value from 252d mean times closeadj
def cae_f098_corporate_action_events_devmean_252d_base_v093_signal(value, closeadj):
    m = _mean(value, 252)
    result = (value - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of value from 504d mean times closeadj
def cae_f098_corporate_action_events_devmean_504d_base_v094_signal(value, closeadj):
    m = _mean(value, 504)
    result = (value - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of value times closeadj
def cae_f098_corporate_action_events_logdiff_21d_base_v095_signal(value, closeadj):
    lr = _corporate_action_events_log(value)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of value times closeadj
def cae_f098_corporate_action_events_logdiff_63d_base_v096_signal(value, closeadj):
    lr = _corporate_action_events_log(value)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of value times closeadj
def cae_f098_corporate_action_events_logdiff_252d_base_v097_signal(value, closeadj):
    lr = _corporate_action_events_log(value)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of value times closeadj
def cae_f098_corporate_action_events_range_63d_base_v098_signal(value, closeadj):
    hi = value.rolling(63, min_periods=max(1, 63//2)).max()
    lo = value.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of value times closeadj
def cae_f098_corporate_action_events_range_252d_base_v099_signal(value, closeadj):
    hi = value.rolling(252, min_periods=max(1, 252//2)).max()
    lo = value.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of value times closeadj
def cae_f098_corporate_action_events_range_504d_base_v100_signal(value, closeadj):
    hi = value.rolling(504, min_periods=max(1, 504//2)).max()
    lo = value.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 252d mean times closeadj
def cae_f098_corporate_action_events_rel_252d_base_v101_signal(value, closeadj):
    m = _mean(value, 252).replace(0, np.nan)
    result = (value / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 504d mean times closeadj
def cae_f098_corporate_action_events_rel_504d_base_v102_signal(value, closeadj):
    m = _mean(value, 504).replace(0, np.nan)
    result = (value / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 1008d mean times closeadj
def cae_f098_corporate_action_events_rel_1008d_base_v103_signal(value, closeadj):
    m = _mean(value, 1008).replace(0, np.nan)
    result = (value / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/sharesbas 63d mean
def cae_f098_corporate_action_events_sqnorm_sharesbas_63d_base_v104_signal(value, sharesbas):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/sharesbas 252d mean
def cae_f098_corporate_action_events_sqnorm_sharesbas_252d_base_v105_signal(value, sharesbas):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/assets 63d mean
def cae_f098_corporate_action_events_sqnorm_assets_63d_base_v106_signal(value, assets):
    r = _corporate_action_events_scaled(value, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/assets 252d mean
def cae_f098_corporate_action_events_sqnorm_assets_252d_base_v107_signal(value, assets):
    r = _corporate_action_events_scaled(value, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/sharesbas 63d mean
def cae_f098_corporate_action_events_sqnorm_sharesbas_63d_base_v108_signal(value, sharesbas):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized value/sharesbas 252d mean
def cae_f098_corporate_action_events_sqnorm_sharesbas_252d_base_v109_signal(value, sharesbas):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of value times closeadj
def cae_f098_corporate_action_events_infrat_63d_base_v110_signal(value, closeadj):
    m = _mean(value, 63)
    s = _std(value, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of value times closeadj
def cae_f098_corporate_action_events_infrat_252d_base_v111_signal(value, closeadj):
    m = _mean(value, 252)
    s = _std(value, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of value times closeadj
def cae_f098_corporate_action_events_infrat_504d_base_v112_signal(value, closeadj):
    m = _mean(value, 504)
    s = _std(value, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of value
def cae_f098_corporate_action_events_cv_252d_base_v113_signal(value):
    m = _mean(value, 252).abs().replace(0, np.nan)
    s = _std(value, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of value
def cae_f098_corporate_action_events_cv_504d_base_v114_signal(value):
    m = _mean(value, 504).abs().replace(0, np.nan)
    s = _std(value, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged value times closeadj
def cae_f098_corporate_action_events_lag_5d_base_v115_signal(value, closeadj):
    result = value.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged value times closeadj
def cae_f098_corporate_action_events_lag_21d_base_v116_signal(value, closeadj):
    result = value.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged value times closeadj
def cae_f098_corporate_action_events_lag_63d_base_v117_signal(value, closeadj):
    result = value.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged value times closeadj
def cae_f098_corporate_action_events_lag_252d_base_v118_signal(value, closeadj):
    result = value.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(value) / mean(sharesbas) x closeadj
def cae_f098_corporate_action_events_cumper_sharesbas_252d_base_v119_signal(value, sharesbas, closeadj):
    s = value.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(value) / mean(sharesbas) x closeadj
def cae_f098_corporate_action_events_cumper_sharesbas_504d_base_v120_signal(value, sharesbas, closeadj):
    s = value.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(value) / mean(assets) x closeadj
def cae_f098_corporate_action_events_cumper_assets_252d_base_v121_signal(value, assets, closeadj):
    s = value.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(value) / mean(assets) x closeadj
def cae_f098_corporate_action_events_cumper_assets_504d_base_v122_signal(value, assets, closeadj):
    s = value.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only value times closeadj
def cae_f098_corporate_action_events_pos_63d_base_v123_signal(value, closeadj):
    pos = value.where(value > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only value times closeadj
def cae_f098_corporate_action_events_pos_252d_base_v124_signal(value, closeadj):
    pos = value.where(value > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only value times closeadj
def cae_f098_corporate_action_events_neg_63d_base_v125_signal(value, closeadj):
    neg = value.where(value < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only value times closeadj
def cae_f098_corporate_action_events_neg_252d_base_v126_signal(value, closeadj):
    neg = value.where(value < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of value times closeadj
def cae_f098_corporate_action_events_hl_21d_base_v127_signal(value, closeadj):
    result = value.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of value times closeadj
def cae_f098_corporate_action_events_hl_63d_base_v128_signal(value, closeadj):
    result = value.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of value times closeadj
def cae_f098_corporate_action_events_hl_252d_base_v129_signal(value, closeadj):
    result = value.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of value
def cae_f098_corporate_action_events_z_63d_base_v130_signal(value):
    result = _z(value, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of value
def cae_f098_corporate_action_events_z_126d_base_v131_signal(value):
    result = _z(value, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of value
def cae_f098_corporate_action_events_z_1008d_base_v132_signal(value):
    result = _z(value, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of value times closeadj
def cae_f098_corporate_action_events_st_lt_252_21d_base_v133_signal(value, closeadj):
    sm = _mean(value, 21)
    lm = _mean(value, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of value times closeadj
def cae_f098_corporate_action_events_st_lt_252_63d_base_v134_signal(value, closeadj):
    sm = _mean(value, 63)
    lm = _mean(value, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of value times closeadj
def cae_f098_corporate_action_events_st_lt_504_21d_base_v135_signal(value, closeadj):
    sm = _mean(value, 21)
    lm = _mean(value, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of value times closeadj
def cae_f098_corporate_action_events_st_lt_504_63d_base_v136_signal(value, closeadj):
    sm = _mean(value, 63)
    lm = _mean(value, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged value/sharesbas times closeadj
def cae_f098_corporate_action_events_lag_per_sharesbas_21d_base_v137_signal(value, sharesbas, closeadj):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged value/sharesbas times closeadj
def cae_f098_corporate_action_events_lag_per_sharesbas_63d_base_v138_signal(value, sharesbas, closeadj):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged value/sharesbas times closeadj
def cae_f098_corporate_action_events_lag_per_sharesbas_252d_base_v139_signal(value, sharesbas, closeadj):
    r = _corporate_action_events_scaled(value, sharesbas)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged value/assets times closeadj
def cae_f098_corporate_action_events_lag_per_assets_21d_base_v140_signal(value, assets, closeadj):
    r = _corporate_action_events_scaled(value, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged value/assets times closeadj
def cae_f098_corporate_action_events_lag_per_assets_63d_base_v141_signal(value, assets, closeadj):
    r = _corporate_action_events_scaled(value, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged value/assets times closeadj
def cae_f098_corporate_action_events_lag_per_assets_252d_base_v142_signal(value, assets, closeadj):
    r = _corporate_action_events_scaled(value, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |value| times closeadj
def cae_f098_corporate_action_events_abssum_63d_base_v143_signal(value, closeadj):
    result = value.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |value| times closeadj
def cae_f098_corporate_action_events_abssum_252d_base_v144_signal(value, closeadj):
    result = value.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |value| times closeadj
def cae_f098_corporate_action_events_abssum_504d_base_v145_signal(value, closeadj):
    result = value.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of value
def cae_f098_corporate_action_events_acf1_252d_base_v146_signal(value):
    result = value.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of value
def cae_f098_corporate_action_events_acf1_504d_base_v147_signal(value):
    result = value.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of value
def cae_f098_corporate_action_events_posinrange_252d_base_v148_signal(value):
    m = _mean(value, 252)
    hi = value.rolling(252, min_periods=max(1, 252//2)).max()
    lo = value.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of value
def cae_f098_corporate_action_events_posinrange_504d_base_v149_signal(value):
    m = _mean(value, 504)
    hi = value.rolling(504, min_periods=max(1, 504//2)).max()
    lo = value.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of value times closeadj
def cae_f098_corporate_action_events_hl_5d_base_v150_signal(value, closeadj):
    result = value.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
