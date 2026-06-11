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


# 21d mean of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_21d_base_v001_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_63d_base_v002_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_126d_base_v003_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_252d_base_v004_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_mean_504d_base_v005_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z_21d_base_v006_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z_63d_base_v007_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z_126d_base_v008_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z_252d_base_v009_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z of capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_z_504d_base_v010_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rz_21d_base_v011_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rz_63d_base_v012_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rz_126d_base_v013_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rz_252d_base_v014_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rz_504d_base_v015_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max_21d_base_v016_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max_63d_base_v017_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max_126d_base_v018_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max_252d_base_v019_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_max_504d_base_v020_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min_21d_base_v021_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min_63d_base_v022_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min_126d_base_v023_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min_252d_base_v024_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_min_504d_base_v025_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng_21d_base_v026_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 21) - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng_63d_base_v027_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 63) - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng_126d_base_v028_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 126) - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng_252d_base_v029_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 252) - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_rng_504d_base_v030_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _max(ratio, 504) - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pos-in-range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos_21d_base_v031_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 21)
    hi = _max(ratio, 21)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pos-in-range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos_63d_base_v032_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pos-in-range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos_126d_base_v033_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 126)
    hi = _max(ratio, 126)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pos-in-range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos_252d_base_v034_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pos-in-range capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_pos_504d_base_v035_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    lo = _min(ratio, 504)
    hi = _max(ratio, 504)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd_21d_base_v036_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd_63d_base_v037_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd_126d_base_v038_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd_252d_base_v039_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_dd_504d_base_v040_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_runup_21d_base_v041_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_runup_63d_base_v042_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_runup_126d_base_v043_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_runup_252d_base_v044_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_runup_504d_base_v045_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std_21d_base_v046_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _std(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std_63d_base_v047_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _std(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std_126d_base_v048_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _std(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std_252d_base_v049_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _std(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_std_504d_base_v050_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = _std(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew_21d_base_v051_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew_63d_base_v052_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew_126d_base_v053_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew_252d_base_v054_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_skew_504d_base_v055_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt_21d_base_v056_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt_63d_base_v057_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt_126d_base_v058_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt_252d_base_v059_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurt capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_kurt_504d_base_v060_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction days capex/depamor > 1
def f26cd_f26_semi_capex_to_depreciation_cdratio_above1_21d_base_v061_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction days capex/depamor > 1
def f26cd_f26_semi_capex_to_depreciation_cdratio_above1_63d_base_v062_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction days capex/depamor > 1
def f26cd_f26_semi_capex_to_depreciation_cdratio_above1_126d_base_v063_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction days capex/depamor > 1
def f26cd_f26_semi_capex_to_depreciation_cdratio_above1_252d_base_v064_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction days capex/depamor > 1
def f26cd_f26_semi_capex_to_depreciation_cdratio_above1_504d_base_v065_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = (ratio > 1).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cum capex/depamor innovations
def f26cd_f26_semi_capex_to_depreciation_cdratio_signcum_21d_base_v066_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cum capex/depamor innovations
def f26cd_f26_semi_capex_to_depreciation_cdratio_signcum_63d_base_v067_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cum capex/depamor innovations
def f26cd_f26_semi_capex_to_depreciation_cdratio_signcum_126d_base_v068_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cum capex/depamor innovations
def f26cd_f26_semi_capex_to_depreciation_cdratio_signcum_252d_base_v069_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cum capex/depamor innovations
def f26cd_f26_semi_capex_to_depreciation_cdratio_signcum_504d_base_v070_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema(5)-ema(21) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_21d_base_v071_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(5)-ema(63) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_63d_base_v072_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(5)-ema(126) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_126d_base_v073_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(5)-ema(252) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_252d_base_v074_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(5)-ema(504) capex/depamor
def f26cd_f26_semi_capex_to_depreciation_cdratio_ema_504d_base_v075_signal(capex, depamor, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    da = depamor.reindex(closeadj.index).ffill()
    ratio = cx / da.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)
