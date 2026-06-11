"""Family f073 - Earnings and EBITDA multiples (Valuation Multiples) | Sharadar tables: SF1,DAILY | fields: pe, evebit, evebitda, ebit, ebitda | base 076-150"""
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
def _earnings_multiples_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _earnings_multiples_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _earnings_multiples_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of pe/evebitda
def em_f073_earnings_multiples_log_per_evebitda_504d_base_v076_signal(pe, evebitda):
    s = _earnings_multiples_scaled(pe, evebitda)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of pe/ebit
def em_f073_earnings_multiples_log_per_ebit_252d_base_v077_signal(pe, ebit):
    s = _earnings_multiples_scaled(pe, ebit)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of pe/ebit
def em_f073_earnings_multiples_log_per_ebit_504d_base_v078_signal(pe, ebit):
    s = _earnings_multiples_scaled(pe, ebit)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of pe times closeadj
def em_f073_earnings_multiples_ewm_21d_base_v079_signal(pe, closeadj):
    result = pe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of pe times closeadj
def em_f073_earnings_multiples_ewm_63d_base_v080_signal(pe, closeadj):
    result = pe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of pe times closeadj
def em_f073_earnings_multiples_ewm_252d_base_v081_signal(pe, closeadj):
    result = pe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of pe times closeadj
def em_f073_earnings_multiples_med_63d_base_v082_signal(pe, closeadj):
    result = pe.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of pe times closeadj
def em_f073_earnings_multiples_med_252d_base_v083_signal(pe, closeadj):
    result = pe.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of pe times closeadj
def em_f073_earnings_multiples_med_504d_base_v084_signal(pe, closeadj):
    result = pe.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of pe
def em_f073_earnings_multiples_skew_252d_base_v085_signal(pe):
    result = pe.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of pe
def em_f073_earnings_multiples_skew_504d_base_v086_signal(pe):
    result = pe.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of pe
def em_f073_earnings_multiples_kurt_252d_base_v087_signal(pe):
    result = pe.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of pe
def em_f073_earnings_multiples_kurt_504d_base_v088_signal(pe):
    result = pe.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of pe times closeadj
