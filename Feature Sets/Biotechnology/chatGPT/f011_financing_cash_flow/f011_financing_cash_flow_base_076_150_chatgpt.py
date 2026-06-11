"""Family f011 - Capital raised through financing (Cash Flow and Burn) | Sharadar tables: SF1 | fields: ncff, ncfcommon, ncfdebt, ncfi | base 076-150"""
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
def _financing_cash_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _financing_cash_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _financing_cash_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ncff/ncfdebt
def fcf_f011_financing_cash_flow_log_per_ncfdebt_504d_base_v076_signal(ncff, ncfdebt):
    s = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncff/ncfi
def fcf_f011_financing_cash_flow_log_per_ncfi_252d_base_v077_signal(ncff, ncfi):
    s = _financing_cash_flow_scaled(ncff, ncfi)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncff/ncfi
def fcf_f011_financing_cash_flow_log_per_ncfi_504d_base_v078_signal(ncff, ncfi):
    s = _financing_cash_flow_scaled(ncff, ncfi)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ncff times closeadj
def fcf_f011_financing_cash_flow_ewm_21d_base_v079_signal(ncff, closeadj):
    result = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ncff times closeadj
def fcf_f011_financing_cash_flow_ewm_63d_base_v080_signal(ncff, closeadj):
    result = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ncff times closeadj
def fcf_f011_financing_cash_flow_ewm_252d_base_v081_signal(ncff, closeadj):
    result = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ncff times closeadj
def fcf_f011_financing_cash_flow_med_63d_base_v082_signal(ncff, closeadj):
    result = ncff.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ncff times closeadj
def fcf_f011_financing_cash_flow_med_252d_base_v083_signal(ncff, closeadj):
    result = ncff.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ncff times closeadj
def fcf_f011_financing_cash_flow_med_504d_base_v084_signal(ncff, closeadj):
    result = ncff.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ncff
def fcf_f011_financing_cash_flow_skew_252d_base_v085_signal(ncff):
    result = ncff.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ncff
def fcf_f011_financing_cash_flow_skew_504d_base_v086_signal(ncff):
    result = ncff.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ncff
def fcf_f011_financing_cash_flow_kurt_252d_base_v087_signal(ncff):
    result = ncff.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ncff
def fcf_f011_financing_cash_flow_kurt_504d_base_v088_signal(ncff):
    result = ncff.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ncff times closeadj
