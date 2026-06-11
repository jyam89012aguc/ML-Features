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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f048_momentum(close, w):
    return close.pct_change(periods=w)


def _f048_rank_proxy(close, w):
    mn = close.rolling(w, min_periods=max(1, w // 2)).min()
    mx = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close - mn) / (mx - mn).replace(0, np.nan)


def _f048_momentum_quantile(close, w):
    mom = close.pct_change(periods=w)
    mn = mom.rolling(w, min_periods=max(1, w // 2)).min()
    mx = mom.rolling(w, min_periods=max(1, w // 2)).max()
    return ((mom - mn) / (mx - mn).replace(0, np.nan)) * close


def _make_slope(base_concept_fn, base_window, slope_window, mult_fn=None):
    """Helper used inline; we don't call it directly to keep primitive checks."""
    pass


# 5d slope of 21d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_21d_jerk_v001_signal(closeadj):
    base = _f048_momentum(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_63d_jerk_v002_signal(closeadj):
    base = _f048_momentum(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_126d_jerk_v003_signal(closeadj):
    base = _f048_momentum(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_252d_jerk_v004_signal(closeadj):
    base = _f048_momentum(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_504d_jerk_v005_signal(closeadj):
    base = _f048_momentum(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rs new high × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh_21d_jerk_v006_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs new high × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh_63d_jerk_v007_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rs new high × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh_126d_jerk_v008_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs new high × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh_252d_jerk_v009_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d rs new high × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh_504d_jerk_v010_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d leadership rate × close
def f048csm_f048_cross_sectional_momentum_rank_lead_21d_jerk_v011_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 21) / closeadj.replace(0, np.nan)
    base = _mean(lc, 21) * closeadj * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d leadership × close
def f048csm_f048_cross_sectional_momentum_rank_lead_63d_jerk_v012_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 63) / closeadj.replace(0, np.nan)
    base = _mean(lc, 63) * closeadj * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d leadership × close
def f048csm_f048_cross_sectional_momentum_rank_lead_126d_jerk_v013_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 126) / closeadj.replace(0, np.nan)
    base = _mean(lc, 126) * closeadj * _mean(closeadj, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d leadership × close
def f048csm_f048_cross_sectional_momentum_rank_lead_252d_jerk_v014_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 252) / closeadj.replace(0, np.nan)
    base = _mean(lc, 252) * closeadj * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d leadership × close
def f048csm_f048_cross_sectional_momentum_rank_lead_504d_jerk_v015_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 504) / closeadj.replace(0, np.nan)
    base = _mean(lc, 504) * closeadj * _mean(closeadj, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rs gap × close
def f048csm_f048_cross_sectional_momentum_rank_rsgap_21d_jerk_v016_signal(closeadj):
    base = (_f048_momentum(closeadj, 21) - 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs gap × close
def f048csm_f048_cross_sectional_momentum_rank_rsgap_63d_jerk_v017_signal(closeadj):
    base = (_f048_momentum(closeadj, 63) - 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rs gap
def f048csm_f048_cross_sectional_momentum_rank_rsgap_126d_jerk_v018_signal(closeadj):
    base = (_f048_momentum(closeadj, 126) - 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs gap
def f048csm_f048_cross_sectional_momentum_rank_rsgap_252d_jerk_v019_signal(closeadj):
    base = (_f048_momentum(closeadj, 252) - 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d rs gap
def f048csm_f048_cross_sectional_momentum_rank_rsgap_504d_jerk_v020_signal(closeadj):
    base = (_f048_momentum(closeadj, 504) - 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d rs z (252)
def f048csm_f048_cross_sectional_momentum_rank_rsz_21d_jerk_v021_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 21), 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs z (252)
def f048csm_f048_cross_sectional_momentum_rank_rsz_63d_jerk_v022_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 63), 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d rs z (504)
def f048csm_f048_cross_sectional_momentum_rank_rsz_126d_jerk_v023_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 126), 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs z (504)
def f048csm_f048_cross_sectional_momentum_rank_rsz_252d_jerk_v024_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 252), 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs EMA 21 × close
def f048csm_f048_cross_sectional_momentum_rank_rsema_21d_jerk_v025_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    base = rs.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs EMA 63 × close
def f048csm_f048_cross_sectional_momentum_rank_rsema_63d_jerk_v026_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    base = rs.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs EMA 126 × close
def f048csm_f048_cross_sectional_momentum_rank_rsema_126d_jerk_v027_signal(closeadj):
    rs = _f048_momentum(closeadj, 126)
    base = rs.ewm(span=126, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs EMA 252 × close
def f048csm_f048_cross_sectional_momentum_rank_rsema_252d_jerk_v028_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    base = rs.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high count 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhcount_252d_jerk_v029_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at_high = (rs >= rs_max).astype(float)
    base = at_high.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high count 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhcount_63d_jerk_v030_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    rs_max = rs.rolling(21, min_periods=5).max()
    at_high = (rs >= rs_max).astype(float)
    base = at_high.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs new-high count 504d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhcount_504d_jerk_v031_signal(closeadj):
    rs = _f048_momentum(closeadj, 126)
    rs_max = rs.rolling(126, min_periods=42).max()
    at_high = (rs >= rs_max).astype(float)
    base = at_high.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 63v252
def f048csm_f048_cross_sectional_momentum_rank_rsratio_63v252_jerk_v032_signal(closeadj):
    a = _f048_momentum(closeadj, 63)
    b = _f048_momentum(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 21v126
def f048csm_f048_cross_sectional_momentum_rank_rsratio_21v126_jerk_v033_signal(closeadj):
    a = _f048_momentum(closeadj, 21)
    b = _f048_momentum(closeadj, 126).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs ratio 252v504
def f048csm_f048_cross_sectional_momentum_rank_rsratio_252v504_jerk_v034_signal(closeadj):
    a = _f048_momentum(closeadj, 252)
    b = _f048_momentum(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs diff 21m63
def f048csm_f048_cross_sectional_momentum_rank_rsdiff_21m63_jerk_v035_signal(closeadj):
    base = (_f048_momentum(closeadj, 21) - _f048_momentum(closeadj, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs diff 63m252
def f048csm_f048_cross_sectional_momentum_rank_rsdiff_63m252_jerk_v036_signal(closeadj):
    base = (_f048_momentum(closeadj, 63) - _f048_momentum(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs diff 126m504
def f048csm_f048_cross_sectional_momentum_rank_rsdiff_126m504_jerk_v037_signal(closeadj):
    base = (_f048_momentum(closeadj, 126) - _f048_momentum(closeadj, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_5d_jerk_v038_signal(closeadj):
    base = _f048_momentum(closeadj, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_10d_jerk_v039_signal(closeadj):
    base = _f048_momentum(closeadj, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_42d_jerk_v040_signal(closeadj):
    base = _f048_momentum(closeadj, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_189d_jerk_v041_signal(closeadj):
    base = _f048_momentum(closeadj, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d rs line × close
def f048csm_f048_cross_sectional_momentum_rank_rsline_378d_jerk_v042_signal(closeadj):
    base = _f048_momentum(closeadj, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high × mean close 21d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxmean_21d_jerk_v043_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high × mean close 63d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxmean_63d_jerk_v044_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 63) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs new-high × mean close 252d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxmean_252d_jerk_v045_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 252) * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs std 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsstd_21d_jerk_v046_signal(closeadj):
    base = _std(_f048_momentum(closeadj, 21), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs std 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsstd_63d_jerk_v047_signal(closeadj):
    base = _std(_f048_momentum(closeadj, 63), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs std 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsstd_252d_jerk_v048_signal(closeadj):
    base = _std(_f048_momentum(closeadj, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs squared 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rssq_21d_jerk_v049_signal(closeadj):
    rs = _f048_momentum(closeadj, 21) - 1.0
    base = rs * rs.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs squared 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rssq_63d_jerk_v050_signal(closeadj):
    rs = _f048_momentum(closeadj, 63) - 1.0
    base = rs * rs.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs squared 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rssq_252d_jerk_v051_signal(closeadj):
    rs = _f048_momentum(closeadj, 252) - 1.0
    base = rs * rs.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs log 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rslog_21d_jerk_v052_signal(closeadj):
    rs = _f048_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.log(rs) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs log 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rslog_63d_jerk_v053_signal(closeadj):
    rs = _f048_momentum(closeadj, 63).replace(0, np.nan).abs()
    base = np.log(rs) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs log 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rslog_252d_jerk_v054_signal(closeadj):
    rs = _f048_momentum(closeadj, 252).replace(0, np.nan).abs()
    base = np.log(rs) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leadership-sum 63d × close
def f048csm_f048_cross_sectional_momentum_rank_leadsum_63d_jerk_v055_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 21) / closeadj.replace(0, np.nan)
    base = lc.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leadership-sum 252d × close
def f048csm_f048_cross_sectional_momentum_rank_leadsum_252d_jerk_v056_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 63) / closeadj.replace(0, np.nan)
    base = lc.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leadership-sum 504d × close
def f048csm_f048_cross_sectional_momentum_rank_leadsum_504d_jerk_v057_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 126) / closeadj.replace(0, np.nan)
    base = lc.rolling(504, min_periods=126).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar-mean 21d
def f048csm_f048_cross_sectional_momentum_rank_rsxdmean_21d_jerk_v058_signal(closeadj):
    base = _f048_momentum(closeadj, 21) * closeadj * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar-mean 63d
def f048csm_f048_cross_sectional_momentum_rank_rsxdmean_63d_jerk_v059_signal(closeadj):
    base = _f048_momentum(closeadj, 63) * closeadj * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × dollar-mean 252d
def f048csm_f048_cross_sectional_momentum_rank_rsxdmean_252d_jerk_v060_signal(closeadj):
    base = _f048_momentum(closeadj, 252) * closeadj * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding rs-new-high × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhexp_jerk_v061_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    rs_max = rs.expanding(min_periods=63).max()
    base = ((rs - rs_max) / rs_max.replace(0, np.nan).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high persistence 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhpersist_21d_jerk_v062_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 63) / closeadj.replace(0, np.nan)
    base = lc.rolling(21, min_periods=5).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs new-high persistence 126d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhpersist_126d_jerk_v063_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 252) / closeadj.replace(0, np.nan)
    base = lc.rolling(126, min_periods=42).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs oscillator 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsosc_21d_jerk_v064_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    base = (rs - rs.ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs oscillator 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsosc_63d_jerk_v065_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    base = (rs - rs.ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs oscillator 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsosc_252d_jerk_v066_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    base = (rs - rs.ewm(span=252, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs range 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsrange_63d_jerk_v067_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    lo = rs.rolling(63, min_periods=21).min()
    hi = rs.rolling(63, min_periods=21).max()
    base = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs range 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsrange_252d_jerk_v068_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    lo = rs.rolling(252, min_periods=63).min()
    hi = rs.rolling(252, min_periods=63).max()
    base = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs range 504d × close
def f048csm_f048_cross_sectional_momentum_rank_rsrange_504d_jerk_v069_signal(closeadj):
    rs = _f048_momentum(closeadj, 504)
    lo = rs.rolling(504, min_periods=126).min()
    hi = rs.rolling(504, min_periods=126).max()
    base = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of days-since-RS-nh 252d × close
def f048csm_f048_cross_sectional_momentum_rank_daysrsnh_252d_jerk_v070_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    rs_max = rs.rolling(252, min_periods=63).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of days-since-RS-nh 63d × close
def f048csm_f048_cross_sectional_momentum_rank_daysrsnh_63d_jerk_v071_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of days-since-RS-nh 504d × close
def f048csm_f048_cross_sectional_momentum_rank_daysrsnh_504d_jerk_v072_signal(closeadj):
    rs = _f048_momentum(closeadj, 504)
    rs_max = rs.rolling(504, min_periods=126).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × leadership rate × close 63d
def f048csm_f048_cross_sectional_momentum_rank_rsxlead_63d_jerk_v073_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 63) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 63) + 0.1
    base = _f048_momentum(closeadj, 63) * rate * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × leadership rate × close 252d
def f048csm_f048_cross_sectional_momentum_rank_rsxlead_252d_jerk_v074_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 252) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 252) + 0.1
    base = _f048_momentum(closeadj, 252) * rate * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs-new-high × ema5 × close 63d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxema5_63d_jerk_v075_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 63) * closeadj * closeadj.ewm(span=5, adjust=False).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs - median 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmed_63d_jerk_v076_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    med = rs.rolling(63, min_periods=21).median()
    base = (rs - med) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs - median 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmed_252d_jerk_v077_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    med = rs.rolling(252, min_periods=63).median()
    base = (rs - med) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs - median 504d × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmed_504d_jerk_v078_signal(closeadj):
    rs = _f048_momentum(closeadj, 504)
    med = rs.rolling(504, min_periods=126).median()
    base = (rs - med) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs max 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsmax_21d_jerk_v079_signal(closeadj):
    base = _f048_momentum(closeadj, 21).rolling(21, min_periods=5).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs max 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsmax_63d_jerk_v080_signal(closeadj):
    base = _f048_momentum(closeadj, 63).rolling(63, min_periods=21).max() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs max 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsmax_252d_jerk_v081_signal(closeadj):
    base = _f048_momentum(closeadj, 252).rolling(252, min_periods=63).max() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs min 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsmin_63d_jerk_v082_signal(closeadj):
    base = _f048_momentum(closeadj, 63).rolling(63, min_periods=21).min() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs min 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsmin_252d_jerk_v083_signal(closeadj):
    base = _f048_momentum(closeadj, 252).rolling(252, min_periods=63).min() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sum 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rssum_21d_jerk_v084_signal(closeadj):
    base = _f048_momentum(closeadj, 21).rolling(21, min_periods=5).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sum 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rssum_63d_jerk_v085_signal(closeadj):
    base = _f048_momentum(closeadj, 63).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs sum 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rssum_252d_jerk_v086_signal(closeadj):
    base = _f048_momentum(closeadj, 252).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh21_jerk_v087_signal(closeadj):
    rs = _f048_momentum(closeadj, 10)
    rs_max = rs.rolling(10, min_periods=3).max()
    flg = (rs >= rs_max).astype(float)
    base = flg.rolling(21, min_periods=5).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh 126d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnh126_jerk_v088_signal(closeadj):
    rs = _f048_momentum(closeadj, 42)
    rs_max = rs.rolling(42, min_periods=10).max()
    flg = (rs >= rs_max).astype(float)
    base = flg.rolling(126, min_periods=42).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh rate 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhrate_252d_jerk_v089_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    flg = (rs >= rs_max).astype(float)
    base = (flg.rolling(252, min_periods=63).sum() / 252.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh rate 504d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhrate_504d_jerk_v090_signal(closeadj):
    rs = _f048_momentum(closeadj, 126)
    rs_max = rs.rolling(126, min_periods=42).max()
    flg = (rs >= rs_max).astype(float)
    base = (flg.rolling(504, min_periods=126).sum() / 504.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs gap × mean 21d
def f048csm_f048_cross_sectional_momentum_rank_rsgxm_21d_jerk_v091_signal(closeadj):
    base = (_f048_momentum(closeadj, 21) - 1.0) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs gap × mean 63d
def f048csm_f048_cross_sectional_momentum_rank_rsgxm_63d_jerk_v092_signal(closeadj):
    base = (_f048_momentum(closeadj, 63) - 1.0) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs gap × mean 252d
def f048csm_f048_cross_sectional_momentum_rank_rsgxm_252d_jerk_v093_signal(closeadj):
    base = (_f048_momentum(closeadj, 252) - 1.0) * _mean(closeadj, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh z 63d
def f048csm_f048_cross_sectional_momentum_rank_rsnhz_63d_jerk_v094_signal(closeadj):
    base = _z(_f048_rank_proxy(closeadj, 63), 252) + _f048_momentum(closeadj, 63) * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh z 252d
def f048csm_f048_cross_sectional_momentum_rank_rsnhz_252d_jerk_v095_signal(closeadj):
    base = _z(_f048_rank_proxy(closeadj, 252), 504) + _f048_momentum(closeadj, 252) * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sign × close 21d
def f048csm_f048_cross_sectional_momentum_rank_rssign_21d_jerk_v096_signal(closeadj):
    rs = _f048_momentum(closeadj, 21) - 1.0
    base = np.sign(rs) * rs.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sign × close 63d
def f048csm_f048_cross_sectional_momentum_rank_rssign_63d_jerk_v097_signal(closeadj):
    rs = _f048_momentum(closeadj, 63) - 1.0
    base = np.sign(rs) * rs.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs sign × close 252d
def f048csm_f048_cross_sectional_momentum_rank_rssign_252d_jerk_v098_signal(closeadj):
    rs = _f048_momentum(closeadj, 252) - 1.0
    base = np.sign(rs) * rs.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × std × close 21d
def f048csm_f048_cross_sectional_momentum_rank_rsxstd_21d_jerk_v099_signal(closeadj):
    base = _f048_momentum(closeadj, 21) * _std(closeadj, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × std × close 63d
def f048csm_f048_cross_sectional_momentum_rank_rsxstd_63d_jerk_v100_signal(closeadj):
    base = _f048_momentum(closeadj, 63) * _std(closeadj, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × std × close 252d
def f048csm_f048_cross_sectional_momentum_rank_rsxstd_252d_jerk_v101_signal(closeadj):
    base = _f048_momentum(closeadj, 252) * _std(closeadj, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs momentum 21v42 × close
def f048csm_f048_cross_sectional_momentum_rank_rsmoment_21v42_jerk_v102_signal(closeadj):
    base = (_f048_momentum(closeadj, 21) - _f048_momentum(closeadj, 42)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs momentum 42v189
def f048csm_f048_cross_sectional_momentum_rank_rsmoment_42v189_jerk_v103_signal(closeadj):
    base = (_f048_momentum(closeadj, 42) - _f048_momentum(closeadj, 189)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs momentum 189v378
def f048csm_f048_cross_sectional_momentum_rank_rsmoment_189v378_jerk_v104_signal(closeadj):
    base = (_f048_momentum(closeadj, 189) - _f048_momentum(closeadj, 378)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 5v21
def f048csm_f048_cross_sectional_momentum_rank_rsratio_5v21_jerk_v105_signal(closeadj):
    base = _f048_momentum(closeadj, 5) / _f048_momentum(closeadj, 21).replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 10v42
def f048csm_f048_cross_sectional_momentum_rank_rsratio_10v42_jerk_v106_signal(closeadj):
    base = _f048_momentum(closeadj, 10) / _f048_momentum(closeadj, 42).replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs ratio 42v189
def f048csm_f048_cross_sectional_momentum_rank_rsratio_42v189_jerk_v107_signal(closeadj):
    base = _f048_momentum(closeadj, 42) / _f048_momentum(closeadj, 189).replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs z 42d
def f048csm_f048_cross_sectional_momentum_rank_rsz_42d_jerk_v108_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 42), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs z 189d
def f048csm_f048_cross_sectional_momentum_rank_rsz_189d_jerk_v109_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 189), 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs z 378d
def f048csm_f048_cross_sectional_momentum_rank_rsz_378d_jerk_v110_signal(closeadj):
    base = _z(_f048_momentum(closeadj, 378), 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh × close^2 63d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxsq_63d_jerk_v111_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 63) * closeadj * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh × close^2 252d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxsq_252d_jerk_v112_signal(closeadj):
    base = _f048_rank_proxy(closeadj, 252) * closeadj * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ema5 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsema5_21d_jerk_v113_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    base = rs.ewm(span=5, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ema10 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsema10_63d_jerk_v114_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    base = rs.ewm(span=10, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs ema42 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsema42_252d_jerk_v115_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    base = rs.ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh mean 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhmean_63d_jerk_v116_signal(closeadj):
    base = _mean(_f048_rank_proxy(closeadj, 21), 63) * closeadj * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh mean 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhmean_252d_jerk_v117_signal(closeadj):
    base = _mean(_f048_rank_proxy(closeadj, 63), 252) * closeadj * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh std 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhstd_63d_jerk_v118_signal(closeadj):
    base = _std(_f048_rank_proxy(closeadj, 21), 63) * closeadj * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh std 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsnhstd_252d_jerk_v119_signal(closeadj):
    base = _std(_f048_rank_proxy(closeadj, 63), 252) * closeadj * _mean(closeadj, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × close - close 21d
def f048csm_f048_cross_sectional_momentum_rank_rsmclose_21d_jerk_v120_signal(closeadj):
    base = (_f048_momentum(closeadj, 21) * closeadj - closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × close - close 63d
def f048csm_f048_cross_sectional_momentum_rank_rsmclose_63d_jerk_v121_signal(closeadj):
    base = (_f048_momentum(closeadj, 63) * closeadj - closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × close - close 252d
def f048csm_f048_cross_sectional_momentum_rank_rsmclose_252d_jerk_v122_signal(closeadj):
    base = (_f048_momentum(closeadj, 252) * closeadj - closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of days-at-nh smoothed 63d × close
def f048csm_f048_cross_sectional_momentum_rank_daysatnh_63d_jerk_v123_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at = (rs >= rs_max).astype(float)
    streak = at * (at.groupby((at != at.shift()).cumsum()).cumcount() + 1)
    base = (streak + _mean(closeadj, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of days-at-nh smoothed 252d × close
def f048csm_f048_cross_sectional_momentum_rank_daysatnh_252d_jerk_v124_signal(closeadj):
    rs = _f048_momentum(closeadj, 252)
    rs_max = rs.rolling(252, min_periods=63).max()
    at = (rs >= rs_max).astype(float)
    streak = at * (at.groupby((at != at.shift()).cumsum()).cumcount() + 1)
    base = (streak + _mean(closeadj, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs geo 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsgeo_21d_jerk_v125_signal(closeadj):
    rs = _f048_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.exp(np.log(rs).rolling(21, min_periods=5).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs geo 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsgeo_63d_jerk_v126_signal(closeadj):
    rs = _f048_momentum(closeadj, 63).replace(0, np.nan).abs()
    base = np.exp(np.log(rs).rolling(63, min_periods=21).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs geo 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsgeo_252d_jerk_v127_signal(closeadj):
    rs = _f048_momentum(closeadj, 252).replace(0, np.nan).abs()
    base = np.exp(np.log(rs).rolling(252, min_periods=63).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × ret 5d × close
def f048csm_f048_cross_sectional_momentum_rank_rsxret_5d_jerk_v128_signal(closeadj):
    ret = closeadj.pct_change(5)
    base = _f048_momentum(closeadj, 21) * ret * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × ret 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsxret_21d_jerk_v129_signal(closeadj):
    ret = closeadj.pct_change(21)
    base = _f048_momentum(closeadj, 63) * ret * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × ret 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsxret_63d_jerk_v130_signal(closeadj):
    ret = closeadj.pct_change(63)
    base = _f048_momentum(closeadj, 252) * ret * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh × ret 5d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxret_5d_jerk_v131_signal(closeadj):
    ret = closeadj.pct_change(5)
    base = _f048_rank_proxy(closeadj, 21) * ret * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh × ret 21d
def f048csm_f048_cross_sectional_momentum_rank_rsnhxret_21d_jerk_v132_signal(closeadj):
    ret = closeadj.pct_change(21)
    base = _f048_rank_proxy(closeadj, 63) * ret * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs abs gap 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsabsgap_21d_jerk_v133_signal(closeadj):
    base = (_f048_momentum(closeadj, 21) - 1.0).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs abs gap 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsabsgap_63d_jerk_v134_signal(closeadj):
    base = (_f048_momentum(closeadj, 63) - 1.0).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs abs gap 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsabsgap_252d_jerk_v135_signal(closeadj):
    base = (_f048_momentum(closeadj, 252) - 1.0).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × log close 21d
def f048csm_f048_cross_sectional_momentum_rank_rsxlog_21d_jerk_v136_signal(closeadj):
    base = _f048_momentum(closeadj, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × log close 252d
def f048csm_f048_cross_sectional_momentum_rank_rsxlog_252d_jerk_v137_signal(closeadj):
    base = _f048_momentum(closeadj, 252) * np.log(closeadj.replace(0, np.nan).abs())
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh osc 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rsoscnh_21d_jerk_v138_signal(closeadj):
    rs = _f048_momentum(closeadj, 10)
    rs_max = rs.rolling(21, min_periods=5).max()
    base = (rs - rs_max) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh osc 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsoscnh_63d_jerk_v139_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    rs_max = rs.rolling(63, min_periods=21).max()
    base = (rs - rs_max) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh osc 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsoscnh_252d_jerk_v140_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    rs_max = rs.rolling(252, min_periods=63).max()
    base = (rs - rs_max) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar^2 21d
def f048csm_f048_cross_sectional_momentum_rank_rsxdsq_21d_jerk_v141_signal(closeadj):
    base = _f048_momentum(closeadj, 21) * closeadj * _mean(closeadj, 21) * _mean(closeadj, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar^2 63d
def f048csm_f048_cross_sectional_momentum_rank_rsxdsq_63d_jerk_v142_signal(closeadj):
    base = _f048_momentum(closeadj, 63) * closeadj * _mean(closeadj, 63) * _mean(closeadj, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs/max 63d × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmax_63d_jerk_v143_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    rs_max = rs.rolling(63, min_periods=21).max().replace(0, np.nan)
    base = (rs / rs_max) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs/max 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmax_252d_jerk_v144_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    rs_max = rs.rolling(252, min_periods=63).max().replace(0, np.nan)
    base = (rs / rs_max) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs/max 504d × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmax_504d_jerk_v145_signal(closeadj):
    rs = _f048_momentum(closeadj, 126)
    rs_max = rs.rolling(504, min_periods=126).max().replace(0, np.nan)
    base = (rs / rs_max) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs - mean(rs, 504d) × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmean_504d_jerk_v146_signal(closeadj):
    rs = _f048_momentum(closeadj, 63)
    base = (rs - _mean(rs, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs - mean(rs, 252d) × close
def f048csm_f048_cross_sectional_momentum_rank_rsdmean_252d_jerk_v147_signal(closeadj):
    rs = _f048_momentum(closeadj, 21)
    base = (rs - _mean(rs, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs cum log 21d × close
def f048csm_f048_cross_sectional_momentum_rank_rscum_21d_jerk_v148_signal(closeadj):
    rs = _f048_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.log(rs).rolling(21, min_periods=5).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs cum log 252d × close
def f048csm_f048_cross_sectional_momentum_rank_rscum_252d_jerk_v149_signal(closeadj):
    rs = _f048_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.log(rs).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × leadership smoothed × close 126d
def f048csm_f048_cross_sectional_momentum_rank_rsxleadsm_126d_jerk_v150_signal(closeadj):
    lc = _f048_momentum_quantile(closeadj, 126) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 126) + 0.1
    base = _f048_momentum(closeadj, 126) * rate * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f048csm_f048_cross_sectional_momentum_rank_rsline_21d_jerk_v001_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_63d_jerk_v002_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_126d_jerk_v003_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_252d_jerk_v004_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_504d_jerk_v005_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh_21d_jerk_v006_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh_63d_jerk_v007_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh_126d_jerk_v008_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh_252d_jerk_v009_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh_504d_jerk_v010_signal,
    f048csm_f048_cross_sectional_momentum_rank_lead_21d_jerk_v011_signal,
    f048csm_f048_cross_sectional_momentum_rank_lead_63d_jerk_v012_signal,
    f048csm_f048_cross_sectional_momentum_rank_lead_126d_jerk_v013_signal,
    f048csm_f048_cross_sectional_momentum_rank_lead_252d_jerk_v014_signal,
    f048csm_f048_cross_sectional_momentum_rank_lead_504d_jerk_v015_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgap_21d_jerk_v016_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgap_63d_jerk_v017_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgap_126d_jerk_v018_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgap_252d_jerk_v019_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgap_504d_jerk_v020_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_21d_jerk_v021_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_63d_jerk_v022_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_126d_jerk_v023_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_252d_jerk_v024_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema_21d_jerk_v025_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema_63d_jerk_v026_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema_126d_jerk_v027_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema_252d_jerk_v028_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhcount_252d_jerk_v029_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhcount_63d_jerk_v030_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhcount_504d_jerk_v031_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsratio_63v252_jerk_v032_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsratio_21v126_jerk_v033_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsratio_252v504_jerk_v034_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdiff_21m63_jerk_v035_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdiff_63m252_jerk_v036_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdiff_126m504_jerk_v037_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_5d_jerk_v038_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_10d_jerk_v039_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_42d_jerk_v040_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_189d_jerk_v041_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsline_378d_jerk_v042_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxmean_21d_jerk_v043_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxmean_63d_jerk_v044_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxmean_252d_jerk_v045_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsstd_21d_jerk_v046_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsstd_63d_jerk_v047_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsstd_252d_jerk_v048_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssq_21d_jerk_v049_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssq_63d_jerk_v050_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssq_252d_jerk_v051_signal,
    f048csm_f048_cross_sectional_momentum_rank_rslog_21d_jerk_v052_signal,
    f048csm_f048_cross_sectional_momentum_rank_rslog_63d_jerk_v053_signal,
    f048csm_f048_cross_sectional_momentum_rank_rslog_252d_jerk_v054_signal,
    f048csm_f048_cross_sectional_momentum_rank_leadsum_63d_jerk_v055_signal,
    f048csm_f048_cross_sectional_momentum_rank_leadsum_252d_jerk_v056_signal,
    f048csm_f048_cross_sectional_momentum_rank_leadsum_504d_jerk_v057_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxdmean_21d_jerk_v058_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxdmean_63d_jerk_v059_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxdmean_252d_jerk_v060_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhexp_jerk_v061_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhpersist_21d_jerk_v062_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhpersist_126d_jerk_v063_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsosc_21d_jerk_v064_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsosc_63d_jerk_v065_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsosc_252d_jerk_v066_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsrange_63d_jerk_v067_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsrange_252d_jerk_v068_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsrange_504d_jerk_v069_signal,
    f048csm_f048_cross_sectional_momentum_rank_daysrsnh_252d_jerk_v070_signal,
    f048csm_f048_cross_sectional_momentum_rank_daysrsnh_63d_jerk_v071_signal,
    f048csm_f048_cross_sectional_momentum_rank_daysrsnh_504d_jerk_v072_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxlead_63d_jerk_v073_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxlead_252d_jerk_v074_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxema5_63d_jerk_v075_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmed_63d_jerk_v076_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmed_252d_jerk_v077_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmed_504d_jerk_v078_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmax_21d_jerk_v079_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmax_63d_jerk_v080_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmax_252d_jerk_v081_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmin_63d_jerk_v082_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmin_252d_jerk_v083_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssum_21d_jerk_v084_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssum_63d_jerk_v085_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssum_252d_jerk_v086_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh21_jerk_v087_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnh126_jerk_v088_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhrate_252d_jerk_v089_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhrate_504d_jerk_v090_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgxm_21d_jerk_v091_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgxm_63d_jerk_v092_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgxm_252d_jerk_v093_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhz_63d_jerk_v094_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhz_252d_jerk_v095_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssign_21d_jerk_v096_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssign_63d_jerk_v097_signal,
    f048csm_f048_cross_sectional_momentum_rank_rssign_252d_jerk_v098_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxstd_21d_jerk_v099_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxstd_63d_jerk_v100_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxstd_252d_jerk_v101_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmoment_21v42_jerk_v102_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmoment_42v189_jerk_v103_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmoment_189v378_jerk_v104_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsratio_5v21_jerk_v105_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsratio_10v42_jerk_v106_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsratio_42v189_jerk_v107_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_42d_jerk_v108_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_189d_jerk_v109_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsz_378d_jerk_v110_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxsq_63d_jerk_v111_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxsq_252d_jerk_v112_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema5_21d_jerk_v113_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema10_63d_jerk_v114_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsema42_252d_jerk_v115_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhmean_63d_jerk_v116_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhmean_252d_jerk_v117_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhstd_63d_jerk_v118_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhstd_252d_jerk_v119_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmclose_21d_jerk_v120_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmclose_63d_jerk_v121_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsmclose_252d_jerk_v122_signal,
    f048csm_f048_cross_sectional_momentum_rank_daysatnh_63d_jerk_v123_signal,
    f048csm_f048_cross_sectional_momentum_rank_daysatnh_252d_jerk_v124_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgeo_21d_jerk_v125_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgeo_63d_jerk_v126_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsgeo_252d_jerk_v127_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxret_5d_jerk_v128_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxret_21d_jerk_v129_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxret_63d_jerk_v130_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxret_5d_jerk_v131_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsnhxret_21d_jerk_v132_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsabsgap_21d_jerk_v133_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsabsgap_63d_jerk_v134_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsabsgap_252d_jerk_v135_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxlog_21d_jerk_v136_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxlog_252d_jerk_v137_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsoscnh_21d_jerk_v138_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsoscnh_63d_jerk_v139_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsoscnh_252d_jerk_v140_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxdsq_21d_jerk_v141_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxdsq_63d_jerk_v142_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmax_63d_jerk_v143_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmax_252d_jerk_v144_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmax_504d_jerk_v145_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmean_504d_jerk_v146_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsdmean_252d_jerk_v147_signal,
    f048csm_f048_cross_sectional_momentum_rank_rscum_21d_jerk_v148_signal,
    f048csm_f048_cross_sectional_momentum_rank_rscum_252d_jerk_v149_signal,
    f048csm_f048_cross_sectional_momentum_rank_rsxleadsm_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F048_CROSS_SECTIONAL_MOMENTUM_RANK_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f048_momentum", "_f048_rank_proxy", "_f048_momentum_quantile")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f048_cross_sectional_momentum_rank_3rd_derivatives_001_150_claude: {n_features} features pass")
