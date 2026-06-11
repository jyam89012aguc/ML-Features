"""Family f043 - Inventory build and launch readiness (Balance Sheet Composition) | Sharadar tables: SF1 | fields: inventory, revenue, cor, assets | base 076-150"""
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
def _inventory_build_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _inventory_build_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _inventory_build_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of inventory/cor
def ib_f043_inventory_build_log_per_cor_504d_base_v076_signal(inventory, cor):
    s = _inventory_build_scaled(inventory, cor)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of inventory/assets
def ib_f043_inventory_build_log_per_assets_252d_base_v077_signal(inventory, assets):
    s = _inventory_build_scaled(inventory, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of inventory/assets
def ib_f043_inventory_build_log_per_assets_504d_base_v078_signal(inventory, assets):
    s = _inventory_build_scaled(inventory, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of inventory times closeadj
def ib_f043_inventory_build_ewm_21d_base_v079_signal(inventory, closeadj):
    result = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of inventory times closeadj
def ib_f043_inventory_build_ewm_63d_base_v080_signal(inventory, closeadj):
    result = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of inventory times closeadj
def ib_f043_inventory_build_ewm_252d_base_v081_signal(inventory, closeadj):
    result = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of inventory times closeadj
def ib_f043_inventory_build_med_63d_base_v082_signal(inventory, closeadj):
    result = inventory.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of inventory times closeadj
def ib_f043_inventory_build_med_252d_base_v083_signal(inventory, closeadj):
    result = inventory.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of inventory times closeadj
def ib_f043_inventory_build_med_504d_base_v084_signal(inventory, closeadj):
    result = inventory.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of inventory
def ib_f043_inventory_build_skew_252d_base_v085_signal(inventory):
    result = inventory.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of inventory
def ib_f043_inventory_build_skew_504d_base_v086_signal(inventory):
    result = inventory.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of inventory
def ib_f043_inventory_build_kurt_252d_base_v087_signal(inventory):
    result = inventory.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of inventory
def ib_f043_inventory_build_kurt_504d_base_v088_signal(inventory):
    result = inventory.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of inventory times closeadj
def ib_f043_inventory_build_rank_252d_base_v089_signal(inventory, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = inventory.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of inventory times closeadj
def ib_f043_inventory_build_rank_504d_base_v090_signal(inventory, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = inventory.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of inventory times closeadj
def ib_f043_inventory_build_rank_1008d_base_v091_signal(inventory, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = inventory.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of inventory from 63d mean times closeadj
def ib_f043_inventory_build_devmean_63d_base_v092_signal(inventory, closeadj):
    m = _mean(inventory, 63)
    result = (inventory - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of inventory from 252d mean times closeadj
def ib_f043_inventory_build_devmean_252d_base_v093_signal(inventory, closeadj):
    m = _mean(inventory, 252)
    result = (inventory - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of inventory from 504d mean times closeadj
def ib_f043_inventory_build_devmean_504d_base_v094_signal(inventory, closeadj):
    m = _mean(inventory, 504)
    result = (inventory - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of inventory times closeadj
def ib_f043_inventory_build_logdiff_21d_base_v095_signal(inventory, closeadj):
    lr = _inventory_build_log(inventory)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of inventory times closeadj
def ib_f043_inventory_build_logdiff_63d_base_v096_signal(inventory, closeadj):
    lr = _inventory_build_log(inventory)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of inventory times closeadj
def ib_f043_inventory_build_logdiff_252d_base_v097_signal(inventory, closeadj):
    lr = _inventory_build_log(inventory)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of inventory times closeadj
def ib_f043_inventory_build_range_63d_base_v098_signal(inventory, closeadj):
    hi = inventory.rolling(63, min_periods=max(1, 63//2)).max()
    lo = inventory.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of inventory times closeadj
def ib_f043_inventory_build_range_252d_base_v099_signal(inventory, closeadj):
    hi = inventory.rolling(252, min_periods=max(1, 252//2)).max()
    lo = inventory.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of inventory times closeadj
def ib_f043_inventory_build_range_504d_base_v100_signal(inventory, closeadj):
    hi = inventory.rolling(504, min_periods=max(1, 504//2)).max()
    lo = inventory.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 252d mean times closeadj
def ib_f043_inventory_build_rel_252d_base_v101_signal(inventory, closeadj):
    m = _mean(inventory, 252).replace(0, np.nan)
    result = (inventory / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 504d mean times closeadj
def ib_f043_inventory_build_rel_504d_base_v102_signal(inventory, closeadj):
    m = _mean(inventory, 504).replace(0, np.nan)
    result = (inventory / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to 1008d mean times closeadj
def ib_f043_inventory_build_rel_1008d_base_v103_signal(inventory, closeadj):
    m = _mean(inventory, 1008).replace(0, np.nan)
    result = (inventory / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized inventory/revenue 63d mean
def ib_f043_inventory_build_sqnorm_revenue_63d_base_v104_signal(inventory, revenue):
    r = _inventory_build_scaled(inventory, revenue)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized inventory/revenue 252d mean
def ib_f043_inventory_build_sqnorm_revenue_252d_base_v105_signal(inventory, revenue):
    r = _inventory_build_scaled(inventory, revenue)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized inventory/cor 63d mean
def ib_f043_inventory_build_sqnorm_cor_63d_base_v106_signal(inventory, cor):
    r = _inventory_build_scaled(inventory, cor)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized inventory/cor 252d mean
def ib_f043_inventory_build_sqnorm_cor_252d_base_v107_signal(inventory, cor):
    r = _inventory_build_scaled(inventory, cor)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized inventory/assets 63d mean
def ib_f043_inventory_build_sqnorm_assets_63d_base_v108_signal(inventory, assets):
    r = _inventory_build_scaled(inventory, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized inventory/assets 252d mean
def ib_f043_inventory_build_sqnorm_assets_252d_base_v109_signal(inventory, assets):
    r = _inventory_build_scaled(inventory, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of inventory times closeadj
def ib_f043_inventory_build_infrat_63d_base_v110_signal(inventory, closeadj):
    m = _mean(inventory, 63)
    s = _std(inventory, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of inventory times closeadj
def ib_f043_inventory_build_infrat_252d_base_v111_signal(inventory, closeadj):
    m = _mean(inventory, 252)
    s = _std(inventory, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of inventory times closeadj
def ib_f043_inventory_build_infrat_504d_base_v112_signal(inventory, closeadj):
    m = _mean(inventory, 504)
    s = _std(inventory, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of inventory
def ib_f043_inventory_build_cv_252d_base_v113_signal(inventory):
    m = _mean(inventory, 252).abs().replace(0, np.nan)
    s = _std(inventory, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of inventory
def ib_f043_inventory_build_cv_504d_base_v114_signal(inventory):
    m = _mean(inventory, 504).abs().replace(0, np.nan)
    s = _std(inventory, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged inventory times closeadj
def ib_f043_inventory_build_lag_5d_base_v115_signal(inventory, closeadj):
    result = inventory.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged inventory times closeadj
def ib_f043_inventory_build_lag_21d_base_v116_signal(inventory, closeadj):
    result = inventory.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged inventory times closeadj
def ib_f043_inventory_build_lag_63d_base_v117_signal(inventory, closeadj):
    result = inventory.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged inventory times closeadj
def ib_f043_inventory_build_lag_252d_base_v118_signal(inventory, closeadj):
    result = inventory.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(inventory) / mean(revenue) x closeadj
def ib_f043_inventory_build_cumper_revenue_252d_base_v119_signal(inventory, revenue, closeadj):
    s = inventory.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(inventory) / mean(revenue) x closeadj
def ib_f043_inventory_build_cumper_revenue_504d_base_v120_signal(inventory, revenue, closeadj):
    s = inventory.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(inventory) / mean(cor) x closeadj
def ib_f043_inventory_build_cumper_cor_252d_base_v121_signal(inventory, cor, closeadj):
    s = inventory.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(cor, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(inventory) / mean(cor) x closeadj
def ib_f043_inventory_build_cumper_cor_504d_base_v122_signal(inventory, cor, closeadj):
    s = inventory.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(cor, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only inventory times closeadj
def ib_f043_inventory_build_pos_63d_base_v123_signal(inventory, closeadj):
    pos = inventory.where(inventory > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only inventory times closeadj
def ib_f043_inventory_build_pos_252d_base_v124_signal(inventory, closeadj):
    pos = inventory.where(inventory > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only inventory times closeadj
def ib_f043_inventory_build_neg_63d_base_v125_signal(inventory, closeadj):
    neg = inventory.where(inventory < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only inventory times closeadj
def ib_f043_inventory_build_neg_252d_base_v126_signal(inventory, closeadj):
    neg = inventory.where(inventory < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of inventory times closeadj
def ib_f043_inventory_build_hl_21d_base_v127_signal(inventory, closeadj):
    result = inventory.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of inventory times closeadj
def ib_f043_inventory_build_hl_63d_base_v128_signal(inventory, closeadj):
    result = inventory.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of inventory times closeadj
def ib_f043_inventory_build_hl_252d_base_v129_signal(inventory, closeadj):
    result = inventory.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of inventory
def ib_f043_inventory_build_z_63d_base_v130_signal(inventory):
    result = _z(inventory, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of inventory
def ib_f043_inventory_build_z_126d_base_v131_signal(inventory):
    result = _z(inventory, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of inventory
def ib_f043_inventory_build_z_1008d_base_v132_signal(inventory):
    result = _z(inventory, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of inventory times closeadj
def ib_f043_inventory_build_st_lt_252_21d_base_v133_signal(inventory, closeadj):
    sm = _mean(inventory, 21)
    lm = _mean(inventory, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of inventory times closeadj
def ib_f043_inventory_build_st_lt_252_63d_base_v134_signal(inventory, closeadj):
    sm = _mean(inventory, 63)
    lm = _mean(inventory, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of inventory times closeadj
def ib_f043_inventory_build_st_lt_504_21d_base_v135_signal(inventory, closeadj):
    sm = _mean(inventory, 21)
    lm = _mean(inventory, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of inventory times closeadj
def ib_f043_inventory_build_st_lt_504_63d_base_v136_signal(inventory, closeadj):
    sm = _mean(inventory, 63)
    lm = _mean(inventory, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged inventory/revenue times closeadj
def ib_f043_inventory_build_lag_per_revenue_21d_base_v137_signal(inventory, revenue, closeadj):
    r = _inventory_build_scaled(inventory, revenue)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged inventory/revenue times closeadj
def ib_f043_inventory_build_lag_per_revenue_63d_base_v138_signal(inventory, revenue, closeadj):
    r = _inventory_build_scaled(inventory, revenue)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged inventory/revenue times closeadj
def ib_f043_inventory_build_lag_per_revenue_252d_base_v139_signal(inventory, revenue, closeadj):
    r = _inventory_build_scaled(inventory, revenue)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged inventory/cor times closeadj
def ib_f043_inventory_build_lag_per_cor_21d_base_v140_signal(inventory, cor, closeadj):
    r = _inventory_build_scaled(inventory, cor)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged inventory/cor times closeadj
def ib_f043_inventory_build_lag_per_cor_63d_base_v141_signal(inventory, cor, closeadj):
    r = _inventory_build_scaled(inventory, cor)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged inventory/cor times closeadj
def ib_f043_inventory_build_lag_per_cor_252d_base_v142_signal(inventory, cor, closeadj):
    r = _inventory_build_scaled(inventory, cor)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |inventory| times closeadj
def ib_f043_inventory_build_abssum_63d_base_v143_signal(inventory, closeadj):
    result = inventory.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |inventory| times closeadj
def ib_f043_inventory_build_abssum_252d_base_v144_signal(inventory, closeadj):
    result = inventory.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |inventory| times closeadj
def ib_f043_inventory_build_abssum_504d_base_v145_signal(inventory, closeadj):
    result = inventory.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of inventory
def ib_f043_inventory_build_acf1_252d_base_v146_signal(inventory):
    result = inventory.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of inventory
def ib_f043_inventory_build_acf1_504d_base_v147_signal(inventory):
    result = inventory.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of inventory
def ib_f043_inventory_build_posinrange_252d_base_v148_signal(inventory):
    m = _mean(inventory, 252)
    hi = inventory.rolling(252, min_periods=max(1, 252//2)).max()
    lo = inventory.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of inventory
def ib_f043_inventory_build_posinrange_504d_base_v149_signal(inventory):
    m = _mean(inventory, 504)
    hi = inventory.rolling(504, min_periods=max(1, 504//2)).max()
    lo = inventory.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of inventory times closeadj
def ib_f043_inventory_build_hl_5d_base_v150_signal(inventory, closeadj):
    result = inventory.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
