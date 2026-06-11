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


# 21d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slope_21d_2d_v001_signal(inventory, closeadj):
    base = inventory
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slope_63d_2d_v002_signal(inventory, closeadj):
    base = inventory
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slope_126d_2d_v003_signal(inventory, closeadj):
    base = inventory
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slope_252d_2d_v004_signal(inventory, closeadj):
    base = inventory
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_slope_504d_2d_v005_signal(inventory, closeadj):
    base = inventory
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slope_21d_2d_v006_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slope_63d_2d_v007_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slope_126d_2d_v008_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slope_252d_2d_v009_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_slope_504d_2d_v010_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slope_21d_2d_v011_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slope_63d_2d_v012_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slope_126d_2d_v013_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slope_252d_2d_v014_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_slope_504d_2d_v015_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slope_21d_2d_v016_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slope_63d_2d_v017_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slope_126d_2d_v018_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slope_252d_2d_v019_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_slope_504d_2d_v020_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slope_21d_2d_v021_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slope_63d_2d_v022_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slope_126d_2d_v023_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slope_252d_2d_v024_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_slope_504d_2d_v025_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slope_21d_2d_v026_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slope_63d_2d_v027_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slope_126d_2d_v028_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slope_252d_2d_v029_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_slope_504d_2d_v030_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slope_21d_2d_v031_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slope_63d_2d_v032_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slope_126d_2d_v033_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slope_252d_2d_v034_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_slope_504d_2d_v035_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sm21_sl21_2d_v036_signal(inventory, closeadj):
    base = _mean(inventory, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sm63_sl21_2d_v037_signal(inventory, closeadj):
    base = _mean(inventory, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sm63_sl63_2d_v038_signal(inventory, closeadj):
    base = _mean(inventory, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sm252_sl63_2d_v039_signal(inventory, closeadj):
    base = _mean(inventory, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sm252_sl126_2d_v040_signal(inventory, closeadj):
    base = _mean(inventory, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sm21_sl21_2d_v041_signal(inventory, revenue, closeadj):
    base = _mean(_f044_inv_to_rev(inventory, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sm63_sl21_2d_v042_signal(inventory, revenue, closeadj):
    base = _mean(_f044_inv_to_rev(inventory, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sm63_sl63_2d_v043_signal(inventory, revenue, closeadj):
    base = _mean(_f044_inv_to_rev(inventory, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sm252_sl63_2d_v044_signal(inventory, revenue, closeadj):
    base = _mean(_f044_inv_to_rev(inventory, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sm252_sl126_2d_v045_signal(inventory, revenue, closeadj):
    base = _mean(_f044_inv_to_rev(inventory, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sm21_sl21_2d_v046_signal(cor, inventory, closeadj):
    base = _mean(cor / inventory.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sm63_sl21_2d_v047_signal(cor, inventory, closeadj):
    base = _mean(cor / inventory.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sm63_sl63_2d_v048_signal(cor, inventory, closeadj):
    base = _mean(cor / inventory.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sm252_sl63_2d_v049_signal(cor, inventory, closeadj):
    base = _mean(cor / inventory.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sm252_sl126_2d_v050_signal(cor, inventory, closeadj):
    base = _mean(cor / inventory.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sm21_sl21_2d_v051_signal(inventory, closeadj):
    base = _mean(inventory.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sm63_sl21_2d_v052_signal(inventory, closeadj):
    base = _mean(inventory.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sm63_sl63_2d_v053_signal(inventory, closeadj):
    base = _mean(inventory.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sm252_sl63_2d_v054_signal(inventory, closeadj):
    base = _mean(inventory.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sm252_sl126_2d_v055_signal(inventory, closeadj):
    base = _mean(inventory.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sm21_sl21_2d_v056_signal(inventory, assets, closeadj):
    base = _mean(inventory / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sm63_sl21_2d_v057_signal(inventory, assets, closeadj):
    base = _mean(inventory / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sm63_sl63_2d_v058_signal(inventory, assets, closeadj):
    base = _mean(inventory / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sm252_sl63_2d_v059_signal(inventory, assets, closeadj):
    base = _mean(inventory / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sm252_sl126_2d_v060_signal(inventory, assets, closeadj):
    base = _mean(inventory / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sm21_sl21_2d_v061_signal(inventory, sharesbas, closeadj):
    base = _mean(inventory / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sm63_sl21_2d_v062_signal(inventory, sharesbas, closeadj):
    base = _mean(inventory / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sm63_sl63_2d_v063_signal(inventory, sharesbas, closeadj):
    base = _mean(inventory / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sm252_sl63_2d_v064_signal(inventory, sharesbas, closeadj):
    base = _mean(inventory / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sm252_sl126_2d_v065_signal(inventory, sharesbas, closeadj):
    base = _mean(inventory / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sm21_sl21_2d_v066_signal(inventory, assetsc, closeadj):
    base = _mean(inventory / assetsc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sm63_sl21_2d_v067_signal(inventory, assetsc, closeadj):
    base = _mean(inventory / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sm63_sl63_2d_v068_signal(inventory, assetsc, closeadj):
    base = _mean(inventory / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sm252_sl63_2d_v069_signal(inventory, assetsc, closeadj):
    base = _mean(inventory / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sm252_sl126_2d_v070_signal(inventory, assetsc, closeadj):
    base = _mean(inventory / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_pctslope_21d_2d_v071_signal(inventory, closeadj):
    base = inventory
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_pctslope_63d_2d_v072_signal(inventory, closeadj):
    base = inventory
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_pctslope_252d_2d_v073_signal(inventory, closeadj):
    base = inventory
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_pctslope_21d_2d_v074_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_pctslope_63d_2d_v075_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_pctslope_252d_2d_v076_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_pctslope_21d_2d_v077_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_pctslope_63d_2d_v078_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_pctslope_252d_2d_v079_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_pctslope_21d_2d_v080_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_pctslope_63d_2d_v081_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_pctslope_252d_2d_v082_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_pctslope_21d_2d_v083_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_pctslope_63d_2d_v084_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_pctslope_252d_2d_v085_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_pctslope_21d_2d_v086_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_pctslope_63d_2d_v087_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_pctslope_252d_2d_v088_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_pctslope_21d_2d_v089_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_pctslope_63d_2d_v090_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_pctslope_252d_2d_v091_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sgnslope_21d_2d_v092_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sgnslope_63d_2d_v093_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_sgnslope_252d_2d_v094_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sgnslope_21d_2d_v095_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sgnslope_63d_2d_v096_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_sgnslope_252d_2d_v097_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sgnslope_21d_2d_v098_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sgnslope_63d_2d_v099_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_sgnslope_252d_2d_v100_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sgnslope_21d_2d_v101_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sgnslope_63d_2d_v102_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_sgnslope_252d_2d_v103_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sgnslope_21d_2d_v104_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sgnslope_63d_2d_v105_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_sgnslope_252d_2d_v106_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sgnslope_21d_2d_v107_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sgnslope_63d_2d_v108_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_sgnslope_252d_2d_v109_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sgnslope_21d_2d_v110_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sgnslope_63d_2d_v111_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_sgnslope_252d_2d_v112_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_logmagslope_21d_2d_v113_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_logmagslope_63d_2d_v114_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_logmagslope_252d_2d_v115_signal(inventory, closeadj):
    base = inventory
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_logmagslope_21d_2d_v116_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_logmagslope_63d_2d_v117_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_logmagslope_252d_2d_v118_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_logmagslope_21d_2d_v119_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_logmagslope_63d_2d_v120_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_logmagslope_252d_2d_v121_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_logmagslope_21d_2d_v122_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_logmagslope_63d_2d_v123_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_logmagslope_252d_2d_v124_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_logmagslope_21d_2d_v125_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_logmagslope_63d_2d_v126_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_logmagslope_252d_2d_v127_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_logmagslope_21d_2d_v128_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_logmagslope_63d_2d_v129_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_logmagslope_252d_2d_v130_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_logmagslope_21d_2d_v131_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_logmagslope_63d_2d_v132_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_logmagslope_252d_2d_v133_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_lvl|
def f044ind_f044_inventory_dynamics_inv_lvl_logslope_63d_2d_v134_signal(inventory, closeadj):
    base = np.log((inventory).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_lvl|
def f044ind_f044_inventory_dynamics_inv_lvl_logslope_252d_2d_v135_signal(inventory, closeadj):
    base = np.log((inventory).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_to_rev|
def f044ind_f044_inventory_dynamics_inv_to_rev_logslope_63d_2d_v136_signal(inventory, revenue, closeadj):
    base = np.log((_f044_inv_to_rev(inventory, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_to_rev|
def f044ind_f044_inventory_dynamics_inv_to_rev_logslope_252d_2d_v137_signal(inventory, revenue, closeadj):
    base = np.log((_f044_inv_to_rev(inventory, revenue)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_turns|
def f044ind_f044_inventory_dynamics_inv_turns_logslope_63d_2d_v138_signal(cor, inventory, closeadj):
    base = np.log((cor / inventory.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_turns|
def f044ind_f044_inventory_dynamics_inv_turns_logslope_252d_2d_v139_signal(cor, inventory, closeadj):
    base = np.log((cor / inventory.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_growth|
def f044ind_f044_inventory_dynamics_inv_growth_logslope_63d_2d_v140_signal(inventory, closeadj):
    base = np.log((inventory.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_growth|
def f044ind_f044_inventory_dynamics_inv_growth_logslope_252d_2d_v141_signal(inventory, closeadj):
    base = np.log((inventory.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_to_asset|
def f044ind_f044_inventory_dynamics_inv_to_asset_logslope_63d_2d_v142_signal(inventory, assets, closeadj):
    base = np.log((inventory / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_to_asset|
def f044ind_f044_inventory_dynamics_inv_to_asset_logslope_252d_2d_v143_signal(inventory, assets, closeadj):
    base = np.log((inventory / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_per_share|
def f044ind_f044_inventory_dynamics_inv_per_share_logslope_63d_2d_v144_signal(inventory, sharesbas, closeadj):
    base = np.log((inventory / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_per_share|
def f044ind_f044_inventory_dynamics_inv_per_share_logslope_252d_2d_v145_signal(inventory, sharesbas, closeadj):
    base = np.log((inventory / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|inv_to_curasset|
def f044ind_f044_inventory_dynamics_inv_to_curasset_logslope_63d_2d_v146_signal(inventory, assetsc, closeadj):
    base = np.log((inventory / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|inv_to_curasset|
def f044ind_f044_inventory_dynamics_inv_to_curasset_logslope_252d_2d_v147_signal(inventory, assetsc, closeadj):
    base = np.log((inventory / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

