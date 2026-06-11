"""Family f088 - OHLCV highest-highs context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: date, open, high, low, close, volume, closeadj, closeunadj | base 076-150"""
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
def _ohlcv_multi_year_highs_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ohlcv_multi_year_highs_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ohlcv_multi_year_highs_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of open/low
def omyh_f088_ohlcv_multi_year_highs_log_per_low_504d_base_v076_signal(open, low):
    s = _ohlcv_multi_year_highs_scaled(open, low)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of open/close
def omyh_f088_ohlcv_multi_year_highs_log_per_close_252d_base_v077_signal(open, close):
    s = _ohlcv_multi_year_highs_scaled(open, close)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of open/close
def omyh_f088_ohlcv_multi_year_highs_log_per_close_504d_base_v078_signal(open, close):
    s = _ohlcv_multi_year_highs_scaled(open, close)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_base_v079_signal(open, closeadj):
    result = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_base_v080_signal(open, closeadj):
    result = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_base_v081_signal(open, closeadj):
    result = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_med_63d_base_v082_signal(open, closeadj):
    result = open.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_med_252d_base_v083_signal(open, closeadj):
    result = open.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_med_504d_base_v084_signal(open, closeadj):
    result = open.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of open
def omyh_f088_ohlcv_multi_year_highs_skew_252d_base_v085_signal(open):
    result = open.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of open
def omyh_f088_ohlcv_multi_year_highs_skew_504d_base_v086_signal(open):
    result = open.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of open
def omyh_f088_ohlcv_multi_year_highs_kurt_252d_base_v087_signal(open):
    result = open.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of open
