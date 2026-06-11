"""Family f05 - Current ratio & trend  (A_Liquidity_Runway) | base 076-150"""
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
def _current_ratio_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _current_ratio_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _current_ratio_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of currentratio/marketcap
def cur_f05_current_ratio_log_per_marketcap_504d_base_v076_signal(currentratio, marketcap):
    s = _current_ratio_scaled(currentratio, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of currentratio/equity
def cur_f05_current_ratio_log_per_equity_252d_base_v077_signal(currentratio, equity):
    s = _current_ratio_scaled(currentratio, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of currentratio/equity
def cur_f05_current_ratio_log_per_equity_504d_base_v078_signal(currentratio, equity):
    s = _current_ratio_scaled(currentratio, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of currentratio times closeadj
def cur_f05_current_ratio_ewm_21d_base_v079_signal(currentratio, closeadj):
    result = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of currentratio times closeadj
def cur_f05_current_ratio_ewm_63d_base_v080_signal(currentratio, closeadj):
    result = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of currentratio times closeadj
def cur_f05_current_ratio_ewm_252d_base_v081_signal(currentratio, closeadj):
    result = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of currentratio times closeadj
def cur_f05_current_ratio_med_63d_base_v082_signal(currentratio, closeadj):
    result = currentratio.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of currentratio times closeadj
def cur_f05_current_ratio_med_252d_base_v083_signal(currentratio, closeadj):
    result = currentratio.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of currentratio times closeadj
def cur_f05_current_ratio_med_504d_base_v084_signal(currentratio, closeadj):
    result = currentratio.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of currentratio
def cur_f05_current_ratio_skew_252d_base_v085_signal(currentratio):
    result = currentratio.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of currentratio
def cur_f05_current_ratio_skew_504d_base_v086_signal(currentratio):
    result = currentratio.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of currentratio
def cur_f05_current_ratio_kurt_252d_base_v087_signal(currentratio):
    result = currentratio.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of currentratio
def cur_f05_current_ratio_kurt_504d_base_v088_signal(currentratio):
    result = currentratio.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of currentratio times closeadj
def cur_f05_current_ratio_rank_252d_base_v089_signal(currentratio, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = currentratio.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of currentratio times closeadj
def cur_f05_current_ratio_rank_504d_base_v090_signal(currentratio, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = currentratio.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of currentratio times closeadj
def cur_f05_current_ratio_rank_1008d_base_v091_signal(currentratio, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = currentratio.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of currentratio from 63d mean times closeadj
def cur_f05_current_ratio_devmean_63d_base_v092_signal(currentratio, closeadj):
    m = _mean(currentratio, 63)
    result = (currentratio - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of currentratio from 252d mean times closeadj
def cur_f05_current_ratio_devmean_252d_base_v093_signal(currentratio, closeadj):
    m = _mean(currentratio, 252)
    result = (currentratio - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of currentratio from 504d mean times closeadj
def cur_f05_current_ratio_devmean_504d_base_v094_signal(currentratio, closeadj):
    m = _mean(currentratio, 504)
    result = (currentratio - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of currentratio times closeadj
def cur_f05_current_ratio_logdiff_21d_base_v095_signal(currentratio, closeadj):
    lr = _current_ratio_log(currentratio)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of currentratio times closeadj
def cur_f05_current_ratio_logdiff_63d_base_v096_signal(currentratio, closeadj):
    lr = _current_ratio_log(currentratio)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of currentratio times closeadj
def cur_f05_current_ratio_logdiff_252d_base_v097_signal(currentratio, closeadj):
    lr = _current_ratio_log(currentratio)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of currentratio times closeadj
def cur_f05_current_ratio_range_63d_base_v098_signal(currentratio, closeadj):
    hi = currentratio.rolling(63, min_periods=max(1, 63//2)).max()
    lo = currentratio.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of currentratio times closeadj
def cur_f05_current_ratio_range_252d_base_v099_signal(currentratio, closeadj):
    hi = currentratio.rolling(252, min_periods=max(1, 252//2)).max()
    lo = currentratio.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of currentratio times closeadj
def cur_f05_current_ratio_range_504d_base_v100_signal(currentratio, closeadj):
    hi = currentratio.rolling(504, min_periods=max(1, 504//2)).max()
    lo = currentratio.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 252d mean times closeadj
def cur_f05_current_ratio_rel_252d_base_v101_signal(currentratio, closeadj):
    m = _mean(currentratio, 252).replace(0, np.nan)
    result = (currentratio / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 504d mean times closeadj
def cur_f05_current_ratio_rel_504d_base_v102_signal(currentratio, closeadj):
    m = _mean(currentratio, 504).replace(0, np.nan)
    result = (currentratio / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 1008d mean times closeadj
def cur_f05_current_ratio_rel_1008d_base_v103_signal(currentratio, closeadj):
    m = _mean(currentratio, 1008).replace(0, np.nan)
    result = (currentratio / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized currentratio/assets 63d mean
def cur_f05_current_ratio_sqnorm_assets_63d_base_v104_signal(currentratio, assets):
    r = _current_ratio_scaled(currentratio, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized currentratio/assets 252d mean
def cur_f05_current_ratio_sqnorm_assets_252d_base_v105_signal(currentratio, assets):
    r = _current_ratio_scaled(currentratio, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized currentratio/marketcap 63d mean
def cur_f05_current_ratio_sqnorm_marketcap_63d_base_v106_signal(currentratio, marketcap):
    r = _current_ratio_scaled(currentratio, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized currentratio/marketcap 252d mean
def cur_f05_current_ratio_sqnorm_marketcap_252d_base_v107_signal(currentratio, marketcap):
    r = _current_ratio_scaled(currentratio, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized currentratio/equity 63d mean
def cur_f05_current_ratio_sqnorm_equity_63d_base_v108_signal(currentratio, equity):
    r = _current_ratio_scaled(currentratio, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized currentratio/equity 252d mean
def cur_f05_current_ratio_sqnorm_equity_252d_base_v109_signal(currentratio, equity):
    r = _current_ratio_scaled(currentratio, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of currentratio times closeadj
def cur_f05_current_ratio_infrat_63d_base_v110_signal(currentratio, closeadj):
    m = _mean(currentratio, 63)
    s = _std(currentratio, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of currentratio times closeadj
def cur_f05_current_ratio_infrat_252d_base_v111_signal(currentratio, closeadj):
    m = _mean(currentratio, 252)
    s = _std(currentratio, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of currentratio times closeadj
def cur_f05_current_ratio_infrat_504d_base_v112_signal(currentratio, closeadj):
    m = _mean(currentratio, 504)
    s = _std(currentratio, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of currentratio
def cur_f05_current_ratio_cv_252d_base_v113_signal(currentratio):
    m = _mean(currentratio, 252).abs().replace(0, np.nan)
    s = _std(currentratio, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of currentratio
def cur_f05_current_ratio_cv_504d_base_v114_signal(currentratio):
    m = _mean(currentratio, 504).abs().replace(0, np.nan)
    s = _std(currentratio, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged currentratio times closeadj
def cur_f05_current_ratio_lag_5d_base_v115_signal(currentratio, closeadj):
    result = currentratio.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged currentratio times closeadj
def cur_f05_current_ratio_lag_21d_base_v116_signal(currentratio, closeadj):
    result = currentratio.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged currentratio times closeadj
def cur_f05_current_ratio_lag_63d_base_v117_signal(currentratio, closeadj):
    result = currentratio.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged currentratio times closeadj
def cur_f05_current_ratio_lag_252d_base_v118_signal(currentratio, closeadj):
    result = currentratio.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(currentratio) / mean(assets) x closeadj
def cur_f05_current_ratio_cumper_assets_252d_base_v119_signal(currentratio, assets, closeadj):
    s = currentratio.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(currentratio) / mean(assets) x closeadj
def cur_f05_current_ratio_cumper_assets_504d_base_v120_signal(currentratio, assets, closeadj):
    s = currentratio.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(currentratio) / mean(marketcap) x closeadj
def cur_f05_current_ratio_cumper_marketcap_252d_base_v121_signal(currentratio, marketcap, closeadj):
    s = currentratio.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(currentratio) / mean(marketcap) x closeadj
def cur_f05_current_ratio_cumper_marketcap_504d_base_v122_signal(currentratio, marketcap, closeadj):
    s = currentratio.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only currentratio times closeadj
def cur_f05_current_ratio_pos_63d_base_v123_signal(currentratio, closeadj):
    pos = currentratio.where(currentratio > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only currentratio times closeadj
def cur_f05_current_ratio_pos_252d_base_v124_signal(currentratio, closeadj):
    pos = currentratio.where(currentratio > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only currentratio times closeadj
def cur_f05_current_ratio_neg_63d_base_v125_signal(currentratio, closeadj):
    neg = currentratio.where(currentratio < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only currentratio times closeadj
def cur_f05_current_ratio_neg_252d_base_v126_signal(currentratio, closeadj):
    neg = currentratio.where(currentratio < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of currentratio times closeadj
def cur_f05_current_ratio_hl_21d_base_v127_signal(currentratio, closeadj):
    result = currentratio.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of currentratio times closeadj
def cur_f05_current_ratio_hl_63d_base_v128_signal(currentratio, closeadj):
    result = currentratio.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of currentratio times closeadj
def cur_f05_current_ratio_hl_252d_base_v129_signal(currentratio, closeadj):
    result = currentratio.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of currentratio
def cur_f05_current_ratio_z_63d_base_v130_signal(currentratio):
    result = _z(currentratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of currentratio
def cur_f05_current_ratio_z_126d_base_v131_signal(currentratio):
    result = _z(currentratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of currentratio
def cur_f05_current_ratio_z_1008d_base_v132_signal(currentratio):
    result = _z(currentratio, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of currentratio times closeadj
def cur_f05_current_ratio_st_lt_252_21d_base_v133_signal(currentratio, closeadj):
    sm = _mean(currentratio, 21)
    lm = _mean(currentratio, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of currentratio times closeadj
def cur_f05_current_ratio_st_lt_252_63d_base_v134_signal(currentratio, closeadj):
    sm = _mean(currentratio, 63)
    lm = _mean(currentratio, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of currentratio times closeadj
def cur_f05_current_ratio_st_lt_504_21d_base_v135_signal(currentratio, closeadj):
    sm = _mean(currentratio, 21)
    lm = _mean(currentratio, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of currentratio times closeadj
def cur_f05_current_ratio_st_lt_504_63d_base_v136_signal(currentratio, closeadj):
    sm = _mean(currentratio, 63)
    lm = _mean(currentratio, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged currentratio/assets times closeadj
def cur_f05_current_ratio_lag_per_assets_21d_base_v137_signal(currentratio, assets, closeadj):
    r = _current_ratio_scaled(currentratio, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged currentratio/assets times closeadj
def cur_f05_current_ratio_lag_per_assets_63d_base_v138_signal(currentratio, assets, closeadj):
    r = _current_ratio_scaled(currentratio, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged currentratio/assets times closeadj
def cur_f05_current_ratio_lag_per_assets_252d_base_v139_signal(currentratio, assets, closeadj):
    r = _current_ratio_scaled(currentratio, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged currentratio/marketcap times closeadj
def cur_f05_current_ratio_lag_per_marketcap_21d_base_v140_signal(currentratio, marketcap, closeadj):
    r = _current_ratio_scaled(currentratio, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged currentratio/marketcap times closeadj
def cur_f05_current_ratio_lag_per_marketcap_63d_base_v141_signal(currentratio, marketcap, closeadj):
    r = _current_ratio_scaled(currentratio, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged currentratio/marketcap times closeadj
def cur_f05_current_ratio_lag_per_marketcap_252d_base_v142_signal(currentratio, marketcap, closeadj):
    r = _current_ratio_scaled(currentratio, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |currentratio| times closeadj
def cur_f05_current_ratio_abssum_63d_base_v143_signal(currentratio, closeadj):
    result = currentratio.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |currentratio| times closeadj
def cur_f05_current_ratio_abssum_252d_base_v144_signal(currentratio, closeadj):
    result = currentratio.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |currentratio| times closeadj
def cur_f05_current_ratio_abssum_504d_base_v145_signal(currentratio, closeadj):
    result = currentratio.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of currentratio
def cur_f05_current_ratio_acf1_252d_base_v146_signal(currentratio):
    result = currentratio.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of currentratio
def cur_f05_current_ratio_acf1_504d_base_v147_signal(currentratio):
    result = currentratio.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of currentratio
def cur_f05_current_ratio_posinrange_252d_base_v148_signal(currentratio):
    m = _mean(currentratio, 252)
    hi = currentratio.rolling(252, min_periods=max(1, 252//2)).max()
    lo = currentratio.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of currentratio
def cur_f05_current_ratio_posinrange_504d_base_v149_signal(currentratio):
    m = _mean(currentratio, 504)
    hi = currentratio.rolling(504, min_periods=max(1, 504//2)).max()
    lo = currentratio.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of currentratio times closeadj
def cur_f05_current_ratio_hl_5d_base_v150_signal(currentratio, closeadj):
    result = currentratio.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
