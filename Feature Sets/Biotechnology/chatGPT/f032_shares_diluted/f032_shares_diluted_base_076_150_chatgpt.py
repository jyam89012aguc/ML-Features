"""Family f032 - Diluted share overhang (Dilution and Share Count) | Sharadar tables: SF1 | fields: shareswa, shareswadil, sharesbas | base 076-150"""
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
def _shares_diluted_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _shares_diluted_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _shares_diluted_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of shareswa/sharesbas
def sd_f032_shares_diluted_log_per_sharesbas_504d_base_v076_signal(shareswa, sharesbas):
    s = _shares_diluted_scaled(shareswa, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of shareswa/assets
def sd_f032_shares_diluted_log_per_assets_252d_base_v077_signal(shareswa, assets):
    s = _shares_diluted_scaled(shareswa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of shareswa/assets
def sd_f032_shares_diluted_log_per_assets_504d_base_v078_signal(shareswa, assets):
    s = _shares_diluted_scaled(shareswa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of shareswa times closeadj
def sd_f032_shares_diluted_ewm_21d_base_v079_signal(shareswa, closeadj):
    result = shareswa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of shareswa times closeadj
def sd_f032_shares_diluted_ewm_63d_base_v080_signal(shareswa, closeadj):
    result = shareswa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of shareswa times closeadj
def sd_f032_shares_diluted_ewm_252d_base_v081_signal(shareswa, closeadj):
    result = shareswa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of shareswa times closeadj
def sd_f032_shares_diluted_med_63d_base_v082_signal(shareswa, closeadj):
    result = shareswa.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of shareswa times closeadj
def sd_f032_shares_diluted_med_252d_base_v083_signal(shareswa, closeadj):
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of shareswa times closeadj
def sd_f032_shares_diluted_med_504d_base_v084_signal(shareswa, closeadj):
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of shareswa
def sd_f032_shares_diluted_skew_252d_base_v085_signal(shareswa):
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of shareswa
def sd_f032_shares_diluted_skew_504d_base_v086_signal(shareswa):
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of shareswa
def sd_f032_shares_diluted_kurt_252d_base_v087_signal(shareswa):
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of shareswa
def sd_f032_shares_diluted_kurt_504d_base_v088_signal(shareswa):
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of shareswa times closeadj
def sd_f032_shares_diluted_rank_252d_base_v089_signal(shareswa, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of shareswa times closeadj
def sd_f032_shares_diluted_rank_504d_base_v090_signal(shareswa, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of shareswa times closeadj
def sd_f032_shares_diluted_rank_1008d_base_v091_signal(shareswa, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = shareswa.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of shareswa from 63d mean times closeadj
def sd_f032_shares_diluted_devmean_63d_base_v092_signal(shareswa, closeadj):
    m = _mean(shareswa, 63)
    result = (shareswa - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of shareswa from 252d mean times closeadj
def sd_f032_shares_diluted_devmean_252d_base_v093_signal(shareswa, closeadj):
    m = _mean(shareswa, 252)
    result = (shareswa - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of shareswa from 504d mean times closeadj
def sd_f032_shares_diluted_devmean_504d_base_v094_signal(shareswa, closeadj):
    m = _mean(shareswa, 504)
    result = (shareswa - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of shareswa times closeadj
def sd_f032_shares_diluted_logdiff_21d_base_v095_signal(shareswa, closeadj):
    lr = _shares_diluted_log(shareswa)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of shareswa times closeadj
def sd_f032_shares_diluted_logdiff_63d_base_v096_signal(shareswa, closeadj):
    lr = _shares_diluted_log(shareswa)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of shareswa times closeadj
def sd_f032_shares_diluted_logdiff_252d_base_v097_signal(shareswa, closeadj):
    lr = _shares_diluted_log(shareswa)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of shareswa times closeadj
def sd_f032_shares_diluted_range_63d_base_v098_signal(shareswa, closeadj):
    hi = shareswa.rolling(63, min_periods=max(1, 63//2)).max()
    lo = shareswa.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of shareswa times closeadj
def sd_f032_shares_diluted_range_252d_base_v099_signal(shareswa, closeadj):
    hi = shareswa.rolling(252, min_periods=max(1, 252//2)).max()
    lo = shareswa.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of shareswa times closeadj
def sd_f032_shares_diluted_range_504d_base_v100_signal(shareswa, closeadj):
    hi = shareswa.rolling(504, min_periods=max(1, 504//2)).max()
    lo = shareswa.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 252d mean times closeadj
def sd_f032_shares_diluted_rel_252d_base_v101_signal(shareswa, closeadj):
    m = _mean(shareswa, 252).replace(0, np.nan)
    result = (shareswa / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 504d mean times closeadj
def sd_f032_shares_diluted_rel_504d_base_v102_signal(shareswa, closeadj):
    m = _mean(shareswa, 504).replace(0, np.nan)
    result = (shareswa / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa relative to 1008d mean times closeadj
def sd_f032_shares_diluted_rel_1008d_base_v103_signal(shareswa, closeadj):
    m = _mean(shareswa, 1008).replace(0, np.nan)
    result = (shareswa / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized shareswa/shareswadil 63d mean
def sd_f032_shares_diluted_sqnorm_shareswadil_63d_base_v104_signal(shareswa, shareswadil):
    r = _shares_diluted_scaled(shareswa, shareswadil)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized shareswa/shareswadil 252d mean
def sd_f032_shares_diluted_sqnorm_shareswadil_252d_base_v105_signal(shareswa, shareswadil):
    r = _shares_diluted_scaled(shareswa, shareswadil)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized shareswa/sharesbas 63d mean
def sd_f032_shares_diluted_sqnorm_sharesbas_63d_base_v106_signal(shareswa, sharesbas):
    r = _shares_diluted_scaled(shareswa, sharesbas)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized shareswa/sharesbas 252d mean
def sd_f032_shares_diluted_sqnorm_sharesbas_252d_base_v107_signal(shareswa, sharesbas):
    r = _shares_diluted_scaled(shareswa, sharesbas)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized shareswa/assets 63d mean
def sd_f032_shares_diluted_sqnorm_assets_63d_base_v108_signal(shareswa, assets):
    r = _shares_diluted_scaled(shareswa, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized shareswa/assets 252d mean
def sd_f032_shares_diluted_sqnorm_assets_252d_base_v109_signal(shareswa, assets):
    r = _shares_diluted_scaled(shareswa, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of shareswa times closeadj
def sd_f032_shares_diluted_infrat_63d_base_v110_signal(shareswa, closeadj):
    m = _mean(shareswa, 63)
    s = _std(shareswa, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of shareswa times closeadj
def sd_f032_shares_diluted_infrat_252d_base_v111_signal(shareswa, closeadj):
    m = _mean(shareswa, 252)
    s = _std(shareswa, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of shareswa times closeadj
def sd_f032_shares_diluted_infrat_504d_base_v112_signal(shareswa, closeadj):
    m = _mean(shareswa, 504)
    s = _std(shareswa, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of shareswa
def sd_f032_shares_diluted_cv_252d_base_v113_signal(shareswa):
    m = _mean(shareswa, 252).abs().replace(0, np.nan)
    s = _std(shareswa, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of shareswa
def sd_f032_shares_diluted_cv_504d_base_v114_signal(shareswa):
    m = _mean(shareswa, 504).abs().replace(0, np.nan)
    s = _std(shareswa, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged shareswa times closeadj
def sd_f032_shares_diluted_lag_5d_base_v115_signal(shareswa, closeadj):
    result = shareswa.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged shareswa times closeadj
def sd_f032_shares_diluted_lag_21d_base_v116_signal(shareswa, closeadj):
    result = shareswa.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged shareswa times closeadj
def sd_f032_shares_diluted_lag_63d_base_v117_signal(shareswa, closeadj):
    result = shareswa.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged shareswa times closeadj
def sd_f032_shares_diluted_lag_252d_base_v118_signal(shareswa, closeadj):
    result = shareswa.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(shareswa) / mean(shareswadil) x closeadj
def sd_f032_shares_diluted_cumper_shareswadil_252d_base_v119_signal(shareswa, shareswadil, closeadj):
    s = shareswa.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(shareswadil, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(shareswa) / mean(shareswadil) x closeadj
def sd_f032_shares_diluted_cumper_shareswadil_504d_base_v120_signal(shareswa, shareswadil, closeadj):
    s = shareswa.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(shareswadil, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(shareswa) / mean(sharesbas) x closeadj
def sd_f032_shares_diluted_cumper_sharesbas_252d_base_v121_signal(shareswa, sharesbas, closeadj):
    s = shareswa.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(shareswa) / mean(sharesbas) x closeadj
def sd_f032_shares_diluted_cumper_sharesbas_504d_base_v122_signal(shareswa, sharesbas, closeadj):
    s = shareswa.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only shareswa times closeadj
def sd_f032_shares_diluted_pos_63d_base_v123_signal(shareswa, closeadj):
    pos = shareswa.where(shareswa > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only shareswa times closeadj
def sd_f032_shares_diluted_pos_252d_base_v124_signal(shareswa, closeadj):
    pos = shareswa.where(shareswa > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only shareswa times closeadj
def sd_f032_shares_diluted_neg_63d_base_v125_signal(shareswa, closeadj):
    neg = shareswa.where(shareswa < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only shareswa times closeadj
def sd_f032_shares_diluted_neg_252d_base_v126_signal(shareswa, closeadj):
    neg = shareswa.where(shareswa < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of shareswa times closeadj
def sd_f032_shares_diluted_hl_21d_base_v127_signal(shareswa, closeadj):
    result = shareswa.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of shareswa times closeadj
def sd_f032_shares_diluted_hl_63d_base_v128_signal(shareswa, closeadj):
    result = shareswa.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of shareswa times closeadj
def sd_f032_shares_diluted_hl_252d_base_v129_signal(shareswa, closeadj):
    result = shareswa.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of shareswa
def sd_f032_shares_diluted_z_63d_base_v130_signal(shareswa):
    result = _z(shareswa, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of shareswa
def sd_f032_shares_diluted_z_126d_base_v131_signal(shareswa):
    result = _z(shareswa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of shareswa
def sd_f032_shares_diluted_z_1008d_base_v132_signal(shareswa):
    result = _z(shareswa, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of shareswa times closeadj
def sd_f032_shares_diluted_st_lt_252_21d_base_v133_signal(shareswa, closeadj):
    sm = _mean(shareswa, 21)
    lm = _mean(shareswa, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of shareswa times closeadj
def sd_f032_shares_diluted_st_lt_252_63d_base_v134_signal(shareswa, closeadj):
    sm = _mean(shareswa, 63)
    lm = _mean(shareswa, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of shareswa times closeadj
def sd_f032_shares_diluted_st_lt_504_21d_base_v135_signal(shareswa, closeadj):
    sm = _mean(shareswa, 21)
    lm = _mean(shareswa, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of shareswa times closeadj
def sd_f032_shares_diluted_st_lt_504_63d_base_v136_signal(shareswa, closeadj):
    sm = _mean(shareswa, 63)
    lm = _mean(shareswa, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged shareswa/shareswadil times closeadj
def sd_f032_shares_diluted_lag_per_shareswadil_21d_base_v137_signal(shareswa, shareswadil, closeadj):
    r = _shares_diluted_scaled(shareswa, shareswadil)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged shareswa/shareswadil times closeadj
def sd_f032_shares_diluted_lag_per_shareswadil_63d_base_v138_signal(shareswa, shareswadil, closeadj):
    r = _shares_diluted_scaled(shareswa, shareswadil)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged shareswa/shareswadil times closeadj
def sd_f032_shares_diluted_lag_per_shareswadil_252d_base_v139_signal(shareswa, shareswadil, closeadj):
    r = _shares_diluted_scaled(shareswa, shareswadil)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged shareswa/sharesbas times closeadj
def sd_f032_shares_diluted_lag_per_sharesbas_21d_base_v140_signal(shareswa, sharesbas, closeadj):
    r = _shares_diluted_scaled(shareswa, sharesbas)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged shareswa/sharesbas times closeadj
def sd_f032_shares_diluted_lag_per_sharesbas_63d_base_v141_signal(shareswa, sharesbas, closeadj):
    r = _shares_diluted_scaled(shareswa, sharesbas)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged shareswa/sharesbas times closeadj
def sd_f032_shares_diluted_lag_per_sharesbas_252d_base_v142_signal(shareswa, sharesbas, closeadj):
    r = _shares_diluted_scaled(shareswa, sharesbas)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |shareswa| times closeadj
def sd_f032_shares_diluted_abssum_63d_base_v143_signal(shareswa, closeadj):
    result = shareswa.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |shareswa| times closeadj
def sd_f032_shares_diluted_abssum_252d_base_v144_signal(shareswa, closeadj):
    result = shareswa.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |shareswa| times closeadj
def sd_f032_shares_diluted_abssum_504d_base_v145_signal(shareswa, closeadj):
    result = shareswa.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of shareswa
def sd_f032_shares_diluted_acf1_252d_base_v146_signal(shareswa):
    result = shareswa.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of shareswa
def sd_f032_shares_diluted_acf1_504d_base_v147_signal(shareswa):
    result = shareswa.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of shareswa
def sd_f032_shares_diluted_posinrange_252d_base_v148_signal(shareswa):
    m = _mean(shareswa, 252)
    hi = shareswa.rolling(252, min_periods=max(1, 252//2)).max()
    lo = shareswa.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of shareswa
def sd_f032_shares_diluted_posinrange_504d_base_v149_signal(shareswa):
    m = _mean(shareswa, 504)
    hi = shareswa.rolling(504, min_periods=max(1, 504//2)).max()
    lo = shareswa.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of shareswa times closeadj
def sd_f032_shares_diluted_hl_5d_base_v150_signal(shareswa, closeadj):
    result = shareswa.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
