"""Family f039 - Total asset base (Balance Sheet Composition) | Sharadar tables: SF1 | fields: assets, assetsavg, assetsc | base 076-150"""
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
def _asset_base_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _asset_base_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _asset_base_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of assets/assetsc
def ab_f039_asset_base_log_per_assetsc_504d_base_v076_signal(assets, assetsc):
    s = _asset_base_scaled(assets, assetsc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assets/marketcap
def ab_f039_asset_base_log_per_marketcap_252d_base_v077_signal(assets, marketcap):
    s = _asset_base_scaled(assets, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of assets/marketcap
def ab_f039_asset_base_log_per_marketcap_504d_base_v078_signal(assets, marketcap):
    s = _asset_base_scaled(assets, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of assets times closeadj
def ab_f039_asset_base_ewm_21d_base_v079_signal(assets, closeadj):
    result = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of assets times closeadj
def ab_f039_asset_base_ewm_63d_base_v080_signal(assets, closeadj):
    result = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of assets times closeadj
def ab_f039_asset_base_ewm_252d_base_v081_signal(assets, closeadj):
    result = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of assets times closeadj
def ab_f039_asset_base_med_63d_base_v082_signal(assets, closeadj):
    result = assets.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of assets times closeadj
def ab_f039_asset_base_med_252d_base_v083_signal(assets, closeadj):
    result = assets.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of assets times closeadj
def ab_f039_asset_base_med_504d_base_v084_signal(assets, closeadj):
    result = assets.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of assets
def ab_f039_asset_base_skew_252d_base_v085_signal(assets):
    result = assets.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of assets
def ab_f039_asset_base_skew_504d_base_v086_signal(assets):
    result = assets.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of assets
def ab_f039_asset_base_kurt_252d_base_v087_signal(assets):
    result = assets.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of assets
def ab_f039_asset_base_kurt_504d_base_v088_signal(assets):
    result = assets.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of assets times closeadj
def ab_f039_asset_base_rank_252d_base_v089_signal(assets, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assets.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of assets times closeadj
def ab_f039_asset_base_rank_504d_base_v090_signal(assets, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assets.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of assets times closeadj
def ab_f039_asset_base_rank_1008d_base_v091_signal(assets, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = assets.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assets from 63d mean times closeadj
def ab_f039_asset_base_devmean_63d_base_v092_signal(assets, closeadj):
    m = _mean(assets, 63)
    result = (assets - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assets from 252d mean times closeadj
def ab_f039_asset_base_devmean_252d_base_v093_signal(assets, closeadj):
    m = _mean(assets, 252)
    result = (assets - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of assets from 504d mean times closeadj
def ab_f039_asset_base_devmean_504d_base_v094_signal(assets, closeadj):
    m = _mean(assets, 504)
    result = (assets - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of assets times closeadj
def ab_f039_asset_base_logdiff_21d_base_v095_signal(assets, closeadj):
    lr = _asset_base_log(assets)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of assets times closeadj
def ab_f039_asset_base_logdiff_63d_base_v096_signal(assets, closeadj):
    lr = _asset_base_log(assets)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of assets times closeadj
def ab_f039_asset_base_logdiff_252d_base_v097_signal(assets, closeadj):
    lr = _asset_base_log(assets)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of assets times closeadj
def ab_f039_asset_base_range_63d_base_v098_signal(assets, closeadj):
    hi = assets.rolling(63, min_periods=max(1, 63//2)).max()
    lo = assets.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of assets times closeadj
def ab_f039_asset_base_range_252d_base_v099_signal(assets, closeadj):
    hi = assets.rolling(252, min_periods=max(1, 252//2)).max()
    lo = assets.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of assets times closeadj
def ab_f039_asset_base_range_504d_base_v100_signal(assets, closeadj):
    hi = assets.rolling(504, min_periods=max(1, 504//2)).max()
    lo = assets.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 252d mean times closeadj
def ab_f039_asset_base_rel_252d_base_v101_signal(assets, closeadj):
    m = _mean(assets, 252).replace(0, np.nan)
    result = (assets / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 504d mean times closeadj
def ab_f039_asset_base_rel_504d_base_v102_signal(assets, closeadj):
    m = _mean(assets, 504).replace(0, np.nan)
    result = (assets / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 1008d mean times closeadj
def ab_f039_asset_base_rel_1008d_base_v103_signal(assets, closeadj):
    m = _mean(assets, 1008).replace(0, np.nan)
    result = (assets / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assets/assetsavg 63d mean
def ab_f039_asset_base_sqnorm_assetsavg_63d_base_v104_signal(assets, assetsavg):
    r = _asset_base_scaled(assets, assetsavg)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assets/assetsavg 252d mean
def ab_f039_asset_base_sqnorm_assetsavg_252d_base_v105_signal(assets, assetsavg):
    r = _asset_base_scaled(assets, assetsavg)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assets/assetsc 63d mean
def ab_f039_asset_base_sqnorm_assetsc_63d_base_v106_signal(assets, assetsc):
    r = _asset_base_scaled(assets, assetsc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assets/assetsc 252d mean
def ab_f039_asset_base_sqnorm_assetsc_252d_base_v107_signal(assets, assetsc):
    r = _asset_base_scaled(assets, assetsc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assets/marketcap 63d mean
def ab_f039_asset_base_sqnorm_marketcap_63d_base_v108_signal(assets, marketcap):
    r = _asset_base_scaled(assets, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized assets/marketcap 252d mean
def ab_f039_asset_base_sqnorm_marketcap_252d_base_v109_signal(assets, marketcap):
    r = _asset_base_scaled(assets, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of assets times closeadj
def ab_f039_asset_base_infrat_63d_base_v110_signal(assets, closeadj):
    m = _mean(assets, 63)
    s = _std(assets, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of assets times closeadj
def ab_f039_asset_base_infrat_252d_base_v111_signal(assets, closeadj):
    m = _mean(assets, 252)
    s = _std(assets, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of assets times closeadj
def ab_f039_asset_base_infrat_504d_base_v112_signal(assets, closeadj):
    m = _mean(assets, 504)
    s = _std(assets, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of assets
def ab_f039_asset_base_cv_252d_base_v113_signal(assets):
    m = _mean(assets, 252).abs().replace(0, np.nan)
    s = _std(assets, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of assets
def ab_f039_asset_base_cv_504d_base_v114_signal(assets):
    m = _mean(assets, 504).abs().replace(0, np.nan)
    s = _std(assets, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged assets times closeadj
def ab_f039_asset_base_lag_5d_base_v115_signal(assets, closeadj):
    result = assets.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assets times closeadj
def ab_f039_asset_base_lag_21d_base_v116_signal(assets, closeadj):
    result = assets.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assets times closeadj
def ab_f039_asset_base_lag_63d_base_v117_signal(assets, closeadj):
    result = assets.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assets times closeadj
def ab_f039_asset_base_lag_252d_base_v118_signal(assets, closeadj):
    result = assets.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(assets) / mean(assetsavg) x closeadj
def ab_f039_asset_base_cumper_assetsavg_252d_base_v119_signal(assets, assetsavg, closeadj):
    s = assets.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assetsavg, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(assets) / mean(assetsavg) x closeadj
def ab_f039_asset_base_cumper_assetsavg_504d_base_v120_signal(assets, assetsavg, closeadj):
    s = assets.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assetsavg, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(assets) / mean(assetsc) x closeadj
def ab_f039_asset_base_cumper_assetsc_252d_base_v121_signal(assets, assetsc, closeadj):
    s = assets.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assetsc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(assets) / mean(assetsc) x closeadj
def ab_f039_asset_base_cumper_assetsc_504d_base_v122_signal(assets, assetsc, closeadj):
    s = assets.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assetsc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only assets times closeadj
def ab_f039_asset_base_pos_63d_base_v123_signal(assets, closeadj):
    pos = assets.where(assets > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only assets times closeadj
def ab_f039_asset_base_pos_252d_base_v124_signal(assets, closeadj):
    pos = assets.where(assets > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only assets times closeadj
def ab_f039_asset_base_neg_63d_base_v125_signal(assets, closeadj):
    neg = assets.where(assets < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only assets times closeadj
def ab_f039_asset_base_neg_252d_base_v126_signal(assets, closeadj):
    neg = assets.where(assets < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of assets times closeadj
def ab_f039_asset_base_hl_21d_base_v127_signal(assets, closeadj):
    result = assets.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of assets times closeadj
def ab_f039_asset_base_hl_63d_base_v128_signal(assets, closeadj):
    result = assets.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of assets times closeadj
def ab_f039_asset_base_hl_252d_base_v129_signal(assets, closeadj):
    result = assets.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of assets
def ab_f039_asset_base_z_63d_base_v130_signal(assets):
    result = _z(assets, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of assets
def ab_f039_asset_base_z_126d_base_v131_signal(assets):
    result = _z(assets, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of assets
def ab_f039_asset_base_z_1008d_base_v132_signal(assets):
    result = _z(assets, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of assets times closeadj
def ab_f039_asset_base_st_lt_252_21d_base_v133_signal(assets, closeadj):
    sm = _mean(assets, 21)
    lm = _mean(assets, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of assets times closeadj
def ab_f039_asset_base_st_lt_252_63d_base_v134_signal(assets, closeadj):
    sm = _mean(assets, 63)
    lm = _mean(assets, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of assets times closeadj
def ab_f039_asset_base_st_lt_504_21d_base_v135_signal(assets, closeadj):
    sm = _mean(assets, 21)
    lm = _mean(assets, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of assets times closeadj
def ab_f039_asset_base_st_lt_504_63d_base_v136_signal(assets, closeadj):
    sm = _mean(assets, 63)
    lm = _mean(assets, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assets/assetsavg times closeadj
def ab_f039_asset_base_lag_per_assetsavg_21d_base_v137_signal(assets, assetsavg, closeadj):
    r = _asset_base_scaled(assets, assetsavg)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assets/assetsavg times closeadj
def ab_f039_asset_base_lag_per_assetsavg_63d_base_v138_signal(assets, assetsavg, closeadj):
    r = _asset_base_scaled(assets, assetsavg)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assets/assetsavg times closeadj
def ab_f039_asset_base_lag_per_assetsavg_252d_base_v139_signal(assets, assetsavg, closeadj):
    r = _asset_base_scaled(assets, assetsavg)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged assets/assetsc times closeadj
def ab_f039_asset_base_lag_per_assetsc_21d_base_v140_signal(assets, assetsc, closeadj):
    r = _asset_base_scaled(assets, assetsc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged assets/assetsc times closeadj
def ab_f039_asset_base_lag_per_assetsc_63d_base_v141_signal(assets, assetsc, closeadj):
    r = _asset_base_scaled(assets, assetsc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged assets/assetsc times closeadj
def ab_f039_asset_base_lag_per_assetsc_252d_base_v142_signal(assets, assetsc, closeadj):
    r = _asset_base_scaled(assets, assetsc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |assets| times closeadj
def ab_f039_asset_base_abssum_63d_base_v143_signal(assets, closeadj):
    result = assets.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |assets| times closeadj
def ab_f039_asset_base_abssum_252d_base_v144_signal(assets, closeadj):
    result = assets.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |assets| times closeadj
def ab_f039_asset_base_abssum_504d_base_v145_signal(assets, closeadj):
    result = assets.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of assets
def ab_f039_asset_base_acf1_252d_base_v146_signal(assets):
    result = assets.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of assets
def ab_f039_asset_base_acf1_504d_base_v147_signal(assets):
    result = assets.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of assets
def ab_f039_asset_base_posinrange_252d_base_v148_signal(assets):
    m = _mean(assets, 252)
    hi = assets.rolling(252, min_periods=max(1, 252//2)).max()
    lo = assets.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of assets
def ab_f039_asset_base_posinrange_504d_base_v149_signal(assets):
    m = _mean(assets, 504)
    hi = assets.rolling(504, min_periods=max(1, 504//2)).max()
    lo = assets.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of assets times closeadj
def ab_f039_asset_base_hl_5d_base_v150_signal(assets, closeadj):
    result = assets.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
