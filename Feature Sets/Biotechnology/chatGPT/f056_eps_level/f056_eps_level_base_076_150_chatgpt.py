"""Family f056 - EPS level and sign (Earnings and Quality) | Sharadar tables: SF1 | fields: eps, epsdil, netinc | base 076-150"""
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
def _eps_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _eps_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _eps_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of eps/netinc
def el_f056_eps_level_log_per_netinc_504d_base_v076_signal(eps, netinc):
    s = _eps_level_scaled(eps, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of eps/assets
def el_f056_eps_level_log_per_assets_252d_base_v077_signal(eps, assets):
    s = _eps_level_scaled(eps, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of eps/assets
def el_f056_eps_level_log_per_assets_504d_base_v078_signal(eps, assets):
    s = _eps_level_scaled(eps, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of eps times closeadj
def el_f056_eps_level_ewm_21d_base_v079_signal(eps, closeadj):
    result = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of eps times closeadj
def el_f056_eps_level_ewm_63d_base_v080_signal(eps, closeadj):
    result = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of eps times closeadj
def el_f056_eps_level_ewm_252d_base_v081_signal(eps, closeadj):
    result = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of eps times closeadj
def el_f056_eps_level_med_63d_base_v082_signal(eps, closeadj):
    result = eps.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of eps times closeadj
def el_f056_eps_level_med_252d_base_v083_signal(eps, closeadj):
    result = eps.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of eps times closeadj
def el_f056_eps_level_med_504d_base_v084_signal(eps, closeadj):
    result = eps.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of eps
def el_f056_eps_level_skew_252d_base_v085_signal(eps):
    result = eps.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of eps
def el_f056_eps_level_skew_504d_base_v086_signal(eps):
    result = eps.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of eps
def el_f056_eps_level_kurt_252d_base_v087_signal(eps):
    result = eps.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of eps
def el_f056_eps_level_kurt_504d_base_v088_signal(eps):
    result = eps.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of eps times closeadj
def el_f056_eps_level_rank_252d_base_v089_signal(eps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = eps.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of eps times closeadj
def el_f056_eps_level_rank_504d_base_v090_signal(eps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = eps.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of eps times closeadj
def el_f056_eps_level_rank_1008d_base_v091_signal(eps, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = eps.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of eps from 63d mean times closeadj
def el_f056_eps_level_devmean_63d_base_v092_signal(eps, closeadj):
    m = _mean(eps, 63)
    result = (eps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of eps from 252d mean times closeadj
def el_f056_eps_level_devmean_252d_base_v093_signal(eps, closeadj):
    m = _mean(eps, 252)
    result = (eps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of eps from 504d mean times closeadj
def el_f056_eps_level_devmean_504d_base_v094_signal(eps, closeadj):
    m = _mean(eps, 504)
    result = (eps - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of eps times closeadj
def el_f056_eps_level_logdiff_21d_base_v095_signal(eps, closeadj):
    lr = _eps_level_log(eps)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of eps times closeadj
def el_f056_eps_level_logdiff_63d_base_v096_signal(eps, closeadj):
    lr = _eps_level_log(eps)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of eps times closeadj
def el_f056_eps_level_logdiff_252d_base_v097_signal(eps, closeadj):
    lr = _eps_level_log(eps)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of eps times closeadj
def el_f056_eps_level_range_63d_base_v098_signal(eps, closeadj):
    hi = eps.rolling(63, min_periods=max(1, 63//2)).max()
    lo = eps.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of eps times closeadj
def el_f056_eps_level_range_252d_base_v099_signal(eps, closeadj):
    hi = eps.rolling(252, min_periods=max(1, 252//2)).max()
    lo = eps.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of eps times closeadj
def el_f056_eps_level_range_504d_base_v100_signal(eps, closeadj):
    hi = eps.rolling(504, min_periods=max(1, 504//2)).max()
    lo = eps.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 252d mean times closeadj
def el_f056_eps_level_rel_252d_base_v101_signal(eps, closeadj):
    m = _mean(eps, 252).replace(0, np.nan)
    result = (eps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 504d mean times closeadj
def el_f056_eps_level_rel_504d_base_v102_signal(eps, closeadj):
    m = _mean(eps, 504).replace(0, np.nan)
    result = (eps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eps relative to 1008d mean times closeadj
def el_f056_eps_level_rel_1008d_base_v103_signal(eps, closeadj):
    m = _mean(eps, 1008).replace(0, np.nan)
    result = (eps / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eps/epsdil 63d mean
def el_f056_eps_level_sqnorm_epsdil_63d_base_v104_signal(eps, epsdil):
    r = _eps_level_scaled(eps, epsdil)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eps/epsdil 252d mean
def el_f056_eps_level_sqnorm_epsdil_252d_base_v105_signal(eps, epsdil):
    r = _eps_level_scaled(eps, epsdil)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eps/netinc 63d mean
def el_f056_eps_level_sqnorm_netinc_63d_base_v106_signal(eps, netinc):
    r = _eps_level_scaled(eps, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eps/netinc 252d mean
def el_f056_eps_level_sqnorm_netinc_252d_base_v107_signal(eps, netinc):
    r = _eps_level_scaled(eps, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eps/assets 63d mean
def el_f056_eps_level_sqnorm_assets_63d_base_v108_signal(eps, assets):
    r = _eps_level_scaled(eps, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eps/assets 252d mean
def el_f056_eps_level_sqnorm_assets_252d_base_v109_signal(eps, assets):
    r = _eps_level_scaled(eps, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of eps times closeadj
def el_f056_eps_level_infrat_63d_base_v110_signal(eps, closeadj):
    m = _mean(eps, 63)
    s = _std(eps, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of eps times closeadj
def el_f056_eps_level_infrat_252d_base_v111_signal(eps, closeadj):
    m = _mean(eps, 252)
    s = _std(eps, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of eps times closeadj
def el_f056_eps_level_infrat_504d_base_v112_signal(eps, closeadj):
    m = _mean(eps, 504)
    s = _std(eps, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of eps
def el_f056_eps_level_cv_252d_base_v113_signal(eps):
    m = _mean(eps, 252).abs().replace(0, np.nan)
    s = _std(eps, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of eps
def el_f056_eps_level_cv_504d_base_v114_signal(eps):
    m = _mean(eps, 504).abs().replace(0, np.nan)
    s = _std(eps, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged eps times closeadj
def el_f056_eps_level_lag_5d_base_v115_signal(eps, closeadj):
    result = eps.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged eps times closeadj
def el_f056_eps_level_lag_21d_base_v116_signal(eps, closeadj):
    result = eps.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged eps times closeadj
def el_f056_eps_level_lag_63d_base_v117_signal(eps, closeadj):
    result = eps.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged eps times closeadj
def el_f056_eps_level_lag_252d_base_v118_signal(eps, closeadj):
    result = eps.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(eps) / mean(epsdil) x closeadj
def el_f056_eps_level_cumper_epsdil_252d_base_v119_signal(eps, epsdil, closeadj):
    s = eps.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(epsdil, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(eps) / mean(epsdil) x closeadj
def el_f056_eps_level_cumper_epsdil_504d_base_v120_signal(eps, epsdil, closeadj):
    s = eps.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(epsdil, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(eps) / mean(netinc) x closeadj
def el_f056_eps_level_cumper_netinc_252d_base_v121_signal(eps, netinc, closeadj):
    s = eps.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(eps) / mean(netinc) x closeadj
def el_f056_eps_level_cumper_netinc_504d_base_v122_signal(eps, netinc, closeadj):
    s = eps.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only eps times closeadj
def el_f056_eps_level_pos_63d_base_v123_signal(eps, closeadj):
    pos = eps.where(eps > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only eps times closeadj
def el_f056_eps_level_pos_252d_base_v124_signal(eps, closeadj):
    pos = eps.where(eps > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only eps times closeadj
def el_f056_eps_level_neg_63d_base_v125_signal(eps, closeadj):
    neg = eps.where(eps < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only eps times closeadj
def el_f056_eps_level_neg_252d_base_v126_signal(eps, closeadj):
    neg = eps.where(eps < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of eps times closeadj
def el_f056_eps_level_hl_21d_base_v127_signal(eps, closeadj):
    result = eps.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of eps times closeadj
def el_f056_eps_level_hl_63d_base_v128_signal(eps, closeadj):
    result = eps.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of eps times closeadj
def el_f056_eps_level_hl_252d_base_v129_signal(eps, closeadj):
    result = eps.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of eps
def el_f056_eps_level_z_63d_base_v130_signal(eps):
    result = _z(eps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of eps
def el_f056_eps_level_z_126d_base_v131_signal(eps):
    result = _z(eps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of eps
def el_f056_eps_level_z_1008d_base_v132_signal(eps):
    result = _z(eps, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of eps times closeadj
def el_f056_eps_level_st_lt_252_21d_base_v133_signal(eps, closeadj):
    sm = _mean(eps, 21)
    lm = _mean(eps, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of eps times closeadj
def el_f056_eps_level_st_lt_252_63d_base_v134_signal(eps, closeadj):
    sm = _mean(eps, 63)
    lm = _mean(eps, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of eps times closeadj
def el_f056_eps_level_st_lt_504_21d_base_v135_signal(eps, closeadj):
    sm = _mean(eps, 21)
    lm = _mean(eps, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of eps times closeadj
def el_f056_eps_level_st_lt_504_63d_base_v136_signal(eps, closeadj):
    sm = _mean(eps, 63)
    lm = _mean(eps, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged eps/epsdil times closeadj
def el_f056_eps_level_lag_per_epsdil_21d_base_v137_signal(eps, epsdil, closeadj):
    r = _eps_level_scaled(eps, epsdil)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged eps/epsdil times closeadj
def el_f056_eps_level_lag_per_epsdil_63d_base_v138_signal(eps, epsdil, closeadj):
    r = _eps_level_scaled(eps, epsdil)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged eps/epsdil times closeadj
def el_f056_eps_level_lag_per_epsdil_252d_base_v139_signal(eps, epsdil, closeadj):
    r = _eps_level_scaled(eps, epsdil)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged eps/netinc times closeadj
def el_f056_eps_level_lag_per_netinc_21d_base_v140_signal(eps, netinc, closeadj):
    r = _eps_level_scaled(eps, netinc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged eps/netinc times closeadj
def el_f056_eps_level_lag_per_netinc_63d_base_v141_signal(eps, netinc, closeadj):
    r = _eps_level_scaled(eps, netinc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged eps/netinc times closeadj
def el_f056_eps_level_lag_per_netinc_252d_base_v142_signal(eps, netinc, closeadj):
    r = _eps_level_scaled(eps, netinc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |eps| times closeadj
def el_f056_eps_level_abssum_63d_base_v143_signal(eps, closeadj):
    result = eps.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |eps| times closeadj
def el_f056_eps_level_abssum_252d_base_v144_signal(eps, closeadj):
    result = eps.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |eps| times closeadj
def el_f056_eps_level_abssum_504d_base_v145_signal(eps, closeadj):
    result = eps.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of eps
def el_f056_eps_level_acf1_252d_base_v146_signal(eps):
    result = eps.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of eps
def el_f056_eps_level_acf1_504d_base_v147_signal(eps):
    result = eps.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of eps
def el_f056_eps_level_posinrange_252d_base_v148_signal(eps):
    m = _mean(eps, 252)
    hi = eps.rolling(252, min_periods=max(1, 252//2)).max()
    lo = eps.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of eps
def el_f056_eps_level_posinrange_504d_base_v149_signal(eps):
    m = _mean(eps, 504)
    hi = eps.rolling(504, min_periods=max(1, 504//2)).max()
    lo = eps.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of eps times closeadj
def el_f056_eps_level_hl_5d_base_v150_signal(eps, closeadj):
    result = eps.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
