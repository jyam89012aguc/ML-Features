"""Family f62 - Invested capital  (J_Returns_Efficiency) | base 076-150"""
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
def _invested_capital_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _invested_capital_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _invested_capital_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of invcap/marketcap
def ivc_f62_invested_capital_log_per_marketcap_504d_base_v076_signal(invcap, marketcap):
    s = _invested_capital_scaled(invcap, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of invcap/equity
def ivc_f62_invested_capital_log_per_equity_252d_base_v077_signal(invcap, equity):
    s = _invested_capital_scaled(invcap, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of invcap/equity
def ivc_f62_invested_capital_log_per_equity_504d_base_v078_signal(invcap, equity):
    s = _invested_capital_scaled(invcap, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of invcap times closeadj
def ivc_f62_invested_capital_ewm_21d_base_v079_signal(invcap, closeadj):
    result = invcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of invcap times closeadj
def ivc_f62_invested_capital_ewm_63d_base_v080_signal(invcap, closeadj):
    result = invcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of invcap times closeadj
def ivc_f62_invested_capital_ewm_252d_base_v081_signal(invcap, closeadj):
    result = invcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of invcap times closeadj
def ivc_f62_invested_capital_med_63d_base_v082_signal(invcap, closeadj):
    result = invcap.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of invcap times closeadj
def ivc_f62_invested_capital_med_252d_base_v083_signal(invcap, closeadj):
    result = invcap.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of invcap times closeadj
def ivc_f62_invested_capital_med_504d_base_v084_signal(invcap, closeadj):
    result = invcap.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of invcap
def ivc_f62_invested_capital_skew_252d_base_v085_signal(invcap):
    result = invcap.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of invcap
def ivc_f62_invested_capital_skew_504d_base_v086_signal(invcap):
    result = invcap.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of invcap
def ivc_f62_invested_capital_kurt_252d_base_v087_signal(invcap):
    result = invcap.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of invcap
def ivc_f62_invested_capital_kurt_504d_base_v088_signal(invcap):
    result = invcap.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of invcap times closeadj
def ivc_f62_invested_capital_rank_252d_base_v089_signal(invcap, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = invcap.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of invcap times closeadj
def ivc_f62_invested_capital_rank_504d_base_v090_signal(invcap, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = invcap.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of invcap times closeadj
def ivc_f62_invested_capital_rank_1008d_base_v091_signal(invcap, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = invcap.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of invcap from 63d mean times closeadj
def ivc_f62_invested_capital_devmean_63d_base_v092_signal(invcap, closeadj):
    m = _mean(invcap, 63)
    result = (invcap - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of invcap from 252d mean times closeadj
def ivc_f62_invested_capital_devmean_252d_base_v093_signal(invcap, closeadj):
    m = _mean(invcap, 252)
    result = (invcap - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of invcap from 504d mean times closeadj
def ivc_f62_invested_capital_devmean_504d_base_v094_signal(invcap, closeadj):
    m = _mean(invcap, 504)
    result = (invcap - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of invcap times closeadj
def ivc_f62_invested_capital_logdiff_21d_base_v095_signal(invcap, closeadj):
    lr = _invested_capital_log(invcap)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of invcap times closeadj
def ivc_f62_invested_capital_logdiff_63d_base_v096_signal(invcap, closeadj):
    lr = _invested_capital_log(invcap)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of invcap times closeadj
def ivc_f62_invested_capital_logdiff_252d_base_v097_signal(invcap, closeadj):
    lr = _invested_capital_log(invcap)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of invcap times closeadj
def ivc_f62_invested_capital_range_63d_base_v098_signal(invcap, closeadj):
    hi = invcap.rolling(63, min_periods=max(1, 63//2)).max()
    lo = invcap.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of invcap times closeadj
def ivc_f62_invested_capital_range_252d_base_v099_signal(invcap, closeadj):
    hi = invcap.rolling(252, min_periods=max(1, 252//2)).max()
    lo = invcap.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of invcap times closeadj
def ivc_f62_invested_capital_range_504d_base_v100_signal(invcap, closeadj):
    hi = invcap.rolling(504, min_periods=max(1, 504//2)).max()
    lo = invcap.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 252d mean times closeadj
def ivc_f62_invested_capital_rel_252d_base_v101_signal(invcap, closeadj):
    m = _mean(invcap, 252).replace(0, np.nan)
    result = (invcap / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 504d mean times closeadj
def ivc_f62_invested_capital_rel_504d_base_v102_signal(invcap, closeadj):
    m = _mean(invcap, 504).replace(0, np.nan)
    result = (invcap / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 1008d mean times closeadj
def ivc_f62_invested_capital_rel_1008d_base_v103_signal(invcap, closeadj):
    m = _mean(invcap, 1008).replace(0, np.nan)
    result = (invcap / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized invcap/assets 63d mean
def ivc_f62_invested_capital_sqnorm_assets_63d_base_v104_signal(invcap, assets):
    r = _invested_capital_scaled(invcap, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized invcap/assets 252d mean
def ivc_f62_invested_capital_sqnorm_assets_252d_base_v105_signal(invcap, assets):
    r = _invested_capital_scaled(invcap, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized invcap/marketcap 63d mean
def ivc_f62_invested_capital_sqnorm_marketcap_63d_base_v106_signal(invcap, marketcap):
    r = _invested_capital_scaled(invcap, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized invcap/marketcap 252d mean
def ivc_f62_invested_capital_sqnorm_marketcap_252d_base_v107_signal(invcap, marketcap):
    r = _invested_capital_scaled(invcap, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized invcap/equity 63d mean
def ivc_f62_invested_capital_sqnorm_equity_63d_base_v108_signal(invcap, equity):
    r = _invested_capital_scaled(invcap, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized invcap/equity 252d mean
def ivc_f62_invested_capital_sqnorm_equity_252d_base_v109_signal(invcap, equity):
    r = _invested_capital_scaled(invcap, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of invcap times closeadj
def ivc_f62_invested_capital_infrat_63d_base_v110_signal(invcap, closeadj):
    m = _mean(invcap, 63)
    s = _std(invcap, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of invcap times closeadj
def ivc_f62_invested_capital_infrat_252d_base_v111_signal(invcap, closeadj):
    m = _mean(invcap, 252)
    s = _std(invcap, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of invcap times closeadj
def ivc_f62_invested_capital_infrat_504d_base_v112_signal(invcap, closeadj):
    m = _mean(invcap, 504)
    s = _std(invcap, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of invcap
def ivc_f62_invested_capital_cv_252d_base_v113_signal(invcap):
    m = _mean(invcap, 252).abs().replace(0, np.nan)
    s = _std(invcap, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of invcap
def ivc_f62_invested_capital_cv_504d_base_v114_signal(invcap):
    m = _mean(invcap, 504).abs().replace(0, np.nan)
    s = _std(invcap, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged invcap times closeadj
def ivc_f62_invested_capital_lag_5d_base_v115_signal(invcap, closeadj):
    result = invcap.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged invcap times closeadj
def ivc_f62_invested_capital_lag_21d_base_v116_signal(invcap, closeadj):
    result = invcap.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged invcap times closeadj
def ivc_f62_invested_capital_lag_63d_base_v117_signal(invcap, closeadj):
    result = invcap.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged invcap times closeadj
def ivc_f62_invested_capital_lag_252d_base_v118_signal(invcap, closeadj):
    result = invcap.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(invcap) / mean(assets) x closeadj
def ivc_f62_invested_capital_cumper_assets_252d_base_v119_signal(invcap, assets, closeadj):
    s = invcap.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(invcap) / mean(assets) x closeadj
def ivc_f62_invested_capital_cumper_assets_504d_base_v120_signal(invcap, assets, closeadj):
    s = invcap.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(invcap) / mean(marketcap) x closeadj
def ivc_f62_invested_capital_cumper_marketcap_252d_base_v121_signal(invcap, marketcap, closeadj):
    s = invcap.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(invcap) / mean(marketcap) x closeadj
def ivc_f62_invested_capital_cumper_marketcap_504d_base_v122_signal(invcap, marketcap, closeadj):
    s = invcap.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only invcap times closeadj
def ivc_f62_invested_capital_pos_63d_base_v123_signal(invcap, closeadj):
    pos = invcap.where(invcap > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only invcap times closeadj
def ivc_f62_invested_capital_pos_252d_base_v124_signal(invcap, closeadj):
    pos = invcap.where(invcap > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only invcap times closeadj
def ivc_f62_invested_capital_neg_63d_base_v125_signal(invcap, closeadj):
    neg = invcap.where(invcap < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only invcap times closeadj
def ivc_f62_invested_capital_neg_252d_base_v126_signal(invcap, closeadj):
    neg = invcap.where(invcap < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of invcap times closeadj
def ivc_f62_invested_capital_hl_21d_base_v127_signal(invcap, closeadj):
    result = invcap.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of invcap times closeadj
def ivc_f62_invested_capital_hl_63d_base_v128_signal(invcap, closeadj):
    result = invcap.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of invcap times closeadj
def ivc_f62_invested_capital_hl_252d_base_v129_signal(invcap, closeadj):
    result = invcap.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of invcap
def ivc_f62_invested_capital_z_63d_base_v130_signal(invcap):
    result = _z(invcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of invcap
def ivc_f62_invested_capital_z_126d_base_v131_signal(invcap):
    result = _z(invcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of invcap
def ivc_f62_invested_capital_z_1008d_base_v132_signal(invcap):
    result = _z(invcap, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of invcap times closeadj
def ivc_f62_invested_capital_st_lt_252_21d_base_v133_signal(invcap, closeadj):
    sm = _mean(invcap, 21)
    lm = _mean(invcap, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of invcap times closeadj
def ivc_f62_invested_capital_st_lt_252_63d_base_v134_signal(invcap, closeadj):
    sm = _mean(invcap, 63)
    lm = _mean(invcap, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of invcap times closeadj
def ivc_f62_invested_capital_st_lt_504_21d_base_v135_signal(invcap, closeadj):
    sm = _mean(invcap, 21)
    lm = _mean(invcap, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of invcap times closeadj
def ivc_f62_invested_capital_st_lt_504_63d_base_v136_signal(invcap, closeadj):
    sm = _mean(invcap, 63)
    lm = _mean(invcap, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged invcap/assets times closeadj
def ivc_f62_invested_capital_lag_per_assets_21d_base_v137_signal(invcap, assets, closeadj):
    r = _invested_capital_scaled(invcap, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged invcap/assets times closeadj
def ivc_f62_invested_capital_lag_per_assets_63d_base_v138_signal(invcap, assets, closeadj):
    r = _invested_capital_scaled(invcap, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged invcap/assets times closeadj
def ivc_f62_invested_capital_lag_per_assets_252d_base_v139_signal(invcap, assets, closeadj):
    r = _invested_capital_scaled(invcap, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged invcap/marketcap times closeadj
def ivc_f62_invested_capital_lag_per_marketcap_21d_base_v140_signal(invcap, marketcap, closeadj):
    r = _invested_capital_scaled(invcap, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged invcap/marketcap times closeadj
def ivc_f62_invested_capital_lag_per_marketcap_63d_base_v141_signal(invcap, marketcap, closeadj):
    r = _invested_capital_scaled(invcap, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged invcap/marketcap times closeadj
def ivc_f62_invested_capital_lag_per_marketcap_252d_base_v142_signal(invcap, marketcap, closeadj):
    r = _invested_capital_scaled(invcap, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |invcap| times closeadj
def ivc_f62_invested_capital_abssum_63d_base_v143_signal(invcap, closeadj):
    result = invcap.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |invcap| times closeadj
def ivc_f62_invested_capital_abssum_252d_base_v144_signal(invcap, closeadj):
    result = invcap.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |invcap| times closeadj
def ivc_f62_invested_capital_abssum_504d_base_v145_signal(invcap, closeadj):
    result = invcap.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of invcap
def ivc_f62_invested_capital_acf1_252d_base_v146_signal(invcap):
    result = invcap.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of invcap
def ivc_f62_invested_capital_acf1_504d_base_v147_signal(invcap):
    result = invcap.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of invcap
def ivc_f62_invested_capital_posinrange_252d_base_v148_signal(invcap):
    m = _mean(invcap, 252)
    hi = invcap.rolling(252, min_periods=max(1, 252//2)).max()
    lo = invcap.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of invcap
def ivc_f62_invested_capital_posinrange_504d_base_v149_signal(invcap):
    m = _mean(invcap, 504)
    hi = invcap.rolling(504, min_periods=max(1, 504//2)).max()
    lo = invcap.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of invcap times closeadj
def ivc_f62_invested_capital_hl_5d_base_v150_signal(invcap, closeadj):
    result = invcap.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
