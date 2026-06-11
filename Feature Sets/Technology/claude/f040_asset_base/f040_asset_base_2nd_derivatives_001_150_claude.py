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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f040_log_assets(assets):
    return np.log(assets.abs().replace(0, np.nan))


# 21d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slope_21d_2d_v001_signal(assets, closeadj):
    base = assets
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slope_63d_2d_v002_signal(assets, closeadj):
    base = assets
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slope_126d_2d_v003_signal(assets, closeadj):
    base = assets
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slope_252d_2d_v004_signal(assets, closeadj):
    base = assets
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slope_504d_2d_v005_signal(assets, closeadj):
    base = assets
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of log_assets
def f040asb_f040_asset_base_log_assets_slope_21d_2d_v006_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log_assets
def f040asb_f040_asset_base_log_assets_slope_63d_2d_v007_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of log_assets
def f040asb_f040_asset_base_log_assets_slope_126d_2d_v008_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log_assets
def f040asb_f040_asset_base_log_assets_slope_252d_2d_v009_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of log_assets
def f040asb_f040_asset_base_log_assets_slope_504d_2d_v010_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slope_21d_2d_v011_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slope_63d_2d_v012_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slope_126d_2d_v013_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slope_252d_2d_v014_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slope_504d_2d_v015_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_slope_21d_2d_v016_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_slope_63d_2d_v017_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_slope_126d_2d_v018_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_slope_252d_2d_v019_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_slope_504d_2d_v020_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slope_21d_2d_v021_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slope_63d_2d_v022_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slope_126d_2d_v023_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slope_252d_2d_v024_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slope_504d_2d_v025_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_slope_21d_2d_v026_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_slope_63d_2d_v027_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_slope_126d_2d_v028_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_slope_252d_2d_v029_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_slope_504d_2d_v030_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slope_21d_2d_v031_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slope_63d_2d_v032_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slope_126d_2d_v033_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slope_252d_2d_v034_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slope_504d_2d_v035_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sm21_sl21_2d_v036_signal(assets, closeadj):
    base = _mean(assets, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sm63_sl21_2d_v037_signal(assets, closeadj):
    base = _mean(assets, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sm63_sl63_2d_v038_signal(assets, closeadj):
    base = _mean(assets, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sm252_sl63_2d_v039_signal(assets, closeadj):
    base = _mean(assets, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sm252_sl126_2d_v040_signal(assets, closeadj):
    base = _mean(assets, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of log_assets
def f040asb_f040_asset_base_log_assets_sm21_sl21_2d_v041_signal(assets, closeadj):
    base = _mean(_f040_log_assets(assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of log_assets
def f040asb_f040_asset_base_log_assets_sm63_sl21_2d_v042_signal(assets, closeadj):
    base = _mean(_f040_log_assets(assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of log_assets
def f040asb_f040_asset_base_log_assets_sm63_sl63_2d_v043_signal(assets, closeadj):
    base = _mean(_f040_log_assets(assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of log_assets
def f040asb_f040_asset_base_log_assets_sm252_sl63_2d_v044_signal(assets, closeadj):
    base = _mean(_f040_log_assets(assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of log_assets
def f040asb_f040_asset_base_log_assets_sm252_sl126_2d_v045_signal(assets, closeadj):
    base = _mean(_f040_log_assets(assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sm21_sl21_2d_v046_signal(assets, closeadj):
    base = _mean(assets.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sm63_sl21_2d_v047_signal(assets, closeadj):
    base = _mean(assets.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sm63_sl63_2d_v048_signal(assets, closeadj):
    base = _mean(assets.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sm252_sl63_2d_v049_signal(assets, closeadj):
    base = _mean(assets.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sm252_sl126_2d_v050_signal(assets, closeadj):
    base = _mean(assets.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sm21_sl21_2d_v051_signal(assetsc, assets, closeadj):
    base = _mean(assetsc / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sm63_sl21_2d_v052_signal(assetsc, assets, closeadj):
    base = _mean(assetsc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sm63_sl63_2d_v053_signal(assetsc, assets, closeadj):
    base = _mean(assetsc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sm252_sl63_2d_v054_signal(assetsc, assets, closeadj):
    base = _mean(assetsc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sm252_sl126_2d_v055_signal(assetsc, assets, closeadj):
    base = _mean(assetsc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sm21_sl21_2d_v056_signal(assetsnc, assets, closeadj):
    base = _mean(assetsnc / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sm63_sl21_2d_v057_signal(assetsnc, assets, closeadj):
    base = _mean(assetsnc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sm63_sl63_2d_v058_signal(assetsnc, assets, closeadj):
    base = _mean(assetsnc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sm252_sl63_2d_v059_signal(assetsnc, assets, closeadj):
    base = _mean(assetsnc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sm252_sl126_2d_v060_signal(assetsnc, assets, closeadj):
    base = _mean(assetsnc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sm21_sl21_2d_v061_signal(revenue, assetsavg, closeadj):
    base = _mean(revenue / assetsavg.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sm63_sl21_2d_v062_signal(revenue, assetsavg, closeadj):
    base = _mean(revenue / assetsavg.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sm63_sl63_2d_v063_signal(revenue, assetsavg, closeadj):
    base = _mean(revenue / assetsavg.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sm252_sl63_2d_v064_signal(revenue, assetsavg, closeadj):
    base = _mean(revenue / assetsavg.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sm252_sl126_2d_v065_signal(revenue, assetsavg, closeadj):
    base = _mean(revenue / assetsavg.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sm21_sl21_2d_v066_signal(assets, sharesbas, closeadj):
    base = _mean(assets / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sm63_sl21_2d_v067_signal(assets, sharesbas, closeadj):
    base = _mean(assets / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sm63_sl63_2d_v068_signal(assets, sharesbas, closeadj):
    base = _mean(assets / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sm252_sl63_2d_v069_signal(assets, sharesbas, closeadj):
    base = _mean(assets / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sm252_sl126_2d_v070_signal(assets, sharesbas, closeadj):
    base = _mean(assets / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_pctslope_21d_2d_v071_signal(assets, closeadj):
    base = assets
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_pctslope_63d_2d_v072_signal(assets, closeadj):
    base = assets
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_pctslope_252d_2d_v073_signal(assets, closeadj):
    base = assets
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of log_assets
def f040asb_f040_asset_base_log_assets_pctslope_21d_2d_v074_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of log_assets
def f040asb_f040_asset_base_log_assets_pctslope_63d_2d_v075_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of log_assets
def f040asb_f040_asset_base_log_assets_pctslope_252d_2d_v076_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_pctslope_21d_2d_v077_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_pctslope_63d_2d_v078_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_pctslope_252d_2d_v079_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of assetc_share
def f040asb_f040_asset_base_assetc_share_pctslope_21d_2d_v080_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of assetc_share
def f040asb_f040_asset_base_assetc_share_pctslope_63d_2d_v081_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of assetc_share
def f040asb_f040_asset_base_assetc_share_pctslope_252d_2d_v082_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_pctslope_21d_2d_v083_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_pctslope_63d_2d_v084_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_pctslope_252d_2d_v085_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of asset_turn
def f040asb_f040_asset_base_asset_turn_pctslope_21d_2d_v086_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of asset_turn
def f040asb_f040_asset_base_asset_turn_pctslope_63d_2d_v087_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of asset_turn
def f040asb_f040_asset_base_asset_turn_pctslope_252d_2d_v088_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_pctslope_21d_2d_v089_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_pctslope_63d_2d_v090_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_pctslope_252d_2d_v091_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sgnslope_21d_2d_v092_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sgnslope_63d_2d_v093_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_sgnslope_252d_2d_v094_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of log_assets
def f040asb_f040_asset_base_log_assets_sgnslope_21d_2d_v095_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of log_assets
def f040asb_f040_asset_base_log_assets_sgnslope_63d_2d_v096_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of log_assets
def f040asb_f040_asset_base_log_assets_sgnslope_252d_2d_v097_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sgnslope_21d_2d_v098_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sgnslope_63d_2d_v099_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_sgnslope_252d_2d_v100_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sgnslope_21d_2d_v101_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sgnslope_63d_2d_v102_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_sgnslope_252d_2d_v103_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sgnslope_21d_2d_v104_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sgnslope_63d_2d_v105_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_sgnslope_252d_2d_v106_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sgnslope_21d_2d_v107_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sgnslope_63d_2d_v108_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_sgnslope_252d_2d_v109_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sgnslope_21d_2d_v110_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sgnslope_63d_2d_v111_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_sgnslope_252d_2d_v112_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_logmagslope_21d_2d_v113_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_logmagslope_63d_2d_v114_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_logmagslope_252d_2d_v115_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of log_assets
def f040asb_f040_asset_base_log_assets_logmagslope_21d_2d_v116_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of log_assets
def f040asb_f040_asset_base_log_assets_logmagslope_63d_2d_v117_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of log_assets
def f040asb_f040_asset_base_log_assets_logmagslope_252d_2d_v118_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_logmagslope_21d_2d_v119_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_logmagslope_63d_2d_v120_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_logmagslope_252d_2d_v121_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_logmagslope_21d_2d_v122_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_logmagslope_63d_2d_v123_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of assetc_share
def f040asb_f040_asset_base_assetc_share_logmagslope_252d_2d_v124_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_logmagslope_21d_2d_v125_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_logmagslope_63d_2d_v126_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_logmagslope_252d_2d_v127_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_logmagslope_21d_2d_v128_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_logmagslope_63d_2d_v129_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of asset_turn
def f040asb_f040_asset_base_asset_turn_logmagslope_252d_2d_v130_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_logmagslope_21d_2d_v131_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_logmagslope_63d_2d_v132_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of asset_per_share
def f040asb_f040_asset_base_asset_per_share_logmagslope_252d_2d_v133_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|assets_lvl|
def f040asb_f040_asset_base_assets_lvl_logslope_63d_2d_v134_signal(assets, closeadj):
    base = np.log((assets).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|assets_lvl|
def f040asb_f040_asset_base_assets_lvl_logslope_252d_2d_v135_signal(assets, closeadj):
    base = np.log((assets).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|log_assets|
def f040asb_f040_asset_base_log_assets_logslope_63d_2d_v136_signal(assets, closeadj):
    base = np.log((_f040_log_assets(assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|log_assets|
def f040asb_f040_asset_base_log_assets_logslope_252d_2d_v137_signal(assets, closeadj):
    base = np.log((_f040_log_assets(assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|assets_yoy|
def f040asb_f040_asset_base_assets_yoy_logslope_63d_2d_v138_signal(assets, closeadj):
    base = np.log((assets.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|assets_yoy|
def f040asb_f040_asset_base_assets_yoy_logslope_252d_2d_v139_signal(assets, closeadj):
    base = np.log((assets.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|assetc_share|
def f040asb_f040_asset_base_assetc_share_logslope_63d_2d_v140_signal(assetsc, assets, closeadj):
    base = np.log((assetsc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|assetc_share|
def f040asb_f040_asset_base_assetc_share_logslope_252d_2d_v141_signal(assetsc, assets, closeadj):
    base = np.log((assetsc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|assetsnc_share|
def f040asb_f040_asset_base_assetsnc_share_logslope_63d_2d_v142_signal(assetsnc, assets, closeadj):
    base = np.log((assetsnc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|assetsnc_share|
def f040asb_f040_asset_base_assetsnc_share_logslope_252d_2d_v143_signal(assetsnc, assets, closeadj):
    base = np.log((assetsnc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|asset_turn|
def f040asb_f040_asset_base_asset_turn_logslope_63d_2d_v144_signal(revenue, assetsavg, closeadj):
    base = np.log((revenue / assetsavg.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|asset_turn|
def f040asb_f040_asset_base_asset_turn_logslope_252d_2d_v145_signal(revenue, assetsavg, closeadj):
    base = np.log((revenue / assetsavg.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|asset_per_share|
def f040asb_f040_asset_base_asset_per_share_logslope_63d_2d_v146_signal(assets, sharesbas, closeadj):
    base = np.log((assets / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|asset_per_share|
def f040asb_f040_asset_base_asset_per_share_logslope_252d_2d_v147_signal(assets, sharesbas, closeadj):
    base = np.log((assets / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

