"""Family f97 - Multi-year price context  (R_Price_Context) | base 076-150"""
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
def _multi_year_price_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _multi_year_price_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _multi_year_price_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of close/marketcap
def mpc_f97_multi_year_price_context_log_per_marketcap_504d_base_v076_signal(close, marketcap):
    s = _multi_year_price_context_scaled(close, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of close/equity
def mpc_f97_multi_year_price_context_log_per_equity_252d_base_v077_signal(close, equity):
    s = _multi_year_price_context_scaled(close, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of close/equity
def mpc_f97_multi_year_price_context_log_per_equity_504d_base_v078_signal(close, equity):
    s = _multi_year_price_context_scaled(close, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of close times closeadj
def mpc_f97_multi_year_price_context_ewm_21d_base_v079_signal(close, closeadj):
    result = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of close times closeadj
def mpc_f97_multi_year_price_context_ewm_63d_base_v080_signal(close, closeadj):
    result = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of close times closeadj
def mpc_f97_multi_year_price_context_ewm_252d_base_v081_signal(close, closeadj):
    result = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of close times closeadj
def mpc_f97_multi_year_price_context_med_63d_base_v082_signal(close, closeadj):
    result = close.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of close times closeadj
def mpc_f97_multi_year_price_context_med_252d_base_v083_signal(close, closeadj):
    result = close.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of close times closeadj
def mpc_f97_multi_year_price_context_med_504d_base_v084_signal(close, closeadj):
    result = close.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of close
def mpc_f97_multi_year_price_context_skew_252d_base_v085_signal(close):
    result = close.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of close
def mpc_f97_multi_year_price_context_skew_504d_base_v086_signal(close):
    result = close.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of close
def mpc_f97_multi_year_price_context_kurt_252d_base_v087_signal(close):
    result = close.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of close
def mpc_f97_multi_year_price_context_kurt_504d_base_v088_signal(close):
    result = close.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of close times closeadj
def mpc_f97_multi_year_price_context_rank_252d_base_v089_signal(close, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = close.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of close times closeadj
def mpc_f97_multi_year_price_context_rank_504d_base_v090_signal(close, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = close.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of close times closeadj
def mpc_f97_multi_year_price_context_rank_1008d_base_v091_signal(close, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = close.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of close from 63d mean times closeadj
def mpc_f97_multi_year_price_context_devmean_63d_base_v092_signal(close, closeadj):
    m = _mean(close, 63)
    result = (close - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of close from 252d mean times closeadj
def mpc_f97_multi_year_price_context_devmean_252d_base_v093_signal(close, closeadj):
    m = _mean(close, 252)
    result = (close - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of close from 504d mean times closeadj
def mpc_f97_multi_year_price_context_devmean_504d_base_v094_signal(close, closeadj):
    m = _mean(close, 504)
    result = (close - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of close times closeadj
def mpc_f97_multi_year_price_context_logdiff_21d_base_v095_signal(close, closeadj):
    lr = _multi_year_price_context_log(close)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of close times closeadj
def mpc_f97_multi_year_price_context_logdiff_63d_base_v096_signal(close, closeadj):
    lr = _multi_year_price_context_log(close)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of close times closeadj
def mpc_f97_multi_year_price_context_logdiff_252d_base_v097_signal(close, closeadj):
    lr = _multi_year_price_context_log(close)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of close times closeadj
def mpc_f97_multi_year_price_context_range_63d_base_v098_signal(close, closeadj):
    hi = close.rolling(63, min_periods=max(1, 63//2)).max()
    lo = close.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of close times closeadj
def mpc_f97_multi_year_price_context_range_252d_base_v099_signal(close, closeadj):
    hi = close.rolling(252, min_periods=max(1, 252//2)).max()
    lo = close.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of close times closeadj
def mpc_f97_multi_year_price_context_range_504d_base_v100_signal(close, closeadj):
    hi = close.rolling(504, min_periods=max(1, 504//2)).max()
    lo = close.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 252d mean times closeadj
def mpc_f97_multi_year_price_context_rel_252d_base_v101_signal(close, closeadj):
    m = _mean(close, 252).replace(0, np.nan)
    result = (close / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 504d mean times closeadj
def mpc_f97_multi_year_price_context_rel_504d_base_v102_signal(close, closeadj):
    m = _mean(close, 504).replace(0, np.nan)
    result = (close / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# close relative to 1008d mean times closeadj
def mpc_f97_multi_year_price_context_rel_1008d_base_v103_signal(close, closeadj):
    m = _mean(close, 1008).replace(0, np.nan)
    result = (close / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized close/assets 63d mean
def mpc_f97_multi_year_price_context_sqnorm_assets_63d_base_v104_signal(close, assets):
    r = _multi_year_price_context_scaled(close, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized close/assets 252d mean
def mpc_f97_multi_year_price_context_sqnorm_assets_252d_base_v105_signal(close, assets):
    r = _multi_year_price_context_scaled(close, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized close/marketcap 63d mean
def mpc_f97_multi_year_price_context_sqnorm_marketcap_63d_base_v106_signal(close, marketcap):
    r = _multi_year_price_context_scaled(close, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized close/marketcap 252d mean
def mpc_f97_multi_year_price_context_sqnorm_marketcap_252d_base_v107_signal(close, marketcap):
    r = _multi_year_price_context_scaled(close, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized close/equity 63d mean
def mpc_f97_multi_year_price_context_sqnorm_equity_63d_base_v108_signal(close, equity):
    r = _multi_year_price_context_scaled(close, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized close/equity 252d mean
def mpc_f97_multi_year_price_context_sqnorm_equity_252d_base_v109_signal(close, equity):
    r = _multi_year_price_context_scaled(close, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of close times closeadj
def mpc_f97_multi_year_price_context_infrat_63d_base_v110_signal(close, closeadj):
    m = _mean(close, 63)
    s = _std(close, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of close times closeadj
def mpc_f97_multi_year_price_context_infrat_252d_base_v111_signal(close, closeadj):
    m = _mean(close, 252)
    s = _std(close, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of close times closeadj
def mpc_f97_multi_year_price_context_infrat_504d_base_v112_signal(close, closeadj):
    m = _mean(close, 504)
    s = _std(close, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of close
def mpc_f97_multi_year_price_context_cv_252d_base_v113_signal(close):
    m = _mean(close, 252).abs().replace(0, np.nan)
    s = _std(close, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of close
def mpc_f97_multi_year_price_context_cv_504d_base_v114_signal(close):
    m = _mean(close, 504).abs().replace(0, np.nan)
    s = _std(close, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged close times closeadj
def mpc_f97_multi_year_price_context_lag_5d_base_v115_signal(close, closeadj):
    result = close.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged close times closeadj
def mpc_f97_multi_year_price_context_lag_21d_base_v116_signal(close, closeadj):
    result = close.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged close times closeadj
def mpc_f97_multi_year_price_context_lag_63d_base_v117_signal(close, closeadj):
    result = close.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged close times closeadj
def mpc_f97_multi_year_price_context_lag_252d_base_v118_signal(close, closeadj):
    result = close.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(close) / mean(assets) x closeadj
def mpc_f97_multi_year_price_context_cumper_assets_252d_base_v119_signal(close, assets, closeadj):
    s = close.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(close) / mean(assets) x closeadj
def mpc_f97_multi_year_price_context_cumper_assets_504d_base_v120_signal(close, assets, closeadj):
    s = close.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(close) / mean(marketcap) x closeadj
def mpc_f97_multi_year_price_context_cumper_marketcap_252d_base_v121_signal(close, marketcap, closeadj):
    s = close.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(close) / mean(marketcap) x closeadj
def mpc_f97_multi_year_price_context_cumper_marketcap_504d_base_v122_signal(close, marketcap, closeadj):
    s = close.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only close times closeadj
def mpc_f97_multi_year_price_context_pos_63d_base_v123_signal(close, closeadj):
    pos = close.where(close > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only close times closeadj
def mpc_f97_multi_year_price_context_pos_252d_base_v124_signal(close, closeadj):
    pos = close.where(close > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only close times closeadj
def mpc_f97_multi_year_price_context_neg_63d_base_v125_signal(close, closeadj):
    neg = close.where(close < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only close times closeadj
def mpc_f97_multi_year_price_context_neg_252d_base_v126_signal(close, closeadj):
    neg = close.where(close < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of close times closeadj
def mpc_f97_multi_year_price_context_hl_21d_base_v127_signal(close, closeadj):
    result = close.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of close times closeadj
def mpc_f97_multi_year_price_context_hl_63d_base_v128_signal(close, closeadj):
    result = close.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of close times closeadj
def mpc_f97_multi_year_price_context_hl_252d_base_v129_signal(close, closeadj):
    result = close.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of close
def mpc_f97_multi_year_price_context_z_63d_base_v130_signal(close):
    result = _z(close, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of close
def mpc_f97_multi_year_price_context_z_126d_base_v131_signal(close):
    result = _z(close, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of close
def mpc_f97_multi_year_price_context_z_1008d_base_v132_signal(close):
    result = _z(close, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of close times closeadj
def mpc_f97_multi_year_price_context_st_lt_252_21d_base_v133_signal(close, closeadj):
    sm = _mean(close, 21)
    lm = _mean(close, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of close times closeadj
def mpc_f97_multi_year_price_context_st_lt_252_63d_base_v134_signal(close, closeadj):
    sm = _mean(close, 63)
    lm = _mean(close, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of close times closeadj
def mpc_f97_multi_year_price_context_st_lt_504_21d_base_v135_signal(close, closeadj):
    sm = _mean(close, 21)
    lm = _mean(close, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of close times closeadj
def mpc_f97_multi_year_price_context_st_lt_504_63d_base_v136_signal(close, closeadj):
    sm = _mean(close, 63)
    lm = _mean(close, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged close/assets times closeadj
def mpc_f97_multi_year_price_context_lag_per_assets_21d_base_v137_signal(close, assets, closeadj):
    r = _multi_year_price_context_scaled(close, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged close/assets times closeadj
def mpc_f97_multi_year_price_context_lag_per_assets_63d_base_v138_signal(close, assets, closeadj):
    r = _multi_year_price_context_scaled(close, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged close/assets times closeadj
def mpc_f97_multi_year_price_context_lag_per_assets_252d_base_v139_signal(close, assets, closeadj):
    r = _multi_year_price_context_scaled(close, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged close/marketcap times closeadj
def mpc_f97_multi_year_price_context_lag_per_marketcap_21d_base_v140_signal(close, marketcap, closeadj):
    r = _multi_year_price_context_scaled(close, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged close/marketcap times closeadj
def mpc_f97_multi_year_price_context_lag_per_marketcap_63d_base_v141_signal(close, marketcap, closeadj):
    r = _multi_year_price_context_scaled(close, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged close/marketcap times closeadj
def mpc_f97_multi_year_price_context_lag_per_marketcap_252d_base_v142_signal(close, marketcap, closeadj):
    r = _multi_year_price_context_scaled(close, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |close| times closeadj
def mpc_f97_multi_year_price_context_abssum_63d_base_v143_signal(close, closeadj):
    result = close.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |close| times closeadj
def mpc_f97_multi_year_price_context_abssum_252d_base_v144_signal(close, closeadj):
    result = close.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |close| times closeadj
def mpc_f97_multi_year_price_context_abssum_504d_base_v145_signal(close, closeadj):
    result = close.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of close
def mpc_f97_multi_year_price_context_acf1_252d_base_v146_signal(close):
    result = close.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of close
def mpc_f97_multi_year_price_context_acf1_504d_base_v147_signal(close):
    result = close.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of close
def mpc_f97_multi_year_price_context_posinrange_252d_base_v148_signal(close):
    m = _mean(close, 252)
    hi = close.rolling(252, min_periods=max(1, 252//2)).max()
    lo = close.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of close
def mpc_f97_multi_year_price_context_posinrange_504d_base_v149_signal(close):
    m = _mean(close, 504)
    hi = close.rolling(504, min_periods=max(1, 504//2)).max()
    lo = close.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of close times closeadj
def mpc_f97_multi_year_price_context_hl_5d_base_v150_signal(close, closeadj):
    result = close.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
