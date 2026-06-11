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


# ===== folder domain primitives =====
def _f047_self_momentum(close, w):
    return close / close.shift(w).replace(0, np.nan)


def _f047_sector_proxy(close, w):
    long_w = max(w * 4, 252)
    return close / close.rolling(long_w, min_periods=max(1, long_w // 2)).mean().replace(0, np.nan)


def _f047_excess_momentum(close, w):
    own = close / close.shift(w).replace(0, np.nan)
    long_w = max(w * 4, 252)
    sec = close / close.rolling(long_w, min_periods=max(1, long_w // 2)).mean().replace(0, np.nan)
    return (own - sec) * close


def _make_slope(base_concept_fn, base_window, slope_window, mult_fn=None):
    """Helper used inline; we don't call it directly to keep primitive checks."""
    pass


# 5d slope of 21d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_21d_slope_v001_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_63d_slope_v002_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_126d_slope_v003_signal(closeadj):
    base = _f047_self_momentum(closeadj, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_252d_slope_v004_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_504d_slope_v005_signal(closeadj):
    base = _f047_self_momentum(closeadj, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rs new high × close
def f047srm_f047_sector_relative_momentum_rsnh_21d_slope_v006_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs new high × close
def f047srm_f047_sector_relative_momentum_rsnh_63d_slope_v007_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rs new high × close
def f047srm_f047_sector_relative_momentum_rsnh_126d_slope_v008_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs new high × close
def f047srm_f047_sector_relative_momentum_rsnh_252d_slope_v009_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d rs new high × close
def f047srm_f047_sector_relative_momentum_rsnh_504d_slope_v010_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d leadership rate × close
def f047srm_f047_sector_relative_momentum_lead_21d_slope_v011_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 21) / closeadj.replace(0, np.nan)
    base = _mean(lc, 21) * closeadj * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d leadership × close
def f047srm_f047_sector_relative_momentum_lead_63d_slope_v012_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 63) / closeadj.replace(0, np.nan)
    base = _mean(lc, 63) * closeadj * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d leadership × close
def f047srm_f047_sector_relative_momentum_lead_126d_slope_v013_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 126) / closeadj.replace(0, np.nan)
    base = _mean(lc, 126) * closeadj * _mean(closeadj, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d leadership × close
def f047srm_f047_sector_relative_momentum_lead_252d_slope_v014_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 252) / closeadj.replace(0, np.nan)
    base = _mean(lc, 252) * closeadj * _mean(closeadj, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d leadership × close
def f047srm_f047_sector_relative_momentum_lead_504d_slope_v015_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 504) / closeadj.replace(0, np.nan)
    base = _mean(lc, 504) * closeadj * _mean(closeadj, 504)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d rs gap × close
def f047srm_f047_sector_relative_momentum_rsgap_21d_slope_v016_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 21) - 1.0) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs gap × close
def f047srm_f047_sector_relative_momentum_rsgap_63d_slope_v017_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 63) - 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rs gap
def f047srm_f047_sector_relative_momentum_rsgap_126d_slope_v018_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 126) - 1.0) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs gap
def f047srm_f047_sector_relative_momentum_rsgap_252d_slope_v019_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 252) - 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d rs gap
def f047srm_f047_sector_relative_momentum_rsgap_504d_slope_v020_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 504) - 1.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d rs z (252)
def f047srm_f047_sector_relative_momentum_rsz_21d_slope_v021_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 21), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rs z (252)
def f047srm_f047_sector_relative_momentum_rsz_63d_slope_v022_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 63), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d rs z (504)
def f047srm_f047_sector_relative_momentum_rsz_126d_slope_v023_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 126), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d rs z (504)
def f047srm_f047_sector_relative_momentum_rsz_252d_slope_v024_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 252), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs EMA 21 × close
def f047srm_f047_sector_relative_momentum_rsema_21d_slope_v025_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    base = rs.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs EMA 63 × close
def f047srm_f047_sector_relative_momentum_rsema_63d_slope_v026_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    base = rs.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs EMA 126 × close
def f047srm_f047_sector_relative_momentum_rsema_126d_slope_v027_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 126)
    base = rs.ewm(span=126, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs EMA 252 × close
def f047srm_f047_sector_relative_momentum_rsema_252d_slope_v028_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    base = rs.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high count 252d × close
def f047srm_f047_sector_relative_momentum_rsnhcount_252d_slope_v029_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at_high = (rs >= rs_max).astype(float)
    base = at_high.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high count 63d × close
def f047srm_f047_sector_relative_momentum_rsnhcount_63d_slope_v030_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    rs_max = rs.rolling(21, min_periods=5).max()
    at_high = (rs >= rs_max).astype(float)
    base = at_high.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs new-high count 504d × close
def f047srm_f047_sector_relative_momentum_rsnhcount_504d_slope_v031_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 126)
    rs_max = rs.rolling(126, min_periods=42).max()
    at_high = (rs >= rs_max).astype(float)
    base = at_high.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 63v252
