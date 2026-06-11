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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f75_at(revenue, assets):
    return revenue / assets.replace(0, np.nan)


# 5d curv of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_curv_v001_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_curv_v002_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_curv_v003_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_curv_v004_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_curv_v005_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_curv_v006_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_curv_v007_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_curv_v008_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_curv_v009_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_curv_v010_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_curv_v011_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_curv_v012_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_curv_v013_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_curv_v014_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_curv_v015_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_curv_v016_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_curv_v017_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_curv_v018_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_curv_v019_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_curv_v020_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_curv_v021_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_curv_v022_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_curv_v023_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_curv_v024_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_curv_v025_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _curvature(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_curv_v026_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_curv_v027_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_curv_v028_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_curv_v029_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_curv_v030_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_curv_v031_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_curv_v032_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_curv_v033_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_curv_v034_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_curv_v035_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_curv_v036_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_curv_v037_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_curv_v038_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_curv_v039_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_curv_v040_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_curv_v041_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_curv_v042_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_curv_v043_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_curv_v044_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_curv_v045_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_curv_v046_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_curv_v047_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_curv_v048_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_curv_v049_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_curv_v050_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_curv_v051_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_curv_v052_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_curv_v053_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_curv_v054_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_curv_v055_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_curv_v056_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_curv_v057_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_curv_v058_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_curv_v059_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_curv_v060_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_curv_v061_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_curv_v062_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_curv_v063_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_curv_v064_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_curv_v065_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_curv_v066_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_curv_v067_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_curv_v068_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_curv_v069_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_curv_v070_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_curv_v071_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_curv_v072_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_curv_v073_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_curv_v074_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_curv_v075_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_curv_v076_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_curv_v077_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_curv_v078_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_curv_v079_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_curv_v080_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_curv_v081_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_curv_v082_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_curv_v083_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_curv_v084_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_curv_v085_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_curv_v086_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_curv_v087_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_curv_v088_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_curv_v089_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_curv_v090_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_curv_v091_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_curv_v092_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_curv_v093_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_curv_v094_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_curv_v095_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_curv_v096_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_curv_v097_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_curv_v098_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_curv_v099_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_curv_v100_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_curv_v101_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_curv_v102_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_curv_v103_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_curv_v104_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_curv_v105_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_curv_v106_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_curv_v107_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_curv_v108_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_curv_v109_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_curv_v110_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_curv_v111_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_curv_v112_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_curv_v113_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_curv_v114_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_curv_v115_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_curv_v116_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_curv_v117_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_curv_v118_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_curv_v119_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_curv_v120_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_curv_v121_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_curv_v122_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_curv_v123_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_curv_v124_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_curv_v125_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_curv_v126_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_curv_v127_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_curv_v128_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_curv_v129_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_curv_v130_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_curv_v131_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_curv_v132_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_curv_v133_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_curv_v134_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_curv_v135_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_curv_v136_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_curv_v137_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_curv_v138_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_curv_v139_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_curv_v140_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_curv_v141_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_curv_v142_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_curv_v143_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_curv_v144_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_curv_v145_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curv of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_curv_v146_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curv of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_curv_v147_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curv of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_curv_v148_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curv of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_curv_v149_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curv of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_curv_v150_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
