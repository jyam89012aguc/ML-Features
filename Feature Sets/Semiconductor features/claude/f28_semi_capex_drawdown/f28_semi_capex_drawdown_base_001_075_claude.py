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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f28_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f28_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f28_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d mean of capex drawdown vs 21d peak
def f28cdd_f28_semi_capex_drawdown_cddabs_mean_21d_base_v001_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = _mean(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex drawdown vs 63d peak
def f28cdd_f28_semi_capex_drawdown_cddabs_mean_63d_base_v002_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = _mean(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex drawdown vs 126d peak
def f28cdd_f28_semi_capex_drawdown_cddabs_mean_126d_base_v003_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = _mean(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex drawdown vs 252d peak
def f28cdd_f28_semi_capex_drawdown_cddabs_mean_252d_base_v004_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = _mean(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex drawdown vs 504d peak
def f28cdd_f28_semi_capex_drawdown_cddabs_mean_504d_base_v005_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = _mean(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min (deepest) capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_min_21d_base_v006_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = _min(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min (deepest) capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_min_63d_base_v007_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = _min(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min (deepest) capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_min_126d_base_v008_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = _min(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min (deepest) capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_min_252d_base_v009_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = _min(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min (deepest) capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_min_504d_base_v010_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = _min(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_z_21d_base_v011_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 21)
    result = _z(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_z_63d_base_v012_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 63)
    result = _z(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_z_126d_base_v013_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 126)
    result = _z(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_z_252d_base_v014_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 252)
    result = _z(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of capex drawdown
def f28cdd_f28_semi_capex_drawdown_cddabs_z_504d_base_v015_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    dd = cx - _max(cx, 504)
    result = _z(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean relative drawdown (capex/peak - 1)
def f28cdd_f28_semi_capex_drawdown_cddrel_mean_21d_base_v016_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _mean(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean relative drawdown (capex/peak - 1)
def f28cdd_f28_semi_capex_drawdown_cddrel_mean_63d_base_v017_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _mean(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean relative drawdown (capex/peak - 1)
def f28cdd_f28_semi_capex_drawdown_cddrel_mean_126d_base_v018_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _mean(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean relative drawdown (capex/peak - 1)
def f28cdd_f28_semi_capex_drawdown_cddrel_mean_252d_base_v019_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _mean(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean relative drawdown (capex/peak - 1)
def f28cdd_f28_semi_capex_drawdown_cddrel_mean_504d_base_v020_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _mean(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_min_21d_base_v021_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _min(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_min_63d_base_v022_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _min(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_min_126d_base_v023_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _min(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_min_252d_base_v024_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _min(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_min_504d_base_v025_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _min(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_z_21d_base_v026_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _z(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_z_63d_base_v027_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _z(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_z_126d_base_v028_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _z(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_z_252d_base_v029_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _z(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z relative drawdown
def f28cdd_f28_semi_capex_drawdown_cddrel_z_504d_base_v030_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = _z(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean log drawdown (log capex - log peak)
def f28cdd_f28_semi_capex_drawdown_cddlog_mean_21d_base_v031_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 21)
    dd = lc - peak
    result = _mean(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean log drawdown (log capex - log peak)
def f28cdd_f28_semi_capex_drawdown_cddlog_mean_63d_base_v032_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 63)
    dd = lc - peak
    result = _mean(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean log drawdown (log capex - log peak)
def f28cdd_f28_semi_capex_drawdown_cddlog_mean_126d_base_v033_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 126)
    dd = lc - peak
    result = _mean(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean log drawdown (log capex - log peak)
def f28cdd_f28_semi_capex_drawdown_cddlog_mean_252d_base_v034_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 252)
    dd = lc - peak
    result = _mean(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean log drawdown (log capex - log peak)
def f28cdd_f28_semi_capex_drawdown_cddlog_mean_504d_base_v035_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 504)
    dd = lc - peak
    result = _mean(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min log drawdown
def f28cdd_f28_semi_capex_drawdown_cddlog_min_21d_base_v036_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 21)
    dd = lc - peak
    result = _min(dd, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min log drawdown
def f28cdd_f28_semi_capex_drawdown_cddlog_min_63d_base_v037_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 63)
    dd = lc - peak
    result = _min(dd, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min log drawdown
def f28cdd_f28_semi_capex_drawdown_cddlog_min_126d_base_v038_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 126)
    dd = lc - peak
    result = _min(dd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min log drawdown
def f28cdd_f28_semi_capex_drawdown_cddlog_min_252d_base_v039_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 252)
    dd = lc - peak
    result = _min(dd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min log drawdown
def f28cdd_f28_semi_capex_drawdown_cddlog_min_504d_base_v040_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lc = np.log(cx.abs().replace(0, np.nan))
    peak = _max(lc, 504)
    dd = lc - peak
    result = _min(dd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean capex run-up from 21d trough
def f28cdd_f28_semi_capex_drawdown_cddrun_mean_21d_base_v041_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 21)
    ru = cx - trough
    result = _mean(ru, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean capex run-up from 63d trough
def f28cdd_f28_semi_capex_drawdown_cddrun_mean_63d_base_v042_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 63)
    ru = cx - trough
    result = _mean(ru, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean capex run-up from 126d trough
def f28cdd_f28_semi_capex_drawdown_cddrun_mean_126d_base_v043_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 126)
    ru = cx - trough
    result = _mean(ru, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean capex run-up from 252d trough
def f28cdd_f28_semi_capex_drawdown_cddrun_mean_252d_base_v044_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 252)
    ru = cx - trough
    result = _mean(ru, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean capex run-up from 504d trough
def f28cdd_f28_semi_capex_drawdown_cddrun_mean_504d_base_v045_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 504)
    ru = cx - trough
    result = _mean(ru, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_max_21d_base_v046_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 21)
    ru = cx - trough
    result = _max(ru, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_max_63d_base_v047_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 63)
    ru = cx - trough
    result = _max(ru, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_max_126d_base_v048_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 126)
    ru = cx - trough
    result = _max(ru, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_max_252d_base_v049_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 252)
    ru = cx - trough
    result = _max(ru, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_max_504d_base_v050_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 504)
    ru = cx - trough
    result = _max(ru, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_z_21d_base_v051_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 21)
    ru = cx - trough
    result = _z(ru, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_z_63d_base_v052_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 63)
    ru = cx - trough
    result = _z(ru, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_z_126d_base_v053_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 126)
    ru = cx - trough
    result = _z(ru, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_z_252d_base_v054_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 252)
    ru = cx - trough
    result = _z(ru, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z capex run-up
def f28cdd_f28_semi_capex_drawdown_cddrun_z_504d_base_v055_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    trough = _min(cx, 504)
    ru = cx - trough
    result = _z(ru, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex distance to rolling peak (positive)
def f28cdd_f28_semi_capex_drawdown_cddpeakdist_21d_base_v056_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = _max(cx, 21) - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex distance to rolling peak (positive)
def f28cdd_f28_semi_capex_drawdown_cddpeakdist_63d_base_v057_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = _max(cx, 63) - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex distance to rolling peak (positive)
def f28cdd_f28_semi_capex_drawdown_cddpeakdist_126d_base_v058_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = _max(cx, 126) - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex distance to rolling peak (positive)
def f28cdd_f28_semi_capex_drawdown_cddpeakdist_252d_base_v059_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = _max(cx, 252) - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex distance to rolling peak (positive)
def f28cdd_f28_semi_capex_drawdown_cddpeakdist_504d_base_v060_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = _max(cx, 504) - cx
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex distance from rolling trough
def f28cdd_f28_semi_capex_drawdown_cddtrohdist_21d_base_v061_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = cx - _min(cx, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex distance from rolling trough
def f28cdd_f28_semi_capex_drawdown_cddtrohdist_63d_base_v062_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = cx - _min(cx, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex distance from rolling trough
def f28cdd_f28_semi_capex_drawdown_cddtrohdist_126d_base_v063_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = cx - _min(cx, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex distance from rolling trough
def f28cdd_f28_semi_capex_drawdown_cddtrohdist_252d_base_v064_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = cx - _min(cx, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex distance from rolling trough
def f28cdd_f28_semi_capex_drawdown_cddtrohdist_504d_base_v065_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    result = cx - _min(cx, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d duration with capex below 21d peak by >10pct
def f28cdd_f28_semi_capex_drawdown_cddrelmin_dur_21d_base_v066_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 21)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = (dd < -0.1).astype(float).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration with capex below 63d peak by >10pct
def f28cdd_f28_semi_capex_drawdown_cddrelmin_dur_63d_base_v067_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 63)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = (dd < -0.1).astype(float).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d duration with capex below 126d peak by >10pct
def f28cdd_f28_semi_capex_drawdown_cddrelmin_dur_126d_base_v068_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 126)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = (dd < -0.1).astype(float).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration with capex below 252d peak by >10pct
def f28cdd_f28_semi_capex_drawdown_cddrelmin_dur_252d_base_v069_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 252)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = (dd < -0.1).astype(float).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d duration with capex below 504d peak by >10pct
def f28cdd_f28_semi_capex_drawdown_cddrelmin_dur_504d_base_v070_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    peak = _max(cx, 504)
    dd = cx / peak.replace(0, np.nan) - 1.0
    result = (dd < -0.1).astype(float).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position in capex range (low..high)
def f28cdd_f28_semi_capex_drawdown_cddpos_21d_base_v071_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lo = _min(cx, 21)
    hi = _max(cx, 21)
    result = (cx - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position in capex range (low..high)
def f28cdd_f28_semi_capex_drawdown_cddpos_63d_base_v072_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lo = _min(cx, 63)
    hi = _max(cx, 63)
    result = (cx - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position in capex range (low..high)
def f28cdd_f28_semi_capex_drawdown_cddpos_126d_base_v073_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lo = _min(cx, 126)
    hi = _max(cx, 126)
    result = (cx - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position in capex range (low..high)
def f28cdd_f28_semi_capex_drawdown_cddpos_252d_base_v074_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lo = _min(cx, 252)
    hi = _max(cx, 252)
    result = (cx - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position in capex range (low..high)
def f28cdd_f28_semi_capex_drawdown_cddpos_504d_base_v075_signal(capex, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    lo = _min(cx, 504)
    hi = _max(cx, 504)
    result = (cx - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
