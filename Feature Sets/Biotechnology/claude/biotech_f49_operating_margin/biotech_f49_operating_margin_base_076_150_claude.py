"""Family f49 - Operating margin  (H_Margins) | base 076-150"""
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
def _operating_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _operating_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _operating_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of opinc/marketcap
def om_f49_operating_margin_log_per_marketcap_504d_base_v076_signal(opinc, marketcap):
    s = _operating_margin_scaled(opinc, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of opinc/equity
def om_f49_operating_margin_log_per_equity_252d_base_v077_signal(opinc, equity):
    s = _operating_margin_scaled(opinc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of opinc/equity
def om_f49_operating_margin_log_per_equity_504d_base_v078_signal(opinc, equity):
    s = _operating_margin_scaled(opinc, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of opinc times closeadj
def om_f49_operating_margin_ewm_21d_base_v079_signal(opinc, closeadj):
    result = opinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of opinc times closeadj
def om_f49_operating_margin_ewm_63d_base_v080_signal(opinc, closeadj):
    result = opinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of opinc times closeadj
def om_f49_operating_margin_ewm_252d_base_v081_signal(opinc, closeadj):
    result = opinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of opinc times closeadj
def om_f49_operating_margin_med_63d_base_v082_signal(opinc, closeadj):
    result = opinc.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of opinc times closeadj
def om_f49_operating_margin_med_252d_base_v083_signal(opinc, closeadj):
    result = opinc.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of opinc times closeadj
def om_f49_operating_margin_med_504d_base_v084_signal(opinc, closeadj):
    result = opinc.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of opinc
def om_f49_operating_margin_skew_252d_base_v085_signal(opinc):
    result = opinc.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of opinc
def om_f49_operating_margin_skew_504d_base_v086_signal(opinc):
    result = opinc.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of opinc
def om_f49_operating_margin_kurt_252d_base_v087_signal(opinc):
    result = opinc.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of opinc
def om_f49_operating_margin_kurt_504d_base_v088_signal(opinc):
    result = opinc.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of opinc times closeadj
def om_f49_operating_margin_rank_252d_base_v089_signal(opinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = opinc.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of opinc times closeadj
def om_f49_operating_margin_rank_504d_base_v090_signal(opinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = opinc.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of opinc times closeadj
def om_f49_operating_margin_rank_1008d_base_v091_signal(opinc, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = opinc.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of opinc from 63d mean times closeadj
def om_f49_operating_margin_devmean_63d_base_v092_signal(opinc, closeadj):
    m = _mean(opinc, 63)
    result = (opinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of opinc from 252d mean times closeadj
def om_f49_operating_margin_devmean_252d_base_v093_signal(opinc, closeadj):
    m = _mean(opinc, 252)
    result = (opinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of opinc from 504d mean times closeadj
def om_f49_operating_margin_devmean_504d_base_v094_signal(opinc, closeadj):
    m = _mean(opinc, 504)
    result = (opinc - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of opinc times closeadj
def om_f49_operating_margin_logdiff_21d_base_v095_signal(opinc, closeadj):
    lr = _operating_margin_log(opinc)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of opinc times closeadj
def om_f49_operating_margin_logdiff_63d_base_v096_signal(opinc, closeadj):
    lr = _operating_margin_log(opinc)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of opinc times closeadj
def om_f49_operating_margin_logdiff_252d_base_v097_signal(opinc, closeadj):
    lr = _operating_margin_log(opinc)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of opinc times closeadj
def om_f49_operating_margin_range_63d_base_v098_signal(opinc, closeadj):
    hi = opinc.rolling(63, min_periods=max(1, 63//2)).max()
    lo = opinc.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of opinc times closeadj
def om_f49_operating_margin_range_252d_base_v099_signal(opinc, closeadj):
    hi = opinc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = opinc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of opinc times closeadj
def om_f49_operating_margin_range_504d_base_v100_signal(opinc, closeadj):
    hi = opinc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = opinc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 252d mean times closeadj
def om_f49_operating_margin_rel_252d_base_v101_signal(opinc, closeadj):
    m = _mean(opinc, 252).replace(0, np.nan)
    result = (opinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 504d mean times closeadj
def om_f49_operating_margin_rel_504d_base_v102_signal(opinc, closeadj):
    m = _mean(opinc, 504).replace(0, np.nan)
    result = (opinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# opinc relative to 1008d mean times closeadj
def om_f49_operating_margin_rel_1008d_base_v103_signal(opinc, closeadj):
    m = _mean(opinc, 1008).replace(0, np.nan)
    result = (opinc / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized opinc/assets 63d mean
def om_f49_operating_margin_sqnorm_assets_63d_base_v104_signal(opinc, assets):
    r = _operating_margin_scaled(opinc, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized opinc/assets 252d mean
def om_f49_operating_margin_sqnorm_assets_252d_base_v105_signal(opinc, assets):
    r = _operating_margin_scaled(opinc, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized opinc/marketcap 63d mean
def om_f49_operating_margin_sqnorm_marketcap_63d_base_v106_signal(opinc, marketcap):
    r = _operating_margin_scaled(opinc, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized opinc/marketcap 252d mean
def om_f49_operating_margin_sqnorm_marketcap_252d_base_v107_signal(opinc, marketcap):
    r = _operating_margin_scaled(opinc, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized opinc/equity 63d mean
def om_f49_operating_margin_sqnorm_equity_63d_base_v108_signal(opinc, equity):
    r = _operating_margin_scaled(opinc, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized opinc/equity 252d mean
def om_f49_operating_margin_sqnorm_equity_252d_base_v109_signal(opinc, equity):
    r = _operating_margin_scaled(opinc, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of opinc times closeadj
def om_f49_operating_margin_infrat_63d_base_v110_signal(opinc, closeadj):
    m = _mean(opinc, 63)
    s = _std(opinc, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of opinc times closeadj
def om_f49_operating_margin_infrat_252d_base_v111_signal(opinc, closeadj):
    m = _mean(opinc, 252)
    s = _std(opinc, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of opinc times closeadj
def om_f49_operating_margin_infrat_504d_base_v112_signal(opinc, closeadj):
    m = _mean(opinc, 504)
    s = _std(opinc, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of opinc
def om_f49_operating_margin_cv_252d_base_v113_signal(opinc):
    m = _mean(opinc, 252).abs().replace(0, np.nan)
    s = _std(opinc, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of opinc
def om_f49_operating_margin_cv_504d_base_v114_signal(opinc):
    m = _mean(opinc, 504).abs().replace(0, np.nan)
    s = _std(opinc, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged opinc times closeadj
def om_f49_operating_margin_lag_5d_base_v115_signal(opinc, closeadj):
    result = opinc.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged opinc times closeadj
def om_f49_operating_margin_lag_21d_base_v116_signal(opinc, closeadj):
    result = opinc.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged opinc times closeadj
def om_f49_operating_margin_lag_63d_base_v117_signal(opinc, closeadj):
    result = opinc.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged opinc times closeadj
def om_f49_operating_margin_lag_252d_base_v118_signal(opinc, closeadj):
    result = opinc.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(opinc) / mean(assets) x closeadj
def om_f49_operating_margin_cumper_assets_252d_base_v119_signal(opinc, assets, closeadj):
    s = opinc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(opinc) / mean(assets) x closeadj
def om_f49_operating_margin_cumper_assets_504d_base_v120_signal(opinc, assets, closeadj):
    s = opinc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(opinc) / mean(marketcap) x closeadj
def om_f49_operating_margin_cumper_marketcap_252d_base_v121_signal(opinc, marketcap, closeadj):
    s = opinc.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(opinc) / mean(marketcap) x closeadj
def om_f49_operating_margin_cumper_marketcap_504d_base_v122_signal(opinc, marketcap, closeadj):
    s = opinc.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only opinc times closeadj
def om_f49_operating_margin_pos_63d_base_v123_signal(opinc, closeadj):
    pos = opinc.where(opinc > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only opinc times closeadj
def om_f49_operating_margin_pos_252d_base_v124_signal(opinc, closeadj):
    pos = opinc.where(opinc > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only opinc times closeadj
def om_f49_operating_margin_neg_63d_base_v125_signal(opinc, closeadj):
    neg = opinc.where(opinc < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only opinc times closeadj
def om_f49_operating_margin_neg_252d_base_v126_signal(opinc, closeadj):
    neg = opinc.where(opinc < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of opinc times closeadj
def om_f49_operating_margin_hl_21d_base_v127_signal(opinc, closeadj):
    result = opinc.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of opinc times closeadj
def om_f49_operating_margin_hl_63d_base_v128_signal(opinc, closeadj):
    result = opinc.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of opinc times closeadj
def om_f49_operating_margin_hl_252d_base_v129_signal(opinc, closeadj):
    result = opinc.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of opinc
def om_f49_operating_margin_z_63d_base_v130_signal(opinc):
    result = _z(opinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of opinc
def om_f49_operating_margin_z_126d_base_v131_signal(opinc):
    result = _z(opinc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of opinc
def om_f49_operating_margin_z_1008d_base_v132_signal(opinc):
    result = _z(opinc, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of opinc times closeadj
def om_f49_operating_margin_st_lt_252_21d_base_v133_signal(opinc, closeadj):
    sm = _mean(opinc, 21)
    lm = _mean(opinc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of opinc times closeadj
def om_f49_operating_margin_st_lt_252_63d_base_v134_signal(opinc, closeadj):
    sm = _mean(opinc, 63)
    lm = _mean(opinc, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of opinc times closeadj
def om_f49_operating_margin_st_lt_504_21d_base_v135_signal(opinc, closeadj):
    sm = _mean(opinc, 21)
    lm = _mean(opinc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of opinc times closeadj
def om_f49_operating_margin_st_lt_504_63d_base_v136_signal(opinc, closeadj):
    sm = _mean(opinc, 63)
    lm = _mean(opinc, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged opinc/assets times closeadj
def om_f49_operating_margin_lag_per_assets_21d_base_v137_signal(opinc, assets, closeadj):
    r = _operating_margin_scaled(opinc, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged opinc/assets times closeadj
def om_f49_operating_margin_lag_per_assets_63d_base_v138_signal(opinc, assets, closeadj):
    r = _operating_margin_scaled(opinc, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged opinc/assets times closeadj
def om_f49_operating_margin_lag_per_assets_252d_base_v139_signal(opinc, assets, closeadj):
    r = _operating_margin_scaled(opinc, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged opinc/marketcap times closeadj
def om_f49_operating_margin_lag_per_marketcap_21d_base_v140_signal(opinc, marketcap, closeadj):
    r = _operating_margin_scaled(opinc, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged opinc/marketcap times closeadj
def om_f49_operating_margin_lag_per_marketcap_63d_base_v141_signal(opinc, marketcap, closeadj):
    r = _operating_margin_scaled(opinc, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged opinc/marketcap times closeadj
def om_f49_operating_margin_lag_per_marketcap_252d_base_v142_signal(opinc, marketcap, closeadj):
    r = _operating_margin_scaled(opinc, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |opinc| times closeadj
def om_f49_operating_margin_abssum_63d_base_v143_signal(opinc, closeadj):
    result = opinc.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |opinc| times closeadj
def om_f49_operating_margin_abssum_252d_base_v144_signal(opinc, closeadj):
    result = opinc.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |opinc| times closeadj
def om_f49_operating_margin_abssum_504d_base_v145_signal(opinc, closeadj):
    result = opinc.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of opinc
def om_f49_operating_margin_acf1_252d_base_v146_signal(opinc):
    result = opinc.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of opinc
def om_f49_operating_margin_acf1_504d_base_v147_signal(opinc):
    result = opinc.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of opinc
def om_f49_operating_margin_posinrange_252d_base_v148_signal(opinc):
    m = _mean(opinc, 252)
    hi = opinc.rolling(252, min_periods=max(1, 252//2)).max()
    lo = opinc.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of opinc
def om_f49_operating_margin_posinrange_504d_base_v149_signal(opinc):
    m = _mean(opinc, 504)
    hi = opinc.rolling(504, min_periods=max(1, 504//2)).max()
    lo = opinc.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of opinc times closeadj
def om_f49_operating_margin_hl_5d_base_v150_signal(opinc, closeadj):
    result = opinc.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
