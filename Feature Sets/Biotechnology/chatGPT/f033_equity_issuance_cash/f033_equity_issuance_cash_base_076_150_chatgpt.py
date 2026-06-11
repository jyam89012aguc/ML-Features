"""Family f033 - Equity issuance proceeds (Dilution and Share Count) | Sharadar tables: SF1 | fields: ncfcommon, ncff, sharesbas | base 076-150"""
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
def _equity_issuance_cash_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _equity_issuance_cash_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _equity_issuance_cash_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ncfcommon/sharesbas
def eic_f033_equity_issuance_cash_log_per_sharesbas_504d_base_v076_signal(ncfcommon, sharesbas):
    s = _equity_issuance_cash_scaled(ncfcommon, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfcommon/assets
def eic_f033_equity_issuance_cash_log_per_assets_252d_base_v077_signal(ncfcommon, assets):
    s = _equity_issuance_cash_scaled(ncfcommon, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncfcommon/assets
def eic_f033_equity_issuance_cash_log_per_assets_504d_base_v078_signal(ncfcommon, assets):
    s = _equity_issuance_cash_scaled(ncfcommon, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_ewm_21d_base_v079_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_ewm_63d_base_v080_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_ewm_252d_base_v081_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_med_63d_base_v082_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_med_252d_base_v083_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_med_504d_base_v084_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ncfcommon
def eic_f033_equity_issuance_cash_skew_252d_base_v085_signal(ncfcommon):
    result = ncfcommon.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ncfcommon
def eic_f033_equity_issuance_cash_skew_504d_base_v086_signal(ncfcommon):
    result = ncfcommon.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ncfcommon
def eic_f033_equity_issuance_cash_kurt_252d_base_v087_signal(ncfcommon):
    result = ncfcommon.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ncfcommon
def eic_f033_equity_issuance_cash_kurt_504d_base_v088_signal(ncfcommon):
    result = ncfcommon.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_rank_252d_base_v089_signal(ncfcommon, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfcommon.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_rank_504d_base_v090_signal(ncfcommon, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfcommon.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_rank_1008d_base_v091_signal(ncfcommon, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfcommon.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfcommon from 63d mean times closeadj
def eic_f033_equity_issuance_cash_devmean_63d_base_v092_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 63)
    result = (ncfcommon - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfcommon from 252d mean times closeadj
def eic_f033_equity_issuance_cash_devmean_252d_base_v093_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 252)
    result = (ncfcommon - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfcommon from 504d mean times closeadj
def eic_f033_equity_issuance_cash_devmean_504d_base_v094_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 504)
    result = (ncfcommon - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_logdiff_21d_base_v095_signal(ncfcommon, closeadj):
    lr = _equity_issuance_cash_log(ncfcommon)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_logdiff_63d_base_v096_signal(ncfcommon, closeadj):
    lr = _equity_issuance_cash_log(ncfcommon)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_logdiff_252d_base_v097_signal(ncfcommon, closeadj):
    lr = _equity_issuance_cash_log(ncfcommon)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_range_63d_base_v098_signal(ncfcommon, closeadj):
    hi = ncfcommon.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ncfcommon.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_range_252d_base_v099_signal(ncfcommon, closeadj):
    hi = ncfcommon.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncfcommon.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_range_504d_base_v100_signal(ncfcommon, closeadj):
    hi = ncfcommon.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncfcommon.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 252d mean times closeadj
def eic_f033_equity_issuance_cash_rel_252d_base_v101_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 252).replace(0, np.nan)
    result = (ncfcommon / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 504d mean times closeadj
def eic_f033_equity_issuance_cash_rel_504d_base_v102_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 504).replace(0, np.nan)
    result = (ncfcommon / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 1008d mean times closeadj
def eic_f033_equity_issuance_cash_rel_1008d_base_v103_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 1008).replace(0, np.nan)
    result = (ncfcommon / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfcommon/ncff 63d mean
def eic_f033_equity_issuance_cash_sqnorm_ncff_63d_base_v104_signal(ncfcommon, ncff):
    r = _equity_issuance_cash_scaled(ncfcommon, ncff)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfcommon/ncff 252d mean
def eic_f033_equity_issuance_cash_sqnorm_ncff_252d_base_v105_signal(ncfcommon, ncff):
    r = _equity_issuance_cash_scaled(ncfcommon, ncff)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfcommon/sharesbas 63d mean
def eic_f033_equity_issuance_cash_sqnorm_sharesbas_63d_base_v106_signal(ncfcommon, sharesbas):
    r = _equity_issuance_cash_scaled(ncfcommon, sharesbas)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfcommon/sharesbas 252d mean
def eic_f033_equity_issuance_cash_sqnorm_sharesbas_252d_base_v107_signal(ncfcommon, sharesbas):
    r = _equity_issuance_cash_scaled(ncfcommon, sharesbas)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfcommon/assets 63d mean
def eic_f033_equity_issuance_cash_sqnorm_assets_63d_base_v108_signal(ncfcommon, assets):
    r = _equity_issuance_cash_scaled(ncfcommon, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfcommon/assets 252d mean
def eic_f033_equity_issuance_cash_sqnorm_assets_252d_base_v109_signal(ncfcommon, assets):
    r = _equity_issuance_cash_scaled(ncfcommon, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_infrat_63d_base_v110_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 63)
    s = _std(ncfcommon, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_infrat_252d_base_v111_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 252)
    s = _std(ncfcommon, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_infrat_504d_base_v112_signal(ncfcommon, closeadj):
    m = _mean(ncfcommon, 504)
    s = _std(ncfcommon, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ncfcommon
def eic_f033_equity_issuance_cash_cv_252d_base_v113_signal(ncfcommon):
    m = _mean(ncfcommon, 252).abs().replace(0, np.nan)
    s = _std(ncfcommon, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ncfcommon
def eic_f033_equity_issuance_cash_cv_504d_base_v114_signal(ncfcommon):
    m = _mean(ncfcommon, 504).abs().replace(0, np.nan)
    s = _std(ncfcommon, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ncfcommon times closeadj
def eic_f033_equity_issuance_cash_lag_5d_base_v115_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfcommon times closeadj
def eic_f033_equity_issuance_cash_lag_21d_base_v116_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfcommon times closeadj
def eic_f033_equity_issuance_cash_lag_63d_base_v117_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfcommon times closeadj
def eic_f033_equity_issuance_cash_lag_252d_base_v118_signal(ncfcommon, closeadj):
    result = ncfcommon.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncfcommon) / mean(ncff) x closeadj
def eic_f033_equity_issuance_cash_cumper_ncff_252d_base_v119_signal(ncfcommon, ncff, closeadj):
    s = ncfcommon.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ncff, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncfcommon) / mean(ncff) x closeadj
def eic_f033_equity_issuance_cash_cumper_ncff_504d_base_v120_signal(ncfcommon, ncff, closeadj):
    s = ncfcommon.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ncff, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncfcommon) / mean(sharesbas) x closeadj
def eic_f033_equity_issuance_cash_cumper_sharesbas_252d_base_v121_signal(ncfcommon, sharesbas, closeadj):
    s = ncfcommon.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncfcommon) / mean(sharesbas) x closeadj
def eic_f033_equity_issuance_cash_cumper_sharesbas_504d_base_v122_signal(ncfcommon, sharesbas, closeadj):
    s = ncfcommon.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ncfcommon times closeadj
def eic_f033_equity_issuance_cash_pos_63d_base_v123_signal(ncfcommon, closeadj):
    pos = ncfcommon.where(ncfcommon > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ncfcommon times closeadj
def eic_f033_equity_issuance_cash_pos_252d_base_v124_signal(ncfcommon, closeadj):
    pos = ncfcommon.where(ncfcommon > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ncfcommon times closeadj
def eic_f033_equity_issuance_cash_neg_63d_base_v125_signal(ncfcommon, closeadj):
    neg = ncfcommon.where(ncfcommon < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ncfcommon times closeadj
def eic_f033_equity_issuance_cash_neg_252d_base_v126_signal(ncfcommon, closeadj):
    neg = ncfcommon.where(ncfcommon < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_hl_21d_base_v127_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_hl_63d_base_v128_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_hl_252d_base_v129_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ncfcommon
def eic_f033_equity_issuance_cash_z_63d_base_v130_signal(ncfcommon):
    result = _z(ncfcommon, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ncfcommon
def eic_f033_equity_issuance_cash_z_126d_base_v131_signal(ncfcommon):
    result = _z(ncfcommon, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ncfcommon
def eic_f033_equity_issuance_cash_z_1008d_base_v132_signal(ncfcommon):
    result = _z(ncfcommon, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_st_lt_252_21d_base_v133_signal(ncfcommon, closeadj):
    sm = _mean(ncfcommon, 21)
    lm = _mean(ncfcommon, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_st_lt_252_63d_base_v134_signal(ncfcommon, closeadj):
    sm = _mean(ncfcommon, 63)
    lm = _mean(ncfcommon, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_st_lt_504_21d_base_v135_signal(ncfcommon, closeadj):
    sm = _mean(ncfcommon, 21)
    lm = _mean(ncfcommon, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_st_lt_504_63d_base_v136_signal(ncfcommon, closeadj):
    sm = _mean(ncfcommon, 63)
    lm = _mean(ncfcommon, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfcommon/ncff times closeadj
def eic_f033_equity_issuance_cash_lag_per_ncff_21d_base_v137_signal(ncfcommon, ncff, closeadj):
    r = _equity_issuance_cash_scaled(ncfcommon, ncff)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfcommon/ncff times closeadj
def eic_f033_equity_issuance_cash_lag_per_ncff_63d_base_v138_signal(ncfcommon, ncff, closeadj):
    r = _equity_issuance_cash_scaled(ncfcommon, ncff)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfcommon/ncff times closeadj
def eic_f033_equity_issuance_cash_lag_per_ncff_252d_base_v139_signal(ncfcommon, ncff, closeadj):
    r = _equity_issuance_cash_scaled(ncfcommon, ncff)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfcommon/sharesbas times closeadj
def eic_f033_equity_issuance_cash_lag_per_sharesbas_21d_base_v140_signal(ncfcommon, sharesbas, closeadj):
    r = _equity_issuance_cash_scaled(ncfcommon, sharesbas)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfcommon/sharesbas times closeadj
def eic_f033_equity_issuance_cash_lag_per_sharesbas_63d_base_v141_signal(ncfcommon, sharesbas, closeadj):
    r = _equity_issuance_cash_scaled(ncfcommon, sharesbas)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfcommon/sharesbas times closeadj
def eic_f033_equity_issuance_cash_lag_per_sharesbas_252d_base_v142_signal(ncfcommon, sharesbas, closeadj):
    r = _equity_issuance_cash_scaled(ncfcommon, sharesbas)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ncfcommon| times closeadj
def eic_f033_equity_issuance_cash_abssum_63d_base_v143_signal(ncfcommon, closeadj):
    result = ncfcommon.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ncfcommon| times closeadj
def eic_f033_equity_issuance_cash_abssum_252d_base_v144_signal(ncfcommon, closeadj):
    result = ncfcommon.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ncfcommon| times closeadj
def eic_f033_equity_issuance_cash_abssum_504d_base_v145_signal(ncfcommon, closeadj):
    result = ncfcommon.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ncfcommon
def eic_f033_equity_issuance_cash_acf1_252d_base_v146_signal(ncfcommon):
    result = ncfcommon.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ncfcommon
def eic_f033_equity_issuance_cash_acf1_504d_base_v147_signal(ncfcommon):
    result = ncfcommon.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ncfcommon
def eic_f033_equity_issuance_cash_posinrange_252d_base_v148_signal(ncfcommon):
    m = _mean(ncfcommon, 252)
    hi = ncfcommon.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncfcommon.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ncfcommon
def eic_f033_equity_issuance_cash_posinrange_504d_base_v149_signal(ncfcommon):
    m = _mean(ncfcommon, 504)
    hi = ncfcommon.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncfcommon.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ncfcommon times closeadj
def eic_f033_equity_issuance_cash_hl_5d_base_v150_signal(ncfcommon, closeadj):
    result = ncfcommon.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
