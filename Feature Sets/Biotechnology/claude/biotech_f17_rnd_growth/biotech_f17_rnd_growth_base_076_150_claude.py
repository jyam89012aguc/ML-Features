"""Family f17 - R&D growth rate  (C_RnD_Innovation) | base 076-150"""
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
def _rnd_growth_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _rnd_growth_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _rnd_growth_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of rnd/marketcap
def rg_f17_rnd_growth_log_per_marketcap_504d_base_v076_signal(rnd, marketcap):
    s = _rnd_growth_scaled(rnd, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of rnd/equity
def rg_f17_rnd_growth_log_per_equity_252d_base_v077_signal(rnd, equity):
    s = _rnd_growth_scaled(rnd, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of rnd/equity
def rg_f17_rnd_growth_log_per_equity_504d_base_v078_signal(rnd, equity):
    s = _rnd_growth_scaled(rnd, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of rnd times closeadj
def rg_f17_rnd_growth_ewm_21d_base_v079_signal(rnd, closeadj):
    result = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of rnd times closeadj
def rg_f17_rnd_growth_ewm_63d_base_v080_signal(rnd, closeadj):
    result = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of rnd times closeadj
def rg_f17_rnd_growth_ewm_252d_base_v081_signal(rnd, closeadj):
    result = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of rnd times closeadj
def rg_f17_rnd_growth_med_63d_base_v082_signal(rnd, closeadj):
    result = rnd.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of rnd times closeadj
def rg_f17_rnd_growth_med_252d_base_v083_signal(rnd, closeadj):
    result = rnd.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of rnd times closeadj
def rg_f17_rnd_growth_med_504d_base_v084_signal(rnd, closeadj):
    result = rnd.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of rnd
def rg_f17_rnd_growth_skew_252d_base_v085_signal(rnd):
    result = rnd.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of rnd
def rg_f17_rnd_growth_skew_504d_base_v086_signal(rnd):
    result = rnd.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of rnd
def rg_f17_rnd_growth_kurt_252d_base_v087_signal(rnd):
    result = rnd.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of rnd
def rg_f17_rnd_growth_kurt_504d_base_v088_signal(rnd):
    result = rnd.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of rnd times closeadj
def rg_f17_rnd_growth_rank_252d_base_v089_signal(rnd, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = rnd.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of rnd times closeadj
def rg_f17_rnd_growth_rank_504d_base_v090_signal(rnd, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = rnd.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of rnd times closeadj
def rg_f17_rnd_growth_rank_1008d_base_v091_signal(rnd, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = rnd.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of rnd from 63d mean times closeadj
def rg_f17_rnd_growth_devmean_63d_base_v092_signal(rnd, closeadj):
    m = _mean(rnd, 63)
    result = (rnd - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of rnd from 252d mean times closeadj
def rg_f17_rnd_growth_devmean_252d_base_v093_signal(rnd, closeadj):
    m = _mean(rnd, 252)
    result = (rnd - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of rnd from 504d mean times closeadj
def rg_f17_rnd_growth_devmean_504d_base_v094_signal(rnd, closeadj):
    m = _mean(rnd, 504)
    result = (rnd - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of rnd times closeadj
def rg_f17_rnd_growth_logdiff_21d_base_v095_signal(rnd, closeadj):
    lr = _rnd_growth_log(rnd)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of rnd times closeadj
def rg_f17_rnd_growth_logdiff_63d_base_v096_signal(rnd, closeadj):
    lr = _rnd_growth_log(rnd)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of rnd times closeadj
def rg_f17_rnd_growth_logdiff_252d_base_v097_signal(rnd, closeadj):
    lr = _rnd_growth_log(rnd)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of rnd times closeadj
def rg_f17_rnd_growth_range_63d_base_v098_signal(rnd, closeadj):
    hi = rnd.rolling(63, min_periods=max(1, 63//2)).max()
    lo = rnd.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of rnd times closeadj
def rg_f17_rnd_growth_range_252d_base_v099_signal(rnd, closeadj):
    hi = rnd.rolling(252, min_periods=max(1, 252//2)).max()
    lo = rnd.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of rnd times closeadj
def rg_f17_rnd_growth_range_504d_base_v100_signal(rnd, closeadj):
    hi = rnd.rolling(504, min_periods=max(1, 504//2)).max()
    lo = rnd.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 252d mean times closeadj
def rg_f17_rnd_growth_rel_252d_base_v101_signal(rnd, closeadj):
    m = _mean(rnd, 252).replace(0, np.nan)
    result = (rnd / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 504d mean times closeadj
def rg_f17_rnd_growth_rel_504d_base_v102_signal(rnd, closeadj):
    m = _mean(rnd, 504).replace(0, np.nan)
    result = (rnd / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rnd relative to 1008d mean times closeadj
def rg_f17_rnd_growth_rel_1008d_base_v103_signal(rnd, closeadj):
    m = _mean(rnd, 1008).replace(0, np.nan)
    result = (rnd / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized rnd/assets 63d mean
def rg_f17_rnd_growth_sqnorm_assets_63d_base_v104_signal(rnd, assets):
    r = _rnd_growth_scaled(rnd, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized rnd/assets 252d mean
def rg_f17_rnd_growth_sqnorm_assets_252d_base_v105_signal(rnd, assets):
    r = _rnd_growth_scaled(rnd, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized rnd/marketcap 63d mean
def rg_f17_rnd_growth_sqnorm_marketcap_63d_base_v106_signal(rnd, marketcap):
    r = _rnd_growth_scaled(rnd, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized rnd/marketcap 252d mean
def rg_f17_rnd_growth_sqnorm_marketcap_252d_base_v107_signal(rnd, marketcap):
    r = _rnd_growth_scaled(rnd, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized rnd/equity 63d mean
def rg_f17_rnd_growth_sqnorm_equity_63d_base_v108_signal(rnd, equity):
    r = _rnd_growth_scaled(rnd, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized rnd/equity 252d mean
def rg_f17_rnd_growth_sqnorm_equity_252d_base_v109_signal(rnd, equity):
    r = _rnd_growth_scaled(rnd, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of rnd times closeadj
def rg_f17_rnd_growth_infrat_63d_base_v110_signal(rnd, closeadj):
    m = _mean(rnd, 63)
    s = _std(rnd, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of rnd times closeadj
def rg_f17_rnd_growth_infrat_252d_base_v111_signal(rnd, closeadj):
    m = _mean(rnd, 252)
    s = _std(rnd, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of rnd times closeadj
def rg_f17_rnd_growth_infrat_504d_base_v112_signal(rnd, closeadj):
    m = _mean(rnd, 504)
    s = _std(rnd, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of rnd
def rg_f17_rnd_growth_cv_252d_base_v113_signal(rnd):
    m = _mean(rnd, 252).abs().replace(0, np.nan)
    s = _std(rnd, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of rnd
def rg_f17_rnd_growth_cv_504d_base_v114_signal(rnd):
    m = _mean(rnd, 504).abs().replace(0, np.nan)
    s = _std(rnd, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged rnd times closeadj
def rg_f17_rnd_growth_lag_5d_base_v115_signal(rnd, closeadj):
    result = rnd.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged rnd times closeadj
def rg_f17_rnd_growth_lag_21d_base_v116_signal(rnd, closeadj):
    result = rnd.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged rnd times closeadj
def rg_f17_rnd_growth_lag_63d_base_v117_signal(rnd, closeadj):
    result = rnd.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged rnd times closeadj
def rg_f17_rnd_growth_lag_252d_base_v118_signal(rnd, closeadj):
    result = rnd.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(rnd) / mean(assets) x closeadj
def rg_f17_rnd_growth_cumper_assets_252d_base_v119_signal(rnd, assets, closeadj):
    s = rnd.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(rnd) / mean(assets) x closeadj
def rg_f17_rnd_growth_cumper_assets_504d_base_v120_signal(rnd, assets, closeadj):
    s = rnd.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(rnd) / mean(marketcap) x closeadj
def rg_f17_rnd_growth_cumper_marketcap_252d_base_v121_signal(rnd, marketcap, closeadj):
    s = rnd.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(rnd) / mean(marketcap) x closeadj
def rg_f17_rnd_growth_cumper_marketcap_504d_base_v122_signal(rnd, marketcap, closeadj):
    s = rnd.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only rnd times closeadj
def rg_f17_rnd_growth_pos_63d_base_v123_signal(rnd, closeadj):
    pos = rnd.where(rnd > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only rnd times closeadj
def rg_f17_rnd_growth_pos_252d_base_v124_signal(rnd, closeadj):
    pos = rnd.where(rnd > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only rnd times closeadj
def rg_f17_rnd_growth_neg_63d_base_v125_signal(rnd, closeadj):
    neg = rnd.where(rnd < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only rnd times closeadj
def rg_f17_rnd_growth_neg_252d_base_v126_signal(rnd, closeadj):
    neg = rnd.where(rnd < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of rnd times closeadj
def rg_f17_rnd_growth_hl_21d_base_v127_signal(rnd, closeadj):
    result = rnd.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of rnd times closeadj
def rg_f17_rnd_growth_hl_63d_base_v128_signal(rnd, closeadj):
    result = rnd.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of rnd times closeadj
def rg_f17_rnd_growth_hl_252d_base_v129_signal(rnd, closeadj):
    result = rnd.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of rnd
def rg_f17_rnd_growth_z_63d_base_v130_signal(rnd):
    result = _z(rnd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of rnd
def rg_f17_rnd_growth_z_126d_base_v131_signal(rnd):
    result = _z(rnd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of rnd
def rg_f17_rnd_growth_z_1008d_base_v132_signal(rnd):
    result = _z(rnd, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of rnd times closeadj
def rg_f17_rnd_growth_st_lt_252_21d_base_v133_signal(rnd, closeadj):
    sm = _mean(rnd, 21)
    lm = _mean(rnd, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of rnd times closeadj
def rg_f17_rnd_growth_st_lt_252_63d_base_v134_signal(rnd, closeadj):
    sm = _mean(rnd, 63)
    lm = _mean(rnd, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of rnd times closeadj
def rg_f17_rnd_growth_st_lt_504_21d_base_v135_signal(rnd, closeadj):
    sm = _mean(rnd, 21)
    lm = _mean(rnd, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of rnd times closeadj
def rg_f17_rnd_growth_st_lt_504_63d_base_v136_signal(rnd, closeadj):
    sm = _mean(rnd, 63)
    lm = _mean(rnd, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged rnd/assets times closeadj
def rg_f17_rnd_growth_lag_per_assets_21d_base_v137_signal(rnd, assets, closeadj):
    r = _rnd_growth_scaled(rnd, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged rnd/assets times closeadj
def rg_f17_rnd_growth_lag_per_assets_63d_base_v138_signal(rnd, assets, closeadj):
    r = _rnd_growth_scaled(rnd, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged rnd/assets times closeadj
def rg_f17_rnd_growth_lag_per_assets_252d_base_v139_signal(rnd, assets, closeadj):
    r = _rnd_growth_scaled(rnd, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged rnd/marketcap times closeadj
def rg_f17_rnd_growth_lag_per_marketcap_21d_base_v140_signal(rnd, marketcap, closeadj):
    r = _rnd_growth_scaled(rnd, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged rnd/marketcap times closeadj
def rg_f17_rnd_growth_lag_per_marketcap_63d_base_v141_signal(rnd, marketcap, closeadj):
    r = _rnd_growth_scaled(rnd, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged rnd/marketcap times closeadj
def rg_f17_rnd_growth_lag_per_marketcap_252d_base_v142_signal(rnd, marketcap, closeadj):
    r = _rnd_growth_scaled(rnd, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |rnd| times closeadj
def rg_f17_rnd_growth_abssum_63d_base_v143_signal(rnd, closeadj):
    result = rnd.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |rnd| times closeadj
def rg_f17_rnd_growth_abssum_252d_base_v144_signal(rnd, closeadj):
    result = rnd.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |rnd| times closeadj
def rg_f17_rnd_growth_abssum_504d_base_v145_signal(rnd, closeadj):
    result = rnd.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of rnd
def rg_f17_rnd_growth_acf1_252d_base_v146_signal(rnd):
    result = rnd.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of rnd
def rg_f17_rnd_growth_acf1_504d_base_v147_signal(rnd):
    result = rnd.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of rnd
def rg_f17_rnd_growth_posinrange_252d_base_v148_signal(rnd):
    m = _mean(rnd, 252)
    hi = rnd.rolling(252, min_periods=max(1, 252//2)).max()
    lo = rnd.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of rnd
def rg_f17_rnd_growth_posinrange_504d_base_v149_signal(rnd):
    m = _mean(rnd, 504)
    hi = rnd.rolling(504, min_periods=max(1, 504//2)).max()
    lo = rnd.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of rnd times closeadj
def rg_f17_rnd_growth_hl_5d_base_v150_signal(rnd, closeadj):
    result = rnd.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
