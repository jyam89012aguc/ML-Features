"""Family f083 - Listing lifecycle and delisting context (Security Master and Universe) | Sharadar tables: TICKERS | fields: isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter | base 076-150"""
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
def _listing_status_and_dates_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _listing_status_and_dates_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _listing_status_and_dates_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of listingage/marketcap
def lsad_f083_listing_status_and_dates_log_per_marketcap_504d_base_v076_signal(listingage, marketcap):
    s = _listing_status_and_dates_scaled(listingage, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of listingage/equity
def lsad_f083_listing_status_and_dates_log_per_equity_252d_base_v077_signal(listingage, equity):
    s = _listing_status_and_dates_scaled(listingage, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of listingage/equity
def lsad_f083_listing_status_and_dates_log_per_equity_504d_base_v078_signal(listingage, equity):
    s = _listing_status_and_dates_scaled(listingage, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of listingage times closeadj
def lsad_f083_listing_status_and_dates_ewm_21d_base_v079_signal(listingage, closeadj):
    result = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of listingage times closeadj
def lsad_f083_listing_status_and_dates_ewm_63d_base_v080_signal(listingage, closeadj):
    result = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of listingage times closeadj
def lsad_f083_listing_status_and_dates_ewm_252d_base_v081_signal(listingage, closeadj):
    result = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of listingage times closeadj
def lsad_f083_listing_status_and_dates_med_63d_base_v082_signal(listingage, closeadj):
    result = listingage.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of listingage times closeadj
def lsad_f083_listing_status_and_dates_med_252d_base_v083_signal(listingage, closeadj):
    result = listingage.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of listingage times closeadj
def lsad_f083_listing_status_and_dates_med_504d_base_v084_signal(listingage, closeadj):
    result = listingage.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of listingage
def lsad_f083_listing_status_and_dates_skew_252d_base_v085_signal(listingage):
    result = listingage.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of listingage
def lsad_f083_listing_status_and_dates_skew_504d_base_v086_signal(listingage):
    result = listingage.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of listingage
def lsad_f083_listing_status_and_dates_kurt_252d_base_v087_signal(listingage):
    result = listingage.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of listingage
def lsad_f083_listing_status_and_dates_kurt_504d_base_v088_signal(listingage):
    result = listingage.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of listingage times closeadj
def lsad_f083_listing_status_and_dates_rank_252d_base_v089_signal(listingage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = listingage.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of listingage times closeadj
def lsad_f083_listing_status_and_dates_rank_504d_base_v090_signal(listingage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = listingage.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of listingage times closeadj
def lsad_f083_listing_status_and_dates_rank_1008d_base_v091_signal(listingage, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = listingage.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of listingage from 63d mean times closeadj
def lsad_f083_listing_status_and_dates_devmean_63d_base_v092_signal(listingage, closeadj):
    m = _mean(listingage, 63)
    result = (listingage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of listingage from 252d mean times closeadj
def lsad_f083_listing_status_and_dates_devmean_252d_base_v093_signal(listingage, closeadj):
    m = _mean(listingage, 252)
    result = (listingage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of listingage from 504d mean times closeadj
def lsad_f083_listing_status_and_dates_devmean_504d_base_v094_signal(listingage, closeadj):
    m = _mean(listingage, 504)
    result = (listingage - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of listingage times closeadj
def lsad_f083_listing_status_and_dates_logdiff_21d_base_v095_signal(listingage, closeadj):
    lr = _listing_status_and_dates_log(listingage)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of listingage times closeadj
def lsad_f083_listing_status_and_dates_logdiff_63d_base_v096_signal(listingage, closeadj):
    lr = _listing_status_and_dates_log(listingage)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of listingage times closeadj
def lsad_f083_listing_status_and_dates_logdiff_252d_base_v097_signal(listingage, closeadj):
    lr = _listing_status_and_dates_log(listingage)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of listingage times closeadj
def lsad_f083_listing_status_and_dates_range_63d_base_v098_signal(listingage, closeadj):
    hi = listingage.rolling(63, min_periods=max(1, 63//2)).max()
    lo = listingage.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of listingage times closeadj
def lsad_f083_listing_status_and_dates_range_252d_base_v099_signal(listingage, closeadj):
    hi = listingage.rolling(252, min_periods=max(1, 252//2)).max()
    lo = listingage.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of listingage times closeadj
def lsad_f083_listing_status_and_dates_range_504d_base_v100_signal(listingage, closeadj):
    hi = listingage.rolling(504, min_periods=max(1, 504//2)).max()
    lo = listingage.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 252d mean times closeadj
def lsad_f083_listing_status_and_dates_rel_252d_base_v101_signal(listingage, closeadj):
    m = _mean(listingage, 252).replace(0, np.nan)
    result = (listingage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 504d mean times closeadj
def lsad_f083_listing_status_and_dates_rel_504d_base_v102_signal(listingage, closeadj):
    m = _mean(listingage, 504).replace(0, np.nan)
    result = (listingage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 1008d mean times closeadj
def lsad_f083_listing_status_and_dates_rel_1008d_base_v103_signal(listingage, closeadj):
    m = _mean(listingage, 1008).replace(0, np.nan)
    result = (listingage / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized listingage/assets 63d mean
def lsad_f083_listing_status_and_dates_sqnorm_assets_63d_base_v104_signal(listingage, assets):
    r = _listing_status_and_dates_scaled(listingage, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized listingage/assets 252d mean
def lsad_f083_listing_status_and_dates_sqnorm_assets_252d_base_v105_signal(listingage, assets):
    r = _listing_status_and_dates_scaled(listingage, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized listingage/marketcap 63d mean
def lsad_f083_listing_status_and_dates_sqnorm_marketcap_63d_base_v106_signal(listingage, marketcap):
    r = _listing_status_and_dates_scaled(listingage, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized listingage/marketcap 252d mean
def lsad_f083_listing_status_and_dates_sqnorm_marketcap_252d_base_v107_signal(listingage, marketcap):
    r = _listing_status_and_dates_scaled(listingage, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized listingage/equity 63d mean
def lsad_f083_listing_status_and_dates_sqnorm_equity_63d_base_v108_signal(listingage, equity):
    r = _listing_status_and_dates_scaled(listingage, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized listingage/equity 252d mean
def lsad_f083_listing_status_and_dates_sqnorm_equity_252d_base_v109_signal(listingage, equity):
    r = _listing_status_and_dates_scaled(listingage, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of listingage times closeadj
def lsad_f083_listing_status_and_dates_infrat_63d_base_v110_signal(listingage, closeadj):
    m = _mean(listingage, 63)
    s = _std(listingage, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of listingage times closeadj
def lsad_f083_listing_status_and_dates_infrat_252d_base_v111_signal(listingage, closeadj):
    m = _mean(listingage, 252)
    s = _std(listingage, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of listingage times closeadj
def lsad_f083_listing_status_and_dates_infrat_504d_base_v112_signal(listingage, closeadj):
    m = _mean(listingage, 504)
    s = _std(listingage, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of listingage
def lsad_f083_listing_status_and_dates_cv_252d_base_v113_signal(listingage):
    m = _mean(listingage, 252).abs().replace(0, np.nan)
    s = _std(listingage, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of listingage
def lsad_f083_listing_status_and_dates_cv_504d_base_v114_signal(listingage):
    m = _mean(listingage, 504).abs().replace(0, np.nan)
    s = _std(listingage, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged listingage times closeadj
def lsad_f083_listing_status_and_dates_lag_5d_base_v115_signal(listingage, closeadj):
    result = listingage.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged listingage times closeadj
def lsad_f083_listing_status_and_dates_lag_21d_base_v116_signal(listingage, closeadj):
    result = listingage.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged listingage times closeadj
def lsad_f083_listing_status_and_dates_lag_63d_base_v117_signal(listingage, closeadj):
    result = listingage.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged listingage times closeadj
def lsad_f083_listing_status_and_dates_lag_252d_base_v118_signal(listingage, closeadj):
    result = listingage.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(listingage) / mean(assets) x closeadj
def lsad_f083_listing_status_and_dates_cumper_assets_252d_base_v119_signal(listingage, assets, closeadj):
    s = listingage.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(listingage) / mean(assets) x closeadj
def lsad_f083_listing_status_and_dates_cumper_assets_504d_base_v120_signal(listingage, assets, closeadj):
    s = listingage.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(listingage) / mean(marketcap) x closeadj
def lsad_f083_listing_status_and_dates_cumper_marketcap_252d_base_v121_signal(listingage, marketcap, closeadj):
    s = listingage.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(listingage) / mean(marketcap) x closeadj
def lsad_f083_listing_status_and_dates_cumper_marketcap_504d_base_v122_signal(listingage, marketcap, closeadj):
    s = listingage.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only listingage times closeadj
def lsad_f083_listing_status_and_dates_pos_63d_base_v123_signal(listingage, closeadj):
    pos = listingage.where(listingage > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only listingage times closeadj
def lsad_f083_listing_status_and_dates_pos_252d_base_v124_signal(listingage, closeadj):
    pos = listingage.where(listingage > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only listingage times closeadj
def lsad_f083_listing_status_and_dates_neg_63d_base_v125_signal(listingage, closeadj):
    neg = listingage.where(listingage < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only listingage times closeadj
def lsad_f083_listing_status_and_dates_neg_252d_base_v126_signal(listingage, closeadj):
    neg = listingage.where(listingage < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of listingage times closeadj
def lsad_f083_listing_status_and_dates_hl_21d_base_v127_signal(listingage, closeadj):
    result = listingage.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of listingage times closeadj
def lsad_f083_listing_status_and_dates_hl_63d_base_v128_signal(listingage, closeadj):
    result = listingage.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of listingage times closeadj
def lsad_f083_listing_status_and_dates_hl_252d_base_v129_signal(listingage, closeadj):
    result = listingage.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of listingage
def lsad_f083_listing_status_and_dates_z_63d_base_v130_signal(listingage):
    result = _z(listingage, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of listingage
def lsad_f083_listing_status_and_dates_z_126d_base_v131_signal(listingage):
    result = _z(listingage, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of listingage
def lsad_f083_listing_status_and_dates_z_1008d_base_v132_signal(listingage):
    result = _z(listingage, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of listingage times closeadj
def lsad_f083_listing_status_and_dates_st_lt_252_21d_base_v133_signal(listingage, closeadj):
    sm = _mean(listingage, 21)
    lm = _mean(listingage, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of listingage times closeadj
def lsad_f083_listing_status_and_dates_st_lt_252_63d_base_v134_signal(listingage, closeadj):
    sm = _mean(listingage, 63)
    lm = _mean(listingage, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of listingage times closeadj
def lsad_f083_listing_status_and_dates_st_lt_504_21d_base_v135_signal(listingage, closeadj):
    sm = _mean(listingage, 21)
    lm = _mean(listingage, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of listingage times closeadj
def lsad_f083_listing_status_and_dates_st_lt_504_63d_base_v136_signal(listingage, closeadj):
    sm = _mean(listingage, 63)
    lm = _mean(listingage, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged listingage/assets times closeadj
def lsad_f083_listing_status_and_dates_lag_per_assets_21d_base_v137_signal(listingage, assets, closeadj):
    r = _listing_status_and_dates_scaled(listingage, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged listingage/assets times closeadj
def lsad_f083_listing_status_and_dates_lag_per_assets_63d_base_v138_signal(listingage, assets, closeadj):
    r = _listing_status_and_dates_scaled(listingage, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged listingage/assets times closeadj
def lsad_f083_listing_status_and_dates_lag_per_assets_252d_base_v139_signal(listingage, assets, closeadj):
    r = _listing_status_and_dates_scaled(listingage, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged listingage/marketcap times closeadj
def lsad_f083_listing_status_and_dates_lag_per_marketcap_21d_base_v140_signal(listingage, marketcap, closeadj):
    r = _listing_status_and_dates_scaled(listingage, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged listingage/marketcap times closeadj
def lsad_f083_listing_status_and_dates_lag_per_marketcap_63d_base_v141_signal(listingage, marketcap, closeadj):
    r = _listing_status_and_dates_scaled(listingage, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged listingage/marketcap times closeadj
def lsad_f083_listing_status_and_dates_lag_per_marketcap_252d_base_v142_signal(listingage, marketcap, closeadj):
    r = _listing_status_and_dates_scaled(listingage, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |listingage| times closeadj
def lsad_f083_listing_status_and_dates_abssum_63d_base_v143_signal(listingage, closeadj):
    result = listingage.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |listingage| times closeadj
def lsad_f083_listing_status_and_dates_abssum_252d_base_v144_signal(listingage, closeadj):
    result = listingage.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |listingage| times closeadj
def lsad_f083_listing_status_and_dates_abssum_504d_base_v145_signal(listingage, closeadj):
    result = listingage.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of listingage
def lsad_f083_listing_status_and_dates_acf1_252d_base_v146_signal(listingage):
    result = listingage.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of listingage
def lsad_f083_listing_status_and_dates_acf1_504d_base_v147_signal(listingage):
    result = listingage.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of listingage
def lsad_f083_listing_status_and_dates_posinrange_252d_base_v148_signal(listingage):
    m = _mean(listingage, 252)
    hi = listingage.rolling(252, min_periods=max(1, 252//2)).max()
    lo = listingage.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of listingage
def lsad_f083_listing_status_and_dates_posinrange_504d_base_v149_signal(listingage):
    m = _mean(listingage, 504)
    hi = listingage.rolling(504, min_periods=max(1, 504//2)).max()
    lo = listingage.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of listingage times closeadj
def lsad_f083_listing_status_and_dates_hl_5d_base_v150_signal(listingage, closeadj):
    result = listingage.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
