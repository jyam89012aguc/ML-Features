"""Family f57 - Earnings vs trailing-trend surprise  (I_Earnings_EPS) | base 076-150"""
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
def _earnings_surprise_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _earnings_surprise_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _earnings_surprise_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of netinc/marketcap
def esu_f57_earnings_surprise_log_per_marketcap_504d_base_v076_signal(netinc, marketcap):
    s = _earnings_surprise_scaled(netinc, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of netinc/equity
def esu_f57_earnings_surprise_log_per_equity_252d_base_v077_signal(netinc, equity):
    s = _earnings_surprise_scaled(netinc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of netinc/equity
def esu_f57_earnings_surprise_log_per_equity_504d_base_v078_signal(netinc, equity):
    s = _earnings_surprise_scaled(netinc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of netinc times closeadj
def esu_f57_earnings_surprise_ewm_21d_base_v079_signal(netinc, closeadj):
    result = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of netinc times closeadj
def esu_f57_earnings_surprise_ewm_63d_base_v080_signal(netinc, closeadj):
    result = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of netinc times closeadj
def esu_f57_earnings_surprise_ewm_252d_base_v081_signal(netinc, closeadj):
    result = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of netinc times closeadj
def esu_f57_earnings_surprise_med_63d_base_v082_signal(netinc, closeadj):
    result = netinc.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of netinc times closeadj
def esu_f57_earnings_surprise_med_252d_base_v083_signal(netinc, closeadj):
    result = netinc.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of netinc times closeadj
def esu_f57_earnings_surprise_med_504d_base_v084_signal(netinc, closeadj):
    result = netinc.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of netinc
def esu_f57_earnings_surprise_skew_252d_base_v085_signal(netinc):
    result = netinc.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of netinc
def esu_f57_earnings_surprise_skew_504d_base_v086_signal(netinc):
    result = netinc.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of netinc
def esu_f57_earnings_surprise_kurt_252d_base_v087_signal(netinc):
    result = netinc.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of netinc
def esu_f57_earnings_surprise_kurt_504d_base_v088_signal(netinc):
    result = netinc.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of netinc times closeadj
def esu_f57_earnings_surprise_rank_252d_base_v089_signal(netinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = netinc.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of netinc times closeadj
def esu_f57_earnings_surprise_rank_504d_base_v090_signal(netinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = netinc.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of netinc times closeadj
def esu_f57_earnings_surprise_rank_1008d_base_v091_signal(netinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = netinc.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of netinc from 63d mean times closeadj
def esu_f57_earnings_surprise_devmean_63d_base_v092_signal(netinc, closeadj):
    m = _mean(netinc, 63)
    result = (netinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of netinc from 252d mean times closeadj
def esu_f57_earnings_surprise_devmean_252d_base_v093_signal(netinc, closeadj):
    m = _mean(netinc, 252)
    result = (netinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of netinc from 504d mean times closeadj
def esu_f57_earnings_surprise_devmean_504d_base_v094_signal(netinc, closeadj):
    m = _mean(netinc, 504)
    result = (netinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of netinc times closeadj
def esu_f57_earnings_surprise_logdiff_21d_base_v095_signal(netinc, closeadj):
    lr = _earnings_surprise_log(netinc)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of netinc times closeadj
def esu_f57_earnings_surprise_logdiff_63d_base_v096_signal(netinc, closeadj):
    lr = _earnings_surprise_log(netinc)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of netinc times closeadj
def esu_f57_earnings_surprise_logdiff_252d_base_v097_signal(netinc, closeadj):
    lr = _earnings_surprise_log(netinc)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of netinc times closeadj
def esu_f57_earnings_surprise_range_63d_base_v098_signal(netinc, closeadj):
    hi = netinc.rolling(63, min_periods=max(1, 63//2)).max()
    lo = netinc.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of netinc times closeadj
def esu_f57_earnings_surprise_range_252d_base_v099_signal(netinc, closeadj):
    hi = netinc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = netinc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of netinc times closeadj
def esu_f57_earnings_surprise_range_504d_base_v100_signal(netinc, closeadj):
    hi = netinc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = netinc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 252d mean times closeadj
def esu_f57_earnings_surprise_rel_252d_base_v101_signal(netinc, closeadj):
    m = _mean(netinc, 252).replace(0, np.nan)
    result = (netinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 504d mean times closeadj
def esu_f57_earnings_surprise_rel_504d_base_v102_signal(netinc, closeadj):
    m = _mean(netinc, 504).replace(0, np.nan)
    result = (netinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netinc relative to 1008d mean times closeadj
def esu_f57_earnings_surprise_rel_1008d_base_v103_signal(netinc, closeadj):
    m = _mean(netinc, 1008).replace(0, np.nan)
    result = (netinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netinc/assets 63d mean
def esu_f57_earnings_surprise_sqnorm_assets_63d_base_v104_signal(netinc, assets):
    r = _earnings_surprise_scaled(netinc, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netinc/assets 252d mean
def esu_f57_earnings_surprise_sqnorm_assets_252d_base_v105_signal(netinc, assets):
    r = _earnings_surprise_scaled(netinc, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netinc/marketcap 63d mean
def esu_f57_earnings_surprise_sqnorm_marketcap_63d_base_v106_signal(netinc, marketcap):
    r = _earnings_surprise_scaled(netinc, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netinc/marketcap 252d mean
def esu_f57_earnings_surprise_sqnorm_marketcap_252d_base_v107_signal(netinc, marketcap):
    r = _earnings_surprise_scaled(netinc, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netinc/equity 63d mean
def esu_f57_earnings_surprise_sqnorm_equity_63d_base_v108_signal(netinc, equity):
    r = _earnings_surprise_scaled(netinc, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized netinc/equity 252d mean
def esu_f57_earnings_surprise_sqnorm_equity_252d_base_v109_signal(netinc, equity):
    r = _earnings_surprise_scaled(netinc, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of netinc times closeadj
def esu_f57_earnings_surprise_infrat_63d_base_v110_signal(netinc, closeadj):
    m = _mean(netinc, 63)
    s = _std(netinc, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of netinc times closeadj
def esu_f57_earnings_surprise_infrat_252d_base_v111_signal(netinc, closeadj):
    m = _mean(netinc, 252)
    s = _std(netinc, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of netinc times closeadj
def esu_f57_earnings_surprise_infrat_504d_base_v112_signal(netinc, closeadj):
    m = _mean(netinc, 504)
    s = _std(netinc, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of netinc
def esu_f57_earnings_surprise_cv_252d_base_v113_signal(netinc):
    m = _mean(netinc, 252).abs().replace(0, np.nan)
    s = _std(netinc, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of netinc
def esu_f57_earnings_surprise_cv_504d_base_v114_signal(netinc):
    m = _mean(netinc, 504).abs().replace(0, np.nan)
    s = _std(netinc, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged netinc times closeadj
def esu_f57_earnings_surprise_lag_5d_base_v115_signal(netinc, closeadj):
    result = netinc.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged netinc times closeadj
def esu_f57_earnings_surprise_lag_21d_base_v116_signal(netinc, closeadj):
    result = netinc.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged netinc times closeadj
def esu_f57_earnings_surprise_lag_63d_base_v117_signal(netinc, closeadj):
    result = netinc.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged netinc times closeadj
def esu_f57_earnings_surprise_lag_252d_base_v118_signal(netinc, closeadj):
    result = netinc.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(netinc) / mean(assets) x closeadj
def esu_f57_earnings_surprise_cumper_assets_252d_base_v119_signal(netinc, assets, closeadj):
    s = netinc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(netinc) / mean(assets) x closeadj
def esu_f57_earnings_surprise_cumper_assets_504d_base_v120_signal(netinc, assets, closeadj):
    s = netinc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(netinc) / mean(marketcap) x closeadj
def esu_f57_earnings_surprise_cumper_marketcap_252d_base_v121_signal(netinc, marketcap, closeadj):
    s = netinc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(netinc) / mean(marketcap) x closeadj
def esu_f57_earnings_surprise_cumper_marketcap_504d_base_v122_signal(netinc, marketcap, closeadj):
    s = netinc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only netinc times closeadj
def esu_f57_earnings_surprise_pos_63d_base_v123_signal(netinc, closeadj):
    pos = netinc.where(netinc > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only netinc times closeadj
def esu_f57_earnings_surprise_pos_252d_base_v124_signal(netinc, closeadj):
    pos = netinc.where(netinc > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only netinc times closeadj
def esu_f57_earnings_surprise_neg_63d_base_v125_signal(netinc, closeadj):
    neg = netinc.where(netinc < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only netinc times closeadj
def esu_f57_earnings_surprise_neg_252d_base_v126_signal(netinc, closeadj):
    neg = netinc.where(netinc < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of netinc times closeadj
def esu_f57_earnings_surprise_hl_21d_base_v127_signal(netinc, closeadj):
    result = netinc.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of netinc times closeadj
def esu_f57_earnings_surprise_hl_63d_base_v128_signal(netinc, closeadj):
    result = netinc.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of netinc times closeadj
def esu_f57_earnings_surprise_hl_252d_base_v129_signal(netinc, closeadj):
    result = netinc.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of netinc
def esu_f57_earnings_surprise_z_63d_base_v130_signal(netinc):
    result = _z(netinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of netinc
def esu_f57_earnings_surprise_z_126d_base_v131_signal(netinc):
    result = _z(netinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of netinc
def esu_f57_earnings_surprise_z_1008d_base_v132_signal(netinc):
    result = _z(netinc, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of netinc times closeadj
def esu_f57_earnings_surprise_st_lt_252_21d_base_v133_signal(netinc, closeadj):
    sm = _mean(netinc, 21)
    lm = _mean(netinc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of netinc times closeadj
def esu_f57_earnings_surprise_st_lt_252_63d_base_v134_signal(netinc, closeadj):
    sm = _mean(netinc, 63)
    lm = _mean(netinc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of netinc times closeadj
def esu_f57_earnings_surprise_st_lt_504_21d_base_v135_signal(netinc, closeadj):
    sm = _mean(netinc, 21)
    lm = _mean(netinc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of netinc times closeadj
def esu_f57_earnings_surprise_st_lt_504_63d_base_v136_signal(netinc, closeadj):
    sm = _mean(netinc, 63)
    lm = _mean(netinc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged netinc/assets times closeadj
def esu_f57_earnings_surprise_lag_per_assets_21d_base_v137_signal(netinc, assets, closeadj):
    r = _earnings_surprise_scaled(netinc, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged netinc/assets times closeadj
def esu_f57_earnings_surprise_lag_per_assets_63d_base_v138_signal(netinc, assets, closeadj):
    r = _earnings_surprise_scaled(netinc, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged netinc/assets times closeadj
def esu_f57_earnings_surprise_lag_per_assets_252d_base_v139_signal(netinc, assets, closeadj):
    r = _earnings_surprise_scaled(netinc, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged netinc/marketcap times closeadj
def esu_f57_earnings_surprise_lag_per_marketcap_21d_base_v140_signal(netinc, marketcap, closeadj):
    r = _earnings_surprise_scaled(netinc, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged netinc/marketcap times closeadj
def esu_f57_earnings_surprise_lag_per_marketcap_63d_base_v141_signal(netinc, marketcap, closeadj):
    r = _earnings_surprise_scaled(netinc, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged netinc/marketcap times closeadj
def esu_f57_earnings_surprise_lag_per_marketcap_252d_base_v142_signal(netinc, marketcap, closeadj):
    r = _earnings_surprise_scaled(netinc, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |netinc| times closeadj
def esu_f57_earnings_surprise_abssum_63d_base_v143_signal(netinc, closeadj):
    result = netinc.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |netinc| times closeadj
def esu_f57_earnings_surprise_abssum_252d_base_v144_signal(netinc, closeadj):
    result = netinc.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |netinc| times closeadj
def esu_f57_earnings_surprise_abssum_504d_base_v145_signal(netinc, closeadj):
    result = netinc.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of netinc
def esu_f57_earnings_surprise_acf1_252d_base_v146_signal(netinc):
    result = netinc.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of netinc
def esu_f57_earnings_surprise_acf1_504d_base_v147_signal(netinc):
    result = netinc.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of netinc
def esu_f57_earnings_surprise_posinrange_252d_base_v148_signal(netinc):
    m = _mean(netinc, 252)
    hi = netinc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = netinc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of netinc
def esu_f57_earnings_surprise_posinrange_504d_base_v149_signal(netinc):
    m = _mean(netinc, 504)
    hi = netinc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = netinc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of netinc times closeadj
def esu_f57_earnings_surprise_hl_5d_base_v150_signal(netinc, closeadj):
    result = netinc.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
