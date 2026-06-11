"""Family f33 - Sharefactor / split continuity  (E_Dilution_Shares) | base 076-150"""
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
def _sharefactor_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sharefactor_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sharefactor_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sharefactor/marketcap
def sf_f33_sharefactor_log_per_marketcap_504d_base_v076_signal(sharefactor, marketcap):
    s = _sharefactor_scaled(sharefactor, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharefactor/equity
def sf_f33_sharefactor_log_per_equity_252d_base_v077_signal(sharefactor, equity):
    s = _sharefactor_scaled(sharefactor, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sharefactor/equity
def sf_f33_sharefactor_log_per_equity_504d_base_v078_signal(sharefactor, equity):
    s = _sharefactor_scaled(sharefactor, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sharefactor times closeadj
def sf_f33_sharefactor_ewm_21d_base_v079_signal(sharefactor, closeadj):
    result = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sharefactor times closeadj
def sf_f33_sharefactor_ewm_63d_base_v080_signal(sharefactor, closeadj):
    result = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sharefactor times closeadj
def sf_f33_sharefactor_ewm_252d_base_v081_signal(sharefactor, closeadj):
    result = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sharefactor times closeadj
def sf_f33_sharefactor_med_63d_base_v082_signal(sharefactor, closeadj):
    result = sharefactor.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sharefactor times closeadj
def sf_f33_sharefactor_med_252d_base_v083_signal(sharefactor, closeadj):
    result = sharefactor.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sharefactor times closeadj
def sf_f33_sharefactor_med_504d_base_v084_signal(sharefactor, closeadj):
    result = sharefactor.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sharefactor
def sf_f33_sharefactor_skew_252d_base_v085_signal(sharefactor):
    result = sharefactor.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sharefactor
def sf_f33_sharefactor_skew_504d_base_v086_signal(sharefactor):
    result = sharefactor.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sharefactor
def sf_f33_sharefactor_kurt_252d_base_v087_signal(sharefactor):
    result = sharefactor.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sharefactor
def sf_f33_sharefactor_kurt_504d_base_v088_signal(sharefactor):
    result = sharefactor.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sharefactor times closeadj
def sf_f33_sharefactor_rank_252d_base_v089_signal(sharefactor, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharefactor.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sharefactor times closeadj
def sf_f33_sharefactor_rank_504d_base_v090_signal(sharefactor, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharefactor.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sharefactor times closeadj
def sf_f33_sharefactor_rank_1008d_base_v091_signal(sharefactor, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharefactor.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharefactor from 63d mean times closeadj
def sf_f33_sharefactor_devmean_63d_base_v092_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 63)
    result = (sharefactor - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharefactor from 252d mean times closeadj
def sf_f33_sharefactor_devmean_252d_base_v093_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 252)
    result = (sharefactor - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharefactor from 504d mean times closeadj
def sf_f33_sharefactor_devmean_504d_base_v094_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 504)
    result = (sharefactor - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sharefactor times closeadj
def sf_f33_sharefactor_logdiff_21d_base_v095_signal(sharefactor, closeadj):
    lr = _sharefactor_log(sharefactor)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sharefactor times closeadj
def sf_f33_sharefactor_logdiff_63d_base_v096_signal(sharefactor, closeadj):
    lr = _sharefactor_log(sharefactor)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sharefactor times closeadj
def sf_f33_sharefactor_logdiff_252d_base_v097_signal(sharefactor, closeadj):
    lr = _sharefactor_log(sharefactor)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sharefactor times closeadj
def sf_f33_sharefactor_range_63d_base_v098_signal(sharefactor, closeadj):
    hi = sharefactor.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sharefactor.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sharefactor times closeadj
def sf_f33_sharefactor_range_252d_base_v099_signal(sharefactor, closeadj):
    hi = sharefactor.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sharefactor.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sharefactor times closeadj
def sf_f33_sharefactor_range_504d_base_v100_signal(sharefactor, closeadj):
    hi = sharefactor.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sharefactor.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharefactor relative to 252d mean times closeadj
def sf_f33_sharefactor_rel_252d_base_v101_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 252).replace(0, np.nan)
    result = (sharefactor / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharefactor relative to 504d mean times closeadj
def sf_f33_sharefactor_rel_504d_base_v102_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 504).replace(0, np.nan)
    result = (sharefactor / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharefactor relative to 1008d mean times closeadj
def sf_f33_sharefactor_rel_1008d_base_v103_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 1008).replace(0, np.nan)
    result = (sharefactor / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharefactor/assets 63d mean
def sf_f33_sharefactor_sqnorm_assets_63d_base_v104_signal(sharefactor, assets):
    r = _sharefactor_scaled(sharefactor, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharefactor/assets 252d mean
def sf_f33_sharefactor_sqnorm_assets_252d_base_v105_signal(sharefactor, assets):
    r = _sharefactor_scaled(sharefactor, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharefactor/marketcap 63d mean
def sf_f33_sharefactor_sqnorm_marketcap_63d_base_v106_signal(sharefactor, marketcap):
    r = _sharefactor_scaled(sharefactor, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharefactor/marketcap 252d mean
def sf_f33_sharefactor_sqnorm_marketcap_252d_base_v107_signal(sharefactor, marketcap):
    r = _sharefactor_scaled(sharefactor, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharefactor/equity 63d mean
def sf_f33_sharefactor_sqnorm_equity_63d_base_v108_signal(sharefactor, equity):
    r = _sharefactor_scaled(sharefactor, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharefactor/equity 252d mean
def sf_f33_sharefactor_sqnorm_equity_252d_base_v109_signal(sharefactor, equity):
    r = _sharefactor_scaled(sharefactor, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sharefactor times closeadj
def sf_f33_sharefactor_infrat_63d_base_v110_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 63)
    s = _std(sharefactor, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sharefactor times closeadj
def sf_f33_sharefactor_infrat_252d_base_v111_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 252)
    s = _std(sharefactor, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sharefactor times closeadj
def sf_f33_sharefactor_infrat_504d_base_v112_signal(sharefactor, closeadj):
    m = _mean(sharefactor, 504)
    s = _std(sharefactor, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sharefactor
def sf_f33_sharefactor_cv_252d_base_v113_signal(sharefactor):
    m = _mean(sharefactor, 252).abs().replace(0, np.nan)
    s = _std(sharefactor, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sharefactor
def sf_f33_sharefactor_cv_504d_base_v114_signal(sharefactor):
    m = _mean(sharefactor, 504).abs().replace(0, np.nan)
    s = _std(sharefactor, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sharefactor times closeadj
def sf_f33_sharefactor_lag_5d_base_v115_signal(sharefactor, closeadj):
    result = sharefactor.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharefactor times closeadj
def sf_f33_sharefactor_lag_21d_base_v116_signal(sharefactor, closeadj):
    result = sharefactor.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharefactor times closeadj
def sf_f33_sharefactor_lag_63d_base_v117_signal(sharefactor, closeadj):
    result = sharefactor.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharefactor times closeadj
def sf_f33_sharefactor_lag_252d_base_v118_signal(sharefactor, closeadj):
    result = sharefactor.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sharefactor) / mean(assets) x closeadj
def sf_f33_sharefactor_cumper_assets_252d_base_v119_signal(sharefactor, assets, closeadj):
    s = sharefactor.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sharefactor) / mean(assets) x closeadj
def sf_f33_sharefactor_cumper_assets_504d_base_v120_signal(sharefactor, assets, closeadj):
    s = sharefactor.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sharefactor) / mean(marketcap) x closeadj
def sf_f33_sharefactor_cumper_marketcap_252d_base_v121_signal(sharefactor, marketcap, closeadj):
    s = sharefactor.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sharefactor) / mean(marketcap) x closeadj
def sf_f33_sharefactor_cumper_marketcap_504d_base_v122_signal(sharefactor, marketcap, closeadj):
    s = sharefactor.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sharefactor times closeadj
def sf_f33_sharefactor_pos_63d_base_v123_signal(sharefactor, closeadj):
    pos = sharefactor.where(sharefactor > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sharefactor times closeadj
def sf_f33_sharefactor_pos_252d_base_v124_signal(sharefactor, closeadj):
    pos = sharefactor.where(sharefactor > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sharefactor times closeadj
def sf_f33_sharefactor_neg_63d_base_v125_signal(sharefactor, closeadj):
    neg = sharefactor.where(sharefactor < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sharefactor times closeadj
def sf_f33_sharefactor_neg_252d_base_v126_signal(sharefactor, closeadj):
    neg = sharefactor.where(sharefactor < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sharefactor times closeadj
def sf_f33_sharefactor_hl_21d_base_v127_signal(sharefactor, closeadj):
    result = sharefactor.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sharefactor times closeadj
def sf_f33_sharefactor_hl_63d_base_v128_signal(sharefactor, closeadj):
    result = sharefactor.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sharefactor times closeadj
def sf_f33_sharefactor_hl_252d_base_v129_signal(sharefactor, closeadj):
    result = sharefactor.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sharefactor
def sf_f33_sharefactor_z_63d_base_v130_signal(sharefactor):
    result = _z(sharefactor, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sharefactor
def sf_f33_sharefactor_z_126d_base_v131_signal(sharefactor):
    result = _z(sharefactor, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sharefactor
def sf_f33_sharefactor_z_1008d_base_v132_signal(sharefactor):
    result = _z(sharefactor, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sharefactor times closeadj
def sf_f33_sharefactor_st_lt_252_21d_base_v133_signal(sharefactor, closeadj):
    sm = _mean(sharefactor, 21)
    lm = _mean(sharefactor, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sharefactor times closeadj
def sf_f33_sharefactor_st_lt_252_63d_base_v134_signal(sharefactor, closeadj):
    sm = _mean(sharefactor, 63)
    lm = _mean(sharefactor, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sharefactor times closeadj
def sf_f33_sharefactor_st_lt_504_21d_base_v135_signal(sharefactor, closeadj):
    sm = _mean(sharefactor, 21)
    lm = _mean(sharefactor, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sharefactor times closeadj
def sf_f33_sharefactor_st_lt_504_63d_base_v136_signal(sharefactor, closeadj):
    sm = _mean(sharefactor, 63)
    lm = _mean(sharefactor, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharefactor/assets times closeadj
def sf_f33_sharefactor_lag_per_assets_21d_base_v137_signal(sharefactor, assets, closeadj):
    r = _sharefactor_scaled(sharefactor, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharefactor/assets times closeadj
def sf_f33_sharefactor_lag_per_assets_63d_base_v138_signal(sharefactor, assets, closeadj):
    r = _sharefactor_scaled(sharefactor, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharefactor/assets times closeadj
def sf_f33_sharefactor_lag_per_assets_252d_base_v139_signal(sharefactor, assets, closeadj):
    r = _sharefactor_scaled(sharefactor, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharefactor/marketcap times closeadj
def sf_f33_sharefactor_lag_per_marketcap_21d_base_v140_signal(sharefactor, marketcap, closeadj):
    r = _sharefactor_scaled(sharefactor, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharefactor/marketcap times closeadj
def sf_f33_sharefactor_lag_per_marketcap_63d_base_v141_signal(sharefactor, marketcap, closeadj):
    r = _sharefactor_scaled(sharefactor, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharefactor/marketcap times closeadj
def sf_f33_sharefactor_lag_per_marketcap_252d_base_v142_signal(sharefactor, marketcap, closeadj):
    r = _sharefactor_scaled(sharefactor, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sharefactor| times closeadj
def sf_f33_sharefactor_abssum_63d_base_v143_signal(sharefactor, closeadj):
    result = sharefactor.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sharefactor| times closeadj
def sf_f33_sharefactor_abssum_252d_base_v144_signal(sharefactor, closeadj):
    result = sharefactor.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sharefactor| times closeadj
def sf_f33_sharefactor_abssum_504d_base_v145_signal(sharefactor, closeadj):
    result = sharefactor.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sharefactor
def sf_f33_sharefactor_acf1_252d_base_v146_signal(sharefactor):
    result = sharefactor.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sharefactor
def sf_f33_sharefactor_acf1_504d_base_v147_signal(sharefactor):
    result = sharefactor.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sharefactor
def sf_f33_sharefactor_posinrange_252d_base_v148_signal(sharefactor):
    m = _mean(sharefactor, 252)
    hi = sharefactor.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sharefactor.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sharefactor
def sf_f33_sharefactor_posinrange_504d_base_v149_signal(sharefactor):
    m = _mean(sharefactor, 504)
    hi = sharefactor.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sharefactor.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sharefactor times closeadj
def sf_f33_sharefactor_hl_5d_base_v150_signal(sharefactor, closeadj):
    result = sharefactor.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
