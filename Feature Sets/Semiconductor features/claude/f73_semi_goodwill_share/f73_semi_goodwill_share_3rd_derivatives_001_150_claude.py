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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


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


# 5d curv of 21d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_21d_curv_v001_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_21d_curv_v002_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_21d_curv_v003_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_21d_curv_v004_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_21d_curv_v005_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d level of intequity
def f73gs_f73_semi_goodwill_share_intequity_level_63d_curv_v006_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d level of intequity
def f73gs_f73_semi_goodwill_share_intequity_level_63d_curv_v007_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d level of intequity
def f73gs_f73_semi_goodwill_share_intequity_level_63d_curv_v008_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d level of intequity
def f73gs_f73_semi_goodwill_share_intequity_level_63d_curv_v009_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d level of intequity
def f73gs_f73_semi_goodwill_share_intequity_level_63d_curv_v010_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d level of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_level_126d_curv_v011_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d level of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_level_126d_curv_v012_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d level of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_level_126d_curv_v013_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d level of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_level_126d_curv_v014_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d level of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_level_126d_curv_v015_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = m - _mean(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d level of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_level_252d_curv_v016_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d level of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_level_252d_curv_v017_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d level of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_level_252d_curv_v018_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d level of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_level_252d_curv_v019_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d level of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_level_252d_curv_v020_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = m - _mean(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_504d_curv_v021_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_504d_curv_v022_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_504d_curv_v023_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_504d_curv_v024_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d level of intassets
def f73gs_f73_semi_goodwill_share_intassets_level_504d_curv_v025_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = m - _mean(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_21d_curv_v026_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_21d_curv_v027_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_21d_curv_v028_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_21d_curv_v029_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_21d_curv_v030_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d z of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_63d_curv_v031_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d z of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_63d_curv_v032_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d z of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_63d_curv_v033_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d z of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_63d_curv_v034_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d z of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_z_63d_curv_v035_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d z of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_126d_curv_v036_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d z of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_126d_curv_v037_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d z of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_126d_curv_v038_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d z of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_126d_curv_v039_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d z of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_z_126d_curv_v040_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d z of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_252d_curv_v041_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d z of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_252d_curv_v042_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d z of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_252d_curv_v043_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d z of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_252d_curv_v044_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d z of intassets
def f73gs_f73_semi_goodwill_share_intassets_z_252d_curv_v045_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _z(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_504d_curv_v046_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_504d_curv_v047_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_504d_curv_v048_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_504d_curv_v049_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d z of intequity
def f73gs_f73_semi_goodwill_share_intequity_z_504d_curv_v050_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _z(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_21d_curv_v051_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_21d_curv_v052_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_21d_curv_v053_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_21d_curv_v054_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_21d_curv_v055_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_63d_curv_v056_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_63d_curv_v057_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_63d_curv_v058_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_63d_curv_v059_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d max of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_max_63d_curv_v060_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_126d_curv_v061_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_126d_curv_v062_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_126d_curv_v063_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_126d_curv_v064_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d max of intassets
def f73gs_f73_semi_goodwill_share_intassets_max_126d_curv_v065_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_252d_curv_v066_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_252d_curv_v067_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_252d_curv_v068_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_252d_curv_v069_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d max of intequity
def f73gs_f73_semi_goodwill_share_intequity_max_252d_curv_v070_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_504d_curv_v071_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_504d_curv_v072_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_504d_curv_v073_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_504d_curv_v074_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d max of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_max_504d_curv_v075_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_21d_curv_v076_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_21d_curv_v077_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_21d_curv_v078_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_21d_curv_v079_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_21d_curv_v080_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_63d_curv_v081_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_63d_curv_v082_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_63d_curv_v083_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_63d_curv_v084_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d min of intassets
def f73gs_f73_semi_goodwill_share_intassets_min_63d_curv_v085_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_126d_curv_v086_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_126d_curv_v087_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_126d_curv_v088_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_126d_curv_v089_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d min of intequity
def f73gs_f73_semi_goodwill_share_intequity_min_126d_curv_v090_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _min(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_252d_curv_v091_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_252d_curv_v092_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_252d_curv_v093_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_252d_curv_v094_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d min of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_min_252d_curv_v095_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _min(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_504d_curv_v096_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_504d_curv_v097_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_504d_curv_v098_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_504d_curv_v099_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d min of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_min_504d_curv_v100_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _min(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_21d_curv_v101_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_21d_curv_v102_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_21d_curv_v103_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_21d_curv_v104_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_21d_curv_v105_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 21)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d dd of intequity
def f73gs_f73_semi_goodwill_share_intequity_dd_63d_curv_v106_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d dd of intequity
def f73gs_f73_semi_goodwill_share_intequity_dd_63d_curv_v107_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d dd of intequity
def f73gs_f73_semi_goodwill_share_intequity_dd_63d_curv_v108_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d dd of intequity
def f73gs_f73_semi_goodwill_share_intequity_dd_63d_curv_v109_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d dd of intequity
def f73gs_f73_semi_goodwill_share_intequity_dd_63d_curv_v110_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d dd of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_dd_126d_curv_v111_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d dd of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_dd_126d_curv_v112_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d dd of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_dd_126d_curv_v113_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d dd of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_dd_126d_curv_v114_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d dd of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_dd_126d_curv_v115_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    peak = _max(m, 126)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d dd of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_dd_252d_curv_v116_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d dd of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_dd_252d_curv_v117_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d dd of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_dd_252d_curv_v118_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d dd of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_dd_252d_curv_v119_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d dd of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_dd_252d_curv_v120_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    peak = _max(m, 252)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_504d_curv_v121_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_504d_curv_v122_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_504d_curv_v123_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_504d_curv_v124_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d dd of intassets
def f73gs_f73_semi_goodwill_share_intassets_dd_504d_curv_v125_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    peak = _max(m, 504)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_21d_curv_v126_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_21d_curv_v127_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_21d_curv_v128_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_21d_curv_v129_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_21d_curv_v130_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 21) - _min(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d rng of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_63d_curv_v131_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d rng of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_63d_curv_v132_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d rng of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_63d_curv_v133_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d rng of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_63d_curv_v134_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d rng of inttangibles
def f73gs_f73_semi_goodwill_share_inttangibles_rng_63d_curv_v135_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_tangibles(intangibles, tangibles), closeadj.index)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d rng of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_126d_curv_v136_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d rng of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_126d_curv_v137_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d rng of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_126d_curv_v138_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d rng of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_126d_curv_v139_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d rng of intrevenue
def f73gs_f73_semi_goodwill_share_intrevenue_rng_126d_curv_v140_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_revenue(intangibles, revenue), closeadj.index)
    base = _max(m, 126) - _min(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d rng of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_252d_curv_v141_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d rng of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_252d_curv_v142_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d rng of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_252d_curv_v143_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d rng of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_252d_curv_v144_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d rng of intassets
def f73gs_f73_semi_goodwill_share_intassets_rng_252d_curv_v145_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_assets(intangibles, assets), closeadj.index)
    base = _max(m, 252) - _min(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_504d_curv_v146_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_504d_curv_v147_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_504d_curv_v148_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_504d_curv_v149_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d rng of intequity
def f73gs_f73_semi_goodwill_share_intequity_rng_504d_curv_v150_signal(intangibles, assets, equity, tangibles, revenue, closeadj):
    m = _f73gs_align(_f73gs_int_equity(intangibles, equity), closeadj.index)
    base = _max(m, 504) - _min(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

