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


# 63d z-score of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_z_63d_base_v076_signal(inventory, closeadj):
    base = inventory
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_z_126d_base_v077_signal(inventory, closeadj):
    base = inventory
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_z_252d_base_v078_signal(inventory, closeadj):
    base = inventory
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_z_504d_base_v079_signal(inventory, closeadj):
    base = inventory
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_z_63d_base_v080_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_z_126d_base_v081_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_z_252d_base_v082_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_z_504d_base_v083_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_z_63d_base_v084_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_z_126d_base_v085_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_z_252d_base_v086_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_z_504d_base_v087_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_z_63d_base_v088_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_z_126d_base_v089_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_z_252d_base_v090_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_z_504d_base_v091_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_z_63d_base_v092_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_z_126d_base_v093_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_z_252d_base_v094_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_z_504d_base_v095_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_z_63d_base_v096_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_z_126d_base_v097_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_z_252d_base_v098_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_z_504d_base_v099_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_z_63d_base_v100_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_z_126d_base_v101_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_z_252d_base_v102_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_z_504d_base_v103_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_distmax_252d_base_v104_signal(inventory, closeadj):
    base = inventory
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_distmax_504d_base_v105_signal(inventory, closeadj):
    base = inventory
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_distmax_252d_base_v106_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_distmax_504d_base_v107_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_distmax_252d_base_v108_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_distmax_504d_base_v109_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_distmax_252d_base_v110_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_distmax_504d_base_v111_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_distmax_252d_base_v112_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_distmax_504d_base_v113_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_distmax_252d_base_v114_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_distmax_504d_base_v115_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_distmax_252d_base_v116_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_distmax_504d_base_v117_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_distmed_126d_base_v118_signal(inventory, closeadj):
    base = inventory
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_distmed_252d_base_v119_signal(inventory, closeadj):
    base = inventory
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_distmed_504d_base_v120_signal(inventory, closeadj):
    base = inventory
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_distmed_126d_base_v121_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_distmed_252d_base_v122_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_distmed_504d_base_v123_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_distmed_126d_base_v124_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_distmed_252d_base_v125_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_distmed_504d_base_v126_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_distmed_126d_base_v127_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_distmed_252d_base_v128_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_distmed_504d_base_v129_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_distmed_126d_base_v130_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_distmed_252d_base_v131_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_distmed_504d_base_v132_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_distmed_126d_base_v133_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_distmed_252d_base_v134_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_distmed_504d_base_v135_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_distmed_126d_base_v136_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_distmed_252d_base_v137_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of inv_to_curasset
def f044ind_f044_inventory_dynamics_inv_to_curasset_distmed_504d_base_v138_signal(inventory, assetsc, closeadj):
    base = inventory / assetsc.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_chg_63d_base_v139_signal(inventory, closeadj):
    base = inventory
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_lvl
def f044ind_f044_inventory_dynamics_inv_lvl_chg_252d_base_v140_signal(inventory, closeadj):
    base = inventory
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_chg_63d_base_v141_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_to_rev
def f044ind_f044_inventory_dynamics_inv_to_rev_chg_252d_base_v142_signal(inventory, revenue, closeadj):
    base = _f044_inv_to_rev(inventory, revenue)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_chg_63d_base_v143_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_turns
def f044ind_f044_inventory_dynamics_inv_turns_chg_252d_base_v144_signal(cor, inventory, closeadj):
    base = cor / inventory.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_chg_63d_base_v145_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_growth
def f044ind_f044_inventory_dynamics_inv_growth_chg_252d_base_v146_signal(inventory, closeadj):
    base = inventory.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_chg_63d_base_v147_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_to_asset
def f044ind_f044_inventory_dynamics_inv_to_asset_chg_252d_base_v148_signal(inventory, assets, closeadj):
    base = inventory / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_chg_63d_base_v149_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in inv_per_share
def f044ind_f044_inventory_dynamics_inv_per_share_chg_252d_base_v150_signal(inventory, sharesbas, closeadj):
    base = inventory / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

