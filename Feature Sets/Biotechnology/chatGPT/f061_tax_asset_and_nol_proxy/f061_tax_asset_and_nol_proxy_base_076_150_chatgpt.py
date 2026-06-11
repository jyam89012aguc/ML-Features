"""Family f061 - Tax assets and NOL proxy (Earnings and Quality) | Sharadar tables: SF1 | fields: taxassets, taxexp, ebt, assets | base 076-150"""
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
def _tax_asset_and_nol_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _tax_asset_and_nol_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _tax_asset_and_nol_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of taxassets/ebt
def taan_f061_tax_asset_and_nol_proxy_log_per_ebt_504d_base_v076_signal(taxassets, ebt):
    s = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of taxassets/assets
def taan_f061_tax_asset_and_nol_proxy_log_per_assets_252d_base_v077_signal(taxassets, assets):
    s = _tax_asset_and_nol_proxy_scaled(taxassets, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of taxassets/assets
def taan_f061_tax_asset_and_nol_proxy_log_per_assets_504d_base_v078_signal(taxassets, assets):
    s = _tax_asset_and_nol_proxy_scaled(taxassets, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_ewm_21d_base_v079_signal(taxassets, closeadj):
    result = taxassets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_ewm_63d_base_v080_signal(taxassets, closeadj):
    result = taxassets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_ewm_252d_base_v081_signal(taxassets, closeadj):
    result = taxassets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_med_63d_base_v082_signal(taxassets, closeadj):
    result = taxassets.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_med_252d_base_v083_signal(taxassets, closeadj):
    result = taxassets.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_med_504d_base_v084_signal(taxassets, closeadj):
    result = taxassets.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of taxassets
def taan_f061_tax_asset_and_nol_proxy_skew_252d_base_v085_signal(taxassets):
    result = taxassets.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of taxassets
def taan_f061_tax_asset_and_nol_proxy_skew_504d_base_v086_signal(taxassets):
    result = taxassets.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of taxassets
def taan_f061_tax_asset_and_nol_proxy_kurt_252d_base_v087_signal(taxassets):
    result = taxassets.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of taxassets
def taan_f061_tax_asset_and_nol_proxy_kurt_504d_base_v088_signal(taxassets):
    result = taxassets.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_rank_252d_base_v089_signal(taxassets, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = taxassets.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_rank_504d_base_v090_signal(taxassets, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = taxassets.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_rank_1008d_base_v091_signal(taxassets, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = taxassets.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of taxassets from 63d mean times closeadj
def taan_f061_tax_asset_and_nol_proxy_devmean_63d_base_v092_signal(taxassets, closeadj):
    m = _mean(taxassets, 63)
    result = (taxassets - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of taxassets from 252d mean times closeadj
def taan_f061_tax_asset_and_nol_proxy_devmean_252d_base_v093_signal(taxassets, closeadj):
    m = _mean(taxassets, 252)
    result = (taxassets - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of taxassets from 504d mean times closeadj
def taan_f061_tax_asset_and_nol_proxy_devmean_504d_base_v094_signal(taxassets, closeadj):
    m = _mean(taxassets, 504)
    result = (taxassets - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_logdiff_21d_base_v095_signal(taxassets, closeadj):
    lr = _tax_asset_and_nol_proxy_log(taxassets)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_logdiff_63d_base_v096_signal(taxassets, closeadj):
    lr = _tax_asset_and_nol_proxy_log(taxassets)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_logdiff_252d_base_v097_signal(taxassets, closeadj):
    lr = _tax_asset_and_nol_proxy_log(taxassets)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_range_63d_base_v098_signal(taxassets, closeadj):
    hi = taxassets.rolling(63, min_periods=max(1, 63//2)).max()
    lo = taxassets.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_range_252d_base_v099_signal(taxassets, closeadj):
    hi = taxassets.rolling(252, min_periods=max(1, 252//2)).max()
    lo = taxassets.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_range_504d_base_v100_signal(taxassets, closeadj):
    hi = taxassets.rolling(504, min_periods=max(1, 504//2)).max()
    lo = taxassets.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 252d mean times closeadj
def taan_f061_tax_asset_and_nol_proxy_rel_252d_base_v101_signal(taxassets, closeadj):
    m = _mean(taxassets, 252).replace(0, np.nan)
    result = (taxassets / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 504d mean times closeadj
def taan_f061_tax_asset_and_nol_proxy_rel_504d_base_v102_signal(taxassets, closeadj):
    m = _mean(taxassets, 504).replace(0, np.nan)
    result = (taxassets / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxassets relative to 1008d mean times closeadj
def taan_f061_tax_asset_and_nol_proxy_rel_1008d_base_v103_signal(taxassets, closeadj):
    m = _mean(taxassets, 1008).replace(0, np.nan)
    result = (taxassets / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized taxassets/taxexp 63d mean
def taan_f061_tax_asset_and_nol_proxy_sqnorm_taxexp_63d_base_v104_signal(taxassets, taxexp):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized taxassets/taxexp 252d mean
def taan_f061_tax_asset_and_nol_proxy_sqnorm_taxexp_252d_base_v105_signal(taxassets, taxexp):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized taxassets/ebt 63d mean
def taan_f061_tax_asset_and_nol_proxy_sqnorm_ebt_63d_base_v106_signal(taxassets, ebt):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized taxassets/ebt 252d mean
def taan_f061_tax_asset_and_nol_proxy_sqnorm_ebt_252d_base_v107_signal(taxassets, ebt):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized taxassets/assets 63d mean
def taan_f061_tax_asset_and_nol_proxy_sqnorm_assets_63d_base_v108_signal(taxassets, assets):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized taxassets/assets 252d mean
def taan_f061_tax_asset_and_nol_proxy_sqnorm_assets_252d_base_v109_signal(taxassets, assets):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_infrat_63d_base_v110_signal(taxassets, closeadj):
    m = _mean(taxassets, 63)
    s = _std(taxassets, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_infrat_252d_base_v111_signal(taxassets, closeadj):
    m = _mean(taxassets, 252)
    s = _std(taxassets, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_infrat_504d_base_v112_signal(taxassets, closeadj):
    m = _mean(taxassets, 504)
    s = _std(taxassets, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of taxassets
def taan_f061_tax_asset_and_nol_proxy_cv_252d_base_v113_signal(taxassets):
    m = _mean(taxassets, 252).abs().replace(0, np.nan)
    s = _std(taxassets, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of taxassets
def taan_f061_tax_asset_and_nol_proxy_cv_504d_base_v114_signal(taxassets):
    m = _mean(taxassets, 504).abs().replace(0, np.nan)
    s = _std(taxassets, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_5d_base_v115_signal(taxassets, closeadj):
    result = taxassets.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_21d_base_v116_signal(taxassets, closeadj):
    result = taxassets.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_63d_base_v117_signal(taxassets, closeadj):
    result = taxassets.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_252d_base_v118_signal(taxassets, closeadj):
    result = taxassets.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(taxassets) / mean(taxexp) x closeadj
def taan_f061_tax_asset_and_nol_proxy_cumper_taxexp_252d_base_v119_signal(taxassets, taxexp, closeadj):
    s = taxassets.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(taxexp, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(taxassets) / mean(taxexp) x closeadj
def taan_f061_tax_asset_and_nol_proxy_cumper_taxexp_504d_base_v120_signal(taxassets, taxexp, closeadj):
    s = taxassets.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(taxexp, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(taxassets) / mean(ebt) x closeadj
def taan_f061_tax_asset_and_nol_proxy_cumper_ebt_252d_base_v121_signal(taxassets, ebt, closeadj):
    s = taxassets.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(ebt, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(taxassets) / mean(ebt) x closeadj
def taan_f061_tax_asset_and_nol_proxy_cumper_ebt_504d_base_v122_signal(taxassets, ebt, closeadj):
    s = taxassets.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(ebt, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_pos_63d_base_v123_signal(taxassets, closeadj):
    pos = taxassets.where(taxassets > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_pos_252d_base_v124_signal(taxassets, closeadj):
    pos = taxassets.where(taxassets > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_neg_63d_base_v125_signal(taxassets, closeadj):
    neg = taxassets.where(taxassets < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_neg_252d_base_v126_signal(taxassets, closeadj):
    neg = taxassets.where(taxassets < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_hl_21d_base_v127_signal(taxassets, closeadj):
    result = taxassets.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_hl_63d_base_v128_signal(taxassets, closeadj):
    result = taxassets.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_hl_252d_base_v129_signal(taxassets, closeadj):
    result = taxassets.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of taxassets
def taan_f061_tax_asset_and_nol_proxy_z_63d_base_v130_signal(taxassets):
    result = _z(taxassets, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of taxassets
def taan_f061_tax_asset_and_nol_proxy_z_126d_base_v131_signal(taxassets):
    result = _z(taxassets, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of taxassets
def taan_f061_tax_asset_and_nol_proxy_z_1008d_base_v132_signal(taxassets):
    result = _z(taxassets, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_st_lt_252_21d_base_v133_signal(taxassets, closeadj):
    sm = _mean(taxassets, 21)
    lm = _mean(taxassets, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_st_lt_252_63d_base_v134_signal(taxassets, closeadj):
    sm = _mean(taxassets, 63)
    lm = _mean(taxassets, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_st_lt_504_21d_base_v135_signal(taxassets, closeadj):
    sm = _mean(taxassets, 21)
    lm = _mean(taxassets, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_st_lt_504_63d_base_v136_signal(taxassets, closeadj):
    sm = _mean(taxassets, 63)
    lm = _mean(taxassets, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged taxassets/taxexp times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_per_taxexp_21d_base_v137_signal(taxassets, taxexp, closeadj):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged taxassets/taxexp times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_per_taxexp_63d_base_v138_signal(taxassets, taxexp, closeadj):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged taxassets/taxexp times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_per_taxexp_252d_base_v139_signal(taxassets, taxexp, closeadj):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, taxexp)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged taxassets/ebt times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_per_ebt_21d_base_v140_signal(taxassets, ebt, closeadj):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged taxassets/ebt times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_per_ebt_63d_base_v141_signal(taxassets, ebt, closeadj):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged taxassets/ebt times closeadj
def taan_f061_tax_asset_and_nol_proxy_lag_per_ebt_252d_base_v142_signal(taxassets, ebt, closeadj):
    r = _tax_asset_and_nol_proxy_scaled(taxassets, ebt)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |taxassets| times closeadj
def taan_f061_tax_asset_and_nol_proxy_abssum_63d_base_v143_signal(taxassets, closeadj):
    result = taxassets.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |taxassets| times closeadj
def taan_f061_tax_asset_and_nol_proxy_abssum_252d_base_v144_signal(taxassets, closeadj):
    result = taxassets.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |taxassets| times closeadj
def taan_f061_tax_asset_and_nol_proxy_abssum_504d_base_v145_signal(taxassets, closeadj):
    result = taxassets.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of taxassets
def taan_f061_tax_asset_and_nol_proxy_acf1_252d_base_v146_signal(taxassets):
    result = taxassets.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of taxassets
def taan_f061_tax_asset_and_nol_proxy_acf1_504d_base_v147_signal(taxassets):
    result = taxassets.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of taxassets
def taan_f061_tax_asset_and_nol_proxy_posinrange_252d_base_v148_signal(taxassets):
    m = _mean(taxassets, 252)
    hi = taxassets.rolling(252, min_periods=max(1, 252//2)).max()
    lo = taxassets.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of taxassets
def taan_f061_tax_asset_and_nol_proxy_posinrange_504d_base_v149_signal(taxassets):
    m = _mean(taxassets, 504)
    hi = taxassets.rolling(504, min_periods=max(1, 504//2)).max()
    lo = taxassets.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of taxassets times closeadj
def taan_f061_tax_asset_and_nol_proxy_hl_5d_base_v150_signal(taxassets, closeadj):
    result = taxassets.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
