"""Family f11 - Burn acceleration  (B_CashFlow_Burn) | base 076-150"""
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
def _burn_acceleration_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _burn_acceleration_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _burn_acceleration_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of ncfo/marketcap
def ba_f11_burn_acceleration_log_per_marketcap_504d_base_v076_signal(ncfo, marketcap):
    s = _burn_acceleration_scaled(ncfo, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfo/equity
def ba_f11_burn_acceleration_log_per_equity_252d_base_v077_signal(ncfo, equity):
    s = _burn_acceleration_scaled(ncfo, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncfo/equity
def ba_f11_burn_acceleration_log_per_equity_504d_base_v078_signal(ncfo, equity):
    s = _burn_acceleration_scaled(ncfo, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of ncfo times closeadj
def ba_f11_burn_acceleration_ewm_21d_base_v079_signal(ncfo, closeadj):
    result = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of ncfo times closeadj
def ba_f11_burn_acceleration_ewm_63d_base_v080_signal(ncfo, closeadj):
    result = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of ncfo times closeadj
def ba_f11_burn_acceleration_ewm_252d_base_v081_signal(ncfo, closeadj):
    result = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of ncfo times closeadj
def ba_f11_burn_acceleration_med_63d_base_v082_signal(ncfo, closeadj):
    result = ncfo.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of ncfo times closeadj
def ba_f11_burn_acceleration_med_252d_base_v083_signal(ncfo, closeadj):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of ncfo times closeadj
def ba_f11_burn_acceleration_med_504d_base_v084_signal(ncfo, closeadj):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of ncfo
def ba_f11_burn_acceleration_skew_252d_base_v085_signal(ncfo):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of ncfo
def ba_f11_burn_acceleration_skew_504d_base_v086_signal(ncfo):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of ncfo
def ba_f11_burn_acceleration_kurt_252d_base_v087_signal(ncfo):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of ncfo
def ba_f11_burn_acceleration_kurt_504d_base_v088_signal(ncfo):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ncfo times closeadj
def ba_f11_burn_acceleration_rank_252d_base_v089_signal(ncfo, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ncfo times closeadj
def ba_f11_burn_acceleration_rank_504d_base_v090_signal(ncfo, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of ncfo times closeadj
def ba_f11_burn_acceleration_rank_1008d_base_v091_signal(ncfo, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = ncfo.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfo from 63d mean times closeadj
def ba_f11_burn_acceleration_devmean_63d_base_v092_signal(ncfo, closeadj):
    m = _mean(ncfo, 63)
    result = (ncfo - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfo from 252d mean times closeadj
def ba_f11_burn_acceleration_devmean_252d_base_v093_signal(ncfo, closeadj):
    m = _mean(ncfo, 252)
    result = (ncfo - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of ncfo from 504d mean times closeadj
def ba_f11_burn_acceleration_devmean_504d_base_v094_signal(ncfo, closeadj):
    m = _mean(ncfo, 504)
    result = (ncfo - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of ncfo times closeadj
def ba_f11_burn_acceleration_logdiff_21d_base_v095_signal(ncfo, closeadj):
    lr = _burn_acceleration_log(ncfo)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of ncfo times closeadj
def ba_f11_burn_acceleration_logdiff_63d_base_v096_signal(ncfo, closeadj):
    lr = _burn_acceleration_log(ncfo)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of ncfo times closeadj
def ba_f11_burn_acceleration_logdiff_252d_base_v097_signal(ncfo, closeadj):
    lr = _burn_acceleration_log(ncfo)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of ncfo times closeadj
def ba_f11_burn_acceleration_range_63d_base_v098_signal(ncfo, closeadj):
    hi = ncfo.rolling(63, min_periods=max(1, 63//2)).max()
    lo = ncfo.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of ncfo times closeadj
def ba_f11_burn_acceleration_range_252d_base_v099_signal(ncfo, closeadj):
    hi = ncfo.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncfo.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of ncfo times closeadj
def ba_f11_burn_acceleration_range_504d_base_v100_signal(ncfo, closeadj):
    hi = ncfo.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncfo.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 252d mean times closeadj
def ba_f11_burn_acceleration_rel_252d_base_v101_signal(ncfo, closeadj):
    m = _mean(ncfo, 252).replace(0, np.nan)
    result = (ncfo / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 504d mean times closeadj
def ba_f11_burn_acceleration_rel_504d_base_v102_signal(ncfo, closeadj):
    m = _mean(ncfo, 504).replace(0, np.nan)
    result = (ncfo / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 1008d mean times closeadj
def ba_f11_burn_acceleration_rel_1008d_base_v103_signal(ncfo, closeadj):
    m = _mean(ncfo, 1008).replace(0, np.nan)
    result = (ncfo / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/assets 63d mean
def ba_f11_burn_acceleration_sqnorm_assets_63d_base_v104_signal(ncfo, assets):
    r = _burn_acceleration_scaled(ncfo, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/assets 252d mean
def ba_f11_burn_acceleration_sqnorm_assets_252d_base_v105_signal(ncfo, assets):
    r = _burn_acceleration_scaled(ncfo, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/marketcap 63d mean
def ba_f11_burn_acceleration_sqnorm_marketcap_63d_base_v106_signal(ncfo, marketcap):
    r = _burn_acceleration_scaled(ncfo, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/marketcap 252d mean
def ba_f11_burn_acceleration_sqnorm_marketcap_252d_base_v107_signal(ncfo, marketcap):
    r = _burn_acceleration_scaled(ncfo, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/equity 63d mean
def ba_f11_burn_acceleration_sqnorm_equity_63d_base_v108_signal(ncfo, equity):
    r = _burn_acceleration_scaled(ncfo, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized ncfo/equity 252d mean
def ba_f11_burn_acceleration_sqnorm_equity_252d_base_v109_signal(ncfo, equity):
    r = _burn_acceleration_scaled(ncfo, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of ncfo times closeadj
def ba_f11_burn_acceleration_infrat_63d_base_v110_signal(ncfo, closeadj):
    m = _mean(ncfo, 63)
    s = _std(ncfo, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of ncfo times closeadj
def ba_f11_burn_acceleration_infrat_252d_base_v111_signal(ncfo, closeadj):
    m = _mean(ncfo, 252)
    s = _std(ncfo, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of ncfo times closeadj
def ba_f11_burn_acceleration_infrat_504d_base_v112_signal(ncfo, closeadj):
    m = _mean(ncfo, 504)
    s = _std(ncfo, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of ncfo
def ba_f11_burn_acceleration_cv_252d_base_v113_signal(ncfo):
    m = _mean(ncfo, 252).abs().replace(0, np.nan)
    s = _std(ncfo, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of ncfo
def ba_f11_burn_acceleration_cv_504d_base_v114_signal(ncfo):
    m = _mean(ncfo, 504).abs().replace(0, np.nan)
    s = _std(ncfo, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged ncfo times closeadj
def ba_f11_burn_acceleration_lag_5d_base_v115_signal(ncfo, closeadj):
    result = ncfo.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfo times closeadj
def ba_f11_burn_acceleration_lag_21d_base_v116_signal(ncfo, closeadj):
    result = ncfo.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfo times closeadj
def ba_f11_burn_acceleration_lag_63d_base_v117_signal(ncfo, closeadj):
    result = ncfo.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfo times closeadj
def ba_f11_burn_acceleration_lag_252d_base_v118_signal(ncfo, closeadj):
    result = ncfo.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncfo) / mean(assets) x closeadj
def ba_f11_burn_acceleration_cumper_assets_252d_base_v119_signal(ncfo, assets, closeadj):
    s = ncfo.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncfo) / mean(assets) x closeadj
def ba_f11_burn_acceleration_cumper_assets_504d_base_v120_signal(ncfo, assets, closeadj):
    s = ncfo.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(ncfo) / mean(marketcap) x closeadj
def ba_f11_burn_acceleration_cumper_marketcap_252d_base_v121_signal(ncfo, marketcap, closeadj):
    s = ncfo.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(ncfo) / mean(marketcap) x closeadj
def ba_f11_burn_acceleration_cumper_marketcap_504d_base_v122_signal(ncfo, marketcap, closeadj):
    s = ncfo.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only ncfo times closeadj
def ba_f11_burn_acceleration_pos_63d_base_v123_signal(ncfo, closeadj):
    pos = ncfo.where(ncfo > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only ncfo times closeadj
def ba_f11_burn_acceleration_pos_252d_base_v124_signal(ncfo, closeadj):
    pos = ncfo.where(ncfo > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only ncfo times closeadj
def ba_f11_burn_acceleration_neg_63d_base_v125_signal(ncfo, closeadj):
    neg = ncfo.where(ncfo < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only ncfo times closeadj
def ba_f11_burn_acceleration_neg_252d_base_v126_signal(ncfo, closeadj):
    neg = ncfo.where(ncfo < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of ncfo times closeadj
def ba_f11_burn_acceleration_hl_21d_base_v127_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of ncfo times closeadj
def ba_f11_burn_acceleration_hl_63d_base_v128_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of ncfo times closeadj
def ba_f11_burn_acceleration_hl_252d_base_v129_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of ncfo
def ba_f11_burn_acceleration_z_63d_base_v130_signal(ncfo):
    result = _z(ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of ncfo
def ba_f11_burn_acceleration_z_126d_base_v131_signal(ncfo):
    result = _z(ncfo, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of ncfo
def ba_f11_burn_acceleration_z_1008d_base_v132_signal(ncfo):
    result = _z(ncfo, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of ncfo times closeadj
def ba_f11_burn_acceleration_st_lt_252_21d_base_v133_signal(ncfo, closeadj):
    sm = _mean(ncfo, 21)
    lm = _mean(ncfo, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of ncfo times closeadj
def ba_f11_burn_acceleration_st_lt_252_63d_base_v134_signal(ncfo, closeadj):
    sm = _mean(ncfo, 63)
    lm = _mean(ncfo, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of ncfo times closeadj
def ba_f11_burn_acceleration_st_lt_504_21d_base_v135_signal(ncfo, closeadj):
    sm = _mean(ncfo, 21)
    lm = _mean(ncfo, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of ncfo times closeadj
def ba_f11_burn_acceleration_st_lt_504_63d_base_v136_signal(ncfo, closeadj):
    sm = _mean(ncfo, 63)
    lm = _mean(ncfo, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfo/assets times closeadj
def ba_f11_burn_acceleration_lag_per_assets_21d_base_v137_signal(ncfo, assets, closeadj):
    r = _burn_acceleration_scaled(ncfo, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfo/assets times closeadj
def ba_f11_burn_acceleration_lag_per_assets_63d_base_v138_signal(ncfo, assets, closeadj):
    r = _burn_acceleration_scaled(ncfo, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfo/assets times closeadj
def ba_f11_burn_acceleration_lag_per_assets_252d_base_v139_signal(ncfo, assets, closeadj):
    r = _burn_acceleration_scaled(ncfo, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged ncfo/marketcap times closeadj
def ba_f11_burn_acceleration_lag_per_marketcap_21d_base_v140_signal(ncfo, marketcap, closeadj):
    r = _burn_acceleration_scaled(ncfo, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged ncfo/marketcap times closeadj
def ba_f11_burn_acceleration_lag_per_marketcap_63d_base_v141_signal(ncfo, marketcap, closeadj):
    r = _burn_acceleration_scaled(ncfo, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged ncfo/marketcap times closeadj
def ba_f11_burn_acceleration_lag_per_marketcap_252d_base_v142_signal(ncfo, marketcap, closeadj):
    r = _burn_acceleration_scaled(ncfo, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |ncfo| times closeadj
def ba_f11_burn_acceleration_abssum_63d_base_v143_signal(ncfo, closeadj):
    result = ncfo.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |ncfo| times closeadj
def ba_f11_burn_acceleration_abssum_252d_base_v144_signal(ncfo, closeadj):
    result = ncfo.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |ncfo| times closeadj
def ba_f11_burn_acceleration_abssum_504d_base_v145_signal(ncfo, closeadj):
    result = ncfo.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of ncfo
def ba_f11_burn_acceleration_acf1_252d_base_v146_signal(ncfo):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of ncfo
def ba_f11_burn_acceleration_acf1_504d_base_v147_signal(ncfo):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of ncfo
def ba_f11_burn_acceleration_posinrange_252d_base_v148_signal(ncfo):
    m = _mean(ncfo, 252)
    hi = ncfo.rolling(252, min_periods=max(1, 252//2)).max()
    lo = ncfo.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of ncfo
def ba_f11_burn_acceleration_posinrange_504d_base_v149_signal(ncfo):
    m = _mean(ncfo, 504)
    hi = ncfo.rolling(504, min_periods=max(1, 504//2)).max()
    lo = ncfo.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of ncfo times closeadj
def ba_f11_burn_acceleration_hl_5d_base_v150_signal(ncfo, closeadj):
    result = ncfo.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
