"""Family f77 - Price / book  (M_Valuation) | base 076-150"""
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
def _price_book_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _price_book_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _price_book_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 504d log of pb/marketcap
def pb_f77_price_book_log_per_marketcap_504d_base_v076_signal(pb, marketcap):
    s = _price_book_scaled(pb, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of pb/equity
def pb_f77_price_book_log_per_equity_252d_base_v077_signal(pb, equity):
    s = _price_book_scaled(pb, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of pb/equity
def pb_f77_price_book_log_per_equity_504d_base_v078_signal(pb, equity):
    s = _price_book_scaled(pb, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=21) of pb times closeadj
def pb_f77_price_book_ewm_21d_base_v079_signal(pb, closeadj):
    result = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=63) of pb times closeadj
def pb_f77_price_book_ewm_63d_base_v080_signal(pb, closeadj):
    result = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# EWM(span=252) of pb times closeadj
def pb_f77_price_book_ewm_252d_base_v081_signal(pb, closeadj):
    result = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling median of pb times closeadj
def pb_f77_price_book_med_63d_base_v082_signal(pb, closeadj):
    result = pb.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling median of pb times closeadj
def pb_f77_price_book_med_252d_base_v083_signal(pb, closeadj):
    result = pb.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling median of pb times closeadj
def pb_f77_price_book_med_504d_base_v084_signal(pb, closeadj):
    result = pb.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling skew of pb
def pb_f77_price_book_skew_252d_base_v085_signal(pb):
    result = pb.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling skew of pb
def pb_f77_price_book_skew_504d_base_v086_signal(pb):
    result = pb.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling kurtosis of pb
def pb_f77_price_book_kurt_252d_base_v087_signal(pb):
    result = pb.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling kurtosis of pb
def pb_f77_price_book_kurt_504d_base_v088_signal(pb):
    result = pb.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of pb times closeadj
def pb_f77_price_book_rank_252d_base_v089_signal(pb, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = pb.rolling(252, min_periods=max(1, 252//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of pb times closeadj
def pb_f77_price_book_rank_504d_base_v090_signal(pb, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = pb.rolling(504, min_periods=max(1, 504//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d percentile rank of pb times closeadj
def pb_f77_price_book_rank_1008d_base_v091_signal(pb, closeadj):
    def _rank(x):
        if len(x) < 2: return np.nan
        return (x.rank(pct=True).iloc[-1])
    result = pb.rolling(1008, min_periods=max(1, 1008//2)).apply(_rank, raw=False) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of pb from 63d mean times closeadj
def pb_f77_price_book_devmean_63d_base_v092_signal(pb, closeadj):
    m = _mean(pb, 63)
    result = (pb - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of pb from 252d mean times closeadj
def pb_f77_price_book_devmean_252d_base_v093_signal(pb, closeadj):
    m = _mean(pb, 252)
    result = (pb - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deviation of pb from 504d mean times closeadj
def pb_f77_price_book_devmean_504d_base_v094_signal(pb, closeadj):
    m = _mean(pb, 504)
    result = (pb - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-difference of pb times closeadj
def pb_f77_price_book_logdiff_21d_base_v095_signal(pb, closeadj):
    lr = _price_book_log(pb)
    result = _diff(lr, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-difference of pb times closeadj
def pb_f77_price_book_logdiff_63d_base_v096_signal(pb, closeadj):
    lr = _price_book_log(pb)
    result = _diff(lr, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-difference of pb times closeadj
def pb_f77_price_book_logdiff_252d_base_v097_signal(pb, closeadj):
    lr = _price_book_log(pb)
    result = _diff(lr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling range of pb times closeadj
def pb_f77_price_book_range_63d_base_v098_signal(pb, closeadj):
    hi = pb.rolling(63, min_periods=max(1, 63//2)).max()
    lo = pb.rolling(63, min_periods=max(1, 63//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling range of pb times closeadj
def pb_f77_price_book_range_252d_base_v099_signal(pb, closeadj):
    hi = pb.rolling(252, min_periods=max(1, 252//2)).max()
    lo = pb.rolling(252, min_periods=max(1, 252//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling range of pb times closeadj
def pb_f77_price_book_range_504d_base_v100_signal(pb, closeadj):
    hi = pb.rolling(504, min_periods=max(1, 504//2)).max()
    lo = pb.rolling(504, min_periods=max(1, 504//2)).min()
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 252d mean times closeadj
def pb_f77_price_book_rel_252d_base_v101_signal(pb, closeadj):
    m = _mean(pb, 252).replace(0, np.nan)
    result = (pb / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 504d mean times closeadj
def pb_f77_price_book_rel_504d_base_v102_signal(pb, closeadj):
    m = _mean(pb, 504).replace(0, np.nan)
    result = (pb / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative to 1008d mean times closeadj
def pb_f77_price_book_rel_1008d_base_v103_signal(pb, closeadj):
    m = _mean(pb, 1008).replace(0, np.nan)
    result = (pb / m.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pb/assets 63d mean
def pb_f77_price_book_sqnorm_assets_63d_base_v104_signal(pb, assets):
    r = _price_book_scaled(pb, assets)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pb/assets 252d mean
def pb_f77_price_book_sqnorm_assets_252d_base_v105_signal(pb, assets):
    r = _price_book_scaled(pb, assets)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pb/marketcap 63d mean
def pb_f77_price_book_sqnorm_marketcap_63d_base_v106_signal(pb, marketcap):
    r = _price_book_scaled(pb, marketcap)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pb/marketcap 252d mean
def pb_f77_price_book_sqnorm_marketcap_252d_base_v107_signal(pb, marketcap):
    r = _price_book_scaled(pb, marketcap)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pb/equity 63d mean
def pb_f77_price_book_sqnorm_equity_63d_base_v108_signal(pb, equity):
    r = _price_book_scaled(pb, equity)
    result = _mean(r, 63) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-normalized pb/equity 252d mean
def pb_f77_price_book_sqnorm_equity_252d_base_v109_signal(pb, equity):
    r = _price_book_scaled(pb, equity)
    result = _mean(r, 252) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean/std of pb times closeadj
def pb_f77_price_book_infrat_63d_base_v110_signal(pb, closeadj):
    m = _mean(pb, 63)
    s = _std(pb, 63).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean/std of pb times closeadj
def pb_f77_price_book_infrat_252d_base_v111_signal(pb, closeadj):
    m = _mean(pb, 252)
    s = _std(pb, 252).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean/std of pb times closeadj
def pb_f77_price_book_infrat_504d_base_v112_signal(pb, closeadj):
    m = _mean(pb, 504)
    s = _std(pb, 504).replace(0, np.nan)
    result = (m / s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of pb
def pb_f77_price_book_cv_252d_base_v113_signal(pb):
    m = _mean(pb, 252).abs().replace(0, np.nan)
    s = _std(pb, 252)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 504d coefficient of variation of pb
def pb_f77_price_book_cv_504d_base_v114_signal(pb):
    m = _mean(pb, 504).abs().replace(0, np.nan)
    s = _std(pb, 504)
    result = s / m
    return result.replace([np.inf, -np.inf], np.nan)


# 5d lagged pb times closeadj
def pb_f77_price_book_lag_5d_base_v115_signal(pb, closeadj):
    result = pb.shift(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged pb times closeadj
def pb_f77_price_book_lag_21d_base_v116_signal(pb, closeadj):
    result = pb.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged pb times closeadj
def pb_f77_price_book_lag_63d_base_v117_signal(pb, closeadj):
    result = pb.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged pb times closeadj
def pb_f77_price_book_lag_252d_base_v118_signal(pb, closeadj):
    result = pb.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(pb) / mean(assets) x closeadj
def pb_f77_price_book_cumper_assets_252d_base_v119_signal(pb, assets, closeadj):
    s = pb.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(assets, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(pb) / mean(assets) x closeadj
def pb_f77_price_book_cumper_assets_504d_base_v120_signal(pb, assets, closeadj):
    s = pb.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(assets, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumsum(pb) / mean(marketcap) x closeadj
def pb_f77_price_book_cumper_marketcap_252d_base_v121_signal(pb, marketcap, closeadj):
    s = pb.rolling(252, min_periods=max(1, 252//2)).sum()
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumsum(pb) / mean(marketcap) x closeadj
def pb_f77_price_book_cumper_marketcap_504d_base_v122_signal(pb, marketcap, closeadj):
    s = pb.rolling(504, min_periods=max(1, 504//2)).sum()
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (s / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of positive-only pb times closeadj
def pb_f77_price_book_pos_63d_base_v123_signal(pb, closeadj):
    pos = pb.where(pb > 0, 0)
    result = _mean(pos, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of positive-only pb times closeadj
def pb_f77_price_book_pos_252d_base_v124_signal(pb, closeadj):
    pos = pb.where(pb > 0, 0)
    result = _mean(pos, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of negative-only pb times closeadj
def pb_f77_price_book_neg_63d_base_v125_signal(pb, closeadj):
    neg = pb.where(pb < 0, 0)
    result = _mean(neg, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of negative-only pb times closeadj
def pb_f77_price_book_neg_252d_base_v126_signal(pb, closeadj):
    neg = pb.where(pb < 0, 0)
    result = _mean(neg, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=21 EWM of pb times closeadj
def pb_f77_price_book_hl_21d_base_v127_signal(pb, closeadj):
    result = pb.ewm(halflife=21, min_periods=max(1, 21//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=63 EWM of pb times closeadj
def pb_f77_price_book_hl_63d_base_v128_signal(pb, closeadj):
    result = pb.ewm(halflife=63, min_periods=max(1, 63//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=252 EWM of pb times closeadj
def pb_f77_price_book_hl_252d_base_v129_signal(pb, closeadj):
    result = pb.ewm(halflife=252, min_periods=max(1, 252//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d zscore of pb
def pb_f77_price_book_z_63d_base_v130_signal(pb):
    result = _z(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d zscore of pb
def pb_f77_price_book_z_126d_base_v131_signal(pb):
    result = _z(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d zscore of pb
def pb_f77_price_book_z_1008d_base_v132_signal(pb):
    result = _z(pb, 1008)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/252d mean ratio of pb times closeadj
def pb_f77_price_book_st_lt_252_21d_base_v133_signal(pb, closeadj):
    sm = _mean(pb, 21)
    lm = _mean(pb, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d mean ratio of pb times closeadj
def pb_f77_price_book_st_lt_252_63d_base_v134_signal(pb, closeadj):
    sm = _mean(pb, 63)
    lm = _mean(pb, 252).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/504d mean ratio of pb times closeadj
def pb_f77_price_book_st_lt_504_21d_base_v135_signal(pb, closeadj):
    sm = _mean(pb, 21)
    lm = _mean(pb, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/504d mean ratio of pb times closeadj
def pb_f77_price_book_st_lt_504_63d_base_v136_signal(pb, closeadj):
    sm = _mean(pb, 63)
    lm = _mean(pb, 504).replace(0, np.nan)
    result = (sm / lm.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged pb/assets times closeadj
def pb_f77_price_book_lag_per_assets_21d_base_v137_signal(pb, assets, closeadj):
    r = _price_book_scaled(pb, assets)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged pb/assets times closeadj
def pb_f77_price_book_lag_per_assets_63d_base_v138_signal(pb, assets, closeadj):
    r = _price_book_scaled(pb, assets)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged pb/assets times closeadj
def pb_f77_price_book_lag_per_assets_252d_base_v139_signal(pb, assets, closeadj):
    r = _price_book_scaled(pb, assets)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d lagged pb/marketcap times closeadj
def pb_f77_price_book_lag_per_marketcap_21d_base_v140_signal(pb, marketcap, closeadj):
    r = _price_book_scaled(pb, marketcap)
    result = r.shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d lagged pb/marketcap times closeadj
def pb_f77_price_book_lag_per_marketcap_63d_base_v141_signal(pb, marketcap, closeadj):
    r = _price_book_scaled(pb, marketcap)
    result = r.shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d lagged pb/marketcap times closeadj
def pb_f77_price_book_lag_per_marketcap_252d_base_v142_signal(pb, marketcap, closeadj):
    r = _price_book_scaled(pb, marketcap)
    result = r.shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of |pb| times closeadj
def pb_f77_price_book_abssum_63d_base_v143_signal(pb, closeadj):
    result = pb.abs().rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of |pb| times closeadj
def pb_f77_price_book_abssum_252d_base_v144_signal(pb, closeadj):
    result = pb.abs().rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of |pb| times closeadj
def pb_f77_price_book_abssum_504d_base_v145_signal(pb, closeadj):
    result = pb.abs().rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling autocorr(1) of pb
def pb_f77_price_book_acf1_252d_base_v146_signal(pb):
    result = pb.rolling(252, min_periods=max(1, 252//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling autocorr(1) of pb
def pb_f77_price_book_acf1_504d_base_v147_signal(pb):
    result = pb.rolling(504, min_periods=max(1, 504//2)).apply(lambda x: x.autocorr(lag=1) if len(x) > 2 else np.nan, raw=False)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of pb
def pb_f77_price_book_posinrange_252d_base_v148_signal(pb):
    m = _mean(pb, 252)
    hi = pb.rolling(252, min_periods=max(1, 252//2)).max()
    lo = pb.rolling(252, min_periods=max(1, 252//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of pb
def pb_f77_price_book_posinrange_504d_base_v149_signal(pb):
    m = _mean(pb, 504)
    hi = pb.rolling(504, min_periods=max(1, 504//2)).max()
    lo = pb.rolling(504, min_periods=max(1, 504//2)).min()
    result = (m - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# halflife=5 EWM of pb times closeadj
def pb_f77_price_book_hl_5d_base_v150_signal(pb, closeadj):
    result = pb.ewm(halflife=5, min_periods=max(1, 5//2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
