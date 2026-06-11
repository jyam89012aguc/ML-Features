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
def _f23_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f23_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f23_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 5d slope of capex/revenue level
def f23ci_f23_semi_capex_intensity_intensrv_mean_21d_curv_v001_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/revenue level
def f23ci_f23_semi_capex_intensity_intensrv_mean_21d_curv_v002_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/revenue level
def f23ci_f23_semi_capex_intensity_intensrv_mean_21d_curv_v003_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex/revenue level
def f23ci_f23_semi_capex_intensity_intensrv_mean_21d_curv_v004_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex/revenue level
def f23ci_f23_semi_capex_intensity_intensrv_mean_21d_curv_v005_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    base = cx / rv.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z21_21d_curv_v006_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z21_21d_curv_v007_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z21_21d_curv_v008_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z21_21d_curv_v009_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z21_21d_curv_v010_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z63_63d_curv_v011_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z63_63d_curv_v012_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z63_63d_curv_v013_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z63_63d_curv_v014_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z63_63d_curv_v015_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z126_126d_curv_v016_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z126_126d_curv_v017_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z126_126d_curv_v018_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z126_126d_curv_v019_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z126_126d_curv_v020_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z252_252d_curv_v021_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z252_252d_curv_v022_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z252_252d_curv_v023_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z252_252d_curv_v024_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_z252_252d_curv_v025_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of capex/assets level
def f23ci_f23_semi_capex_intensity_intensas_mean_21d_curv_v026_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    base = cx / asx.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/assets level
def f23ci_f23_semi_capex_intensity_intensas_mean_21d_curv_v027_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    base = cx / asx.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/assets level
def f23ci_f23_semi_capex_intensity_intensas_mean_21d_curv_v028_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    base = cx / asx.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex/assets level
def f23ci_f23_semi_capex_intensity_intensas_mean_21d_curv_v029_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    base = cx / asx.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex/assets level
def f23ci_f23_semi_capex_intensity_intensas_mean_21d_curv_v030_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    base = cx / asx.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z63_63d_curv_v031_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z63_63d_curv_v032_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z63_63d_curv_v033_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z63_63d_curv_v034_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z63_63d_curv_v035_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z252_252d_curv_v036_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z252_252d_curv_v037_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z252_252d_curv_v038_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z252_252d_curv_v039_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z capex/assets
def f23ci_f23_semi_capex_intensity_intensas_z252_252d_curv_v040_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of capex/ppne level
def f23ci_f23_semi_capex_intensity_intenspp_mean_21d_curv_v041_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    base = cx / pp.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/ppne level
def f23ci_f23_semi_capex_intensity_intenspp_mean_21d_curv_v042_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    base = cx / pp.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/ppne level
def f23ci_f23_semi_capex_intensity_intenspp_mean_21d_curv_v043_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    base = cx / pp.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex/ppne level
def f23ci_f23_semi_capex_intensity_intenspp_mean_21d_curv_v044_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    base = cx / pp.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex/ppne level
def f23ci_f23_semi_capex_intensity_intenspp_mean_21d_curv_v045_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    base = cx / pp.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z63_63d_curv_v046_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z63_63d_curv_v047_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z63_63d_curv_v048_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z63_63d_curv_v049_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z63_63d_curv_v050_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z252_252d_curv_v051_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z252_252d_curv_v052_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z252_252d_curv_v053_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z252_252d_curv_v054_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z capex/ppne
def f23ci_f23_semi_capex_intensity_intenspp_z252_252d_curv_v055_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max63_63d_curv_v056_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max63_63d_curv_v057_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max63_63d_curv_v058_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max63_63d_curv_v059_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max63_63d_curv_v060_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max252_252d_curv_v061_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max252_252d_curv_v062_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max252_252d_curv_v063_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max252_252d_curv_v064_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d max capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max252_252d_curv_v065_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min63_63d_curv_v066_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min63_63d_curv_v067_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min63_63d_curv_v068_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min63_63d_curv_v069_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min63_63d_curv_v070_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min252_252d_curv_v071_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min252_252d_curv_v072_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min252_252d_curv_v073_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min252_252d_curv_v074_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d min capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min252_252d_curv_v075_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng63_63d_curv_v076_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng63_63d_curv_v077_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng63_63d_curv_v078_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng63_63d_curv_v079_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng63_63d_curv_v080_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng252_252d_curv_v081_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng252_252d_curv_v082_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng252_252d_curv_v083_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng252_252d_curv_v084_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d range capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng252_252d_curv_v085_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos63_63d_curv_v086_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos63_63d_curv_v087_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos63_63d_curv_v088_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos63_63d_curv_v089_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos63_63d_curv_v090_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos252_252d_curv_v091_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos252_252d_curv_v092_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos252_252d_curv_v093_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos252_252d_curv_v094_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pos-in-range
def f23ci_f23_semi_capex_intensity_intensrv_pos252_252d_curv_v095_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd63_63d_curv_v096_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd63_63d_curv_v097_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd63_63d_curv_v098_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd63_63d_curv_v099_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd63_63d_curv_v100_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd252_252d_curv_v101_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd252_252d_curv_v102_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd252_252d_curv_v103_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd252_252d_curv_v104_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d capex/revenue drawdown
def f23ci_f23_semi_capex_intensity_intensrv_dd252_252d_curv_v105_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std63_63d_curv_v106_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std63_63d_curv_v107_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std63_63d_curv_v108_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std63_63d_curv_v109_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std63_63d_curv_v110_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std252_252d_curv_v111_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std252_252d_curv_v112_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std252_252d_curv_v113_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std252_252d_curv_v114_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d std capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std252_252d_curv_v115_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz63_63d_curv_v116_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz63_63d_curv_v117_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz63_63d_curv_v118_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz63_63d_curv_v119_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz63_63d_curv_v120_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz252_252d_curv_v121_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz252_252d_curv_v122_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz252_252d_curv_v123_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz252_252d_curv_v124_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d log z capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_logz252_252d_curv_v125_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    lr = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    base = _z(lr, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew63_63d_curv_v126_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew63_63d_curv_v127_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew63_63d_curv_v128_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew63_63d_curv_v129_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew63_63d_curv_v130_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d kurt capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt63_63d_curv_v131_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d kurt capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt63_63d_curv_v132_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d kurt capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt63_63d_curv_v133_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d kurt capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt63_63d_curv_v134_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d kurt capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt63_63d_curv_v135_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(5)-ema(63) capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_5v63_curv_v136_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(5)-ema(63) capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_5v63_curv_v137_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(5)-ema(63) capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_5v63_curv_v138_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(5)-ema(63) capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_5v63_curv_v139_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(5)-ema(63) capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_5v63_curv_v140_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d rank capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rank63_63d_curv_v141_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rank capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rank63_63d_curv_v142_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d rank capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rank63_63d_curv_v143_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d rank capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rank63_63d_curv_v144_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d rank capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rank63_63d_curv_v145_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of mix composite z(63) intensity
def f23ci_f23_semi_capex_intensity_intensmix_z63_63d_curv_v146_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    base = _z(r1, 63) + _z(r2, 63) + _z(r3, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mix composite z(63) intensity
def f23ci_f23_semi_capex_intensity_intensmix_z63_63d_curv_v147_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    base = _z(r1, 63) + _z(r2, 63) + _z(r3, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mix composite z(63) intensity
def f23ci_f23_semi_capex_intensity_intensmix_z63_63d_curv_v148_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    base = _z(r1, 63) + _z(r2, 63) + _z(r3, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mix composite z(63) intensity
def f23ci_f23_semi_capex_intensity_intensmix_z63_63d_curv_v149_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    base = _z(r1, 63) + _z(r2, 63) + _z(r3, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of mix composite z(63) intensity
def f23ci_f23_semi_capex_intensity_intensmix_z63_63d_curv_v150_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    base = _z(r1, 63) + _z(r2, 63) + _z(r3, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
