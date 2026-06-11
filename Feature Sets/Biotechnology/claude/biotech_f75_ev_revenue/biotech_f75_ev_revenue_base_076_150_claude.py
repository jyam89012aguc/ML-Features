"""Family f75 - EV / revenue  (M_Valuation) | base 076-150"""
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
def _ev_revenue_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ev_revenue_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ev_revenue_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ev/marketcap
def evr_f75_ev_revenue_log_per_marketcap_504d_base_v076_signal(ev, marketcap):
    s = _ev_revenue_scaled(ev, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ev/equity
def evr_f75_ev_revenue_log_per_equity_252d_base_v077_signal(ev, equity):
    s = _ev_revenue_scaled(ev, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ev/equity
def evr_f75_ev_revenue_log_per_equity_504d_base_v078_signal(ev, equity):
    s = _ev_revenue_scaled(ev, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ev times closeadj
def evr_f75_ev_revenue_ewm_21d_base_v079_signal(ev, closeadj):
    result = ev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ev times closeadj
def evr_f75_ev_revenue_ewm_63d_base_v080_signal(ev, closeadj):
    result = ev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ev times closeadj
def evr_f75_ev_revenue_ewm_252d_base_v081_signal(ev, closeadj):
    result = ev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ev times closeadj
def evr_f75_ev_revenue_med_63d_base_v082_signal(ev, closeadj):
    result = ev.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ev times closeadj
def evr_f75_ev_revenue_med_252d_base_v083_signal(ev, closeadj):
    result = ev.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ev times closeadj
def evr_f75_ev_revenue_med_504d_base_v084_signal(ev, closeadj):
    result = ev.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ev
def evr_f75_ev_revenue_skew_252d_base_v085_signal(ev):
    result = ev.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ev
def evr_f75_ev_revenue_skew_504d_base_v086_signal(ev):
    result = ev.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ev
def evr_f75_ev_revenue_kurt_252d_base_v087_signal(ev):
    result = ev.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ev
def evr_f75_ev_revenue_kurt_504d_base_v088_signal(ev):
    result = ev.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ev times closeadj
def evr_f75_ev_revenue_rank_252d_base_v089_signal(ev, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ev.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ev times closeadj
def evr_f75_ev_revenue_rank_504d_base_v090_signal(ev, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ev.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ev times closeadj
def evr_f75_ev_revenue_rank_1008d_base_v091_signal(ev, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ev.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ev from 63d mean times closeadj
def evr_f75_ev_revenue_devmean_63d_base_v092_signal(ev, closeadj):
    m = _mean(ev, 63)
    result = (ev - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ev from 252d mean times closeadj
def evr_f75_ev_revenue_devmean_252d_base_v093_signal(ev, closeadj):
    m = _mean(ev, 252)
    result = (ev - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ev from 504d mean times closeadj
def evr_f75_ev_revenue_devmean_504d_base_v094_signal(ev, closeadj):
    m = _mean(ev, 504)
    result = (ev - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ev times closeadj
def evr_f75_ev_revenue_logdiff_21d_base_v095_signal(ev, closeadj):
    lr = _ev_revenue_log(ev)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ev times closeadj
def evr_f75_ev_revenue_logdiff_63d_base_v096_signal(ev, closeadj):
    lr = _ev_revenue_log(ev)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ev times closeadj
def evr_f75_ev_revenue_logdiff_252d_base_v097_signal(ev, closeadj):
    lr = _ev_revenue_log(ev)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ev times closeadj
def evr_f75_ev_revenue_range_63d_base_v098_signal(ev, closeadj):
    hi = ev.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ev.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ev times closeadj
def evr_f75_ev_revenue_range_252d_base_v099_signal(ev, closeadj):
    hi = ev.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ev.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ev times closeadj
def evr_f75_ev_revenue_range_504d_base_v100_signal(ev, closeadj):
    hi = ev.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ev.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 252d mean times closeadj
def evr_f75_ev_revenue_rel_252d_base_v101_signal(ev, closeadj):
    m = _mean(ev, 252).replace(0, np.nan)
    result = (ev / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 504d mean times closeadj
def evr_f75_ev_revenue_rel_504d_base_v102_signal(ev, closeadj):
    m = _mean(ev, 504).replace(0, np.nan)
    result = (ev / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ev relative to 1008d mean times closeadj
def evr_f75_ev_revenue_rel_1008d_base_v103_signal(ev, closeadj):
    m = _mean(ev, 1008).replace(0, np.nan)
    result = (ev / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ev/assets 63d mean
def evr_f75_ev_revenue_sqnorm_assets_63d_base_v104_signal(ev, assets):
    r = _ev_revenue_scaled(ev, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ev/assets 252d mean
def evr_f75_ev_revenue_sqnorm_assets_252d_base_v105_signal(ev, assets):
    r = _ev_revenue_scaled(ev, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ev/marketcap 63d mean
def evr_f75_ev_revenue_sqnorm_marketcap_63d_base_v106_signal(ev, marketcap):
    r = _ev_revenue_scaled(ev, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ev/marketcap 252d mean
def evr_f75_ev_revenue_sqnorm_marketcap_252d_base_v107_signal(ev, marketcap):
    r = _ev_revenue_scaled(ev, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ev/equity 63d mean
def evr_f75_ev_revenue_sqnorm_equity_63d_base_v108_signal(ev, equity):
    r = _ev_revenue_scaled(ev, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ev/equity 252d mean
def evr_f75_ev_revenue_sqnorm_equity_252d_base_v109_signal(ev, equity):
    r = _ev_revenue_scaled(ev, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ev times closeadj
def evr_f75_ev_revenue_infrat_63d_base_v110_signal(ev, closeadj):
    m = _mean(ev, 63)
    s = _std(ev, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ev times closeadj
def evr_f75_ev_revenue_infrat_252d_base_v111_signal(ev, closeadj):
    m = _mean(ev, 252)
    s = _std(ev, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ev times closeadj
def evr_f75_ev_revenue_infrat_504d_base_v112_signal(ev, closeadj):
    m = _mean(ev, 504)
    s = _std(ev, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ev
def evr_f75_ev_revenue_cv_252d_base_v113_signal(ev):
    m = _mean(ev, 252).abs().replace(0, np.nan)
    s = _std(ev, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ev
def evr_f75_ev_revenue_cv_504d_base_v114_signal(ev):
    m = _mean(ev, 504).abs().replace(0, np.nan)
    s = _std(ev, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ev times closeadj
def evr_f75_ev_revenue_lag_5d_base_v115_signal(ev, closeadj):
    result = ev.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ev times closeadj
def evr_f75_ev_revenue_lag_21d_base_v116_signal(ev, closeadj):
    result = ev.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ev times closeadj
def evr_f75_ev_revenue_lag_63d_base_v117_signal(ev, closeadj):
    result = ev.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ev times closeadj
def evr_f75_ev_revenue_lag_252d_base_v118_signal(ev, closeadj):
    result = ev.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ev) / mean(assets) x closeadj
def evr_f75_ev_revenue_cumper_assets_252d_base_v119_signal(ev, assets, closeadj):
    s = ev.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ev) / mean(assets) x closeadj
def evr_f75_ev_revenue_cumper_assets_504d_base_v120_signal(ev, assets, closeadj):
    s = ev.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ev) / mean(marketcap) x closeadj
def evr_f75_ev_revenue_cumper_marketcap_252d_base_v121_signal(ev, marketcap, closeadj):
    s = ev.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ev) / mean(marketcap) x closeadj
def evr_f75_ev_revenue_cumper_marketcap_504d_base_v122_signal(ev, marketcap, closeadj):
    s = ev.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ev times closeadj
def evr_f75_ev_revenue_pos_63d_base_v123_signal(ev, closeadj):
    pos = ev.where(ev > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ev times closeadj
def evr_f75_ev_revenue_pos_252d_base_v124_signal(ev, closeadj):
    pos = ev.where(ev > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ev times closeadj
def evr_f75_ev_revenue_neg_63d_base_v125_signal(ev, closeadj):
    neg = ev.where(ev < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ev times closeadj
def evr_f75_ev_revenue_neg_252d_base_v126_signal(ev, closeadj):
    neg = ev.where(ev < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ev times closeadj
def evr_f75_ev_revenue_hl_21d_base_v127_signal(ev, closeadj):
    result = ev.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ev times closeadj
def evr_f75_ev_revenue_hl_63d_base_v128_signal(ev, closeadj):
    result = ev.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ev times closeadj
def evr_f75_ev_revenue_hl_252d_base_v129_signal(ev, closeadj):
    result = ev.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ev
def evr_f75_ev_revenue_z_63d_base_v130_signal(ev):
    result = _z(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ev
def evr_f75_ev_revenue_z_126d_base_v131_signal(ev):
    result = _z(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ev
def evr_f75_ev_revenue_z_1008d_base_v132_signal(ev):
    result = _z(ev, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ev times closeadj
def evr_f75_ev_revenue_st_lt_252_21d_base_v133_signal(ev, closeadj):
    sm = _mean(ev, 21)
    lm = _mean(ev, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ev times closeadj
def evr_f75_ev_revenue_st_lt_252_63d_base_v134_signal(ev, closeadj):
    sm = _mean(ev, 63)
    lm = _mean(ev, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ev times closeadj
def evr_f75_ev_revenue_st_lt_504_21d_base_v135_signal(ev, closeadj):
    sm = _mean(ev, 21)
    lm = _mean(ev, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ev times closeadj
def evr_f75_ev_revenue_st_lt_504_63d_base_v136_signal(ev, closeadj):
    sm = _mean(ev, 63)
    lm = _mean(ev, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ev/assets times closeadj
def evr_f75_ev_revenue_lag_per_assets_21d_base_v137_signal(ev, assets, closeadj):
    r = _ev_revenue_scaled(ev, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ev/assets times closeadj
def evr_f75_ev_revenue_lag_per_assets_63d_base_v138_signal(ev, assets, closeadj):
    r = _ev_revenue_scaled(ev, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ev/assets times closeadj
def evr_f75_ev_revenue_lag_per_assets_252d_base_v139_signal(ev, assets, closeadj):
    r = _ev_revenue_scaled(ev, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ev/marketcap times closeadj
def evr_f75_ev_revenue_lag_per_marketcap_21d_base_v140_signal(ev, marketcap, closeadj):
    r = _ev_revenue_scaled(ev, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ev/marketcap times closeadj
def evr_f75_ev_revenue_lag_per_marketcap_63d_base_v141_signal(ev, marketcap, closeadj):
    r = _ev_revenue_scaled(ev, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ev/marketcap times closeadj
def evr_f75_ev_revenue_lag_per_marketcap_252d_base_v142_signal(ev, marketcap, closeadj):
    r = _ev_revenue_scaled(ev, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ev| times closeadj
def evr_f75_ev_revenue_abssum_63d_base_v143_signal(ev, closeadj):
    result = ev.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ev| times closeadj
def evr_f75_ev_revenue_abssum_252d_base_v144_signal(ev, closeadj):
    result = ev.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ev| times closeadj
def evr_f75_ev_revenue_abssum_504d_base_v145_signal(ev, closeadj):
    result = ev.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ev
def evr_f75_ev_revenue_acf1_252d_base_v146_signal(ev):
    result = ev.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ev
def evr_f75_ev_revenue_acf1_504d_base_v147_signal(ev):
    result = ev.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ev
def evr_f75_ev_revenue_posinrange_252d_base_v148_signal(ev):
    m = _mean(ev, 252)
    hi = ev.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ev.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ev
def evr_f75_ev_revenue_posinrange_504d_base_v149_signal(ev):
    m = _mean(ev, 504)
    hi = ev.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ev.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ev times closeadj
def evr_f75_ev_revenue_hl_5d_base_v150_signal(ev, closeadj):
    result = ev.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
