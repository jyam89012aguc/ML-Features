"""Family f19 - SG&A vs R&D mix  (C_RnD_Innovation) | base 076-150"""
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
def _sga_vs_rnd_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sga_vs_rnd_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sga_vs_rnd_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sgna/marketcap
def svr_f19_sga_vs_rnd_log_per_marketcap_504d_base_v076_signal(sgna, marketcap):
    s = _sga_vs_rnd_scaled(sgna, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sgna/equity
def svr_f19_sga_vs_rnd_log_per_equity_252d_base_v077_signal(sgna, equity):
    s = _sga_vs_rnd_scaled(sgna, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sgna/equity
def svr_f19_sga_vs_rnd_log_per_equity_504d_base_v078_signal(sgna, equity):
    s = _sga_vs_rnd_scaled(sgna, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sgna times closeadj
def svr_f19_sga_vs_rnd_ewm_21d_base_v079_signal(sgna, closeadj):
    result = sgna.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sgna times closeadj
def svr_f19_sga_vs_rnd_ewm_63d_base_v080_signal(sgna, closeadj):
    result = sgna.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sgna times closeadj
def svr_f19_sga_vs_rnd_ewm_252d_base_v081_signal(sgna, closeadj):
    result = sgna.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sgna times closeadj
def svr_f19_sga_vs_rnd_med_63d_base_v082_signal(sgna, closeadj):
    result = sgna.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sgna times closeadj
def svr_f19_sga_vs_rnd_med_252d_base_v083_signal(sgna, closeadj):
    result = sgna.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sgna times closeadj
def svr_f19_sga_vs_rnd_med_504d_base_v084_signal(sgna, closeadj):
    result = sgna.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sgna
def svr_f19_sga_vs_rnd_skew_252d_base_v085_signal(sgna):
    result = sgna.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sgna
def svr_f19_sga_vs_rnd_skew_504d_base_v086_signal(sgna):
    result = sgna.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sgna
def svr_f19_sga_vs_rnd_kurt_252d_base_v087_signal(sgna):
    result = sgna.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sgna
def svr_f19_sga_vs_rnd_kurt_504d_base_v088_signal(sgna):
    result = sgna.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sgna times closeadj
def svr_f19_sga_vs_rnd_rank_252d_base_v089_signal(sgna, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sgna.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sgna times closeadj
def svr_f19_sga_vs_rnd_rank_504d_base_v090_signal(sgna, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sgna.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sgna times closeadj
def svr_f19_sga_vs_rnd_rank_1008d_base_v091_signal(sgna, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sgna.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sgna from 63d mean times closeadj
def svr_f19_sga_vs_rnd_devmean_63d_base_v092_signal(sgna, closeadj):
    m = _mean(sgna, 63)
    result = (sgna - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sgna from 252d mean times closeadj
def svr_f19_sga_vs_rnd_devmean_252d_base_v093_signal(sgna, closeadj):
    m = _mean(sgna, 252)
    result = (sgna - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sgna from 504d mean times closeadj
def svr_f19_sga_vs_rnd_devmean_504d_base_v094_signal(sgna, closeadj):
    m = _mean(sgna, 504)
    result = (sgna - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sgna times closeadj
def svr_f19_sga_vs_rnd_logdiff_21d_base_v095_signal(sgna, closeadj):
    lr = _sga_vs_rnd_log(sgna)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sgna times closeadj
def svr_f19_sga_vs_rnd_logdiff_63d_base_v096_signal(sgna, closeadj):
    lr = _sga_vs_rnd_log(sgna)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sgna times closeadj
def svr_f19_sga_vs_rnd_logdiff_252d_base_v097_signal(sgna, closeadj):
    lr = _sga_vs_rnd_log(sgna)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sgna times closeadj
def svr_f19_sga_vs_rnd_range_63d_base_v098_signal(sgna, closeadj):
    hi = sgna.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sgna.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sgna times closeadj
def svr_f19_sga_vs_rnd_range_252d_base_v099_signal(sgna, closeadj):
    hi = sgna.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sgna.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sgna times closeadj
def svr_f19_sga_vs_rnd_range_504d_base_v100_signal(sgna, closeadj):
    hi = sgna.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sgna.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 252d mean times closeadj
def svr_f19_sga_vs_rnd_rel_252d_base_v101_signal(sgna, closeadj):
    m = _mean(sgna, 252).replace(0, np.nan)
    result = (sgna / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 504d mean times closeadj
def svr_f19_sga_vs_rnd_rel_504d_base_v102_signal(sgna, closeadj):
    m = _mean(sgna, 504).replace(0, np.nan)
    result = (sgna / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sgna relative to 1008d mean times closeadj
def svr_f19_sga_vs_rnd_rel_1008d_base_v103_signal(sgna, closeadj):
    m = _mean(sgna, 1008).replace(0, np.nan)
    result = (sgna / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sgna/assets 63d mean
def svr_f19_sga_vs_rnd_sqnorm_assets_63d_base_v104_signal(sgna, assets):
    r = _sga_vs_rnd_scaled(sgna, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sgna/assets 252d mean
def svr_f19_sga_vs_rnd_sqnorm_assets_252d_base_v105_signal(sgna, assets):
    r = _sga_vs_rnd_scaled(sgna, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sgna/marketcap 63d mean
def svr_f19_sga_vs_rnd_sqnorm_marketcap_63d_base_v106_signal(sgna, marketcap):
    r = _sga_vs_rnd_scaled(sgna, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sgna/marketcap 252d mean
def svr_f19_sga_vs_rnd_sqnorm_marketcap_252d_base_v107_signal(sgna, marketcap):
    r = _sga_vs_rnd_scaled(sgna, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sgna/equity 63d mean
def svr_f19_sga_vs_rnd_sqnorm_equity_63d_base_v108_signal(sgna, equity):
    r = _sga_vs_rnd_scaled(sgna, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sgna/equity 252d mean
def svr_f19_sga_vs_rnd_sqnorm_equity_252d_base_v109_signal(sgna, equity):
    r = _sga_vs_rnd_scaled(sgna, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sgna times closeadj
def svr_f19_sga_vs_rnd_infrat_63d_base_v110_signal(sgna, closeadj):
    m = _mean(sgna, 63)
    s = _std(sgna, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sgna times closeadj
def svr_f19_sga_vs_rnd_infrat_252d_base_v111_signal(sgna, closeadj):
    m = _mean(sgna, 252)
    s = _std(sgna, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sgna times closeadj
def svr_f19_sga_vs_rnd_infrat_504d_base_v112_signal(sgna, closeadj):
    m = _mean(sgna, 504)
    s = _std(sgna, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sgna
def svr_f19_sga_vs_rnd_cv_252d_base_v113_signal(sgna):
    m = _mean(sgna, 252).abs().replace(0, np.nan)
    s = _std(sgna, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sgna
def svr_f19_sga_vs_rnd_cv_504d_base_v114_signal(sgna):
    m = _mean(sgna, 504).abs().replace(0, np.nan)
    s = _std(sgna, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sgna times closeadj
def svr_f19_sga_vs_rnd_lag_5d_base_v115_signal(sgna, closeadj):
    result = sgna.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sgna times closeadj
def svr_f19_sga_vs_rnd_lag_21d_base_v116_signal(sgna, closeadj):
    result = sgna.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sgna times closeadj
def svr_f19_sga_vs_rnd_lag_63d_base_v117_signal(sgna, closeadj):
    result = sgna.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sgna times closeadj
def svr_f19_sga_vs_rnd_lag_252d_base_v118_signal(sgna, closeadj):
    result = sgna.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sgna) / mean(assets) x closeadj
def svr_f19_sga_vs_rnd_cumper_assets_252d_base_v119_signal(sgna, assets, closeadj):
    s = sgna.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sgna) / mean(assets) x closeadj
def svr_f19_sga_vs_rnd_cumper_assets_504d_base_v120_signal(sgna, assets, closeadj):
    s = sgna.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sgna) / mean(marketcap) x closeadj
def svr_f19_sga_vs_rnd_cumper_marketcap_252d_base_v121_signal(sgna, marketcap, closeadj):
    s = sgna.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sgna) / mean(marketcap) x closeadj
def svr_f19_sga_vs_rnd_cumper_marketcap_504d_base_v122_signal(sgna, marketcap, closeadj):
    s = sgna.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sgna times closeadj
def svr_f19_sga_vs_rnd_pos_63d_base_v123_signal(sgna, closeadj):
    pos = sgna.where(sgna > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sgna times closeadj
def svr_f19_sga_vs_rnd_pos_252d_base_v124_signal(sgna, closeadj):
    pos = sgna.where(sgna > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sgna times closeadj
def svr_f19_sga_vs_rnd_neg_63d_base_v125_signal(sgna, closeadj):
    neg = sgna.where(sgna < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sgna times closeadj
def svr_f19_sga_vs_rnd_neg_252d_base_v126_signal(sgna, closeadj):
    neg = sgna.where(sgna < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sgna times closeadj
def svr_f19_sga_vs_rnd_hl_21d_base_v127_signal(sgna, closeadj):
    result = sgna.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sgna times closeadj
def svr_f19_sga_vs_rnd_hl_63d_base_v128_signal(sgna, closeadj):
    result = sgna.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sgna times closeadj
def svr_f19_sga_vs_rnd_hl_252d_base_v129_signal(sgna, closeadj):
    result = sgna.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sgna
def svr_f19_sga_vs_rnd_z_63d_base_v130_signal(sgna):
    result = _z(sgna, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sgna
def svr_f19_sga_vs_rnd_z_126d_base_v131_signal(sgna):
    result = _z(sgna, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sgna
def svr_f19_sga_vs_rnd_z_1008d_base_v132_signal(sgna):
    result = _z(sgna, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sgna times closeadj
def svr_f19_sga_vs_rnd_st_lt_252_21d_base_v133_signal(sgna, closeadj):
    sm = _mean(sgna, 21)
    lm = _mean(sgna, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sgna times closeadj
def svr_f19_sga_vs_rnd_st_lt_252_63d_base_v134_signal(sgna, closeadj):
    sm = _mean(sgna, 63)
    lm = _mean(sgna, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sgna times closeadj
def svr_f19_sga_vs_rnd_st_lt_504_21d_base_v135_signal(sgna, closeadj):
    sm = _mean(sgna, 21)
    lm = _mean(sgna, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sgna times closeadj
def svr_f19_sga_vs_rnd_st_lt_504_63d_base_v136_signal(sgna, closeadj):
    sm = _mean(sgna, 63)
    lm = _mean(sgna, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sgna/assets times closeadj
def svr_f19_sga_vs_rnd_lag_per_assets_21d_base_v137_signal(sgna, assets, closeadj):
    r = _sga_vs_rnd_scaled(sgna, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sgna/assets times closeadj
def svr_f19_sga_vs_rnd_lag_per_assets_63d_base_v138_signal(sgna, assets, closeadj):
    r = _sga_vs_rnd_scaled(sgna, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sgna/assets times closeadj
def svr_f19_sga_vs_rnd_lag_per_assets_252d_base_v139_signal(sgna, assets, closeadj):
    r = _sga_vs_rnd_scaled(sgna, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sgna/marketcap times closeadj
def svr_f19_sga_vs_rnd_lag_per_marketcap_21d_base_v140_signal(sgna, marketcap, closeadj):
    r = _sga_vs_rnd_scaled(sgna, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sgna/marketcap times closeadj
def svr_f19_sga_vs_rnd_lag_per_marketcap_63d_base_v141_signal(sgna, marketcap, closeadj):
    r = _sga_vs_rnd_scaled(sgna, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sgna/marketcap times closeadj
def svr_f19_sga_vs_rnd_lag_per_marketcap_252d_base_v142_signal(sgna, marketcap, closeadj):
    r = _sga_vs_rnd_scaled(sgna, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sgna| times closeadj
def svr_f19_sga_vs_rnd_abssum_63d_base_v143_signal(sgna, closeadj):
    result = sgna.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sgna| times closeadj
def svr_f19_sga_vs_rnd_abssum_252d_base_v144_signal(sgna, closeadj):
    result = sgna.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sgna| times closeadj
def svr_f19_sga_vs_rnd_abssum_504d_base_v145_signal(sgna, closeadj):
    result = sgna.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sgna
def svr_f19_sga_vs_rnd_acf1_252d_base_v146_signal(sgna):
    result = sgna.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sgna
def svr_f19_sga_vs_rnd_acf1_504d_base_v147_signal(sgna):
    result = sgna.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sgna
def svr_f19_sga_vs_rnd_posinrange_252d_base_v148_signal(sgna):
    m = _mean(sgna, 252)
    hi = sgna.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sgna.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sgna
def svr_f19_sga_vs_rnd_posinrange_504d_base_v149_signal(sgna):
    m = _mean(sgna, 504)
    hi = sgna.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sgna.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sgna times closeadj
def svr_f19_sga_vs_rnd_hl_5d_base_v150_signal(sgna, closeadj):
    result = sgna.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
