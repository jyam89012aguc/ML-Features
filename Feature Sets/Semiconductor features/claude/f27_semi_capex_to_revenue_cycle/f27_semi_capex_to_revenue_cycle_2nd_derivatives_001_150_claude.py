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


# ===== folder domain primitives =====
def _f27_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f27_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f27_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 5d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_slope_v001_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_slope_v002_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_slope_v003_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_slope_v004_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex/rev level
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_mean_level_slope_v005_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_slope_v006_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_slope_v007_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_slope_v008_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_slope_v009_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z21_21d_slope_v010_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_slope_v011_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_slope_v012_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_slope_v013_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_slope_v014_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z63_63d_slope_v015_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_slope_v016_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_slope_v017_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_slope_v018_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_slope_v019_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z126_126d_slope_v020_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_slope_v021_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_slope_v022_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_slope_v023_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_slope_v024_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crratio_z252_252d_slope_v025_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_slope_v026_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_slope_v027_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_slope_v028_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_slope_v029_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(21)-ema(63) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema63_21v63_slope_v030_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_slope_v031_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_slope_v032_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_slope_v033_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_slope_v034_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(21)-ema(126) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema126_21v126_slope_v035_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_slope_v036_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_slope_v037_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_slope_v038_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_slope_v039_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(63)-ema(252) capex/rev
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_ema252_63v252_slope_v040_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_slope_v041_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_slope_v042_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_slope_v043_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_slope_v044_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of above-63d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above63_63d_slope_v045_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_slope_v046_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_slope_v047_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_slope_v048_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_slope_v049_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of above-252d-mean mask
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_above252_252d_slope_v050_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_slope_v051_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_slope_v052_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_slope_v053_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_slope_v054_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup63_63d_slope_v055_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio > m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_slope_v056_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_slope_v057_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_slope_v058_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_slope_v059_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d dn-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durdn63_63d_slope_v060_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = (ratio < m).astype(float).rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_slope_v061_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_slope_v062_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_slope_v063_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_slope_v064_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d up-duration
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_durup252_252d_slope_v065_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    base = (ratio > m).astype(float).rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_slope_v066_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_slope_v067_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_slope_v068_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_slope_v069_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff63_63d_slope_v070_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_slope_v071_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_slope_v072_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_slope_v073_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_slope_v074_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d capex/rev minus mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pdiff252_252d_slope_v075_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _mean(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_slope_v076_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_slope_v077_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_slope_v078_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_slope_v079_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio63_63d_slope_v080_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 63).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_slope_v081_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_slope_v082_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_slope_v083_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_slope_v084_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d capex/rev divided by mean
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_pratio252_252d_slope_v085_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio / _mean(ratio, 252).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_slope_v086_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_slope_v087_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_slope_v088_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_slope_v089_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d peak distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_peak63_63d_slope_v090_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - ratio
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_slope_v091_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_slope_v092_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_slope_v093_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_slope_v094_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d trough distance
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_trough63_63d_slope_v095_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _min(ratio, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_slope_v096_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_slope_v097_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_slope_v098_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_slope_v099_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d centered
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_centered63_63d_slope_v100_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    mid = 0.5 * (_max(ratio, 63) + _min(ratio, 63))
    base = ratio - mid
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_slope_v101_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_slope_v102_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_slope_v103_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_slope_v104_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d mean of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zmean63_63d_slope_v105_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _mean(z, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_slope_v106_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_slope_v107_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_slope_v108_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_slope_v109_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of 63d-z
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_zstd63_63d_slope_v110_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = _std(z, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_slope_v111_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_slope_v112_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_slope_v113_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_slope_v114_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d duration-frac z>0
def f27cr_f27_semi_capex_to_revenue_cycle_crregime_hizfrac63_63d_slope_v115_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    z = _z(ratio, 63)
    base = (z > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_slope_v116_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_slope_v117_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_slope_v118_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_slope_v119_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(63)-ema(252) regime
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_emadiff252_63v252_slope_v120_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_slope_v121_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_slope_v122_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_slope_v123_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_slope_v124_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/rev/median
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_robpiq63_63d_slope_v125_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio / med.replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_slope_v126_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_slope_v127_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_slope_v128_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_slope_v129_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d-z minus 252d-z spread
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_zspread63_spread_slope_v130_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) - _z(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_slope_v131_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_slope_v132_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_slope_v133_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_slope_v134_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d sign-flip count
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_flips63_63d_slope_v135_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    d = ratio - _mean(ratio, 63)
    sg = np.sign(d).diff().abs()
    base = sg.rolling(63, min_periods=32).sum() / 2.0
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_slope_v136_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_slope_v137_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_slope_v138_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_slope_v139_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d phase-up mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phaseup63_63d_slope_v140_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio > m) & (ratio.diff() > 0)).astype(float)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_slope_v141_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_slope_v142_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_slope_v143_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_slope_v144_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d phase-dn mask
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_phasedn63_63d_slope_v145_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    base = ((ratio < m) & (ratio.diff() < 0)).astype(float)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_slope_v146_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_slope_v147_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_slope_v148_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_slope_v149_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d composite z signal
def f27cr_f27_semi_capex_to_revenue_cycle_crcycle_compos63_compos_slope_v150_signal(capex, revenue, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21) + _z(ratio, 63) + _z(ratio, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
