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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f044_inv_to_rev(inventory, revenue):
    return inventory / revenue.abs().replace(0, np.nan)


# 21d mean of inv_lvl scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_lvl_mean_21d_base_v001_signal(inventory, closeadj):
    base = inventory
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_lvl scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_lvl_mean_63d_base_v002_signal(inventory, closeadj):
    base = inventory
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_lvl scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_lvl_mean_126d_base_v003_signal(inventory, closeadj):
    base = inventory
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_lvl scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_lvl_mean_252d_base_v004_signal(inventory, closeadj):
    base = inventory
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_lvl scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_lvl_mean_504d_base_v005_signal(inventory, closeadj):
    base = inventory
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inv_to_rev scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_rev_mean_21d_base_v006_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_to_rev scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_rev_mean_63d_base_v007_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_to_rev scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_rev_mean_126d_base_v008_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_to_rev scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_rev_mean_252d_base_v009_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_to_rev scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_rev_mean_504d_base_v010_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inv_turns scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_turns_mean_21d_base_v011_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_turns scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_turns_mean_63d_base_v012_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_turns scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_turns_mean_126d_base_v013_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_turns scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_turns_mean_252d_base_v014_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_turns scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_turns_mean_504d_base_v015_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inv_growth scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_growth_mean_21d_base_v016_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_growth scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_growth_mean_63d_base_v017_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_growth scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_growth_mean_126d_base_v018_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_growth scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_growth_mean_252d_base_v019_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_growth scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_growth_mean_504d_base_v020_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inv_to_asset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_asset_mean_21d_base_v021_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_to_asset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_asset_mean_63d_base_v022_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_to_asset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_asset_mean_126d_base_v023_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_to_asset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_asset_mean_252d_base_v024_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_to_asset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_asset_mean_504d_base_v025_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inv_per_share scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_per_share_mean_21d_base_v026_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_per_share scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_per_share_mean_63d_base_v027_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_per_share scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_per_share_mean_126d_base_v028_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_per_share scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_per_share_mean_252d_base_v029_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_per_share scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_per_share_mean_504d_base_v030_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inv_to_curasset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_curasset_mean_21d_base_v031_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inv_to_curasset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_curasset_mean_63d_base_v032_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inv_to_curasset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_curasset_mean_126d_base_v033_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inv_to_curasset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_curasset_mean_252d_base_v034_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inv_to_curasset scaled by closeadj
def f044ind_f044_inventory_dynamics_inv_to_curasset_mean_504d_base_v035_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_median_63d_base_v036_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_median_252d_base_v037_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_median_504d_base_v038_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_median_63d_base_v039_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_median_252d_base_v040_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_median_504d_base_v041_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_median_63d_base_v042_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_median_252d_base_v043_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_median_504d_base_v044_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_median_63d_base_v045_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_median_252d_base_v046_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_median_504d_base_v047_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_median_63d_base_v048_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_median_252d_base_v049_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_median_504d_base_v050_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_median_63d_base_v051_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_median_252d_base_v052_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_median_504d_base_v053_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_median_63d_base_v054_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_median_252d_base_v055_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_median_504d_base_v056_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_rmax_252d_base_v057_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_rmax_504d_base_v058_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_rmax_252d_base_v059_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_rmax_504d_base_v060_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_rmax_252d_base_v061_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_rmax_504d_base_v062_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_rmax_252d_base_v063_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_rmax_504d_base_v064_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_rmax_252d_base_v065_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_rmax_504d_base_v066_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_rmax_252d_base_v067_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_rmax_504d_base_v068_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_rmax_252d_base_v069_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_rmax_504d_base_v070_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_rmin_252d_base_v071_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_rmin_504d_base_v072_signal(inventory, closeadj):
    base = inventory
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_rmin_252d_base_v073_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_rmin_504d_base_v074_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_rmin_252d_base_v075_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

