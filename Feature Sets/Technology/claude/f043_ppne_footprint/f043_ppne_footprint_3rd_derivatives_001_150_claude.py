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
def _f043_ppne_share(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan).abs()


# 21d acceleration of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_accel_21d_3d_v001_signal(ppnenet, closeadj):
    base = ppnenet
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_accel_63d_3d_v002_signal(ppnenet, closeadj):
    base = ppnenet
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_accel_126d_3d_v003_signal(ppnenet, closeadj):
    base = ppnenet
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_accel_252d_3d_v004_signal(ppnenet, closeadj):
    base = ppnenet
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_accel_21d_3d_v005_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_accel_63d_3d_v006_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_accel_126d_3d_v007_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_accel_252d_3d_v008_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_accel_21d_3d_v009_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_accel_63d_3d_v010_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_accel_126d_3d_v011_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_accel_252d_3d_v012_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_accel_21d_3d_v013_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_accel_63d_3d_v014_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_accel_126d_3d_v015_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_accel_252d_3d_v016_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_accel_21d_3d_v017_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_accel_63d_3d_v018_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_accel_126d_3d_v019_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_accel_252d_3d_v020_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_accel_21d_3d_v021_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_accel_63d_3d_v022_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_accel_126d_3d_v023_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_accel_252d_3d_v024_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_accel_21d_3d_v025_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_accel_63d_3d_v026_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_accel_126d_3d_v027_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_accel_252d_3d_v028_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slopez_21d_z126_3d_v029_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slopez_63d_z252_3d_v030_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slopez_126d_z252_3d_v031_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slopez_252d_z504_3d_v032_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slopez_21d_z126_3d_v033_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slopez_63d_z252_3d_v034_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slopez_126d_z252_3d_v035_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slopez_252d_z504_3d_v036_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slopez_21d_z126_3d_v037_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slopez_63d_z252_3d_v038_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slopez_126d_z252_3d_v039_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slopez_252d_z504_3d_v040_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slopez_21d_z126_3d_v041_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slopez_63d_z252_3d_v042_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slopez_126d_z252_3d_v043_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slopez_252d_z504_3d_v044_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slopez_21d_z126_3d_v045_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slopez_63d_z252_3d_v046_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slopez_126d_z252_3d_v047_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slopez_252d_z504_3d_v048_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slopez_21d_z126_3d_v049_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slopez_63d_z252_3d_v050_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slopez_126d_z252_3d_v051_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slopez_252d_z504_3d_v052_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slopez_21d_z126_3d_v053_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slopez_63d_z252_3d_v054_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slopez_126d_z252_3d_v055_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slopez_252d_z504_3d_v056_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_jerk_21d_3d_v057_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_jerk_63d_3d_v058_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_jerk_126d_3d_v059_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_jerk_21d_3d_v060_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_jerk_63d_3d_v061_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_jerk_126d_3d_v062_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_jerk_21d_3d_v063_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_jerk_63d_3d_v064_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_jerk_126d_3d_v065_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_jerk_21d_3d_v066_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_jerk_63d_3d_v067_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_jerk_126d_3d_v068_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_jerk_21d_3d_v069_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_jerk_63d_3d_v070_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_jerk_126d_3d_v071_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_jerk_21d_3d_v072_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_jerk_63d_3d_v073_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_jerk_126d_3d_v074_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_jerk_21d_3d_v075_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_jerk_63d_3d_v076_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_jerk_126d_3d_v077_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_lvl smoothed over 252d
def f043ppe_f043_ppne_footprint_ppne_lvl_smoothaccel_63d_sm252_3d_v078_signal(ppnenet, closeadj):
    base = ppnenet
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_lvl smoothed over 504d
def f043ppe_f043_ppne_footprint_ppne_lvl_smoothaccel_252d_sm504_3d_v079_signal(ppnenet, closeadj):
    base = ppnenet
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_to_asset smoothed over 252d
def f043ppe_f043_ppne_footprint_ppne_to_asset_smoothaccel_63d_sm252_3d_v080_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_to_asset smoothed over 504d
def f043ppe_f043_ppne_footprint_ppne_to_asset_smoothaccel_252d_sm504_3d_v081_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_yoy smoothed over 252d
def f043ppe_f043_ppne_footprint_ppne_yoy_smoothaccel_63d_sm252_3d_v082_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_yoy smoothed over 504d
def f043ppe_f043_ppne_footprint_ppne_yoy_smoothaccel_252d_sm504_3d_v083_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_ppne smoothed over 252d
def f043ppe_f043_ppne_footprint_capex_to_ppne_smoothaccel_63d_sm252_3d_v084_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_ppne smoothed over 504d
def f043ppe_f043_ppne_footprint_capex_to_ppne_smoothaccel_252d_sm504_3d_v085_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_per_share smoothed over 252d
def f043ppe_f043_ppne_footprint_ppne_per_share_smoothaccel_63d_sm252_3d_v086_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_per_share smoothed over 504d
def f043ppe_f043_ppne_footprint_ppne_per_share_smoothaccel_252d_sm504_3d_v087_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_to_rev smoothed over 252d
def f043ppe_f043_ppne_footprint_ppne_to_rev_smoothaccel_63d_sm252_3d_v088_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_to_rev smoothed over 504d
def f043ppe_f043_ppne_footprint_ppne_to_rev_smoothaccel_252d_sm504_3d_v089_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_to_equity smoothed over 252d
def f043ppe_f043_ppne_footprint_ppne_to_equity_smoothaccel_63d_sm252_3d_v090_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_to_equity smoothed over 504d
def f043ppe_f043_ppne_footprint_ppne_to_equity_smoothaccel_252d_sm504_3d_v091_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_accelz_21d_z252_3d_v092_signal(ppnenet, closeadj):
    base = ppnenet
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_accelz_63d_z504_3d_v093_signal(ppnenet, closeadj):
    base = ppnenet
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_accelz_21d_z252_3d_v094_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_accelz_63d_z504_3d_v095_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_accelz_21d_z252_3d_v096_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_accelz_63d_z504_3d_v097_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_accelz_21d_z252_3d_v098_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_accelz_63d_z504_3d_v099_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_accelz_21d_z252_3d_v100_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_accelz_63d_z504_3d_v101_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_accelz_21d_z252_3d_v102_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_accelz_63d_z504_3d_v103_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_accelz_21d_z252_3d_v104_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_accelz_63d_z504_3d_v105_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ppne_lvl (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_lvl_signflip_63d_3d_v106_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ppne_lvl (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_lvl_signflip_252d_3d_v107_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ppne_to_asset (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_to_asset_signflip_63d_3d_v108_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ppne_to_asset (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_to_asset_signflip_252d_3d_v109_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ppne_yoy (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_yoy_signflip_63d_3d_v110_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ppne_yoy (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_yoy_signflip_252d_3d_v111_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in capex_to_ppne (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_capex_to_ppne_signflip_63d_3d_v112_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in capex_to_ppne (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_capex_to_ppne_signflip_252d_3d_v113_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ppne_per_share (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_per_share_signflip_63d_3d_v114_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ppne_per_share (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_per_share_signflip_252d_3d_v115_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ppne_to_rev (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_to_rev_signflip_63d_3d_v116_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ppne_to_rev (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_to_rev_signflip_252d_3d_v117_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ppne_to_equity (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_to_equity_signflip_63d_3d_v118_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ppne_to_equity (raw count, no price scaling)
def f043ppe_f043_ppne_footprint_ppne_to_equity_signflip_252d_3d_v119_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_lvl normalized by 252d range
def f043ppe_f043_ppne_footprint_ppne_lvl_rngaccel_63d_r252_3d_v120_signal(ppnenet, closeadj):
    base = ppnenet
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_lvl normalized by 504d range
def f043ppe_f043_ppne_footprint_ppne_lvl_rngaccel_252d_r504_3d_v121_signal(ppnenet, closeadj):
    base = ppnenet
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_asset normalized by 252d range
def f043ppe_f043_ppne_footprint_ppne_to_asset_rngaccel_63d_r252_3d_v122_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_asset normalized by 504d range
def f043ppe_f043_ppne_footprint_ppne_to_asset_rngaccel_252d_r504_3d_v123_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_yoy normalized by 252d range
def f043ppe_f043_ppne_footprint_ppne_yoy_rngaccel_63d_r252_3d_v124_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_yoy normalized by 504d range
def f043ppe_f043_ppne_footprint_ppne_yoy_rngaccel_252d_r504_3d_v125_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_ppne normalized by 252d range
def f043ppe_f043_ppne_footprint_capex_to_ppne_rngaccel_63d_r252_3d_v126_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_ppne normalized by 504d range
def f043ppe_f043_ppne_footprint_capex_to_ppne_rngaccel_252d_r504_3d_v127_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_per_share normalized by 252d range
def f043ppe_f043_ppne_footprint_ppne_per_share_rngaccel_63d_r252_3d_v128_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_per_share normalized by 504d range
def f043ppe_f043_ppne_footprint_ppne_per_share_rngaccel_252d_r504_3d_v129_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_rev normalized by 252d range
def f043ppe_f043_ppne_footprint_ppne_to_rev_rngaccel_63d_r252_3d_v130_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_rev normalized by 504d range
def f043ppe_f043_ppne_footprint_ppne_to_rev_rngaccel_252d_r504_3d_v131_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_equity normalized by 252d range
def f043ppe_f043_ppne_footprint_ppne_to_equity_rngaccel_63d_r252_3d_v132_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_equity normalized by 504d range
def f043ppe_f043_ppne_footprint_ppne_to_equity_rngaccel_252d_r504_3d_v133_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_cumslope_21d_3d_v134_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_cumslope_63d_3d_v135_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_cumslope_252d_3d_v136_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_cumslope_21d_3d_v137_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_cumslope_63d_3d_v138_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_cumslope_252d_3d_v139_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_cumslope_21d_3d_v140_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_cumslope_63d_3d_v141_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_cumslope_252d_3d_v142_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_cumslope_21d_3d_v143_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_cumslope_63d_3d_v144_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_cumslope_252d_3d_v145_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_cumslope_21d_3d_v146_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_cumslope_63d_3d_v147_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_cumslope_252d_3d_v148_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_cumslope_21d_3d_v149_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_cumslope_63d_3d_v150_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

