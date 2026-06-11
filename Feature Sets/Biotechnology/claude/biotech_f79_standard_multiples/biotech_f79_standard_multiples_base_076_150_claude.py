"""Family f79 - EV/EBIT EV/EBITDA P/E P/S  (M_Valuation) | base 076-150"""
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
def _standard_multiples_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _standard_multiples_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _standard_multiples_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of evebit/marketcap
def sm_f79_standard_multiples_log_per_marketcap_504d_base_v076_signal(evebit, marketcap):
    s = _standard_multiples_scaled(evebit, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of evebit/equity
def sm_f79_standard_multiples_log_per_equity_252d_base_v077_signal(evebit, equity):
    s = _standard_multiples_scaled(evebit, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of evebit/equity
def sm_f79_standard_multiples_log_per_equity_504d_base_v078_signal(evebit, equity):
    s = _standard_multiples_scaled(evebit, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of evebit times closeadj
def sm_f79_standard_multiples_ewm_21d_base_v079_signal(evebit, closeadj):
    result = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of evebit times closeadj
def sm_f79_standard_multiples_ewm_63d_base_v080_signal(evebit, closeadj):
    result = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of evebit times closeadj
def sm_f79_standard_multiples_ewm_252d_base_v081_signal(evebit, closeadj):
    result = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of evebit times closeadj
def sm_f79_standard_multiples_med_63d_base_v082_signal(evebit, closeadj):
    result = evebit.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of evebit times closeadj
def sm_f79_standard_multiples_med_252d_base_v083_signal(evebit, closeadj):
    result = evebit.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of evebit times closeadj
def sm_f79_standard_multiples_med_504d_base_v084_signal(evebit, closeadj):
    result = evebit.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of evebit
def sm_f79_standard_multiples_skew_252d_base_v085_signal(evebit):
    result = evebit.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of evebit
def sm_f79_standard_multiples_skew_504d_base_v086_signal(evebit):
    result = evebit.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of evebit
def sm_f79_standard_multiples_kurt_252d_base_v087_signal(evebit):
    result = evebit.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of evebit
def sm_f79_standard_multiples_kurt_504d_base_v088_signal(evebit):
    result = evebit.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of evebit times closeadj
def sm_f79_standard_multiples_rank_252d_base_v089_signal(evebit, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = evebit.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of evebit times closeadj
def sm_f79_standard_multiples_rank_504d_base_v090_signal(evebit, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = evebit.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of evebit times closeadj
def sm_f79_standard_multiples_rank_1008d_base_v091_signal(evebit, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = evebit.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of evebit from 63d mean times closeadj
def sm_f79_standard_multiples_devmean_63d_base_v092_signal(evebit, closeadj):
    m = _mean(evebit, 63)
    result = (evebit - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of evebit from 252d mean times closeadj
def sm_f79_standard_multiples_devmean_252d_base_v093_signal(evebit, closeadj):
    m = _mean(evebit, 252)
    result = (evebit - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of evebit from 504d mean times closeadj
def sm_f79_standard_multiples_devmean_504d_base_v094_signal(evebit, closeadj):
    m = _mean(evebit, 504)
    result = (evebit - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of evebit times closeadj
def sm_f79_standard_multiples_logdiff_21d_base_v095_signal(evebit, closeadj):
    lr = _standard_multiples_log(evebit)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of evebit times closeadj
def sm_f79_standard_multiples_logdiff_63d_base_v096_signal(evebit, closeadj):
    lr = _standard_multiples_log(evebit)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of evebit times closeadj
def sm_f79_standard_multiples_logdiff_252d_base_v097_signal(evebit, closeadj):
    lr = _standard_multiples_log(evebit)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of evebit times closeadj
def sm_f79_standard_multiples_range_63d_base_v098_signal(evebit, closeadj):
    hi = evebit.rolling(63, min_periods=max(1, 63//2)).max()
    lo = evebit.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of evebit times closeadj
def sm_f79_standard_multiples_range_252d_base_v099_signal(evebit, closeadj):
    hi = evebit.rolling(252, min_periods=max(1, 252//2)).max()
    lo = evebit.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of evebit times closeadj
def sm_f79_standard_multiples_range_504d_base_v100_signal(evebit, closeadj):
    hi = evebit.rolling(504, min_periods=max(1, 504//2)).max()
    lo = evebit.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 252d mean times closeadj
def sm_f79_standard_multiples_rel_252d_base_v101_signal(evebit, closeadj):
    m = _mean(evebit, 252).replace(0, np.nan)
    result = (evebit / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 504d mean times closeadj
def sm_f79_standard_multiples_rel_504d_base_v102_signal(evebit, closeadj):
    m = _mean(evebit, 504).replace(0, np.nan)
    result = (evebit / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# evebit relative to 1008d mean times closeadj
def sm_f79_standard_multiples_rel_1008d_base_v103_signal(evebit, closeadj):
    m = _mean(evebit, 1008).replace(0, np.nan)
    result = (evebit / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized evebit/assets 63d mean
def sm_f79_standard_multiples_sqnorm_assets_63d_base_v104_signal(evebit, assets):
    r = _standard_multiples_scaled(evebit, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized evebit/assets 252d mean
def sm_f79_standard_multiples_sqnorm_assets_252d_base_v105_signal(evebit, assets):
    r = _standard_multiples_scaled(evebit, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized evebit/marketcap 63d mean
def sm_f79_standard_multiples_sqnorm_marketcap_63d_base_v106_signal(evebit, marketcap):
    r = _standard_multiples_scaled(evebit, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized evebit/marketcap 252d mean
def sm_f79_standard_multiples_sqnorm_marketcap_252d_base_v107_signal(evebit, marketcap):
    r = _standard_multiples_scaled(evebit, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized evebit/equity 63d mean
def sm_f79_standard_multiples_sqnorm_equity_63d_base_v108_signal(evebit, equity):
    r = _standard_multiples_scaled(evebit, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized evebit/equity 252d mean
def sm_f79_standard_multiples_sqnorm_equity_252d_base_v109_signal(evebit, equity):
    r = _standard_multiples_scaled(evebit, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of evebit times closeadj
def sm_f79_standard_multiples_infrat_63d_base_v110_signal(evebit, closeadj):
    m = _mean(evebit, 63)
    s = _std(evebit, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of evebit times closeadj
def sm_f79_standard_multiples_infrat_252d_base_v111_signal(evebit, closeadj):
    m = _mean(evebit, 252)
    s = _std(evebit, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of evebit times closeadj
def sm_f79_standard_multiples_infrat_504d_base_v112_signal(evebit, closeadj):
    m = _mean(evebit, 504)
    s = _std(evebit, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of evebit
def sm_f79_standard_multiples_cv_252d_base_v113_signal(evebit):
    m = _mean(evebit, 252).abs().replace(0, np.nan)
    s = _std(evebit, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of evebit
def sm_f79_standard_multiples_cv_504d_base_v114_signal(evebit):
    m = _mean(evebit, 504).abs().replace(0, np.nan)
    s = _std(evebit, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged evebit times closeadj
def sm_f79_standard_multiples_lag_5d_base_v115_signal(evebit, closeadj):
    result = evebit.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged evebit times closeadj
def sm_f79_standard_multiples_lag_21d_base_v116_signal(evebit, closeadj):
    result = evebit.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged evebit times closeadj
def sm_f79_standard_multiples_lag_63d_base_v117_signal(evebit, closeadj):
    result = evebit.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged evebit times closeadj
def sm_f79_standard_multiples_lag_252d_base_v118_signal(evebit, closeadj):
    result = evebit.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(evebit) / mean(assets) x closeadj
def sm_f79_standard_multiples_cumper_assets_252d_base_v119_signal(evebit, assets, closeadj):
    s = evebit.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(evebit) / mean(assets) x closeadj
def sm_f79_standard_multiples_cumper_assets_504d_base_v120_signal(evebit, assets, closeadj):
    s = evebit.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(evebit) / mean(marketcap) x closeadj
def sm_f79_standard_multiples_cumper_marketcap_252d_base_v121_signal(evebit, marketcap, closeadj):
    s = evebit.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(evebit) / mean(marketcap) x closeadj
def sm_f79_standard_multiples_cumper_marketcap_504d_base_v122_signal(evebit, marketcap, closeadj):
    s = evebit.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only evebit times closeadj
def sm_f79_standard_multiples_pos_63d_base_v123_signal(evebit, closeadj):
    pos = evebit.where(evebit > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only evebit times closeadj
def sm_f79_standard_multiples_pos_252d_base_v124_signal(evebit, closeadj):
    pos = evebit.where(evebit > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only evebit times closeadj
def sm_f79_standard_multiples_neg_63d_base_v125_signal(evebit, closeadj):
    neg = evebit.where(evebit < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only evebit times closeadj
def sm_f79_standard_multiples_neg_252d_base_v126_signal(evebit, closeadj):
    neg = evebit.where(evebit < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of evebit times closeadj
def sm_f79_standard_multiples_hl_21d_base_v127_signal(evebit, closeadj):
    result = evebit.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of evebit times closeadj
def sm_f79_standard_multiples_hl_63d_base_v128_signal(evebit, closeadj):
    result = evebit.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of evebit times closeadj
def sm_f79_standard_multiples_hl_252d_base_v129_signal(evebit, closeadj):
    result = evebit.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of evebit
def sm_f79_standard_multiples_z_63d_base_v130_signal(evebit):
    result = _z(evebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of evebit
def sm_f79_standard_multiples_z_126d_base_v131_signal(evebit):
    result = _z(evebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of evebit
def sm_f79_standard_multiples_z_1008d_base_v132_signal(evebit):
    result = _z(evebit, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of evebit times closeadj
def sm_f79_standard_multiples_st_lt_252_21d_base_v133_signal(evebit, closeadj):
    sm = _mean(evebit, 21)
    lm = _mean(evebit, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of evebit times closeadj
def sm_f79_standard_multiples_st_lt_252_63d_base_v134_signal(evebit, closeadj):
    sm = _mean(evebit, 63)
    lm = _mean(evebit, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of evebit times closeadj
def sm_f79_standard_multiples_st_lt_504_21d_base_v135_signal(evebit, closeadj):
    sm = _mean(evebit, 21)
    lm = _mean(evebit, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of evebit times closeadj
def sm_f79_standard_multiples_st_lt_504_63d_base_v136_signal(evebit, closeadj):
    sm = _mean(evebit, 63)
    lm = _mean(evebit, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged evebit/assets times closeadj
def sm_f79_standard_multiples_lag_per_assets_21d_base_v137_signal(evebit, assets, closeadj):
    r = _standard_multiples_scaled(evebit, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged evebit/assets times closeadj
def sm_f79_standard_multiples_lag_per_assets_63d_base_v138_signal(evebit, assets, closeadj):
    r = _standard_multiples_scaled(evebit, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged evebit/assets times closeadj
def sm_f79_standard_multiples_lag_per_assets_252d_base_v139_signal(evebit, assets, closeadj):
    r = _standard_multiples_scaled(evebit, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged evebit/marketcap times closeadj
def sm_f79_standard_multiples_lag_per_marketcap_21d_base_v140_signal(evebit, marketcap, closeadj):
    r = _standard_multiples_scaled(evebit, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged evebit/marketcap times closeadj
def sm_f79_standard_multiples_lag_per_marketcap_63d_base_v141_signal(evebit, marketcap, closeadj):
    r = _standard_multiples_scaled(evebit, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged evebit/marketcap times closeadj
def sm_f79_standard_multiples_lag_per_marketcap_252d_base_v142_signal(evebit, marketcap, closeadj):
    r = _standard_multiples_scaled(evebit, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |evebit| times closeadj
def sm_f79_standard_multiples_abssum_63d_base_v143_signal(evebit, closeadj):
    result = evebit.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |evebit| times closeadj
def sm_f79_standard_multiples_abssum_252d_base_v144_signal(evebit, closeadj):
    result = evebit.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |evebit| times closeadj
def sm_f79_standard_multiples_abssum_504d_base_v145_signal(evebit, closeadj):
    result = evebit.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of evebit
def sm_f79_standard_multiples_acf1_252d_base_v146_signal(evebit):
    result = evebit.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of evebit
def sm_f79_standard_multiples_acf1_504d_base_v147_signal(evebit):
    result = evebit.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of evebit
def sm_f79_standard_multiples_posinrange_252d_base_v148_signal(evebit):
    m = _mean(evebit, 252)
    hi = evebit.rolling(252, min_periods=max(1, 252//2)).max()
    lo = evebit.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of evebit
def sm_f79_standard_multiples_posinrange_504d_base_v149_signal(evebit):
    m = _mean(evebit, 504)
    hi = evebit.rolling(504, min_periods=max(1, 504//2)).max()
    lo = evebit.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of evebit times closeadj
def sm_f79_standard_multiples_hl_5d_base_v150_signal(evebit, closeadj):
    result = evebit.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
