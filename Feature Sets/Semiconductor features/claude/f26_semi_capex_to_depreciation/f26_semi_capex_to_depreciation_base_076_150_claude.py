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
def _f26_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f26_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f26_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d mean of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_21d_base_v001_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_63d_base_v002_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_126d_base_v003_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_252d_base_v004_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_mean_504d_base_v005_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z_21d_base_v006_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z_63d_base_v007_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z_126d_base_v008_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z_252d_base_v009_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_z_504d_base_v010_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rz_21d_base_v011_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rz_63d_base_v012_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rz_126d_base_v013_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rz_252d_base_v014_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rz_504d_base_v015_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_max_21d_base_v016_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_max_63d_base_v017_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_max_126d_base_v018_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_max_252d_base_v019_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_max_504d_base_v020_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_min_21d_base_v021_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_min_63d_base_v022_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_min_126d_base_v023_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_min_252d_base_v024_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_min_504d_base_v025_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rng_21d_base_v026_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 21) - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rng_63d_base_v027_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 63) - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rng_126d_base_v028_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 126) - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rng_252d_base_v029_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 252) - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_rng_504d_base_v030_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = _max(ratio, 504) - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pos-in-range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_pos_21d_base_v031_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    lo = _min(ratio, 21)
    hi = _max(ratio, 21)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pos-in-range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_pos_63d_base_v032_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pos-in-range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_pos_126d_base_v033_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    lo = _min(ratio, 126)
    hi = _max(ratio, 126)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pos-in-range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_pos_252d_base_v034_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pos-in-range log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_pos_504d_base_v035_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    lo = _min(ratio, 504)
    hi = _max(ratio, 504)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_dd_21d_base_v036_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = ratio - _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_dd_63d_base_v037_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = ratio - _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_dd_126d_base_v038_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = ratio - _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_dd_252d_base_v039_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = ratio - _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown log capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdlog_dd_504d_base_v040_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / da.abs().replace(0, np.nan))
    result = ratio - _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of capex/depamor YoY growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg_21d_base_v041_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=252)
    result = _mean(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/depamor YoY growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg_63d_base_v042_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=252)
    result = _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/depamor YoY growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg_126d_base_v043_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=252)
    result = _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/depamor YoY growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg_252d_base_v044_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=252)
    result = _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex/depamor YoY growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_yoyg_504d_base_v045_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=252)
    result = _mean(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of capex/depamor QoQ growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg_21d_base_v046_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=63)
    result = _mean(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/depamor QoQ growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg_63d_base_v047_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=63)
    result = _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/depamor QoQ growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg_126d_base_v048_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=63)
    result = _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/depamor QoQ growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg_252d_base_v049_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=63)
    result = _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex/depamor QoQ growth
def f26cd_f26_semi_capex_to_depreciation_cdratio_qoqg_504d_base_v050_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    g = ratio.pct_change(periods=63)
    result = _mean(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deviation from median capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed_21d_base_v051_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deviation from median capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed_63d_base_v052_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deviation from median capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed_126d_base_v053_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deviation from median capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed_252d_base_v054_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deviation from median capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_devmed_504d_base_v055_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quartile rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_quart_21d_base_v056_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quartile rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_quart_63d_base_v057_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quartile rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_quart_126d_base_v058_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quartile rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_quart_252d_base_v059_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quartile rank capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_quart_504d_base_v060_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of d/dt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_diff_21d_base_v061_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio.diff(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of d/dt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_diff_63d_base_v062_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio.diff(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of d/dt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_diff_126d_base_v063_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio.diff(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of d/dt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_diff_252d_base_v064_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio.diff(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of d/dt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_diff_504d_base_v065_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio.diff(), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction days capex/depamor < 0.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_loabsmask_21d_base_v066_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio < 0.5).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction days capex/depamor < 0.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_loabsmask_63d_base_v067_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio < 0.5).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction days capex/depamor < 0.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_loabsmask_126d_base_v068_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio < 0.5).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction days capex/depamor < 0.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_loabsmask_252d_base_v069_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio < 0.5).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction days capex/depamor < 0.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_loabsmask_504d_base_v070_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio < 0.5).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction days capex/depamor > 1.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_hiabsmask_21d_base_v071_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1.5).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction days capex/depamor > 1.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_hiabsmask_63d_base_v072_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1.5).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction days capex/depamor > 1.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_hiabsmask_126d_base_v073_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1.5).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction days capex/depamor > 1.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_hiabsmask_252d_base_v074_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1.5).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction days capex/depamor > 1.5
def f26cd_f26_semi_capex_to_depreciation_cdratio_hiabsmask_504d_base_v075_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1.5).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)
