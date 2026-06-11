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
def _f26_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f26_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f26_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 5d slope of capex/depamor level
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_level_curv_v001_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = cx / da.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/depamor level
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_level_curv_v002_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = cx / da.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/depamor level
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_level_curv_v003_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = cx / da.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of capex/depamor level
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_level_curv_v004_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = cx / da.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of capex/depamor level
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_level_curv_v005_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = cx / da.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z21_21d_curv_v006_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z21_21d_curv_v007_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z21_21d_curv_v008_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z21_21d_curv_v009_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z21_21d_curv_v010_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z63_63d_curv_v011_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z63_63d_curv_v012_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z63_63d_curv_v013_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z63_63d_curv_v014_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z63_63d_curv_v015_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z126_126d_curv_v016_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z126_126d_curv_v017_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z126_126d_curv_v018_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z126_126d_curv_v019_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z126_126d_curv_v020_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z252_252d_curv_v021_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z252_252d_curv_v022_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z252_252d_curv_v023_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z252_252d_curv_v024_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z252_252d_curv_v025_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_log_curv_v026_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_log_curv_v027_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_log_curv_v028_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_log_curv_v029_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_log_curv_v030_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    base = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z63_63d_curv_v031_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z63_63d_curv_v032_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z63_63d_curv_v033_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z63_63d_curv_v034_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z63_63d_curv_v035_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z252_252d_curv_v036_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z252_252d_curv_v037_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z252_252d_curv_v038_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z252_252d_curv_v039_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z252_252d_curv_v040_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    base = _z(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max63_63d_curv_v041_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max63_63d_curv_v042_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max63_63d_curv_v043_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max63_63d_curv_v044_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max63_63d_curv_v045_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max252_252d_curv_v046_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max252_252d_curv_v047_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max252_252d_curv_v048_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max252_252d_curv_v049_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max252_252d_curv_v050_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min63_63d_curv_v051_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min63_63d_curv_v052_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min63_63d_curv_v053_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min63_63d_curv_v054_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min63_63d_curv_v055_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min252_252d_curv_v056_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min252_252d_curv_v057_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min252_252d_curv_v058_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min252_252d_curv_v059_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min252_252d_curv_v060_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _min(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng63_63d_curv_v061_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng63_63d_curv_v062_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng63_63d_curv_v063_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng63_63d_curv_v064_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng63_63d_curv_v065_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 63) - _min(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng252_252d_curv_v066_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng252_252d_curv_v067_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng252_252d_curv_v068_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng252_252d_curv_v069_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng252_252d_curv_v070_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _max(ratio, 252) - _min(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos63_63d_curv_v071_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos63_63d_curv_v072_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos63_63d_curv_v073_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos63_63d_curv_v074_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos63_63d_curv_v075_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos252_252d_curv_v076_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos252_252d_curv_v077_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos252_252d_curv_v078_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos252_252d_curv_v079_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pos-in-range
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos252_252d_curv_v080_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    base = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd63_63d_curv_v081_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd63_63d_curv_v082_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd63_63d_curv_v083_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd63_63d_curv_v084_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd63_63d_curv_v085_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd252_252d_curv_v086_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd252_252d_curv_v087_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd252_252d_curv_v088_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd252_252d_curv_v089_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d drawdown
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd252_252d_curv_v090_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio - _max(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std63_63d_curv_v091_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std63_63d_curv_v092_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std63_63d_curv_v093_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std63_63d_curv_v094_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std63_63d_curv_v095_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std252_252d_curv_v096_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std252_252d_curv_v097_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std252_252d_curv_v098_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std252_252d_curv_v099_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std252_252d_curv_v100_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _std(ratio, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew63_63d_curv_v101_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew63_63d_curv_v102_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew63_63d_curv_v103_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew63_63d_curv_v104_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew63_63d_curv_v105_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt63_63d_curv_v106_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt63_63d_curv_v107_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt63_63d_curv_v108_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt63_63d_curv_v109_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt63_63d_curv_v110_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).kurt()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m63_63d_curv_v111_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m63_63d_curv_v112_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m63_63d_curv_v113_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m63_63d_curv_v114_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m63_63d_curv_v115_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m252_252d_curv_v116_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m252_252d_curv_v117_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m252_252d_curv_v118_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m252_252d_curv_v119_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d above-1 mask
def f26cd_f26_semi_capex_to_depreciation_cdratio_ab1m252_252d_curv_v120_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = (ratio > 1).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ema(5)-ema(63) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_5v63_curv_v121_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ema(5)-ema(63) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_5v63_curv_v122_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ema(5)-ema(63) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_5v63_curv_v123_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ema(5)-ema(63) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_5v63_curv_v124_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of ema(5)-ema(63) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_5v63_curv_v125_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rank63_63d_curv_v126_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rank63_63d_curv_v127_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rank63_63d_curv_v128_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rank63_63d_curv_v129_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rank63_63d_curv_v130_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = ratio.rolling(63, min_periods=32).rank(pct=True)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg63_63d_curv_v131_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg63_63d_curv_v132_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg63_63d_curv_v133_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg63_63d_curv_v134_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg63_63d_curv_v135_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg252_252d_curv_v136_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg252_252d_curv_v137_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg252_252d_curv_v138_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg252_252d_curv_v139_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d YoY growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg252_252d_curv_v140_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=252), 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d QoQ growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg63_63d_curv_v141_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=63), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d QoQ growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg63_63d_curv_v142_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=63), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d QoQ growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg63_63d_curv_v143_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=63), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d QoQ growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg63_63d_curv_v144_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=63), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d QoQ growth capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg63_63d_curv_v145_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    base = _mean(ratio.pct_change(periods=63), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d dev-from-median
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed63_63d_curv_v146_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio - med
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dev-from-median
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed63_63d_curv_v147_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio - med
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d dev-from-median
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed63_63d_curv_v148_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio - med
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d dev-from-median
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed63_63d_curv_v149_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio - med
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d dev-from-median
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed63_63d_curv_v150_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=32).median()
    base = ratio - med
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
