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


# ===== folder domain primitives =====
def _f046_rs_line(close, w):
    # RS line proxy: price normalized to its own long-term mean (the "market" proxy)
    base = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return close / base.replace(0, np.nan)


def _f046_rs_new_high(close, w):
    rs = close / close.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    rs_max = rs.rolling(w, min_periods=max(1, w // 2)).max()
    return (rs - rs_max) / rs_max.replace(0, np.nan).abs()


def _f046_leadership_confirm(close, w):
    rs = close / close.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    rs_max = rs.rolling(w, min_periods=max(1, w // 2)).max()
    at_high = (rs >= rs_max).astype(float)
    return at_high * close


# 21d rs line scaled by close
def f046rln_f046_rs_line_new_high_rsline_21d_base_v001_signal(closeadj):
    result = _f046_rs_line(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rs line scaled by close
def f046rln_f046_rs_line_new_high_rsline_63d_base_v002_signal(closeadj):
    result = _f046_rs_line(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rs line scaled by close
def f046rln_f046_rs_line_new_high_rsline_126d_base_v003_signal(closeadj):
    result = _f046_rs_line(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rs line scaled by close
def f046rln_f046_rs_line_new_high_rsline_252d_base_v004_signal(closeadj):
    result = _f046_rs_line(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rs line scaled by close
def f046rln_f046_rs_line_new_high_rsline_504d_base_v005_signal(closeadj):
    result = _f046_rs_line(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rs new high distance × close
def f046rln_f046_rs_line_new_high_rsnewhigh_21d_base_v006_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rs new high distance × close
def f046rln_f046_rs_line_new_high_rsnewhigh_63d_base_v007_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rs new high distance × close
def f046rln_f046_rs_line_new_high_rsnewhigh_126d_base_v008_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rs new high distance × close
def f046rln_f046_rs_line_new_high_rsnewhigh_252d_base_v009_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rs new high distance × close
def f046rln_f046_rs_line_new_high_rsnewhigh_504d_base_v010_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d leadership confirm flag smoothed × close
def f046rln_f046_rs_line_new_high_leadership_21d_base_v011_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 21) / closeadj.replace(0, np.nan)
    result = _mean(lc, 21) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leadership confirm flag smoothed × close
def f046rln_f046_rs_line_new_high_leadership_63d_base_v012_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 63) / closeadj.replace(0, np.nan)
    result = _mean(lc, 63) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d leadership confirm flag smoothed × close
def f046rln_f046_rs_line_new_high_leadership_126d_base_v013_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 126) / closeadj.replace(0, np.nan)
    result = _mean(lc, 126) * closeadj * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leadership confirm flag smoothed × close
def f046rln_f046_rs_line_new_high_leadership_252d_base_v014_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 252) / closeadj.replace(0, np.nan)
    result = _mean(lc, 252) * closeadj * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d leadership confirm flag smoothed × close
def f046rln_f046_rs_line_new_high_leadership_504d_base_v015_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 504) / closeadj.replace(0, np.nan)
    result = _mean(lc, 504) * closeadj * _mean(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 21d minus 1 × close (gap from baseline)
def f046rln_f046_rs_line_new_high_rsgap_21d_base_v016_signal(closeadj):
    result = (_f046_rs_line(closeadj, 21) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 63d minus 1 × close
def f046rln_f046_rs_line_new_high_rsgap_63d_base_v017_signal(closeadj):
    result = (_f046_rs_line(closeadj, 63) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 126d minus 1 × close
def f046rln_f046_rs_line_new_high_rsgap_126d_base_v018_signal(closeadj):
    result = (_f046_rs_line(closeadj, 126) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 252d minus 1 × close
def f046rln_f046_rs_line_new_high_rsgap_252d_base_v019_signal(closeadj):
    result = (_f046_rs_line(closeadj, 252) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 504d minus 1 × close
def f046rln_f046_rs_line_new_high_rsgap_504d_base_v020_signal(closeadj):
    result = (_f046_rs_line(closeadj, 504) - 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rs line z-score over 252d
def f046rln_f046_rs_line_new_high_rsz_21d_base_v021_signal(closeadj):
    result = _z(_f046_rs_line(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rs line z-score over 252d
def f046rln_f046_rs_line_new_high_rsz_63d_base_v022_signal(closeadj):
    result = _z(_f046_rs_line(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rs line z-score over 504d
def f046rln_f046_rs_line_new_high_rsz_126d_base_v023_signal(closeadj):
    result = _z(_f046_rs_line(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rs line z-score over 504d
def f046rln_f046_rs_line_new_high_rsz_252d_base_v024_signal(closeadj):
    result = _z(_f046_rs_line(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of rs line × close
def f046rln_f046_rs_line_new_high_rsema_21d_base_v025_signal(closeadj):
    rs = _f046_rs_line(closeadj, 21)
    result = rs.ewm(span=21, adjust=False).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of rs line × close
def f046rln_f046_rs_line_new_high_rsema_63d_base_v026_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63)
    result = rs.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA of rs line × close
def f046rln_f046_rs_line_new_high_rsema_126d_base_v027_signal(closeadj):
    rs = _f046_rs_line(closeadj, 126)
    result = rs.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of rs line × close
def f046rln_f046_rs_line_new_high_rsema_252d_base_v028_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252)
    result = rs.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs new high count over 252d × close (frequency of leadership)
def f046rln_f046_rs_line_new_high_rsnhcount_252d_base_v029_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at_high = (rs >= rs_max).astype(float)
    result = at_high.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs new high count over 63d × close
def f046rln_f046_rs_line_new_high_rsnhcount_63d_base_v030_signal(closeadj):
    rs = _f046_rs_line(closeadj, 21)
    rs_max = rs.rolling(21, min_periods=5).max()
    at_high = (rs >= rs_max).astype(float)
    result = at_high.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs new high count over 504d × close
def f046rln_f046_rs_line_new_high_rsnhcount_504d_base_v031_signal(closeadj):
    rs = _f046_rs_line(closeadj, 126)
    rs_max = rs.rolling(126, min_periods=42).max()
    at_high = (rs >= rs_max).astype(float)
    result = at_high.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line ratio 63d vs 252d × close
def f046rln_f046_rs_line_new_high_rsratio_63v252_base_v032_signal(closeadj):
    a = _f046_rs_line(closeadj, 63)
    b = _f046_rs_line(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line ratio 21d vs 126d × close
def f046rln_f046_rs_line_new_high_rsratio_21v126_base_v033_signal(closeadj):
    a = _f046_rs_line(closeadj, 21)
    b = _f046_rs_line(closeadj, 126).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line ratio 252d vs 504d × close
def f046rln_f046_rs_line_new_high_rsratio_252v504_base_v034_signal(closeadj):
    a = _f046_rs_line(closeadj, 252)
    b = _f046_rs_line(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 21d - rs line 63d × close
def f046rln_f046_rs_line_new_high_rsdiff_21m63_base_v035_signal(closeadj):
    result = (_f046_rs_line(closeadj, 21) - _f046_rs_line(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 63d - rs line 252d × close
def f046rln_f046_rs_line_new_high_rsdiff_63m252_base_v036_signal(closeadj):
    result = (_f046_rs_line(closeadj, 63) - _f046_rs_line(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 126d - rs line 504d × close
def f046rln_f046_rs_line_new_high_rsdiff_126m504_base_v037_signal(closeadj):
    result = (_f046_rs_line(closeadj, 126) - _f046_rs_line(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d rs line × close (short)
def f046rln_f046_rs_line_new_high_rsline_5d_base_v038_signal(closeadj):
    result = _f046_rs_line(closeadj, 5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d rs line × close
def f046rln_f046_rs_line_new_high_rsline_10d_base_v039_signal(closeadj):
    result = _f046_rs_line(closeadj, 10) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rs line × close
def f046rln_f046_rs_line_new_high_rsline_42d_base_v040_signal(closeadj):
    result = _f046_rs_line(closeadj, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rs line × close
def f046rln_f046_rs_line_new_high_rsline_189d_base_v041_signal(closeadj):
    result = _f046_rs_line(closeadj, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d rs line × close
def f046rln_f046_rs_line_new_high_rsline_378d_base_v042_signal(closeadj):
    result = _f046_rs_line(closeadj, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rs new high distance × close * mean(close, 21)
def f046rln_f046_rs_line_new_high_rsnhxmean_21d_base_v043_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rs new high distance × close * mean(close, 63)
def f046rln_f046_rs_line_new_high_rsnhxmean_63d_base_v044_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rs new high distance × close * mean(close, 252)
def f046rln_f046_rs_line_new_high_rsnhxmean_252d_base_v045_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rs line std × close
def f046rln_f046_rs_line_new_high_rsstd_21d_base_v046_signal(closeadj):
    result = _std(_f046_rs_line(closeadj, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rs line std × close
def f046rln_f046_rs_line_new_high_rsstd_63d_base_v047_signal(closeadj):
    result = _std(_f046_rs_line(closeadj, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rs line std × close
def f046rln_f046_rs_line_new_high_rsstd_252d_base_v048_signal(closeadj):
    result = _std(_f046_rs_line(closeadj, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 21d squared × close (convexity)
def f046rln_f046_rs_line_new_high_rssq_21d_base_v049_signal(closeadj):
    rs = _f046_rs_line(closeadj, 21) - 1.0
    result = rs * rs.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 63d squared × close
def f046rln_f046_rs_line_new_high_rssq_63d_base_v050_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63) - 1.0
    result = rs * rs.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 252d squared × close
def f046rln_f046_rs_line_new_high_rssq_252d_base_v051_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252) - 1.0
    result = rs * rs.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 21d log × close
def f046rln_f046_rs_line_new_high_rslog_21d_base_v052_signal(closeadj):
    rs = _f046_rs_line(closeadj, 21).replace(0, np.nan).abs()
    result = np.log(rs) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 63d log × close
def f046rln_f046_rs_line_new_high_rslog_63d_base_v053_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63).replace(0, np.nan).abs()
    result = np.log(rs) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 252d log × close
def f046rln_f046_rs_line_new_high_rslog_252d_base_v054_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252).replace(0, np.nan).abs()
    result = np.log(rs) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# leadership confirm sum over 63d × close
def f046rln_f046_rs_line_new_high_leadsum_63d_base_v055_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 21) / closeadj.replace(0, np.nan)
    result = lc.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# leadership confirm sum over 252d × close
def f046rln_f046_rs_line_new_high_leadsum_252d_base_v056_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 63) / closeadj.replace(0, np.nan)
    result = lc.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# leadership confirm sum over 504d × close
def f046rln_f046_rs_line_new_high_leadsum_504d_base_v057_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 126) / closeadj.replace(0, np.nan)
    result = lc.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 21d × dollar-mean (close × mean close 21d)
def f046rln_f046_rs_line_new_high_rsxdmean_21d_base_v058_signal(closeadj):
    result = _f046_rs_line(closeadj, 21) * _safe_div(closeadj, _mean(closeadj, 252)) * _safe_div(_mean(closeadj, 21), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 63d × dollar-mean
def f046rln_f046_rs_line_new_high_rsxdmean_63d_base_v059_signal(closeadj):
    result = _f046_rs_line(closeadj, 63) * _safe_div(closeadj, _mean(closeadj, 252)) * _safe_div(_mean(closeadj, 63), _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# rs line 252d × dollar-mean
def f046rln_f046_rs_line_new_high_rsxdmean_252d_base_v060_signal(closeadj):
    result = _f046_rs_line(closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252)) * _safe_div(_mean(closeadj, 252), _mean(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# expanding RS new-high gap × close
def f046rln_f046_rs_line_new_high_rsnhexp_base_v061_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252)
    rs_max = rs.expanding(min_periods=63).max()
    result = ((rs - rs_max) / rs_max.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS at-new-high persistence (21d rolling count) × close
def f046rln_f046_rs_line_new_high_rsnhpersist_21d_base_v062_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 63) / closeadj.replace(0, np.nan)
    result = lc.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS at-new-high persistence (126d) × close
def f046rln_f046_rs_line_new_high_rsnhpersist_126d_base_v063_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 252) / closeadj.replace(0, np.nan)
    result = lc.rolling(126, min_periods=42).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line minus its own EMA (oscillator) × close
def f046rln_f046_rs_line_new_high_rsosc_21d_base_v064_signal(closeadj):
    rs = _f046_rs_line(closeadj, 21)
    result = (rs - rs.ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line minus its own EMA over 63d × close
def f046rln_f046_rs_line_new_high_rsosc_63d_base_v065_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63)
    result = (rs - rs.ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line minus its own EMA over 252d × close
def f046rln_f046_rs_line_new_high_rsosc_252d_base_v066_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252)
    result = (rs - rs.ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS rank-style: position of current rs in 63d range × close
def f046rln_f046_rs_line_new_high_rsrange_63d_base_v067_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63)
    lo = rs.rolling(63, min_periods=21).min()
    hi = rs.rolling(63, min_periods=21).max()
    result = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS rank-style 252d × close
def f046rln_f046_rs_line_new_high_rsrange_252d_base_v068_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252)
    lo = rs.rolling(252, min_periods=63).min()
    hi = rs.rolling(252, min_periods=63).max()
    result = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS rank-style 504d × close
def f046rln_f046_rs_line_new_high_rsrange_504d_base_v069_signal(closeadj):
    rs = _f046_rs_line(closeadj, 504)
    lo = rs.rolling(504, min_periods=126).min()
    hi = rs.rolling(504, min_periods=126).max()
    result = ((rs - lo) / (hi - lo).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# days since last RS new high × close
def f046rln_f046_rs_line_new_high_daysrsnh_252d_base_v070_signal(closeadj):
    rs = _f046_rs_line(closeadj, 252)
    rs_max = rs.rolling(252, min_periods=63).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    result = age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# days since last RS new high 63d × close
def f046rln_f046_rs_line_new_high_daysrsnh_63d_base_v071_signal(closeadj):
    rs = _f046_rs_line(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    result = age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# days since last RS new high 504d × close
def f046rln_f046_rs_line_new_high_daysrsnh_504d_base_v072_signal(closeadj):
    rs = _f046_rs_line(closeadj, 504)
    rs_max = rs.rolling(504, min_periods=126).max()
    at_high = (rs >= rs_max).astype(float)
    grp = at_high.cumsum()
    age = (~at_high.astype(bool)).astype(float).groupby(grp).cumsum()
    result = age * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × smoothed leadership-rate 63d × close
def f046rln_f046_rs_line_new_high_rsxlead_63d_base_v073_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 63) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 63) + 0.1
    result = _f046_rs_line(closeadj, 63) * rate * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × smoothed leadership-rate 252d × close
def f046rln_f046_rs_line_new_high_rsxlead_252d_base_v074_signal(closeadj):
    lc = _f046_leadership_confirm(closeadj, 252) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 252) + 0.1
    result = _f046_rs_line(closeadj, 252) * rate * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new high gap 63d × volume not allowed; use close × ema(close,5)
def f046rln_f046_rs_line_new_high_rsnhxema5_63d_base_v075_signal(closeadj):
    result = _f046_rs_new_high(closeadj, 63) * closeadj * closeadj.ewm(span=5, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f046rln_f046_rs_line_new_high_rsline_21d_base_v001_signal,
    f046rln_f046_rs_line_new_high_rsline_63d_base_v002_signal,
    f046rln_f046_rs_line_new_high_rsline_126d_base_v003_signal,
    f046rln_f046_rs_line_new_high_rsline_252d_base_v004_signal,
    f046rln_f046_rs_line_new_high_rsline_504d_base_v005_signal,
    f046rln_f046_rs_line_new_high_rsnewhigh_21d_base_v006_signal,
    f046rln_f046_rs_line_new_high_rsnewhigh_63d_base_v007_signal,
    f046rln_f046_rs_line_new_high_rsnewhigh_126d_base_v008_signal,
    f046rln_f046_rs_line_new_high_rsnewhigh_252d_base_v009_signal,
    f046rln_f046_rs_line_new_high_rsnewhigh_504d_base_v010_signal,
    f046rln_f046_rs_line_new_high_leadership_21d_base_v011_signal,
    f046rln_f046_rs_line_new_high_leadership_63d_base_v012_signal,
    f046rln_f046_rs_line_new_high_leadership_126d_base_v013_signal,
    f046rln_f046_rs_line_new_high_leadership_252d_base_v014_signal,
    f046rln_f046_rs_line_new_high_leadership_504d_base_v015_signal,
    f046rln_f046_rs_line_new_high_rsgap_21d_base_v016_signal,
    f046rln_f046_rs_line_new_high_rsgap_63d_base_v017_signal,
    f046rln_f046_rs_line_new_high_rsgap_126d_base_v018_signal,
    f046rln_f046_rs_line_new_high_rsgap_252d_base_v019_signal,
    f046rln_f046_rs_line_new_high_rsgap_504d_base_v020_signal,
    f046rln_f046_rs_line_new_high_rsz_21d_base_v021_signal,
    f046rln_f046_rs_line_new_high_rsz_63d_base_v022_signal,
    f046rln_f046_rs_line_new_high_rsz_126d_base_v023_signal,
    f046rln_f046_rs_line_new_high_rsz_252d_base_v024_signal,
    f046rln_f046_rs_line_new_high_rsema_21d_base_v025_signal,
    f046rln_f046_rs_line_new_high_rsema_63d_base_v026_signal,
    f046rln_f046_rs_line_new_high_rsema_126d_base_v027_signal,
    f046rln_f046_rs_line_new_high_rsema_252d_base_v028_signal,
    f046rln_f046_rs_line_new_high_rsnhcount_252d_base_v029_signal,
    f046rln_f046_rs_line_new_high_rsnhcount_63d_base_v030_signal,
    f046rln_f046_rs_line_new_high_rsnhcount_504d_base_v031_signal,
    f046rln_f046_rs_line_new_high_rsratio_63v252_base_v032_signal,
    f046rln_f046_rs_line_new_high_rsratio_21v126_base_v033_signal,
    f046rln_f046_rs_line_new_high_rsratio_252v504_base_v034_signal,
    f046rln_f046_rs_line_new_high_rsdiff_21m63_base_v035_signal,
    f046rln_f046_rs_line_new_high_rsdiff_63m252_base_v036_signal,
    f046rln_f046_rs_line_new_high_rsdiff_126m504_base_v037_signal,
    f046rln_f046_rs_line_new_high_rsline_5d_base_v038_signal,
    f046rln_f046_rs_line_new_high_rsline_10d_base_v039_signal,
    f046rln_f046_rs_line_new_high_rsline_42d_base_v040_signal,
    f046rln_f046_rs_line_new_high_rsline_189d_base_v041_signal,
    f046rln_f046_rs_line_new_high_rsline_378d_base_v042_signal,
    f046rln_f046_rs_line_new_high_rsnhxmean_21d_base_v043_signal,
    f046rln_f046_rs_line_new_high_rsnhxmean_63d_base_v044_signal,
    f046rln_f046_rs_line_new_high_rsnhxmean_252d_base_v045_signal,
    f046rln_f046_rs_line_new_high_rsstd_21d_base_v046_signal,
    f046rln_f046_rs_line_new_high_rsstd_63d_base_v047_signal,
    f046rln_f046_rs_line_new_high_rsstd_252d_base_v048_signal,
    f046rln_f046_rs_line_new_high_rssq_21d_base_v049_signal,
    f046rln_f046_rs_line_new_high_rssq_63d_base_v050_signal,
    f046rln_f046_rs_line_new_high_rssq_252d_base_v051_signal,
    f046rln_f046_rs_line_new_high_rslog_21d_base_v052_signal,
    f046rln_f046_rs_line_new_high_rslog_63d_base_v053_signal,
    f046rln_f046_rs_line_new_high_rslog_252d_base_v054_signal,
    f046rln_f046_rs_line_new_high_leadsum_63d_base_v055_signal,
    f046rln_f046_rs_line_new_high_leadsum_252d_base_v056_signal,
    f046rln_f046_rs_line_new_high_leadsum_504d_base_v057_signal,
    f046rln_f046_rs_line_new_high_rsxdmean_21d_base_v058_signal,
    f046rln_f046_rs_line_new_high_rsxdmean_63d_base_v059_signal,
    f046rln_f046_rs_line_new_high_rsxdmean_252d_base_v060_signal,
    f046rln_f046_rs_line_new_high_rsnhexp_base_v061_signal,
    f046rln_f046_rs_line_new_high_rsnhpersist_21d_base_v062_signal,
    f046rln_f046_rs_line_new_high_rsnhpersist_126d_base_v063_signal,
    f046rln_f046_rs_line_new_high_rsosc_21d_base_v064_signal,
    f046rln_f046_rs_line_new_high_rsosc_63d_base_v065_signal,
    f046rln_f046_rs_line_new_high_rsosc_252d_base_v066_signal,
    f046rln_f046_rs_line_new_high_rsrange_63d_base_v067_signal,
    f046rln_f046_rs_line_new_high_rsrange_252d_base_v068_signal,
    f046rln_f046_rs_line_new_high_rsrange_504d_base_v069_signal,
    f046rln_f046_rs_line_new_high_daysrsnh_252d_base_v070_signal,
    f046rln_f046_rs_line_new_high_daysrsnh_63d_base_v071_signal,
    f046rln_f046_rs_line_new_high_daysrsnh_504d_base_v072_signal,
    f046rln_f046_rs_line_new_high_rsxlead_63d_base_v073_signal,
    f046rln_f046_rs_line_new_high_rsxlead_252d_base_v074_signal,
    f046rln_f046_rs_line_new_high_rsnhxema5_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F046_RS_LINE_NEW_HIGH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f046_rs_line", "_f046_rs_new_high", "_f046_leadership_confirm")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f046_rs_line_new_high_base_001_075_claude: {n_features} features pass")
