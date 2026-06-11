"""Family f060 - Non-cash expense composition (Earnings and Quality) | Sharadar tables: SF1 | fields: depamor, sbcomp, netinc, opex | base 076-150"""
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
def _non_cash_expense_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _non_cash_expense_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _non_cash_expense_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of depamor/netinc
def ncem_f060_non_cash_expense_mix_log_per_netinc_504d_base_v076_signal(depamor, netinc):
    s = _non_cash_expense_mix_scaled(depamor, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of depamor/assets
def ncem_f060_non_cash_expense_mix_log_per_assets_252d_base_v077_signal(depamor, assets):
    s = _non_cash_expense_mix_scaled(depamor, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of depamor/assets
def ncem_f060_non_cash_expense_mix_log_per_assets_504d_base_v078_signal(depamor, assets):
    s = _non_cash_expense_mix_scaled(depamor, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of depamor times closeadj
def ncem_f060_non_cash_expense_mix_ewm_21d_base_v079_signal(depamor, closeadj):
    result = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of depamor times closeadj
def ncem_f060_non_cash_expense_mix_ewm_63d_base_v080_signal(depamor, closeadj):
    result = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of depamor times closeadj
def ncem_f060_non_cash_expense_mix_ewm_252d_base_v081_signal(depamor, closeadj):
    result = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of depamor times closeadj
def ncem_f060_non_cash_expense_mix_med_63d_base_v082_signal(depamor, closeadj):
    result = depamor.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of depamor times closeadj
def ncem_f060_non_cash_expense_mix_med_252d_base_v083_signal(depamor, closeadj):
    result = depamor.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of depamor times closeadj
def ncem_f060_non_cash_expense_mix_med_504d_base_v084_signal(depamor, closeadj):
    result = depamor.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of depamor
def ncem_f060_non_cash_expense_mix_skew_252d_base_v085_signal(depamor):
    result = depamor.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of depamor
def ncem_f060_non_cash_expense_mix_skew_504d_base_v086_signal(depamor):
    result = depamor.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of depamor
def ncem_f060_non_cash_expense_mix_kurt_252d_base_v087_signal(depamor):
    result = depamor.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of depamor
def ncem_f060_non_cash_expense_mix_kurt_504d_base_v088_signal(depamor):
    result = depamor.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of depamor times closeadj
def ncem_f060_non_cash_expense_mix_rank_252d_base_v089_signal(depamor, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = depamor.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of depamor times closeadj
def ncem_f060_non_cash_expense_mix_rank_504d_base_v090_signal(depamor, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = depamor.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of depamor times closeadj
def ncem_f060_non_cash_expense_mix_rank_1008d_base_v091_signal(depamor, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = depamor.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of depamor from 63d mean times closeadj
def ncem_f060_non_cash_expense_mix_devmean_63d_base_v092_signal(depamor, closeadj):
    m = _mean(depamor, 63)
    result = (depamor - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of depamor from 252d mean times closeadj
def ncem_f060_non_cash_expense_mix_devmean_252d_base_v093_signal(depamor, closeadj):
    m = _mean(depamor, 252)
    result = (depamor - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of depamor from 504d mean times closeadj
def ncem_f060_non_cash_expense_mix_devmean_504d_base_v094_signal(depamor, closeadj):
    m = _mean(depamor, 504)
    result = (depamor - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of depamor times closeadj
def ncem_f060_non_cash_expense_mix_logdiff_21d_base_v095_signal(depamor, closeadj):
    lr = _non_cash_expense_mix_log(depamor)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of depamor times closeadj
def ncem_f060_non_cash_expense_mix_logdiff_63d_base_v096_signal(depamor, closeadj):
    lr = _non_cash_expense_mix_log(depamor)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of depamor times closeadj
def ncem_f060_non_cash_expense_mix_logdiff_252d_base_v097_signal(depamor, closeadj):
    lr = _non_cash_expense_mix_log(depamor)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of depamor times closeadj
def ncem_f060_non_cash_expense_mix_range_63d_base_v098_signal(depamor, closeadj):
    hi = depamor.rolling(63, min_periods=max(1, 63//2)).max()
    lo = depamor.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of depamor times closeadj
def ncem_f060_non_cash_expense_mix_range_252d_base_v099_signal(depamor, closeadj):
    hi = depamor.rolling(252, min_periods=max(1, 252//2)).max()
    lo = depamor.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of depamor times closeadj
def ncem_f060_non_cash_expense_mix_range_504d_base_v100_signal(depamor, closeadj):
    hi = depamor.rolling(504, min_periods=max(1, 504//2)).max()
    lo = depamor.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 252d mean times closeadj
def ncem_f060_non_cash_expense_mix_rel_252d_base_v101_signal(depamor, closeadj):
    m = _mean(depamor, 252).replace(0, np.nan)
    result = (depamor / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 504d mean times closeadj
def ncem_f060_non_cash_expense_mix_rel_504d_base_v102_signal(depamor, closeadj):
    m = _mean(depamor, 504).replace(0, np.nan)
    result = (depamor / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 1008d mean times closeadj
def ncem_f060_non_cash_expense_mix_rel_1008d_base_v103_signal(depamor, closeadj):
    m = _mean(depamor, 1008).replace(0, np.nan)
    result = (depamor / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized depamor/sbcomp 63d mean
def ncem_f060_non_cash_expense_mix_sqnorm_sbcomp_63d_base_v104_signal(depamor, sbcomp):
    r = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized depamor/sbcomp 252d mean
def ncem_f060_non_cash_expense_mix_sqnorm_sbcomp_252d_base_v105_signal(depamor, sbcomp):
    r = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized depamor/netinc 63d mean
def ncem_f060_non_cash_expense_mix_sqnorm_netinc_63d_base_v106_signal(depamor, netinc):
    r = _non_cash_expense_mix_scaled(depamor, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized depamor/netinc 252d mean
def ncem_f060_non_cash_expense_mix_sqnorm_netinc_252d_base_v107_signal(depamor, netinc):
    r = _non_cash_expense_mix_scaled(depamor, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized depamor/assets 63d mean
def ncem_f060_non_cash_expense_mix_sqnorm_assets_63d_base_v108_signal(depamor, assets):
    r = _non_cash_expense_mix_scaled(depamor, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized depamor/assets 252d mean
def ncem_f060_non_cash_expense_mix_sqnorm_assets_252d_base_v109_signal(depamor, assets):
    r = _non_cash_expense_mix_scaled(depamor, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of depamor times closeadj
def ncem_f060_non_cash_expense_mix_infrat_63d_base_v110_signal(depamor, closeadj):
    m = _mean(depamor, 63)
    s = _std(depamor, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of depamor times closeadj
def ncem_f060_non_cash_expense_mix_infrat_252d_base_v111_signal(depamor, closeadj):
    m = _mean(depamor, 252)
    s = _std(depamor, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of depamor times closeadj
def ncem_f060_non_cash_expense_mix_infrat_504d_base_v112_signal(depamor, closeadj):
    m = _mean(depamor, 504)
    s = _std(depamor, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of depamor
def ncem_f060_non_cash_expense_mix_cv_252d_base_v113_signal(depamor):
    m = _mean(depamor, 252).abs().replace(0, np.nan)
    s = _std(depamor, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of depamor
def ncem_f060_non_cash_expense_mix_cv_504d_base_v114_signal(depamor):
    m = _mean(depamor, 504).abs().replace(0, np.nan)
    s = _std(depamor, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged depamor times closeadj
def ncem_f060_non_cash_expense_mix_lag_5d_base_v115_signal(depamor, closeadj):
    result = depamor.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged depamor times closeadj
def ncem_f060_non_cash_expense_mix_lag_21d_base_v116_signal(depamor, closeadj):
    result = depamor.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged depamor times closeadj
def ncem_f060_non_cash_expense_mix_lag_63d_base_v117_signal(depamor, closeadj):
    result = depamor.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged depamor times closeadj
def ncem_f060_non_cash_expense_mix_lag_252d_base_v118_signal(depamor, closeadj):
    result = depamor.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(depamor) / mean(sbcomp) x closeadj
def ncem_f060_non_cash_expense_mix_cumper_sbcomp_252d_base_v119_signal(depamor, sbcomp, closeadj):
    s = depamor.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(sbcomp, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(depamor) / mean(sbcomp) x closeadj
def ncem_f060_non_cash_expense_mix_cumper_sbcomp_504d_base_v120_signal(depamor, sbcomp, closeadj):
    s = depamor.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(sbcomp, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(depamor) / mean(netinc) x closeadj
def ncem_f060_non_cash_expense_mix_cumper_netinc_252d_base_v121_signal(depamor, netinc, closeadj):
    s = depamor.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(depamor) / mean(netinc) x closeadj
def ncem_f060_non_cash_expense_mix_cumper_netinc_504d_base_v122_signal(depamor, netinc, closeadj):
    s = depamor.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only depamor times closeadj
def ncem_f060_non_cash_expense_mix_pos_63d_base_v123_signal(depamor, closeadj):
    pos = depamor.where(depamor > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only depamor times closeadj
def ncem_f060_non_cash_expense_mix_pos_252d_base_v124_signal(depamor, closeadj):
    pos = depamor.where(depamor > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only depamor times closeadj
def ncem_f060_non_cash_expense_mix_neg_63d_base_v125_signal(depamor, closeadj):
    neg = depamor.where(depamor < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only depamor times closeadj
def ncem_f060_non_cash_expense_mix_neg_252d_base_v126_signal(depamor, closeadj):
    neg = depamor.where(depamor < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of depamor times closeadj
def ncem_f060_non_cash_expense_mix_hl_21d_base_v127_signal(depamor, closeadj):
    result = depamor.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of depamor times closeadj
def ncem_f060_non_cash_expense_mix_hl_63d_base_v128_signal(depamor, closeadj):
    result = depamor.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of depamor times closeadj
def ncem_f060_non_cash_expense_mix_hl_252d_base_v129_signal(depamor, closeadj):
    result = depamor.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of depamor
def ncem_f060_non_cash_expense_mix_z_63d_base_v130_signal(depamor):
    result = _z(depamor, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of depamor
def ncem_f060_non_cash_expense_mix_z_126d_base_v131_signal(depamor):
    result = _z(depamor, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of depamor
def ncem_f060_non_cash_expense_mix_z_1008d_base_v132_signal(depamor):
    result = _z(depamor, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of depamor times closeadj
def ncem_f060_non_cash_expense_mix_st_lt_252_21d_base_v133_signal(depamor, closeadj):
    sm = _mean(depamor, 21)
    lm = _mean(depamor, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of depamor times closeadj
def ncem_f060_non_cash_expense_mix_st_lt_252_63d_base_v134_signal(depamor, closeadj):
    sm = _mean(depamor, 63)
    lm = _mean(depamor, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of depamor times closeadj
def ncem_f060_non_cash_expense_mix_st_lt_504_21d_base_v135_signal(depamor, closeadj):
    sm = _mean(depamor, 21)
    lm = _mean(depamor, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of depamor times closeadj
def ncem_f060_non_cash_expense_mix_st_lt_504_63d_base_v136_signal(depamor, closeadj):
    sm = _mean(depamor, 63)
    lm = _mean(depamor, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged depamor/sbcomp times closeadj
def ncem_f060_non_cash_expense_mix_lag_per_sbcomp_21d_base_v137_signal(depamor, sbcomp, closeadj):
    r = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged depamor/sbcomp times closeadj
def ncem_f060_non_cash_expense_mix_lag_per_sbcomp_63d_base_v138_signal(depamor, sbcomp, closeadj):
    r = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged depamor/sbcomp times closeadj
def ncem_f060_non_cash_expense_mix_lag_per_sbcomp_252d_base_v139_signal(depamor, sbcomp, closeadj):
    r = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged depamor/netinc times closeadj
def ncem_f060_non_cash_expense_mix_lag_per_netinc_21d_base_v140_signal(depamor, netinc, closeadj):
    r = _non_cash_expense_mix_scaled(depamor, netinc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged depamor/netinc times closeadj
def ncem_f060_non_cash_expense_mix_lag_per_netinc_63d_base_v141_signal(depamor, netinc, closeadj):
    r = _non_cash_expense_mix_scaled(depamor, netinc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged depamor/netinc times closeadj
def ncem_f060_non_cash_expense_mix_lag_per_netinc_252d_base_v142_signal(depamor, netinc, closeadj):
    r = _non_cash_expense_mix_scaled(depamor, netinc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |depamor| times closeadj
def ncem_f060_non_cash_expense_mix_abssum_63d_base_v143_signal(depamor, closeadj):
    result = depamor.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |depamor| times closeadj
def ncem_f060_non_cash_expense_mix_abssum_252d_base_v144_signal(depamor, closeadj):
    result = depamor.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |depamor| times closeadj
def ncem_f060_non_cash_expense_mix_abssum_504d_base_v145_signal(depamor, closeadj):
    result = depamor.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of depamor
def ncem_f060_non_cash_expense_mix_acf1_252d_base_v146_signal(depamor):
    result = depamor.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of depamor
def ncem_f060_non_cash_expense_mix_acf1_504d_base_v147_signal(depamor):
    result = depamor.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of depamor
def ncem_f060_non_cash_expense_mix_posinrange_252d_base_v148_signal(depamor):
    m = _mean(depamor, 252)
    hi = depamor.rolling(252, min_periods=max(1, 252//2)).max()
    lo = depamor.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of depamor
def ncem_f060_non_cash_expense_mix_posinrange_504d_base_v149_signal(depamor):
    m = _mean(depamor, 504)
    hi = depamor.rolling(504, min_periods=max(1, 504//2)).max()
    lo = depamor.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of depamor times closeadj
def ncem_f060_non_cash_expense_mix_hl_5d_base_v150_signal(depamor, closeadj):
    result = depamor.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
