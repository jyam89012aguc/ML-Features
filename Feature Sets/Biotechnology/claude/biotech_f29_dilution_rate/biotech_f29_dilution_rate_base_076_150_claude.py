"""Family f29 - Dilution rate  (E_Dilution_Shares) | base 076-150"""
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
def _dilution_rate_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _dilution_rate_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _dilution_rate_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sharesbas/marketcap
def dil_f29_dilution_rate_log_per_marketcap_504d_base_v076_signal(sharesbas, marketcap):
    s = _dilution_rate_scaled(sharesbas, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesbas/equity
def dil_f29_dilution_rate_log_per_equity_252d_base_v077_signal(sharesbas, equity):
    s = _dilution_rate_scaled(sharesbas, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sharesbas/equity
def dil_f29_dilution_rate_log_per_equity_504d_base_v078_signal(sharesbas, equity):
    s = _dilution_rate_scaled(sharesbas, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sharesbas times closeadj
def dil_f29_dilution_rate_ewm_21d_base_v079_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sharesbas times closeadj
def dil_f29_dilution_rate_ewm_63d_base_v080_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sharesbas times closeadj
def dil_f29_dilution_rate_ewm_252d_base_v081_signal(sharesbas, closeadj):
    result = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sharesbas times closeadj
def dil_f29_dilution_rate_med_63d_base_v082_signal(sharesbas, closeadj):
    result = sharesbas.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sharesbas times closeadj
def dil_f29_dilution_rate_med_252d_base_v083_signal(sharesbas, closeadj):
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sharesbas times closeadj
def dil_f29_dilution_rate_med_504d_base_v084_signal(sharesbas, closeadj):
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sharesbas
def dil_f29_dilution_rate_skew_252d_base_v085_signal(sharesbas):
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sharesbas
def dil_f29_dilution_rate_skew_504d_base_v086_signal(sharesbas):
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sharesbas
def dil_f29_dilution_rate_kurt_252d_base_v087_signal(sharesbas):
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sharesbas
def dil_f29_dilution_rate_kurt_504d_base_v088_signal(sharesbas):
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sharesbas times closeadj
def dil_f29_dilution_rate_rank_252d_base_v089_signal(sharesbas, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sharesbas times closeadj
def dil_f29_dilution_rate_rank_504d_base_v090_signal(sharesbas, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sharesbas times closeadj
def dil_f29_dilution_rate_rank_1008d_base_v091_signal(sharesbas, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharesbas.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharesbas from 63d mean times closeadj
def dil_f29_dilution_rate_devmean_63d_base_v092_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 63)
    result = (sharesbas - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharesbas from 252d mean times closeadj
def dil_f29_dilution_rate_devmean_252d_base_v093_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 252)
    result = (sharesbas - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharesbas from 504d mean times closeadj
def dil_f29_dilution_rate_devmean_504d_base_v094_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 504)
    result = (sharesbas - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sharesbas times closeadj
def dil_f29_dilution_rate_logdiff_21d_base_v095_signal(sharesbas, closeadj):
    lr = _dilution_rate_log(sharesbas)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sharesbas times closeadj
def dil_f29_dilution_rate_logdiff_63d_base_v096_signal(sharesbas, closeadj):
    lr = _dilution_rate_log(sharesbas)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sharesbas times closeadj
def dil_f29_dilution_rate_logdiff_252d_base_v097_signal(sharesbas, closeadj):
    lr = _dilution_rate_log(sharesbas)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sharesbas times closeadj
def dil_f29_dilution_rate_range_63d_base_v098_signal(sharesbas, closeadj):
    hi = sharesbas.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sharesbas.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sharesbas times closeadj
def dil_f29_dilution_rate_range_252d_base_v099_signal(sharesbas, closeadj):
    hi = sharesbas.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sharesbas.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sharesbas times closeadj
def dil_f29_dilution_rate_range_504d_base_v100_signal(sharesbas, closeadj):
    hi = sharesbas.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sharesbas.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 252d mean times closeadj
def dil_f29_dilution_rate_rel_252d_base_v101_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 252).replace(0, np.nan)
    result = (sharesbas / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 504d mean times closeadj
def dil_f29_dilution_rate_rel_504d_base_v102_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 504).replace(0, np.nan)
    result = (sharesbas / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 1008d mean times closeadj
def dil_f29_dilution_rate_rel_1008d_base_v103_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 1008).replace(0, np.nan)
    result = (sharesbas / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesbas/assets 63d mean
def dil_f29_dilution_rate_sqnorm_assets_63d_base_v104_signal(sharesbas, assets):
    r = _dilution_rate_scaled(sharesbas, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesbas/assets 252d mean
def dil_f29_dilution_rate_sqnorm_assets_252d_base_v105_signal(sharesbas, assets):
    r = _dilution_rate_scaled(sharesbas, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesbas/marketcap 63d mean
def dil_f29_dilution_rate_sqnorm_marketcap_63d_base_v106_signal(sharesbas, marketcap):
    r = _dilution_rate_scaled(sharesbas, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesbas/marketcap 252d mean
def dil_f29_dilution_rate_sqnorm_marketcap_252d_base_v107_signal(sharesbas, marketcap):
    r = _dilution_rate_scaled(sharesbas, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesbas/equity 63d mean
def dil_f29_dilution_rate_sqnorm_equity_63d_base_v108_signal(sharesbas, equity):
    r = _dilution_rate_scaled(sharesbas, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesbas/equity 252d mean
def dil_f29_dilution_rate_sqnorm_equity_252d_base_v109_signal(sharesbas, equity):
    r = _dilution_rate_scaled(sharesbas, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sharesbas times closeadj
def dil_f29_dilution_rate_infrat_63d_base_v110_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 63)
    s = _std(sharesbas, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sharesbas times closeadj
def dil_f29_dilution_rate_infrat_252d_base_v111_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 252)
    s = _std(sharesbas, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sharesbas times closeadj
def dil_f29_dilution_rate_infrat_504d_base_v112_signal(sharesbas, closeadj):
    m = _mean(sharesbas, 504)
    s = _std(sharesbas, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sharesbas
def dil_f29_dilution_rate_cv_252d_base_v113_signal(sharesbas):
    m = _mean(sharesbas, 252).abs().replace(0, np.nan)
    s = _std(sharesbas, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sharesbas
def dil_f29_dilution_rate_cv_504d_base_v114_signal(sharesbas):
    m = _mean(sharesbas, 504).abs().replace(0, np.nan)
    s = _std(sharesbas, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sharesbas times closeadj
def dil_f29_dilution_rate_lag_5d_base_v115_signal(sharesbas, closeadj):
    result = sharesbas.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharesbas times closeadj
def dil_f29_dilution_rate_lag_21d_base_v116_signal(sharesbas, closeadj):
    result = sharesbas.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharesbas times closeadj
def dil_f29_dilution_rate_lag_63d_base_v117_signal(sharesbas, closeadj):
    result = sharesbas.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharesbas times closeadj
def dil_f29_dilution_rate_lag_252d_base_v118_signal(sharesbas, closeadj):
    result = sharesbas.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sharesbas) / mean(assets) x closeadj
def dil_f29_dilution_rate_cumper_assets_252d_base_v119_signal(sharesbas, assets, closeadj):
    s = sharesbas.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sharesbas) / mean(assets) x closeadj
def dil_f29_dilution_rate_cumper_assets_504d_base_v120_signal(sharesbas, assets, closeadj):
    s = sharesbas.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sharesbas) / mean(marketcap) x closeadj
def dil_f29_dilution_rate_cumper_marketcap_252d_base_v121_signal(sharesbas, marketcap, closeadj):
    s = sharesbas.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sharesbas) / mean(marketcap) x closeadj
def dil_f29_dilution_rate_cumper_marketcap_504d_base_v122_signal(sharesbas, marketcap, closeadj):
    s = sharesbas.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sharesbas times closeadj
def dil_f29_dilution_rate_pos_63d_base_v123_signal(sharesbas, closeadj):
    pos = sharesbas.where(sharesbas > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sharesbas times closeadj
def dil_f29_dilution_rate_pos_252d_base_v124_signal(sharesbas, closeadj):
    pos = sharesbas.where(sharesbas > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sharesbas times closeadj
def dil_f29_dilution_rate_neg_63d_base_v125_signal(sharesbas, closeadj):
    neg = sharesbas.where(sharesbas < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sharesbas times closeadj
def dil_f29_dilution_rate_neg_252d_base_v126_signal(sharesbas, closeadj):
    neg = sharesbas.where(sharesbas < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sharesbas times closeadj
def dil_f29_dilution_rate_hl_21d_base_v127_signal(sharesbas, closeadj):
    result = sharesbas.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sharesbas times closeadj
def dil_f29_dilution_rate_hl_63d_base_v128_signal(sharesbas, closeadj):
    result = sharesbas.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sharesbas times closeadj
def dil_f29_dilution_rate_hl_252d_base_v129_signal(sharesbas, closeadj):
    result = sharesbas.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sharesbas
def dil_f29_dilution_rate_z_63d_base_v130_signal(sharesbas):
    result = _z(sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sharesbas
def dil_f29_dilution_rate_z_126d_base_v131_signal(sharesbas):
    result = _z(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sharesbas
def dil_f29_dilution_rate_z_1008d_base_v132_signal(sharesbas):
    result = _z(sharesbas, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sharesbas times closeadj
def dil_f29_dilution_rate_st_lt_252_21d_base_v133_signal(sharesbas, closeadj):
    sm = _mean(sharesbas, 21)
    lm = _mean(sharesbas, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sharesbas times closeadj
def dil_f29_dilution_rate_st_lt_252_63d_base_v134_signal(sharesbas, closeadj):
    sm = _mean(sharesbas, 63)
    lm = _mean(sharesbas, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sharesbas times closeadj
def dil_f29_dilution_rate_st_lt_504_21d_base_v135_signal(sharesbas, closeadj):
    sm = _mean(sharesbas, 21)
    lm = _mean(sharesbas, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sharesbas times closeadj
def dil_f29_dilution_rate_st_lt_504_63d_base_v136_signal(sharesbas, closeadj):
    sm = _mean(sharesbas, 63)
    lm = _mean(sharesbas, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharesbas/assets times closeadj
def dil_f29_dilution_rate_lag_per_assets_21d_base_v137_signal(sharesbas, assets, closeadj):
    r = _dilution_rate_scaled(sharesbas, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharesbas/assets times closeadj
def dil_f29_dilution_rate_lag_per_assets_63d_base_v138_signal(sharesbas, assets, closeadj):
    r = _dilution_rate_scaled(sharesbas, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharesbas/assets times closeadj
def dil_f29_dilution_rate_lag_per_assets_252d_base_v139_signal(sharesbas, assets, closeadj):
    r = _dilution_rate_scaled(sharesbas, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharesbas/marketcap times closeadj
def dil_f29_dilution_rate_lag_per_marketcap_21d_base_v140_signal(sharesbas, marketcap, closeadj):
    r = _dilution_rate_scaled(sharesbas, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharesbas/marketcap times closeadj
def dil_f29_dilution_rate_lag_per_marketcap_63d_base_v141_signal(sharesbas, marketcap, closeadj):
    r = _dilution_rate_scaled(sharesbas, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharesbas/marketcap times closeadj
def dil_f29_dilution_rate_lag_per_marketcap_252d_base_v142_signal(sharesbas, marketcap, closeadj):
    r = _dilution_rate_scaled(sharesbas, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sharesbas| times closeadj
def dil_f29_dilution_rate_abssum_63d_base_v143_signal(sharesbas, closeadj):
    result = sharesbas.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sharesbas| times closeadj
def dil_f29_dilution_rate_abssum_252d_base_v144_signal(sharesbas, closeadj):
    result = sharesbas.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sharesbas| times closeadj
def dil_f29_dilution_rate_abssum_504d_base_v145_signal(sharesbas, closeadj):
    result = sharesbas.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sharesbas
def dil_f29_dilution_rate_acf1_252d_base_v146_signal(sharesbas):
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sharesbas
def dil_f29_dilution_rate_acf1_504d_base_v147_signal(sharesbas):
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sharesbas
def dil_f29_dilution_rate_posinrange_252d_base_v148_signal(sharesbas):
    m = _mean(sharesbas, 252)
    hi = sharesbas.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sharesbas.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sharesbas
def dil_f29_dilution_rate_posinrange_504d_base_v149_signal(sharesbas):
    m = _mean(sharesbas, 504)
    hi = sharesbas.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sharesbas.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sharesbas times closeadj
def dil_f29_dilution_rate_hl_5d_base_v150_signal(sharesbas, closeadj):
    result = sharesbas.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