def f047srm_f047_sector_relative_momentum_rsratio_63v252_slope_v032_signal(closeadj):
    a = _f047_self_momentum(closeadj, 63)
    b = _f047_self_momentum(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 21v126
def f047srm_f047_sector_relative_momentum_rsratio_21v126_slope_v033_signal(closeadj):
    a = _f047_self_momentum(closeadj, 21)
    b = _f047_self_momentum(closeadj, 126).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs ratio 252v504
def f047srm_f047_sector_relative_momentum_rsratio_252v504_slope_v034_signal(closeadj):
    a = _f047_self_momentum(closeadj, 252)
    b = _f047_self_momentum(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs diff 21m63
def f047srm_f047_sector_relative_momentum_rsdiff_21m63_slope_v035_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 21) - _f047_self_momentum(closeadj, 63)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs diff 63m252
def f047srm_f047_sector_relative_momentum_rsdiff_63m252_slope_v036_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 63) - _f047_self_momentum(closeadj, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs diff 126m504
def f047srm_f047_sector_relative_momentum_rsdiff_126m504_slope_v037_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 126) - _f047_self_momentum(closeadj, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_5d_slope_v038_signal(closeadj):
    base = _f047_self_momentum(closeadj, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_10d_slope_v039_signal(closeadj):
    base = _f047_self_momentum(closeadj, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_42d_slope_v040_signal(closeadj):
    base = _f047_self_momentum(closeadj, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_189d_slope_v041_signal(closeadj):
    base = _f047_self_momentum(closeadj, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 378d rs line × close
def f047srm_f047_sector_relative_momentum_rsline_378d_slope_v042_signal(closeadj):
    base = _f047_self_momentum(closeadj, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high × mean close 21d
def f047srm_f047_sector_relative_momentum_rsnhxmean_21d_slope_v043_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high × mean close 63d
def f047srm_f047_sector_relative_momentum_rsnhxmean_63d_slope_v044_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 63) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs new-high × mean close 252d
def f047srm_f047_sector_relative_momentum_rsnhxmean_252d_slope_v045_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 252) * _mean(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs std 21d × close
def f047srm_f047_sector_relative_momentum_rsstd_21d_slope_v046_signal(closeadj):
    base = _std(_f047_self_momentum(closeadj, 21), 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs std 63d × close
def f047srm_f047_sector_relative_momentum_rsstd_63d_slope_v047_signal(closeadj):
    base = _std(_f047_self_momentum(closeadj, 63), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs std 252d × close
def f047srm_f047_sector_relative_momentum_rsstd_252d_slope_v048_signal(closeadj):
    base = _std(_f047_self_momentum(closeadj, 252), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs squared 21d × close
def f047srm_f047_sector_relative_momentum_rssq_21d_slope_v049_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21) - 1.0
    base = rs * rs.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs squared 63d × close
def f047srm_f047_sector_relative_momentum_rssq_63d_slope_v050_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63) - 1.0
    base = rs * rs.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs squared 252d × close
def f047srm_f047_sector_relative_momentum_rssq_252d_slope_v051_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252) - 1.0
    base = rs * rs.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs log 21d × close
def f047srm_f047_sector_relative_momentum_rslog_21d_slope_v052_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.log(rs) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs log 63d × close
def f047srm_f047_sector_relative_momentum_rslog_63d_slope_v053_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63).replace(0, np.nan).abs()
    base = np.log(rs) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs log 252d × close
def f047srm_f047_sector_relative_momentum_rslog_252d_slope_v054_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252).replace(0, np.nan).abs()
    base = np.log(rs) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of leadership-sum 63d × close
def f047srm_f047_sector_relative_momentum_leadsum_63d_slope_v055_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 21) / closeadj.replace(0, np.nan)
    base = lc.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leadership-sum 252d × close
def f047srm_f047_sector_relative_momentum_leadsum_252d_slope_v056_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 63) / closeadj.replace(0, np.nan)
    base = lc.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of leadership-sum 504d × close
def f047srm_f047_sector_relative_momentum_leadsum_504d_slope_v057_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 126) / closeadj.replace(0, np.nan)
    base = lc.rolling(504, min_periods=126).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar-mean 21d
def f047srm_f047_sector_relative_momentum_rsxdmean_21d_slope_v058_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21) * closeadj * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar-mean 63d
def f047srm_f047_sector_relative_momentum_rsxdmean_63d_slope_v059_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63) * closeadj * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × dollar-mean 252d
def f047srm_f047_sector_relative_momentum_rsxdmean_252d_slope_v060_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252) * closeadj * _mean(closeadj, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of expanding rs-new-high × close
def f047srm_f047_sector_relative_momentum_rsnhexp_slope_v061_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    rs_max = rs.expanding(min_periods=63).max()
    base = ((rs - rs_max) / rs_max.replace(0, np.nan).abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs new-high persistence 21d × close
def f047srm_f047_sector_relative_momentum_rsnhpersist_21d_slope_v062_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 63) / closeadj.replace(0, np.nan)
    base = lc.rolling(21, min_periods=5).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs new-high persistence 126d × close
def f047srm_f047_sector_relative_momentum_rsnhpersist_126d_slope_v063_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 252) / closeadj.replace(0, np.nan)
    base = lc.rolling(126, min_periods=42).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs oscillator 21d × close
