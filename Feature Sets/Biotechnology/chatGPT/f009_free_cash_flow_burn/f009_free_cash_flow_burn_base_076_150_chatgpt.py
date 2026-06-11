"""Family f009 - Free cash flow burn (Cash Flow and Burn) | Sharadar tables: SF1 | fields: fcf, fcfps, ncfo, capex | base 076-150"""
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
def _free_cash_flow_burn_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _free_cash_flow_burn_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _free_cash_flow_burn_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of fcf/ncfo
def fcfb_f009_free_cash_flow_burn_log_per_ncfo_504d_base_v076_signal(fcf, ncfo):
    s = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of fcf/assets
def fcfb_f009_free_cash_flow_burn_log_per_assets_252d_base_v077_signal(fcf, assets):
    s = _free_cash_flow_burn_scaled(fcf, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of fcf/assets
def fcfb_f009_free_cash_flow_burn_log_per_assets_504d_base_v078_signal(fcf, assets):
    s = _free_cash_flow_burn_scaled(fcf, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_ewm_21d_base_v079_signal(fcf, closeadj):
    result = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_ewm_63d_base_v080_signal(fcf, closeadj):
    result = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_ewm_252d_base_v081_signal(fcf, closeadj):
    result = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_med_63d_base_v082_signal(fcf, closeadj):
    result = fcf.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_med_252d_base_v083_signal(fcf, closeadj):
    result = fcf.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_med_504d_base_v084_signal(fcf, closeadj):
    result = fcf.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of fcf
def fcfb_f009_free_cash_flow_burn_skew_252d_base_v085_signal(fcf):
    result = fcf.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of fcf
def fcfb_f009_free_cash_flow_burn_skew_504d_base_v086_signal(fcf):
    result = fcf.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of fcf
def fcfb_f009_free_cash_flow_burn_kurt_252d_base_v087_signal(fcf):
    result = fcf.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of fcf
def fcfb_f009_free_cash_flow_burn_kurt_504d_base_v088_signal(fcf):
    result = fcf.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_rank_252d_base_v089_signal(fcf, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = fcf.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_rank_504d_base_v090_signal(fcf, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = fcf.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_rank_1008d_base_v091_signal(fcf, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = fcf.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of fcf from 63d mean times closeadj
def fcfb_f009_free_cash_flow_burn_devmean_63d_base_v092_signal(fcf, closeadj):
    m = _mean(fcf, 63)
    result = (fcf - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of fcf from 252d mean times closeadj
def fcfb_f009_free_cash_flow_burn_devmean_252d_base_v093_signal(fcf, closeadj):
    m = _mean(fcf, 252)
    result = (fcf - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of fcf from 504d mean times closeadj
def fcfb_f009_free_cash_flow_burn_devmean_504d_base_v094_signal(fcf, closeadj):
    m = _mean(fcf, 504)
    result = (fcf - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_logdiff_21d_base_v095_signal(fcf, closeadj):
    lr = _free_cash_flow_burn_log(fcf)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_logdiff_63d_base_v096_signal(fcf, closeadj):
    lr = _free_cash_flow_burn_log(fcf)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_logdiff_252d_base_v097_signal(fcf, closeadj):
    lr = _free_cash_flow_burn_log(fcf)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_range_63d_base_v098_signal(fcf, closeadj):
    hi = fcf.rolling(63, min_periods=max(1, 63//2)).max()
    lo = fcf.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_range_252d_base_v099_signal(fcf, closeadj):
    hi = fcf.rolling(252, min_periods=max(1, 252//2)).max()
    lo = fcf.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_range_504d_base_v100_signal(fcf, closeadj):
    hi = fcf.rolling(504, min_periods=max(1, 504//2)).max()
    lo = fcf.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 252d mean times closeadj
def fcfb_f009_free_cash_flow_burn_rel_252d_base_v101_signal(fcf, closeadj):
    m = _mean(fcf, 252).replace(0, np.nan)
    result = (fcf / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 504d mean times closeadj
def fcfb_f009_free_cash_flow_burn_rel_504d_base_v102_signal(fcf, closeadj):
    m = _mean(fcf, 504).replace(0, np.nan)
    result = (fcf / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 1008d mean times closeadj
def fcfb_f009_free_cash_flow_burn_rel_1008d_base_v103_signal(fcf, closeadj):
    m = _mean(fcf, 1008).replace(0, np.nan)
    result = (fcf / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized fcf/fcfps 63d mean
def fcfb_f009_free_cash_flow_burn_sqnorm_fcfps_63d_base_v104_signal(fcf, fcfps):
    r = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized fcf/fcfps 252d mean
def fcfb_f009_free_cash_flow_burn_sqnorm_fcfps_252d_base_v105_signal(fcf, fcfps):
    r = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized fcf/ncfo 63d mean
def fcfb_f009_free_cash_flow_burn_sqnorm_ncfo_63d_base_v106_signal(fcf, ncfo):
    r = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized fcf/ncfo 252d mean
def fcfb_f009_free_cash_flow_burn_sqnorm_ncfo_252d_base_v107_signal(fcf, ncfo):
    r = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized fcf/assets 63d mean
def fcfb_f009_free_cash_flow_burn_sqnorm_assets_63d_base_v108_signal(fcf, assets):
    r = _free_cash_flow_burn_scaled(fcf, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized fcf/assets 252d mean
def fcfb_f009_free_cash_flow_burn_sqnorm_assets_252d_base_v109_signal(fcf, assets):
    r = _free_cash_flow_burn_scaled(fcf, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_infrat_63d_base_v110_signal(fcf, closeadj):
    m = _mean(fcf, 63)
    s = _std(fcf, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_infrat_252d_base_v111_signal(fcf, closeadj):
    m = _mean(fcf, 252)
    s = _std(fcf, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_infrat_504d_base_v112_signal(fcf, closeadj):
    m = _mean(fcf, 504)
    s = _std(fcf, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of fcf
def fcfb_f009_free_cash_flow_burn_cv_252d_base_v113_signal(fcf):
    m = _mean(fcf, 252).abs().replace(0, np.nan)
    s = _std(fcf, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of fcf
def fcfb_f009_free_cash_flow_burn_cv_504d_base_v114_signal(fcf):
    m = _mean(fcf, 504).abs().replace(0, np.nan)
    s = _std(fcf, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged fcf times closeadj
def fcfb_f009_free_cash_flow_burn_lag_5d_base_v115_signal(fcf, closeadj):
    result = fcf.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged fcf times closeadj
def fcfb_f009_free_cash_flow_burn_lag_21d_base_v116_signal(fcf, closeadj):
    result = fcf.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged fcf times closeadj
def fcfb_f009_free_cash_flow_burn_lag_63d_base_v117_signal(fcf, closeadj):
    result = fcf.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged fcf times closeadj
def fcfb_f009_free_cash_flow_burn_lag_252d_base_v118_signal(fcf, closeadj):
    result = fcf.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(fcf) / mean(fcfps) x closeadj
def fcfb_f009_free_cash_flow_burn_cumper_fcfps_252d_base_v119_signal(fcf, fcfps, closeadj):
    s = fcf.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(fcfps, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(fcf) / mean(fcfps) x closeadj
def fcfb_f009_free_cash_flow_burn_cumper_fcfps_504d_base_v120_signal(fcf, fcfps, closeadj):
    s = fcf.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(fcfps, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(fcf) / mean(ncfo) x closeadj
def fcfb_f009_free_cash_flow_burn_cumper_ncfo_252d_base_v121_signal(fcf, ncfo, closeadj):
    s = fcf.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ncfo, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(fcf) / mean(ncfo) x closeadj
def fcfb_f009_free_cash_flow_burn_cumper_ncfo_504d_base_v122_signal(fcf, ncfo, closeadj):
    s = fcf.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ncfo, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only fcf times closeadj
def fcfb_f009_free_cash_flow_burn_pos_63d_base_v123_signal(fcf, closeadj):
    pos = fcf.where(fcf > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only fcf times closeadj
def fcfb_f009_free_cash_flow_burn_pos_252d_base_v124_signal(fcf, closeadj):
    pos = fcf.where(fcf > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only fcf times closeadj
def fcfb_f009_free_cash_flow_burn_neg_63d_base_v125_signal(fcf, closeadj):
    neg = fcf.where(fcf < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only fcf times closeadj
def fcfb_f009_free_cash_flow_burn_neg_252d_base_v126_signal(fcf, closeadj):
    neg = fcf.where(fcf < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_hl_21d_base_v127_signal(fcf, closeadj):
    result = fcf.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_hl_63d_base_v128_signal(fcf, closeadj):
    result = fcf.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_hl_252d_base_v129_signal(fcf, closeadj):
    result = fcf.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of fcf
def fcfb_f009_free_cash_flow_burn_z_63d_base_v130_signal(fcf):
    result = _z(fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of fcf
def fcfb_f009_free_cash_flow_burn_z_126d_base_v131_signal(fcf):
    result = _z(fcf, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of fcf
def fcfb_f009_free_cash_flow_burn_z_1008d_base_v132_signal(fcf):
    result = _z(fcf, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_st_lt_252_21d_base_v133_signal(fcf, closeadj):
    sm = _mean(fcf, 21)
    lm = _mean(fcf, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_st_lt_252_63d_base_v134_signal(fcf, closeadj):
    sm = _mean(fcf, 63)
    lm = _mean(fcf, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_st_lt_504_21d_base_v135_signal(fcf, closeadj):
    sm = _mean(fcf, 21)
    lm = _mean(fcf, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_st_lt_504_63d_base_v136_signal(fcf, closeadj):
    sm = _mean(fcf, 63)
    lm = _mean(fcf, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged fcf/fcfps times closeadj
def fcfb_f009_free_cash_flow_burn_lag_per_fcfps_21d_base_v137_signal(fcf, fcfps, closeadj):
    r = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged fcf/fcfps times closeadj
def fcfb_f009_free_cash_flow_burn_lag_per_fcfps_63d_base_v138_signal(fcf, fcfps, closeadj):
    r = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged fcf/fcfps times closeadj
def fcfb_f009_free_cash_flow_burn_lag_per_fcfps_252d_base_v139_signal(fcf, fcfps, closeadj):
    r = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged fcf/ncfo times closeadj
def fcfb_f009_free_cash_flow_burn_lag_per_ncfo_21d_base_v140_signal(fcf, ncfo, closeadj):
    r = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged fcf/ncfo times closeadj
def fcfb_f009_free_cash_flow_burn_lag_per_ncfo_63d_base_v141_signal(fcf, ncfo, closeadj):
    r = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged fcf/ncfo times closeadj
def fcfb_f009_free_cash_flow_burn_lag_per_ncfo_252d_base_v142_signal(fcf, ncfo, closeadj):
    r = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |fcf| times closeadj
def fcfb_f009_free_cash_flow_burn_abssum_63d_base_v143_signal(fcf, closeadj):
    result = fcf.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |fcf| times closeadj
def fcfb_f009_free_cash_flow_burn_abssum_252d_base_v144_signal(fcf, closeadj):
    result = fcf.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |fcf| times closeadj
def fcfb_f009_free_cash_flow_burn_abssum_504d_base_v145_signal(fcf, closeadj):
    result = fcf.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of fcf
def fcfb_f009_free_cash_flow_burn_acf1_252d_base_v146_signal(fcf):
    result = fcf.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of fcf
def fcfb_f009_free_cash_flow_burn_acf1_504d_base_v147_signal(fcf):
    result = fcf.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of fcf
def fcfb_f009_free_cash_flow_burn_posinrange_252d_base_v148_signal(fcf):
    m = _mean(fcf, 252)
    hi = fcf.rolling(252, min_periods=max(1, 252//2)).max()
    lo = fcf.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of fcf
def fcfb_f009_free_cash_flow_burn_posinrange_504d_base_v149_signal(fcf):
    m = _mean(fcf, 504)
    hi = fcf.rolling(504, min_periods=max(1, 504//2)).max()
    lo = fcf.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_hl_5d_base_v150_signal(fcf, closeadj):
    result = fcf.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
