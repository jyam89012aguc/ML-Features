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
def _f044_inv_to_rev(inventory, revenue):
    return inventory / revenue.abs().replace(0, np.nan)


# 21d acceleration of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_accel_21d_3d_v001_signal(inventory, closeadj):
    base = inventory
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_accel_63d_3d_v002_signal(inventory, closeadj):
    base = inventory
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_accel_126d_3d_v003_signal(inventory, closeadj):
    base = inventory
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_accel_252d_3d_v004_signal(inventory, closeadj):
    base = inventory
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_accel_21d_3d_v005_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_accel_63d_3d_v006_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_accel_126d_3d_v007_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_accel_252d_3d_v008_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_accel_21d_3d_v009_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_accel_63d_3d_v010_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_accel_126d_3d_v011_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_accel_252d_3d_v012_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_accel_21d_3d_v013_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_accel_63d_3d_v014_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_accel_126d_3d_v015_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_accel_252d_3d_v016_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_accel_21d_3d_v017_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_accel_63d_3d_v018_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_accel_126d_3d_v019_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_accel_252d_3d_v020_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_accel_21d_3d_v021_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_accel_63d_3d_v022_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_accel_126d_3d_v023_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_accel_252d_3d_v024_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_accel_21d_3d_v025_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_accel_63d_3d_v026_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_accel_126d_3d_v027_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_accel_252d_3d_v028_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slopez_21d_z126_3d_v029_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slopez_63d_z252_3d_v030_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slopez_126d_z252_3d_v031_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slopez_252d_z504_3d_v032_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slopez_21d_z126_3d_v033_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slopez_63d_z252_3d_v034_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slopez_126d_z252_3d_v035_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slopez_252d_z504_3d_v036_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slopez_21d_z126_3d_v037_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slopez_63d_z252_3d_v038_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slopez_126d_z252_3d_v039_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slopez_252d_z504_3d_v040_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slopez_21d_z126_3d_v041_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slopez_63d_z252_3d_v042_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slopez_126d_z252_3d_v043_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slopez_252d_z504_3d_v044_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slopez_21d_z126_3d_v045_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slopez_63d_z252_3d_v046_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slopez_126d_z252_3d_v047_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slopez_252d_z504_3d_v048_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slopez_21d_z126_3d_v049_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slopez_63d_z252_3d_v050_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slopez_126d_z252_3d_v051_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slopez_252d_z504_3d_v052_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slopez_21d_z126_3d_v053_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slopez_63d_z252_3d_v054_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slopez_126d_z252_3d_v055_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slopez_252d_z504_3d_v056_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_jerk_21d_3d_v057_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_jerk_63d_3d_v058_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_jerk_126d_3d_v059_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_jerk_21d_3d_v060_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_jerk_63d_3d_v061_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_jerk_126d_3d_v062_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_jerk_21d_3d_v063_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_jerk_63d_3d_v064_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_jerk_126d_3d_v065_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_jerk_21d_3d_v066_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_jerk_63d_3d_v067_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_jerk_126d_3d_v068_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_jerk_21d_3d_v069_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_jerk_63d_3d_v070_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_jerk_126d_3d_v071_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_jerk_21d_3d_v072_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_jerk_63d_3d_v073_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_jerk_126d_3d_v074_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_jerk_21d_3d_v075_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_jerk_63d_3d_v076_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_jerk_126d_3d_v077_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_lvl smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_lvl_smoothaccel_63d_sm252_3d_v078_signal(inventory, closeadj):
    base = inventory
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_lvl smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_lvl_smoothaccel_252d_sm504_3d_v079_signal(inventory, closeadj):
    base = inventory
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_to_rev smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_to_rev_smoothaccel_63d_sm252_3d_v080_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_to_rev smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_to_rev_smoothaccel_252d_sm504_3d_v081_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_turns smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_turns_smoothaccel_63d_sm252_3d_v082_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_turns smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_turns_smoothaccel_252d_sm504_3d_v083_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_growth smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_growth_smoothaccel_63d_sm252_3d_v084_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_growth smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_growth_smoothaccel_252d_sm504_3d_v085_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_to_asset smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_to_asset_smoothaccel_63d_sm252_3d_v086_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_to_asset smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_to_asset_smoothaccel_252d_sm504_3d_v087_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_per_share smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_per_share_smoothaccel_63d_sm252_3d_v088_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_per_share smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_per_share_smoothaccel_252d_sm504_3d_v089_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of inv_to_curasset smoothed over 252d
def f044ind_f044_inventory_dynamics_inv_to_curasset_smoothaccel_63d_sm252_3d_v090_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of inv_to_curasset smoothed over 504d
def f044ind_f044_inventory_dynamics_inv_to_curasset_smoothaccel_252d_sm504_3d_v091_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_accelz_21d_z252_3d_v092_signal(inventory, closeadj):
    base = inventory
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_accelz_63d_z504_3d_v093_signal(inventory, closeadj):
    base = inventory
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_accelz_21d_z252_3d_v094_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_accelz_63d_z504_3d_v095_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_accelz_21d_z252_3d_v096_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_accelz_63d_z504_3d_v097_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_accelz_21d_z252_3d_v098_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_accelz_63d_z504_3d_v099_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_accelz_21d_z252_3d_v100_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_accelz_63d_z504_3d_v101_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_accelz_21d_z252_3d_v102_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_accelz_63d_z504_3d_v103_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_accelz_21d_z252_3d_v104_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_accelz_63d_z504_3d_v105_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_lvl (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_lvl_signflip_63d_3d_v106_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_lvl (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_lvl_signflip_252d_3d_v107_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_to_rev (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_to_rev_signflip_63d_3d_v108_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_to_rev (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_to_rev_signflip_252d_3d_v109_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_turns (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_turns_signflip_63d_3d_v110_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_turns (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_turns_signflip_252d_3d_v111_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_growth (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_growth_signflip_63d_3d_v112_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_growth (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_growth_signflip_252d_3d_v113_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_to_asset (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_to_asset_signflip_63d_3d_v114_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_to_asset (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_to_asset_signflip_252d_3d_v115_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_per_share (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_per_share_signflip_63d_3d_v116_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_per_share (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_per_share_signflip_252d_3d_v117_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in inv_to_curasset (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_to_curasset_signflip_63d_3d_v118_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in inv_to_curasset (raw count, no price scaling)
def f044ind_f044_inventory_dynamics_inv_to_curasset_signflip_252d_3d_v119_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_lvl normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_lvl_rngaccel_63d_r252_3d_v120_signal(inventory, closeadj):
    base = inventory
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_lvl normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_lvl_rngaccel_252d_r504_3d_v121_signal(inventory, closeadj):
    base = inventory
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_to_rev normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_to_rev_rngaccel_63d_r252_3d_v122_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_to_rev normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_to_rev_rngaccel_252d_r504_3d_v123_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_turns normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_turns_rngaccel_63d_r252_3d_v124_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_turns normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_turns_rngaccel_252d_r504_3d_v125_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_growth normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_growth_rngaccel_63d_r252_3d_v126_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_growth normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_growth_rngaccel_252d_r504_3d_v127_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_to_asset normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_to_asset_rngaccel_63d_r252_3d_v128_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_to_asset normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_to_asset_rngaccel_252d_r504_3d_v129_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_per_share normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_per_share_rngaccel_63d_r252_3d_v130_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_per_share normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_per_share_rngaccel_252d_r504_3d_v131_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inv_to_curasset normalized by 252d range
def f044ind_f044_inventory_dynamics_inv_to_curasset_rngaccel_63d_r252_3d_v132_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inv_to_curasset normalized by 504d range
def f044ind_f044_inventory_dynamics_inv_to_curasset_rngaccel_252d_r504_3d_v133_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_cumslope_21d_3d_v134_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_cumslope_63d_3d_v135_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_cumslope_252d_3d_v136_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_cumslope_21d_3d_v137_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_cumslope_63d_3d_v138_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_cumslope_252d_3d_v139_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_cumslope_21d_3d_v140_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_cumslope_63d_3d_v141_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_cumslope_252d_3d_v142_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_cumslope_21d_3d_v143_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_cumslope_63d_3d_v144_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_cumslope_252d_3d_v145_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_cumslope_21d_3d_v146_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_cumslope_63d_3d_v147_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_cumslope_252d_3d_v148_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_cumslope_21d_3d_v149_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_cumslope_63d_3d_v150_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

