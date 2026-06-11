"""Family f064 - Return on equity (Returns and Efficiency) | Sharadar tables: SF1 | fields: roe, netinc, equity | base 076-150"""
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
def _return_on_equity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_equity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_equity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of roe/equity
def roe_f064_return_on_equity_log_per_equity_504d_base_v076_signal(roe, equity):
    s = _return_on_equity_scaled(roe, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roe/assets
def roe_f064_return_on_equity_log_per_assets_252d_base_v077_signal(roe, assets):
    s = _return_on_equity_scaled(roe, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of roe/assets
def roe_f064_return_on_equity_log_per_assets_504d_base_v078_signal(roe, assets):
    s = _return_on_equity_scaled(roe, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of roe times closeadj
def roe_f064_return_on_equity_ewm_21d_base_v079_signal(roe, closeadj):
    result = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of roe times closeadj
def roe_f064_return_on_equity_ewm_63d_base_v080_signal(roe, closeadj):
    result = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of roe times closeadj
def roe_f064_return_on_equity_ewm_252d_base_v081_signal(roe, closeadj):
    result = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of roe times closeadj
def roe_f064_return_on_equity_med_63d_base_v082_signal(roe, closeadj):
    result = roe.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of roe times closeadj
def roe_f064_return_on_equity_med_252d_base_v083_signal(roe, closeadj):
    result = roe.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of roe times closeadj
def roe_f064_return_on_equity_med_504d_base_v084_signal(roe, closeadj):
    result = roe.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of roe
def roe_f064_return_on_equity_skew_252d_base_v085_signal(roe):
    result = roe.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of roe
def roe_f064_return_on_equity_skew_504d_base_v086_signal(roe):
    result = roe.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of roe
def roe_f064_return_on_equity_kurt_252d_base_v087_signal(roe):
    result = roe.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of roe
def roe_f064_return_on_equity_kurt_504d_base_v088_signal(roe):
    result = roe.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of roe times closeadj
def roe_f064_return_on_equity_rank_252d_base_v089_signal(roe, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roe.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of roe times closeadj
def roe_f064_return_on_equity_rank_504d_base_v090_signal(roe, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roe.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of roe times closeadj
def roe_f064_return_on_equity_rank_1008d_base_v091_signal(roe, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roe.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roe from 63d mean times closeadj
def roe_f064_return_on_equity_devmean_63d_base_v092_signal(roe, closeadj):
    m = _mean(roe, 63)
    result = (roe - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roe from 252d mean times closeadj
def roe_f064_return_on_equity_devmean_252d_base_v093_signal(roe, closeadj):
    m = _mean(roe, 252)
    result = (roe - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roe from 504d mean times closeadj
def roe_f064_return_on_equity_devmean_504d_base_v094_signal(roe, closeadj):
    m = _mean(roe, 504)
    result = (roe - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of roe times closeadj
def roe_f064_return_on_equity_logdiff_21d_base_v095_signal(roe, closeadj):
    lr = _return_on_equity_log(roe)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of roe times closeadj
def roe_f064_return_on_equity_logdiff_63d_base_v096_signal(roe, closeadj):
    lr = _return_on_equity_log(roe)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of roe times closeadj
def roe_f064_return_on_equity_logdiff_252d_base_v097_signal(roe, closeadj):
    lr = _return_on_equity_log(roe)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of roe times closeadj
def roe_f064_return_on_equity_range_63d_base_v098_signal(roe, closeadj):
    hi = roe.rolling(63, min_periods=max(1, 63//2)).max()
    lo = roe.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of roe times closeadj
def roe_f064_return_on_equity_range_252d_base_v099_signal(roe, closeadj):
    hi = roe.rolling(252, min_periods=max(1, 252//2)).max()
    lo = roe.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of roe times closeadj
def roe_f064_return_on_equity_range_504d_base_v100_signal(roe, closeadj):
    hi = roe.rolling(504, min_periods=max(1, 504//2)).max()
    lo = roe.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 252d mean times closeadj
def roe_f064_return_on_equity_rel_252d_base_v101_signal(roe, closeadj):
    m = _mean(roe, 252).replace(0, np.nan)
    result = (roe / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 504d mean times closeadj
def roe_f064_return_on_equity_rel_504d_base_v102_signal(roe, closeadj):
    m = _mean(roe, 504).replace(0, np.nan)
    result = (roe / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roe relative to 1008d mean times closeadj
def roe_f064_return_on_equity_rel_1008d_base_v103_signal(roe, closeadj):
    m = _mean(roe, 1008).replace(0, np.nan)
    result = (roe / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roe/netinc 63d mean
def roe_f064_return_on_equity_sqnorm_netinc_63d_base_v104_signal(roe, netinc):
    r = _return_on_equity_scaled(roe, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roe/netinc 252d mean
def roe_f064_return_on_equity_sqnorm_netinc_252d_base_v105_signal(roe, netinc):
    r = _return_on_equity_scaled(roe, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roe/equity 63d mean
def roe_f064_return_on_equity_sqnorm_equity_63d_base_v106_signal(roe, equity):
    r = _return_on_equity_scaled(roe, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roe/equity 252d mean
def roe_f064_return_on_equity_sqnorm_equity_252d_base_v107_signal(roe, equity):
    r = _return_on_equity_scaled(roe, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roe/assets 63d mean
def roe_f064_return_on_equity_sqnorm_assets_63d_base_v108_signal(roe, assets):
    r = _return_on_equity_scaled(roe, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roe/assets 252d mean
def roe_f064_return_on_equity_sqnorm_assets_252d_base_v109_signal(roe, assets):
    r = _return_on_equity_scaled(roe, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of roe times closeadj
def roe_f064_return_on_equity_infrat_63d_base_v110_signal(roe, closeadj):
    m = _mean(roe, 63)
    s = _std(roe, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of roe times closeadj
def roe_f064_return_on_equity_infrat_252d_base_v111_signal(roe, closeadj):
    m = _mean(roe, 252)
    s = _std(roe, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of roe times closeadj
def roe_f064_return_on_equity_infrat_504d_base_v112_signal(roe, closeadj):
    m = _mean(roe, 504)
    s = _std(roe, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of roe
def roe_f064_return_on_equity_cv_252d_base_v113_signal(roe):
    m = _mean(roe, 252).abs().replace(0, np.nan)
    s = _std(roe, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of roe
def roe_f064_return_on_equity_cv_504d_base_v114_signal(roe):
    m = _mean(roe, 504).abs().replace(0, np.nan)
    s = _std(roe, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged roe times closeadj
def roe_f064_return_on_equity_lag_5d_base_v115_signal(roe, closeadj):
    result = roe.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roe times closeadj
def roe_f064_return_on_equity_lag_21d_base_v116_signal(roe, closeadj):
    result = roe.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roe times closeadj
def roe_f064_return_on_equity_lag_63d_base_v117_signal(roe, closeadj):
    result = roe.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roe times closeadj
def roe_f064_return_on_equity_lag_252d_base_v118_signal(roe, closeadj):
    result = roe.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(roe) / mean(netinc) x closeadj
def roe_f064_return_on_equity_cumper_netinc_252d_base_v119_signal(roe, netinc, closeadj):
    s = roe.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(roe) / mean(netinc) x closeadj
def roe_f064_return_on_equity_cumper_netinc_504d_base_v120_signal(roe, netinc, closeadj):
    s = roe.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(roe) / mean(equity) x closeadj
def roe_f064_return_on_equity_cumper_equity_252d_base_v121_signal(roe, equity, closeadj):
    s = roe.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(equity, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(roe) / mean(equity) x closeadj
def roe_f064_return_on_equity_cumper_equity_504d_base_v122_signal(roe, equity, closeadj):
    s = roe.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(equity, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only roe times closeadj
def roe_f064_return_on_equity_pos_63d_base_v123_signal(roe, closeadj):
    pos = roe.where(roe > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only roe times closeadj
def roe_f064_return_on_equity_pos_252d_base_v124_signal(roe, closeadj):
    pos = roe.where(roe > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only roe times closeadj
def roe_f064_return_on_equity_neg_63d_base_v125_signal(roe, closeadj):
    neg = roe.where(roe < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only roe times closeadj
def roe_f064_return_on_equity_neg_252d_base_v126_signal(roe, closeadj):
    neg = roe.where(roe < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of roe times closeadj
def roe_f064_return_on_equity_hl_21d_base_v127_signal(roe, closeadj):
    result = roe.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of roe times closeadj
def roe_f064_return_on_equity_hl_63d_base_v128_signal(roe, closeadj):
    result = roe.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of roe times closeadj
def roe_f064_return_on_equity_hl_252d_base_v129_signal(roe, closeadj):
    result = roe.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of roe
def roe_f064_return_on_equity_z_63d_base_v130_signal(roe):
    result = _z(roe, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of roe
def roe_f064_return_on_equity_z_126d_base_v131_signal(roe):
    result = _z(roe, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of roe
def roe_f064_return_on_equity_z_1008d_base_v132_signal(roe):
    result = _z(roe, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of roe times closeadj
def roe_f064_return_on_equity_st_lt_252_21d_base_v133_signal(roe, closeadj):
    sm = _mean(roe, 21)
    lm = _mean(roe, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of roe times closeadj
def roe_f064_return_on_equity_st_lt_252_63d_base_v134_signal(roe, closeadj):
    sm = _mean(roe, 63)
    lm = _mean(roe, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of roe times closeadj
def roe_f064_return_on_equity_st_lt_504_21d_base_v135_signal(roe, closeadj):
    sm = _mean(roe, 21)
    lm = _mean(roe, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of roe times closeadj
def roe_f064_return_on_equity_st_lt_504_63d_base_v136_signal(roe, closeadj):
    sm = _mean(roe, 63)
    lm = _mean(roe, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roe/netinc times closeadj
def roe_f064_return_on_equity_lag_per_netinc_21d_base_v137_signal(roe, netinc, closeadj):
    r = _return_on_equity_scaled(roe, netinc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roe/netinc times closeadj
def roe_f064_return_on_equity_lag_per_netinc_63d_base_v138_signal(roe, netinc, closeadj):
    r = _return_on_equity_scaled(roe, netinc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roe/netinc times closeadj
def roe_f064_return_on_equity_lag_per_netinc_252d_base_v139_signal(roe, netinc, closeadj):
    r = _return_on_equity_scaled(roe, netinc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roe/equity times closeadj
def roe_f064_return_on_equity_lag_per_equity_21d_base_v140_signal(roe, equity, closeadj):
    r = _return_on_equity_scaled(roe, equity)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roe/equity times closeadj
def roe_f064_return_on_equity_lag_per_equity_63d_base_v141_signal(roe, equity, closeadj):
    r = _return_on_equity_scaled(roe, equity)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roe/equity times closeadj
def roe_f064_return_on_equity_lag_per_equity_252d_base_v142_signal(roe, equity, closeadj):
    r = _return_on_equity_scaled(roe, equity)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |roe| times closeadj
def roe_f064_return_on_equity_abssum_63d_base_v143_signal(roe, closeadj):
    result = roe.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |roe| times closeadj
def roe_f064_return_on_equity_abssum_252d_base_v144_signal(roe, closeadj):
    result = roe.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |roe| times closeadj
def roe_f064_return_on_equity_abssum_504d_base_v145_signal(roe, closeadj):
    result = roe.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of roe
def roe_f064_return_on_equity_acf1_252d_base_v146_signal(roe):
    result = roe.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of roe
def roe_f064_return_on_equity_acf1_504d_base_v147_signal(roe):
    result = roe.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of roe
def roe_f064_return_on_equity_posinrange_252d_base_v148_signal(roe):
    m = _mean(roe, 252)
    hi = roe.rolling(252, min_periods=max(1, 252//2)).max()
    lo = roe.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of roe
def roe_f064_return_on_equity_posinrange_504d_base_v149_signal(roe):
    m = _mean(roe, 504)
    hi = roe.rolling(504, min_periods=max(1, 504//2)).max()
    lo = roe.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of roe times closeadj
def roe_f064_return_on_equity_hl_5d_base_v150_signal(roe, closeadj):
    result = roe.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
