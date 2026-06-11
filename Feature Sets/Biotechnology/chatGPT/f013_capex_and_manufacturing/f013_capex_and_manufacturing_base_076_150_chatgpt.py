"""Family f013 - Capex and manufacturing buildout (Cash Flow and Burn) | Sharadar tables: SF1 | fields: capex, ppnenet, assets, revenue | base 076-150"""
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
def _capex_and_manufacturing_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capex_and_manufacturing_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capex_and_manufacturing_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of capex/assets
def cam_f013_capex_and_manufacturing_log_per_assets_504d_base_v076_signal(capex, assets):
    s = _capex_and_manufacturing_scaled(capex, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of capex/revenue
def cam_f013_capex_and_manufacturing_log_per_revenue_252d_base_v077_signal(capex, revenue):
    s = _capex_and_manufacturing_scaled(capex, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of capex/revenue
def cam_f013_capex_and_manufacturing_log_per_revenue_504d_base_v078_signal(capex, revenue):
    s = _capex_and_manufacturing_scaled(capex, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of capex times closeadj
def cam_f013_capex_and_manufacturing_ewm_21d_base_v079_signal(capex, closeadj):
    result = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of capex times closeadj
def cam_f013_capex_and_manufacturing_ewm_63d_base_v080_signal(capex, closeadj):
    result = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of capex times closeadj
def cam_f013_capex_and_manufacturing_ewm_252d_base_v081_signal(capex, closeadj):
    result = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of capex times closeadj
def cam_f013_capex_and_manufacturing_med_63d_base_v082_signal(capex, closeadj):
    result = capex.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of capex times closeadj
def cam_f013_capex_and_manufacturing_med_252d_base_v083_signal(capex, closeadj):
    result = capex.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of capex times closeadj
def cam_f013_capex_and_manufacturing_med_504d_base_v084_signal(capex, closeadj):
    result = capex.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of capex
def cam_f013_capex_and_manufacturing_skew_252d_base_v085_signal(capex):
    result = capex.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of capex
def cam_f013_capex_and_manufacturing_skew_504d_base_v086_signal(capex):
    result = capex.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of capex
def cam_f013_capex_and_manufacturing_kurt_252d_base_v087_signal(capex):
    result = capex.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of capex
def cam_f013_capex_and_manufacturing_kurt_504d_base_v088_signal(capex):
    result = capex.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of capex times closeadj
def cam_f013_capex_and_manufacturing_rank_252d_base_v089_signal(capex, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = capex.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of capex times closeadj
def cam_f013_capex_and_manufacturing_rank_504d_base_v090_signal(capex, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = capex.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of capex times closeadj
def cam_f013_capex_and_manufacturing_rank_1008d_base_v091_signal(capex, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = capex.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of capex from 63d mean times closeadj
def cam_f013_capex_and_manufacturing_devmean_63d_base_v092_signal(capex, closeadj):
    m = _mean(capex, 63)
    result = (capex - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of capex from 252d mean times closeadj
def cam_f013_capex_and_manufacturing_devmean_252d_base_v093_signal(capex, closeadj):
    m = _mean(capex, 252)
    result = (capex - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of capex from 504d mean times closeadj
def cam_f013_capex_and_manufacturing_devmean_504d_base_v094_signal(capex, closeadj):
    m = _mean(capex, 504)
    result = (capex - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of capex times closeadj
def cam_f013_capex_and_manufacturing_logdiff_21d_base_v095_signal(capex, closeadj):
    lr = _capex_and_manufacturing_log(capex)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of capex times closeadj
def cam_f013_capex_and_manufacturing_logdiff_63d_base_v096_signal(capex, closeadj):
    lr = _capex_and_manufacturing_log(capex)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of capex times closeadj
def cam_f013_capex_and_manufacturing_logdiff_252d_base_v097_signal(capex, closeadj):
    lr = _capex_and_manufacturing_log(capex)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of capex times closeadj
def cam_f013_capex_and_manufacturing_range_63d_base_v098_signal(capex, closeadj):
    hi = capex.rolling(63, min_periods=max(1, 63//2)).max()
    lo = capex.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of capex times closeadj
def cam_f013_capex_and_manufacturing_range_252d_base_v099_signal(capex, closeadj):
    hi = capex.rolling(252, min_periods=max(1, 252//2)).max()
    lo = capex.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of capex times closeadj
def cam_f013_capex_and_manufacturing_range_504d_base_v100_signal(capex, closeadj):
    hi = capex.rolling(504, min_periods=max(1, 504//2)).max()
    lo = capex.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 252d mean times closeadj
def cam_f013_capex_and_manufacturing_rel_252d_base_v101_signal(capex, closeadj):
    m = _mean(capex, 252).replace(0, np.nan)
    result = (capex / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 504d mean times closeadj
def cam_f013_capex_and_manufacturing_rel_504d_base_v102_signal(capex, closeadj):
    m = _mean(capex, 504).replace(0, np.nan)
    result = (capex / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 1008d mean times closeadj
def cam_f013_capex_and_manufacturing_rel_1008d_base_v103_signal(capex, closeadj):
    m = _mean(capex, 1008).replace(0, np.nan)
    result = (capex / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized capex/ppnenet 63d mean
def cam_f013_capex_and_manufacturing_sqnorm_ppnenet_63d_base_v104_signal(capex, ppnenet):
    r = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized capex/ppnenet 252d mean
def cam_f013_capex_and_manufacturing_sqnorm_ppnenet_252d_base_v105_signal(capex, ppnenet):
    r = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized capex/assets 63d mean
def cam_f013_capex_and_manufacturing_sqnorm_assets_63d_base_v106_signal(capex, assets):
    r = _capex_and_manufacturing_scaled(capex, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized capex/assets 252d mean
def cam_f013_capex_and_manufacturing_sqnorm_assets_252d_base_v107_signal(capex, assets):
    r = _capex_and_manufacturing_scaled(capex, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized capex/revenue 63d mean
def cam_f013_capex_and_manufacturing_sqnorm_revenue_63d_base_v108_signal(capex, revenue):
    r = _capex_and_manufacturing_scaled(capex, revenue)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized capex/revenue 252d mean
def cam_f013_capex_and_manufacturing_sqnorm_revenue_252d_base_v109_signal(capex, revenue):
    r = _capex_and_manufacturing_scaled(capex, revenue)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of capex times closeadj
def cam_f013_capex_and_manufacturing_infrat_63d_base_v110_signal(capex, closeadj):
    m = _mean(capex, 63)
    s = _std(capex, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of capex times closeadj
def cam_f013_capex_and_manufacturing_infrat_252d_base_v111_signal(capex, closeadj):
    m = _mean(capex, 252)
    s = _std(capex, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of capex times closeadj
def cam_f013_capex_and_manufacturing_infrat_504d_base_v112_signal(capex, closeadj):
    m = _mean(capex, 504)
    s = _std(capex, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of capex
def cam_f013_capex_and_manufacturing_cv_252d_base_v113_signal(capex):
    m = _mean(capex, 252).abs().replace(0, np.nan)
    s = _std(capex, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of capex
def cam_f013_capex_and_manufacturing_cv_504d_base_v114_signal(capex):
    m = _mean(capex, 504).abs().replace(0, np.nan)
    s = _std(capex, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged capex times closeadj
def cam_f013_capex_and_manufacturing_lag_5d_base_v115_signal(capex, closeadj):
    result = capex.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged capex times closeadj
def cam_f013_capex_and_manufacturing_lag_21d_base_v116_signal(capex, closeadj):
    result = capex.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged capex times closeadj
def cam_f013_capex_and_manufacturing_lag_63d_base_v117_signal(capex, closeadj):
    result = capex.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged capex times closeadj
def cam_f013_capex_and_manufacturing_lag_252d_base_v118_signal(capex, closeadj):
    result = capex.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(capex) / mean(ppnenet) x closeadj
def cam_f013_capex_and_manufacturing_cumper_ppnenet_252d_base_v119_signal(capex, ppnenet, closeadj):
    s = capex.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ppnenet, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(capex) / mean(ppnenet) x closeadj
def cam_f013_capex_and_manufacturing_cumper_ppnenet_504d_base_v120_signal(capex, ppnenet, closeadj):
    s = capex.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ppnenet, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(capex) / mean(assets) x closeadj
def cam_f013_capex_and_manufacturing_cumper_assets_252d_base_v121_signal(capex, assets, closeadj):
    s = capex.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(capex) / mean(assets) x closeadj
def cam_f013_capex_and_manufacturing_cumper_assets_504d_base_v122_signal(capex, assets, closeadj):
    s = capex.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only capex times closeadj
def cam_f013_capex_and_manufacturing_pos_63d_base_v123_signal(capex, closeadj):
    pos = capex.where(capex > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only capex times closeadj
def cam_f013_capex_and_manufacturing_pos_252d_base_v124_signal(capex, closeadj):
    pos = capex.where(capex > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only capex times closeadj
def cam_f013_capex_and_manufacturing_neg_63d_base_v125_signal(capex, closeadj):
    neg = capex.where(capex < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only capex times closeadj
def cam_f013_capex_and_manufacturing_neg_252d_base_v126_signal(capex, closeadj):
    neg = capex.where(capex < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of capex times closeadj
def cam_f013_capex_and_manufacturing_hl_21d_base_v127_signal(capex, closeadj):
    result = capex.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of capex times closeadj
def cam_f013_capex_and_manufacturing_hl_63d_base_v128_signal(capex, closeadj):
    result = capex.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of capex times closeadj
def cam_f013_capex_and_manufacturing_hl_252d_base_v129_signal(capex, closeadj):
    result = capex.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of capex
def cam_f013_capex_and_manufacturing_z_63d_base_v130_signal(capex):
    result = _z(capex, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of capex
def cam_f013_capex_and_manufacturing_z_126d_base_v131_signal(capex):
    result = _z(capex, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of capex
def cam_f013_capex_and_manufacturing_z_1008d_base_v132_signal(capex):
    result = _z(capex, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of capex times closeadj
def cam_f013_capex_and_manufacturing_st_lt_252_21d_base_v133_signal(capex, closeadj):
    sm = _mean(capex, 21)
    lm = _mean(capex, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of capex times closeadj
def cam_f013_capex_and_manufacturing_st_lt_252_63d_base_v134_signal(capex, closeadj):
    sm = _mean(capex, 63)
    lm = _mean(capex, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of capex times closeadj
def cam_f013_capex_and_manufacturing_st_lt_504_21d_base_v135_signal(capex, closeadj):
    sm = _mean(capex, 21)
    lm = _mean(capex, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of capex times closeadj
def cam_f013_capex_and_manufacturing_st_lt_504_63d_base_v136_signal(capex, closeadj):
    sm = _mean(capex, 63)
    lm = _mean(capex, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged capex/ppnenet times closeadj
def cam_f013_capex_and_manufacturing_lag_per_ppnenet_21d_base_v137_signal(capex, ppnenet, closeadj):
    r = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged capex/ppnenet times closeadj
def cam_f013_capex_and_manufacturing_lag_per_ppnenet_63d_base_v138_signal(capex, ppnenet, closeadj):
    r = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged capex/ppnenet times closeadj
def cam_f013_capex_and_manufacturing_lag_per_ppnenet_252d_base_v139_signal(capex, ppnenet, closeadj):
    r = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged capex/assets times closeadj
def cam_f013_capex_and_manufacturing_lag_per_assets_21d_base_v140_signal(capex, assets, closeadj):
    r = _capex_and_manufacturing_scaled(capex, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged capex/assets times closeadj
def cam_f013_capex_and_manufacturing_lag_per_assets_63d_base_v141_signal(capex, assets, closeadj):
    r = _capex_and_manufacturing_scaled(capex, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged capex/assets times closeadj
def cam_f013_capex_and_manufacturing_lag_per_assets_252d_base_v142_signal(capex, assets, closeadj):
    r = _capex_and_manufacturing_scaled(capex, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |capex| times closeadj
def cam_f013_capex_and_manufacturing_abssum_63d_base_v143_signal(capex, closeadj):
    result = capex.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |capex| times closeadj
def cam_f013_capex_and_manufacturing_abssum_252d_base_v144_signal(capex, closeadj):
    result = capex.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |capex| times closeadj
def cam_f013_capex_and_manufacturing_abssum_504d_base_v145_signal(capex, closeadj):
    result = capex.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of capex
def cam_f013_capex_and_manufacturing_acf1_252d_base_v146_signal(capex):
    result = capex.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of capex
def cam_f013_capex_and_manufacturing_acf1_504d_base_v147_signal(capex):
    result = capex.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of capex
def cam_f013_capex_and_manufacturing_posinrange_252d_base_v148_signal(capex):
    m = _mean(capex, 252)
    hi = capex.rolling(252, min_periods=max(1, 252//2)).max()
    lo = capex.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of capex
def cam_f013_capex_and_manufacturing_posinrange_504d_base_v149_signal(capex):
    m = _mean(capex, 504)
    hi = capex.rolling(504, min_periods=max(1, 504//2)).max()
    lo = capex.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of capex times closeadj
def cam_f013_capex_and_manufacturing_hl_5d_base_v150_signal(capex, closeadj):
    result = capex.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
