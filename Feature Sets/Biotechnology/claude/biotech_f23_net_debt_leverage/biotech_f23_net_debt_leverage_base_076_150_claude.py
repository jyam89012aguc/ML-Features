"""Family f23 - Net debt & leverage  (D_Capital_Debt) | base 076-150"""
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
def _net_debt_leverage_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_debt_leverage_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_debt_leverage_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of debt/marketcap
def ndl_f23_net_debt_leverage_log_per_marketcap_504d_base_v076_signal(debt, marketcap):
    s = _net_debt_leverage_scaled(debt, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of debt/equity
def ndl_f23_net_debt_leverage_log_per_equity_252d_base_v077_signal(debt, equity):
    s = _net_debt_leverage_scaled(debt, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of debt/equity
def ndl_f23_net_debt_leverage_log_per_equity_504d_base_v078_signal(debt, equity):
    s = _net_debt_leverage_scaled(debt, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of debt times closeadj
def ndl_f23_net_debt_leverage_ewm_21d_base_v079_signal(debt, closeadj):
    result = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of debt times closeadj
def ndl_f23_net_debt_leverage_ewm_63d_base_v080_signal(debt, closeadj):
    result = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of debt times closeadj
def ndl_f23_net_debt_leverage_ewm_252d_base_v081_signal(debt, closeadj):
    result = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of debt times closeadj
def ndl_f23_net_debt_leverage_med_63d_base_v082_signal(debt, closeadj):
    result = debt.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of debt times closeadj
def ndl_f23_net_debt_leverage_med_252d_base_v083_signal(debt, closeadj):
    result = debt.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of debt times closeadj
def ndl_f23_net_debt_leverage_med_504d_base_v084_signal(debt, closeadj):
    result = debt.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of debt
def ndl_f23_net_debt_leverage_skew_252d_base_v085_signal(debt):
    result = debt.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of debt
def ndl_f23_net_debt_leverage_skew_504d_base_v086_signal(debt):
    result = debt.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of debt
def ndl_f23_net_debt_leverage_kurt_252d_base_v087_signal(debt):
    result = debt.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of debt
def ndl_f23_net_debt_leverage_kurt_504d_base_v088_signal(debt):
    result = debt.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of debt times closeadj
def ndl_f23_net_debt_leverage_rank_252d_base_v089_signal(debt, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = debt.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of debt times closeadj
def ndl_f23_net_debt_leverage_rank_504d_base_v090_signal(debt, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = debt.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of debt times closeadj
def ndl_f23_net_debt_leverage_rank_1008d_base_v091_signal(debt, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = debt.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of debt from 63d mean times closeadj
def ndl_f23_net_debt_leverage_devmean_63d_base_v092_signal(debt, closeadj):
    m = _mean(debt, 63)
    result = (debt - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of debt from 252d mean times closeadj
def ndl_f23_net_debt_leverage_devmean_252d_base_v093_signal(debt, closeadj):
    m = _mean(debt, 252)
    result = (debt - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of debt from 504d mean times closeadj
def ndl_f23_net_debt_leverage_devmean_504d_base_v094_signal(debt, closeadj):
    m = _mean(debt, 504)
    result = (debt - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of debt times closeadj
def ndl_f23_net_debt_leverage_logdiff_21d_base_v095_signal(debt, closeadj):
    lr = _net_debt_leverage_log(debt)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of debt times closeadj
def ndl_f23_net_debt_leverage_logdiff_63d_base_v096_signal(debt, closeadj):
    lr = _net_debt_leverage_log(debt)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of debt times closeadj
def ndl_f23_net_debt_leverage_logdiff_252d_base_v097_signal(debt, closeadj):
    lr = _net_debt_leverage_log(debt)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of debt times closeadj
def ndl_f23_net_debt_leverage_range_63d_base_v098_signal(debt, closeadj):
    hi = debt.rolling(63, min_periods=max(1, 63//2)).max()
    lo = debt.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of debt times closeadj
def ndl_f23_net_debt_leverage_range_252d_base_v099_signal(debt, closeadj):
    hi = debt.rolling(252, min_periods=max(1, 252//2)).max()
    lo = debt.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of debt times closeadj
def ndl_f23_net_debt_leverage_range_504d_base_v100_signal(debt, closeadj):
    hi = debt.rolling(504, min_periods=max(1, 504//2)).max()
    lo = debt.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 252d mean times closeadj
def ndl_f23_net_debt_leverage_rel_252d_base_v101_signal(debt, closeadj):
    m = _mean(debt, 252).replace(0, np.nan)
    result = (debt / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 504d mean times closeadj
def ndl_f23_net_debt_leverage_rel_504d_base_v102_signal(debt, closeadj):
    m = _mean(debt, 504).replace(0, np.nan)
    result = (debt / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 1008d mean times closeadj
def ndl_f23_net_debt_leverage_rel_1008d_base_v103_signal(debt, closeadj):
    m = _mean(debt, 1008).replace(0, np.nan)
    result = (debt / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debt/assets 63d mean
def ndl_f23_net_debt_leverage_sqnorm_assets_63d_base_v104_signal(debt, assets):
    r = _net_debt_leverage_scaled(debt, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debt/assets 252d mean
def ndl_f23_net_debt_leverage_sqnorm_assets_252d_base_v105_signal(debt, assets):
    r = _net_debt_leverage_scaled(debt, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debt/marketcap 63d mean
def ndl_f23_net_debt_leverage_sqnorm_marketcap_63d_base_v106_signal(debt, marketcap):
    r = _net_debt_leverage_scaled(debt, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debt/marketcap 252d mean
def ndl_f23_net_debt_leverage_sqnorm_marketcap_252d_base_v107_signal(debt, marketcap):
    r = _net_debt_leverage_scaled(debt, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debt/equity 63d mean
def ndl_f23_net_debt_leverage_sqnorm_equity_63d_base_v108_signal(debt, equity):
    r = _net_debt_leverage_scaled(debt, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized debt/equity 252d mean
def ndl_f23_net_debt_leverage_sqnorm_equity_252d_base_v109_signal(debt, equity):
    r = _net_debt_leverage_scaled(debt, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of debt times closeadj
def ndl_f23_net_debt_leverage_infrat_63d_base_v110_signal(debt, closeadj):
    m = _mean(debt, 63)
    s = _std(debt, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of debt times closeadj
def ndl_f23_net_debt_leverage_infrat_252d_base_v111_signal(debt, closeadj):
    m = _mean(debt, 252)
    s = _std(debt, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of debt times closeadj
def ndl_f23_net_debt_leverage_infrat_504d_base_v112_signal(debt, closeadj):
    m = _mean(debt, 504)
    s = _std(debt, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of debt
def ndl_f23_net_debt_leverage_cv_252d_base_v113_signal(debt):
    m = _mean(debt, 252).abs().replace(0, np.nan)
    s = _std(debt, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of debt
def ndl_f23_net_debt_leverage_cv_504d_base_v114_signal(debt):
    m = _mean(debt, 504).abs().replace(0, np.nan)
    s = _std(debt, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged debt times closeadj
def ndl_f23_net_debt_leverage_lag_5d_base_v115_signal(debt, closeadj):
    result = debt.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged debt times closeadj
def ndl_f23_net_debt_leverage_lag_21d_base_v116_signal(debt, closeadj):
    result = debt.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged debt times closeadj
def ndl_f23_net_debt_leverage_lag_63d_base_v117_signal(debt, closeadj):
    result = debt.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged debt times closeadj
def ndl_f23_net_debt_leverage_lag_252d_base_v118_signal(debt, closeadj):
    result = debt.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(debt) / mean(assets) x closeadj
def ndl_f23_net_debt_leverage_cumper_assets_252d_base_v119_signal(debt, assets, closeadj):
    s = debt.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(debt) / mean(assets) x closeadj
def ndl_f23_net_debt_leverage_cumper_assets_504d_base_v120_signal(debt, assets, closeadj):
    s = debt.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(debt) / mean(marketcap) x closeadj
def ndl_f23_net_debt_leverage_cumper_marketcap_252d_base_v121_signal(debt, marketcap, closeadj):
    s = debt.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(debt) / mean(marketcap) x closeadj
def ndl_f23_net_debt_leverage_cumper_marketcap_504d_base_v122_signal(debt, marketcap, closeadj):
    s = debt.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only debt times closeadj
def ndl_f23_net_debt_leverage_pos_63d_base_v123_signal(debt, closeadj):
    pos = debt.where(debt > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only debt times closeadj
def ndl_f23_net_debt_leverage_pos_252d_base_v124_signal(debt, closeadj):
    pos = debt.where(debt > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only debt times closeadj
def ndl_f23_net_debt_leverage_neg_63d_base_v125_signal(debt, closeadj):
    neg = debt.where(debt < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only debt times closeadj
def ndl_f23_net_debt_leverage_neg_252d_base_v126_signal(debt, closeadj):
    neg = debt.where(debt < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of debt times closeadj
def ndl_f23_net_debt_leverage_hl_21d_base_v127_signal(debt, closeadj):
    result = debt.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of debt times closeadj
def ndl_f23_net_debt_leverage_hl_63d_base_v128_signal(debt, closeadj):
    result = debt.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of debt times closeadj
def ndl_f23_net_debt_leverage_hl_252d_base_v129_signal(debt, closeadj):
    result = debt.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of debt
def ndl_f23_net_debt_leverage_z_63d_base_v130_signal(debt):
    result = _z(debt, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of debt
def ndl_f23_net_debt_leverage_z_126d_base_v131_signal(debt):
    result = _z(debt, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of debt
def ndl_f23_net_debt_leverage_z_1008d_base_v132_signal(debt):
    result = _z(debt, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of debt times closeadj
def ndl_f23_net_debt_leverage_st_lt_252_21d_base_v133_signal(debt, closeadj):
    sm = _mean(debt, 21)
    lm = _mean(debt, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of debt times closeadj
def ndl_f23_net_debt_leverage_st_lt_252_63d_base_v134_signal(debt, closeadj):
    sm = _mean(debt, 63)
    lm = _mean(debt, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of debt times closeadj
def ndl_f23_net_debt_leverage_st_lt_504_21d_base_v135_signal(debt, closeadj):
    sm = _mean(debt, 21)
    lm = _mean(debt, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of debt times closeadj
def ndl_f23_net_debt_leverage_st_lt_504_63d_base_v136_signal(debt, closeadj):
    sm = _mean(debt, 63)
    lm = _mean(debt, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged debt/assets times closeadj
def ndl_f23_net_debt_leverage_lag_per_assets_21d_base_v137_signal(debt, assets, closeadj):
    r = _net_debt_leverage_scaled(debt, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged debt/assets times closeadj
def ndl_f23_net_debt_leverage_lag_per_assets_63d_base_v138_signal(debt, assets, closeadj):
    r = _net_debt_leverage_scaled(debt, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged debt/assets times closeadj
def ndl_f23_net_debt_leverage_lag_per_assets_252d_base_v139_signal(debt, assets, closeadj):
    r = _net_debt_leverage_scaled(debt, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged debt/marketcap times closeadj
def ndl_f23_net_debt_leverage_lag_per_marketcap_21d_base_v140_signal(debt, marketcap, closeadj):
    r = _net_debt_leverage_scaled(debt, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged debt/marketcap times closeadj
def ndl_f23_net_debt_leverage_lag_per_marketcap_63d_base_v141_signal(debt, marketcap, closeadj):
    r = _net_debt_leverage_scaled(debt, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged debt/marketcap times closeadj
def ndl_f23_net_debt_leverage_lag_per_marketcap_252d_base_v142_signal(debt, marketcap, closeadj):
    r = _net_debt_leverage_scaled(debt, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |debt| times closeadj
def ndl_f23_net_debt_leverage_abssum_63d_base_v143_signal(debt, closeadj):
    result = debt.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |debt| times closeadj
def ndl_f23_net_debt_leverage_abssum_252d_base_v144_signal(debt, closeadj):
    result = debt.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |debt| times closeadj
def ndl_f23_net_debt_leverage_abssum_504d_base_v145_signal(debt, closeadj):
    result = debt.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of debt
def ndl_f23_net_debt_leverage_acf1_252d_base_v146_signal(debt):
    result = debt.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of debt
def ndl_f23_net_debt_leverage_acf1_504d_base_v147_signal(debt):
    result = debt.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of debt
def ndl_f23_net_debt_leverage_posinrange_252d_base_v148_signal(debt):
    m = _mean(debt, 252)
    hi = debt.rolling(252, min_periods=max(1, 252//2)).max()
    lo = debt.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of debt
def ndl_f23_net_debt_leverage_posinrange_504d_base_v149_signal(debt):
    m = _mean(debt, 504)
    hi = debt.rolling(504, min_periods=max(1, 504//2)).max()
    lo = debt.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of debt times closeadj
def ndl_f23_net_debt_leverage_hl_5d_base_v150_signal(debt, closeadj):
    result = debt.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
