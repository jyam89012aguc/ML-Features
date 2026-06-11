"""Family f95 - SEC 8-K event density & mix  (Q_Actions_Events) | base 076-150"""
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
def _event_density_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _event_density_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _event_density_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of eventcount/marketcap
def ed_f95_event_density_log_per_marketcap_504d_base_v076_signal(eventcount, marketcap):
    s = _event_density_scaled(eventcount, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of eventcount/equity
def ed_f95_event_density_log_per_equity_252d_base_v077_signal(eventcount, equity):
    s = _event_density_scaled(eventcount, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of eventcount/equity
def ed_f95_event_density_log_per_equity_504d_base_v078_signal(eventcount, equity):
    s = _event_density_scaled(eventcount, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of eventcount times closeadj
def ed_f95_event_density_ewm_21d_base_v079_signal(eventcount, closeadj):
    result = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of eventcount times closeadj
def ed_f95_event_density_ewm_63d_base_v080_signal(eventcount, closeadj):
    result = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of eventcount times closeadj
def ed_f95_event_density_ewm_252d_base_v081_signal(eventcount, closeadj):
    result = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of eventcount times closeadj
def ed_f95_event_density_med_63d_base_v082_signal(eventcount, closeadj):
    result = eventcount.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of eventcount times closeadj
def ed_f95_event_density_med_252d_base_v083_signal(eventcount, closeadj):
    result = eventcount.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of eventcount times closeadj
def ed_f95_event_density_med_504d_base_v084_signal(eventcount, closeadj):
    result = eventcount.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of eventcount
def ed_f95_event_density_skew_252d_base_v085_signal(eventcount):
    result = eventcount.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of eventcount
def ed_f95_event_density_skew_504d_base_v086_signal(eventcount):
    result = eventcount.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of eventcount
def ed_f95_event_density_kurt_252d_base_v087_signal(eventcount):
    result = eventcount.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of eventcount
def ed_f95_event_density_kurt_504d_base_v088_signal(eventcount):
    result = eventcount.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of eventcount times closeadj
def ed_f95_event_density_rank_252d_base_v089_signal(eventcount, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = eventcount.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of eventcount times closeadj
def ed_f95_event_density_rank_504d_base_v090_signal(eventcount, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = eventcount.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of eventcount times closeadj
def ed_f95_event_density_rank_1008d_base_v091_signal(eventcount, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = eventcount.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of eventcount from 63d mean times closeadj
def ed_f95_event_density_devmean_63d_base_v092_signal(eventcount, closeadj):
    m = _mean(eventcount, 63)
    result = (eventcount - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of eventcount from 252d mean times closeadj
def ed_f95_event_density_devmean_252d_base_v093_signal(eventcount, closeadj):
    m = _mean(eventcount, 252)
    result = (eventcount - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of eventcount from 504d mean times closeadj
def ed_f95_event_density_devmean_504d_base_v094_signal(eventcount, closeadj):
    m = _mean(eventcount, 504)
    result = (eventcount - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of eventcount times closeadj
def ed_f95_event_density_logdiff_21d_base_v095_signal(eventcount, closeadj):
    lr = _event_density_log(eventcount)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of eventcount times closeadj
def ed_f95_event_density_logdiff_63d_base_v096_signal(eventcount, closeadj):
    lr = _event_density_log(eventcount)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of eventcount times closeadj
def ed_f95_event_density_logdiff_252d_base_v097_signal(eventcount, closeadj):
    lr = _event_density_log(eventcount)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of eventcount times closeadj
def ed_f95_event_density_range_63d_base_v098_signal(eventcount, closeadj):
    hi = eventcount.rolling(63, min_periods=max(1, 63//2)).max()
    lo = eventcount.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of eventcount times closeadj
def ed_f95_event_density_range_252d_base_v099_signal(eventcount, closeadj):
    hi = eventcount.rolling(252, min_periods=max(1, 252//2)).max()
    lo = eventcount.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of eventcount times closeadj
def ed_f95_event_density_range_504d_base_v100_signal(eventcount, closeadj):
    hi = eventcount.rolling(504, min_periods=max(1, 504//2)).max()
    lo = eventcount.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eventcount relative to 252d mean times closeadj
def ed_f95_event_density_rel_252d_base_v101_signal(eventcount, closeadj):
    m = _mean(eventcount, 252).replace(0, np.nan)
    result = (eventcount / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eventcount relative to 504d mean times closeadj
def ed_f95_event_density_rel_504d_base_v102_signal(eventcount, closeadj):
    m = _mean(eventcount, 504).replace(0, np.nan)
    result = (eventcount / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# eventcount relative to 1008d mean times closeadj
def ed_f95_event_density_rel_1008d_base_v103_signal(eventcount, closeadj):
    m = _mean(eventcount, 1008).replace(0, np.nan)
    result = (eventcount / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eventcount/assets 63d mean
def ed_f95_event_density_sqnorm_assets_63d_base_v104_signal(eventcount, assets):
    r = _event_density_scaled(eventcount, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eventcount/assets 252d mean
def ed_f95_event_density_sqnorm_assets_252d_base_v105_signal(eventcount, assets):
    r = _event_density_scaled(eventcount, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eventcount/marketcap 63d mean
def ed_f95_event_density_sqnorm_marketcap_63d_base_v106_signal(eventcount, marketcap):
    r = _event_density_scaled(eventcount, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eventcount/marketcap 252d mean
def ed_f95_event_density_sqnorm_marketcap_252d_base_v107_signal(eventcount, marketcap):
    r = _event_density_scaled(eventcount, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eventcount/equity 63d mean
def ed_f95_event_density_sqnorm_equity_63d_base_v108_signal(eventcount, equity):
    r = _event_density_scaled(eventcount, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized eventcount/equity 252d mean
def ed_f95_event_density_sqnorm_equity_252d_base_v109_signal(eventcount, equity):
    r = _event_density_scaled(eventcount, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of eventcount times closeadj
def ed_f95_event_density_infrat_63d_base_v110_signal(eventcount, closeadj):
    m = _mean(eventcount, 63)
    s = _std(eventcount, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of eventcount times closeadj
def ed_f95_event_density_infrat_252d_base_v111_signal(eventcount, closeadj):
    m = _mean(eventcount, 252)
    s = _std(eventcount, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of eventcount times closeadj
def ed_f95_event_density_infrat_504d_base_v112_signal(eventcount, closeadj):
    m = _mean(eventcount, 504)
    s = _std(eventcount, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of eventcount
def ed_f95_event_density_cv_252d_base_v113_signal(eventcount):
    m = _mean(eventcount, 252).abs().replace(0, np.nan)
    s = _std(eventcount, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of eventcount
def ed_f95_event_density_cv_504d_base_v114_signal(eventcount):
    m = _mean(eventcount, 504).abs().replace(0, np.nan)
    s = _std(eventcount, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged eventcount times closeadj
def ed_f95_event_density_lag_5d_base_v115_signal(eventcount, closeadj):
    result = eventcount.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged eventcount times closeadj
def ed_f95_event_density_lag_21d_base_v116_signal(eventcount, closeadj):
    result = eventcount.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged eventcount times closeadj
def ed_f95_event_density_lag_63d_base_v117_signal(eventcount, closeadj):
    result = eventcount.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged eventcount times closeadj
def ed_f95_event_density_lag_252d_base_v118_signal(eventcount, closeadj):
    result = eventcount.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(eventcount) / mean(assets) x closeadj
def ed_f95_event_density_cumper_assets_252d_base_v119_signal(eventcount, assets, closeadj):
    s = eventcount.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(eventcount) / mean(assets) x closeadj
def ed_f95_event_density_cumper_assets_504d_base_v120_signal(eventcount, assets, closeadj):
    s = eventcount.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(eventcount) / mean(marketcap) x closeadj
def ed_f95_event_density_cumper_marketcap_252d_base_v121_signal(eventcount, marketcap, closeadj):
    s = eventcount.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(eventcount) / mean(marketcap) x closeadj
def ed_f95_event_density_cumper_marketcap_504d_base_v122_signal(eventcount, marketcap, closeadj):
    s = eventcount.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only eventcount times closeadj
def ed_f95_event_density_pos_63d_base_v123_signal(eventcount, closeadj):
    pos = eventcount.where(eventcount > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only eventcount times closeadj
def ed_f95_event_density_pos_252d_base_v124_signal(eventcount, closeadj):
    pos = eventcount.where(eventcount > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only eventcount times closeadj
def ed_f95_event_density_neg_63d_base_v125_signal(eventcount, closeadj):
    neg = eventcount.where(eventcount < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only eventcount times closeadj
def ed_f95_event_density_neg_252d_base_v126_signal(eventcount, closeadj):
    neg = eventcount.where(eventcount < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of eventcount times closeadj
def ed_f95_event_density_hl_21d_base_v127_signal(eventcount, closeadj):
    result = eventcount.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of eventcount times closeadj
def ed_f95_event_density_hl_63d_base_v128_signal(eventcount, closeadj):
    result = eventcount.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of eventcount times closeadj
def ed_f95_event_density_hl_252d_base_v129_signal(eventcount, closeadj):
    result = eventcount.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of eventcount
def ed_f95_event_density_z_63d_base_v130_signal(eventcount):
    result = _z(eventcount, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of eventcount
def ed_f95_event_density_z_126d_base_v131_signal(eventcount):
    result = _z(eventcount, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of eventcount
def ed_f95_event_density_z_1008d_base_v132_signal(eventcount):
    result = _z(eventcount, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of eventcount times closeadj
def ed_f95_event_density_st_lt_252_21d_base_v133_signal(eventcount, closeadj):
    sm = _mean(eventcount, 21)
    lm = _mean(eventcount, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of eventcount times closeadj
def ed_f95_event_density_st_lt_252_63d_base_v134_signal(eventcount, closeadj):
    sm = _mean(eventcount, 63)
    lm = _mean(eventcount, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of eventcount times closeadj
def ed_f95_event_density_st_lt_504_21d_base_v135_signal(eventcount, closeadj):
    sm = _mean(eventcount, 21)
    lm = _mean(eventcount, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of eventcount times closeadj
def ed_f95_event_density_st_lt_504_63d_base_v136_signal(eventcount, closeadj):
    sm = _mean(eventcount, 63)
    lm = _mean(eventcount, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged eventcount/assets times closeadj
def ed_f95_event_density_lag_per_assets_21d_base_v137_signal(eventcount, assets, closeadj):
    r = _event_density_scaled(eventcount, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged eventcount/assets times closeadj
def ed_f95_event_density_lag_per_assets_63d_base_v138_signal(eventcount, assets, closeadj):
    r = _event_density_scaled(eventcount, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged eventcount/assets times closeadj
def ed_f95_event_density_lag_per_assets_252d_base_v139_signal(eventcount, assets, closeadj):
    r = _event_density_scaled(eventcount, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged eventcount/marketcap times closeadj
def ed_f95_event_density_lag_per_marketcap_21d_base_v140_signal(eventcount, marketcap, closeadj):
    r = _event_density_scaled(eventcount, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged eventcount/marketcap times closeadj
def ed_f95_event_density_lag_per_marketcap_63d_base_v141_signal(eventcount, marketcap, closeadj):
    r = _event_density_scaled(eventcount, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged eventcount/marketcap times closeadj
def ed_f95_event_density_lag_per_marketcap_252d_base_v142_signal(eventcount, marketcap, closeadj):
    r = _event_density_scaled(eventcount, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |eventcount| times closeadj
def ed_f95_event_density_abssum_63d_base_v143_signal(eventcount, closeadj):
    result = eventcount.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |eventcount| times closeadj
def ed_f95_event_density_abssum_252d_base_v144_signal(eventcount, closeadj):
    result = eventcount.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |eventcount| times closeadj
def ed_f95_event_density_abssum_504d_base_v145_signal(eventcount, closeadj):
    result = eventcount.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of eventcount
def ed_f95_event_density_acf1_252d_base_v146_signal(eventcount):
    result = eventcount.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of eventcount
def ed_f95_event_density_acf1_504d_base_v147_signal(eventcount):
    result = eventcount.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of eventcount
def ed_f95_event_density_posinrange_252d_base_v148_signal(eventcount):
    m = _mean(eventcount, 252)
    hi = eventcount.rolling(252, min_periods=max(1, 252//2)).max()
    lo = eventcount.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of eventcount
def ed_f95_event_density_posinrange_504d_base_v149_signal(eventcount):
    m = _mean(eventcount, 504)
    hi = eventcount.rolling(504, min_periods=max(1, 504//2)).max()
    lo = eventcount.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of eventcount times closeadj
def ed_f95_event_density_hl_5d_base_v150_signal(eventcount, closeadj):
    result = eventcount.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
