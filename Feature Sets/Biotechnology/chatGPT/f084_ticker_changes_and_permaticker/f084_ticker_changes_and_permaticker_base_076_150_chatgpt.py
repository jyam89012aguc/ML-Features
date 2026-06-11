"""Family f084 - Identifier continuity (Security Master and Universe) | Sharadar tables: TICKERS | fields: ticker, permaticker, relatedtickers, table, currency | base 076-150"""
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
def _ticker_changes_and_permaticker_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ticker_changes_and_permaticker_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ticker_changes_and_permaticker_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ticker_change_count/marketcap
def tcap_f084_ticker_changes_and_permaticker_log_per_marketcap_504d_base_v076_signal(ticker_change_count, marketcap):
    s = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ticker_change_count/equity
def tcap_f084_ticker_changes_and_permaticker_log_per_equity_252d_base_v077_signal(ticker_change_count, equity):
    s = _ticker_changes_and_permaticker_scaled(ticker_change_count, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ticker_change_count/equity
def tcap_f084_ticker_changes_and_permaticker_log_per_equity_504d_base_v078_signal(ticker_change_count, equity):
    s = _ticker_changes_and_permaticker_scaled(ticker_change_count, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_ewm_21d_base_v079_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_ewm_63d_base_v080_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_ewm_252d_base_v081_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_med_63d_base_v082_signal(ticker_change_count, closeadj):
    result = ticker_change_count.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_med_252d_base_v083_signal(ticker_change_count, closeadj):
    result = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_med_504d_base_v084_signal(ticker_change_count, closeadj):
    result = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_skew_252d_base_v085_signal(ticker_change_count):
    result = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_skew_504d_base_v086_signal(ticker_change_count):
    result = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_kurt_252d_base_v087_signal(ticker_change_count):
    result = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_kurt_504d_base_v088_signal(ticker_change_count):
    result = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_rank_252d_base_v089_signal(ticker_change_count, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_rank_504d_base_v090_signal(ticker_change_count, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_rank_1008d_base_v091_signal(ticker_change_count, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ticker_change_count.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ticker_change_count from 63d mean times closeadj
def tcap_f084_ticker_changes_and_permaticker_devmean_63d_base_v092_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 63)
    result = (ticker_change_count - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ticker_change_count from 252d mean times closeadj
def tcap_f084_ticker_changes_and_permaticker_devmean_252d_base_v093_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 252)
    result = (ticker_change_count - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ticker_change_count from 504d mean times closeadj
def tcap_f084_ticker_changes_and_permaticker_devmean_504d_base_v094_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 504)
    result = (ticker_change_count - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_logdiff_21d_base_v095_signal(ticker_change_count, closeadj):
    lr = _ticker_changes_and_permaticker_log(ticker_change_count)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_logdiff_63d_base_v096_signal(ticker_change_count, closeadj):
    lr = _ticker_changes_and_permaticker_log(ticker_change_count)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_logdiff_252d_base_v097_signal(ticker_change_count, closeadj):
    lr = _ticker_changes_and_permaticker_log(ticker_change_count)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_range_63d_base_v098_signal(ticker_change_count, closeadj):
    hi = ticker_change_count.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ticker_change_count.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_range_252d_base_v099_signal(ticker_change_count, closeadj):
    hi = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_range_504d_base_v100_signal(ticker_change_count, closeadj):
    hi = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 252d mean times closeadj
def tcap_f084_ticker_changes_and_permaticker_rel_252d_base_v101_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 252).replace(0, np.nan)
    result = (ticker_change_count / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 504d mean times closeadj
def tcap_f084_ticker_changes_and_permaticker_rel_504d_base_v102_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 504).replace(0, np.nan)
    result = (ticker_change_count / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 1008d mean times closeadj
def tcap_f084_ticker_changes_and_permaticker_rel_1008d_base_v103_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 1008).replace(0, np.nan)
    result = (ticker_change_count / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ticker_change_count/assets 63d mean
def tcap_f084_ticker_changes_and_permaticker_sqnorm_assets_63d_base_v104_signal(ticker_change_count, assets):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ticker_change_count/assets 252d mean
def tcap_f084_ticker_changes_and_permaticker_sqnorm_assets_252d_base_v105_signal(ticker_change_count, assets):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ticker_change_count/marketcap 63d mean
def tcap_f084_ticker_changes_and_permaticker_sqnorm_marketcap_63d_base_v106_signal(ticker_change_count, marketcap):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ticker_change_count/marketcap 252d mean
def tcap_f084_ticker_changes_and_permaticker_sqnorm_marketcap_252d_base_v107_signal(ticker_change_count, marketcap):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ticker_change_count/equity 63d mean
def tcap_f084_ticker_changes_and_permaticker_sqnorm_equity_63d_base_v108_signal(ticker_change_count, equity):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ticker_change_count/equity 252d mean
def tcap_f084_ticker_changes_and_permaticker_sqnorm_equity_252d_base_v109_signal(ticker_change_count, equity):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_infrat_63d_base_v110_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 63)
    s = _std(ticker_change_count, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_infrat_252d_base_v111_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 252)
    s = _std(ticker_change_count, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_infrat_504d_base_v112_signal(ticker_change_count, closeadj):
    m = _mean(ticker_change_count, 504)
    s = _std(ticker_change_count, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_cv_252d_base_v113_signal(ticker_change_count):
    m = _mean(ticker_change_count, 252).abs().replace(0, np.nan)
    s = _std(ticker_change_count, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_cv_504d_base_v114_signal(ticker_change_count):
    m = _mean(ticker_change_count, 504).abs().replace(0, np.nan)
    s = _std(ticker_change_count, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_5d_base_v115_signal(ticker_change_count, closeadj):
    result = ticker_change_count.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_21d_base_v116_signal(ticker_change_count, closeadj):
    result = ticker_change_count.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_63d_base_v117_signal(ticker_change_count, closeadj):
    result = ticker_change_count.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_252d_base_v118_signal(ticker_change_count, closeadj):
    result = ticker_change_count.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ticker_change_count) / mean(assets) x closeadj
def tcap_f084_ticker_changes_and_permaticker_cumper_assets_252d_base_v119_signal(ticker_change_count, assets, closeadj):
    s = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ticker_change_count) / mean(assets) x closeadj
def tcap_f084_ticker_changes_and_permaticker_cumper_assets_504d_base_v120_signal(ticker_change_count, assets, closeadj):
    s = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ticker_change_count) / mean(marketcap) x closeadj
def tcap_f084_ticker_changes_and_permaticker_cumper_marketcap_252d_base_v121_signal(ticker_change_count, marketcap, closeadj):
    s = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ticker_change_count) / mean(marketcap) x closeadj
def tcap_f084_ticker_changes_and_permaticker_cumper_marketcap_504d_base_v122_signal(ticker_change_count, marketcap, closeadj):
    s = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_pos_63d_base_v123_signal(ticker_change_count, closeadj):
    pos = ticker_change_count.where(ticker_change_count > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_pos_252d_base_v124_signal(ticker_change_count, closeadj):
    pos = ticker_change_count.where(ticker_change_count > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_neg_63d_base_v125_signal(ticker_change_count, closeadj):
    neg = ticker_change_count.where(ticker_change_count < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_neg_252d_base_v126_signal(ticker_change_count, closeadj):
    neg = ticker_change_count.where(ticker_change_count < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_hl_21d_base_v127_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_hl_63d_base_v128_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_hl_252d_base_v129_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_63d_base_v130_signal(ticker_change_count):
    result = _z(ticker_change_count, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_126d_base_v131_signal(ticker_change_count):
    result = _z(ticker_change_count, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_1008d_base_v132_signal(ticker_change_count):
    result = _z(ticker_change_count, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_st_lt_252_21d_base_v133_signal(ticker_change_count, closeadj):
    sm = _mean(ticker_change_count, 21)
    lm = _mean(ticker_change_count, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_st_lt_252_63d_base_v134_signal(ticker_change_count, closeadj):
    sm = _mean(ticker_change_count, 63)
    lm = _mean(ticker_change_count, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_st_lt_504_21d_base_v135_signal(ticker_change_count, closeadj):
    sm = _mean(ticker_change_count, 21)
    lm = _mean(ticker_change_count, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_st_lt_504_63d_base_v136_signal(ticker_change_count, closeadj):
    sm = _mean(ticker_change_count, 63)
    lm = _mean(ticker_change_count, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ticker_change_count/assets times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_per_assets_21d_base_v137_signal(ticker_change_count, assets, closeadj):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ticker_change_count/assets times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_per_assets_63d_base_v138_signal(ticker_change_count, assets, closeadj):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ticker_change_count/assets times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_per_assets_252d_base_v139_signal(ticker_change_count, assets, closeadj):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ticker_change_count/marketcap times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_per_marketcap_21d_base_v140_signal(ticker_change_count, marketcap, closeadj):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ticker_change_count/marketcap times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_per_marketcap_63d_base_v141_signal(ticker_change_count, marketcap, closeadj):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ticker_change_count/marketcap times closeadj
def tcap_f084_ticker_changes_and_permaticker_lag_per_marketcap_252d_base_v142_signal(ticker_change_count, marketcap, closeadj):
    r = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ticker_change_count| times closeadj
def tcap_f084_ticker_changes_and_permaticker_abssum_63d_base_v143_signal(ticker_change_count, closeadj):
    result = ticker_change_count.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ticker_change_count| times closeadj
def tcap_f084_ticker_changes_and_permaticker_abssum_252d_base_v144_signal(ticker_change_count, closeadj):
    result = ticker_change_count.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ticker_change_count| times closeadj
def tcap_f084_ticker_changes_and_permaticker_abssum_504d_base_v145_signal(ticker_change_count, closeadj):
    result = ticker_change_count.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_acf1_252d_base_v146_signal(ticker_change_count):
    result = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_acf1_504d_base_v147_signal(ticker_change_count):
    result = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_posinrange_252d_base_v148_signal(ticker_change_count):
    m = _mean(ticker_change_count, 252)
    hi = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_posinrange_504d_base_v149_signal(ticker_change_count):
    m = _mean(ticker_change_count, 504)
    hi = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_hl_5d_base_v150_signal(ticker_change_count, closeadj):
    result = ticker_change_count.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