def omyh_f088_ohlcv_multi_year_highs_kurt_504d_base_v088_signal(open):
    result = open.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_rank_252d_base_v089_signal(open, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = open.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_rank_504d_base_v090_signal(open, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = open.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_rank_1008d_base_v091_signal(open, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = open.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of open from 63d mean times closeadj
def omyh_f088_ohlcv_multi_year_highs_devmean_63d_base_v092_signal(open, closeadj):
    m = _mean(open, 63)
    result = (open - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of open from 252d mean times closeadj
def omyh_f088_ohlcv_multi_year_highs_devmean_252d_base_v093_signal(open, closeadj):
    m = _mean(open, 252)
    result = (open - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of open from 504d mean times closeadj
def omyh_f088_ohlcv_multi_year_highs_devmean_504d_base_v094_signal(open, closeadj):
    m = _mean(open, 504)
    result = (open - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_logdiff_21d_base_v095_signal(open, closeadj):
    lr = _ohlcv_multi_year_highs_log(open)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_logdiff_63d_base_v096_signal(open, closeadj):
    lr = _ohlcv_multi_year_highs_log(open)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_logdiff_252d_base_v097_signal(open, closeadj):
    lr = _ohlcv_multi_year_highs_log(open)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_range_63d_base_v098_signal(open, closeadj):
    hi = open.rolling(63, min_periods=max(1, 63//2)).max()
    lo = open.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_range_252d_base_v099_signal(open, closeadj):
    hi = open.rolling(252, min_periods=max(1, 252//2)).max()
    lo = open.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_range_504d_base_v100_signal(open, closeadj):
    hi = open.rolling(504, min_periods=max(1, 504//2)).max()
    lo = open.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 252d mean times closeadj
def omyh_f088_ohlcv_multi_year_highs_rel_252d_base_v101_signal(open, closeadj):
    m = _mean(open, 252).replace(0, np.nan)
    result = (open / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 504d mean times closeadj
def omyh_f088_ohlcv_multi_year_highs_rel_504d_base_v102_signal(open, closeadj):
    m = _mean(open, 504).replace(0, np.nan)
    result = (open / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# open relative to 1008d mean times closeadj
def omyh_f088_ohlcv_multi_year_highs_rel_1008d_base_v103_signal(open, closeadj):
    m = _mean(open, 1008).replace(0, np.nan)
    result = (open / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized open/high 63d mean
def omyh_f088_ohlcv_multi_year_highs_sqnorm_high_63d_base_v104_signal(open, high):
    r = _ohlcv_multi_year_highs_scaled(open, high)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized open/high 252d mean
def omyh_f088_ohlcv_multi_year_highs_sqnorm_high_252d_base_v105_signal(open, high):
    r = _ohlcv_multi_year_highs_scaled(open, high)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized open/low 63d mean
def omyh_f088_ohlcv_multi_year_highs_sqnorm_low_63d_base_v106_signal(open, low):
    r = _ohlcv_multi_year_highs_scaled(open, low)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized open/low 252d mean
def omyh_f088_ohlcv_multi_year_highs_sqnorm_low_252d_base_v107_signal(open, low):
    r = _ohlcv_multi_year_highs_scaled(open, low)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized open/close 63d mean
def omyh_f088_ohlcv_multi_year_highs_sqnorm_close_63d_base_v108_signal(open, close):
    r = _ohlcv_multi_year_highs_scaled(open, close)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized open/close 252d mean
def omyh_f088_ohlcv_multi_year_highs_sqnorm_close_252d_base_v109_signal(open, close):
    r = _ohlcv_multi_year_highs_scaled(open, close)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_infrat_63d_base_v110_signal(open, closeadj):
    m = _mean(open, 63)
    s = _std(open, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_infrat_252d_base_v111_signal(open, closeadj):
    m = _mean(open, 252)
    s = _std(open, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_infrat_504d_base_v112_signal(open, closeadj):
    m = _mean(open, 504)
    s = _std(open, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of open
def omyh_f088_ohlcv_multi_year_highs_cv_252d_base_v113_signal(open):
    m = _mean(open, 252).abs().replace(0, np.nan)
    s = _std(open, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of open
def omyh_f088_ohlcv_multi_year_highs_cv_504d_base_v114_signal(open):
    m = _mean(open, 504).abs().replace(0, np.nan)
    s = _std(open, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged open times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_5d_base_v115_signal(open, closeadj):
    result = open.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged open times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_21d_base_v116_signal(open, closeadj):
    result = open.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged open times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_63d_base_v117_signal(open, closeadj):
    result = open.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged open times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_252d_base_v118_signal(open, closeadj):
    result = open.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(open) / mean(high) x closeadj
def omyh_f088_ohlcv_multi_year_highs_cumper_high_252d_base_v119_signal(open, high, closeadj):
    s = open.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(high, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(open) / mean(high) x closeadj
def omyh_f088_ohlcv_multi_year_highs_cumper_high_504d_base_v120_signal(open, high, closeadj):
    s = open.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(high, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(open) / mean(low) x closeadj
def omyh_f088_ohlcv_multi_year_highs_cumper_low_252d_base_v121_signal(open, low, closeadj):
    s = open.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(low, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(open) / mean(low) x closeadj
def omyh_f088_ohlcv_multi_year_highs_cumper_low_504d_base_v122_signal(open, low, closeadj):
    s = open.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(low, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only open times closeadj
def omyh_f088_ohlcv_multi_year_highs_pos_63d_base_v123_signal(open, closeadj):
    pos = open.where(open > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only open times closeadj
def omyh_f088_ohlcv_multi_year_highs_pos_252d_base_v124_signal(open, closeadj):
    pos = open.where(open > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only open times closeadj
def omyh_f088_ohlcv_multi_year_highs_neg_63d_base_v125_signal(open, closeadj):
    neg = open.where(open < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only open times closeadj
def omyh_f088_ohlcv_multi_year_highs_neg_252d_base_v126_signal(open, closeadj):
    neg = open.where(open < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_hl_21d_base_v127_signal(open, closeadj):
    result = open.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_hl_63d_base_v128_signal(open, closeadj):
    result = open.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_hl_252d_base_v129_signal(open, closeadj):
    result = open.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of open
def omyh_f088_ohlcv_multi_year_highs_z_63d_base_v130_signal(open):
    result = _z(open, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of open
def omyh_f088_ohlcv_multi_year_highs_z_126d_base_v131_signal(open):
    result = _z(open, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of open
def omyh_f088_ohlcv_multi_year_highs_z_1008d_base_v132_signal(open):
    result = _z(open, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_st_lt_252_21d_base_v133_signal(open, closeadj):
    sm = _mean(open, 21)
    lm = _mean(open, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_st_lt_252_63d_base_v134_signal(open, closeadj):
    sm = _mean(open, 63)
    lm = _mean(open, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_st_lt_504_21d_base_v135_signal(open, closeadj):
    sm = _mean(open, 21)
    lm = _mean(open, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_st_lt_504_63d_base_v136_signal(open, closeadj):
    sm = _mean(open, 63)
    lm = _mean(open, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged open/high times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_per_high_21d_base_v137_signal(open, high, closeadj):
    r = _ohlcv_multi_year_highs_scaled(open, high)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged open/high times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_per_high_63d_base_v138_signal(open, high, closeadj):
    r = _ohlcv_multi_year_highs_scaled(open, high)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged open/high times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_per_high_252d_base_v139_signal(open, high, closeadj):
    r = _ohlcv_multi_year_highs_scaled(open, high)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged open/low times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_per_low_21d_base_v140_signal(open, low, closeadj):
    r = _ohlcv_multi_year_highs_scaled(open, low)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged open/low times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_per_low_63d_base_v141_signal(open, low, closeadj):
    r = _ohlcv_multi_year_highs_scaled(open, low)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged open/low times closeadj
def omyh_f088_ohlcv_multi_year_highs_lag_per_low_252d_base_v142_signal(open, low, closeadj):
    r = _ohlcv_multi_year_highs_scaled(open, low)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |open| times closeadj
def omyh_f088_ohlcv_multi_year_highs_abssum_63d_base_v143_signal(open, closeadj):
    result = open.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |open| times closeadj
def omyh_f088_ohlcv_multi_year_highs_abssum_252d_base_v144_signal(open, closeadj):
    result = open.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |open| times closeadj
def omyh_f088_ohlcv_multi_year_highs_abssum_504d_base_v145_signal(open, closeadj):
    result = open.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of open
def omyh_f088_ohlcv_multi_year_highs_acf1_252d_base_v146_signal(open):
    result = open.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of open
def omyh_f088_ohlcv_multi_year_highs_acf1_504d_base_v147_signal(open):
    result = open.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of open
def omyh_f088_ohlcv_multi_year_highs_posinrange_252d_base_v148_signal(open):
    m = _mean(open, 252)
    hi = open.rolling(252, min_periods=max(1, 252//2)).max()
    lo = open.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of open
def omyh_f088_ohlcv_multi_year_highs_posinrange_504d_base_v149_signal(open):
    m = _mean(open, 504)
    hi = open.rolling(504, min_periods=max(1, 504//2)).max()
    lo = open.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of open times closeadj
def omyh_f088_ohlcv_multi_year_highs_hl_5d_base_v150_signal(open, closeadj):
    result = open.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
