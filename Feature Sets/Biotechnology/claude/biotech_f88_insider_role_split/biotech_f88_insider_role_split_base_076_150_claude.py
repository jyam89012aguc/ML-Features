"""Family f88 - Role-split activity  (O_Insider_SF2) | base 076-150"""
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
def _insider_role_split_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_role_split_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_role_split_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of transactionvalue/marketcap
def irs_f88_insider_role_split_log_per_marketcap_504d_base_v076_signal(transactionvalue, marketcap):
    s = _insider_role_split_scaled(transactionvalue, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of transactionvalue/equity
def irs_f88_insider_role_split_log_per_equity_252d_base_v077_signal(transactionvalue, equity):
    s = _insider_role_split_scaled(transactionvalue, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of transactionvalue/equity
def irs_f88_insider_role_split_log_per_equity_504d_base_v078_signal(transactionvalue, equity):
    s = _insider_role_split_scaled(transactionvalue, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of transactionvalue times closeadj
def irs_f88_insider_role_split_ewm_21d_base_v079_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of transactionvalue times closeadj
def irs_f88_insider_role_split_ewm_63d_base_v080_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of transactionvalue times closeadj
def irs_f88_insider_role_split_ewm_252d_base_v081_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of transactionvalue times closeadj
def irs_f88_insider_role_split_med_63d_base_v082_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of transactionvalue times closeadj
def irs_f88_insider_role_split_med_252d_base_v083_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of transactionvalue times closeadj
def irs_f88_insider_role_split_med_504d_base_v084_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of transactionvalue
def irs_f88_insider_role_split_skew_252d_base_v085_signal(transactionvalue):
    result = transactionvalue.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of transactionvalue
def irs_f88_insider_role_split_skew_504d_base_v086_signal(transactionvalue):
    result = transactionvalue.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of transactionvalue
def irs_f88_insider_role_split_kurt_252d_base_v087_signal(transactionvalue):
    result = transactionvalue.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of transactionvalue
def irs_f88_insider_role_split_kurt_504d_base_v088_signal(transactionvalue):
    result = transactionvalue.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of transactionvalue times closeadj
def irs_f88_insider_role_split_rank_252d_base_v089_signal(transactionvalue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = transactionvalue.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of transactionvalue times closeadj
def irs_f88_insider_role_split_rank_504d_base_v090_signal(transactionvalue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = transactionvalue.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of transactionvalue times closeadj
def irs_f88_insider_role_split_rank_1008d_base_v091_signal(transactionvalue, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = transactionvalue.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of transactionvalue from 63d mean times closeadj
def irs_f88_insider_role_split_devmean_63d_base_v092_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 63)
    result = (transactionvalue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of transactionvalue from 252d mean times closeadj
def irs_f88_insider_role_split_devmean_252d_base_v093_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 252)
    result = (transactionvalue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of transactionvalue from 504d mean times closeadj
def irs_f88_insider_role_split_devmean_504d_base_v094_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 504)
    result = (transactionvalue - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of transactionvalue times closeadj
def irs_f88_insider_role_split_logdiff_21d_base_v095_signal(transactionvalue, closeadj):
    lr = _insider_role_split_log(transactionvalue)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of transactionvalue times closeadj
def irs_f88_insider_role_split_logdiff_63d_base_v096_signal(transactionvalue, closeadj):
    lr = _insider_role_split_log(transactionvalue)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of transactionvalue times closeadj
def irs_f88_insider_role_split_logdiff_252d_base_v097_signal(transactionvalue, closeadj):
    lr = _insider_role_split_log(transactionvalue)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of transactionvalue times closeadj
def irs_f88_insider_role_split_range_63d_base_v098_signal(transactionvalue, closeadj):
    hi = transactionvalue.rolling(63, min_periods=max(1, 63//2)).max()
    lo = transactionvalue.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of transactionvalue times closeadj
def irs_f88_insider_role_split_range_252d_base_v099_signal(transactionvalue, closeadj):
    hi = transactionvalue.rolling(252, min_periods=max(1, 252//2)).max()
    lo = transactionvalue.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of transactionvalue times closeadj
def irs_f88_insider_role_split_range_504d_base_v100_signal(transactionvalue, closeadj):
    hi = transactionvalue.rolling(504, min_periods=max(1, 504//2)).max()
    lo = transactionvalue.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 252d mean times closeadj
def irs_f88_insider_role_split_rel_252d_base_v101_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 252).replace(0, np.nan)
    result = (transactionvalue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 504d mean times closeadj
def irs_f88_insider_role_split_rel_504d_base_v102_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 504).replace(0, np.nan)
    result = (transactionvalue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 1008d mean times closeadj
def irs_f88_insider_role_split_rel_1008d_base_v103_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 1008).replace(0, np.nan)
    result = (transactionvalue / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactionvalue/assets 63d mean
def irs_f88_insider_role_split_sqnorm_assets_63d_base_v104_signal(transactionvalue, assets):
    r = _insider_role_split_scaled(transactionvalue, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactionvalue/assets 252d mean
def irs_f88_insider_role_split_sqnorm_assets_252d_base_v105_signal(transactionvalue, assets):
    r = _insider_role_split_scaled(transactionvalue, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactionvalue/marketcap 63d mean
def irs_f88_insider_role_split_sqnorm_marketcap_63d_base_v106_signal(transactionvalue, marketcap):
    r = _insider_role_split_scaled(transactionvalue, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactionvalue/marketcap 252d mean
def irs_f88_insider_role_split_sqnorm_marketcap_252d_base_v107_signal(transactionvalue, marketcap):
    r = _insider_role_split_scaled(transactionvalue, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactionvalue/equity 63d mean
def irs_f88_insider_role_split_sqnorm_equity_63d_base_v108_signal(transactionvalue, equity):
    r = _insider_role_split_scaled(transactionvalue, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized transactionvalue/equity 252d mean
def irs_f88_insider_role_split_sqnorm_equity_252d_base_v109_signal(transactionvalue, equity):
    r = _insider_role_split_scaled(transactionvalue, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of transactionvalue times closeadj
def irs_f88_insider_role_split_infrat_63d_base_v110_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 63)
    s = _std(transactionvalue, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of transactionvalue times closeadj
def irs_f88_insider_role_split_infrat_252d_base_v111_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 252)
    s = _std(transactionvalue, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of transactionvalue times closeadj
def irs_f88_insider_role_split_infrat_504d_base_v112_signal(transactionvalue, closeadj):
    m = _mean(transactionvalue, 504)
    s = _std(transactionvalue, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of transactionvalue
def irs_f88_insider_role_split_cv_252d_base_v113_signal(transactionvalue):
    m = _mean(transactionvalue, 252).abs().replace(0, np.nan)
    s = _std(transactionvalue, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of transactionvalue
def irs_f88_insider_role_split_cv_504d_base_v114_signal(transactionvalue):
    m = _mean(transactionvalue, 504).abs().replace(0, np.nan)
    s = _std(transactionvalue, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged transactionvalue times closeadj
def irs_f88_insider_role_split_lag_5d_base_v115_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged transactionvalue times closeadj
def irs_f88_insider_role_split_lag_21d_base_v116_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged transactionvalue times closeadj
def irs_f88_insider_role_split_lag_63d_base_v117_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged transactionvalue times closeadj
def irs_f88_insider_role_split_lag_252d_base_v118_signal(transactionvalue, closeadj):
    result = transactionvalue.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(transactionvalue) / mean(assets) x closeadj
def irs_f88_insider_role_split_cumper_assets_252d_base_v119_signal(transactionvalue, assets, closeadj):
    s = transactionvalue.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(transactionvalue) / mean(assets) x closeadj
def irs_f88_insider_role_split_cumper_assets_504d_base_v120_signal(transactionvalue, assets, closeadj):
    s = transactionvalue.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(transactionvalue) / mean(marketcap) x closeadj
def irs_f88_insider_role_split_cumper_marketcap_252d_base_v121_signal(transactionvalue, marketcap, closeadj):
    s = transactionvalue.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(transactionvalue) / mean(marketcap) x closeadj
def irs_f88_insider_role_split_cumper_marketcap_504d_base_v122_signal(transactionvalue, marketcap, closeadj):
    s = transactionvalue.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only transactionvalue times closeadj
def irs_f88_insider_role_split_pos_63d_base_v123_signal(transactionvalue, closeadj):
    pos = transactionvalue.where(transactionvalue > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only transactionvalue times closeadj
def irs_f88_insider_role_split_pos_252d_base_v124_signal(transactionvalue, closeadj):
    pos = transactionvalue.where(transactionvalue > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only transactionvalue times closeadj
def irs_f88_insider_role_split_neg_63d_base_v125_signal(transactionvalue, closeadj):
    neg = transactionvalue.where(transactionvalue < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only transactionvalue times closeadj
def irs_f88_insider_role_split_neg_252d_base_v126_signal(transactionvalue, closeadj):
    neg = transactionvalue.where(transactionvalue < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of transactionvalue times closeadj
def irs_f88_insider_role_split_hl_21d_base_v127_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of transactionvalue times closeadj
def irs_f88_insider_role_split_hl_63d_base_v128_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of transactionvalue times closeadj
def irs_f88_insider_role_split_hl_252d_base_v129_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of transactionvalue
def irs_f88_insider_role_split_z_63d_base_v130_signal(transactionvalue):
    result = _z(transactionvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of transactionvalue
def irs_f88_insider_role_split_z_126d_base_v131_signal(transactionvalue):
    result = _z(transactionvalue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of transactionvalue
def irs_f88_insider_role_split_z_1008d_base_v132_signal(transactionvalue):
    result = _z(transactionvalue, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of transactionvalue times closeadj
def irs_f88_insider_role_split_st_lt_252_21d_base_v133_signal(transactionvalue, closeadj):
    sm = _mean(transactionvalue, 21)
    lm = _mean(transactionvalue, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of transactionvalue times closeadj
def irs_f88_insider_role_split_st_lt_252_63d_base_v134_signal(transactionvalue, closeadj):
    sm = _mean(transactionvalue, 63)
    lm = _mean(transactionvalue, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of transactionvalue times closeadj
def irs_f88_insider_role_split_st_lt_504_21d_base_v135_signal(transactionvalue, closeadj):
    sm = _mean(transactionvalue, 21)
    lm = _mean(transactionvalue, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of transactionvalue times closeadj
def irs_f88_insider_role_split_st_lt_504_63d_base_v136_signal(transactionvalue, closeadj):
    sm = _mean(transactionvalue, 63)
    lm = _mean(transactionvalue, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged transactionvalue/assets times closeadj
def irs_f88_insider_role_split_lag_per_assets_21d_base_v137_signal(transactionvalue, assets, closeadj):
    r = _insider_role_split_scaled(transactionvalue, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged transactionvalue/assets times closeadj
def irs_f88_insider_role_split_lag_per_assets_63d_base_v138_signal(transactionvalue, assets, closeadj):
    r = _insider_role_split_scaled(transactionvalue, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged transactionvalue/assets times closeadj
def irs_f88_insider_role_split_lag_per_assets_252d_base_v139_signal(transactionvalue, assets, closeadj):
    r = _insider_role_split_scaled(transactionvalue, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged transactionvalue/marketcap times closeadj
def irs_f88_insider_role_split_lag_per_marketcap_21d_base_v140_signal(transactionvalue, marketcap, closeadj):
    r = _insider_role_split_scaled(transactionvalue, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged transactionvalue/marketcap times closeadj
def irs_f88_insider_role_split_lag_per_marketcap_63d_base_v141_signal(transactionvalue, marketcap, closeadj):
    r = _insider_role_split_scaled(transactionvalue, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged transactionvalue/marketcap times closeadj
def irs_f88_insider_role_split_lag_per_marketcap_252d_base_v142_signal(transactionvalue, marketcap, closeadj):
    r = _insider_role_split_scaled(transactionvalue, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |transactionvalue| times closeadj
def irs_f88_insider_role_split_abssum_63d_base_v143_signal(transactionvalue, closeadj):
    result = transactionvalue.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |transactionvalue| times closeadj
def irs_f88_insider_role_split_abssum_252d_base_v144_signal(transactionvalue, closeadj):
    result = transactionvalue.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |transactionvalue| times closeadj
def irs_f88_insider_role_split_abssum_504d_base_v145_signal(transactionvalue, closeadj):
    result = transactionvalue.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of transactionvalue
def irs_f88_insider_role_split_acf1_252d_base_v146_signal(transactionvalue):
    result = transactionvalue.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of transactionvalue
def irs_f88_insider_role_split_acf1_504d_base_v147_signal(transactionvalue):
    result = transactionvalue.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of transactionvalue
def irs_f88_insider_role_split_posinrange_252d_base_v148_signal(transactionvalue):
    m = _mean(transactionvalue, 252)
    hi = transactionvalue.rolling(252, min_periods=max(1, 252//2)).max()
    lo = transactionvalue.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of transactionvalue
def irs_f88_insider_role_split_posinrange_504d_base_v149_signal(transactionvalue):
    m = _mean(transactionvalue, 504)
    hi = transactionvalue.rolling(504, min_periods=max(1, 504//2)).max()
    lo = transactionvalue.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of transactionvalue times closeadj
def irs_f88_insider_role_split_hl_5d_base_v150_signal(transactionvalue, closeadj):
    result = transactionvalue.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
