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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


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


# 5d slope of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_slope_v001_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_slope_v002_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_slope_v003_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_slope_v004_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_21d_slope_v005_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_slope_v006_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_slope_v007_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_slope_v008_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_slope_v009_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_63d_slope_v010_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_slope_v011_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_slope_v012_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_slope_v013_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_slope_v014_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_126d_slope_v015_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_slope_v016_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_slope_v017_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_slope_v018_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_slope_v019_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_252d_slope_v020_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_slope_v021_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_slope_v022_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_slope_v023_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_slope_v024_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d atrn level
def f75at_f75_semi_asset_turnover_trend_atrn_level_504d_slope_v025_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r
    result = _slope_diff_norm(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_slope_v026_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_slope_v027_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_slope_v028_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_slope_v029_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_21d_slope_v030_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_slope_v031_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_slope_v032_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_slope_v033_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_slope_v034_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_63d_slope_v035_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_slope_v036_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_slope_v037_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_slope_v038_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_slope_v039_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_126d_slope_v040_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_slope_v041_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_slope_v042_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_slope_v043_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_slope_v044_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_252d_slope_v045_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_slope_v046_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_slope_v047_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_slope_v048_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_slope_v049_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d atrn z
def f75at_f75_semi_asset_turnover_trend_atrn_z_504d_slope_v050_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _z(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_slope_v051_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_slope_v052_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_slope_v053_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_slope_v054_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_21d_slope_v055_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_slope_v056_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_slope_v057_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_slope_v058_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_slope_v059_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_63d_slope_v060_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_slope_v061_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_slope_v062_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_slope_v063_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_slope_v064_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_126d_slope_v065_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_slope_v066_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_slope_v067_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_slope_v068_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_slope_v069_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_252d_slope_v070_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_slope_v071_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_slope_v072_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_slope_v073_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_slope_v074_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d atrn max
def f75at_f75_semi_asset_turnover_trend_atrn_max_504d_slope_v075_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_slope_v076_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_slope_v077_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_slope_v078_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_slope_v079_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_21d_slope_v080_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_slope_v081_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_slope_v082_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_slope_v083_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_slope_v084_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_63d_slope_v085_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_slope_v086_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_slope_v087_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_slope_v088_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_slope_v089_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_126d_slope_v090_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_slope_v091_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_slope_v092_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_slope_v093_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_slope_v094_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_252d_slope_v095_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_slope_v096_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_slope_v097_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_slope_v098_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_slope_v099_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d atrn min
def f75at_f75_semi_asset_turnover_trend_atrn_min_504d_slope_v100_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_slope_v101_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_slope_v102_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_slope_v103_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_slope_v104_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_21d_slope_v105_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 21) - _min(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_slope_v106_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_slope_v107_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_slope_v108_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_slope_v109_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_63d_slope_v110_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 63) - _min(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_slope_v111_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_slope_v112_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_slope_v113_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_slope_v114_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_126d_slope_v115_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 126) - _min(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_slope_v116_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_slope_v117_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_slope_v118_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_slope_v119_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_252d_slope_v120_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 252) - _min(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_slope_v121_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_slope_v122_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_slope_v123_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_slope_v124_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d atrn rng
def f75at_f75_semi_asset_turnover_trend_atrn_rng_504d_slope_v125_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = _max(r, 504) - _min(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_slope_v126_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_slope_v127_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_slope_v128_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_slope_v129_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_21d_slope_v130_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_slope_v131_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_slope_v132_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_slope_v133_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_slope_v134_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_63d_slope_v135_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_slope_v136_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_slope_v137_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_slope_v138_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_slope_v139_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_126d_slope_v140_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_slope_v141_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_slope_v142_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_slope_v143_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_slope_v144_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_252d_slope_v145_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_slope_v146_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_slope_v147_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_slope_v148_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_slope_v149_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d atrn dd
def f75at_f75_semi_asset_turnover_trend_atrn_dd_504d_slope_v150_signal(revenue, assets, closeadj):
    r = _f75_at(revenue, assets)
    base = r - _max(r, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
