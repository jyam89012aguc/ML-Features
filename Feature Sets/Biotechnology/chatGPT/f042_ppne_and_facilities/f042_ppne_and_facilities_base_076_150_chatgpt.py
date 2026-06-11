"""Family f042 - PP&E and facility footprint (Balance Sheet Composition) | Sharadar tables: SF1 | fields: ppnenet, capex, assets | base 076-150"""
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
def _ppne_and_facilities_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ppne_and_facilities_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ppne_and_facilities_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ppnenet/marketcap
def paf_f042_ppne_and_facilities_log_per_marketcap_504d_base_v076_signal(ppnenet, marketcap):
    s = _ppne_and_facilities_scaled(ppnenet, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ppnenet/equity
def paf_f042_ppne_and_facilities_log_per_equity_252d_base_v077_signal(ppnenet, equity):
    s = _ppne_and_facilities_scaled(ppnenet, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ppnenet/equity
def paf_f042_ppne_and_facilities_log_per_equity_504d_base_v078_signal(ppnenet, equity):
    s = _ppne_and_facilities_scaled(ppnenet, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ppnenet times closeadj
def paf_f042_ppne_and_facilities_ewm_21d_base_v079_signal(ppnenet, closeadj):
    result = ppnenet.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ppnenet times closeadj
def paf_f042_ppne_and_facilities_ewm_63d_base_v080_signal(ppnenet, closeadj):
    result = ppnenet.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ppnenet times closeadj
def paf_f042_ppne_and_facilities_ewm_252d_base_v081_signal(ppnenet, closeadj):
    result = ppnenet.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ppnenet times closeadj
def paf_f042_ppne_and_facilities_med_63d_base_v082_signal(ppnenet, closeadj):
    result = ppnenet.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ppnenet times closeadj
def paf_f042_ppne_and_facilities_med_252d_base_v083_signal(ppnenet, closeadj):
    result = ppnenet.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ppnenet times closeadj
def paf_f042_ppne_and_facilities_med_504d_base_v084_signal(ppnenet, closeadj):
    result = ppnenet.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ppnenet
def paf_f042_ppne_and_facilities_skew_252d_base_v085_signal(ppnenet):
    result = ppnenet.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ppnenet
def paf_f042_ppne_and_facilities_skew_504d_base_v086_signal(ppnenet):
    result = ppnenet.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ppnenet
def paf_f042_ppne_and_facilities_kurt_252d_base_v087_signal(ppnenet):
    result = ppnenet.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ppnenet
def paf_f042_ppne_and_facilities_kurt_504d_base_v088_signal(ppnenet):
    result = ppnenet.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ppnenet times closeadj
def paf_f042_ppne_and_facilities_rank_252d_base_v089_signal(ppnenet, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ppnenet.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ppnenet times closeadj
def paf_f042_ppne_and_facilities_rank_504d_base_v090_signal(ppnenet, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ppnenet.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ppnenet times closeadj
def paf_f042_ppne_and_facilities_rank_1008d_base_v091_signal(ppnenet, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ppnenet.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ppnenet from 63d mean times closeadj
def paf_f042_ppne_and_facilities_devmean_63d_base_v092_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 63)
    result = (ppnenet - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ppnenet from 252d mean times closeadj
def paf_f042_ppne_and_facilities_devmean_252d_base_v093_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 252)
    result = (ppnenet - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ppnenet from 504d mean times closeadj
def paf_f042_ppne_and_facilities_devmean_504d_base_v094_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 504)
    result = (ppnenet - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ppnenet times closeadj
def paf_f042_ppne_and_facilities_logdiff_21d_base_v095_signal(ppnenet, closeadj):
    lr = _ppne_and_facilities_log(ppnenet)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ppnenet times closeadj
def paf_f042_ppne_and_facilities_logdiff_63d_base_v096_signal(ppnenet, closeadj):
    lr = _ppne_and_facilities_log(ppnenet)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ppnenet times closeadj
def paf_f042_ppne_and_facilities_logdiff_252d_base_v097_signal(ppnenet, closeadj):
    lr = _ppne_and_facilities_log(ppnenet)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ppnenet times closeadj
def paf_f042_ppne_and_facilities_range_63d_base_v098_signal(ppnenet, closeadj):
    hi = ppnenet.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ppnenet.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ppnenet times closeadj
def paf_f042_ppne_and_facilities_range_252d_base_v099_signal(ppnenet, closeadj):
    hi = ppnenet.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ppnenet.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ppnenet times closeadj
def paf_f042_ppne_and_facilities_range_504d_base_v100_signal(ppnenet, closeadj):
    hi = ppnenet.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ppnenet.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet relative to 252d mean times closeadj
def paf_f042_ppne_and_facilities_rel_252d_base_v101_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 252).replace(0, np.nan)
    result = (ppnenet / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet relative to 504d mean times closeadj
def paf_f042_ppne_and_facilities_rel_504d_base_v102_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 504).replace(0, np.nan)
    result = (ppnenet / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet relative to 1008d mean times closeadj
def paf_f042_ppne_and_facilities_rel_1008d_base_v103_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 1008).replace(0, np.nan)
    result = (ppnenet / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ppnenet/assets 63d mean
def paf_f042_ppne_and_facilities_sqnorm_assets_63d_base_v104_signal(ppnenet, assets):
    r = _ppne_and_facilities_scaled(ppnenet, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ppnenet/assets 252d mean
def paf_f042_ppne_and_facilities_sqnorm_assets_252d_base_v105_signal(ppnenet, assets):
    r = _ppne_and_facilities_scaled(ppnenet, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ppnenet/marketcap 63d mean
def paf_f042_ppne_and_facilities_sqnorm_marketcap_63d_base_v106_signal(ppnenet, marketcap):
    r = _ppne_and_facilities_scaled(ppnenet, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ppnenet/marketcap 252d mean
def paf_f042_ppne_and_facilities_sqnorm_marketcap_252d_base_v107_signal(ppnenet, marketcap):
    r = _ppne_and_facilities_scaled(ppnenet, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ppnenet/equity 63d mean
def paf_f042_ppne_and_facilities_sqnorm_equity_63d_base_v108_signal(ppnenet, equity):
    r = _ppne_and_facilities_scaled(ppnenet, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ppnenet/equity 252d mean
def paf_f042_ppne_and_facilities_sqnorm_equity_252d_base_v109_signal(ppnenet, equity):
    r = _ppne_and_facilities_scaled(ppnenet, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ppnenet times closeadj
def paf_f042_ppne_and_facilities_infrat_63d_base_v110_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 63)
    s = _std(ppnenet, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ppnenet times closeadj
def paf_f042_ppne_and_facilities_infrat_252d_base_v111_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 252)
    s = _std(ppnenet, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ppnenet times closeadj
def paf_f042_ppne_and_facilities_infrat_504d_base_v112_signal(ppnenet, closeadj):
    m = _mean(ppnenet, 504)
    s = _std(ppnenet, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ppnenet
def paf_f042_ppne_and_facilities_cv_252d_base_v113_signal(ppnenet):
    m = _mean(ppnenet, 252).abs().replace(0, np.nan)
    s = _std(ppnenet, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ppnenet
def paf_f042_ppne_and_facilities_cv_504d_base_v114_signal(ppnenet):
    m = _mean(ppnenet, 504).abs().replace(0, np.nan)
    s = _std(ppnenet, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ppnenet times closeadj
def paf_f042_ppne_and_facilities_lag_5d_base_v115_signal(ppnenet, closeadj):
    result = ppnenet.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ppnenet times closeadj
def paf_f042_ppne_and_facilities_lag_21d_base_v116_signal(ppnenet, closeadj):
    result = ppnenet.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ppnenet times closeadj
def paf_f042_ppne_and_facilities_lag_63d_base_v117_signal(ppnenet, closeadj):
    result = ppnenet.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ppnenet times closeadj
def paf_f042_ppne_and_facilities_lag_252d_base_v118_signal(ppnenet, closeadj):
    result = ppnenet.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ppnenet) / mean(assets) x closeadj
def paf_f042_ppne_and_facilities_cumper_assets_252d_base_v119_signal(ppnenet, assets, closeadj):
    s = ppnenet.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ppnenet) / mean(assets) x closeadj
def paf_f042_ppne_and_facilities_cumper_assets_504d_base_v120_signal(ppnenet, assets, closeadj):
    s = ppnenet.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ppnenet) / mean(marketcap) x closeadj
def paf_f042_ppne_and_facilities_cumper_marketcap_252d_base_v121_signal(ppnenet, marketcap, closeadj):
    s = ppnenet.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ppnenet) / mean(marketcap) x closeadj
def paf_f042_ppne_and_facilities_cumper_marketcap_504d_base_v122_signal(ppnenet, marketcap, closeadj):
    s = ppnenet.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ppnenet times closeadj
def paf_f042_ppne_and_facilities_pos_63d_base_v123_signal(ppnenet, closeadj):
    pos = ppnenet.where(ppnenet > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ppnenet times closeadj
def paf_f042_ppne_and_facilities_pos_252d_base_v124_signal(ppnenet, closeadj):
    pos = ppnenet.where(ppnenet > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ppnenet times closeadj
def paf_f042_ppne_and_facilities_neg_63d_base_v125_signal(ppnenet, closeadj):
    neg = ppnenet.where(ppnenet < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ppnenet times closeadj
def paf_f042_ppne_and_facilities_neg_252d_base_v126_signal(ppnenet, closeadj):
    neg = ppnenet.where(ppnenet < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ppnenet times closeadj
def paf_f042_ppne_and_facilities_hl_21d_base_v127_signal(ppnenet, closeadj):
    result = ppnenet.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ppnenet times closeadj
def paf_f042_ppne_and_facilities_hl_63d_base_v128_signal(ppnenet, closeadj):
    result = ppnenet.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ppnenet times closeadj
def paf_f042_ppne_and_facilities_hl_252d_base_v129_signal(ppnenet, closeadj):
    result = ppnenet.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ppnenet
def paf_f042_ppne_and_facilities_z_63d_base_v130_signal(ppnenet):
    result = _z(ppnenet, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ppnenet
def paf_f042_ppne_and_facilities_z_126d_base_v131_signal(ppnenet):
    result = _z(ppnenet, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ppnenet
def paf_f042_ppne_and_facilities_z_1008d_base_v132_signal(ppnenet):
    result = _z(ppnenet, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ppnenet times closeadj
def paf_f042_ppne_and_facilities_st_lt_252_21d_base_v133_signal(ppnenet, closeadj):
    sm = _mean(ppnenet, 21)
    lm = _mean(ppnenet, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ppnenet times closeadj
def paf_f042_ppne_and_facilities_st_lt_252_63d_base_v134_signal(ppnenet, closeadj):
    sm = _mean(ppnenet, 63)
    lm = _mean(ppnenet, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ppnenet times closeadj
def paf_f042_ppne_and_facilities_st_lt_504_21d_base_v135_signal(ppnenet, closeadj):
    sm = _mean(ppnenet, 21)
    lm = _mean(ppnenet, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ppnenet times closeadj
def paf_f042_ppne_and_facilities_st_lt_504_63d_base_v136_signal(ppnenet, closeadj):
    sm = _mean(ppnenet, 63)
    lm = _mean(ppnenet, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ppnenet/assets times closeadj
def paf_f042_ppne_and_facilities_lag_per_assets_21d_base_v137_signal(ppnenet, assets, closeadj):
    r = _ppne_and_facilities_scaled(ppnenet, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ppnenet/assets times closeadj
def paf_f042_ppne_and_facilities_lag_per_assets_63d_base_v138_signal(ppnenet, assets, closeadj):
    r = _ppne_and_facilities_scaled(ppnenet, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ppnenet/assets times closeadj
def paf_f042_ppne_and_facilities_lag_per_assets_252d_base_v139_signal(ppnenet, assets, closeadj):
    r = _ppne_and_facilities_scaled(ppnenet, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ppnenet/marketcap times closeadj
def paf_f042_ppne_and_facilities_lag_per_marketcap_21d_base_v140_signal(ppnenet, marketcap, closeadj):
    r = _ppne_and_facilities_scaled(ppnenet, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ppnenet/marketcap times closeadj
def paf_f042_ppne_and_facilities_lag_per_marketcap_63d_base_v141_signal(ppnenet, marketcap, closeadj):
    r = _ppne_and_facilities_scaled(ppnenet, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ppnenet/marketcap times closeadj
def paf_f042_ppne_and_facilities_lag_per_marketcap_252d_base_v142_signal(ppnenet, marketcap, closeadj):
    r = _ppne_and_facilities_scaled(ppnenet, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ppnenet| times closeadj
def paf_f042_ppne_and_facilities_abssum_63d_base_v143_signal(ppnenet, closeadj):
    result = ppnenet.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ppnenet| times closeadj
def paf_f042_ppne_and_facilities_abssum_252d_base_v144_signal(ppnenet, closeadj):
    result = ppnenet.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ppnenet| times closeadj
def paf_f042_ppne_and_facilities_abssum_504d_base_v145_signal(ppnenet, closeadj):
    result = ppnenet.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ppnenet
def paf_f042_ppne_and_facilities_acf1_252d_base_v146_signal(ppnenet):
    result = ppnenet.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ppnenet
def paf_f042_ppne_and_facilities_acf1_504d_base_v147_signal(ppnenet):
    result = ppnenet.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ppnenet
def paf_f042_ppne_and_facilities_posinrange_252d_base_v148_signal(ppnenet):
    m = _mean(ppnenet, 252)
    hi = ppnenet.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ppnenet.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ppnenet
def paf_f042_ppne_and_facilities_posinrange_504d_base_v149_signal(ppnenet):
    m = _mean(ppnenet, 504)
    hi = ppnenet.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ppnenet.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ppnenet times closeadj
def paf_f042_ppne_and_facilities_hl_5d_base_v150_signal(ppnenet, closeadj):
    result = ppnenet.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
