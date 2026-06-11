"""Family f082 - Sector and industry biotech filter (Security Master and Universe) | Sharadar tables: TICKERS | fields: sector, industry, sicsector, sicindustry, famasector, famaindustry | base 076-150"""
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
def _sector_industry_biotech_filter_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sector_industry_biotech_filter_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sector_industry_biotech_filter_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sector_rank/marketcap
def sibf_f082_sector_industry_biotech_filter_log_per_marketcap_504d_base_v076_signal(sector_rank, marketcap):
    s = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sector_rank/equity
def sibf_f082_sector_industry_biotech_filter_log_per_equity_252d_base_v077_signal(sector_rank, equity):
    s = _sector_industry_biotech_filter_scaled(sector_rank, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sector_rank/equity
def sibf_f082_sector_industry_biotech_filter_log_per_equity_504d_base_v078_signal(sector_rank, equity):
    s = _sector_industry_biotech_filter_scaled(sector_rank, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_ewm_21d_base_v079_signal(sector_rank, closeadj):
    result = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_ewm_63d_base_v080_signal(sector_rank, closeadj):
    result = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_ewm_252d_base_v081_signal(sector_rank, closeadj):
    result = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_med_63d_base_v082_signal(sector_rank, closeadj):
    result = sector_rank.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_med_252d_base_v083_signal(sector_rank, closeadj):
    result = sector_rank.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_med_504d_base_v084_signal(sector_rank, closeadj):
    result = sector_rank.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sector_rank
def sibf_f082_sector_industry_biotech_filter_skew_252d_base_v085_signal(sector_rank):
    result = sector_rank.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sector_rank
def sibf_f082_sector_industry_biotech_filter_skew_504d_base_v086_signal(sector_rank):
    result = sector_rank.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sector_rank
def sibf_f082_sector_industry_biotech_filter_kurt_252d_base_v087_signal(sector_rank):
    result = sector_rank.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sector_rank
def sibf_f082_sector_industry_biotech_filter_kurt_504d_base_v088_signal(sector_rank):
    result = sector_rank.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_rank_252d_base_v089_signal(sector_rank, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sector_rank.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_rank_504d_base_v090_signal(sector_rank, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sector_rank.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_rank_1008d_base_v091_signal(sector_rank, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sector_rank.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sector_rank from 63d mean times closeadj
def sibf_f082_sector_industry_biotech_filter_devmean_63d_base_v092_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 63)
    result = (sector_rank - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sector_rank from 252d mean times closeadj
def sibf_f082_sector_industry_biotech_filter_devmean_252d_base_v093_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 252)
    result = (sector_rank - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sector_rank from 504d mean times closeadj
def sibf_f082_sector_industry_biotech_filter_devmean_504d_base_v094_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 504)
    result = (sector_rank - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_logdiff_21d_base_v095_signal(sector_rank, closeadj):
    lr = _sector_industry_biotech_filter_log(sector_rank)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_logdiff_63d_base_v096_signal(sector_rank, closeadj):
    lr = _sector_industry_biotech_filter_log(sector_rank)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_logdiff_252d_base_v097_signal(sector_rank, closeadj):
    lr = _sector_industry_biotech_filter_log(sector_rank)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_range_63d_base_v098_signal(sector_rank, closeadj):
    hi = sector_rank.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sector_rank.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_range_252d_base_v099_signal(sector_rank, closeadj):
    hi = sector_rank.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sector_rank.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_range_504d_base_v100_signal(sector_rank, closeadj):
    hi = sector_rank.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sector_rank.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 252d mean times closeadj
def sibf_f082_sector_industry_biotech_filter_rel_252d_base_v101_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 252).replace(0, np.nan)
    result = (sector_rank / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 504d mean times closeadj
def sibf_f082_sector_industry_biotech_filter_rel_504d_base_v102_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 504).replace(0, np.nan)
    result = (sector_rank / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sector_rank relative to 1008d mean times closeadj
def sibf_f082_sector_industry_biotech_filter_rel_1008d_base_v103_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 1008).replace(0, np.nan)
    result = (sector_rank / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sector_rank/assets 63d mean
def sibf_f082_sector_industry_biotech_filter_sqnorm_assets_63d_base_v104_signal(sector_rank, assets):
    r = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sector_rank/assets 252d mean
def sibf_f082_sector_industry_biotech_filter_sqnorm_assets_252d_base_v105_signal(sector_rank, assets):
    r = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sector_rank/marketcap 63d mean
def sibf_f082_sector_industry_biotech_filter_sqnorm_marketcap_63d_base_v106_signal(sector_rank, marketcap):
    r = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sector_rank/marketcap 252d mean
def sibf_f082_sector_industry_biotech_filter_sqnorm_marketcap_252d_base_v107_signal(sector_rank, marketcap):
    r = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sector_rank/equity 63d mean
def sibf_f082_sector_industry_biotech_filter_sqnorm_equity_63d_base_v108_signal(sector_rank, equity):
    r = _sector_industry_biotech_filter_scaled(sector_rank, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sector_rank/equity 252d mean
def sibf_f082_sector_industry_biotech_filter_sqnorm_equity_252d_base_v109_signal(sector_rank, equity):
    r = _sector_industry_biotech_filter_scaled(sector_rank, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_infrat_63d_base_v110_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 63)
    s = _std(sector_rank, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_infrat_252d_base_v111_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 252)
    s = _std(sector_rank, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_infrat_504d_base_v112_signal(sector_rank, closeadj):
    m = _mean(sector_rank, 504)
    s = _std(sector_rank, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sector_rank
def sibf_f082_sector_industry_biotech_filter_cv_252d_base_v113_signal(sector_rank):
    m = _mean(sector_rank, 252).abs().replace(0, np.nan)
    s = _std(sector_rank, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sector_rank
def sibf_f082_sector_industry_biotech_filter_cv_504d_base_v114_signal(sector_rank):
    m = _mean(sector_rank, 504).abs().replace(0, np.nan)
    s = _std(sector_rank, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_5d_base_v115_signal(sector_rank, closeadj):
    result = sector_rank.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_21d_base_v116_signal(sector_rank, closeadj):
    result = sector_rank.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_63d_base_v117_signal(sector_rank, closeadj):
    result = sector_rank.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_252d_base_v118_signal(sector_rank, closeadj):
    result = sector_rank.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sector_rank) / mean(assets) x closeadj
def sibf_f082_sector_industry_biotech_filter_cumper_assets_252d_base_v119_signal(sector_rank, assets, closeadj):
    s = sector_rank.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sector_rank) / mean(assets) x closeadj
def sibf_f082_sector_industry_biotech_filter_cumper_assets_504d_base_v120_signal(sector_rank, assets, closeadj):
    s = sector_rank.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sector_rank) / mean(marketcap) x closeadj
def sibf_f082_sector_industry_biotech_filter_cumper_marketcap_252d_base_v121_signal(sector_rank, marketcap, closeadj):
    s = sector_rank.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sector_rank) / mean(marketcap) x closeadj
def sibf_f082_sector_industry_biotech_filter_cumper_marketcap_504d_base_v122_signal(sector_rank, marketcap, closeadj):
    s = sector_rank.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_pos_63d_base_v123_signal(sector_rank, closeadj):
    pos = sector_rank.where(sector_rank > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_pos_252d_base_v124_signal(sector_rank, closeadj):
    pos = sector_rank.where(sector_rank > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_neg_63d_base_v125_signal(sector_rank, closeadj):
    neg = sector_rank.where(sector_rank < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_neg_252d_base_v126_signal(sector_rank, closeadj):
    neg = sector_rank.where(sector_rank < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_hl_21d_base_v127_signal(sector_rank, closeadj):
    result = sector_rank.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_hl_63d_base_v128_signal(sector_rank, closeadj):
    result = sector_rank.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_hl_252d_base_v129_signal(sector_rank, closeadj):
    result = sector_rank.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_base_v130_signal(sector_rank):
    result = _z(sector_rank, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_base_v131_signal(sector_rank):
    result = _z(sector_rank, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sector_rank
def sibf_f082_sector_industry_biotech_filter_z_1008d_base_v132_signal(sector_rank):
    result = _z(sector_rank, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_st_lt_252_21d_base_v133_signal(sector_rank, closeadj):
    sm = _mean(sector_rank, 21)
    lm = _mean(sector_rank, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_st_lt_252_63d_base_v134_signal(sector_rank, closeadj):
    sm = _mean(sector_rank, 63)
    lm = _mean(sector_rank, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_st_lt_504_21d_base_v135_signal(sector_rank, closeadj):
    sm = _mean(sector_rank, 21)
    lm = _mean(sector_rank, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_st_lt_504_63d_base_v136_signal(sector_rank, closeadj):
    sm = _mean(sector_rank, 63)
    lm = _mean(sector_rank, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sector_rank/assets times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_per_assets_21d_base_v137_signal(sector_rank, assets, closeadj):
    r = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sector_rank/assets times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_per_assets_63d_base_v138_signal(sector_rank, assets, closeadj):
    r = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sector_rank/assets times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_per_assets_252d_base_v139_signal(sector_rank, assets, closeadj):
    r = _sector_industry_biotech_filter_scaled(sector_rank, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sector_rank/marketcap times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_per_marketcap_21d_base_v140_signal(sector_rank, marketcap, closeadj):
    r = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sector_rank/marketcap times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_per_marketcap_63d_base_v141_signal(sector_rank, marketcap, closeadj):
    r = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sector_rank/marketcap times closeadj
def sibf_f082_sector_industry_biotech_filter_lag_per_marketcap_252d_base_v142_signal(sector_rank, marketcap, closeadj):
    r = _sector_industry_biotech_filter_scaled(sector_rank, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sector_rank| times closeadj
def sibf_f082_sector_industry_biotech_filter_abssum_63d_base_v143_signal(sector_rank, closeadj):
    result = sector_rank.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sector_rank| times closeadj
def sibf_f082_sector_industry_biotech_filter_abssum_252d_base_v144_signal(sector_rank, closeadj):
    result = sector_rank.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sector_rank| times closeadj
def sibf_f082_sector_industry_biotech_filter_abssum_504d_base_v145_signal(sector_rank, closeadj):
    result = sector_rank.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sector_rank
def sibf_f082_sector_industry_biotech_filter_acf1_252d_base_v146_signal(sector_rank):
    result = sector_rank.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sector_rank
def sibf_f082_sector_industry_biotech_filter_acf1_504d_base_v147_signal(sector_rank):
    result = sector_rank.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sector_rank
def sibf_f082_sector_industry_biotech_filter_posinrange_252d_base_v148_signal(sector_rank):
    m = _mean(sector_rank, 252)
    hi = sector_rank.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sector_rank.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sector_rank
def sibf_f082_sector_industry_biotech_filter_posinrange_504d_base_v149_signal(sector_rank):
    m = _mean(sector_rank, 504)
    hi = sector_rank.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sector_rank.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sector_rank times closeadj
def sibf_f082_sector_industry_biotech_filter_hl_5d_base_v150_signal(sector_rank, closeadj):
    result = sector_rank.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
