"""Family f063 - Return on assets (Returns and Efficiency) | Sharadar tables: SF1 | fields: roa, netinc, assetsavg | base 076-150"""
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
def _return_on_assets_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_assets_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_assets_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of roa/assetsavg
def roa_f063_return_on_assets_log_per_assetsavg_504d_base_v076_signal(roa, assetsavg):
    s = _return_on_assets_scaled(roa, assetsavg)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roa/assets
def roa_f063_return_on_assets_log_per_assets_252d_base_v077_signal(roa, assets):
    s = _return_on_assets_scaled(roa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of roa/assets
def roa_f063_return_on_assets_log_per_assets_504d_base_v078_signal(roa, assets):
    s = _return_on_assets_scaled(roa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of roa times closeadj
def roa_f063_return_on_assets_ewm_21d_base_v079_signal(roa, closeadj):
    result = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of roa times closeadj
def roa_f063_return_on_assets_ewm_63d_base_v080_signal(roa, closeadj):
    result = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of roa times closeadj
def roa_f063_return_on_assets_ewm_252d_base_v081_signal(roa, closeadj):
    result = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of roa times closeadj
def roa_f063_return_on_assets_med_63d_base_v082_signal(roa, closeadj):
    result = roa.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of roa times closeadj
def roa_f063_return_on_assets_med_252d_base_v083_signal(roa, closeadj):
    result = roa.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of roa times closeadj
def roa_f063_return_on_assets_med_504d_base_v084_signal(roa, closeadj):
    result = roa.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of roa
def roa_f063_return_on_assets_skew_252d_base_v085_signal(roa):
    result = roa.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of roa
def roa_f063_return_on_assets_skew_504d_base_v086_signal(roa):
    result = roa.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of roa
def roa_f063_return_on_assets_kurt_252d_base_v087_signal(roa):
    result = roa.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of roa
def roa_f063_return_on_assets_kurt_504d_base_v088_signal(roa):
    result = roa.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of roa times closeadj
def roa_f063_return_on_assets_rank_252d_base_v089_signal(roa, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roa.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of roa times closeadj
def roa_f063_return_on_assets_rank_504d_base_v090_signal(roa, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roa.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of roa times closeadj
def roa_f063_return_on_assets_rank_1008d_base_v091_signal(roa, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roa.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roa from 63d mean times closeadj
def roa_f063_return_on_assets_devmean_63d_base_v092_signal(roa, closeadj):
    m = _mean(roa, 63)
    result = (roa - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roa from 252d mean times closeadj
def roa_f063_return_on_assets_devmean_252d_base_v093_signal(roa, closeadj):
    m = _mean(roa, 252)
    result = (roa - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roa from 504d mean times closeadj
def roa_f063_return_on_assets_devmean_504d_base_v094_signal(roa, closeadj):
    m = _mean(roa, 504)
    result = (roa - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of roa times closeadj
def roa_f063_return_on_assets_logdiff_21d_base_v095_signal(roa, closeadj):
    lr = _return_on_assets_log(roa)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of roa times closeadj
def roa_f063_return_on_assets_logdiff_63d_base_v096_signal(roa, closeadj):
    lr = _return_on_assets_log(roa)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of roa times closeadj
def roa_f063_return_on_assets_logdiff_252d_base_v097_signal(roa, closeadj):
    lr = _return_on_assets_log(roa)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of roa times closeadj
def roa_f063_return_on_assets_range_63d_base_v098_signal(roa, closeadj):
    hi = roa.rolling(63, min_periods=max(1, 63//2)).max()
    lo = roa.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of roa times closeadj
def roa_f063_return_on_assets_range_252d_base_v099_signal(roa, closeadj):
    hi = roa.rolling(252, min_periods=max(1, 252//2)).max()
    lo = roa.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of roa times closeadj
def roa_f063_return_on_assets_range_504d_base_v100_signal(roa, closeadj):
    hi = roa.rolling(504, min_periods=max(1, 504//2)).max()
    lo = roa.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 252d mean times closeadj
def roa_f063_return_on_assets_rel_252d_base_v101_signal(roa, closeadj):
    m = _mean(roa, 252).replace(0, np.nan)
    result = (roa / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 504d mean times closeadj
def roa_f063_return_on_assets_rel_504d_base_v102_signal(roa, closeadj):
    m = _mean(roa, 504).replace(0, np.nan)
    result = (roa / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 1008d mean times closeadj
def roa_f063_return_on_assets_rel_1008d_base_v103_signal(roa, closeadj):
    m = _mean(roa, 1008).replace(0, np.nan)
    result = (roa / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roa/netinc 63d mean
def roa_f063_return_on_assets_sqnorm_netinc_63d_base_v104_signal(roa, netinc):
    r = _return_on_assets_scaled(roa, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roa/netinc 252d mean
def roa_f063_return_on_assets_sqnorm_netinc_252d_base_v105_signal(roa, netinc):
    r = _return_on_assets_scaled(roa, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roa/assetsavg 63d mean
def roa_f063_return_on_assets_sqnorm_assetsavg_63d_base_v106_signal(roa, assetsavg):
    r = _return_on_assets_scaled(roa, assetsavg)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roa/assetsavg 252d mean
def roa_f063_return_on_assets_sqnorm_assetsavg_252d_base_v107_signal(roa, assetsavg):
    r = _return_on_assets_scaled(roa, assetsavg)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roa/assets 63d mean
def roa_f063_return_on_assets_sqnorm_assets_63d_base_v108_signal(roa, assets):
    r = _return_on_assets_scaled(roa, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roa/assets 252d mean
def roa_f063_return_on_assets_sqnorm_assets_252d_base_v109_signal(roa, assets):
    r = _return_on_assets_scaled(roa, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of roa times closeadj
def roa_f063_return_on_assets_infrat_63d_base_v110_signal(roa, closeadj):
    m = _mean(roa, 63)
    s = _std(roa, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of roa times closeadj
def roa_f063_return_on_assets_infrat_252d_base_v111_signal(roa, closeadj):
    m = _mean(roa, 252)
    s = _std(roa, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of roa times closeadj
def roa_f063_return_on_assets_infrat_504d_base_v112_signal(roa, closeadj):
    m = _mean(roa, 504)
    s = _std(roa, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of roa
def roa_f063_return_on_assets_cv_252d_base_v113_signal(roa):
    m = _mean(roa, 252).abs().replace(0, np.nan)
    s = _std(roa, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of roa
def roa_f063_return_on_assets_cv_504d_base_v114_signal(roa):
    m = _mean(roa, 504).abs().replace(0, np.nan)
    s = _std(roa, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged roa times closeadj
def roa_f063_return_on_assets_lag_5d_base_v115_signal(roa, closeadj):
    result = roa.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roa times closeadj
def roa_f063_return_on_assets_lag_21d_base_v116_signal(roa, closeadj):
    result = roa.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roa times closeadj
def roa_f063_return_on_assets_lag_63d_base_v117_signal(roa, closeadj):
    result = roa.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roa times closeadj
def roa_f063_return_on_assets_lag_252d_base_v118_signal(roa, closeadj):
    result = roa.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(roa) / mean(netinc) x closeadj
def roa_f063_return_on_assets_cumper_netinc_252d_base_v119_signal(roa, netinc, closeadj):
    s = roa.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(roa) / mean(netinc) x closeadj
def roa_f063_return_on_assets_cumper_netinc_504d_base_v120_signal(roa, netinc, closeadj):
    s = roa.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(roa) / mean(assetsavg) x closeadj
def roa_f063_return_on_assets_cumper_assetsavg_252d_base_v121_signal(roa, assetsavg, closeadj):
    s = roa.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assetsavg, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(roa) / mean(assetsavg) x closeadj
def roa_f063_return_on_assets_cumper_assetsavg_504d_base_v122_signal(roa, assetsavg, closeadj):
    s = roa.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assetsavg, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only roa times closeadj
def roa_f063_return_on_assets_pos_63d_base_v123_signal(roa, closeadj):
    pos = roa.where(roa > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only roa times closeadj
def roa_f063_return_on_assets_pos_252d_base_v124_signal(roa, closeadj):
    pos = roa.where(roa > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only roa times closeadj
def roa_f063_return_on_assets_neg_63d_base_v125_signal(roa, closeadj):
    neg = roa.where(roa < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only roa times closeadj
def roa_f063_return_on_assets_neg_252d_base_v126_signal(roa, closeadj):
    neg = roa.where(roa < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of roa times closeadj
def roa_f063_return_on_assets_hl_21d_base_v127_signal(roa, closeadj):
    result = roa.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of roa times closeadj
def roa_f063_return_on_assets_hl_63d_base_v128_signal(roa, closeadj):
    result = roa.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of roa times closeadj
def roa_f063_return_on_assets_hl_252d_base_v129_signal(roa, closeadj):
    result = roa.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of roa
def roa_f063_return_on_assets_z_63d_base_v130_signal(roa):
    result = _z(roa, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of roa
def roa_f063_return_on_assets_z_126d_base_v131_signal(roa):
    result = _z(roa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of roa
def roa_f063_return_on_assets_z_1008d_base_v132_signal(roa):
    result = _z(roa, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of roa times closeadj
def roa_f063_return_on_assets_st_lt_252_21d_base_v133_signal(roa, closeadj):
    sm = _mean(roa, 21)
    lm = _mean(roa, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of roa times closeadj
def roa_f063_return_on_assets_st_lt_252_63d_base_v134_signal(roa, closeadj):
    sm = _mean(roa, 63)
    lm = _mean(roa, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of roa times closeadj
def roa_f063_return_on_assets_st_lt_504_21d_base_v135_signal(roa, closeadj):
    sm = _mean(roa, 21)
    lm = _mean(roa, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of roa times closeadj
def roa_f063_return_on_assets_st_lt_504_63d_base_v136_signal(roa, closeadj):
    sm = _mean(roa, 63)
    lm = _mean(roa, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roa/netinc times closeadj
def roa_f063_return_on_assets_lag_per_netinc_21d_base_v137_signal(roa, netinc, closeadj):
    r = _return_on_assets_scaled(roa, netinc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roa/netinc times closeadj
def roa_f063_return_on_assets_lag_per_netinc_63d_base_v138_signal(roa, netinc, closeadj):
    r = _return_on_assets_scaled(roa, netinc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roa/netinc times closeadj
def roa_f063_return_on_assets_lag_per_netinc_252d_base_v139_signal(roa, netinc, closeadj):
    r = _return_on_assets_scaled(roa, netinc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roa/assetsavg times closeadj
def roa_f063_return_on_assets_lag_per_assetsavg_21d_base_v140_signal(roa, assetsavg, closeadj):
    r = _return_on_assets_scaled(roa, assetsavg)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roa/assetsavg times closeadj
def roa_f063_return_on_assets_lag_per_assetsavg_63d_base_v141_signal(roa, assetsavg, closeadj):
    r = _return_on_assets_scaled(roa, assetsavg)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roa/assetsavg times closeadj
def roa_f063_return_on_assets_lag_per_assetsavg_252d_base_v142_signal(roa, assetsavg, closeadj):
    r = _return_on_assets_scaled(roa, assetsavg)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |roa| times closeadj
def roa_f063_return_on_assets_abssum_63d_base_v143_signal(roa, closeadj):
    result = roa.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |roa| times closeadj
def roa_f063_return_on_assets_abssum_252d_base_v144_signal(roa, closeadj):
    result = roa.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |roa| times closeadj
def roa_f063_return_on_assets_abssum_504d_base_v145_signal(roa, closeadj):
    result = roa.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of roa
def roa_f063_return_on_assets_acf1_252d_base_v146_signal(roa):
    result = roa.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of roa
def roa_f063_return_on_assets_acf1_504d_base_v147_signal(roa):
    result = roa.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of roa
def roa_f063_return_on_assets_posinrange_252d_base_v148_signal(roa):
    m = _mean(roa, 252)
    hi = roa.rolling(252, min_periods=max(1, 252//2)).max()
    lo = roa.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of roa
def roa_f063_return_on_assets_posinrange_504d_base_v149_signal(roa):
    m = _mean(roa, 504)
    hi = roa.rolling(504, min_periods=max(1, 504//2)).max()
    lo = roa.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of roa times closeadj
def roa_f063_return_on_assets_hl_5d_base_v150_signal(roa, closeadj):
    result = roa.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