def fcf_f011_financing_cash_flow_rank_252d_base_v089_signal(ncff, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncff.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ncff times closeadj
def fcf_f011_financing_cash_flow_rank_504d_base_v090_signal(ncff, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncff.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ncff times closeadj
def fcf_f011_financing_cash_flow_rank_1008d_base_v091_signal(ncff, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncff.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncff from 63d mean times closeadj
def fcf_f011_financing_cash_flow_devmean_63d_base_v092_signal(ncff, closeadj):
    m = _mean(ncff, 63)
    result = (ncff - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncff from 252d mean times closeadj
def fcf_f011_financing_cash_flow_devmean_252d_base_v093_signal(ncff, closeadj):
    m = _mean(ncff, 252)
    result = (ncff - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncff from 504d mean times closeadj
def fcf_f011_financing_cash_flow_devmean_504d_base_v094_signal(ncff, closeadj):
    m = _mean(ncff, 504)
    result = (ncff - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ncff times closeadj
def fcf_f011_financing_cash_flow_logdiff_21d_base_v095_signal(ncff, closeadj):
    lr = _financing_cash_flow_log(ncff)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ncff times closeadj
def fcf_f011_financing_cash_flow_logdiff_63d_base_v096_signal(ncff, closeadj):
    lr = _financing_cash_flow_log(ncff)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ncff times closeadj
def fcf_f011_financing_cash_flow_logdiff_252d_base_v097_signal(ncff, closeadj):
    lr = _financing_cash_flow_log(ncff)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ncff times closeadj
def fcf_f011_financing_cash_flow_range_63d_base_v098_signal(ncff, closeadj):
    hi = ncff.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ncff.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ncff times closeadj
def fcf_f011_financing_cash_flow_range_252d_base_v099_signal(ncff, closeadj):
    hi = ncff.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncff.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ncff times closeadj
def fcf_f011_financing_cash_flow_range_504d_base_v100_signal(ncff, closeadj):
    hi = ncff.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncff.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 252d mean times closeadj
def fcf_f011_financing_cash_flow_rel_252d_base_v101_signal(ncff, closeadj):
    m = _mean(ncff, 252).replace(0, np.nan)
    result = (ncff / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 504d mean times closeadj
def fcf_f011_financing_cash_flow_rel_504d_base_v102_signal(ncff, closeadj):
    m = _mean(ncff, 504).replace(0, np.nan)
    result = (ncff / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 1008d mean times closeadj
def fcf_f011_financing_cash_flow_rel_1008d_base_v103_signal(ncff, closeadj):
    m = _mean(ncff, 1008).replace(0, np.nan)
    result = (ncff / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncff/ncfcommon 63d mean
def fcf_f011_financing_cash_flow_sqnorm_ncfcommon_63d_base_v104_signal(ncff, ncfcommon):
    r = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncff/ncfcommon 252d mean
def fcf_f011_financing_cash_flow_sqnorm_ncfcommon_252d_base_v105_signal(ncff, ncfcommon):
    r = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncff/ncfdebt 63d mean
def fcf_f011_financing_cash_flow_sqnorm_ncfdebt_63d_base_v106_signal(ncff, ncfdebt):
    r = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncff/ncfdebt 252d mean
def fcf_f011_financing_cash_flow_sqnorm_ncfdebt_252d_base_v107_signal(ncff, ncfdebt):
    r = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncff/ncfi 63d mean
def fcf_f011_financing_cash_flow_sqnorm_ncfi_63d_base_v108_signal(ncff, ncfi):
    r = _financing_cash_flow_scaled(ncff, ncfi)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncff/ncfi 252d mean
def fcf_f011_financing_cash_flow_sqnorm_ncfi_252d_base_v109_signal(ncff, ncfi):
    r = _financing_cash_flow_scaled(ncff, ncfi)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ncff times closeadj
def fcf_f011_financing_cash_flow_infrat_63d_base_v110_signal(ncff, closeadj):
    m = _mean(ncff, 63)
    s = _std(ncff, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ncff times closeadj
def fcf_f011_financing_cash_flow_infrat_252d_base_v111_signal(ncff, closeadj):
    m = _mean(ncff, 252)
    s = _std(ncff, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ncff times closeadj
def fcf_f011_financing_cash_flow_infrat_504d_base_v112_signal(ncff, closeadj):
    m = _mean(ncff, 504)
    s = _std(ncff, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ncff
def fcf_f011_financing_cash_flow_cv_252d_base_v113_signal(ncff):
    m = _mean(ncff, 252).abs().replace(0, np.nan)
    s = _std(ncff, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ncff
def fcf_f011_financing_cash_flow_cv_504d_base_v114_signal(ncff):
    m = _mean(ncff, 504).abs().replace(0, np.nan)
    s = _std(ncff, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ncff times closeadj
def fcf_f011_financing_cash_flow_lag_5d_base_v115_signal(ncff, closeadj):
    result = ncff.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncff times closeadj
def fcf_f011_financing_cash_flow_lag_21d_base_v116_signal(ncff, closeadj):
    result = ncff.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncff times closeadj
def fcf_f011_financing_cash_flow_lag_63d_base_v117_signal(ncff, closeadj):
    result = ncff.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncff times closeadj
def fcf_f011_financing_cash_flow_lag_252d_base_v118_signal(ncff, closeadj):
    result = ncff.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncff) / mean(ncfcommon) x closeadj
def fcf_f011_financing_cash_flow_cumper_ncfcommon_252d_base_v119_signal(ncff, ncfcommon, closeadj):
    s = ncff.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ncfcommon, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncff) / mean(ncfcommon) x closeadj
def fcf_f011_financing_cash_flow_cumper_ncfcommon_504d_base_v120_signal(ncff, ncfcommon, closeadj):
    s = ncff.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ncfcommon, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncff) / mean(ncfdebt) x closeadj
def fcf_f011_financing_cash_flow_cumper_ncfdebt_252d_base_v121_signal(ncff, ncfdebt, closeadj):
    s = ncff.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ncfdebt, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncff) / mean(ncfdebt) x closeadj
def fcf_f011_financing_cash_flow_cumper_ncfdebt_504d_base_v122_signal(ncff, ncfdebt, closeadj):
    s = ncff.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ncfdebt, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ncff times closeadj
def fcf_f011_financing_cash_flow_pos_63d_base_v123_signal(ncff, closeadj):
    pos = ncff.where(ncff > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ncff times closeadj
def fcf_f011_financing_cash_flow_pos_252d_base_v124_signal(ncff, closeadj):
    pos = ncff.where(ncff > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ncff times closeadj
def fcf_f011_financing_cash_flow_neg_63d_base_v125_signal(ncff, closeadj):
    neg = ncff.where(ncff < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ncff times closeadj
def fcf_f011_financing_cash_flow_neg_252d_base_v126_signal(ncff, closeadj):
    neg = ncff.where(ncff < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ncff times closeadj
def fcf_f011_financing_cash_flow_hl_21d_base_v127_signal(ncff, closeadj):
    result = ncff.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ncff times closeadj
def fcf_f011_financing_cash_flow_hl_63d_base_v128_signal(ncff, closeadj):
    result = ncff.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ncff times closeadj
def fcf_f011_financing_cash_flow_hl_252d_base_v129_signal(ncff, closeadj):
    result = ncff.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ncff
def fcf_f011_financing_cash_flow_z_63d_base_v130_signal(ncff):
    result = _z(ncff, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ncff
def fcf_f011_financing_cash_flow_z_126d_base_v131_signal(ncff):
    result = _z(ncff, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ncff
def fcf_f011_financing_cash_flow_z_1008d_base_v132_signal(ncff):
    result = _z(ncff, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ncff times closeadj
def fcf_f011_financing_cash_flow_st_lt_252_21d_base_v133_signal(ncff, closeadj):
    sm = _mean(ncff, 21)
    lm = _mean(ncff, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ncff times closeadj
def fcf_f011_financing_cash_flow_st_lt_252_63d_base_v134_signal(ncff, closeadj):
    sm = _mean(ncff, 63)
    lm = _mean(ncff, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ncff times closeadj
def fcf_f011_financing_cash_flow_st_lt_504_21d_base_v135_signal(ncff, closeadj):
    sm = _mean(ncff, 21)
    lm = _mean(ncff, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ncff times closeadj
def fcf_f011_financing_cash_flow_st_lt_504_63d_base_v136_signal(ncff, closeadj):
    sm = _mean(ncff, 63)
    lm = _mean(ncff, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncff/ncfcommon times closeadj
def fcf_f011_financing_cash_flow_lag_per_ncfcommon_21d_base_v137_signal(ncff, ncfcommon, closeadj):
    r = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncff/ncfcommon times closeadj
def fcf_f011_financing_cash_flow_lag_per_ncfcommon_63d_base_v138_signal(ncff, ncfcommon, closeadj):
    r = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncff/ncfcommon times closeadj
def fcf_f011_financing_cash_flow_lag_per_ncfcommon_252d_base_v139_signal(ncff, ncfcommon, closeadj):
    r = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncff/ncfdebt times closeadj
def fcf_f011_financing_cash_flow_lag_per_ncfdebt_21d_base_v140_signal(ncff, ncfdebt, closeadj):
    r = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncff/ncfdebt times closeadj
def fcf_f011_financing_cash_flow_lag_per_ncfdebt_63d_base_v141_signal(ncff, ncfdebt, closeadj):
    r = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncff/ncfdebt times closeadj
def fcf_f011_financing_cash_flow_lag_per_ncfdebt_252d_base_v142_signal(ncff, ncfdebt, closeadj):
    r = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ncff| times closeadj
def fcf_f011_financing_cash_flow_abssum_63d_base_v143_signal(ncff, closeadj):
    result = ncff.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ncff| times closeadj
def fcf_f011_financing_cash_flow_abssum_252d_base_v144_signal(ncff, closeadj):
    result = ncff.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ncff| times closeadj
def fcf_f011_financing_cash_flow_abssum_504d_base_v145_signal(ncff, closeadj):
    result = ncff.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ncff
def fcf_f011_financing_cash_flow_acf1_252d_base_v146_signal(ncff):
    result = ncff.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ncff
def fcf_f011_financing_cash_flow_acf1_504d_base_v147_signal(ncff):
    result = ncff.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ncff
def fcf_f011_financing_cash_flow_posinrange_252d_base_v148_signal(ncff):
    m = _mean(ncff, 252)
    hi = ncff.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncff.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ncff
def fcf_f011_financing_cash_flow_posinrange_504d_base_v149_signal(ncff):
    m = _mean(ncff, 504)
    hi = ncff.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncff.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ncff times closeadj
def fcf_f011_financing_cash_flow_hl_5d_base_v150_signal(ncff, closeadj):
    result = ncff.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
