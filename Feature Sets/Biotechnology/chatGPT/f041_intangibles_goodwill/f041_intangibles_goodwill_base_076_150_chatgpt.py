"""Family f041 - Intangible and goodwill exposure (Balance Sheet Composition) | Sharadar tables: SF1 | fields: intangibles, depamor, assets, equity | base 076-150"""
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
def _intangibles_goodwill_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _intangibles_goodwill_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _intangibles_goodwill_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of intangibles/assets
def ig_f041_intangibles_goodwill_log_per_assets_504d_base_v076_signal(intangibles, assets):
    s = _intangibles_goodwill_scaled(intangibles, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intangibles/equity
def ig_f041_intangibles_goodwill_log_per_equity_252d_base_v077_signal(intangibles, equity):
    s = _intangibles_goodwill_scaled(intangibles, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of intangibles/equity
def ig_f041_intangibles_goodwill_log_per_equity_504d_base_v078_signal(intangibles, equity):
    s = _intangibles_goodwill_scaled(intangibles, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of intangibles times closeadj
def ig_f041_intangibles_goodwill_ewm_21d_base_v079_signal(intangibles, closeadj):
    result = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of intangibles times closeadj
def ig_f041_intangibles_goodwill_ewm_63d_base_v080_signal(intangibles, closeadj):
    result = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of intangibles times closeadj
def ig_f041_intangibles_goodwill_ewm_252d_base_v081_signal(intangibles, closeadj):
    result = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of intangibles times closeadj
def ig_f041_intangibles_goodwill_med_63d_base_v082_signal(intangibles, closeadj):
    result = intangibles.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of intangibles times closeadj
def ig_f041_intangibles_goodwill_med_252d_base_v083_signal(intangibles, closeadj):
    result = intangibles.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of intangibles times closeadj
def ig_f041_intangibles_goodwill_med_504d_base_v084_signal(intangibles, closeadj):
    result = intangibles.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of intangibles
def ig_f041_intangibles_goodwill_skew_252d_base_v085_signal(intangibles):
    result = intangibles.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of intangibles
def ig_f041_intangibles_goodwill_skew_504d_base_v086_signal(intangibles):
    result = intangibles.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of intangibles
def ig_f041_intangibles_goodwill_kurt_252d_base_v087_signal(intangibles):
    result = intangibles.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of intangibles
def ig_f041_intangibles_goodwill_kurt_504d_base_v088_signal(intangibles):
    result = intangibles.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of intangibles times closeadj
def ig_f041_intangibles_goodwill_rank_252d_base_v089_signal(intangibles, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = intangibles.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of intangibles times closeadj
def ig_f041_intangibles_goodwill_rank_504d_base_v090_signal(intangibles, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = intangibles.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of intangibles times closeadj
def ig_f041_intangibles_goodwill_rank_1008d_base_v091_signal(intangibles, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = intangibles.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of intangibles from 63d mean times closeadj
def ig_f041_intangibles_goodwill_devmean_63d_base_v092_signal(intangibles, closeadj):
    m = _mean(intangibles, 63)
    result = (intangibles - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of intangibles from 252d mean times closeadj
def ig_f041_intangibles_goodwill_devmean_252d_base_v093_signal(intangibles, closeadj):
    m = _mean(intangibles, 252)
    result = (intangibles - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of intangibles from 504d mean times closeadj
def ig_f041_intangibles_goodwill_devmean_504d_base_v094_signal(intangibles, closeadj):
    m = _mean(intangibles, 504)
    result = (intangibles - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of intangibles times closeadj
def ig_f041_intangibles_goodwill_logdiff_21d_base_v095_signal(intangibles, closeadj):
    lr = _intangibles_goodwill_log(intangibles)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of intangibles times closeadj
def ig_f041_intangibles_goodwill_logdiff_63d_base_v096_signal(intangibles, closeadj):
    lr = _intangibles_goodwill_log(intangibles)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of intangibles times closeadj
def ig_f041_intangibles_goodwill_logdiff_252d_base_v097_signal(intangibles, closeadj):
    lr = _intangibles_goodwill_log(intangibles)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of intangibles times closeadj
def ig_f041_intangibles_goodwill_range_63d_base_v098_signal(intangibles, closeadj):
    hi = intangibles.rolling(63, min_periods=max(1, 63//2)).max()
    lo = intangibles.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of intangibles times closeadj
def ig_f041_intangibles_goodwill_range_252d_base_v099_signal(intangibles, closeadj):
    hi = intangibles.rolling(252, min_periods=max(1, 252//2)).max()
    lo = intangibles.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of intangibles times closeadj
def ig_f041_intangibles_goodwill_range_504d_base_v100_signal(intangibles, closeadj):
    hi = intangibles.rolling(504, min_periods=max(1, 504//2)).max()
    lo = intangibles.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 252d mean times closeadj
def ig_f041_intangibles_goodwill_rel_252d_base_v101_signal(intangibles, closeadj):
    m = _mean(intangibles, 252).replace(0, np.nan)
    result = (intangibles / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 504d mean times closeadj
def ig_f041_intangibles_goodwill_rel_504d_base_v102_signal(intangibles, closeadj):
    m = _mean(intangibles, 504).replace(0, np.nan)
    result = (intangibles / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles relative to 1008d mean times closeadj
def ig_f041_intangibles_goodwill_rel_1008d_base_v103_signal(intangibles, closeadj):
    m = _mean(intangibles, 1008).replace(0, np.nan)
    result = (intangibles / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intangibles/depamor 63d mean
def ig_f041_intangibles_goodwill_sqnorm_depamor_63d_base_v104_signal(intangibles, depamor):
    r = _intangibles_goodwill_scaled(intangibles, depamor)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intangibles/depamor 252d mean
def ig_f041_intangibles_goodwill_sqnorm_depamor_252d_base_v105_signal(intangibles, depamor):
    r = _intangibles_goodwill_scaled(intangibles, depamor)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intangibles/assets 63d mean
def ig_f041_intangibles_goodwill_sqnorm_assets_63d_base_v106_signal(intangibles, assets):
    r = _intangibles_goodwill_scaled(intangibles, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intangibles/assets 252d mean
def ig_f041_intangibles_goodwill_sqnorm_assets_252d_base_v107_signal(intangibles, assets):
    r = _intangibles_goodwill_scaled(intangibles, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intangibles/equity 63d mean
def ig_f041_intangibles_goodwill_sqnorm_equity_63d_base_v108_signal(intangibles, equity):
    r = _intangibles_goodwill_scaled(intangibles, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intangibles/equity 252d mean
def ig_f041_intangibles_goodwill_sqnorm_equity_252d_base_v109_signal(intangibles, equity):
    r = _intangibles_goodwill_scaled(intangibles, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of intangibles times closeadj
def ig_f041_intangibles_goodwill_infrat_63d_base_v110_signal(intangibles, closeadj):
    m = _mean(intangibles, 63)
    s = _std(intangibles, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of intangibles times closeadj
def ig_f041_intangibles_goodwill_infrat_252d_base_v111_signal(intangibles, closeadj):
    m = _mean(intangibles, 252)
    s = _std(intangibles, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of intangibles times closeadj
def ig_f041_intangibles_goodwill_infrat_504d_base_v112_signal(intangibles, closeadj):
    m = _mean(intangibles, 504)
    s = _std(intangibles, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of intangibles
def ig_f041_intangibles_goodwill_cv_252d_base_v113_signal(intangibles):
    m = _mean(intangibles, 252).abs().replace(0, np.nan)
    s = _std(intangibles, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of intangibles
def ig_f041_intangibles_goodwill_cv_504d_base_v114_signal(intangibles):
    m = _mean(intangibles, 504).abs().replace(0, np.nan)
    s = _std(intangibles, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged intangibles times closeadj
def ig_f041_intangibles_goodwill_lag_5d_base_v115_signal(intangibles, closeadj):
    result = intangibles.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged intangibles times closeadj
def ig_f041_intangibles_goodwill_lag_21d_base_v116_signal(intangibles, closeadj):
    result = intangibles.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged intangibles times closeadj
def ig_f041_intangibles_goodwill_lag_63d_base_v117_signal(intangibles, closeadj):
    result = intangibles.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged intangibles times closeadj
def ig_f041_intangibles_goodwill_lag_252d_base_v118_signal(intangibles, closeadj):
    result = intangibles.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(intangibles) / mean(depamor) x closeadj
def ig_f041_intangibles_goodwill_cumper_depamor_252d_base_v119_signal(intangibles, depamor, closeadj):
    s = intangibles.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(depamor, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(intangibles) / mean(depamor) x closeadj
def ig_f041_intangibles_goodwill_cumper_depamor_504d_base_v120_signal(intangibles, depamor, closeadj):
    s = intangibles.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(depamor, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(intangibles) / mean(assets) x closeadj
def ig_f041_intangibles_goodwill_cumper_assets_252d_base_v121_signal(intangibles, assets, closeadj):
    s = intangibles.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(intangibles) / mean(assets) x closeadj
def ig_f041_intangibles_goodwill_cumper_assets_504d_base_v122_signal(intangibles, assets, closeadj):
    s = intangibles.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only intangibles times closeadj
def ig_f041_intangibles_goodwill_pos_63d_base_v123_signal(intangibles, closeadj):
    pos = intangibles.where(intangibles > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only intangibles times closeadj
def ig_f041_intangibles_goodwill_pos_252d_base_v124_signal(intangibles, closeadj):
    pos = intangibles.where(intangibles > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only intangibles times closeadj
def ig_f041_intangibles_goodwill_neg_63d_base_v125_signal(intangibles, closeadj):
    neg = intangibles.where(intangibles < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only intangibles times closeadj
def ig_f041_intangibles_goodwill_neg_252d_base_v126_signal(intangibles, closeadj):
    neg = intangibles.where(intangibles < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of intangibles times closeadj
def ig_f041_intangibles_goodwill_hl_21d_base_v127_signal(intangibles, closeadj):
    result = intangibles.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of intangibles times closeadj
def ig_f041_intangibles_goodwill_hl_63d_base_v128_signal(intangibles, closeadj):
    result = intangibles.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of intangibles times closeadj
def ig_f041_intangibles_goodwill_hl_252d_base_v129_signal(intangibles, closeadj):
    result = intangibles.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of intangibles
def ig_f041_intangibles_goodwill_z_63d_base_v130_signal(intangibles):
    result = _z(intangibles, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of intangibles
def ig_f041_intangibles_goodwill_z_126d_base_v131_signal(intangibles):
    result = _z(intangibles, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of intangibles
def ig_f041_intangibles_goodwill_z_1008d_base_v132_signal(intangibles):
    result = _z(intangibles, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of intangibles times closeadj
def ig_f041_intangibles_goodwill_st_lt_252_21d_base_v133_signal(intangibles, closeadj):
    sm = _mean(intangibles, 21)
    lm = _mean(intangibles, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of intangibles times closeadj
def ig_f041_intangibles_goodwill_st_lt_252_63d_base_v134_signal(intangibles, closeadj):
    sm = _mean(intangibles, 63)
    lm = _mean(intangibles, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of intangibles times closeadj
def ig_f041_intangibles_goodwill_st_lt_504_21d_base_v135_signal(intangibles, closeadj):
    sm = _mean(intangibles, 21)
    lm = _mean(intangibles, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of intangibles times closeadj
def ig_f041_intangibles_goodwill_st_lt_504_63d_base_v136_signal(intangibles, closeadj):
    sm = _mean(intangibles, 63)
    lm = _mean(intangibles, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged intangibles/depamor times closeadj
def ig_f041_intangibles_goodwill_lag_per_depamor_21d_base_v137_signal(intangibles, depamor, closeadj):
    r = _intangibles_goodwill_scaled(intangibles, depamor)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged intangibles/depamor times closeadj
def ig_f041_intangibles_goodwill_lag_per_depamor_63d_base_v138_signal(intangibles, depamor, closeadj):
    r = _intangibles_goodwill_scaled(intangibles, depamor)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged intangibles/depamor times closeadj
def ig_f041_intangibles_goodwill_lag_per_depamor_252d_base_v139_signal(intangibles, depamor, closeadj):
    r = _intangibles_goodwill_scaled(intangibles, depamor)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged intangibles/assets times closeadj
def ig_f041_intangibles_goodwill_lag_per_assets_21d_base_v140_signal(intangibles, assets, closeadj):
    r = _intangibles_goodwill_scaled(intangibles, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged intangibles/assets times closeadj
def ig_f041_intangibles_goodwill_lag_per_assets_63d_base_v141_signal(intangibles, assets, closeadj):
    r = _intangibles_goodwill_scaled(intangibles, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged intangibles/assets times closeadj
def ig_f041_intangibles_goodwill_lag_per_assets_252d_base_v142_signal(intangibles, assets, closeadj):
    r = _intangibles_goodwill_scaled(intangibles, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |intangibles| times closeadj
def ig_f041_intangibles_goodwill_abssum_63d_base_v143_signal(intangibles, closeadj):
    result = intangibles.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |intangibles| times closeadj
def ig_f041_intangibles_goodwill_abssum_252d_base_v144_signal(intangibles, closeadj):
    result = intangibles.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |intangibles| times closeadj
def ig_f041_intangibles_goodwill_abssum_504d_base_v145_signal(intangibles, closeadj):
    result = intangibles.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of intangibles
def ig_f041_intangibles_goodwill_acf1_252d_base_v146_signal(intangibles):
    result = intangibles.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of intangibles
def ig_f041_intangibles_goodwill_acf1_504d_base_v147_signal(intangibles):
    result = intangibles.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of intangibles
def ig_f041_intangibles_goodwill_posinrange_252d_base_v148_signal(intangibles):
    m = _mean(intangibles, 252)
    hi = intangibles.rolling(252, min_periods=max(1, 252//2)).max()
    lo = intangibles.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of intangibles
def ig_f041_intangibles_goodwill_posinrange_504d_base_v149_signal(intangibles):
    m = _mean(intangibles, 504)
    hi = intangibles.rolling(504, min_periods=max(1, 504//2)).max()
    lo = intangibles.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of intangibles times closeadj
def ig_f041_intangibles_goodwill_hl_5d_base_v150_signal(intangibles, closeadj):
    result = intangibles.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
