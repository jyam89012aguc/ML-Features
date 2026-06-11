"""Family f094 - Post-transaction insider ownership (Insiders and Ownership) | Sharadar tables: SF2 | fields: sharesownedfollowingtransaction, transactionshares | base 076-150"""
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
def _insider_ownership_after_trade_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_ownership_after_trade_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_ownership_after_trade_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of sharesownedfollowingtransaction/assets
def ioat_f094_insider_ownership_after_trade_log_per_assets_504d_base_v076_signal(sharesownedfollowingtransaction, assets):
    s = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesownedfollowingtransaction/marketcap
def ioat_f094_insider_ownership_after_trade_log_per_marketcap_252d_base_v077_signal(sharesownedfollowingtransaction, marketcap):
    s = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sharesownedfollowingtransaction/marketcap
def ioat_f094_insider_ownership_after_trade_log_per_marketcap_504d_base_v078_signal(sharesownedfollowingtransaction, marketcap):
    s = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_ewm_21d_base_v079_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_ewm_63d_base_v080_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_ewm_252d_base_v081_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_med_63d_base_v082_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_med_252d_base_v083_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_med_504d_base_v084_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_skew_252d_base_v085_signal(sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_skew_504d_base_v086_signal(sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_kurt_252d_base_v087_signal(sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_kurt_504d_base_v088_signal(sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_rank_252d_base_v089_signal(sharesownedfollowingtransaction, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_rank_504d_base_v090_signal(sharesownedfollowingtransaction, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_rank_1008d_base_v091_signal(sharesownedfollowingtransaction, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = sharesownedfollowingtransaction.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharesownedfollowingtransaction from 63d mean times closeadj
def ioat_f094_insider_ownership_after_trade_devmean_63d_base_v092_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 63)
    result = (sharesownedfollowingtransaction - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharesownedfollowingtransaction from 252d mean times closeadj
def ioat_f094_insider_ownership_after_trade_devmean_252d_base_v093_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 252)
    result = (sharesownedfollowingtransaction - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of sharesownedfollowingtransaction from 504d mean times closeadj
def ioat_f094_insider_ownership_after_trade_devmean_504d_base_v094_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 504)
    result = (sharesownedfollowingtransaction - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_logdiff_21d_base_v095_signal(sharesownedfollowingtransaction, closeadj):
    lr = _insider_ownership_after_trade_log(sharesownedfollowingtransaction)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_logdiff_63d_base_v096_signal(sharesownedfollowingtransaction, closeadj):
    lr = _insider_ownership_after_trade_log(sharesownedfollowingtransaction)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_logdiff_252d_base_v097_signal(sharesownedfollowingtransaction, closeadj):
    lr = _insider_ownership_after_trade_log(sharesownedfollowingtransaction)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_range_63d_base_v098_signal(sharesownedfollowingtransaction, closeadj):
    hi = sharesownedfollowingtransaction.rolling(63, min_periods=max(1, 63//2)).max()
    lo = sharesownedfollowingtransaction.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_range_252d_base_v099_signal(sharesownedfollowingtransaction, closeadj):
    hi = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_range_504d_base_v100_signal(sharesownedfollowingtransaction, closeadj):
    hi = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 252d mean times closeadj
def ioat_f094_insider_ownership_after_trade_rel_252d_base_v101_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 252).replace(0, np.nan)
    result = (sharesownedfollowingtransaction / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 504d mean times closeadj
def ioat_f094_insider_ownership_after_trade_rel_504d_base_v102_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 504).replace(0, np.nan)
    result = (sharesownedfollowingtransaction / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 1008d mean times closeadj
def ioat_f094_insider_ownership_after_trade_rel_1008d_base_v103_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 1008).replace(0, np.nan)
    result = (sharesownedfollowingtransaction / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesownedfollowingtransaction/transactionshares 63d mean
def ioat_f094_insider_ownership_after_trade_sqnorm_transactionshares_63d_base_v104_signal(sharesownedfollowingtransaction, transactionshares):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesownedfollowingtransaction/transactionshares 252d mean
def ioat_f094_insider_ownership_after_trade_sqnorm_transactionshares_252d_base_v105_signal(sharesownedfollowingtransaction, transactionshares):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesownedfollowingtransaction/assets 63d mean
def ioat_f094_insider_ownership_after_trade_sqnorm_assets_63d_base_v106_signal(sharesownedfollowingtransaction, assets):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesownedfollowingtransaction/assets 252d mean
def ioat_f094_insider_ownership_after_trade_sqnorm_assets_252d_base_v107_signal(sharesownedfollowingtransaction, assets):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesownedfollowingtransaction/marketcap 63d mean
def ioat_f094_insider_ownership_after_trade_sqnorm_marketcap_63d_base_v108_signal(sharesownedfollowingtransaction, marketcap):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized sharesownedfollowingtransaction/marketcap 252d mean
def ioat_f094_insider_ownership_after_trade_sqnorm_marketcap_252d_base_v109_signal(sharesownedfollowingtransaction, marketcap):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_infrat_63d_base_v110_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 63)
    s = _std(sharesownedfollowingtransaction, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_infrat_252d_base_v111_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 252)
    s = _std(sharesownedfollowingtransaction, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_infrat_504d_base_v112_signal(sharesownedfollowingtransaction, closeadj):
    m = _mean(sharesownedfollowingtransaction, 504)
    s = _std(sharesownedfollowingtransaction, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_cv_252d_base_v113_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 252).abs().replace(0, np.nan)
    s = _std(sharesownedfollowingtransaction, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_cv_504d_base_v114_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 504).abs().replace(0, np.nan)
    s = _std(sharesownedfollowingtransaction, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_lag_5d_base_v115_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_lag_21d_base_v116_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_lag_63d_base_v117_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_lag_252d_base_v118_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sharesownedfollowingtransaction) / mean(transactionshares) x closeadj
def ioat_f094_insider_ownership_after_trade_cumper_transactionshares_252d_base_v119_signal(sharesownedfollowingtransaction, transactionshares, closeadj):
    s = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(transactionshares, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sharesownedfollowingtransaction) / mean(transactionshares) x closeadj
def ioat_f094_insider_ownership_after_trade_cumper_transactionshares_504d_base_v120_signal(sharesownedfollowingtransaction, transactionshares, closeadj):
    s = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(transactionshares, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(sharesownedfollowingtransaction) / mean(assets) x closeadj
def ioat_f094_insider_ownership_after_trade_cumper_assets_252d_base_v121_signal(sharesownedfollowingtransaction, assets, closeadj):
    s = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(sharesownedfollowingtransaction) / mean(assets) x closeadj
def ioat_f094_insider_ownership_after_trade_cumper_assets_504d_base_v122_signal(sharesownedfollowingtransaction, assets, closeadj):
    s = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_pos_63d_base_v123_signal(sharesownedfollowingtransaction, closeadj):
    pos = sharesownedfollowingtransaction.where(sharesownedfollowingtransaction > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_pos_252d_base_v124_signal(sharesownedfollowingtransaction, closeadj):
    pos = sharesownedfollowingtransaction.where(sharesownedfollowingtransaction > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_neg_63d_base_v125_signal(sharesownedfollowingtransaction, closeadj):
    neg = sharesownedfollowingtransaction.where(sharesownedfollowingtransaction < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_neg_252d_base_v126_signal(sharesownedfollowingtransaction, closeadj):
    neg = sharesownedfollowingtransaction.where(sharesownedfollowingtransaction < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_hl_21d_base_v127_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_hl_63d_base_v128_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_hl_252d_base_v129_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_63d_base_v130_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_126d_base_v131_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_z_1008d_base_v132_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_st_lt_252_21d_base_v133_signal(sharesownedfollowingtransaction, closeadj):
    sm = _mean(sharesownedfollowingtransaction, 21)
    lm = _mean(sharesownedfollowingtransaction, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_st_lt_252_63d_base_v134_signal(sharesownedfollowingtransaction, closeadj):
    sm = _mean(sharesownedfollowingtransaction, 63)
    lm = _mean(sharesownedfollowingtransaction, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_st_lt_504_21d_base_v135_signal(sharesownedfollowingtransaction, closeadj):
    sm = _mean(sharesownedfollowingtransaction, 21)
    lm = _mean(sharesownedfollowingtransaction, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_st_lt_504_63d_base_v136_signal(sharesownedfollowingtransaction, closeadj):
    sm = _mean(sharesownedfollowingtransaction, 63)
    lm = _mean(sharesownedfollowingtransaction, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharesownedfollowingtransaction/transactionshares times closeadj
def ioat_f094_insider_ownership_after_trade_lag_per_transactionshares_21d_base_v137_signal(sharesownedfollowingtransaction, transactionshares, closeadj):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharesownedfollowingtransaction/transactionshares times closeadj
def ioat_f094_insider_ownership_after_trade_lag_per_transactionshares_63d_base_v138_signal(sharesownedfollowingtransaction, transactionshares, closeadj):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharesownedfollowingtransaction/transactionshares times closeadj
def ioat_f094_insider_ownership_after_trade_lag_per_transactionshares_252d_base_v139_signal(sharesownedfollowingtransaction, transactionshares, closeadj):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, transactionshares)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged sharesownedfollowingtransaction/assets times closeadj
def ioat_f094_insider_ownership_after_trade_lag_per_assets_21d_base_v140_signal(sharesownedfollowingtransaction, assets, closeadj):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged sharesownedfollowingtransaction/assets times closeadj
def ioat_f094_insider_ownership_after_trade_lag_per_assets_63d_base_v141_signal(sharesownedfollowingtransaction, assets, closeadj):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged sharesownedfollowingtransaction/assets times closeadj
def ioat_f094_insider_ownership_after_trade_lag_per_assets_252d_base_v142_signal(sharesownedfollowingtransaction, assets, closeadj):
    r = _insider_ownership_after_trade_scaled(sharesownedfollowingtransaction, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |sharesownedfollowingtransaction| times closeadj
def ioat_f094_insider_ownership_after_trade_abssum_63d_base_v143_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |sharesownedfollowingtransaction| times closeadj
def ioat_f094_insider_ownership_after_trade_abssum_252d_base_v144_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |sharesownedfollowingtransaction| times closeadj
def ioat_f094_insider_ownership_after_trade_abssum_504d_base_v145_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_acf1_252d_base_v146_signal(sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_acf1_504d_base_v147_signal(sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_posinrange_252d_base_v148_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 252)
    hi = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).max()
    lo = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of sharesownedfollowingtransaction
def ioat_f094_insider_ownership_after_trade_posinrange_504d_base_v149_signal(sharesownedfollowingtransaction):
    m = _mean(sharesownedfollowingtransaction, 504)
    hi = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).max()
    lo = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of sharesownedfollowingtransaction times closeadj
def ioat_f094_insider_ownership_after_trade_hl_5d_base_v150_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
