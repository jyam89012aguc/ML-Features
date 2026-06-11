"""Family f51 - EBITDA / EBIT margins  (H_Margins) | base 076-150"""
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
def _ebitda_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ebitda_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ebitda_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ebitda/marketcap
def em_f51_ebitda_margin_log_per_marketcap_504d_base_v076_signal(ebitda, marketcap):
    s = _ebitda_margin_scaled(ebitda, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ebitda/equity
def em_f51_ebitda_margin_log_per_equity_252d_base_v077_signal(ebitda, equity):
    s = _ebitda_margin_scaled(ebitda, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ebitda/equity
def em_f51_ebitda_margin_log_per_equity_504d_base_v078_signal(ebitda, equity):
    s = _ebitda_margin_scaled(ebitda, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ebitda times closeadj
def em_f51_ebitda_margin_ewm_21d_base_v079_signal(ebitda, closeadj):
    result = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ebitda times closeadj
def em_f51_ebitda_margin_ewm_63d_base_v080_signal(ebitda, closeadj):
    result = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ebitda times closeadj
def em_f51_ebitda_margin_ewm_252d_base_v081_signal(ebitda, closeadj):
    result = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ebitda times closeadj
def em_f51_ebitda_margin_med_63d_base_v082_signal(ebitda, closeadj):
    result = ebitda.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ebitda times closeadj
def em_f51_ebitda_margin_med_252d_base_v083_signal(ebitda, closeadj):
    result = ebitda.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ebitda times closeadj
def em_f51_ebitda_margin_med_504d_base_v084_signal(ebitda, closeadj):
    result = ebitda.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ebitda
def em_f51_ebitda_margin_skew_252d_base_v085_signal(ebitda):
    result = ebitda.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ebitda
def em_f51_ebitda_margin_skew_504d_base_v086_signal(ebitda):
    result = ebitda.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ebitda
def em_f51_ebitda_margin_kurt_252d_base_v087_signal(ebitda):
    result = ebitda.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ebitda
def em_f51_ebitda_margin_kurt_504d_base_v088_signal(ebitda):
    result = ebitda.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ebitda times closeadj
def em_f51_ebitda_margin_rank_252d_base_v089_signal(ebitda, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ebitda.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ebitda times closeadj
def em_f51_ebitda_margin_rank_504d_base_v090_signal(ebitda, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ebitda.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ebitda times closeadj
def em_f51_ebitda_margin_rank_1008d_base_v091_signal(ebitda, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ebitda.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ebitda from 63d mean times closeadj
def em_f51_ebitda_margin_devmean_63d_base_v092_signal(ebitda, closeadj):
    m = _mean(ebitda, 63)
    result = (ebitda - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ebitda from 252d mean times closeadj
def em_f51_ebitda_margin_devmean_252d_base_v093_signal(ebitda, closeadj):
    m = _mean(ebitda, 252)
    result = (ebitda - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ebitda from 504d mean times closeadj
def em_f51_ebitda_margin_devmean_504d_base_v094_signal(ebitda, closeadj):
    m = _mean(ebitda, 504)
    result = (ebitda - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ebitda times closeadj
def em_f51_ebitda_margin_logdiff_21d_base_v095_signal(ebitda, closeadj):
    lr = _ebitda_margin_log(ebitda)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ebitda times closeadj
def em_f51_ebitda_margin_logdiff_63d_base_v096_signal(ebitda, closeadj):
    lr = _ebitda_margin_log(ebitda)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ebitda times closeadj
def em_f51_ebitda_margin_logdiff_252d_base_v097_signal(ebitda, closeadj):
    lr = _ebitda_margin_log(ebitda)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ebitda times closeadj
def em_f51_ebitda_margin_range_63d_base_v098_signal(ebitda, closeadj):
    hi = ebitda.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ebitda.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ebitda times closeadj
def em_f51_ebitda_margin_range_252d_base_v099_signal(ebitda, closeadj):
    hi = ebitda.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ebitda.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ebitda times closeadj
def em_f51_ebitda_margin_range_504d_base_v100_signal(ebitda, closeadj):
    hi = ebitda.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ebitda.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 252d mean times closeadj
def em_f51_ebitda_margin_rel_252d_base_v101_signal(ebitda, closeadj):
    m = _mean(ebitda, 252).replace(0, np.nan)
    result = (ebitda / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 504d mean times closeadj
def em_f51_ebitda_margin_rel_504d_base_v102_signal(ebitda, closeadj):
    m = _mean(ebitda, 504).replace(0, np.nan)
    result = (ebitda / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda relative to 1008d mean times closeadj
def em_f51_ebitda_margin_rel_1008d_base_v103_signal(ebitda, closeadj):
    m = _mean(ebitda, 1008).replace(0, np.nan)
    result = (ebitda / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ebitda/assets 63d mean
def em_f51_ebitda_margin_sqnorm_assets_63d_base_v104_signal(ebitda, assets):
    r = _ebitda_margin_scaled(ebitda, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ebitda/assets 252d mean
def em_f51_ebitda_margin_sqnorm_assets_252d_base_v105_signal(ebitda, assets):
    r = _ebitda_margin_scaled(ebitda, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ebitda/marketcap 63d mean
def em_f51_ebitda_margin_sqnorm_marketcap_63d_base_v106_signal(ebitda, marketcap):
    r = _ebitda_margin_scaled(ebitda, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ebitda/marketcap 252d mean
def em_f51_ebitda_margin_sqnorm_marketcap_252d_base_v107_signal(ebitda, marketcap):
    r = _ebitda_margin_scaled(ebitda, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ebitda/equity 63d mean
def em_f51_ebitda_margin_sqnorm_equity_63d_base_v108_signal(ebitda, equity):
    r = _ebitda_margin_scaled(ebitda, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ebitda/equity 252d mean
def em_f51_ebitda_margin_sqnorm_equity_252d_base_v109_signal(ebitda, equity):
    r = _ebitda_margin_scaled(ebitda, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ebitda times closeadj
def em_f51_ebitda_margin_infrat_63d_base_v110_signal(ebitda, closeadj):
    m = _mean(ebitda, 63)
    s = _std(ebitda, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ebitda times closeadj
def em_f51_ebitda_margin_infrat_252d_base_v111_signal(ebitda, closeadj):
    m = _mean(ebitda, 252)
    s = _std(ebitda, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ebitda times closeadj
def em_f51_ebitda_margin_infrat_504d_base_v112_signal(ebitda, closeadj):
    m = _mean(ebitda, 504)
    s = _std(ebitda, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ebitda
def em_f51_ebitda_margin_cv_252d_base_v113_signal(ebitda):
    m = _mean(ebitda, 252).abs().replace(0, np.nan)
    s = _std(ebitda, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ebitda
def em_f51_ebitda_margin_cv_504d_base_v114_signal(ebitda):
    m = _mean(ebitda, 504).abs().replace(0, np.nan)
    s = _std(ebitda, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ebitda times closeadj
def em_f51_ebitda_margin_lag_5d_base_v115_signal(ebitda, closeadj):
    result = ebitda.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ebitda times closeadj
def em_f51_ebitda_margin_lag_21d_base_v116_signal(ebitda, closeadj):
    result = ebitda.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ebitda times closeadj
def em_f51_ebitda_margin_lag_63d_base_v117_signal(ebitda, closeadj):
    result = ebitda.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ebitda times closeadj
def em_f51_ebitda_margin_lag_252d_base_v118_signal(ebitda, closeadj):
    result = ebitda.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ebitda) / mean(assets) x closeadj
def em_f51_ebitda_margin_cumper_assets_252d_base_v119_signal(ebitda, assets, closeadj):
    s = ebitda.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ebitda) / mean(assets) x closeadj
def em_f51_ebitda_margin_cumper_assets_504d_base_v120_signal(ebitda, assets, closeadj):
    s = ebitda.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ebitda) / mean(marketcap) x closeadj
def em_f51_ebitda_margin_cumper_marketcap_252d_base_v121_signal(ebitda, marketcap, closeadj):
    s = ebitda.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ebitda) / mean(marketcap) x closeadj
def em_f51_ebitda_margin_cumper_marketcap_504d_base_v122_signal(ebitda, marketcap, closeadj):
    s = ebitda.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ebitda times closeadj
def em_f51_ebitda_margin_pos_63d_base_v123_signal(ebitda, closeadj):
    pos = ebitda.where(ebitda > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ebitda times closeadj
def em_f51_ebitda_margin_pos_252d_base_v124_signal(ebitda, closeadj):
    pos = ebitda.where(ebitda > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ebitda times closeadj
def em_f51_ebitda_margin_neg_63d_base_v125_signal(ebitda, closeadj):
    neg = ebitda.where(ebitda < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ebitda times closeadj
def em_f51_ebitda_margin_neg_252d_base_v126_signal(ebitda, closeadj):
    neg = ebitda.where(ebitda < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ebitda times closeadj
def em_f51_ebitda_margin_hl_21d_base_v127_signal(ebitda, closeadj):
    result = ebitda.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ebitda times closeadj
def em_f51_ebitda_margin_hl_63d_base_v128_signal(ebitda, closeadj):
    result = ebitda.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ebitda times closeadj
def em_f51_ebitda_margin_hl_252d_base_v129_signal(ebitda, closeadj):
    result = ebitda.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ebitda
def em_f51_ebitda_margin_z_63d_base_v130_signal(ebitda):
    result = _z(ebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ebitda
def em_f51_ebitda_margin_z_126d_base_v131_signal(ebitda):
    result = _z(ebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ebitda
def em_f51_ebitda_margin_z_1008d_base_v132_signal(ebitda):
    result = _z(ebitda, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ebitda times closeadj
def em_f51_ebitda_margin_st_lt_252_21d_base_v133_signal(ebitda, closeadj):
    sm = _mean(ebitda, 21)
    lm = _mean(ebitda, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ebitda times closeadj
def em_f51_ebitda_margin_st_lt_252_63d_base_v134_signal(ebitda, closeadj):
    sm = _mean(ebitda, 63)
    lm = _mean(ebitda, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ebitda times closeadj
def em_f51_ebitda_margin_st_lt_504_21d_base_v135_signal(ebitda, closeadj):
    sm = _mean(ebitda, 21)
    lm = _mean(ebitda, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ebitda times closeadj
def em_f51_ebitda_margin_st_lt_504_63d_base_v136_signal(ebitda, closeadj):
    sm = _mean(ebitda, 63)
    lm = _mean(ebitda, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ebitda/assets times closeadj
def em_f51_ebitda_margin_lag_per_assets_21d_base_v137_signal(ebitda, assets, closeadj):
    r = _ebitda_margin_scaled(ebitda, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ebitda/assets times closeadj
def em_f51_ebitda_margin_lag_per_assets_63d_base_v138_signal(ebitda, assets, closeadj):
    r = _ebitda_margin_scaled(ebitda, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ebitda/assets times closeadj
def em_f51_ebitda_margin_lag_per_assets_252d_base_v139_signal(ebitda, assets, closeadj):
    r = _ebitda_margin_scaled(ebitda, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ebitda/marketcap times closeadj
def em_f51_ebitda_margin_lag_per_marketcap_21d_base_v140_signal(ebitda, marketcap, closeadj):
    r = _ebitda_margin_scaled(ebitda, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ebitda/marketcap times closeadj
def em_f51_ebitda_margin_lag_per_marketcap_63d_base_v141_signal(ebitda, marketcap, closeadj):
    r = _ebitda_margin_scaled(ebitda, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ebitda/marketcap times closeadj
def em_f51_ebitda_margin_lag_per_marketcap_252d_base_v142_signal(ebitda, marketcap, closeadj):
    r = _ebitda_margin_scaled(ebitda, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ebitda| times closeadj
def em_f51_ebitda_margin_abssum_63d_base_v143_signal(ebitda, closeadj):
    result = ebitda.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ebitda| times closeadj
def em_f51_ebitda_margin_abssum_252d_base_v144_signal(ebitda, closeadj):
    result = ebitda.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ebitda| times closeadj
def em_f51_ebitda_margin_abssum_504d_base_v145_signal(ebitda, closeadj):
    result = ebitda.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ebitda
def em_f51_ebitda_margin_acf1_252d_base_v146_signal(ebitda):
    result = ebitda.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ebitda
def em_f51_ebitda_margin_acf1_504d_base_v147_signal(ebitda):
    result = ebitda.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ebitda
def em_f51_ebitda_margin_posinrange_252d_base_v148_signal(ebitda):
    m = _mean(ebitda, 252)
    hi = ebitda.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ebitda.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ebitda
def em_f51_ebitda_margin_posinrange_504d_base_v149_signal(ebitda):
    m = _mean(ebitda, 504)
    hi = ebitda.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ebitda.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ebitda times closeadj
def em_f51_ebitda_margin_hl_5d_base_v150_signal(ebitda, closeadj):
    result = ebitda.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
