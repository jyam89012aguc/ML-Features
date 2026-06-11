"""Family f023 - Current versus long-term debt mix (Capital Structure) | Sharadar tables: SF1 | fields: debtc, debtnc, debt | base 076-150"""
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
def _debt_maturity_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _debt_maturity_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _debt_maturity_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of debtc/debt
def dmm_f023_debt_maturity_mix_log_per_debt_504d_base_v076_signal(debtc, debt):
    s = _debt_maturity_mix_scaled(debtc, debt)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of debtc/assets
def dmm_f023_debt_maturity_mix_log_per_assets_252d_base_v077_signal(debtc, assets):
    s = _debt_maturity_mix_scaled(debtc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of debtc/assets
def dmm_f023_debt_maturity_mix_log_per_assets_504d_base_v078_signal(debtc, assets):
    s = _debt_maturity_mix_scaled(debtc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of debtc times closeadj
def dmm_f023_debt_maturity_mix_ewm_21d_base_v079_signal(debtc, closeadj):
    result = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of debtc times closeadj
def dmm_f023_debt_maturity_mix_ewm_63d_base_v080_signal(debtc, closeadj):
    result = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of debtc times closeadj
def dmm_f023_debt_maturity_mix_ewm_252d_base_v081_signal(debtc, closeadj):
    result = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of debtc times closeadj
def dmm_f023_debt_maturity_mix_med_63d_base_v082_signal(debtc, closeadj):
    result = debtc.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of debtc times closeadj
def dmm_f023_debt_maturity_mix_med_252d_base_v083_signal(debtc, closeadj):
    result = debtc.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of debtc times closeadj
def dmm_f023_debt_maturity_mix_med_504d_base_v084_signal(debtc, closeadj):
    result = debtc.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of debtc
def dmm_f023_debt_maturity_mix_skew_252d_base_v085_signal(debtc):
    result = debtc.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of debtc
def dmm_f023_debt_maturity_mix_skew_504d_base_v086_signal(debtc):
    result = debtc.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of debtc
def dmm_f023_debt_maturity_mix_kurt_252d_base_v087_signal(debtc):
    result = debtc.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of debtc
def dmm_f023_debt_maturity_mix_kurt_504d_base_v088_signal(debtc):
    result = debtc.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of debtc times closeadj
def dmm_f023_debt_maturity_mix_rank_252d_base_v089_signal(debtc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = debtc.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of debtc times closeadj
def dmm_f023_debt_maturity_mix_rank_504d_base_v090_signal(debtc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = debtc.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of debtc times closeadj
def dmm_f023_debt_maturity_mix_rank_1008d_base_v091_signal(debtc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = debtc.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of debtc from 63d mean times closeadj
def dmm_f023_debt_maturity_mix_devmean_63d_base_v092_signal(debtc, closeadj):
    m = _mean(debtc, 63)
    result = (debtc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of debtc from 252d mean times closeadj
def dmm_f023_debt_maturity_mix_devmean_252d_base_v093_signal(debtc, closeadj):
    m = _mean(debtc, 252)
    result = (debtc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of debtc from 504d mean times closeadj
def dmm_f023_debt_maturity_mix_devmean_504d_base_v094_signal(debtc, closeadj):
    m = _mean(debtc, 504)
    result = (debtc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of debtc times closeadj
def dmm_f023_debt_maturity_mix_logdiff_21d_base_v095_signal(debtc, closeadj):
    lr = _debt_maturity_mix_log(debtc)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of debtc times closeadj
def dmm_f023_debt_maturity_mix_logdiff_63d_base_v096_signal(debtc, closeadj):
    lr = _debt_maturity_mix_log(debtc)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of debtc times closeadj
def dmm_f023_debt_maturity_mix_logdiff_252d_base_v097_signal(debtc, closeadj):
    lr = _debt_maturity_mix_log(debtc)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of debtc times closeadj
def dmm_f023_debt_maturity_mix_range_63d_base_v098_signal(debtc, closeadj):
    hi = debtc.rolling(63, min_periods=max(1, 63//2)).max()
    lo = debtc.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of debtc times closeadj
def dmm_f023_debt_maturity_mix_range_252d_base_v099_signal(debtc, closeadj):
    hi = debtc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = debtc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of debtc times closeadj
def dmm_f023_debt_maturity_mix_range_504d_base_v100_signal(debtc, closeadj):
    hi = debtc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = debtc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 252d mean times closeadj
def dmm_f023_debt_maturity_mix_rel_252d_base_v101_signal(debtc, closeadj):
    m = _mean(debtc, 252).replace(0, np.nan)
    result = (debtc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 504d mean times closeadj
def dmm_f023_debt_maturity_mix_rel_504d_base_v102_signal(debtc, closeadj):
    m = _mean(debtc, 504).replace(0, np.nan)
    result = (debtc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 1008d mean times closeadj
def dmm_f023_debt_maturity_mix_rel_1008d_base_v103_signal(debtc, closeadj):
    m = _mean(debtc, 1008).replace(0, np.nan)
    result = (debtc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debtc/debtnc 63d mean
def dmm_f023_debt_maturity_mix_sqnorm_debtnc_63d_base_v104_signal(debtc, debtnc):
    r = _debt_maturity_mix_scaled(debtc, debtnc)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debtc/debtnc 252d mean
def dmm_f023_debt_maturity_mix_sqnorm_debtnc_252d_base_v105_signal(debtc, debtnc):
    r = _debt_maturity_mix_scaled(debtc, debtnc)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debtc/debt 63d mean
def dmm_f023_debt_maturity_mix_sqnorm_debt_63d_base_v106_signal(debtc, debt):
    r = _debt_maturity_mix_scaled(debtc, debt)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debtc/debt 252d mean
def dmm_f023_debt_maturity_mix_sqnorm_debt_252d_base_v107_signal(debtc, debt):
    r = _debt_maturity_mix_scaled(debtc, debt)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debtc/assets 63d mean
def dmm_f023_debt_maturity_mix_sqnorm_assets_63d_base_v108_signal(debtc, assets):
    r = _debt_maturity_mix_scaled(debtc, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debtc/assets 252d mean
def dmm_f023_debt_maturity_mix_sqnorm_assets_252d_base_v109_signal(debtc, assets):
    r = _debt_maturity_mix_scaled(debtc, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of debtc times closeadj
def dmm_f023_debt_maturity_mix_infrat_63d_base_v110_signal(debtc, closeadj):
    m = _mean(debtc, 63)
    s = _std(debtc, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of debtc times closeadj
def dmm_f023_debt_maturity_mix_infrat_252d_base_v111_signal(debtc, closeadj):
    m = _mean(debtc, 252)
    s = _std(debtc, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of debtc times closeadj
def dmm_f023_debt_maturity_mix_infrat_504d_base_v112_signal(debtc, closeadj):
    m = _mean(debtc, 504)
    s = _std(debtc, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of debtc
def dmm_f023_debt_maturity_mix_cv_252d_base_v113_signal(debtc):
    m = _mean(debtc, 252).abs().replace(0, np.nan)
    s = _std(debtc, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of debtc
def dmm_f023_debt_maturity_mix_cv_504d_base_v114_signal(debtc):
    m = _mean(debtc, 504).abs().replace(0, np.nan)
    s = _std(debtc, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged debtc times closeadj
def dmm_f023_debt_maturity_mix_lag_5d_base_v115_signal(debtc, closeadj):
    result = debtc.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged debtc times closeadj
def dmm_f023_debt_maturity_mix_lag_21d_base_v116_signal(debtc, closeadj):
    result = debtc.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged debtc times closeadj
def dmm_f023_debt_maturity_mix_lag_63d_base_v117_signal(debtc, closeadj):
    result = debtc.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged debtc times closeadj
def dmm_f023_debt_maturity_mix_lag_252d_base_v118_signal(debtc, closeadj):
    result = debtc.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(debtc) / mean(debtnc) x closeadj
def dmm_f023_debt_maturity_mix_cumper_debtnc_252d_base_v119_signal(debtc, debtnc, closeadj):
    s = debtc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(debtnc, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(debtc) / mean(debtnc) x closeadj
def dmm_f023_debt_maturity_mix_cumper_debtnc_504d_base_v120_signal(debtc, debtnc, closeadj):
    s = debtc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(debtnc, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(debtc) / mean(debt) x closeadj
def dmm_f023_debt_maturity_mix_cumper_debt_252d_base_v121_signal(debtc, debt, closeadj):
    s = debtc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(debt, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(debtc) / mean(debt) x closeadj
def dmm_f023_debt_maturity_mix_cumper_debt_504d_base_v122_signal(debtc, debt, closeadj):
    s = debtc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(debt, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only debtc times closeadj
def dmm_f023_debt_maturity_mix_pos_63d_base_v123_signal(debtc, closeadj):
    pos = debtc.where(debtc > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only debtc times closeadj
def dmm_f023_debt_maturity_mix_pos_252d_base_v124_signal(debtc, closeadj):
    pos = debtc.where(debtc > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only debtc times closeadj
def dmm_f023_debt_maturity_mix_neg_63d_base_v125_signal(debtc, closeadj):
    neg = debtc.where(debtc < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only debtc times closeadj
def dmm_f023_debt_maturity_mix_neg_252d_base_v126_signal(debtc, closeadj):
    neg = debtc.where(debtc < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of debtc times closeadj
def dmm_f023_debt_maturity_mix_hl_21d_base_v127_signal(debtc, closeadj):
    result = debtc.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of debtc times closeadj
def dmm_f023_debt_maturity_mix_hl_63d_base_v128_signal(debtc, closeadj):
    result = debtc.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of debtc times closeadj
def dmm_f023_debt_maturity_mix_hl_252d_base_v129_signal(debtc, closeadj):
    result = debtc.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of debtc
def dmm_f023_debt_maturity_mix_z_63d_base_v130_signal(debtc):
    result = _z(debtc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of debtc
def dmm_f023_debt_maturity_mix_z_126d_base_v131_signal(debtc):
    result = _z(debtc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of debtc
def dmm_f023_debt_maturity_mix_z_1008d_base_v132_signal(debtc):
    result = _z(debtc, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of debtc times closeadj
def dmm_f023_debt_maturity_mix_st_lt_252_21d_base_v133_signal(debtc, closeadj):
    sm = _mean(debtc, 21)
    lm = _mean(debtc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of debtc times closeadj
def dmm_f023_debt_maturity_mix_st_lt_252_63d_base_v134_signal(debtc, closeadj):
    sm = _mean(debtc, 63)
    lm = _mean(debtc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of debtc times closeadj
def dmm_f023_debt_maturity_mix_st_lt_504_21d_base_v135_signal(debtc, closeadj):
    sm = _mean(debtc, 21)
    lm = _mean(debtc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of debtc times closeadj
def dmm_f023_debt_maturity_mix_st_lt_504_63d_base_v136_signal(debtc, closeadj):
    sm = _mean(debtc, 63)
    lm = _mean(debtc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged debtc/debtnc times closeadj
def dmm_f023_debt_maturity_mix_lag_per_debtnc_21d_base_v137_signal(debtc, debtnc, closeadj):
    r = _debt_maturity_mix_scaled(debtc, debtnc)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged debtc/debtnc times closeadj
def dmm_f023_debt_maturity_mix_lag_per_debtnc_63d_base_v138_signal(debtc, debtnc, closeadj):
    r = _debt_maturity_mix_scaled(debtc, debtnc)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged debtc/debtnc times closeadj
def dmm_f023_debt_maturity_mix_lag_per_debtnc_252d_base_v139_signal(debtc, debtnc, closeadj):
    r = _debt_maturity_mix_scaled(debtc, debtnc)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged debtc/debt times closeadj
def dmm_f023_debt_maturity_mix_lag_per_debt_21d_base_v140_signal(debtc, debt, closeadj):
    r = _debt_maturity_mix_scaled(debtc, debt)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged debtc/debt times closeadj
def dmm_f023_debt_maturity_mix_lag_per_debt_63d_base_v141_signal(debtc, debt, closeadj):
    r = _debt_maturity_mix_scaled(debtc, debt)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged debtc/debt times closeadj
def dmm_f023_debt_maturity_mix_lag_per_debt_252d_base_v142_signal(debtc, debt, closeadj):
    r = _debt_maturity_mix_scaled(debtc, debt)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |debtc| times closeadj
def dmm_f023_debt_maturity_mix_abssum_63d_base_v143_signal(debtc, closeadj):
    result = debtc.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |debtc| times closeadj
def dmm_f023_debt_maturity_mix_abssum_252d_base_v144_signal(debtc, closeadj):
    result = debtc.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |debtc| times closeadj
def dmm_f023_debt_maturity_mix_abssum_504d_base_v145_signal(debtc, closeadj):
    result = debtc.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of debtc
def dmm_f023_debt_maturity_mix_acf1_252d_base_v146_signal(debtc):
    result = debtc.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of debtc
def dmm_f023_debt_maturity_mix_acf1_504d_base_v147_signal(debtc):
    result = debtc.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of debtc
def dmm_f023_debt_maturity_mix_posinrange_252d_base_v148_signal(debtc):
    m = _mean(debtc, 252)
    hi = debtc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = debtc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of debtc
def dmm_f023_debt_maturity_mix_posinrange_504d_base_v149_signal(debtc):
    m = _mean(debtc, 504)
    hi = debtc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = debtc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of debtc times closeadj
def dmm_f023_debt_maturity_mix_hl_5d_base_v150_signal(debtc, closeadj):
    result = debtc.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
