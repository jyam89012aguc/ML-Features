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
def _f23_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f23_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f23_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d mean of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_mean_21d_base_v001_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_mean_63d_base_v002_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_mean_126d_base_v003_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_mean_252d_base_v004_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_mean_504d_base_v005_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_mean_21d_base_v006_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_mean_63d_base_v007_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_mean_126d_base_v008_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_mean_252d_base_v009_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_mean_504d_base_v010_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_mean_21d_base_v011_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _mean(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_mean_63d_base_v012_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _mean(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_mean_126d_base_v013_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _mean(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_mean_252d_base_v014_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _mean(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_mean_504d_base_v015_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _mean(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_z_21d_base_v016_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_z_63d_base_v017_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_z_126d_base_v018_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_z_252d_base_v019_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of capex/revenue intensity
def f23ci_f23_semi_capex_intensity_intensrv_z_504d_base_v020_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_z_21d_base_v021_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_z_63d_base_v022_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_z_126d_base_v023_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_z_252d_base_v024_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of capex/assets intensity
def f23ci_f23_semi_capex_intensity_intensas_z_504d_base_v025_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_z_21d_base_v026_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_z_63d_base_v027_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_z_126d_base_v028_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_z_252d_base_v029_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of capex/ppne intensity
def f23ci_f23_semi_capex_intensity_intenspp_z_504d_base_v030_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of capex/revenue (median/MAD)
def f23ci_f23_semi_capex_intensity_intensrv_rz_21d_base_v031_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of capex/revenue (median/MAD)
def f23ci_f23_semi_capex_intensity_intensrv_rz_63d_base_v032_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of capex/revenue (median/MAD)
def f23ci_f23_semi_capex_intensity_intensrv_rz_126d_base_v033_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of capex/revenue (median/MAD)
def f23ci_f23_semi_capex_intensity_intensrv_rz_252d_base_v034_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of capex/revenue (median/MAD)
def f23ci_f23_semi_capex_intensity_intensrv_rz_504d_base_v035_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of capex/assets (median/MAD)
def f23ci_f23_semi_capex_intensity_intensas_rz_21d_base_v036_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of capex/assets (median/MAD)
def f23ci_f23_semi_capex_intensity_intensas_rz_63d_base_v037_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of capex/assets (median/MAD)
def f23ci_f23_semi_capex_intensity_intensas_rz_126d_base_v038_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of capex/assets (median/MAD)
def f23ci_f23_semi_capex_intensity_intensas_rz_252d_base_v039_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of capex/assets (median/MAD)
def f23ci_f23_semi_capex_intensity_intensas_rz_504d_base_v040_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of capex/ppne (median/MAD)
def f23ci_f23_semi_capex_intensity_intenspp_rz_21d_base_v041_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    mad = (ratio - med).abs().rolling(21, min_periods=max(1, 21//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of capex/ppne (median/MAD)
def f23ci_f23_semi_capex_intensity_intenspp_rz_63d_base_v042_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    mad = (ratio - med).abs().rolling(63, min_periods=max(1, 63//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of capex/ppne (median/MAD)
def f23ci_f23_semi_capex_intensity_intenspp_rz_126d_base_v043_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    mad = (ratio - med).abs().rolling(126, min_periods=max(1, 126//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of capex/ppne (median/MAD)
def f23ci_f23_semi_capex_intensity_intenspp_rz_252d_base_v044_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    mad = (ratio - med).abs().rolling(252, min_periods=max(1, 252//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of capex/ppne (median/MAD)
def f23ci_f23_semi_capex_intensity_intenspp_rz_504d_base_v045_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = cx / pp.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    mad = (ratio - med).abs().rolling(504, min_periods=max(1, 504//2)).median()
    result = (ratio - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling max of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max_21d_base_v046_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling max of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max_63d_base_v047_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling max of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max_126d_base_v048_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling max of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max_252d_base_v049_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling max of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_max_504d_base_v050_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling min of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min_21d_base_v051_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling min of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min_63d_base_v052_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling min of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min_126d_base_v053_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling min of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min_252d_base_v054_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling min of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_min_504d_base_v055_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range (max-min) of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng_21d_base_v056_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 21) - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range (max-min) of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng_63d_base_v057_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 63) - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range (max-min) of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng_126d_base_v058_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 126) - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range (max-min) of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng_252d_base_v059_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 252) - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range (max-min) of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_rng_504d_base_v060_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _max(ratio, 504) - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_pos_21d_base_v061_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 21)
    hi = _max(ratio, 21)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_pos_63d_base_v062_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 63)
    hi = _max(ratio, 63)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_pos_126d_base_v063_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 126)
    hi = _max(ratio, 126)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_pos_252d_base_v064_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 252)
    hi = _max(ratio, 252)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_pos_504d_base_v065_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    lo = _min(ratio, 504)
    hi = _max(ratio, 504)
    result = (ratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std_21d_base_v066_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _std(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std_63d_base_v067_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _std(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std_126d_base_v068_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _std(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std_252d_base_v069_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _std(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_std_504d_base_v070_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = _std(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of capex/revenue from rolling peak
def f23ci_f23_semi_capex_intensity_intensrv_dd_21d_base_v071_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _max(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of capex/revenue from rolling peak
def f23ci_f23_semi_capex_intensity_intensrv_dd_63d_base_v072_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _max(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of capex/revenue from rolling peak
def f23ci_f23_semi_capex_intensity_intensrv_dd_126d_base_v073_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _max(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of capex/revenue from rolling peak
def f23ci_f23_semi_capex_intensity_intensrv_dd_252d_base_v074_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _max(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of capex/revenue from rolling peak
def f23ci_f23_semi_capex_intensity_intensrv_dd_504d_base_v075_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _max(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)