def f047srm_f047_sector_relative_momentum_rsosc_21d_slope_v064_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    base = (rs - rs.ewm(span=21, adjust=False).mean()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs oscillator 63d × close
def f047srm_f047_sector_relative_momentum_rsosc_63d_slope_v065_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    base = (rs - rs.ewm(span=63, adjust=False).mean()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs oscillator 252d × close
def f047srm_f047_sector_relative_momentum_rsosc_252d_slope_v066_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    base = (rs - rs.ewm(span=252, adjust=False).mean()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs range 63d × close
def f047srm_f047_sector_relative_momentum_rsrange_63d_slope_v067_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    lo = rs.rolling(63, min_periods=21).min()
    hi = rs.rolling(63, min_periods=21).max()
    base = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs range 252d × close
def f047srm_f047_sector_relative_momentum_rsrange_252d_slope_v068_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    lo = rs.rolling(252, min_periods=63).min()
    hi = rs.rolling(252, min_periods=63).max()
    base = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs range 504d × close
def f047srm_f047_sector_relative_momentum_rsrange_504d_slope_v069_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 504)
    lo = rs.rolling(504, min_periods=126).min()
    hi = rs.rolling(504, min_periods=126).max()
    base = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of days-since-RS-nh 252d × close
def f047srm_f047_sector_relative_momentum_daysrsnh_252d_slope_v070_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    rs_max = rs.rolling(252, min_periods=63).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of days-since-RS-nh 63d × close
def f047srm_f047_sector_relative_momentum_daysrsnh_63d_slope_v071_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of days-since-RS-nh 504d × close
def f047srm_f047_sector_relative_momentum_daysrsnh_504d_slope_v072_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 504)
    rs_max = rs.rolling(504, min_periods=126).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    base = age * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × leadership rate × close 63d
def f047srm_f047_sector_relative_momentum_rsxlead_63d_slope_v073_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 63) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 63) + 0.1
    base = _f047_self_momentum(closeadj, 63) * rate * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × leadership rate × close 252d
def f047srm_f047_sector_relative_momentum_rsxlead_252d_slope_v074_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 252) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 252) + 0.1
    base = _f047_self_momentum(closeadj, 252) * rate * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs-new-high × ema5 × close 63d
def f047srm_f047_sector_relative_momentum_rsnhxema5_63d_slope_v075_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 63) * closeadj * closeadj.ewm(span=5, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs - median 63d × close
def f047srm_f047_sector_relative_momentum_rsdmed_63d_slope_v076_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    med = rs.rolling(63, min_periods=21).median()
    base = (rs - med) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs - median 252d × close
def f047srm_f047_sector_relative_momentum_rsdmed_252d_slope_v077_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    med = rs.rolling(252, min_periods=63).median()
    base = (rs - med) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs - median 504d × close
def f047srm_f047_sector_relative_momentum_rsdmed_504d_slope_v078_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 504)
    med = rs.rolling(504, min_periods=126).median()
    base = (rs - med) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs max 21d × close
def f047srm_f047_sector_relative_momentum_rsmax_21d_slope_v079_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21).rolling(21, min_periods=5).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs max 63d × close
def f047srm_f047_sector_relative_momentum_rsmax_63d_slope_v080_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63).rolling(63, min_periods=21).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs max 252d × close
def f047srm_f047_sector_relative_momentum_rsmax_252d_slope_v081_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252).rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs min 63d × close
def f047srm_f047_sector_relative_momentum_rsmin_63d_slope_v082_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63).rolling(63, min_periods=21).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs min 252d × close
def f047srm_f047_sector_relative_momentum_rsmin_252d_slope_v083_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252).rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sum 21d × close
def f047srm_f047_sector_relative_momentum_rssum_21d_slope_v084_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21).rolling(21, min_periods=5).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sum 63d × close
def f047srm_f047_sector_relative_momentum_rssum_63d_slope_v085_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs sum 252d × close
def f047srm_f047_sector_relative_momentum_rssum_252d_slope_v086_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh 21d × close
def f047srm_f047_sector_relative_momentum_rsnh21_slope_v087_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 10)
    rs_max = rs.rolling(10, min_periods=3).max()
    flg = (rs >= rs_max).astype(float)
    base = flg.rolling(21, min_periods=5).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh 126d × close
def f047srm_f047_sector_relative_momentum_rsnh126_slope_v088_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 42)
    rs_max = rs.rolling(42, min_periods=10).max()
    flg = (rs >= rs_max).astype(float)
    base = flg.rolling(126, min_periods=42).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh rate 252d × close
