"""Family f31 - Stock-based compensation level  (E_Dilution_Shares) | base 076-150"""
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
def _sbc_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sbc_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sbc_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sbcomp/marketcap
def sbl_f31_sbc_level_log_per_marketcap_504d_base_v076_signal(sbcomp, marketcap):
    s = _sbc_level_scaled(sbcomp, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sbcomp/equity
def sbl_f31_sbc_level_log_per_equity_252d_base_v077_signal(sbcomp, equity):
    s = _sbc_level_scaled(sbcomp, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sbcomp/equity
def sbl_f31_sbc_level_log_per_equity_504d_base_v078_signal(sbcomp, equity):
    s = _sbc_level_scaled(sbcomp, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sbcomp times closeadj
def sbl_f31_sbc_level_ewm_21d_base_v079_signal(sbcomp, closeadj):
    result = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sbcomp times closeadj
def sbl_f31_sbc_level_ewm_63d_base_v080_signal(sbcomp, closeadj):
    result = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sbcomp times closeadj
def sbl_f31_sbc_level_ewm_252d_base_v081_signal(sbcomp, closeadj):
    result = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sbcomp times closeadj
def sbl_f31_sbc_level_med_63d_base_v082_signal(sbcomp, closeadj):
    result = sbcomp.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sbcomp times closeadj
def sbl_f31_sbc_level_med_252d_base_v083_signal(sbcomp, closeadj):
    result = sbcomp.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sbcomp times closeadj
def sbl_f31_sbc_level_med_504d_base_v084_signal(sbcomp, closeadj):
    result = sbcomp.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sbcomp
def sbl_f31_sbc_level_skew_252d_base_v085_signal(sbcomp):
    result = sbcomp.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sbcomp
def sbl_f31_sbc_level_skew_504d_base_v086_signal(sbcomp):
    result = sbcomp.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sbcomp
def sbl_f31_sbc_level_kurt_252d_base_v087_signal(sbcomp):
    result = sbcomp.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sbcomp
def sbl_f31_sbc_level_kurt_504d_base_v088_signal(sbcomp):
    result = sbcomp.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sbcomp times closeadj
def sbl_f31_sbc_level_rank_252d_base_v089_signal(sbcomp, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sbcomp.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sbcomp times closeadj
def sbl_f31_sbc_level_rank_504d_base_v090_signal(sbcomp, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sbcomp.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sbcomp times closeadj
def sbl_f31_sbc_level_rank_1008d_base_v091_signal(sbcomp, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sbcomp.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sbcomp from 63d mean times closeadj
def sbl_f31_sbc_level_devmean_63d_base_v092_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 63)
    result = (sbcomp - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sbcomp from 252d mean times closeadj
def sbl_f31_sbc_level_devmean_252d_base_v093_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 252)
    result = (sbcomp - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sbcomp from 504d mean times closeadj
def sbl_f31_sbc_level_devmean_504d_base_v094_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 504)
    result = (sbcomp - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sbcomp times closeadj
def sbl_f31_sbc_level_logdiff_21d_base_v095_signal(sbcomp, closeadj):
    lr = _sbc_level_log(sbcomp)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sbcomp times closeadj
def sbl_f31_sbc_level_logdiff_63d_base_v096_signal(sbcomp, closeadj):
    lr = _sbc_level_log(sbcomp)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sbcomp times closeadj
def sbl_f31_sbc_level_logdiff_252d_base_v097_signal(sbcomp, closeadj):
    lr = _sbc_level_log(sbcomp)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sbcomp times closeadj
def sbl_f31_sbc_level_range_63d_base_v098_signal(sbcomp, closeadj):
    hi = sbcomp.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sbcomp.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sbcomp times closeadj
def sbl_f31_sbc_level_range_252d_base_v099_signal(sbcomp, closeadj):
    hi = sbcomp.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sbcomp.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sbcomp times closeadj
def sbl_f31_sbc_level_range_504d_base_v100_signal(sbcomp, closeadj):
    hi = sbcomp.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sbcomp.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 252d mean times closeadj
def sbl_f31_sbc_level_rel_252d_base_v101_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 252).replace(0, np.nan)
    result = (sbcomp / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 504d mean times closeadj
def sbl_f31_sbc_level_rel_504d_base_v102_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 504).replace(0, np.nan)
    result = (sbcomp / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 1008d mean times closeadj
def sbl_f31_sbc_level_rel_1008d_base_v103_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 1008).replace(0, np.nan)
    result = (sbcomp / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sbcomp/assets 63d mean
def sbl_f31_sbc_level_sqnorm_assets_63d_base_v104_signal(sbcomp, assets):
    r = _sbc_level_scaled(sbcomp, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sbcomp/assets 252d mean
def sbl_f31_sbc_level_sqnorm_assets_252d_base_v105_signal(sbcomp, assets):
    r = _sbc_level_scaled(sbcomp, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sbcomp/marketcap 63d mean
def sbl_f31_sbc_level_sqnorm_marketcap_63d_base_v106_signal(sbcomp, marketcap):
    r = _sbc_level_scaled(sbcomp, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sbcomp/marketcap 252d mean
def sbl_f31_sbc_level_sqnorm_marketcap_252d_base_v107_signal(sbcomp, marketcap):
    r = _sbc_level_scaled(sbcomp, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sbcomp/equity 63d mean
def sbl_f31_sbc_level_sqnorm_equity_63d_base_v108_signal(sbcomp, equity):
    r = _sbc_level_scaled(sbcomp, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sbcomp/equity 252d mean
def sbl_f31_sbc_level_sqnorm_equity_252d_base_v109_signal(sbcomp, equity):
    r = _sbc_level_scaled(sbcomp, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sbcomp times closeadj
def sbl_f31_sbc_level_infrat_63d_base_v110_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 63)
    s = _std(sbcomp, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sbcomp times closeadj
def sbl_f31_sbc_level_infrat_252d_base_v111_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 252)
    s = _std(sbcomp, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sbcomp times closeadj
def sbl_f31_sbc_level_infrat_504d_base_v112_signal(sbcomp, closeadj):
    m = _mean(sbcomp, 504)
    s = _std(sbcomp, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sbcomp
def sbl_f31_sbc_level_cv_252d_base_v113_signal(sbcomp):
    m = _mean(sbcomp, 252).abs().replace(0, np.nan)
    s = _std(sbcomp, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sbcomp
def sbl_f31_sbc_level_cv_504d_base_v114_signal(sbcomp):
    m = _mean(sbcomp, 504).abs().replace(0, np.nan)
    s = _std(sbcomp, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sbcomp times closeadj
def sbl_f31_sbc_level_lag_5d_base_v115_signal(sbcomp, closeadj):
    result = sbcomp.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sbcomp times closeadj
def sbl_f31_sbc_level_lag_21d_base_v116_signal(sbcomp, closeadj):
    result = sbcomp.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sbcomp times closeadj
def sbl_f31_sbc_level_lag_63d_base_v117_signal(sbcomp, closeadj):
    result = sbcomp.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sbcomp times closeadj
def sbl_f31_sbc_level_lag_252d_base_v118_signal(sbcomp, closeadj):
    result = sbcomp.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sbcomp) / mean(assets) x closeadj
def sbl_f31_sbc_level_cumper_assets_252d_base_v119_signal(sbcomp, assets, closeadj):
    s = sbcomp.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sbcomp) / mean(assets) x closeadj
def sbl_f31_sbc_level_cumper_assets_504d_base_v120_signal(sbcomp, assets, closeadj):
    s = sbcomp.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sbcomp) / mean(marketcap) x closeadj
def sbl_f31_sbc_level_cumper_marketcap_252d_base_v121_signal(sbcomp, marketcap, closeadj):
    s = sbcomp.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sbcomp) / mean(marketcap) x closeadj
def sbl_f31_sbc_level_cumper_marketcap_504d_base_v122_signal(sbcomp, marketcap, closeadj):
    s = sbcomp.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sbcomp times closeadj
def sbl_f31_sbc_level_pos_63d_base_v123_signal(sbcomp, closeadj):
    pos = sbcomp.where(sbcomp > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sbcomp times closeadj
def sbl_f31_sbc_level_pos_252d_base_v124_signal(sbcomp, closeadj):
    pos = sbcomp.where(sbcomp > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sbcomp times closeadj
def sbl_f31_sbc_level_neg_63d_base_v125_signal(sbcomp, closeadj):
    neg = sbcomp.where(sbcomp < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sbcomp times closeadj
def sbl_f31_sbc_level_neg_252d_base_v126_signal(sbcomp, closeadj):
    neg = sbcomp.where(sbcomp < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sbcomp times closeadj
def sbl_f31_sbc_level_hl_21d_base_v127_signal(sbcomp, closeadj):
    result = sbcomp.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sbcomp times closeadj
def sbl_f31_sbc_level_hl_63d_base_v128_signal(sbcomp, closeadj):
    result = sbcomp.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sbcomp times closeadj
def sbl_f31_sbc_level_hl_252d_base_v129_signal(sbcomp, closeadj):
    result = sbcomp.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sbcomp
def sbl_f31_sbc_level_z_63d_base_v130_signal(sbcomp):
    result = _z(sbcomp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sbcomp
def sbl_f31_sbc_level_z_126d_base_v131_signal(sbcomp):
    result = _z(sbcomp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sbcomp
def sbl_f31_sbc_level_z_1008d_base_v132_signal(sbcomp):
    result = _z(sbcomp, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sbcomp times closeadj
def sbl_f31_sbc_level_st_lt_252_21d_base_v133_signal(sbcomp, closeadj):
    sm = _mean(sbcomp, 21)
    lm = _mean(sbcomp, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sbcomp times closeadj
def sbl_f31_sbc_level_st_lt_252_63d_base_v134_signal(sbcomp, closeadj):
    sm = _mean(sbcomp, 63)
    lm = _mean(sbcomp, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sbcomp times closeadj
def sbl_f31_sbc_level_st_lt_504_21d_base_v135_signal(sbcomp, closeadj):
    sm = _mean(sbcomp, 21)
    lm = _mean(sbcomp, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sbcomp times closeadj
def sbl_f31_sbc_level_st_lt_504_63d_base_v136_signal(sbcomp, closeadj):
    sm = _mean(sbcomp, 63)
    lm = _mean(sbcomp, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sbcomp/assets times closeadj
def sbl_f31_sbc_level_lag_per_assets_21d_base_v137_signal(sbcomp, assets, closeadj):
    r = _sbc_level_scaled(sbcomp, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sbcomp/assets times closeadj
def sbl_f31_sbc_level_lag_per_assets_63d_base_v138_signal(sbcomp, assets, closeadj):
    r = _sbc_level_scaled(sbcomp, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sbcomp/assets times closeadj
def sbl_f31_sbc_level_lag_per_assets_252d_base_v139_signal(sbcomp, assets, closeadj):
    r = _sbc_level_scaled(sbcomp, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sbcomp/marketcap times closeadj
def sbl_f31_sbc_level_lag_per_marketcap_21d_base_v140_signal(sbcomp, marketcap, closeadj):
    r = _sbc_level_scaled(sbcomp, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sbcomp/marketcap times closeadj
def sbl_f31_sbc_level_lag_per_marketcap_63d_base_v141_signal(sbcomp, marketcap, closeadj):
    r = _sbc_level_scaled(sbcomp, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sbcomp/marketcap times closeadj
def sbl_f31_sbc_level_lag_per_marketcap_252d_base_v142_signal(sbcomp, marketcap, closeadj):
    r = _sbc_level_scaled(sbcomp, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sbcomp| times closeadj
def sbl_f31_sbc_level_abssum_63d_base_v143_signal(sbcomp, closeadj):
    result = sbcomp.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sbcomp| times closeadj
def sbl_f31_sbc_level_abssum_252d_base_v144_signal(sbcomp, closeadj):
    result = sbcomp.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sbcomp| times closeadj
def sbl_f31_sbc_level_abssum_504d_base_v145_signal(sbcomp, closeadj):
    result = sbcomp.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sbcomp
def sbl_f31_sbc_level_acf1_252d_base_v146_signal(sbcomp):
    result = sbcomp.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sbcomp
def sbl_f31_sbc_level_acf1_504d_base_v147_signal(sbcomp):
    result = sbcomp.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sbcomp
def sbl_f31_sbc_level_posinrange_252d_base_v148_signal(sbcomp):
    m = _mean(sbcomp, 252)
    hi = sbcomp.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sbcomp.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sbcomp
def sbl_f31_sbc_level_posinrange_504d_base_v149_signal(sbcomp):
    m = _mean(sbcomp, 504)
    hi = sbcomp.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sbcomp.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sbcomp times closeadj
def sbl_f31_sbc_level_hl_5d_base_v150_signal(sbcomp, closeadj):
    result = sbcomp.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
