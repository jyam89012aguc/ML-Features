"""Family f06 - Quick ratio  (A_Liquidity_Runway) | base 076-150"""
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
def _quick_ratio_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _quick_ratio_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _quick_ratio_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of assetsc/marketcap
def qr_f06_quick_ratio_log_per_marketcap_504d_base_v076_signal(assetsc, marketcap):
    s = _quick_ratio_scaled(assetsc, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assetsc/equity
def qr_f06_quick_ratio_log_per_equity_252d_base_v077_signal(assetsc, equity):
    s = _quick_ratio_scaled(assetsc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of assetsc/equity
def qr_f06_quick_ratio_log_per_equity_504d_base_v078_signal(assetsc, equity):
    s = _quick_ratio_scaled(assetsc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of assetsc times closeadj
def qr_f06_quick_ratio_ewm_21d_base_v079_signal(assetsc, closeadj):
    result = assetsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of assetsc times closeadj
def qr_f06_quick_ratio_ewm_63d_base_v080_signal(assetsc, closeadj):
    result = assetsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of assetsc times closeadj
def qr_f06_quick_ratio_ewm_252d_base_v081_signal(assetsc, closeadj):
    result = assetsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of assetsc times closeadj
def qr_f06_quick_ratio_med_63d_base_v082_signal(assetsc, closeadj):
    result = assetsc.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of assetsc times closeadj
def qr_f06_quick_ratio_med_252d_base_v083_signal(assetsc, closeadj):
    result = assetsc.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of assetsc times closeadj
def qr_f06_quick_ratio_med_504d_base_v084_signal(assetsc, closeadj):
    result = assetsc.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of assetsc
def qr_f06_quick_ratio_skew_252d_base_v085_signal(assetsc):
    result = assetsc.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of assetsc
def qr_f06_quick_ratio_skew_504d_base_v086_signal(assetsc):
    result = assetsc.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of assetsc
def qr_f06_quick_ratio_kurt_252d_base_v087_signal(assetsc):
    result = assetsc.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of assetsc
def qr_f06_quick_ratio_kurt_504d_base_v088_signal(assetsc):
    result = assetsc.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of assetsc times closeadj
def qr_f06_quick_ratio_rank_252d_base_v089_signal(assetsc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assetsc.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of assetsc times closeadj
def qr_f06_quick_ratio_rank_504d_base_v090_signal(assetsc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assetsc.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of assetsc times closeadj
def qr_f06_quick_ratio_rank_1008d_base_v091_signal(assetsc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assetsc.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assetsc from 63d mean times closeadj
def qr_f06_quick_ratio_devmean_63d_base_v092_signal(assetsc, closeadj):
    m = _mean(assetsc, 63)
    result = (assetsc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assetsc from 252d mean times closeadj
def qr_f06_quick_ratio_devmean_252d_base_v093_signal(assetsc, closeadj):
    m = _mean(assetsc, 252)
    result = (assetsc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assetsc from 504d mean times closeadj
def qr_f06_quick_ratio_devmean_504d_base_v094_signal(assetsc, closeadj):
    m = _mean(assetsc, 504)
    result = (assetsc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of assetsc times closeadj
def qr_f06_quick_ratio_logdiff_21d_base_v095_signal(assetsc, closeadj):
    lr = _quick_ratio_log(assetsc)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of assetsc times closeadj
def qr_f06_quick_ratio_logdiff_63d_base_v096_signal(assetsc, closeadj):
    lr = _quick_ratio_log(assetsc)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of assetsc times closeadj
def qr_f06_quick_ratio_logdiff_252d_base_v097_signal(assetsc, closeadj):
    lr = _quick_ratio_log(assetsc)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of assetsc times closeadj
def qr_f06_quick_ratio_range_63d_base_v098_signal(assetsc, closeadj):
    hi = assetsc.rolling(63, min_periods=max(1, 63//2)).max()
    lo = assetsc.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of assetsc times closeadj
def qr_f06_quick_ratio_range_252d_base_v099_signal(assetsc, closeadj):
    hi = assetsc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = assetsc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of assetsc times closeadj
def qr_f06_quick_ratio_range_504d_base_v100_signal(assetsc, closeadj):
    hi = assetsc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = assetsc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 252d mean times closeadj
def qr_f06_quick_ratio_rel_252d_base_v101_signal(assetsc, closeadj):
    m = _mean(assetsc, 252).replace(0, np.nan)
    result = (assetsc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 504d mean times closeadj
def qr_f06_quick_ratio_rel_504d_base_v102_signal(assetsc, closeadj):
    m = _mean(assetsc, 504).replace(0, np.nan)
    result = (assetsc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetsc relative to 1008d mean times closeadj
def qr_f06_quick_ratio_rel_1008d_base_v103_signal(assetsc, closeadj):
    m = _mean(assetsc, 1008).replace(0, np.nan)
    result = (assetsc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetsc/assets 63d mean
def qr_f06_quick_ratio_sqnorm_assets_63d_base_v104_signal(assetsc, assets):
    r = _quick_ratio_scaled(assetsc, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetsc/assets 252d mean
def qr_f06_quick_ratio_sqnorm_assets_252d_base_v105_signal(assetsc, assets):
    r = _quick_ratio_scaled(assetsc, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetsc/marketcap 63d mean
def qr_f06_quick_ratio_sqnorm_marketcap_63d_base_v106_signal(assetsc, marketcap):
    r = _quick_ratio_scaled(assetsc, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetsc/marketcap 252d mean
def qr_f06_quick_ratio_sqnorm_marketcap_252d_base_v107_signal(assetsc, marketcap):
    r = _quick_ratio_scaled(assetsc, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetsc/equity 63d mean
def qr_f06_quick_ratio_sqnorm_equity_63d_base_v108_signal(assetsc, equity):
    r = _quick_ratio_scaled(assetsc, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assetsc/equity 252d mean
def qr_f06_quick_ratio_sqnorm_equity_252d_base_v109_signal(assetsc, equity):
    r = _quick_ratio_scaled(assetsc, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of assetsc times closeadj
def qr_f06_quick_ratio_infrat_63d_base_v110_signal(assetsc, closeadj):
    m = _mean(assetsc, 63)
    s = _std(assetsc, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of assetsc times closeadj
def qr_f06_quick_ratio_infrat_252d_base_v111_signal(assetsc, closeadj):
    m = _mean(assetsc, 252)
    s = _std(assetsc, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of assetsc times closeadj
def qr_f06_quick_ratio_infrat_504d_base_v112_signal(assetsc, closeadj):
    m = _mean(assetsc, 504)
    s = _std(assetsc, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of assetsc
def qr_f06_quick_ratio_cv_252d_base_v113_signal(assetsc):
    m = _mean(assetsc, 252).abs().replace(0, np.nan)
    s = _std(assetsc, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of assetsc
def qr_f06_quick_ratio_cv_504d_base_v114_signal(assetsc):
    m = _mean(assetsc, 504).abs().replace(0, np.nan)
    s = _std(assetsc, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged assetsc times closeadj
def qr_f06_quick_ratio_lag_5d_base_v115_signal(assetsc, closeadj):
    result = assetsc.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assetsc times closeadj
def qr_f06_quick_ratio_lag_21d_base_v116_signal(assetsc, closeadj):
    result = assetsc.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assetsc times closeadj
def qr_f06_quick_ratio_lag_63d_base_v117_signal(assetsc, closeadj):
    result = assetsc.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assetsc times closeadj
def qr_f06_quick_ratio_lag_252d_base_v118_signal(assetsc, closeadj):
    result = assetsc.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(assetsc) / mean(assets) x closeadj
def qr_f06_quick_ratio_cumper_assets_252d_base_v119_signal(assetsc, assets, closeadj):
    s = assetsc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(assetsc) / mean(assets) x closeadj
def qr_f06_quick_ratio_cumper_assets_504d_base_v120_signal(assetsc, assets, closeadj):
    s = assetsc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(assetsc) / mean(marketcap) x closeadj
def qr_f06_quick_ratio_cumper_marketcap_252d_base_v121_signal(assetsc, marketcap, closeadj):
    s = assetsc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(assetsc) / mean(marketcap) x closeadj
def qr_f06_quick_ratio_cumper_marketcap_504d_base_v122_signal(assetsc, marketcap, closeadj):
    s = assetsc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only assetsc times closeadj
def qr_f06_quick_ratio_pos_63d_base_v123_signal(assetsc, closeadj):
    pos = assetsc.where(assetsc > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only assetsc times closeadj
def qr_f06_quick_ratio_pos_252d_base_v124_signal(assetsc, closeadj):
    pos = assetsc.where(assetsc > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only assetsc times closeadj
def qr_f06_quick_ratio_neg_63d_base_v125_signal(assetsc, closeadj):
    neg = assetsc.where(assetsc < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only assetsc times closeadj
def qr_f06_quick_ratio_neg_252d_base_v126_signal(assetsc, closeadj):
    neg = assetsc.where(assetsc < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of assetsc times closeadj
def qr_f06_quick_ratio_hl_21d_base_v127_signal(assetsc, closeadj):
    result = assetsc.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of assetsc times closeadj
def qr_f06_quick_ratio_hl_63d_base_v128_signal(assetsc, closeadj):
    result = assetsc.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of assetsc times closeadj
def qr_f06_quick_ratio_hl_252d_base_v129_signal(assetsc, closeadj):
    result = assetsc.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of assetsc
def qr_f06_quick_ratio_z_63d_base_v130_signal(assetsc):
    result = _z(assetsc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of assetsc
def qr_f06_quick_ratio_z_126d_base_v131_signal(assetsc):
    result = _z(assetsc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of assetsc
def qr_f06_quick_ratio_z_1008d_base_v132_signal(assetsc):
    result = _z(assetsc, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of assetsc times closeadj
def qr_f06_quick_ratio_st_lt_252_21d_base_v133_signal(assetsc, closeadj):
    sm = _mean(assetsc, 21)
    lm = _mean(assetsc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of assetsc times closeadj
def qr_f06_quick_ratio_st_lt_252_63d_base_v134_signal(assetsc, closeadj):
    sm = _mean(assetsc, 63)
    lm = _mean(assetsc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of assetsc times closeadj
def qr_f06_quick_ratio_st_lt_504_21d_base_v135_signal(assetsc, closeadj):
    sm = _mean(assetsc, 21)
    lm = _mean(assetsc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of assetsc times closeadj
def qr_f06_quick_ratio_st_lt_504_63d_base_v136_signal(assetsc, closeadj):
    sm = _mean(assetsc, 63)
    lm = _mean(assetsc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assetsc/assets times closeadj
def qr_f06_quick_ratio_lag_per_assets_21d_base_v137_signal(assetsc, assets, closeadj):
    r = _quick_ratio_scaled(assetsc, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assetsc/assets times closeadj
def qr_f06_quick_ratio_lag_per_assets_63d_base_v138_signal(assetsc, assets, closeadj):
    r = _quick_ratio_scaled(assetsc, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assetsc/assets times closeadj
def qr_f06_quick_ratio_lag_per_assets_252d_base_v139_signal(assetsc, assets, closeadj):
    r = _quick_ratio_scaled(assetsc, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assetsc/marketcap times closeadj
def qr_f06_quick_ratio_lag_per_marketcap_21d_base_v140_signal(assetsc, marketcap, closeadj):
    r = _quick_ratio_scaled(assetsc, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assetsc/marketcap times closeadj
def qr_f06_quick_ratio_lag_per_marketcap_63d_base_v141_signal(assetsc, marketcap, closeadj):
    r = _quick_ratio_scaled(assetsc, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assetsc/marketcap times closeadj
def qr_f06_quick_ratio_lag_per_marketcap_252d_base_v142_signal(assetsc, marketcap, closeadj):
    r = _quick_ratio_scaled(assetsc, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |assetsc| times closeadj
def qr_f06_quick_ratio_abssum_63d_base_v143_signal(assetsc, closeadj):
    result = assetsc.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |assetsc| times closeadj
def qr_f06_quick_ratio_abssum_252d_base_v144_signal(assetsc, closeadj):
    result = assetsc.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |assetsc| times closeadj
def qr_f06_quick_ratio_abssum_504d_base_v145_signal(assetsc, closeadj):
    result = assetsc.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of assetsc
def qr_f06_quick_ratio_acf1_252d_base_v146_signal(assetsc):
    result = assetsc.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of assetsc
def qr_f06_quick_ratio_acf1_504d_base_v147_signal(assetsc):
    result = assetsc.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of assetsc
def qr_f06_quick_ratio_posinrange_252d_base_v148_signal(assetsc):
    m = _mean(assetsc, 252)
    hi = assetsc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = assetsc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of assetsc
def qr_f06_quick_ratio_posinrange_504d_base_v149_signal(assetsc):
    m = _mean(assetsc, 504)
    hi = assetsc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = assetsc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of assetsc times closeadj
def qr_f06_quick_ratio_hl_5d_base_v150_signal(assetsc, closeadj):
    result = assetsc.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