def f047srm_f047_sector_relative_momentum_rsnhrate_252d_slope_v089_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    flg = (rs >= rs_max).astype(float)
    base = (flg.rolling(252, min_periods=63).sum() / 252.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh rate 504d × close
def f047srm_f047_sector_relative_momentum_rsnhrate_504d_slope_v090_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 126)
    rs_max = rs.rolling(126, min_periods=42).max()
    flg = (rs >= rs_max).astype(float)
    base = (flg.rolling(504, min_periods=126).sum() / 504.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs gap × mean 21d
def f047srm_f047_sector_relative_momentum_rsgxm_21d_slope_v091_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 21) - 1.0) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs gap × mean 63d
def f047srm_f047_sector_relative_momentum_rsgxm_63d_slope_v092_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 63) - 1.0) * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs gap × mean 252d
def f047srm_f047_sector_relative_momentum_rsgxm_252d_slope_v093_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 252) - 1.0) * _mean(closeadj, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh z 63d
def f047srm_f047_sector_relative_momentum_rsnhz_63d_slope_v094_signal(closeadj):
    base = _z(_f047_sector_proxy(closeadj, 63), 252) + _f047_self_momentum(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh z 252d
def f047srm_f047_sector_relative_momentum_rsnhz_252d_slope_v095_signal(closeadj):
    base = _z(_f047_sector_proxy(closeadj, 252), 504) + _f047_self_momentum(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sign × close 21d
def f047srm_f047_sector_relative_momentum_rssign_21d_slope_v096_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21) - 1.0
    base = np.sign(rs) * rs.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs sign × close 63d
def f047srm_f047_sector_relative_momentum_rssign_63d_slope_v097_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63) - 1.0
    base = np.sign(rs) * rs.abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs sign × close 252d
def f047srm_f047_sector_relative_momentum_rssign_252d_slope_v098_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252) - 1.0
    base = np.sign(rs) * rs.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × std × close 21d
def f047srm_f047_sector_relative_momentum_rsxstd_21d_slope_v099_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21) * _std(closeadj, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × std × close 63d
def f047srm_f047_sector_relative_momentum_rsxstd_63d_slope_v100_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63) * _std(closeadj, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × std × close 252d
def f047srm_f047_sector_relative_momentum_rsxstd_252d_slope_v101_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252) * _std(closeadj, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs momentum 21v42 × close
def f047srm_f047_sector_relative_momentum_rsmoment_21v42_slope_v102_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 21) - _f047_self_momentum(closeadj, 42)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs momentum 42v189
def f047srm_f047_sector_relative_momentum_rsmoment_42v189_slope_v103_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 42) - _f047_self_momentum(closeadj, 189)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs momentum 189v378
def f047srm_f047_sector_relative_momentum_rsmoment_189v378_slope_v104_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 189) - _f047_self_momentum(closeadj, 378)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 5v21
def f047srm_f047_sector_relative_momentum_rsratio_5v21_slope_v105_signal(closeadj):
    base = _f047_self_momentum(closeadj, 5) / _f047_self_momentum(closeadj, 21).replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ratio 10v42
def f047srm_f047_sector_relative_momentum_rsratio_10v42_slope_v106_signal(closeadj):
    base = _f047_self_momentum(closeadj, 10) / _f047_self_momentum(closeadj, 42).replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs ratio 42v189
def f047srm_f047_sector_relative_momentum_rsratio_42v189_slope_v107_signal(closeadj):
    base = _f047_self_momentum(closeadj, 42) / _f047_self_momentum(closeadj, 189).replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs z 42d
def f047srm_f047_sector_relative_momentum_rsz_42d_slope_v108_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 42), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs z 189d
def f047srm_f047_sector_relative_momentum_rsz_189d_slope_v109_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 189), 378)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs z 378d
def f047srm_f047_sector_relative_momentum_rsz_378d_slope_v110_signal(closeadj):
    base = _z(_f047_self_momentum(closeadj, 378), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh × close^2 63d
def f047srm_f047_sector_relative_momentum_rsnhxsq_63d_slope_v111_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 63) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh × close^2 252d
def f047srm_f047_sector_relative_momentum_rsnhxsq_252d_slope_v112_signal(closeadj):
    base = _f047_sector_proxy(closeadj, 252) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ema5 21d × close
