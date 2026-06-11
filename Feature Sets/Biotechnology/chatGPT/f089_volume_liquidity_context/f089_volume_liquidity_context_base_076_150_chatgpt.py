"""Family f089 - Volume and dollar liquidity context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: volume, close, closeadj, sharesbas | base 076-150"""
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
def _volume_liquidity_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _volume_liquidity_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _volume_liquidity_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of volume/closeadj
def vlc_f089_volume_liquidity_context_log_per_closeadj_504d_base_v076_signal(volume, closeadj):
    s = _volume_liquidity_context_scaled(volume, closeadj)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of volume/sharesbas
def vlc_f089_volume_liquidity_context_log_per_sharesbas_252d_base_v077_signal(volume, sharesbas):
    s = _volume_liquidity_context_scaled(volume, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of volume/sharesbas
def vlc_f089_volume_liquidity_context_log_per_sharesbas_504d_base_v078_signal(volume, sharesbas):
    s = _volume_liquidity_context_scaled(volume, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of volume times closeadj
def vlc_f089_volume_liquidity_context_ewm_21d_base_v079_signal(volume, closeadj):
    result = volume.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of volume times closeadj
def vlc_f089_volume_liquidity_context_ewm_63d_base_v080_signal(volume, closeadj):
    result = volume.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of volume times closeadj
def vlc_f089_volume_liquidity_context_ewm_252d_base_v081_signal(volume, closeadj):
    result = volume.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of volume times closeadj
def vlc_f089_volume_liquidity_context_med_63d_base_v082_signal(volume, closeadj):
    result = volume.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of volume times closeadj
def vlc_f089_volume_liquidity_context_med_252d_base_v083_signal(volume, closeadj):
    result = volume.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of volume times closeadj
def vlc_f089_volume_liquidity_context_med_504d_base_v084_signal(volume, closeadj):
    result = volume.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of volume
def vlc_f089_volume_liquidity_context_skew_252d_base_v085_signal(volume):
    result = volume.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of volume
def vlc_f089_volume_liquidity_context_skew_504d_base_v086_signal(volume):
    result = volume.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of volume
def vlc_f089_volume_liquidity_context_kurt_252d_base_v087_signal(volume):
    result = volume.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of volume
def vlc_f089_volume_liquidity_context_kurt_504d_base_v088_signal(volume):
    result = volume.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of volume times closeadj
def vlc_f089_volume_liquidity_context_rank_252d_base_v089_signal(volume, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = volume.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of volume times closeadj
def vlc_f089_volume_liquidity_context_rank_504d_base_v090_signal(volume, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = volume.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of volume times closeadj
def vlc_f089_volume_liquidity_context_rank_1008d_base_v091_signal(volume, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = volume.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of volume from 63d mean times closeadj
def vlc_f089_volume_liquidity_context_devmean_63d_base_v092_signal(volume, closeadj):
    m = _mean(volume, 63)
    result = (volume - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of volume from 252d mean times closeadj
def vlc_f089_volume_liquidity_context_devmean_252d_base_v093_signal(volume, closeadj):
    m = _mean(volume, 252)
    result = (volume - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of volume from 504d mean times closeadj
def vlc_f089_volume_liquidity_context_devmean_504d_base_v094_signal(volume, closeadj):
    m = _mean(volume, 504)
    result = (volume - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of volume times closeadj
def vlc_f089_volume_liquidity_context_logdiff_21d_base_v095_signal(volume, closeadj):
    lr = _volume_liquidity_context_log(volume)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of volume times closeadj
def vlc_f089_volume_liquidity_context_logdiff_63d_base_v096_signal(volume, closeadj):
    lr = _volume_liquidity_context_log(volume)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of volume times closeadj
def vlc_f089_volume_liquidity_context_logdiff_252d_base_v097_signal(volume, closeadj):
    lr = _volume_liquidity_context_log(volume)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of volume times closeadj
def vlc_f089_volume_liquidity_context_range_63d_base_v098_signal(volume, closeadj):
    hi = volume.rolling(63, min_periods=max(1, 63//2)).max()
    lo = volume.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of volume times closeadj
def vlc_f089_volume_liquidity_context_range_252d_base_v099_signal(volume, closeadj):
    hi = volume.rolling(252, min_periods=max(1, 252//2)).max()
    lo = volume.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of volume times closeadj
def vlc_f089_volume_liquidity_context_range_504d_base_v100_signal(volume, closeadj):
    hi = volume.rolling(504, min_periods=max(1, 504//2)).max()
    lo = volume.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 252d mean times closeadj
def vlc_f089_volume_liquidity_context_rel_252d_base_v101_signal(volume, closeadj):
    m = _mean(volume, 252).replace(0, np.nan)
    result = (volume / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 504d mean times closeadj
def vlc_f089_volume_liquidity_context_rel_504d_base_v102_signal(volume, closeadj):
    m = _mean(volume, 504).replace(0, np.nan)
    result = (volume / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# volume relative to 1008d mean times closeadj
def vlc_f089_volume_liquidity_context_rel_1008d_base_v103_signal(volume, closeadj):
    m = _mean(volume, 1008).replace(0, np.nan)
    result = (volume / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized volume/close 63d mean
def vlc_f089_volume_liquidity_context_sqnorm_close_63d_base_v104_signal(volume, close):
    r = _volume_liquidity_context_scaled(volume, close)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized volume/close 252d mean
def vlc_f089_volume_liquidity_context_sqnorm_close_252d_base_v105_signal(volume, close):
    r = _volume_liquidity_context_scaled(volume, close)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized volume/closeadj 63d mean
def vlc_f089_volume_liquidity_context_sqnorm_closeadj_63d_base_v106_signal(volume, closeadj):
    r = _volume_liquidity_context_scaled(volume, closeadj)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized volume/closeadj 252d mean
def vlc_f089_volume_liquidity_context_sqnorm_closeadj_252d_base_v107_signal(volume, closeadj):
    r = _volume_liquidity_context_scaled(volume, closeadj)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized volume/sharesbas 63d mean
def vlc_f089_volume_liquidity_context_sqnorm_sharesbas_63d_base_v108_signal(volume, sharesbas):
    r = _volume_liquidity_context_scaled(volume, sharesbas)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized volume/sharesbas 252d mean
def vlc_f089_volume_liquidity_context_sqnorm_sharesbas_252d_base_v109_signal(volume, sharesbas):
    r = _volume_liquidity_context_scaled(volume, sharesbas)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of volume times closeadj
def vlc_f089_volume_liquidity_context_infrat_63d_base_v110_signal(volume, closeadj):
    m = _mean(volume, 63)
    s = _std(volume, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of volume times closeadj
def vlc_f089_volume_liquidity_context_infrat_252d_base_v111_signal(volume, closeadj):
    m = _mean(volume, 252)
    s = _std(volume, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of volume times closeadj
def vlc_f089_volume_liquidity_context_infrat_504d_base_v112_signal(volume, closeadj):
    m = _mean(volume, 504)
    s = _std(volume, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of volume
def vlc_f089_volume_liquidity_context_cv_252d_base_v113_signal(volume):
    m = _mean(volume, 252).abs().replace(0, np.nan)
    s = _std(volume, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of volume
def vlc_f089_volume_liquidity_context_cv_504d_base_v114_signal(volume):
    m = _mean(volume, 504).abs().replace(0, np.nan)
    s = _std(volume, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged volume times closeadj
def vlc_f089_volume_liquidity_context_lag_5d_base_v115_signal(volume, closeadj):
    result = volume.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged volume times closeadj
def vlc_f089_volume_liquidity_context_lag_21d_base_v116_signal(volume, closeadj):
    result = volume.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged volume times closeadj
def vlc_f089_volume_liquidity_context_lag_63d_base_v117_signal(volume, closeadj):
    result = volume.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged volume times closeadj
def vlc_f089_volume_liquidity_context_lag_252d_base_v118_signal(volume, closeadj):
    result = volume.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(volume) / mean(close) x closeadj
def vlc_f089_volume_liquidity_context_cumper_close_252d_base_v119_signal(volume, close, closeadj):
    s = volume.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(close, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(volume) / mean(close) x closeadj
def vlc_f089_volume_liquidity_context_cumper_close_504d_base_v120_signal(volume, close, closeadj):
    s = volume.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(close, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(volume) / mean(closeadj) x closeadj
def vlc_f089_volume_liquidity_context_cumper_closeadj_252d_base_v121_signal(volume, closeadj):
    s = volume.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(closeadj, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(volume) / mean(closeadj) x closeadj
def vlc_f089_volume_liquidity_context_cumper_closeadj_504d_base_v122_signal(volume, closeadj):
    s = volume.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(closeadj, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only volume times closeadj
def vlc_f089_volume_liquidity_context_pos_63d_base_v123_signal(volume, closeadj):
    pos = volume.where(volume > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only volume times closeadj
def vlc_f089_volume_liquidity_context_pos_252d_base_v124_signal(volume, closeadj):
    pos = volume.where(volume > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only volume times closeadj
def vlc_f089_volume_liquidity_context_neg_63d_base_v125_signal(volume, closeadj):
    neg = volume.where(volume < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only volume times closeadj
def vlc_f089_volume_liquidity_context_neg_252d_base_v126_signal(volume, closeadj):
    neg = volume.where(volume < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of volume times closeadj
def vlc_f089_volume_liquidity_context_hl_21d_base_v127_signal(volume, closeadj):
    result = volume.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of volume times closeadj
def vlc_f089_volume_liquidity_context_hl_63d_base_v128_signal(volume, closeadj):
    result = volume.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of volume times closeadj
def vlc_f089_volume_liquidity_context_hl_252d_base_v129_signal(volume, closeadj):
    result = volume.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of volume
def vlc_f089_volume_liquidity_context_z_63d_base_v130_signal(volume):
    result = _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of volume
def vlc_f089_volume_liquidity_context_z_126d_base_v131_signal(volume):
    result = _z(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of volume
def vlc_f089_volume_liquidity_context_z_1008d_base_v132_signal(volume):
    result = _z(volume, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of volume times closeadj
def vlc_f089_volume_liquidity_context_st_lt_252_21d_base_v133_signal(volume, closeadj):
    sm = _mean(volume, 21)
    lm = _mean(volume, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of volume times closeadj
def vlc_f089_volume_liquidity_context_st_lt_252_63d_base_v134_signal(volume, closeadj):
    sm = _mean(volume, 63)
    lm = _mean(volume, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of volume times closeadj
def vlc_f089_volume_liquidity_context_st_lt_504_21d_base_v135_signal(volume, closeadj):
    sm = _mean(volume, 21)
    lm = _mean(volume, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of volume times closeadj
def vlc_f089_volume_liquidity_context_st_lt_504_63d_base_v136_signal(volume, closeadj):
    sm = _mean(volume, 63)
    lm = _mean(volume, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged volume/close times closeadj
def vlc_f089_volume_liquidity_context_lag_per_close_21d_base_v137_signal(volume, close, closeadj):
    r = _volume_liquidity_context_scaled(volume, close)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged volume/close times closeadj
def vlc_f089_volume_liquidity_context_lag_per_close_63d_base_v138_signal(volume, close, closeadj):
    r = _volume_liquidity_context_scaled(volume, close)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged volume/close times closeadj
def vlc_f089_volume_liquidity_context_lag_per_close_252d_base_v139_signal(volume, close, closeadj):
    r = _volume_liquidity_context_scaled(volume, close)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged volume/closeadj times closeadj
def vlc_f089_volume_liquidity_context_lag_per_closeadj_21d_base_v140_signal(volume, closeadj):
    r = _volume_liquidity_context_scaled(volume, closeadj)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged volume/closeadj times closeadj
def vlc_f089_volume_liquidity_context_lag_per_closeadj_63d_base_v141_signal(volume, closeadj):
    r = _volume_liquidity_context_scaled(volume, closeadj)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged volume/closeadj times closeadj
def vlc_f089_volume_liquidity_context_lag_per_closeadj_252d_base_v142_signal(volume, closeadj):
    r = _volume_liquidity_context_scaled(volume, closeadj)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |volume| times closeadj
def vlc_f089_volume_liquidity_context_abssum_63d_base_v143_signal(volume, closeadj):
    result = volume.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |volume| times closeadj
def vlc_f089_volume_liquidity_context_abssum_252d_base_v144_signal(volume, closeadj):
    result = volume.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |volume| times closeadj
def vlc_f089_volume_liquidity_context_abssum_504d_base_v145_signal(volume, closeadj):
    result = volume.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of volume
def vlc_f089_volume_liquidity_context_acf1_252d_base_v146_signal(volume):
    result = volume.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of volume
def vlc_f089_volume_liquidity_context_acf1_504d_base_v147_signal(volume):
    result = volume.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of volume
def vlc_f089_volume_liquidity_context_posinrange_252d_base_v148_signal(volume):
    m = _mean(volume, 252)
    hi = volume.rolling(252, min_periods=max(1, 252//2)).max()
    lo = volume.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of volume
def vlc_f089_volume_liquidity_context_posinrange_504d_base_v149_signal(volume):
    m = _mean(volume, 504)
    hi = volume.rolling(504, min_periods=max(1, 504//2)).max()
    lo = volume.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of volume times closeadj
def vlc_f089_volume_liquidity_context_hl_5d_base_v150_signal(volume, closeadj):
    result = volume.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
