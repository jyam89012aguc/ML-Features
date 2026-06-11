"""Family f66 - Cash conversion cycle  (K_WorkingCapital) | base 076-150"""
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
def _cash_conversion_cycle_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_conversion_cycle_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_conversion_cycle_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of receivables/marketcap
def ccc_f66_cash_conversion_cycle_log_per_marketcap_504d_base_v076_signal(receivables, marketcap):
    s = _cash_conversion_cycle_scaled(receivables, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of receivables/equity
def ccc_f66_cash_conversion_cycle_log_per_equity_252d_base_v077_signal(receivables, equity):
    s = _cash_conversion_cycle_scaled(receivables, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of receivables/equity
def ccc_f66_cash_conversion_cycle_log_per_equity_504d_base_v078_signal(receivables, equity):
    s = _cash_conversion_cycle_scaled(receivables, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of receivables times closeadj
def ccc_f66_cash_conversion_cycle_ewm_21d_base_v079_signal(receivables, closeadj):
    result = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of receivables times closeadj
def ccc_f66_cash_conversion_cycle_ewm_63d_base_v080_signal(receivables, closeadj):
    result = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of receivables times closeadj
def ccc_f66_cash_conversion_cycle_ewm_252d_base_v081_signal(receivables, closeadj):
    result = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of receivables times closeadj
def ccc_f66_cash_conversion_cycle_med_63d_base_v082_signal(receivables, closeadj):
    result = receivables.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of receivables times closeadj
def ccc_f66_cash_conversion_cycle_med_252d_base_v083_signal(receivables, closeadj):
    result = receivables.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of receivables times closeadj
def ccc_f66_cash_conversion_cycle_med_504d_base_v084_signal(receivables, closeadj):
    result = receivables.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of receivables
def ccc_f66_cash_conversion_cycle_skew_252d_base_v085_signal(receivables):
    result = receivables.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of receivables
def ccc_f66_cash_conversion_cycle_skew_504d_base_v086_signal(receivables):
    result = receivables.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of receivables
def ccc_f66_cash_conversion_cycle_kurt_252d_base_v087_signal(receivables):
    result = receivables.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of receivables
def ccc_f66_cash_conversion_cycle_kurt_504d_base_v088_signal(receivables):
    result = receivables.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of receivables times closeadj
def ccc_f66_cash_conversion_cycle_rank_252d_base_v089_signal(receivables, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = receivables.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of receivables times closeadj
def ccc_f66_cash_conversion_cycle_rank_504d_base_v090_signal(receivables, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = receivables.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of receivables times closeadj
def ccc_f66_cash_conversion_cycle_rank_1008d_base_v091_signal(receivables, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = receivables.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of receivables from 63d mean times closeadj
def ccc_f66_cash_conversion_cycle_devmean_63d_base_v092_signal(receivables, closeadj):
    m = _mean(receivables, 63)
    result = (receivables - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of receivables from 252d mean times closeadj
def ccc_f66_cash_conversion_cycle_devmean_252d_base_v093_signal(receivables, closeadj):
    m = _mean(receivables, 252)
    result = (receivables - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of receivables from 504d mean times closeadj
def ccc_f66_cash_conversion_cycle_devmean_504d_base_v094_signal(receivables, closeadj):
    m = _mean(receivables, 504)
    result = (receivables - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of receivables times closeadj
def ccc_f66_cash_conversion_cycle_logdiff_21d_base_v095_signal(receivables, closeadj):
    lr = _cash_conversion_cycle_log(receivables)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of receivables times closeadj
def ccc_f66_cash_conversion_cycle_logdiff_63d_base_v096_signal(receivables, closeadj):
    lr = _cash_conversion_cycle_log(receivables)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of receivables times closeadj
def ccc_f66_cash_conversion_cycle_logdiff_252d_base_v097_signal(receivables, closeadj):
    lr = _cash_conversion_cycle_log(receivables)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of receivables times closeadj
def ccc_f66_cash_conversion_cycle_range_63d_base_v098_signal(receivables, closeadj):
    hi = receivables.rolling(63, min_periods=max(1, 63//2)).max()
    lo = receivables.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of receivables times closeadj
def ccc_f66_cash_conversion_cycle_range_252d_base_v099_signal(receivables, closeadj):
    hi = receivables.rolling(252, min_periods=max(1, 252//2)).max()
    lo = receivables.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of receivables times closeadj
def ccc_f66_cash_conversion_cycle_range_504d_base_v100_signal(receivables, closeadj):
    hi = receivables.rolling(504, min_periods=max(1, 504//2)).max()
    lo = receivables.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 252d mean times closeadj
def ccc_f66_cash_conversion_cycle_rel_252d_base_v101_signal(receivables, closeadj):
    m = _mean(receivables, 252).replace(0, np.nan)
    result = (receivables / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 504d mean times closeadj
def ccc_f66_cash_conversion_cycle_rel_504d_base_v102_signal(receivables, closeadj):
    m = _mean(receivables, 504).replace(0, np.nan)
    result = (receivables / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 1008d mean times closeadj
def ccc_f66_cash_conversion_cycle_rel_1008d_base_v103_signal(receivables, closeadj):
    m = _mean(receivables, 1008).replace(0, np.nan)
    result = (receivables / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized receivables/assets 63d mean
def ccc_f66_cash_conversion_cycle_sqnorm_assets_63d_base_v104_signal(receivables, assets):
    r = _cash_conversion_cycle_scaled(receivables, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized receivables/assets 252d mean
def ccc_f66_cash_conversion_cycle_sqnorm_assets_252d_base_v105_signal(receivables, assets):
    r = _cash_conversion_cycle_scaled(receivables, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized receivables/marketcap 63d mean
def ccc_f66_cash_conversion_cycle_sqnorm_marketcap_63d_base_v106_signal(receivables, marketcap):
    r = _cash_conversion_cycle_scaled(receivables, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized receivables/marketcap 252d mean
def ccc_f66_cash_conversion_cycle_sqnorm_marketcap_252d_base_v107_signal(receivables, marketcap):
    r = _cash_conversion_cycle_scaled(receivables, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized receivables/equity 63d mean
def ccc_f66_cash_conversion_cycle_sqnorm_equity_63d_base_v108_signal(receivables, equity):
    r = _cash_conversion_cycle_scaled(receivables, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized receivables/equity 252d mean
def ccc_f66_cash_conversion_cycle_sqnorm_equity_252d_base_v109_signal(receivables, equity):
    r = _cash_conversion_cycle_scaled(receivables, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of receivables times closeadj
def ccc_f66_cash_conversion_cycle_infrat_63d_base_v110_signal(receivables, closeadj):
    m = _mean(receivables, 63)
    s = _std(receivables, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of receivables times closeadj
def ccc_f66_cash_conversion_cycle_infrat_252d_base_v111_signal(receivables, closeadj):
    m = _mean(receivables, 252)
    s = _std(receivables, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of receivables times closeadj
def ccc_f66_cash_conversion_cycle_infrat_504d_base_v112_signal(receivables, closeadj):
    m = _mean(receivables, 504)
    s = _std(receivables, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of receivables
def ccc_f66_cash_conversion_cycle_cv_252d_base_v113_signal(receivables):
    m = _mean(receivables, 252).abs().replace(0, np.nan)
    s = _std(receivables, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of receivables
def ccc_f66_cash_conversion_cycle_cv_504d_base_v114_signal(receivables):
    m = _mean(receivables, 504).abs().replace(0, np.nan)
    s = _std(receivables, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged receivables times closeadj
def ccc_f66_cash_conversion_cycle_lag_5d_base_v115_signal(receivables, closeadj):
    result = receivables.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged receivables times closeadj
def ccc_f66_cash_conversion_cycle_lag_21d_base_v116_signal(receivables, closeadj):
    result = receivables.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged receivables times closeadj
def ccc_f66_cash_conversion_cycle_lag_63d_base_v117_signal(receivables, closeadj):
    result = receivables.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged receivables times closeadj
def ccc_f66_cash_conversion_cycle_lag_252d_base_v118_signal(receivables, closeadj):
    result = receivables.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(receivables) / mean(assets) x closeadj
def ccc_f66_cash_conversion_cycle_cumper_assets_252d_base_v119_signal(receivables, assets, closeadj):
    s = receivables.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(receivables) / mean(assets) x closeadj
def ccc_f66_cash_conversion_cycle_cumper_assets_504d_base_v120_signal(receivables, assets, closeadj):
    s = receivables.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(receivables) / mean(marketcap) x closeadj
def ccc_f66_cash_conversion_cycle_cumper_marketcap_252d_base_v121_signal(receivables, marketcap, closeadj):
    s = receivables.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(receivables) / mean(marketcap) x closeadj
def ccc_f66_cash_conversion_cycle_cumper_marketcap_504d_base_v122_signal(receivables, marketcap, closeadj):
    s = receivables.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only receivables times closeadj
def ccc_f66_cash_conversion_cycle_pos_63d_base_v123_signal(receivables, closeadj):
    pos = receivables.where(receivables > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only receivables times closeadj
def ccc_f66_cash_conversion_cycle_pos_252d_base_v124_signal(receivables, closeadj):
    pos = receivables.where(receivables > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only receivables times closeadj
def ccc_f66_cash_conversion_cycle_neg_63d_base_v125_signal(receivables, closeadj):
    neg = receivables.where(receivables < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only receivables times closeadj
def ccc_f66_cash_conversion_cycle_neg_252d_base_v126_signal(receivables, closeadj):
    neg = receivables.where(receivables < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of receivables times closeadj
def ccc_f66_cash_conversion_cycle_hl_21d_base_v127_signal(receivables, closeadj):
    result = receivables.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of receivables times closeadj
def ccc_f66_cash_conversion_cycle_hl_63d_base_v128_signal(receivables, closeadj):
    result = receivables.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of receivables times closeadj
def ccc_f66_cash_conversion_cycle_hl_252d_base_v129_signal(receivables, closeadj):
    result = receivables.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of receivables
def ccc_f66_cash_conversion_cycle_z_63d_base_v130_signal(receivables):
    result = _z(receivables, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of receivables
def ccc_f66_cash_conversion_cycle_z_126d_base_v131_signal(receivables):
    result = _z(receivables, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of receivables
def ccc_f66_cash_conversion_cycle_z_1008d_base_v132_signal(receivables):
    result = _z(receivables, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of receivables times closeadj
def ccc_f66_cash_conversion_cycle_st_lt_252_21d_base_v133_signal(receivables, closeadj):
    sm = _mean(receivables, 21)
    lm = _mean(receivables, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of receivables times closeadj
def ccc_f66_cash_conversion_cycle_st_lt_252_63d_base_v134_signal(receivables, closeadj):
    sm = _mean(receivables, 63)
    lm = _mean(receivables, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of receivables times closeadj
def ccc_f66_cash_conversion_cycle_st_lt_504_21d_base_v135_signal(receivables, closeadj):
    sm = _mean(receivables, 21)
    lm = _mean(receivables, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of receivables times closeadj
def ccc_f66_cash_conversion_cycle_st_lt_504_63d_base_v136_signal(receivables, closeadj):
    sm = _mean(receivables, 63)
    lm = _mean(receivables, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged receivables/assets times closeadj
def ccc_f66_cash_conversion_cycle_lag_per_assets_21d_base_v137_signal(receivables, assets, closeadj):
    r = _cash_conversion_cycle_scaled(receivables, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged receivables/assets times closeadj
def ccc_f66_cash_conversion_cycle_lag_per_assets_63d_base_v138_signal(receivables, assets, closeadj):
    r = _cash_conversion_cycle_scaled(receivables, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged receivables/assets times closeadj
def ccc_f66_cash_conversion_cycle_lag_per_assets_252d_base_v139_signal(receivables, assets, closeadj):
    r = _cash_conversion_cycle_scaled(receivables, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged receivables/marketcap times closeadj
def ccc_f66_cash_conversion_cycle_lag_per_marketcap_21d_base_v140_signal(receivables, marketcap, closeadj):
    r = _cash_conversion_cycle_scaled(receivables, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged receivables/marketcap times closeadj
def ccc_f66_cash_conversion_cycle_lag_per_marketcap_63d_base_v141_signal(receivables, marketcap, closeadj):
    r = _cash_conversion_cycle_scaled(receivables, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged receivables/marketcap times closeadj
def ccc_f66_cash_conversion_cycle_lag_per_marketcap_252d_base_v142_signal(receivables, marketcap, closeadj):
    r = _cash_conversion_cycle_scaled(receivables, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |receivables| times closeadj
def ccc_f66_cash_conversion_cycle_abssum_63d_base_v143_signal(receivables, closeadj):
    result = receivables.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |receivables| times closeadj
def ccc_f66_cash_conversion_cycle_abssum_252d_base_v144_signal(receivables, closeadj):
    result = receivables.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |receivables| times closeadj
def ccc_f66_cash_conversion_cycle_abssum_504d_base_v145_signal(receivables, closeadj):
    result = receivables.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of receivables
def ccc_f66_cash_conversion_cycle_acf1_252d_base_v146_signal(receivables):
    result = receivables.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of receivables
def ccc_f66_cash_conversion_cycle_acf1_504d_base_v147_signal(receivables):
    result = receivables.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of receivables
def ccc_f66_cash_conversion_cycle_posinrange_252d_base_v148_signal(receivables):
    m = _mean(receivables, 252)
    hi = receivables.rolling(252, min_periods=max(1, 252//2)).max()
    lo = receivables.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of receivables
def ccc_f66_cash_conversion_cycle_posinrange_504d_base_v149_signal(receivables):
    m = _mean(receivables, 504)
    hi = receivables.rolling(504, min_periods=max(1, 504//2)).max()
    lo = receivables.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of receivables times closeadj
def ccc_f66_cash_conversion_cycle_hl_5d_base_v150_signal(receivables, closeadj):
    result = receivables.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
