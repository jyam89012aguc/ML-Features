import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f27_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f27_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f27_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 5d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_curv_v001_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_curv_v002_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_curv_v003_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_curv_v004_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_curv_v005_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_curv_v006_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_curv_v007_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_curv_v008_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_curv_v009_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_curv_v010_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_curv_v011_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_curv_v012_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_curv_v013_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_curv_v014_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_curv_v015_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_curv_v016_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_curv_v017_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_curv_v018_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_curv_v019_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_curv_v020_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_curv_v021_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_curv_v022_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_curv_v023_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_curv_v024_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_curv_v025_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_curv_v026_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_curv_v027_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_curv_v028_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_curv_v029_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_curv_v030_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_curv_v031_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_curv_v032_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_curv_v033_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_curv_v034_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_curv_v035_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_curv_v036_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_curv_v037_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_curv_v038_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_curv_v039_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_curv_v040_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_curv_v041_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_curv_v042_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_curv_v043_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_curv_v044_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_curv_v045_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_curv_v046_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_curv_v047_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_curv_v048_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_curv_v049_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_curv_v050_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_curv_v051_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_curv_v052_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_curv_v053_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_curv_v054_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_curv_v055_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_curv_v056_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_curv_v057_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_curv_v058_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_curv_v059_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_curv_v060_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_curv_v061_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_curv_v062_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_curv_v063_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_curv_v064_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_curv_v065_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_curv_v066_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_curv_v067_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_curv_v068_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_curv_v069_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_curv_v070_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_curv_v071_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_curv_v072_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_curv_v073_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_curv_v074_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_curv_v075_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_curv_v076_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_curv_v077_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_curv_v078_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_curv_v079_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_curv_v080_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_curv_v081_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_curv_v082_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_curv_v083_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_curv_v084_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_curv_v085_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_curv_v086_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_curv_v087_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_curv_v088_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_curv_v089_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_curv_v090_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_curv_v091_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_curv_v092_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_curv_v093_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_curv_v094_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_curv_v095_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_curv_v096_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_curv_v097_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_curv_v098_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_curv_v099_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_curv_v100_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_curv_v101_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_curv_v102_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_curv_v103_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_curv_v104_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_curv_v105_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_curv_v106_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_curv_v107_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_curv_v108_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_curv_v109_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_curv_v110_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_curv_v111_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_curv_v112_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_curv_v113_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_curv_v114_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_curv_v115_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_curv_v116_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_curv_v117_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_curv_v118_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_curv_v119_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_curv_v120_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_curv_v121_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_curv_v122_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_curv_v123_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_curv_v124_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_curv_v125_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_curv_v126_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_curv_v127_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_curv_v128_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_curv_v129_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_curv_v130_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_curv_v131_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_curv_v132_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_curv_v133_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_curv_v134_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_curv_v135_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_curv_v136_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_curv_v137_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_curv_v138_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_curv_v139_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_curv_v140_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_curv_v141_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_curv_v142_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_curv_v143_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_curv_v144_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_curv_v145_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_curv_v146_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_curv_v147_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_curv_v148_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_curv_v149_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_curv_v150_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
