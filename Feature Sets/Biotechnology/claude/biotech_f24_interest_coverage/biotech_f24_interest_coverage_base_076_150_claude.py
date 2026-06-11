"""Family f24 - Interest expense & coverage  (D_Capital_Debt) | base 076-150"""
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
def _interest_coverage_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _interest_coverage_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _interest_coverage_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of intexp/marketcap
def ic_f24_interest_coverage_log_per_marketcap_504d_base_v076_signal(intexp, marketcap):
    s = _interest_coverage_scaled(intexp, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intexp/equity
def ic_f24_interest_coverage_log_per_equity_252d_base_v077_signal(intexp, equity):
    s = _interest_coverage_scaled(intexp, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of intexp/equity
def ic_f24_interest_coverage_log_per_equity_504d_base_v078_signal(intexp, equity):
    s = _interest_coverage_scaled(intexp, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of intexp times closeadj
def ic_f24_interest_coverage_ewm_21d_base_v079_signal(intexp, closeadj):
    result = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of intexp times closeadj
def ic_f24_interest_coverage_ewm_63d_base_v080_signal(intexp, closeadj):
    result = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of intexp times closeadj
def ic_f24_interest_coverage_ewm_252d_base_v081_signal(intexp, closeadj):
    result = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of intexp times closeadj
def ic_f24_interest_coverage_med_63d_base_v082_signal(intexp, closeadj):
    result = intexp.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of intexp times closeadj
def ic_f24_interest_coverage_med_252d_base_v083_signal(intexp, closeadj):
    result = intexp.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of intexp times closeadj
def ic_f24_interest_coverage_med_504d_base_v084_signal(intexp, closeadj):
    result = intexp.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of intexp
def ic_f24_interest_coverage_skew_252d_base_v085_signal(intexp):
    result = intexp.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of intexp
def ic_f24_interest_coverage_skew_504d_base_v086_signal(intexp):
    result = intexp.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of intexp
def ic_f24_interest_coverage_kurt_252d_base_v087_signal(intexp):
    result = intexp.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of intexp
def ic_f24_interest_coverage_kurt_504d_base_v088_signal(intexp):
    result = intexp.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of intexp times closeadj
def ic_f24_interest_coverage_rank_252d_base_v089_signal(intexp, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = intexp.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of intexp times closeadj
def ic_f24_interest_coverage_rank_504d_base_v090_signal(intexp, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = intexp.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of intexp times closeadj
def ic_f24_interest_coverage_rank_1008d_base_v091_signal(intexp, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = intexp.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of intexp from 63d mean times closeadj
def ic_f24_interest_coverage_devmean_63d_base_v092_signal(intexp, closeadj):
    m = _mean(intexp, 63)
    result = (intexp - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of intexp from 252d mean times closeadj
def ic_f24_interest_coverage_devmean_252d_base_v093_signal(intexp, closeadj):
    m = _mean(intexp, 252)
    result = (intexp - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of intexp from 504d mean times closeadj
def ic_f24_interest_coverage_devmean_504d_base_v094_signal(intexp, closeadj):
    m = _mean(intexp, 504)
    result = (intexp - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of intexp times closeadj
def ic_f24_interest_coverage_logdiff_21d_base_v095_signal(intexp, closeadj):
    lr = _interest_coverage_log(intexp)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of intexp times closeadj
def ic_f24_interest_coverage_logdiff_63d_base_v096_signal(intexp, closeadj):
    lr = _interest_coverage_log(intexp)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of intexp times closeadj
def ic_f24_interest_coverage_logdiff_252d_base_v097_signal(intexp, closeadj):
    lr = _interest_coverage_log(intexp)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of intexp times closeadj
def ic_f24_interest_coverage_range_63d_base_v098_signal(intexp, closeadj):
    hi = intexp.rolling(63, min_periods=max(1, 63//2)).max()
    lo = intexp.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of intexp times closeadj
def ic_f24_interest_coverage_range_252d_base_v099_signal(intexp, closeadj):
    hi = intexp.rolling(252, min_periods=max(1, 252//2)).max()
    lo = intexp.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of intexp times closeadj
def ic_f24_interest_coverage_range_504d_base_v100_signal(intexp, closeadj):
    hi = intexp.rolling(504, min_periods=max(1, 504//2)).max()
    lo = intexp.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 252d mean times closeadj
def ic_f24_interest_coverage_rel_252d_base_v101_signal(intexp, closeadj):
    m = _mean(intexp, 252).replace(0, np.nan)
    result = (intexp / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 504d mean times closeadj
def ic_f24_interest_coverage_rel_504d_base_v102_signal(intexp, closeadj):
    m = _mean(intexp, 504).replace(0, np.nan)
    result = (intexp / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 1008d mean times closeadj
def ic_f24_interest_coverage_rel_1008d_base_v103_signal(intexp, closeadj):
    m = _mean(intexp, 1008).replace(0, np.nan)
    result = (intexp / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intexp/assets 63d mean
def ic_f24_interest_coverage_sqnorm_assets_63d_base_v104_signal(intexp, assets):
    r = _interest_coverage_scaled(intexp, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intexp/assets 252d mean
def ic_f24_interest_coverage_sqnorm_assets_252d_base_v105_signal(intexp, assets):
    r = _interest_coverage_scaled(intexp, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intexp/marketcap 63d mean
def ic_f24_interest_coverage_sqnorm_marketcap_63d_base_v106_signal(intexp, marketcap):
    r = _interest_coverage_scaled(intexp, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intexp/marketcap 252d mean
def ic_f24_interest_coverage_sqnorm_marketcap_252d_base_v107_signal(intexp, marketcap):
    r = _interest_coverage_scaled(intexp, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intexp/equity 63d mean
def ic_f24_interest_coverage_sqnorm_equity_63d_base_v108_signal(intexp, equity):
    r = _interest_coverage_scaled(intexp, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized intexp/equity 252d mean
def ic_f24_interest_coverage_sqnorm_equity_252d_base_v109_signal(intexp, equity):
    r = _interest_coverage_scaled(intexp, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of intexp times closeadj
def ic_f24_interest_coverage_infrat_63d_base_v110_signal(intexp, closeadj):
    m = _mean(intexp, 63)
    s = _std(intexp, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of intexp times closeadj
def ic_f24_interest_coverage_infrat_252d_base_v111_signal(intexp, closeadj):
    m = _mean(intexp, 252)
    s = _std(intexp, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of intexp times closeadj
def ic_f24_interest_coverage_infrat_504d_base_v112_signal(intexp, closeadj):
    m = _mean(intexp, 504)
    s = _std(intexp, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of intexp
def ic_f24_interest_coverage_cv_252d_base_v113_signal(intexp):
    m = _mean(intexp, 252).abs().replace(0, np.nan)
    s = _std(intexp, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of intexp
def ic_f24_interest_coverage_cv_504d_base_v114_signal(intexp):
    m = _mean(intexp, 504).abs().replace(0, np.nan)
    s = _std(intexp, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged intexp times closeadj
def ic_f24_interest_coverage_lag_5d_base_v115_signal(intexp, closeadj):
    result = intexp.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged intexp times closeadj
def ic_f24_interest_coverage_lag_21d_base_v116_signal(intexp, closeadj):
    result = intexp.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged intexp times closeadj
def ic_f24_interest_coverage_lag_63d_base_v117_signal(intexp, closeadj):
    result = intexp.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged intexp times closeadj
def ic_f24_interest_coverage_lag_252d_base_v118_signal(intexp, closeadj):
    result = intexp.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(intexp) / mean(assets) x closeadj
def ic_f24_interest_coverage_cumper_assets_252d_base_v119_signal(intexp, assets, closeadj):
    s = intexp.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(intexp) / mean(assets) x closeadj
def ic_f24_interest_coverage_cumper_assets_504d_base_v120_signal(intexp, assets, closeadj):
    s = intexp.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(intexp) / mean(marketcap) x closeadj
def ic_f24_interest_coverage_cumper_marketcap_252d_base_v121_signal(intexp, marketcap, closeadj):
    s = intexp.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(intexp) / mean(marketcap) x closeadj
def ic_f24_interest_coverage_cumper_marketcap_504d_base_v122_signal(intexp, marketcap, closeadj):
    s = intexp.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only intexp times closeadj
def ic_f24_interest_coverage_pos_63d_base_v123_signal(intexp, closeadj):
    pos = intexp.where(intexp > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only intexp times closeadj
def ic_f24_interest_coverage_pos_252d_base_v124_signal(intexp, closeadj):
    pos = intexp.where(intexp > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only intexp times closeadj
def ic_f24_interest_coverage_neg_63d_base_v125_signal(intexp, closeadj):
    neg = intexp.where(intexp < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only intexp times closeadj
def ic_f24_interest_coverage_neg_252d_base_v126_signal(intexp, closeadj):
    neg = intexp.where(intexp < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of intexp times closeadj
def ic_f24_interest_coverage_hl_21d_base_v127_signal(intexp, closeadj):
    result = intexp.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of intexp times closeadj
def ic_f24_interest_coverage_hl_63d_base_v128_signal(intexp, closeadj):
    result = intexp.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of intexp times closeadj
def ic_f24_interest_coverage_hl_252d_base_v129_signal(intexp, closeadj):
    result = intexp.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of intexp
def ic_f24_interest_coverage_z_63d_base_v130_signal(intexp):
    result = _z(intexp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of intexp
def ic_f24_interest_coverage_z_126d_base_v131_signal(intexp):
    result = _z(intexp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of intexp
def ic_f24_interest_coverage_z_1008d_base_v132_signal(intexp):
    result = _z(intexp, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of intexp times closeadj
def ic_f24_interest_coverage_st_lt_252_21d_base_v133_signal(intexp, closeadj):
    sm = _mean(intexp, 21)
    lm = _mean(intexp, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of intexp times closeadj
def ic_f24_interest_coverage_st_lt_252_63d_base_v134_signal(intexp, closeadj):
    sm = _mean(intexp, 63)
    lm = _mean(intexp, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of intexp times closeadj
def ic_f24_interest_coverage_st_lt_504_21d_base_v135_signal(intexp, closeadj):
    sm = _mean(intexp, 21)
    lm = _mean(intexp, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of intexp times closeadj
def ic_f24_interest_coverage_st_lt_504_63d_base_v136_signal(intexp, closeadj):
    sm = _mean(intexp, 63)
    lm = _mean(intexp, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged intexp/assets times closeadj
def ic_f24_interest_coverage_lag_per_assets_21d_base_v137_signal(intexp, assets, closeadj):
    r = _interest_coverage_scaled(intexp, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged intexp/assets times closeadj
def ic_f24_interest_coverage_lag_per_assets_63d_base_v138_signal(intexp, assets, closeadj):
    r = _interest_coverage_scaled(intexp, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged intexp/assets times closeadj
def ic_f24_interest_coverage_lag_per_assets_252d_base_v139_signal(intexp, assets, closeadj):
    r = _interest_coverage_scaled(intexp, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged intexp/marketcap times closeadj
def ic_f24_interest_coverage_lag_per_marketcap_21d_base_v140_signal(intexp, marketcap, closeadj):
    r = _interest_coverage_scaled(intexp, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged intexp/marketcap times closeadj
def ic_f24_interest_coverage_lag_per_marketcap_63d_base_v141_signal(intexp, marketcap, closeadj):
    r = _interest_coverage_scaled(intexp, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged intexp/marketcap times closeadj
def ic_f24_interest_coverage_lag_per_marketcap_252d_base_v142_signal(intexp, marketcap, closeadj):
    r = _interest_coverage_scaled(intexp, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |intexp| times closeadj
def ic_f24_interest_coverage_abssum_63d_base_v143_signal(intexp, closeadj):
    result = intexp.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |intexp| times closeadj
def ic_f24_interest_coverage_abssum_252d_base_v144_signal(intexp, closeadj):
    result = intexp.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |intexp| times closeadj
def ic_f24_interest_coverage_abssum_504d_base_v145_signal(intexp, closeadj):
    result = intexp.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of intexp
def ic_f24_interest_coverage_acf1_252d_base_v146_signal(intexp):
    result = intexp.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of intexp
def ic_f24_interest_coverage_acf1_504d_base_v147_signal(intexp):
    result = intexp.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of intexp
def ic_f24_interest_coverage_posinrange_252d_base_v148_signal(intexp):
    m = _mean(intexp, 252)
    hi = intexp.rolling(252, min_periods=max(1, 252//2)).max()
    lo = intexp.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of intexp
def ic_f24_interest_coverage_posinrange_504d_base_v149_signal(intexp):
    m = _mean(intexp, 504)
    hi = intexp.rolling(504, min_periods=max(1, 504//2)).max()
    lo = intexp.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of intexp times closeadj
def ic_f24_interest_coverage_hl_5d_base_v150_signal(intexp, closeadj):
    result = intexp.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
