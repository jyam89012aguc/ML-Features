"""Family f026 - preferred, convertible, and senior claim overhang (Capital Structure) | Sharadar tables: SF1 | fields: prefdivis, debtusd, assets, marketcap, equity, debt | base 076-150"""
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
def _preferred_and_convertible_overhang_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _preferred_and_convertible_overhang_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _preferred_and_convertible_overhang_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of prefdivis/assets
def paco_f026_preferred_and_convertible_overhang_log_per_assets_504d_base_v076_signal(prefdivis, assets):
    s = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of prefdivis/marketcap
def paco_f026_preferred_and_convertible_overhang_log_per_marketcap_252d_base_v077_signal(prefdivis, marketcap):
    s = _preferred_and_convertible_overhang_scaled(prefdivis, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of prefdivis/marketcap
def paco_f026_preferred_and_convertible_overhang_log_per_marketcap_504d_base_v078_signal(prefdivis, marketcap):
    s = _preferred_and_convertible_overhang_scaled(prefdivis, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_ewm_21d_base_v079_signal(prefdivis, closeadj):
    result = prefdivis.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_ewm_63d_base_v080_signal(prefdivis, closeadj):
    result = prefdivis.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_ewm_252d_base_v081_signal(prefdivis, closeadj):
    result = prefdivis.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_med_63d_base_v082_signal(prefdivis, closeadj):
    result = prefdivis.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_med_252d_base_v083_signal(prefdivis, closeadj):
    result = prefdivis.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_med_504d_base_v084_signal(prefdivis, closeadj):
    result = prefdivis.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of prefdivis
def paco_f026_preferred_and_convertible_overhang_skew_252d_base_v085_signal(prefdivis):
    result = prefdivis.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of prefdivis
def paco_f026_preferred_and_convertible_overhang_skew_504d_base_v086_signal(prefdivis):
    result = prefdivis.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of prefdivis
def paco_f026_preferred_and_convertible_overhang_kurt_252d_base_v087_signal(prefdivis):
    result = prefdivis.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of prefdivis
def paco_f026_preferred_and_convertible_overhang_kurt_504d_base_v088_signal(prefdivis):
    result = prefdivis.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_rank_252d_base_v089_signal(prefdivis, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = prefdivis.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_rank_504d_base_v090_signal(prefdivis, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = prefdivis.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_rank_1008d_base_v091_signal(prefdivis, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = prefdivis.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of prefdivis from 63d mean times closeadj
def paco_f026_preferred_and_convertible_overhang_devmean_63d_base_v092_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 63)
    result = (prefdivis - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of prefdivis from 252d mean times closeadj
def paco_f026_preferred_and_convertible_overhang_devmean_252d_base_v093_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 252)
    result = (prefdivis - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of prefdivis from 504d mean times closeadj
def paco_f026_preferred_and_convertible_overhang_devmean_504d_base_v094_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 504)
    result = (prefdivis - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_logdiff_21d_base_v095_signal(prefdivis, closeadj):
    lr = _preferred_and_convertible_overhang_log(prefdivis)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_logdiff_63d_base_v096_signal(prefdivis, closeadj):
    lr = _preferred_and_convertible_overhang_log(prefdivis)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_logdiff_252d_base_v097_signal(prefdivis, closeadj):
    lr = _preferred_and_convertible_overhang_log(prefdivis)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_range_63d_base_v098_signal(prefdivis, closeadj):
    hi = prefdivis.rolling(63, min_periods=max(1, 63//2)).max()
    lo = prefdivis.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_range_252d_base_v099_signal(prefdivis, closeadj):
    hi = prefdivis.rolling(252, min_periods=max(1, 252//2)).max()
    lo = prefdivis.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_range_504d_base_v100_signal(prefdivis, closeadj):
    hi = prefdivis.rolling(504, min_periods=max(1, 504//2)).max()
    lo = prefdivis.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 252d mean times closeadj
def paco_f026_preferred_and_convertible_overhang_rel_252d_base_v101_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 252).replace(0, np.nan)
    result = (prefdivis / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 504d mean times closeadj
def paco_f026_preferred_and_convertible_overhang_rel_504d_base_v102_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 504).replace(0, np.nan)
    result = (prefdivis / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# prefdivis relative to 1008d mean times closeadj
def paco_f026_preferred_and_convertible_overhang_rel_1008d_base_v103_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 1008).replace(0, np.nan)
    result = (prefdivis / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized prefdivis/debtusd 63d mean
def paco_f026_preferred_and_convertible_overhang_sqnorm_debtusd_63d_base_v104_signal(prefdivis, debtusd):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized prefdivis/debtusd 252d mean
def paco_f026_preferred_and_convertible_overhang_sqnorm_debtusd_252d_base_v105_signal(prefdivis, debtusd):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized prefdivis/assets 63d mean
def paco_f026_preferred_and_convertible_overhang_sqnorm_assets_63d_base_v106_signal(prefdivis, assets):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized prefdivis/assets 252d mean
def paco_f026_preferred_and_convertible_overhang_sqnorm_assets_252d_base_v107_signal(prefdivis, assets):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized prefdivis/marketcap 63d mean
def paco_f026_preferred_and_convertible_overhang_sqnorm_marketcap_63d_base_v108_signal(prefdivis, marketcap):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized prefdivis/marketcap 252d mean
def paco_f026_preferred_and_convertible_overhang_sqnorm_marketcap_252d_base_v109_signal(prefdivis, marketcap):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_infrat_63d_base_v110_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 63)
    s = _std(prefdivis, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_infrat_252d_base_v111_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 252)
    s = _std(prefdivis, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_infrat_504d_base_v112_signal(prefdivis, closeadj):
    m = _mean(prefdivis, 504)
    s = _std(prefdivis, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of prefdivis
def paco_f026_preferred_and_convertible_overhang_cv_252d_base_v113_signal(prefdivis):
    m = _mean(prefdivis, 252).abs().replace(0, np.nan)
    s = _std(prefdivis, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of prefdivis
def paco_f026_preferred_and_convertible_overhang_cv_504d_base_v114_signal(prefdivis):
    m = _mean(prefdivis, 504).abs().replace(0, np.nan)
    s = _std(prefdivis, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_5d_base_v115_signal(prefdivis, closeadj):
    result = prefdivis.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_21d_base_v116_signal(prefdivis, closeadj):
    result = prefdivis.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_63d_base_v117_signal(prefdivis, closeadj):
    result = prefdivis.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_252d_base_v118_signal(prefdivis, closeadj):
    result = prefdivis.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(prefdivis) / mean(debtusd) x closeadj
def paco_f026_preferred_and_convertible_overhang_cumper_debtusd_252d_base_v119_signal(prefdivis, debtusd, closeadj):
    s = prefdivis.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(debtusd, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(prefdivis) / mean(debtusd) x closeadj
def paco_f026_preferred_and_convertible_overhang_cumper_debtusd_504d_base_v120_signal(prefdivis, debtusd, closeadj):
    s = prefdivis.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(debtusd, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(prefdivis) / mean(assets) x closeadj
def paco_f026_preferred_and_convertible_overhang_cumper_assets_252d_base_v121_signal(prefdivis, assets, closeadj):
    s = prefdivis.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(prefdivis) / mean(assets) x closeadj
def paco_f026_preferred_and_convertible_overhang_cumper_assets_504d_base_v122_signal(prefdivis, assets, closeadj):
    s = prefdivis.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_pos_63d_base_v123_signal(prefdivis, closeadj):
    pos = prefdivis.where(prefdivis > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_pos_252d_base_v124_signal(prefdivis, closeadj):
    pos = prefdivis.where(prefdivis > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_neg_63d_base_v125_signal(prefdivis, closeadj):
    neg = prefdivis.where(prefdivis < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_neg_252d_base_v126_signal(prefdivis, closeadj):
    neg = prefdivis.where(prefdivis < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_hl_21d_base_v127_signal(prefdivis, closeadj):
    result = prefdivis.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_hl_63d_base_v128_signal(prefdivis, closeadj):
    result = prefdivis.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_hl_252d_base_v129_signal(prefdivis, closeadj):
    result = prefdivis.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of prefdivis
def paco_f026_preferred_and_convertible_overhang_z_63d_base_v130_signal(prefdivis):
    result = _z(prefdivis, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of prefdivis
def paco_f026_preferred_and_convertible_overhang_z_126d_base_v131_signal(prefdivis):
    result = _z(prefdivis, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of prefdivis
def paco_f026_preferred_and_convertible_overhang_z_1008d_base_v132_signal(prefdivis):
    result = _z(prefdivis, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_st_lt_252_21d_base_v133_signal(prefdivis, closeadj):
    sm = _mean(prefdivis, 21)
    lm = _mean(prefdivis, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_st_lt_252_63d_base_v134_signal(prefdivis, closeadj):
    sm = _mean(prefdivis, 63)
    lm = _mean(prefdivis, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_st_lt_504_21d_base_v135_signal(prefdivis, closeadj):
    sm = _mean(prefdivis, 21)
    lm = _mean(prefdivis, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_st_lt_504_63d_base_v136_signal(prefdivis, closeadj):
    sm = _mean(prefdivis, 63)
    lm = _mean(prefdivis, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged prefdivis/debtusd times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_per_debtusd_21d_base_v137_signal(prefdivis, debtusd, closeadj):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged prefdivis/debtusd times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_per_debtusd_63d_base_v138_signal(prefdivis, debtusd, closeadj):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged prefdivis/debtusd times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_per_debtusd_252d_base_v139_signal(prefdivis, debtusd, closeadj):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, debtusd)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged prefdivis/assets times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_per_assets_21d_base_v140_signal(prefdivis, assets, closeadj):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged prefdivis/assets times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_per_assets_63d_base_v141_signal(prefdivis, assets, closeadj):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged prefdivis/assets times closeadj
def paco_f026_preferred_and_convertible_overhang_lag_per_assets_252d_base_v142_signal(prefdivis, assets, closeadj):
    r = _preferred_and_convertible_overhang_scaled(prefdivis, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |prefdivis| times closeadj
def paco_f026_preferred_and_convertible_overhang_abssum_63d_base_v143_signal(prefdivis, closeadj):
    result = prefdivis.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |prefdivis| times closeadj
def paco_f026_preferred_and_convertible_overhang_abssum_252d_base_v144_signal(prefdivis, closeadj):
    result = prefdivis.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |prefdivis| times closeadj
def paco_f026_preferred_and_convertible_overhang_abssum_504d_base_v145_signal(prefdivis, closeadj):
    result = prefdivis.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of prefdivis
def paco_f026_preferred_and_convertible_overhang_acf1_252d_base_v146_signal(prefdivis):
    result = prefdivis.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of prefdivis
def paco_f026_preferred_and_convertible_overhang_acf1_504d_base_v147_signal(prefdivis):
    result = prefdivis.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of prefdivis
def paco_f026_preferred_and_convertible_overhang_posinrange_252d_base_v148_signal(prefdivis):
    m = _mean(prefdivis, 252)
    hi = prefdivis.rolling(252, min_periods=max(1, 252//2)).max()
    lo = prefdivis.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of prefdivis
def paco_f026_preferred_and_convertible_overhang_posinrange_504d_base_v149_signal(prefdivis):
    m = _mean(prefdivis, 504)
    hi = prefdivis.rolling(504, min_periods=max(1, 504//2)).max()
    lo = prefdivis.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of prefdivis times closeadj
def paco_f026_preferred_and_convertible_overhang_hl_5d_base_v150_signal(prefdivis, closeadj):
    result = prefdivis.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
