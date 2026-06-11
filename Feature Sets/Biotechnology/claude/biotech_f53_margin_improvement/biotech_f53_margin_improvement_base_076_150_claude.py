"""Family f53 - Margin improvement rate  (H_Margins) | base 076-150"""
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
def _margin_improvement_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _margin_improvement_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _margin_improvement_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of grossmargin/marketcap
def mi_f53_margin_improvement_log_per_marketcap_504d_base_v076_signal(grossmargin, marketcap):
    s = _margin_improvement_scaled(grossmargin, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of grossmargin/equity
def mi_f53_margin_improvement_log_per_equity_252d_base_v077_signal(grossmargin, equity):
    s = _margin_improvement_scaled(grossmargin, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of grossmargin/equity
def mi_f53_margin_improvement_log_per_equity_504d_base_v078_signal(grossmargin, equity):
    s = _margin_improvement_scaled(grossmargin, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of grossmargin times closeadj
def mi_f53_margin_improvement_ewm_21d_base_v079_signal(grossmargin, closeadj):
    result = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of grossmargin times closeadj
def mi_f53_margin_improvement_ewm_63d_base_v080_signal(grossmargin, closeadj):
    result = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of grossmargin times closeadj
def mi_f53_margin_improvement_ewm_252d_base_v081_signal(grossmargin, closeadj):
    result = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of grossmargin times closeadj
def mi_f53_margin_improvement_med_63d_base_v082_signal(grossmargin, closeadj):
    result = grossmargin.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of grossmargin times closeadj
def mi_f53_margin_improvement_med_252d_base_v083_signal(grossmargin, closeadj):
    result = grossmargin.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of grossmargin times closeadj
def mi_f53_margin_improvement_med_504d_base_v084_signal(grossmargin, closeadj):
    result = grossmargin.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of grossmargin
def mi_f53_margin_improvement_skew_252d_base_v085_signal(grossmargin):
    result = grossmargin.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of grossmargin
def mi_f53_margin_improvement_skew_504d_base_v086_signal(grossmargin):
    result = grossmargin.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of grossmargin
def mi_f53_margin_improvement_kurt_252d_base_v087_signal(grossmargin):
    result = grossmargin.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of grossmargin
def mi_f53_margin_improvement_kurt_504d_base_v088_signal(grossmargin):
    result = grossmargin.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of grossmargin times closeadj
def mi_f53_margin_improvement_rank_252d_base_v089_signal(grossmargin, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = grossmargin.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of grossmargin times closeadj
def mi_f53_margin_improvement_rank_504d_base_v090_signal(grossmargin, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = grossmargin.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of grossmargin times closeadj
def mi_f53_margin_improvement_rank_1008d_base_v091_signal(grossmargin, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = grossmargin.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of grossmargin from 63d mean times closeadj
def mi_f53_margin_improvement_devmean_63d_base_v092_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 63)
    result = (grossmargin - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of grossmargin from 252d mean times closeadj
def mi_f53_margin_improvement_devmean_252d_base_v093_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 252)
    result = (grossmargin - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of grossmargin from 504d mean times closeadj
def mi_f53_margin_improvement_devmean_504d_base_v094_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 504)
    result = (grossmargin - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of grossmargin times closeadj
def mi_f53_margin_improvement_logdiff_21d_base_v095_signal(grossmargin, closeadj):
    lr = _margin_improvement_log(grossmargin)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of grossmargin times closeadj
def mi_f53_margin_improvement_logdiff_63d_base_v096_signal(grossmargin, closeadj):
    lr = _margin_improvement_log(grossmargin)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of grossmargin times closeadj
def mi_f53_margin_improvement_logdiff_252d_base_v097_signal(grossmargin, closeadj):
    lr = _margin_improvement_log(grossmargin)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of grossmargin times closeadj
def mi_f53_margin_improvement_range_63d_base_v098_signal(grossmargin, closeadj):
    hi = grossmargin.rolling(63, min_periods=max(1, 63//2)).max()
    lo = grossmargin.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of grossmargin times closeadj
def mi_f53_margin_improvement_range_252d_base_v099_signal(grossmargin, closeadj):
    hi = grossmargin.rolling(252, min_periods=max(1, 252//2)).max()
    lo = grossmargin.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of grossmargin times closeadj
def mi_f53_margin_improvement_range_504d_base_v100_signal(grossmargin, closeadj):
    hi = grossmargin.rolling(504, min_periods=max(1, 504//2)).max()
    lo = grossmargin.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 252d mean times closeadj
def mi_f53_margin_improvement_rel_252d_base_v101_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 252).replace(0, np.nan)
    result = (grossmargin / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 504d mean times closeadj
def mi_f53_margin_improvement_rel_504d_base_v102_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 504).replace(0, np.nan)
    result = (grossmargin / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin relative to 1008d mean times closeadj
def mi_f53_margin_improvement_rel_1008d_base_v103_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 1008).replace(0, np.nan)
    result = (grossmargin / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized grossmargin/assets 63d mean
def mi_f53_margin_improvement_sqnorm_assets_63d_base_v104_signal(grossmargin, assets):
    r = _margin_improvement_scaled(grossmargin, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized grossmargin/assets 252d mean
def mi_f53_margin_improvement_sqnorm_assets_252d_base_v105_signal(grossmargin, assets):
    r = _margin_improvement_scaled(grossmargin, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized grossmargin/marketcap 63d mean
def mi_f53_margin_improvement_sqnorm_marketcap_63d_base_v106_signal(grossmargin, marketcap):
    r = _margin_improvement_scaled(grossmargin, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized grossmargin/marketcap 252d mean
def mi_f53_margin_improvement_sqnorm_marketcap_252d_base_v107_signal(grossmargin, marketcap):
    r = _margin_improvement_scaled(grossmargin, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized grossmargin/equity 63d mean
def mi_f53_margin_improvement_sqnorm_equity_63d_base_v108_signal(grossmargin, equity):
    r = _margin_improvement_scaled(grossmargin, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized grossmargin/equity 252d mean
def mi_f53_margin_improvement_sqnorm_equity_252d_base_v109_signal(grossmargin, equity):
    r = _margin_improvement_scaled(grossmargin, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of grossmargin times closeadj
def mi_f53_margin_improvement_infrat_63d_base_v110_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 63)
    s = _std(grossmargin, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of grossmargin times closeadj
def mi_f53_margin_improvement_infrat_252d_base_v111_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 252)
    s = _std(grossmargin, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of grossmargin times closeadj
def mi_f53_margin_improvement_infrat_504d_base_v112_signal(grossmargin, closeadj):
    m = _mean(grossmargin, 504)
    s = _std(grossmargin, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of grossmargin
def mi_f53_margin_improvement_cv_252d_base_v113_signal(grossmargin):
    m = _mean(grossmargin, 252).abs().replace(0, np.nan)
    s = _std(grossmargin, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of grossmargin
def mi_f53_margin_improvement_cv_504d_base_v114_signal(grossmargin):
    m = _mean(grossmargin, 504).abs().replace(0, np.nan)
    s = _std(grossmargin, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged grossmargin times closeadj
def mi_f53_margin_improvement_lag_5d_base_v115_signal(grossmargin, closeadj):
    result = grossmargin.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged grossmargin times closeadj
def mi_f53_margin_improvement_lag_21d_base_v116_signal(grossmargin, closeadj):
    result = grossmargin.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged grossmargin times closeadj
def mi_f53_margin_improvement_lag_63d_base_v117_signal(grossmargin, closeadj):
    result = grossmargin.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged grossmargin times closeadj
def mi_f53_margin_improvement_lag_252d_base_v118_signal(grossmargin, closeadj):
    result = grossmargin.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(grossmargin) / mean(assets) x closeadj
def mi_f53_margin_improvement_cumper_assets_252d_base_v119_signal(grossmargin, assets, closeadj):
    s = grossmargin.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(grossmargin) / mean(assets) x closeadj
def mi_f53_margin_improvement_cumper_assets_504d_base_v120_signal(grossmargin, assets, closeadj):
    s = grossmargin.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(grossmargin) / mean(marketcap) x closeadj
def mi_f53_margin_improvement_cumper_marketcap_252d_base_v121_signal(grossmargin, marketcap, closeadj):
    s = grossmargin.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(grossmargin) / mean(marketcap) x closeadj
def mi_f53_margin_improvement_cumper_marketcap_504d_base_v122_signal(grossmargin, marketcap, closeadj):
    s = grossmargin.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only grossmargin times closeadj
def mi_f53_margin_improvement_pos_63d_base_v123_signal(grossmargin, closeadj):
    pos = grossmargin.where(grossmargin > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only grossmargin times closeadj
def mi_f53_margin_improvement_pos_252d_base_v124_signal(grossmargin, closeadj):
    pos = grossmargin.where(grossmargin > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only grossmargin times closeadj
def mi_f53_margin_improvement_neg_63d_base_v125_signal(grossmargin, closeadj):
    neg = grossmargin.where(grossmargin < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only grossmargin times closeadj
def mi_f53_margin_improvement_neg_252d_base_v126_signal(grossmargin, closeadj):
    neg = grossmargin.where(grossmargin < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of grossmargin times closeadj
def mi_f53_margin_improvement_hl_21d_base_v127_signal(grossmargin, closeadj):
    result = grossmargin.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of grossmargin times closeadj
def mi_f53_margin_improvement_hl_63d_base_v128_signal(grossmargin, closeadj):
    result = grossmargin.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of grossmargin times closeadj
def mi_f53_margin_improvement_hl_252d_base_v129_signal(grossmargin, closeadj):
    result = grossmargin.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of grossmargin
def mi_f53_margin_improvement_z_63d_base_v130_signal(grossmargin):
    result = _z(grossmargin, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of grossmargin
def mi_f53_margin_improvement_z_126d_base_v131_signal(grossmargin):
    result = _z(grossmargin, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of grossmargin
def mi_f53_margin_improvement_z_1008d_base_v132_signal(grossmargin):
    result = _z(grossmargin, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of grossmargin times closeadj
def mi_f53_margin_improvement_st_lt_252_21d_base_v133_signal(grossmargin, closeadj):
    sm = _mean(grossmargin, 21)
    lm = _mean(grossmargin, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of grossmargin times closeadj
def mi_f53_margin_improvement_st_lt_252_63d_base_v134_signal(grossmargin, closeadj):
    sm = _mean(grossmargin, 63)
    lm = _mean(grossmargin, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of grossmargin times closeadj
def mi_f53_margin_improvement_st_lt_504_21d_base_v135_signal(grossmargin, closeadj):
    sm = _mean(grossmargin, 21)
    lm = _mean(grossmargin, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of grossmargin times closeadj
def mi_f53_margin_improvement_st_lt_504_63d_base_v136_signal(grossmargin, closeadj):
    sm = _mean(grossmargin, 63)
    lm = _mean(grossmargin, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged grossmargin/assets times closeadj
def mi_f53_margin_improvement_lag_per_assets_21d_base_v137_signal(grossmargin, assets, closeadj):
    r = _margin_improvement_scaled(grossmargin, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged grossmargin/assets times closeadj
def mi_f53_margin_improvement_lag_per_assets_63d_base_v138_signal(grossmargin, assets, closeadj):
    r = _margin_improvement_scaled(grossmargin, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged grossmargin/assets times closeadj
def mi_f53_margin_improvement_lag_per_assets_252d_base_v139_signal(grossmargin, assets, closeadj):
    r = _margin_improvement_scaled(grossmargin, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged grossmargin/marketcap times closeadj
def mi_f53_margin_improvement_lag_per_marketcap_21d_base_v140_signal(grossmargin, marketcap, closeadj):
    r = _margin_improvement_scaled(grossmargin, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged grossmargin/marketcap times closeadj
def mi_f53_margin_improvement_lag_per_marketcap_63d_base_v141_signal(grossmargin, marketcap, closeadj):
    r = _margin_improvement_scaled(grossmargin, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged grossmargin/marketcap times closeadj
def mi_f53_margin_improvement_lag_per_marketcap_252d_base_v142_signal(grossmargin, marketcap, closeadj):
    r = _margin_improvement_scaled(grossmargin, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |grossmargin| times closeadj
def mi_f53_margin_improvement_abssum_63d_base_v143_signal(grossmargin, closeadj):
    result = grossmargin.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |grossmargin| times closeadj
def mi_f53_margin_improvement_abssum_252d_base_v144_signal(grossmargin, closeadj):
    result = grossmargin.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |grossmargin| times closeadj
def mi_f53_margin_improvement_abssum_504d_base_v145_signal(grossmargin, closeadj):
    result = grossmargin.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of grossmargin
def mi_f53_margin_improvement_acf1_252d_base_v146_signal(grossmargin):
    result = grossmargin.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of grossmargin
def mi_f53_margin_improvement_acf1_504d_base_v147_signal(grossmargin):
    result = grossmargin.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of grossmargin
def mi_f53_margin_improvement_posinrange_252d_base_v148_signal(grossmargin):
    m = _mean(grossmargin, 252)
    hi = grossmargin.rolling(252, min_periods=max(1, 252//2)).max()
    lo = grossmargin.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of grossmargin
def mi_f53_margin_improvement_posinrange_504d_base_v149_signal(grossmargin):
    m = _mean(grossmargin, 504)
    hi = grossmargin.rolling(504, min_periods=max(1, 504//2)).max()
    lo = grossmargin.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of grossmargin times closeadj
def mi_f53_margin_improvement_hl_5d_base_v150_signal(grossmargin, closeadj):
    result = grossmargin.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
