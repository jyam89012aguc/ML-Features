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


# 21d acceleration of assets_lvl
def f040asb_f040_asset_base_assets_lvl_accel_21d_3d_v001_signal(assets, closeadj):
    base = assets
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assets_lvl
def f040asb_f040_asset_base_assets_lvl_accel_63d_3d_v002_signal(assets, closeadj):
    base = assets
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of assets_lvl
def f040asb_f040_asset_base_assets_lvl_accel_126d_3d_v003_signal(assets, closeadj):
    base = assets
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assets_lvl
def f040asb_f040_asset_base_assets_lvl_accel_252d_3d_v004_signal(assets, closeadj):
    base = assets
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of log_assets
def f040asb_f040_asset_base_log_assets_accel_21d_3d_v005_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_assets
def f040asb_f040_asset_base_log_assets_accel_63d_3d_v006_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of log_assets
def f040asb_f040_asset_base_log_assets_accel_126d_3d_v007_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_assets
def f040asb_f040_asset_base_log_assets_accel_252d_3d_v008_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of assets_yoy
def f040asb_f040_asset_base_assets_yoy_accel_21d_3d_v009_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assets_yoy
def f040asb_f040_asset_base_assets_yoy_accel_63d_3d_v010_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of assets_yoy
def f040asb_f040_asset_base_assets_yoy_accel_126d_3d_v011_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assets_yoy
def f040asb_f040_asset_base_assets_yoy_accel_252d_3d_v012_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of assetc_share
def f040asb_f040_asset_base_assetc_share_accel_21d_3d_v013_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assetc_share
def f040asb_f040_asset_base_assetc_share_accel_63d_3d_v014_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of assetc_share
def f040asb_f040_asset_base_assetc_share_accel_126d_3d_v015_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assetc_share
def f040asb_f040_asset_base_assetc_share_accel_252d_3d_v016_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_accel_21d_3d_v017_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_accel_63d_3d_v018_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_accel_126d_3d_v019_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_accel_252d_3d_v020_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of asset_turn
def f040asb_f040_asset_base_asset_turn_accel_21d_3d_v021_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_turn
def f040asb_f040_asset_base_asset_turn_accel_63d_3d_v022_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of asset_turn
def f040asb_f040_asset_base_asset_turn_accel_126d_3d_v023_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_turn
def f040asb_f040_asset_base_asset_turn_accel_252d_3d_v024_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of asset_per_share
def f040asb_f040_asset_base_asset_per_share_accel_21d_3d_v025_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_per_share
def f040asb_f040_asset_base_asset_per_share_accel_63d_3d_v026_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of asset_per_share
def f040asb_f040_asset_base_asset_per_share_accel_126d_3d_v027_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_per_share
def f040asb_f040_asset_base_asset_per_share_accel_252d_3d_v028_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slopez_21d_z126_3d_v029_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slopez_63d_z252_3d_v030_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slopez_126d_z252_3d_v031_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of assets_lvl
def f040asb_f040_asset_base_assets_lvl_slopez_252d_z504_3d_v032_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of log_assets
def f040asb_f040_asset_base_log_assets_slopez_21d_z126_3d_v033_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of log_assets
def f040asb_f040_asset_base_log_assets_slopez_63d_z252_3d_v034_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of log_assets
def f040asb_f040_asset_base_log_assets_slopez_126d_z252_3d_v035_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of log_assets
def f040asb_f040_asset_base_log_assets_slopez_252d_z504_3d_v036_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slopez_21d_z126_3d_v037_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slopez_63d_z252_3d_v038_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slopez_126d_z252_3d_v039_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of assets_yoy
def f040asb_f040_asset_base_assets_yoy_slopez_252d_z504_3d_v040_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of assetc_share
def f040asb_f040_asset_base_assetc_share_slopez_21d_z126_3d_v041_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of assetc_share
def f040asb_f040_asset_base_assetc_share_slopez_63d_z252_3d_v042_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of assetc_share
def f040asb_f040_asset_base_assetc_share_slopez_126d_z252_3d_v043_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of assetc_share
def f040asb_f040_asset_base_assetc_share_slopez_252d_z504_3d_v044_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slopez_21d_z126_3d_v045_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slopez_63d_z252_3d_v046_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slopez_126d_z252_3d_v047_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_slopez_252d_z504_3d_v048_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of asset_turn
def f040asb_f040_asset_base_asset_turn_slopez_21d_z126_3d_v049_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of asset_turn
def f040asb_f040_asset_base_asset_turn_slopez_63d_z252_3d_v050_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of asset_turn
def f040asb_f040_asset_base_asset_turn_slopez_126d_z252_3d_v051_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of asset_turn
def f040asb_f040_asset_base_asset_turn_slopez_252d_z504_3d_v052_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slopez_21d_z126_3d_v053_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slopez_63d_z252_3d_v054_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slopez_126d_z252_3d_v055_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of asset_per_share
def f040asb_f040_asset_base_asset_per_share_slopez_252d_z504_3d_v056_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of assets_lvl
def f040asb_f040_asset_base_assets_lvl_jerk_21d_3d_v057_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of assets_lvl
def f040asb_f040_asset_base_assets_lvl_jerk_63d_3d_v058_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of assets_lvl
def f040asb_f040_asset_base_assets_lvl_jerk_126d_3d_v059_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of log_assets
def f040asb_f040_asset_base_log_assets_jerk_21d_3d_v060_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of log_assets
def f040asb_f040_asset_base_log_assets_jerk_63d_3d_v061_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of log_assets
def f040asb_f040_asset_base_log_assets_jerk_126d_3d_v062_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of assets_yoy
def f040asb_f040_asset_base_assets_yoy_jerk_21d_3d_v063_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of assets_yoy
def f040asb_f040_asset_base_assets_yoy_jerk_63d_3d_v064_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of assets_yoy
def f040asb_f040_asset_base_assets_yoy_jerk_126d_3d_v065_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of assetc_share
def f040asb_f040_asset_base_assetc_share_jerk_21d_3d_v066_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of assetc_share
def f040asb_f040_asset_base_assetc_share_jerk_63d_3d_v067_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of assetc_share
def f040asb_f040_asset_base_assetc_share_jerk_126d_3d_v068_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_jerk_21d_3d_v069_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_jerk_63d_3d_v070_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_jerk_126d_3d_v071_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of asset_turn
def f040asb_f040_asset_base_asset_turn_jerk_21d_3d_v072_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of asset_turn
def f040asb_f040_asset_base_asset_turn_jerk_63d_3d_v073_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of asset_turn
def f040asb_f040_asset_base_asset_turn_jerk_126d_3d_v074_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of asset_per_share
def f040asb_f040_asset_base_asset_per_share_jerk_21d_3d_v075_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of asset_per_share
def f040asb_f040_asset_base_asset_per_share_jerk_63d_3d_v076_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of asset_per_share
def f040asb_f040_asset_base_asset_per_share_jerk_126d_3d_v077_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of assets_lvl smoothed over 252d
def f040asb_f040_asset_base_assets_lvl_smoothaccel_63d_sm252_3d_v078_signal(assets, closeadj):
    base = assets
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of assets_lvl smoothed over 504d
def f040asb_f040_asset_base_assets_lvl_smoothaccel_252d_sm504_3d_v079_signal(assets, closeadj):
    base = assets
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of log_assets smoothed over 252d
def f040asb_f040_asset_base_log_assets_smoothaccel_63d_sm252_3d_v080_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of log_assets smoothed over 504d
def f040asb_f040_asset_base_log_assets_smoothaccel_252d_sm504_3d_v081_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of assets_yoy smoothed over 252d
def f040asb_f040_asset_base_assets_yoy_smoothaccel_63d_sm252_3d_v082_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of assets_yoy smoothed over 504d
def f040asb_f040_asset_base_assets_yoy_smoothaccel_252d_sm504_3d_v083_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of assetc_share smoothed over 252d
def f040asb_f040_asset_base_assetc_share_smoothaccel_63d_sm252_3d_v084_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of assetc_share smoothed over 504d
def f040asb_f040_asset_base_assetc_share_smoothaccel_252d_sm504_3d_v085_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of assetsnc_share smoothed over 252d
def f040asb_f040_asset_base_assetsnc_share_smoothaccel_63d_sm252_3d_v086_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of assetsnc_share smoothed over 504d
def f040asb_f040_asset_base_assetsnc_share_smoothaccel_252d_sm504_3d_v087_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of asset_turn smoothed over 252d
def f040asb_f040_asset_base_asset_turn_smoothaccel_63d_sm252_3d_v088_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of asset_turn smoothed over 504d
def f040asb_f040_asset_base_asset_turn_smoothaccel_252d_sm504_3d_v089_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of asset_per_share smoothed over 252d
def f040asb_f040_asset_base_asset_per_share_smoothaccel_63d_sm252_3d_v090_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of asset_per_share smoothed over 504d
def f040asb_f040_asset_base_asset_per_share_smoothaccel_252d_sm504_3d_v091_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of assets_lvl
def f040asb_f040_asset_base_assets_lvl_accelz_21d_z252_3d_v092_signal(assets, closeadj):
    base = assets
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of assets_lvl
def f040asb_f040_asset_base_assets_lvl_accelz_63d_z504_3d_v093_signal(assets, closeadj):
    base = assets
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of log_assets
def f040asb_f040_asset_base_log_assets_accelz_21d_z252_3d_v094_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of log_assets
def f040asb_f040_asset_base_log_assets_accelz_63d_z504_3d_v095_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of assets_yoy
def f040asb_f040_asset_base_assets_yoy_accelz_21d_z252_3d_v096_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of assets_yoy
def f040asb_f040_asset_base_assets_yoy_accelz_63d_z504_3d_v097_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of assetc_share
def f040asb_f040_asset_base_assetc_share_accelz_21d_z252_3d_v098_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of assetc_share
def f040asb_f040_asset_base_assetc_share_accelz_63d_z504_3d_v099_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_accelz_21d_z252_3d_v100_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_accelz_63d_z504_3d_v101_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of asset_turn
def f040asb_f040_asset_base_asset_turn_accelz_21d_z252_3d_v102_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of asset_turn
def f040asb_f040_asset_base_asset_turn_accelz_63d_z504_3d_v103_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of asset_per_share
def f040asb_f040_asset_base_asset_per_share_accelz_21d_z252_3d_v104_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of asset_per_share
def f040asb_f040_asset_base_asset_per_share_accelz_63d_z504_3d_v105_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in assets_lvl (raw count, no price scaling)
def f040asb_f040_asset_base_assets_lvl_signflip_63d_3d_v106_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in assets_lvl (raw count, no price scaling)
def f040asb_f040_asset_base_assets_lvl_signflip_252d_3d_v107_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in log_assets (raw count, no price scaling)
def f040asb_f040_asset_base_log_assets_signflip_63d_3d_v108_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in log_assets (raw count, no price scaling)
def f040asb_f040_asset_base_log_assets_signflip_252d_3d_v109_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in assets_yoy (raw count, no price scaling)
def f040asb_f040_asset_base_assets_yoy_signflip_63d_3d_v110_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in assets_yoy (raw count, no price scaling)
def f040asb_f040_asset_base_assets_yoy_signflip_252d_3d_v111_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in assetc_share (raw count, no price scaling)
def f040asb_f040_asset_base_assetc_share_signflip_63d_3d_v112_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in assetc_share (raw count, no price scaling)
def f040asb_f040_asset_base_assetc_share_signflip_252d_3d_v113_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in assetsnc_share (raw count, no price scaling)
def f040asb_f040_asset_base_assetsnc_share_signflip_63d_3d_v114_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in assetsnc_share (raw count, no price scaling)
def f040asb_f040_asset_base_assetsnc_share_signflip_252d_3d_v115_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in asset_turn (raw count, no price scaling)
def f040asb_f040_asset_base_asset_turn_signflip_63d_3d_v116_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in asset_turn (raw count, no price scaling)
def f040asb_f040_asset_base_asset_turn_signflip_252d_3d_v117_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in asset_per_share (raw count, no price scaling)
def f040asb_f040_asset_base_asset_per_share_signflip_63d_3d_v118_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in asset_per_share (raw count, no price scaling)
def f040asb_f040_asset_base_asset_per_share_signflip_252d_3d_v119_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assets_lvl normalized by 252d range
def f040asb_f040_asset_base_assets_lvl_rngaccel_63d_r252_3d_v120_signal(assets, closeadj):
    base = assets
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assets_lvl normalized by 504d range
def f040asb_f040_asset_base_assets_lvl_rngaccel_252d_r504_3d_v121_signal(assets, closeadj):
    base = assets
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_assets normalized by 252d range
def f040asb_f040_asset_base_log_assets_rngaccel_63d_r252_3d_v122_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_assets normalized by 504d range
def f040asb_f040_asset_base_log_assets_rngaccel_252d_r504_3d_v123_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assets_yoy normalized by 252d range
def f040asb_f040_asset_base_assets_yoy_rngaccel_63d_r252_3d_v124_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assets_yoy normalized by 504d range
def f040asb_f040_asset_base_assets_yoy_rngaccel_252d_r504_3d_v125_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assetc_share normalized by 252d range
def f040asb_f040_asset_base_assetc_share_rngaccel_63d_r252_3d_v126_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assetc_share normalized by 504d range
def f040asb_f040_asset_base_assetc_share_rngaccel_252d_r504_3d_v127_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of assetsnc_share normalized by 252d range
def f040asb_f040_asset_base_assetsnc_share_rngaccel_63d_r252_3d_v128_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of assetsnc_share normalized by 504d range
def f040asb_f040_asset_base_assetsnc_share_rngaccel_252d_r504_3d_v129_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_turn normalized by 252d range
def f040asb_f040_asset_base_asset_turn_rngaccel_63d_r252_3d_v130_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_turn normalized by 504d range
def f040asb_f040_asset_base_asset_turn_rngaccel_252d_r504_3d_v131_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_per_share normalized by 252d range
def f040asb_f040_asset_base_asset_per_share_rngaccel_63d_r252_3d_v132_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_per_share normalized by 504d range
def f040asb_f040_asset_base_asset_per_share_rngaccel_252d_r504_3d_v133_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_cumslope_21d_3d_v134_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_cumslope_63d_3d_v135_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of assets_lvl
def f040asb_f040_asset_base_assets_lvl_cumslope_252d_3d_v136_signal(assets, closeadj):
    base = assets
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of log_assets
def f040asb_f040_asset_base_log_assets_cumslope_21d_3d_v137_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of log_assets
def f040asb_f040_asset_base_log_assets_cumslope_63d_3d_v138_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of log_assets
def f040asb_f040_asset_base_log_assets_cumslope_252d_3d_v139_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_cumslope_21d_3d_v140_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_cumslope_63d_3d_v141_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of assets_yoy
def f040asb_f040_asset_base_assets_yoy_cumslope_252d_3d_v142_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of assetc_share
def f040asb_f040_asset_base_assetc_share_cumslope_21d_3d_v143_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of assetc_share
def f040asb_f040_asset_base_assetc_share_cumslope_63d_3d_v144_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of assetc_share
def f040asb_f040_asset_base_assetc_share_cumslope_252d_3d_v145_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_cumslope_21d_3d_v146_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_cumslope_63d_3d_v147_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_cumslope_252d_3d_v148_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of asset_turn
def f040asb_f040_asset_base_asset_turn_cumslope_21d_3d_v149_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of asset_turn
def f040asb_f040_asset_base_asset_turn_cumslope_63d_3d_v150_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