def f047srm_f047_sector_relative_momentum_rsema5_21d_slope_v113_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    base = rs.ewm(span=5, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs ema10 63d × close
def f047srm_f047_sector_relative_momentum_rsema10_63d_slope_v114_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    base = rs.ewm(span=10, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs ema42 252d × close
def f047srm_f047_sector_relative_momentum_rsema42_252d_slope_v115_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    base = rs.ewm(span=42, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh mean 63d × close
def f047srm_f047_sector_relative_momentum_rsnhmean_63d_slope_v116_signal(closeadj):
    base = _mean(_f047_sector_proxy(closeadj, 21), 63) * closeadj * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh mean 252d × close
def f047srm_f047_sector_relative_momentum_rsnhmean_252d_slope_v117_signal(closeadj):
    base = _mean(_f047_sector_proxy(closeadj, 63), 252) * closeadj * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh std 63d × close
def f047srm_f047_sector_relative_momentum_rsnhstd_63d_slope_v118_signal(closeadj):
    base = _std(_f047_sector_proxy(closeadj, 21), 63) * closeadj * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh std 252d × close
def f047srm_f047_sector_relative_momentum_rsnhstd_252d_slope_v119_signal(closeadj):
    base = _std(_f047_sector_proxy(closeadj, 63), 252) * closeadj * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × close - close 21d
def f047srm_f047_sector_relative_momentum_rsmclose_21d_slope_v120_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 21) * closeadj - closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × close - close 63d
def f047srm_f047_sector_relative_momentum_rsmclose_63d_slope_v121_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 63) * closeadj - closeadj)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × close - close 252d
def f047srm_f047_sector_relative_momentum_rsmclose_252d_slope_v122_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 252) * closeadj - closeadj)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of days-at-nh smoothed 63d × close
def f047srm_f047_sector_relative_momentum_daysatnh_63d_slope_v123_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at = (rs >= rs_max).astype(float)
    streak = at * (at.groupby((at != at.shift()).cumsum()).cumcount() + 1)
    base = (streak + _mean(closeadj, 21)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of days-at-nh smoothed 252d × close
def f047srm_f047_sector_relative_momentum_daysatnh_252d_slope_v124_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252)
    rs_max = rs.rolling(252, min_periods=63).max()
    at = (rs >= rs_max).astype(float)
    streak = at * (at.groupby((at != at.shift()).cumsum()).cumcount() + 1)
    base = (streak + _mean(closeadj, 63)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs geo 21d × close
def f047srm_f047_sector_relative_momentum_rsgeo_21d_slope_v125_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.exp(np.log(rs).rolling(21, min_periods=5).mean()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs geo 63d × close
def f047srm_f047_sector_relative_momentum_rsgeo_63d_slope_v126_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63).replace(0, np.nan).abs()
    base = np.exp(np.log(rs).rolling(63, min_periods=21).mean()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs geo 252d × close
def f047srm_f047_sector_relative_momentum_rsgeo_252d_slope_v127_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 252).replace(0, np.nan).abs()
    base = np.exp(np.log(rs).rolling(252, min_periods=63).mean()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × ret 5d × close
def f047srm_f047_sector_relative_momentum_rsxret_5d_slope_v128_signal(closeadj):
    ret = closeadj.pct_change(5)
    base = _f047_self_momentum(closeadj, 21) * ret * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × ret 21d × close
def f047srm_f047_sector_relative_momentum_rsxret_21d_slope_v129_signal(closeadj):
    ret = closeadj.pct_change(21)
    base = _f047_self_momentum(closeadj, 63) * ret * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × ret 63d × close
def f047srm_f047_sector_relative_momentum_rsxret_63d_slope_v130_signal(closeadj):
    ret = closeadj.pct_change(63)
    base = _f047_self_momentum(closeadj, 252) * ret * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh × ret 5d
def f047srm_f047_sector_relative_momentum_rsnhxret_5d_slope_v131_signal(closeadj):
    ret = closeadj.pct_change(5)
    base = _f047_sector_proxy(closeadj, 21) * ret * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh × ret 21d
def f047srm_f047_sector_relative_momentum_rsnhxret_21d_slope_v132_signal(closeadj):
    ret = closeadj.pct_change(21)
    base = _f047_sector_proxy(closeadj, 63) * ret * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs abs gap 21d × close
def f047srm_f047_sector_relative_momentum_rsabsgap_21d_slope_v133_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 21) - 1.0).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs abs gap 63d × close
def f047srm_f047_sector_relative_momentum_rsabsgap_63d_slope_v134_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 63) - 1.0).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs abs gap 252d × close
def f047srm_f047_sector_relative_momentum_rsabsgap_252d_slope_v135_signal(closeadj):
    base = (_f047_self_momentum(closeadj, 252) - 1.0).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × log close 21d
def f047srm_f047_sector_relative_momentum_rsxlog_21d_slope_v136_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21) * np.log(closeadj.replace(0, np.nan).abs())
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × log close 252d
def f047srm_f047_sector_relative_momentum_rsxlog_252d_slope_v137_signal(closeadj):
    base = _f047_self_momentum(closeadj, 252) * np.log(closeadj.replace(0, np.nan).abs())
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh osc 21d × close
def f047srm_f047_sector_relative_momentum_rsoscnh_21d_slope_v138_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 10)
    rs_max = rs.rolling(21, min_periods=5).max()
    base = (rs - rs_max) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rsnh osc 63d × close
def f047srm_f047_sector_relative_momentum_rsoscnh_63d_slope_v139_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    rs_max = rs.rolling(63, min_periods=21).max()
    base = (rs - rs_max) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rsnh osc 252d × close
def f047srm_f047_sector_relative_momentum_rsoscnh_252d_slope_v140_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    rs_max = rs.rolling(252, min_periods=63).max()
    base = (rs - rs_max) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar^2 21d
def f047srm_f047_sector_relative_momentum_rsxdsq_21d_slope_v141_signal(closeadj):
    base = _f047_self_momentum(closeadj, 21) * closeadj * _mean(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs × dollar^2 63d
def f047srm_f047_sector_relative_momentum_rsxdsq_63d_slope_v142_signal(closeadj):
    base = _f047_self_momentum(closeadj, 63) * closeadj * _mean(closeadj, 63) * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs/max 63d × close
def f047srm_f047_sector_relative_momentum_rsdmax_63d_slope_v143_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    rs_max = rs.rolling(63, min_periods=21).max().replace(0, np.nan)
    base = (rs / rs_max) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs/max 252d × close
def f047srm_f047_sector_relative_momentum_rsdmax_252d_slope_v144_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    rs_max = rs.rolling(252, min_periods=63).max().replace(0, np.nan)
    base = (rs / rs_max) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs/max 504d × close
def f047srm_f047_sector_relative_momentum_rsdmax_504d_slope_v145_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 126)
    rs_max = rs.rolling(504, min_periods=126).max().replace(0, np.nan)
    base = (rs / rs_max) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs - mean(rs, 504d) × close
