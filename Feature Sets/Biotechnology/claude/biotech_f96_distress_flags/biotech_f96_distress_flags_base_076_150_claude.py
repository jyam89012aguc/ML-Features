"""Family f96 - Distress & structural flags  (Q_Actions_Events) | base 076-150"""
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
def _distress_flags_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _distress_flags_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _distress_flags_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of distressflag/marketcap
def df_f96_distress_flags_log_per_marketcap_504d_base_v076_signal(distressflag, marketcap):
    s = _distress_flags_scaled(distressflag, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of distressflag/equity
def df_f96_distress_flags_log_per_equity_252d_base_v077_signal(distressflag, equity):
    s = _distress_flags_scaled(distressflag, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of distressflag/equity
def df_f96_distress_flags_log_per_equity_504d_base_v078_signal(distressflag, equity):
    s = _distress_flags_scaled(distressflag, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of distressflag times closeadj
def df_f96_distress_flags_ewm_21d_base_v079_signal(distressflag, closeadj):
    result = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of distressflag times closeadj
def df_f96_distress_flags_ewm_63d_base_v080_signal(distressflag, closeadj):
    result = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of distressflag times closeadj
def df_f96_distress_flags_ewm_252d_base_v081_signal(distressflag, closeadj):
    result = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of distressflag times closeadj
def df_f96_distress_flags_med_63d_base_v082_signal(distressflag, closeadj):
    result = distressflag.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of distressflag times closeadj
def df_f96_distress_flags_med_252d_base_v083_signal(distressflag, closeadj):
    result = distressflag.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of distressflag times closeadj
def df_f96_distress_flags_med_504d_base_v084_signal(distressflag, closeadj):
    result = distressflag.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of distressflag
def df_f96_distress_flags_skew_252d_base_v085_signal(distressflag):
    result = distressflag.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of distressflag
def df_f96_distress_flags_skew_504d_base_v086_signal(distressflag):
    result = distressflag.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of distressflag
def df_f96_distress_flags_kurt_252d_base_v087_signal(distressflag):
    result = distressflag.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of distressflag
def df_f96_distress_flags_kurt_504d_base_v088_signal(distressflag):
    result = distressflag.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of distressflag times closeadj
def df_f96_distress_flags_rank_252d_base_v089_signal(distressflag, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = distressflag.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of distressflag times closeadj
def df_f96_distress_flags_rank_504d_base_v090_signal(distressflag, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = distressflag.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of distressflag times closeadj
def df_f96_distress_flags_rank_1008d_base_v091_signal(distressflag, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = distressflag.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of distressflag from 63d mean times closeadj
def df_f96_distress_flags_devmean_63d_base_v092_signal(distressflag, closeadj):
    m = _mean(distressflag, 63)
    result = (distressflag - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of distressflag from 252d mean times closeadj
def df_f96_distress_flags_devmean_252d_base_v093_signal(distressflag, closeadj):
    m = _mean(distressflag, 252)
    result = (distressflag - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of distressflag from 504d mean times closeadj
def df_f96_distress_flags_devmean_504d_base_v094_signal(distressflag, closeadj):
    m = _mean(distressflag, 504)
    result = (distressflag - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of distressflag times closeadj
def df_f96_distress_flags_logdiff_21d_base_v095_signal(distressflag, closeadj):
    lr = _distress_flags_log(distressflag)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of distressflag times closeadj
def df_f96_distress_flags_logdiff_63d_base_v096_signal(distressflag, closeadj):
    lr = _distress_flags_log(distressflag)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of distressflag times closeadj
def df_f96_distress_flags_logdiff_252d_base_v097_signal(distressflag, closeadj):
    lr = _distress_flags_log(distressflag)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of distressflag times closeadj
def df_f96_distress_flags_range_63d_base_v098_signal(distressflag, closeadj):
    hi = distressflag.rolling(63, min_periods=max(1, 63//2)).max()
    lo = distressflag.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of distressflag times closeadj
def df_f96_distress_flags_range_252d_base_v099_signal(distressflag, closeadj):
    hi = distressflag.rolling(252, min_periods=max(1, 252//2)).max()
    lo = distressflag.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of distressflag times closeadj
def df_f96_distress_flags_range_504d_base_v100_signal(distressflag, closeadj):
    hi = distressflag.rolling(504, min_periods=max(1, 504//2)).max()
    lo = distressflag.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 252d mean times closeadj
def df_f96_distress_flags_rel_252d_base_v101_signal(distressflag, closeadj):
    m = _mean(distressflag, 252).replace(0, np.nan)
    result = (distressflag / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 504d mean times closeadj
def df_f96_distress_flags_rel_504d_base_v102_signal(distressflag, closeadj):
    m = _mean(distressflag, 504).replace(0, np.nan)
    result = (distressflag / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distressflag relative to 1008d mean times closeadj
def df_f96_distress_flags_rel_1008d_base_v103_signal(distressflag, closeadj):
    m = _mean(distressflag, 1008).replace(0, np.nan)
    result = (distressflag / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized distressflag/assets 63d mean
def df_f96_distress_flags_sqnorm_assets_63d_base_v104_signal(distressflag, assets):
    r = _distress_flags_scaled(distressflag, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized distressflag/assets 252d mean
def df_f96_distress_flags_sqnorm_assets_252d_base_v105_signal(distressflag, assets):
    r = _distress_flags_scaled(distressflag, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized distressflag/marketcap 63d mean
def df_f96_distress_flags_sqnorm_marketcap_63d_base_v106_signal(distressflag, marketcap):
    r = _distress_flags_scaled(distressflag, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized distressflag/marketcap 252d mean
def df_f96_distress_flags_sqnorm_marketcap_252d_base_v107_signal(distressflag, marketcap):
    r = _distress_flags_scaled(distressflag, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized distressflag/equity 63d mean
def df_f96_distress_flags_sqnorm_equity_63d_base_v108_signal(distressflag, equity):
    r = _distress_flags_scaled(distressflag, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized distressflag/equity 252d mean
def df_f96_distress_flags_sqnorm_equity_252d_base_v109_signal(distressflag, equity):
    r = _distress_flags_scaled(distressflag, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of distressflag times closeadj
def df_f96_distress_flags_infrat_63d_base_v110_signal(distressflag, closeadj):
    m = _mean(distressflag, 63)
    s = _std(distressflag, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of distressflag times closeadj
def df_f96_distress_flags_infrat_252d_base_v111_signal(distressflag, closeadj):
    m = _mean(distressflag, 252)
    s = _std(distressflag, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of distressflag times closeadj
def df_f96_distress_flags_infrat_504d_base_v112_signal(distressflag, closeadj):
    m = _mean(distressflag, 504)
    s = _std(distressflag, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of distressflag
def df_f96_distress_flags_cv_252d_base_v113_signal(distressflag):
    m = _mean(distressflag, 252).abs().replace(0, np.nan)
    s = _std(distressflag, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of distressflag
def df_f96_distress_flags_cv_504d_base_v114_signal(distressflag):
    m = _mean(distressflag, 504).abs().replace(0, np.nan)
    s = _std(distressflag, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged distressflag times closeadj
def df_f96_distress_flags_lag_5d_base_v115_signal(distressflag, closeadj):
    result = distressflag.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged distressflag times closeadj
def df_f96_distress_flags_lag_21d_base_v116_signal(distressflag, closeadj):
    result = distressflag.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged distressflag times closeadj
def df_f96_distress_flags_lag_63d_base_v117_signal(distressflag, closeadj):
    result = distressflag.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged distressflag times closeadj
def df_f96_distress_flags_lag_252d_base_v118_signal(distressflag, closeadj):
    result = distressflag.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(distressflag) / mean(assets) x closeadj
def df_f96_distress_flags_cumper_assets_252d_base_v119_signal(distressflag, assets, closeadj):
    s = distressflag.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(distressflag) / mean(assets) x closeadj
def df_f96_distress_flags_cumper_assets_504d_base_v120_signal(distressflag, assets, closeadj):
    s = distressflag.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(distressflag) / mean(marketcap) x closeadj
def df_f96_distress_flags_cumper_marketcap_252d_base_v121_signal(distressflag, marketcap, closeadj):
    s = distressflag.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(distressflag) / mean(marketcap) x closeadj
def df_f96_distress_flags_cumper_marketcap_504d_base_v122_signal(distressflag, marketcap, closeadj):
    s = distressflag.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only distressflag times closeadj
def df_f96_distress_flags_pos_63d_base_v123_signal(distressflag, closeadj):
    pos = distressflag.where(distressflag > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only distressflag times closeadj
def df_f96_distress_flags_pos_252d_base_v124_signal(distressflag, closeadj):
    pos = distressflag.where(distressflag > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only distressflag times closeadj
def df_f96_distress_flags_neg_63d_base_v125_signal(distressflag, closeadj):
    neg = distressflag.where(distressflag < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only distressflag times closeadj
def df_f96_distress_flags_neg_252d_base_v126_signal(distressflag, closeadj):
    neg = distressflag.where(distressflag < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of distressflag times closeadj
def df_f96_distress_flags_hl_21d_base_v127_signal(distressflag, closeadj):
    result = distressflag.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of distressflag times closeadj
def df_f96_distress_flags_hl_63d_base_v128_signal(distressflag, closeadj):
    result = distressflag.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of distressflag times closeadj
def df_f96_distress_flags_hl_252d_base_v129_signal(distressflag, closeadj):
    result = distressflag.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of distressflag
def df_f96_distress_flags_z_63d_base_v130_signal(distressflag):
    result = _z(distressflag, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of distressflag
def df_f96_distress_flags_z_126d_base_v131_signal(distressflag):
    result = _z(distressflag, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of distressflag
def df_f96_distress_flags_z_1008d_base_v132_signal(distressflag):
    result = _z(distressflag, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of distressflag times closeadj
def df_f96_distress_flags_st_lt_252_21d_base_v133_signal(distressflag, closeadj):
    sm = _mean(distressflag, 21)
    lm = _mean(distressflag, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of distressflag times closeadj
def df_f96_distress_flags_st_lt_252_63d_base_v134_signal(distressflag, closeadj):
    sm = _mean(distressflag, 63)
    lm = _mean(distressflag, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of distressflag times closeadj
def df_f96_distress_flags_st_lt_504_21d_base_v135_signal(distressflag, closeadj):
    sm = _mean(distressflag, 21)
    lm = _mean(distressflag, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of distressflag times closeadj
def df_f96_distress_flags_st_lt_504_63d_base_v136_signal(distressflag, closeadj):
    sm = _mean(distressflag, 63)
    lm = _mean(distressflag, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged distressflag/assets times closeadj
def df_f96_distress_flags_lag_per_assets_21d_base_v137_signal(distressflag, assets, closeadj):
    r = _distress_flags_scaled(distressflag, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged distressflag/assets times closeadj
def df_f96_distress_flags_lag_per_assets_63d_base_v138_signal(distressflag, assets, closeadj):
    r = _distress_flags_scaled(distressflag, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged distressflag/assets times closeadj
def df_f96_distress_flags_lag_per_assets_252d_base_v139_signal(distressflag, assets, closeadj):
    r = _distress_flags_scaled(distressflag, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged distressflag/marketcap times closeadj
def df_f96_distress_flags_lag_per_marketcap_21d_base_v140_signal(distressflag, marketcap, closeadj):
    r = _distress_flags_scaled(distressflag, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged distressflag/marketcap times closeadj
def df_f96_distress_flags_lag_per_marketcap_63d_base_v141_signal(distressflag, marketcap, closeadj):
    r = _distress_flags_scaled(distressflag, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged distressflag/marketcap times closeadj
def df_f96_distress_flags_lag_per_marketcap_252d_base_v142_signal(distressflag, marketcap, closeadj):
    r = _distress_flags_scaled(distressflag, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |distressflag| times closeadj
def df_f96_distress_flags_abssum_63d_base_v143_signal(distressflag, closeadj):
    result = distressflag.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |distressflag| times closeadj
def df_f96_distress_flags_abssum_252d_base_v144_signal(distressflag, closeadj):
    result = distressflag.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |distressflag| times closeadj
def df_f96_distress_flags_abssum_504d_base_v145_signal(distressflag, closeadj):
    result = distressflag.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of distressflag
def df_f96_distress_flags_acf1_252d_base_v146_signal(distressflag):
    result = distressflag.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of distressflag
def df_f96_distress_flags_acf1_504d_base_v147_signal(distressflag):
    result = distressflag.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of distressflag
def df_f96_distress_flags_posinrange_252d_base_v148_signal(distressflag):
    m = _mean(distressflag, 252)
    hi = distressflag.rolling(252, min_periods=max(1, 252//2)).max()
    lo = distressflag.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of distressflag
def df_f96_distress_flags_posinrange_504d_base_v149_signal(distressflag):
    m = _mean(distressflag, 504)
    hi = distressflag.rolling(504, min_periods=max(1, 504//2)).max()
    lo = distressflag.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of distressflag times closeadj
def df_f96_distress_flags_hl_5d_base_v150_signal(distressflag, closeadj):
    result = distressflag.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
