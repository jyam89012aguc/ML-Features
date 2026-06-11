"""Family f065 - ROIC and invested capital returns (Returns and Efficiency) | Sharadar tables: SF1 | fields: roic, invcap, invcapavg | base 076-150"""
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
def _return_on_invested_capital_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_invested_capital_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_invested_capital_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of roic/invcapavg
def roic_f065_return_on_invested_capital_log_per_invcapavg_504d_base_v076_signal(roic, invcapavg):
    s = _return_on_invested_capital_scaled(roic, invcapavg)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roic/assets
def roic_f065_return_on_invested_capital_log_per_assets_252d_base_v077_signal(roic, assets):
    s = _return_on_invested_capital_scaled(roic, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of roic/assets
def roic_f065_return_on_invested_capital_log_per_assets_504d_base_v078_signal(roic, assets):
    s = _return_on_invested_capital_scaled(roic, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of roic times closeadj
def roic_f065_return_on_invested_capital_ewm_21d_base_v079_signal(roic, closeadj):
    result = roic.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of roic times closeadj
def roic_f065_return_on_invested_capital_ewm_63d_base_v080_signal(roic, closeadj):
    result = roic.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of roic times closeadj
def roic_f065_return_on_invested_capital_ewm_252d_base_v081_signal(roic, closeadj):
    result = roic.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of roic times closeadj
def roic_f065_return_on_invested_capital_med_63d_base_v082_signal(roic, closeadj):
    result = roic.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of roic times closeadj
def roic_f065_return_on_invested_capital_med_252d_base_v083_signal(roic, closeadj):
    result = roic.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of roic times closeadj
def roic_f065_return_on_invested_capital_med_504d_base_v084_signal(roic, closeadj):
    result = roic.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of roic
def roic_f065_return_on_invested_capital_skew_252d_base_v085_signal(roic):
    result = roic.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of roic
def roic_f065_return_on_invested_capital_skew_504d_base_v086_signal(roic):
    result = roic.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of roic
def roic_f065_return_on_invested_capital_kurt_252d_base_v087_signal(roic):
    result = roic.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of roic
def roic_f065_return_on_invested_capital_kurt_504d_base_v088_signal(roic):
    result = roic.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of roic times closeadj
def roic_f065_return_on_invested_capital_rank_252d_base_v089_signal(roic, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roic.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of roic times closeadj
def roic_f065_return_on_invested_capital_rank_504d_base_v090_signal(roic, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roic.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of roic times closeadj
def roic_f065_return_on_invested_capital_rank_1008d_base_v091_signal(roic, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = roic.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roic from 63d mean times closeadj
def roic_f065_return_on_invested_capital_devmean_63d_base_v092_signal(roic, closeadj):
    m = _mean(roic, 63)
    result = (roic - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roic from 252d mean times closeadj
def roic_f065_return_on_invested_capital_devmean_252d_base_v093_signal(roic, closeadj):
    m = _mean(roic, 252)
    result = (roic - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of roic from 504d mean times closeadj
def roic_f065_return_on_invested_capital_devmean_504d_base_v094_signal(roic, closeadj):
    m = _mean(roic, 504)
    result = (roic - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of roic times closeadj
def roic_f065_return_on_invested_capital_logdiff_21d_base_v095_signal(roic, closeadj):
    lr = _return_on_invested_capital_log(roic)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of roic times closeadj
def roic_f065_return_on_invested_capital_logdiff_63d_base_v096_signal(roic, closeadj):
    lr = _return_on_invested_capital_log(roic)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of roic times closeadj
def roic_f065_return_on_invested_capital_logdiff_252d_base_v097_signal(roic, closeadj):
    lr = _return_on_invested_capital_log(roic)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of roic times closeadj
def roic_f065_return_on_invested_capital_range_63d_base_v098_signal(roic, closeadj):
    hi = roic.rolling(63, min_periods=max(1, 63//2)).max()
    lo = roic.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of roic times closeadj
def roic_f065_return_on_invested_capital_range_252d_base_v099_signal(roic, closeadj):
    hi = roic.rolling(252, min_periods=max(1, 252//2)).max()
    lo = roic.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of roic times closeadj
def roic_f065_return_on_invested_capital_range_504d_base_v100_signal(roic, closeadj):
    hi = roic.rolling(504, min_periods=max(1, 504//2)).max()
    lo = roic.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 252d mean times closeadj
def roic_f065_return_on_invested_capital_rel_252d_base_v101_signal(roic, closeadj):
    m = _mean(roic, 252).replace(0, np.nan)
    result = (roic / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 504d mean times closeadj
def roic_f065_return_on_invested_capital_rel_504d_base_v102_signal(roic, closeadj):
    m = _mean(roic, 504).replace(0, np.nan)
    result = (roic / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 1008d mean times closeadj
def roic_f065_return_on_invested_capital_rel_1008d_base_v103_signal(roic, closeadj):
    m = _mean(roic, 1008).replace(0, np.nan)
    result = (roic / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roic/invcap 63d mean
def roic_f065_return_on_invested_capital_sqnorm_invcap_63d_base_v104_signal(roic, invcap):
    r = _return_on_invested_capital_scaled(roic, invcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roic/invcap 252d mean
def roic_f065_return_on_invested_capital_sqnorm_invcap_252d_base_v105_signal(roic, invcap):
    r = _return_on_invested_capital_scaled(roic, invcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roic/invcapavg 63d mean
def roic_f065_return_on_invested_capital_sqnorm_invcapavg_63d_base_v106_signal(roic, invcapavg):
    r = _return_on_invested_capital_scaled(roic, invcapavg)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roic/invcapavg 252d mean
def roic_f065_return_on_invested_capital_sqnorm_invcapavg_252d_base_v107_signal(roic, invcapavg):
    r = _return_on_invested_capital_scaled(roic, invcapavg)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roic/assets 63d mean
def roic_f065_return_on_invested_capital_sqnorm_assets_63d_base_v108_signal(roic, assets):
    r = _return_on_invested_capital_scaled(roic, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized roic/assets 252d mean
def roic_f065_return_on_invested_capital_sqnorm_assets_252d_base_v109_signal(roic, assets):
    r = _return_on_invested_capital_scaled(roic, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of roic times closeadj
def roic_f065_return_on_invested_capital_infrat_63d_base_v110_signal(roic, closeadj):
    m = _mean(roic, 63)
    s = _std(roic, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of roic times closeadj
def roic_f065_return_on_invested_capital_infrat_252d_base_v111_signal(roic, closeadj):
    m = _mean(roic, 252)
    s = _std(roic, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of roic times closeadj
def roic_f065_return_on_invested_capital_infrat_504d_base_v112_signal(roic, closeadj):
    m = _mean(roic, 504)
    s = _std(roic, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of roic
def roic_f065_return_on_invested_capital_cv_252d_base_v113_signal(roic):
    m = _mean(roic, 252).abs().replace(0, np.nan)
    s = _std(roic, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of roic
def roic_f065_return_on_invested_capital_cv_504d_base_v114_signal(roic):
    m = _mean(roic, 504).abs().replace(0, np.nan)
    s = _std(roic, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged roic times closeadj
def roic_f065_return_on_invested_capital_lag_5d_base_v115_signal(roic, closeadj):
    result = roic.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roic times closeadj
def roic_f065_return_on_invested_capital_lag_21d_base_v116_signal(roic, closeadj):
    result = roic.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roic times closeadj
def roic_f065_return_on_invested_capital_lag_63d_base_v117_signal(roic, closeadj):
    result = roic.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roic times closeadj
def roic_f065_return_on_invested_capital_lag_252d_base_v118_signal(roic, closeadj):
    result = roic.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(roic) / mean(invcap) x closeadj
def roic_f065_return_on_invested_capital_cumper_invcap_252d_base_v119_signal(roic, invcap, closeadj):
    s = roic.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(invcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(roic) / mean(invcap) x closeadj
def roic_f065_return_on_invested_capital_cumper_invcap_504d_base_v120_signal(roic, invcap, closeadj):
    s = roic.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(invcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(roic) / mean(invcapavg) x closeadj
def roic_f065_return_on_invested_capital_cumper_invcapavg_252d_base_v121_signal(roic, invcapavg, closeadj):
    s = roic.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(invcapavg, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(roic) / mean(invcapavg) x closeadj
def roic_f065_return_on_invested_capital_cumper_invcapavg_504d_base_v122_signal(roic, invcapavg, closeadj):
    s = roic.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(invcapavg, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only roic times closeadj
def roic_f065_return_on_invested_capital_pos_63d_base_v123_signal(roic, closeadj):
    pos = roic.where(roic > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only roic times closeadj
def roic_f065_return_on_invested_capital_pos_252d_base_v124_signal(roic, closeadj):
    pos = roic.where(roic > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only roic times closeadj
def roic_f065_return_on_invested_capital_neg_63d_base_v125_signal(roic, closeadj):
    neg = roic.where(roic < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only roic times closeadj
def roic_f065_return_on_invested_capital_neg_252d_base_v126_signal(roic, closeadj):
    neg = roic.where(roic < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of roic times closeadj
def roic_f065_return_on_invested_capital_hl_21d_base_v127_signal(roic, closeadj):
    result = roic.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of roic times closeadj
def roic_f065_return_on_invested_capital_hl_63d_base_v128_signal(roic, closeadj):
    result = roic.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of roic times closeadj
def roic_f065_return_on_invested_capital_hl_252d_base_v129_signal(roic, closeadj):
    result = roic.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of roic
def roic_f065_return_on_invested_capital_z_63d_base_v130_signal(roic):
    result = _z(roic, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of roic
def roic_f065_return_on_invested_capital_z_126d_base_v131_signal(roic):
    result = _z(roic, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of roic
def roic_f065_return_on_invested_capital_z_1008d_base_v132_signal(roic):
    result = _z(roic, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of roic times closeadj
def roic_f065_return_on_invested_capital_st_lt_252_21d_base_v133_signal(roic, closeadj):
    sm = _mean(roic, 21)
    lm = _mean(roic, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of roic times closeadj
def roic_f065_return_on_invested_capital_st_lt_252_63d_base_v134_signal(roic, closeadj):
    sm = _mean(roic, 63)
    lm = _mean(roic, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of roic times closeadj
def roic_f065_return_on_invested_capital_st_lt_504_21d_base_v135_signal(roic, closeadj):
    sm = _mean(roic, 21)
    lm = _mean(roic, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of roic times closeadj
def roic_f065_return_on_invested_capital_st_lt_504_63d_base_v136_signal(roic, closeadj):
    sm = _mean(roic, 63)
    lm = _mean(roic, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roic/invcap times closeadj
def roic_f065_return_on_invested_capital_lag_per_invcap_21d_base_v137_signal(roic, invcap, closeadj):
    r = _return_on_invested_capital_scaled(roic, invcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roic/invcap times closeadj
def roic_f065_return_on_invested_capital_lag_per_invcap_63d_base_v138_signal(roic, invcap, closeadj):
    r = _return_on_invested_capital_scaled(roic, invcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roic/invcap times closeadj
def roic_f065_return_on_invested_capital_lag_per_invcap_252d_base_v139_signal(roic, invcap, closeadj):
    r = _return_on_invested_capital_scaled(roic, invcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged roic/invcapavg times closeadj
def roic_f065_return_on_invested_capital_lag_per_invcapavg_21d_base_v140_signal(roic, invcapavg, closeadj):
    r = _return_on_invested_capital_scaled(roic, invcapavg)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged roic/invcapavg times closeadj
def roic_f065_return_on_invested_capital_lag_per_invcapavg_63d_base_v141_signal(roic, invcapavg, closeadj):
    r = _return_on_invested_capital_scaled(roic, invcapavg)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged roic/invcapavg times closeadj
def roic_f065_return_on_invested_capital_lag_per_invcapavg_252d_base_v142_signal(roic, invcapavg, closeadj):
    r = _return_on_invested_capital_scaled(roic, invcapavg)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |roic| times closeadj
def roic_f065_return_on_invested_capital_abssum_63d_base_v143_signal(roic, closeadj):
    result = roic.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |roic| times closeadj
def roic_f065_return_on_invested_capital_abssum_252d_base_v144_signal(roic, closeadj):
    result = roic.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |roic| times closeadj
def roic_f065_return_on_invested_capital_abssum_504d_base_v145_signal(roic, closeadj):
    result = roic.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of roic
def roic_f065_return_on_invested_capital_acf1_252d_base_v146_signal(roic):
    result = roic.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of roic
def roic_f065_return_on_invested_capital_acf1_504d_base_v147_signal(roic):
    result = roic.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of roic
def roic_f065_return_on_invested_capital_posinrange_252d_base_v148_signal(roic):
    m = _mean(roic, 252)
    hi = roic.rolling(252, min_periods=max(1, 252//2)).max()
    lo = roic.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of roic
def roic_f065_return_on_invested_capital_posinrange_504d_base_v149_signal(roic):
    m = _mean(roic, 504)
    hi = roic.rolling(504, min_periods=max(1, 504//2)).max()
    lo = roic.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of roic times closeadj
def roic_f065_return_on_invested_capital_hl_5d_base_v150_signal(roic, closeadj):
    result = roic.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
