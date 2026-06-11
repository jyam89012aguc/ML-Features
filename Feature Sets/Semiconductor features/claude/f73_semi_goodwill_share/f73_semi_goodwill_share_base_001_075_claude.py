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
def _f73gs_int_assets(intang, assets):
    return intang / assets.replace(0, np.nan)


def _f73gs_int_equity(intang, equity):
    return intang / equity.replace(0, np.nan)


def _f73gs_int_tangibles(intang, tangibles):
    return intang / tangibles.replace(0, np.nan)


def _f73gs_int_revenue(intang, revenue):
    return intang / revenue.replace(0, np.nan)


def _f73gs_align(q, idx):
    return q.reindex(idx).ffill()


# level 21d mean-centered (intassets)
def f73gs_f73_semi_goodwill_share_intassets_level_21d_base_v001_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 21d mean-centered (intequity)
def f73gs_f73_semi_goodwill_share_intequity_level_21d_base_v002_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 21d mean-centered (inttangibles)
def f73gs_f73_semi_goodwill_share_inttangibles_level_21d_base_v003_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 21d mean-centered (intrevenue)
def f73gs_f73_semi_goodwill_share_intrevenue_level_21d_base_v004_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = m - _mean(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (intassets)
def f73gs_f73_semi_goodwill_share_intassets_level_63d_base_v005_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (intequity)
def f73gs_f73_semi_goodwill_share_intequity_level_63d_base_v006_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (inttangibles)
def f73gs_f73_semi_goodwill_share_inttangibles_level_63d_base_v007_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 63d mean-centered (intrevenue)
def f73gs_f73_semi_goodwill_share_intrevenue_level_63d_base_v008_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (intassets)
def f73gs_f73_semi_goodwill_share_intassets_level_126d_base_v009_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (intequity)
def f73gs_f73_semi_goodwill_share_intequity_level_126d_base_v010_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (inttangibles)
def f73gs_f73_semi_goodwill_share_inttangibles_level_126d_base_v011_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 126d mean-centered (intrevenue)
def f73gs_f73_semi_goodwill_share_intrevenue_level_126d_base_v012_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = m - _mean(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (intassets)
def f73gs_f73_semi_goodwill_share_intassets_level_252d_base_v013_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (intequity)
def f73gs_f73_semi_goodwill_share_intequity_level_252d_base_v014_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (inttangibles)
def f73gs_f73_semi_goodwill_share_inttangibles_level_252d_base_v015_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 252d mean-centered (intrevenue)
def f73gs_f73_semi_goodwill_share_intrevenue_level_252d_base_v016_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = m - _mean(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (intassets)
def f73gs_f73_semi_goodwill_share_intassets_level_504d_base_v017_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (intequity)
def f73gs_f73_semi_goodwill_share_intequity_level_504d_base_v018_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (inttangibles)
def f73gs_f73_semi_goodwill_share_inttangibles_level_504d_base_v019_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# level 504d mean-centered (intrevenue)
def f73gs_f73_semi_goodwill_share_intrevenue_level_504d_base_v020_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = m - _mean(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_21d_base_v021_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_21d_base_v022_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_21d_base_v023_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_21d_base_v024_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _z(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_63d_base_v025_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_63d_base_v026_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_63d_base_v027_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_63d_base_v028_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _z(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_126d_base_v029_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_126d_base_v030_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_126d_base_v031_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_126d_base_v032_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _z(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_252d_base_v033_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_252d_base_v034_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_252d_base_v035_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_252d_base_v036_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_504d_base_v037_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_504d_base_v038_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_504d_base_v039_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_504d_base_v040_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _z(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_robustz_21d_base_v041_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_robustz_21d_base_v042_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_robustz_21d_base_v043_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_robustz_21d_base_v044_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    med = m.rolling(21, min_periods=max(1, 21 // 2)).median()
    mad = (m - med).abs().rolling(21, min_periods=max(1, 21 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_robustz_63d_base_v045_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_robustz_63d_base_v046_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_robustz_63d_base_v047_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_robustz_63d_base_v048_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    med = m.rolling(63, min_periods=max(1, 63 // 2)).median()
    mad = (m - med).abs().rolling(63, min_periods=max(1, 63 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_robustz_126d_base_v049_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_robustz_126d_base_v050_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_robustz_126d_base_v051_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_robustz_126d_base_v052_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    med = m.rolling(126, min_periods=max(1, 126 // 2)).median()
    mad = (m - med).abs().rolling(126, min_periods=max(1, 126 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_robustz_252d_base_v053_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_robustz_252d_base_v054_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_robustz_252d_base_v055_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_robustz_252d_base_v056_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    med = m.rolling(252, min_periods=max(1, 252 // 2)).median()
    mad = (m - med).abs().rolling(252, min_periods=max(1, 252 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of intassets
def f73gs_f73_semi_goodwill_share_intassets_robustz_504d_base_v057_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of intequity
def f73gs_f73_semi_goodwill_share_intequity_robustz_504d_base_v058_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_robustz_504d_base_v059_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_robustz_504d_base_v060_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    med = m.rolling(504, min_periods=max(1, 504 // 2)).median()
    mad = (m - med).abs().rolling(504, min_periods=max(1, 504 // 2)).median()
    result = (m - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_21d_base_v061_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_21d_base_v062_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_21d_base_v063_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_21d_base_v064_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_63d_base_v065_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_63d_base_v066_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_63d_base_v067_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_63d_base_v068_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_126d_base_v069_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_126d_base_v070_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_126d_base_v071_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_126d_base_v072_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    result = _max(m, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_252d_base_v073_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_252d_base_v074_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_252d_base_v075_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    result = _max(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