def em_f073_earnings_multiples_rank_252d_base_v089_signal(pe, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = pe.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of pe times closeadj
def em_f073_earnings_multiples_rank_504d_base_v090_signal(pe, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = pe.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of pe times closeadj
def em_f073_earnings_multiples_rank_1008d_base_v091_signal(pe, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = pe.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of pe from 63d mean times closeadj
def em_f073_earnings_multiples_devmean_63d_base_v092_signal(pe, closeadj):
    m = _mean(pe, 63)
    result = (pe - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of pe from 252d mean times closeadj
def em_f073_earnings_multiples_devmean_252d_base_v093_signal(pe, closeadj):
    m = _mean(pe, 252)
    result = (pe - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of pe from 504d mean times closeadj
def em_f073_earnings_multiples_devmean_504d_base_v094_signal(pe, closeadj):
    m = _mean(pe, 504)
    result = (pe - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of pe times closeadj
def em_f073_earnings_multiples_logdiff_21d_base_v095_signal(pe, closeadj):
    lr = _earnings_multiples_log(pe)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of pe times closeadj
def em_f073_earnings_multiples_logdiff_63d_base_v096_signal(pe, closeadj):
    lr = _earnings_multiples_log(pe)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of pe times closeadj
def em_f073_earnings_multiples_logdiff_252d_base_v097_signal(pe, closeadj):
    lr = _earnings_multiples_log(pe)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of pe times closeadj
def em_f073_earnings_multiples_range_63d_base_v098_signal(pe, closeadj):
    hi = pe.rolling(63, min_periods=max(1, 63//2)).max()
    lo = pe.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of pe times closeadj
def em_f073_earnings_multiples_range_252d_base_v099_signal(pe, closeadj):
    hi = pe.rolling(252, min_periods=max(1, 252//2)).max()
    lo = pe.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of pe times closeadj
def em_f073_earnings_multiples_range_504d_base_v100_signal(pe, closeadj):
    hi = pe.rolling(504, min_periods=max(1, 504//2)).max()
    lo = pe.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 252d mean times closeadj
def em_f073_earnings_multiples_rel_252d_base_v101_signal(pe, closeadj):
    m = _mean(pe, 252).replace(0, np.nan)
    result = (pe / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 504d mean times closeadj
def em_f073_earnings_multiples_rel_504d_base_v102_signal(pe, closeadj):
    m = _mean(pe, 504).replace(0, np.nan)
    result = (pe / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pe relative to 1008d mean times closeadj
def em_f073_earnings_multiples_rel_1008d_base_v103_signal(pe, closeadj):
    m = _mean(pe, 1008).replace(0, np.nan)
    result = (pe / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pe/evebit 63d mean
def em_f073_earnings_multiples_sqnorm_evebit_63d_base_v104_signal(pe, evebit):
    r = _earnings_multiples_scaled(pe, evebit)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pe/evebit 252d mean
def em_f073_earnings_multiples_sqnorm_evebit_252d_base_v105_signal(pe, evebit):
    r = _earnings_multiples_scaled(pe, evebit)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pe/evebitda 63d mean
def em_f073_earnings_multiples_sqnorm_evebitda_63d_base_v106_signal(pe, evebitda):
    r = _earnings_multiples_scaled(pe, evebitda)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pe/evebitda 252d mean
def em_f073_earnings_multiples_sqnorm_evebitda_252d_base_v107_signal(pe, evebitda):
    r = _earnings_multiples_scaled(pe, evebitda)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pe/ebit 63d mean
def em_f073_earnings_multiples_sqnorm_ebit_63d_base_v108_signal(pe, ebit):
    r = _earnings_multiples_scaled(pe, ebit)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pe/ebit 252d mean
def em_f073_earnings_multiples_sqnorm_ebit_252d_base_v109_signal(pe, ebit):
    r = _earnings_multiples_scaled(pe, ebit)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of pe times closeadj
def em_f073_earnings_multiples_infrat_63d_base_v110_signal(pe, closeadj):
    m = _mean(pe, 63)
    s = _std(pe, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of pe times closeadj
def em_f073_earnings_multiples_infrat_252d_base_v111_signal(pe, closeadj):
    m = _mean(pe, 252)
    s = _std(pe, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of pe times closeadj
def em_f073_earnings_multiples_infrat_504d_base_v112_signal(pe, closeadj):
    m = _mean(pe, 504)
    s = _std(pe, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of pe
def em_f073_earnings_multiples_cv_252d_base_v113_signal(pe):
    m = _mean(pe, 252).abs().replace(0, np.nan)
    s = _std(pe, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of pe
def em_f073_earnings_multiples_cv_504d_base_v114_signal(pe):
    m = _mean(pe, 504).abs().replace(0, np.nan)
    s = _std(pe, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged pe times closeadj
def em_f073_earnings_multiples_lag_5d_base_v115_signal(pe, closeadj):
    result = pe.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged pe times closeadj
def em_f073_earnings_multiples_lag_21d_base_v116_signal(pe, closeadj):
    result = pe.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged pe times closeadj
def em_f073_earnings_multiples_lag_63d_base_v117_signal(pe, closeadj):
    result = pe.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged pe times closeadj
def em_f073_earnings_multiples_lag_252d_base_v118_signal(pe, closeadj):
    result = pe.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(pe) / mean(evebit) x closeadj
def em_f073_earnings_multiples_cumper_evebit_252d_base_v119_signal(pe, evebit, closeadj):
    s = pe.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(evebit, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(pe) / mean(evebit) x closeadj
def em_f073_earnings_multiples_cumper_evebit_504d_base_v120_signal(pe, evebit, closeadj):
    s = pe.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(evebit, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(pe) / mean(evebitda) x closeadj
def em_f073_earnings_multiples_cumper_evebitda_252d_base_v121_signal(pe, evebitda, closeadj):
    s = pe.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(evebitda, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(pe) / mean(evebitda) x closeadj
def em_f073_earnings_multiples_cumper_evebitda_504d_base_v122_signal(pe, evebitda, closeadj):
    s = pe.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(evebitda, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only pe times closeadj
def em_f073_earnings_multiples_pos_63d_base_v123_signal(pe, closeadj):
    pos = pe.where(pe > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only pe times closeadj
def em_f073_earnings_multiples_pos_252d_base_v124_signal(pe, closeadj):
    pos = pe.where(pe > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only pe times closeadj
def em_f073_earnings_multiples_neg_63d_base_v125_signal(pe, closeadj):
    neg = pe.where(pe < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only pe times closeadj
def em_f073_earnings_multiples_neg_252d_base_v126_signal(pe, closeadj):
    neg = pe.where(pe < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of pe times closeadj
def em_f073_earnings_multiples_hl_21d_base_v127_signal(pe, closeadj):
    result = pe.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of pe times closeadj
def em_f073_earnings_multiples_hl_63d_base_v128_signal(pe, closeadj):
    result = pe.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of pe times closeadj
def em_f073_earnings_multiples_hl_252d_base_v129_signal(pe, closeadj):
    result = pe.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of pe
def em_f073_earnings_multiples_z_63d_base_v130_signal(pe):
    result = _z(pe, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of pe
def em_f073_earnings_multiples_z_126d_base_v131_signal(pe):
    result = _z(pe, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of pe
def em_f073_earnings_multiples_z_1008d_base_v132_signal(pe):
    result = _z(pe, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of pe times closeadj
def em_f073_earnings_multiples_st_lt_252_21d_base_v133_signal(pe, closeadj):
    sm = _mean(pe, 21)
    lm = _mean(pe, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of pe times closeadj
def em_f073_earnings_multiples_st_lt_252_63d_base_v134_signal(pe, closeadj):
    sm = _mean(pe, 63)
    lm = _mean(pe, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of pe times closeadj
def em_f073_earnings_multiples_st_lt_504_21d_base_v135_signal(pe, closeadj):
    sm = _mean(pe, 21)
    lm = _mean(pe, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of pe times closeadj
def em_f073_earnings_multiples_st_lt_504_63d_base_v136_signal(pe, closeadj):
    sm = _mean(pe, 63)
    lm = _mean(pe, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged pe/evebit times closeadj
def em_f073_earnings_multiples_lag_per_evebit_21d_base_v137_signal(pe, evebit, closeadj):
    r = _earnings_multiples_scaled(pe, evebit)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged pe/evebit times closeadj
def em_f073_earnings_multiples_lag_per_evebit_63d_base_v138_signal(pe, evebit, closeadj):
    r = _earnings_multiples_scaled(pe, evebit)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged pe/evebit times closeadj
def em_f073_earnings_multiples_lag_per_evebit_252d_base_v139_signal(pe, evebit, closeadj):
    r = _earnings_multiples_scaled(pe, evebit)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged pe/evebitda times closeadj
def em_f073_earnings_multiples_lag_per_evebitda_21d_base_v140_signal(pe, evebitda, closeadj):
    r = _earnings_multiples_scaled(pe, evebitda)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged pe/evebitda times closeadj
def em_f073_earnings_multiples_lag_per_evebitda_63d_base_v141_signal(pe, evebitda, closeadj):
    r = _earnings_multiples_scaled(pe, evebitda)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged pe/evebitda times closeadj
def em_f073_earnings_multiples_lag_per_evebitda_252d_base_v142_signal(pe, evebitda, closeadj):
    r = _earnings_multiples_scaled(pe, evebitda)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |pe| times closeadj
def em_f073_earnings_multiples_abssum_63d_base_v143_signal(pe, closeadj):
    result = pe.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |pe| times closeadj
def em_f073_earnings_multiples_abssum_252d_base_v144_signal(pe, closeadj):
    result = pe.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |pe| times closeadj
def em_f073_earnings_multiples_abssum_504d_base_v145_signal(pe, closeadj):
    result = pe.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of pe
def em_f073_earnings_multiples_acf1_252d_base_v146_signal(pe):
    result = pe.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of pe
def em_f073_earnings_multiples_acf1_504d_base_v147_signal(pe):
    result = pe.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of pe
def em_f073_earnings_multiples_posinrange_252d_base_v148_signal(pe):
    m = _mean(pe, 252)
    hi = pe.rolling(252, min_periods=max(1, 252//2)).max()
    lo = pe.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of pe
def em_f073_earnings_multiples_posinrange_504d_base_v149_signal(pe):
    m = _mean(pe, 504)
    hi = pe.rolling(504, min_periods=max(1, 504//2)).max()
    lo = pe.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of pe times closeadj
def em_f073_earnings_multiples_hl_5d_base_v150_signal(pe, closeadj):
    result = pe.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
