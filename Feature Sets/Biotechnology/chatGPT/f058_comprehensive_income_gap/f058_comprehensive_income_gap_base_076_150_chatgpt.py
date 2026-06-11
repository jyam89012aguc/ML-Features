"""Family f058 - Comprehensive income versus net income (Earnings and Quality) | Sharadar tables: SF1 | fields: consolinc, netinc, equity | base 076-150"""
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
def _comprehensive_income_gap_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _comprehensive_income_gap_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _comprehensive_income_gap_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of consolinc/equity
def cig_f058_comprehensive_income_gap_log_per_equity_504d_base_v076_signal(consolinc, equity):
    s = _comprehensive_income_gap_scaled(consolinc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of consolinc/assets
def cig_f058_comprehensive_income_gap_log_per_assets_252d_base_v077_signal(consolinc, assets):
    s = _comprehensive_income_gap_scaled(consolinc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of consolinc/assets
def cig_f058_comprehensive_income_gap_log_per_assets_504d_base_v078_signal(consolinc, assets):
    s = _comprehensive_income_gap_scaled(consolinc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of consolinc times closeadj
def cig_f058_comprehensive_income_gap_ewm_21d_base_v079_signal(consolinc, closeadj):
    result = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of consolinc times closeadj
def cig_f058_comprehensive_income_gap_ewm_63d_base_v080_signal(consolinc, closeadj):
    result = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of consolinc times closeadj
def cig_f058_comprehensive_income_gap_ewm_252d_base_v081_signal(consolinc, closeadj):
    result = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of consolinc times closeadj
def cig_f058_comprehensive_income_gap_med_63d_base_v082_signal(consolinc, closeadj):
    result = consolinc.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of consolinc times closeadj
def cig_f058_comprehensive_income_gap_med_252d_base_v083_signal(consolinc, closeadj):
    result = consolinc.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of consolinc times closeadj
def cig_f058_comprehensive_income_gap_med_504d_base_v084_signal(consolinc, closeadj):
    result = consolinc.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of consolinc
def cig_f058_comprehensive_income_gap_skew_252d_base_v085_signal(consolinc):
    result = consolinc.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of consolinc
def cig_f058_comprehensive_income_gap_skew_504d_base_v086_signal(consolinc):
    result = consolinc.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of consolinc
def cig_f058_comprehensive_income_gap_kurt_252d_base_v087_signal(consolinc):
    result = consolinc.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of consolinc
def cig_f058_comprehensive_income_gap_kurt_504d_base_v088_signal(consolinc):
    result = consolinc.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of consolinc times closeadj
def cig_f058_comprehensive_income_gap_rank_252d_base_v089_signal(consolinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = consolinc.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of consolinc times closeadj
def cig_f058_comprehensive_income_gap_rank_504d_base_v090_signal(consolinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = consolinc.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of consolinc times closeadj
def cig_f058_comprehensive_income_gap_rank_1008d_base_v091_signal(consolinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = consolinc.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of consolinc from 63d mean times closeadj
def cig_f058_comprehensive_income_gap_devmean_63d_base_v092_signal(consolinc, closeadj):
    m = _mean(consolinc, 63)
    result = (consolinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of consolinc from 252d mean times closeadj
def cig_f058_comprehensive_income_gap_devmean_252d_base_v093_signal(consolinc, closeadj):
    m = _mean(consolinc, 252)
    result = (consolinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of consolinc from 504d mean times closeadj
def cig_f058_comprehensive_income_gap_devmean_504d_base_v094_signal(consolinc, closeadj):
    m = _mean(consolinc, 504)
    result = (consolinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of consolinc times closeadj
def cig_f058_comprehensive_income_gap_logdiff_21d_base_v095_signal(consolinc, closeadj):
    lr = _comprehensive_income_gap_log(consolinc)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of consolinc times closeadj
def cig_f058_comprehensive_income_gap_logdiff_63d_base_v096_signal(consolinc, closeadj):
    lr = _comprehensive_income_gap_log(consolinc)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of consolinc times closeadj
def cig_f058_comprehensive_income_gap_logdiff_252d_base_v097_signal(consolinc, closeadj):
    lr = _comprehensive_income_gap_log(consolinc)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of consolinc times closeadj
def cig_f058_comprehensive_income_gap_range_63d_base_v098_signal(consolinc, closeadj):
    hi = consolinc.rolling(63, min_periods=max(1, 63//2)).max()
    lo = consolinc.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of consolinc times closeadj
def cig_f058_comprehensive_income_gap_range_252d_base_v099_signal(consolinc, closeadj):
    hi = consolinc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = consolinc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of consolinc times closeadj
def cig_f058_comprehensive_income_gap_range_504d_base_v100_signal(consolinc, closeadj):
    hi = consolinc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = consolinc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 252d mean times closeadj
def cig_f058_comprehensive_income_gap_rel_252d_base_v101_signal(consolinc, closeadj):
    m = _mean(consolinc, 252).replace(0, np.nan)
    result = (consolinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 504d mean times closeadj
def cig_f058_comprehensive_income_gap_rel_504d_base_v102_signal(consolinc, closeadj):
    m = _mean(consolinc, 504).replace(0, np.nan)
    result = (consolinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 1008d mean times closeadj
def cig_f058_comprehensive_income_gap_rel_1008d_base_v103_signal(consolinc, closeadj):
    m = _mean(consolinc, 1008).replace(0, np.nan)
    result = (consolinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized consolinc/netinc 63d mean
def cig_f058_comprehensive_income_gap_sqnorm_netinc_63d_base_v104_signal(consolinc, netinc):
    r = _comprehensive_income_gap_scaled(consolinc, netinc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized consolinc/netinc 252d mean
def cig_f058_comprehensive_income_gap_sqnorm_netinc_252d_base_v105_signal(consolinc, netinc):
    r = _comprehensive_income_gap_scaled(consolinc, netinc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized consolinc/equity 63d mean
def cig_f058_comprehensive_income_gap_sqnorm_equity_63d_base_v106_signal(consolinc, equity):
    r = _comprehensive_income_gap_scaled(consolinc, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized consolinc/equity 252d mean
def cig_f058_comprehensive_income_gap_sqnorm_equity_252d_base_v107_signal(consolinc, equity):
    r = _comprehensive_income_gap_scaled(consolinc, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized consolinc/assets 63d mean
def cig_f058_comprehensive_income_gap_sqnorm_assets_63d_base_v108_signal(consolinc, assets):
    r = _comprehensive_income_gap_scaled(consolinc, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized consolinc/assets 252d mean
def cig_f058_comprehensive_income_gap_sqnorm_assets_252d_base_v109_signal(consolinc, assets):
    r = _comprehensive_income_gap_scaled(consolinc, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of consolinc times closeadj
def cig_f058_comprehensive_income_gap_infrat_63d_base_v110_signal(consolinc, closeadj):
    m = _mean(consolinc, 63)
    s = _std(consolinc, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of consolinc times closeadj
def cig_f058_comprehensive_income_gap_infrat_252d_base_v111_signal(consolinc, closeadj):
    m = _mean(consolinc, 252)
    s = _std(consolinc, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of consolinc times closeadj
def cig_f058_comprehensive_income_gap_infrat_504d_base_v112_signal(consolinc, closeadj):
    m = _mean(consolinc, 504)
    s = _std(consolinc, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of consolinc
def cig_f058_comprehensive_income_gap_cv_252d_base_v113_signal(consolinc):
    m = _mean(consolinc, 252).abs().replace(0, np.nan)
    s = _std(consolinc, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of consolinc
def cig_f058_comprehensive_income_gap_cv_504d_base_v114_signal(consolinc):
    m = _mean(consolinc, 504).abs().replace(0, np.nan)
    s = _std(consolinc, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged consolinc times closeadj
def cig_f058_comprehensive_income_gap_lag_5d_base_v115_signal(consolinc, closeadj):
    result = consolinc.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged consolinc times closeadj
def cig_f058_comprehensive_income_gap_lag_21d_base_v116_signal(consolinc, closeadj):
    result = consolinc.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged consolinc times closeadj
def cig_f058_comprehensive_income_gap_lag_63d_base_v117_signal(consolinc, closeadj):
    result = consolinc.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged consolinc times closeadj
def cig_f058_comprehensive_income_gap_lag_252d_base_v118_signal(consolinc, closeadj):
    result = consolinc.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(consolinc) / mean(netinc) x closeadj
def cig_f058_comprehensive_income_gap_cumper_netinc_252d_base_v119_signal(consolinc, netinc, closeadj):
    s = consolinc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(consolinc) / mean(netinc) x closeadj
def cig_f058_comprehensive_income_gap_cumper_netinc_504d_base_v120_signal(consolinc, netinc, closeadj):
    s = consolinc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(consolinc) / mean(equity) x closeadj
def cig_f058_comprehensive_income_gap_cumper_equity_252d_base_v121_signal(consolinc, equity, closeadj):
    s = consolinc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(equity, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(consolinc) / mean(equity) x closeadj
def cig_f058_comprehensive_income_gap_cumper_equity_504d_base_v122_signal(consolinc, equity, closeadj):
    s = consolinc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(equity, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only consolinc times closeadj
def cig_f058_comprehensive_income_gap_pos_63d_base_v123_signal(consolinc, closeadj):
    pos = consolinc.where(consolinc > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only consolinc times closeadj
def cig_f058_comprehensive_income_gap_pos_252d_base_v124_signal(consolinc, closeadj):
    pos = consolinc.where(consolinc > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only consolinc times closeadj
def cig_f058_comprehensive_income_gap_neg_63d_base_v125_signal(consolinc, closeadj):
    neg = consolinc.where(consolinc < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only consolinc times closeadj
def cig_f058_comprehensive_income_gap_neg_252d_base_v126_signal(consolinc, closeadj):
    neg = consolinc.where(consolinc < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of consolinc times closeadj
def cig_f058_comprehensive_income_gap_hl_21d_base_v127_signal(consolinc, closeadj):
    result = consolinc.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of consolinc times closeadj
def cig_f058_comprehensive_income_gap_hl_63d_base_v128_signal(consolinc, closeadj):
    result = consolinc.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of consolinc times closeadj
def cig_f058_comprehensive_income_gap_hl_252d_base_v129_signal(consolinc, closeadj):
    result = consolinc.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of consolinc
def cig_f058_comprehensive_income_gap_z_63d_base_v130_signal(consolinc):
    result = _z(consolinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of consolinc
def cig_f058_comprehensive_income_gap_z_126d_base_v131_signal(consolinc):
    result = _z(consolinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of consolinc
def cig_f058_comprehensive_income_gap_z_1008d_base_v132_signal(consolinc):
    result = _z(consolinc, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of consolinc times closeadj
def cig_f058_comprehensive_income_gap_st_lt_252_21d_base_v133_signal(consolinc, closeadj):
    sm = _mean(consolinc, 21)
    lm = _mean(consolinc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of consolinc times closeadj
def cig_f058_comprehensive_income_gap_st_lt_252_63d_base_v134_signal(consolinc, closeadj):
    sm = _mean(consolinc, 63)
    lm = _mean(consolinc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of consolinc times closeadj
def cig_f058_comprehensive_income_gap_st_lt_504_21d_base_v135_signal(consolinc, closeadj):
    sm = _mean(consolinc, 21)
    lm = _mean(consolinc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of consolinc times closeadj
def cig_f058_comprehensive_income_gap_st_lt_504_63d_base_v136_signal(consolinc, closeadj):
    sm = _mean(consolinc, 63)
    lm = _mean(consolinc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged consolinc/netinc times closeadj
def cig_f058_comprehensive_income_gap_lag_per_netinc_21d_base_v137_signal(consolinc, netinc, closeadj):
    r = _comprehensive_income_gap_scaled(consolinc, netinc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged consolinc/netinc times closeadj
def cig_f058_comprehensive_income_gap_lag_per_netinc_63d_base_v138_signal(consolinc, netinc, closeadj):
    r = _comprehensive_income_gap_scaled(consolinc, netinc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged consolinc/netinc times closeadj
def cig_f058_comprehensive_income_gap_lag_per_netinc_252d_base_v139_signal(consolinc, netinc, closeadj):
    r = _comprehensive_income_gap_scaled(consolinc, netinc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged consolinc/equity times closeadj
def cig_f058_comprehensive_income_gap_lag_per_equity_21d_base_v140_signal(consolinc, equity, closeadj):
    r = _comprehensive_income_gap_scaled(consolinc, equity)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged consolinc/equity times closeadj
def cig_f058_comprehensive_income_gap_lag_per_equity_63d_base_v141_signal(consolinc, equity, closeadj):
    r = _comprehensive_income_gap_scaled(consolinc, equity)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged consolinc/equity times closeadj
def cig_f058_comprehensive_income_gap_lag_per_equity_252d_base_v142_signal(consolinc, equity, closeadj):
    r = _comprehensive_income_gap_scaled(consolinc, equity)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |consolinc| times closeadj
def cig_f058_comprehensive_income_gap_abssum_63d_base_v143_signal(consolinc, closeadj):
    result = consolinc.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |consolinc| times closeadj
def cig_f058_comprehensive_income_gap_abssum_252d_base_v144_signal(consolinc, closeadj):
    result = consolinc.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |consolinc| times closeadj
def cig_f058_comprehensive_income_gap_abssum_504d_base_v145_signal(consolinc, closeadj):
    result = consolinc.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of consolinc
def cig_f058_comprehensive_income_gap_acf1_252d_base_v146_signal(consolinc):
    result = consolinc.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of consolinc
def cig_f058_comprehensive_income_gap_acf1_504d_base_v147_signal(consolinc):
    result = consolinc.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of consolinc
def cig_f058_comprehensive_income_gap_posinrange_252d_base_v148_signal(consolinc):
    m = _mean(consolinc, 252)
    hi = consolinc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = consolinc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of consolinc
def cig_f058_comprehensive_income_gap_posinrange_504d_base_v149_signal(consolinc):
    m = _mean(consolinc, 504)
    hi = consolinc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = consolinc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of consolinc times closeadj
def cig_f058_comprehensive_income_gap_hl_5d_base_v150_signal(consolinc, closeadj):
    result = consolinc.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