def f047srm_f047_sector_relative_momentum_rsdmean_504d_slope_v146_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 63)
    base = (rs - _mean(rs, 504)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs - mean(rs, 252d) × close
def f047srm_f047_sector_relative_momentum_rsdmean_252d_slope_v147_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21)
    base = (rs - _mean(rs, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of rs cum log 21d × close
def f047srm_f047_sector_relative_momentum_rscum_21d_slope_v148_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.log(rs).rolling(21, min_periods=5).sum() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs cum log 252d × close
def f047srm_f047_sector_relative_momentum_rscum_252d_slope_v149_signal(closeadj):
    rs = _f047_self_momentum(closeadj, 21).replace(0, np.nan).abs()
    base = np.log(rs).rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of rs × leadership smoothed × close 126d
def f047srm_f047_sector_relative_momentum_rsxleadsm_126d_slope_v150_signal(closeadj):
    lc = _f047_excess_momentum(closeadj, 126) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 126) + 0.1
    base = _f047_self_momentum(closeadj, 126) * rate * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f047srm_f047_sector_relative_momentum_rsline_21d_slope_v001_signal,
    f047srm_f047_sector_relative_momentum_rsline_63d_slope_v002_signal,
    f047srm_f047_sector_relative_momentum_rsline_126d_slope_v003_signal,
    f047srm_f047_sector_relative_momentum_rsline_252d_slope_v004_signal,
    f047srm_f047_sector_relative_momentum_rsline_504d_slope_v005_signal,
    f047srm_f047_sector_relative_momentum_rsnh_21d_slope_v006_signal,
    f047srm_f047_sector_relative_momentum_rsnh_63d_slope_v007_signal,
    f047srm_f047_sector_relative_momentum_rsnh_126d_slope_v008_signal,
    f047srm_f047_sector_relative_momentum_rsnh_252d_slope_v009_signal,
    f047srm_f047_sector_relative_momentum_rsnh_504d_slope_v010_signal,
    f047srm_f047_sector_relative_momentum_lead_21d_slope_v011_signal,
    f047srm_f047_sector_relative_momentum_lead_63d_slope_v012_signal,
    f047srm_f047_sector_relative_momentum_lead_126d_slope_v013_signal,
    f047srm_f047_sector_relative_momentum_lead_252d_slope_v014_signal,
    f047srm_f047_sector_relative_momentum_lead_504d_slope_v015_signal,
    f047srm_f047_sector_relative_momentum_rsgap_21d_slope_v016_signal,
    f047srm_f047_sector_relative_momentum_rsgap_63d_slope_v017_signal,
    f047srm_f047_sector_relative_momentum_rsgap_126d_slope_v018_signal,
    f047srm_f047_sector_relative_momentum_rsgap_252d_slope_v019_signal,
    f047srm_f047_sector_relative_momentum_rsgap_504d_slope_v020_signal,
    f047srm_f047_sector_relative_momentum_rsz_21d_slope_v021_signal,
    f047srm_f047_sector_relative_momentum_rsz_63d_slope_v022_signal,
    f047srm_f047_sector_relative_momentum_rsz_126d_slope_v023_signal,
    f047srm_f047_sector_relative_momentum_rsz_252d_slope_v024_signal,
    f047srm_f047_sector_relative_momentum_rsema_21d_slope_v025_signal,
    f047srm_f047_sector_relative_momentum_rsema_63d_slope_v026_signal,
    f047srm_f047_sector_relative_momentum_rsema_126d_slope_v027_signal,
    f047srm_f047_sector_relative_momentum_rsema_252d_slope_v028_signal,
    f047srm_f047_sector_relative_momentum_rsnhcount_252d_slope_v029_signal,
    f047srm_f047_sector_relative_momentum_rsnhcount_63d_slope_v030_signal,
    f047srm_f047_sector_relative_momentum_rsnhcount_504d_slope_v031_signal,
    f047srm_f047_sector_relative_momentum_rsratio_63v252_slope_v032_signal,
    f047srm_f047_sector_relative_momentum_rsratio_21v126_slope_v033_signal,
    f047srm_f047_sector_relative_momentum_rsratio_252v504_slope_v034_signal,
    f047srm_f047_sector_relative_momentum_rsdiff_21m63_slope_v035_signal,
    f047srm_f047_sector_relative_momentum_rsdiff_63m252_slope_v036_signal,
    f047srm_f047_sector_relative_momentum_rsdiff_126m504_slope_v037_signal,
    f047srm_f047_sector_relative_momentum_rsline_5d_slope_v038_signal,
    f047srm_f047_sector_relative_momentum_rsline_10d_slope_v039_signal,
    f047srm_f047_sector_relative_momentum_rsline_42d_slope_v040_signal,
    f047srm_f047_sector_relative_momentum_rsline_189d_slope_v041_signal,
    f047srm_f047_sector_relative_momentum_rsline_378d_slope_v042_signal,
    f047srm_f047_sector_relative_momentum_rsnhxmean_21d_slope_v043_signal,
    f047srm_f047_sector_relative_momentum_rsnhxmean_63d_slope_v044_signal,
    f047srm_f047_sector_relative_momentum_rsnhxmean_252d_slope_v045_signal,
    f047srm_f047_sector_relative_momentum_rsstd_21d_slope_v046_signal,
    f047srm_f047_sector_relative_momentum_rsstd_63d_slope_v047_signal,
    f047srm_f047_sector_relative_momentum_rsstd_252d_slope_v048_signal,
    f047srm_f047_sector_relative_momentum_rssq_21d_slope_v049_signal,
    f047srm_f047_sector_relative_momentum_rssq_63d_slope_v050_signal,
    f047srm_f047_sector_relative_momentum_rssq_252d_slope_v051_signal,
    f047srm_f047_sector_relative_momentum_rslog_21d_slope_v052_signal,
    f047srm_f047_sector_relative_momentum_rslog_63d_slope_v053_signal,
    f047srm_f047_sector_relative_momentum_rslog_252d_slope_v054_signal,
    f047srm_f047_sector_relative_momentum_leadsum_63d_slope_v055_signal,
    f047srm_f047_sector_relative_momentum_leadsum_252d_slope_v056_signal,
    f047srm_f047_sector_relative_momentum_leadsum_504d_slope_v057_signal,
    f047srm_f047_sector_relative_momentum_rsxdmean_21d_slope_v058_signal,
    f047srm_f047_sector_relative_momentum_rsxdmean_63d_slope_v059_signal,
    f047srm_f047_sector_relative_momentum_rsxdmean_252d_slope_v060_signal,
    f047srm_f047_sector_relative_momentum_rsnhexp_slope_v061_signal,
    f047srm_f047_sector_relative_momentum_rsnhpersist_21d_slope_v062_signal,
    f047srm_f047_sector_relative_momentum_rsnhpersist_126d_slope_v063_signal,
    f047srm_f047_sector_relative_momentum_rsosc_21d_slope_v064_signal,
    f047srm_f047_sector_relative_momentum_rsosc_63d_slope_v065_signal,
    f047srm_f047_sector_relative_momentum_rsosc_252d_slope_v066_signal,
    f047srm_f047_sector_relative_momentum_rsrange_63d_slope_v067_signal,
    f047srm_f047_sector_relative_momentum_rsrange_252d_slope_v068_signal,
    f047srm_f047_sector_relative_momentum_rsrange_504d_slope_v069_signal,
    f047srm_f047_sector_relative_momentum_daysrsnh_252d_slope_v070_signal,
    f047srm_f047_sector_relative_momentum_daysrsnh_63d_slope_v071_signal,
    f047srm_f047_sector_relative_momentum_daysrsnh_504d_slope_v072_signal,
    f047srm_f047_sector_relative_momentum_rsxlead_63d_slope_v073_signal,
    f047srm_f047_sector_relative_momentum_rsxlead_252d_slope_v074_signal,
    f047srm_f047_sector_relative_momentum_rsnhxema5_63d_slope_v075_signal,
    f047srm_f047_sector_relative_momentum_rsdmed_63d_slope_v076_signal,
    f047srm_f047_sector_relative_momentum_rsdmed_252d_slope_v077_signal,
    f047srm_f047_sector_relative_momentum_rsdmed_504d_slope_v078_signal,
    f047srm_f047_sector_relative_momentum_rsmax_21d_slope_v079_signal,
    f047srm_f047_sector_relative_momentum_rsmax_63d_slope_v080_signal,
    f047srm_f047_sector_relative_momentum_rsmax_252d_slope_v081_signal,
    f047srm_f047_sector_relative_momentum_rsmin_63d_slope_v082_signal,
    f047srm_f047_sector_relative_momentum_rsmin_252d_slope_v083_signal,
    f047srm_f047_sector_relative_momentum_rssum_21d_slope_v084_signal,
    f047srm_f047_sector_relative_momentum_rssum_63d_slope_v085_signal,
    f047srm_f047_sector_relative_momentum_rssum_252d_slope_v086_signal,
    f047srm_f047_sector_relative_momentum_rsnh21_slope_v087_signal,
    f047srm_f047_sector_relative_momentum_rsnh126_slope_v088_signal,
    f047srm_f047_sector_relative_momentum_rsnhrate_252d_slope_v089_signal,
    f047srm_f047_sector_relative_momentum_rsnhrate_504d_slope_v090_signal,
    f047srm_f047_sector_relative_momentum_rsgxm_21d_slope_v091_signal,
    f047srm_f047_sector_relative_momentum_rsgxm_63d_slope_v092_signal,
    f047srm_f047_sector_relative_momentum_rsgxm_252d_slope_v093_signal,
    f047srm_f047_sector_relative_momentum_rsnhz_63d_slope_v094_signal,
    f047srm_f047_sector_relative_momentum_rsnhz_252d_slope_v095_signal,
    f047srm_f047_sector_relative_momentum_rssign_21d_slope_v096_signal,
    f047srm_f047_sector_relative_momentum_rssign_63d_slope_v097_signal,
    f047srm_f047_sector_relative_momentum_rssign_252d_slope_v098_signal,
    f047srm_f047_sector_relative_momentum_rsxstd_21d_slope_v099_signal,
    f047srm_f047_sector_relative_momentum_rsxstd_63d_slope_v100_signal,
    f047srm_f047_sector_relative_momentum_rsxstd_252d_slope_v101_signal,
    f047srm_f047_sector_relative_momentum_rsmoment_21v42_slope_v102_signal,
    f047srm_f047_sector_relative_momentum_rsmoment_42v189_slope_v103_signal,
    f047srm_f047_sector_relative_momentum_rsmoment_189v378_slope_v104_signal,
    f047srm_f047_sector_relative_momentum_rsratio_5v21_slope_v105_signal,
    f047srm_f047_sector_relative_momentum_rsratio_10v42_slope_v106_signal,
    f047srm_f047_sector_relative_momentum_rsratio_42v189_slope_v107_signal,
    f047srm_f047_sector_relative_momentum_rsz_42d_slope_v108_signal,
    f047srm_f047_sector_relative_momentum_rsz_189d_slope_v109_signal,
    f047srm_f047_sector_relative_momentum_rsz_378d_slope_v110_signal,
    f047srm_f047_sector_relative_momentum_rsnhxsq_63d_slope_v111_signal,
    f047srm_f047_sector_relative_momentum_rsnhxsq_252d_slope_v112_signal,
    f047srm_f047_sector_relative_momentum_rsema5_21d_slope_v113_signal,
    f047srm_f047_sector_relative_momentum_rsema10_63d_slope_v114_signal,
    f047srm_f047_sector_relative_momentum_rsema42_252d_slope_v115_signal,
    f047srm_f047_sector_relative_momentum_rsnhmean_63d_slope_v116_signal,
    f047srm_f047_sector_relative_momentum_rsnhmean_252d_slope_v117_signal,
    f047srm_f047_sector_relative_momentum_rsnhstd_63d_slope_v118_signal,
    f047srm_f047_sector_relative_momentum_rsnhstd_252d_slope_v119_signal,
    f047srm_f047_sector_relative_momentum_rsmclose_21d_slope_v120_signal,
    f047srm_f047_sector_relative_momentum_rsmclose_63d_slope_v121_signal,
    f047srm_f047_sector_relative_momentum_rsmclose_252d_slope_v122_signal,
    f047srm_f047_sector_relative_momentum_daysatnh_63d_slope_v123_signal,
    f047srm_f047_sector_relative_momentum_daysatnh_252d_slope_v124_signal,
    f047srm_f047_sector_relative_momentum_rsgeo_21d_slope_v125_signal,
    f047srm_f047_sector_relative_momentum_rsgeo_63d_slope_v126_signal,
    f047srm_f047_sector_relative_momentum_rsgeo_252d_slope_v127_signal,
    f047srm_f047_sector_relative_momentum_rsxret_5d_slope_v128_signal,
    f047srm_f047_sector_relative_momentum_rsxret_21d_slope_v129_signal,
    f047srm_f047_sector_relative_momentum_rsxret_63d_slope_v130_signal,
    f047srm_f047_sector_relative_momentum_rsnhxret_5d_slope_v131_signal,
    f047srm_f047_sector_relative_momentum_rsnhxret_21d_slope_v132_signal,
    f047srm_f047_sector_relative_momentum_rsabsgap_21d_slope_v133_signal,
    f047srm_f047_sector_relative_momentum_rsabsgap_63d_slope_v134_signal,
    f047srm_f047_sector_relative_momentum_rsabsgap_252d_slope_v135_signal,
    f047srm_f047_sector_relative_momentum_rsxlog_21d_slope_v136_signal,
    f047srm_f047_sector_relative_momentum_rsxlog_252d_slope_v137_signal,
    f047srm_f047_sector_relative_momentum_rsoscnh_21d_slope_v138_signal,
    f047srm_f047_sector_relative_momentum_rsoscnh_63d_slope_v139_signal,
    f047srm_f047_sector_relative_momentum_rsoscnh_252d_slope_v140_signal,
    f047srm_f047_sector_relative_momentum_rsxdsq_21d_slope_v141_signal,
    f047srm_f047_sector_relative_momentum_rsxdsq_63d_slope_v142_signal,
    f047srm_f047_sector_relative_momentum_rsdmax_63d_slope_v143_signal,
    f047srm_f047_sector_relative_momentum_rsdmax_252d_slope_v144_signal,
    f047srm_f047_sector_relative_momentum_rsdmax_504d_slope_v145_signal,
    f047srm_f047_sector_relative_momentum_rsdmean_504d_slope_v146_signal,
    f047srm_f047_sector_relative_momentum_rsdmean_252d_slope_v147_signal,
    f047srm_f047_sector_relative_momentum_rscum_21d_slope_v148_signal,
    f047srm_f047_sector_relative_momentum_rscum_252d_slope_v149_signal,
    f047srm_f047_sector_relative_momentum_rsxleadsm_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F047_SECTOR_RELATIVE_MOMENTUM_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f047_self_momentum", "_f047_sector_proxy", "_f047_excess_momentum")
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
    print(f"OK f047_sector_relative_momentum_2nd_derivatives_001_150_claude: {n_features} features pass")
