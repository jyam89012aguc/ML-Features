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


# 21d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slope_21d_2d_v001_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slope_63d_2d_v002_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slope_126d_2d_v003_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slope_252d_2d_v004_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_slope_504d_2d_v005_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slope_21d_2d_v006_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slope_63d_2d_v007_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slope_126d_2d_v008_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slope_252d_2d_v009_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_slope_504d_2d_v010_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slope_21d_2d_v011_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slope_63d_2d_v012_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slope_126d_2d_v013_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slope_252d_2d_v014_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_slope_504d_2d_v015_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slope_21d_2d_v016_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slope_63d_2d_v017_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slope_126d_2d_v018_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slope_252d_2d_v019_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_slope_504d_2d_v020_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slope_21d_2d_v021_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slope_63d_2d_v022_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slope_126d_2d_v023_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slope_252d_2d_v024_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_slope_504d_2d_v025_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slope_21d_2d_v026_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slope_63d_2d_v027_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slope_126d_2d_v028_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slope_252d_2d_v029_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_slope_504d_2d_v030_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slope_21d_2d_v031_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slope_63d_2d_v032_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slope_126d_2d_v033_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slope_252d_2d_v034_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_slope_504d_2d_v035_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sm21_sl21_2d_v036_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sm63_sl21_2d_v037_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sm63_sl63_2d_v038_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sm252_sl63_2d_v039_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sm252_sl126_2d_v040_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sm21_sl21_2d_v041_signal(ppnenet, assets, closeadj):
    base = _mean(_f043_ppne_share(ppnenet, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sm63_sl21_2d_v042_signal(ppnenet, assets, closeadj):
    base = _mean(_f043_ppne_share(ppnenet, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sm63_sl63_2d_v043_signal(ppnenet, assets, closeadj):
    base = _mean(_f043_ppne_share(ppnenet, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sm252_sl63_2d_v044_signal(ppnenet, assets, closeadj):
    base = _mean(_f043_ppne_share(ppnenet, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sm252_sl126_2d_v045_signal(ppnenet, assets, closeadj):
    base = _mean(_f043_ppne_share(ppnenet, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sm21_sl21_2d_v046_signal(ppnenet, closeadj):
    base = _mean(ppnenet.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sm63_sl21_2d_v047_signal(ppnenet, closeadj):
    base = _mean(ppnenet.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sm63_sl63_2d_v048_signal(ppnenet, closeadj):
    base = _mean(ppnenet.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sm252_sl63_2d_v049_signal(ppnenet, closeadj):
    base = _mean(ppnenet.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sm252_sl126_2d_v050_signal(ppnenet, closeadj):
    base = _mean(ppnenet.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sm21_sl21_2d_v051_signal(capex, ppnenet, closeadj):
    base = _mean(capex.abs() / ppnenet.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sm63_sl21_2d_v052_signal(capex, ppnenet, closeadj):
    base = _mean(capex.abs() / ppnenet.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sm63_sl63_2d_v053_signal(capex, ppnenet, closeadj):
    base = _mean(capex.abs() / ppnenet.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sm252_sl63_2d_v054_signal(capex, ppnenet, closeadj):
    base = _mean(capex.abs() / ppnenet.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sm252_sl126_2d_v055_signal(capex, ppnenet, closeadj):
    base = _mean(capex.abs() / ppnenet.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sm21_sl21_2d_v056_signal(ppnenet, sharesbas, closeadj):
    base = _mean(ppnenet / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sm63_sl21_2d_v057_signal(ppnenet, sharesbas, closeadj):
    base = _mean(ppnenet / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sm63_sl63_2d_v058_signal(ppnenet, sharesbas, closeadj):
    base = _mean(ppnenet / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sm252_sl63_2d_v059_signal(ppnenet, sharesbas, closeadj):
    base = _mean(ppnenet / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sm252_sl126_2d_v060_signal(ppnenet, sharesbas, closeadj):
    base = _mean(ppnenet / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sm21_sl21_2d_v061_signal(ppnenet, revenue, closeadj):
    base = _mean(ppnenet / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sm63_sl21_2d_v062_signal(ppnenet, revenue, closeadj):
    base = _mean(ppnenet / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sm63_sl63_2d_v063_signal(ppnenet, revenue, closeadj):
    base = _mean(ppnenet / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sm252_sl63_2d_v064_signal(ppnenet, revenue, closeadj):
    base = _mean(ppnenet / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sm252_sl126_2d_v065_signal(ppnenet, revenue, closeadj):
    base = _mean(ppnenet / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sm21_sl21_2d_v066_signal(ppnenet, equity, closeadj):
    base = _mean(ppnenet / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sm63_sl21_2d_v067_signal(ppnenet, equity, closeadj):
    base = _mean(ppnenet / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sm63_sl63_2d_v068_signal(ppnenet, equity, closeadj):
    base = _mean(ppnenet / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sm252_sl63_2d_v069_signal(ppnenet, equity, closeadj):
    base = _mean(ppnenet / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sm252_sl126_2d_v070_signal(ppnenet, equity, closeadj):
    base = _mean(ppnenet / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_pctslope_21d_2d_v071_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_pctslope_63d_2d_v072_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_pctslope_252d_2d_v073_signal(ppnenet, closeadj):
    base = ppnenet
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_pctslope_21d_2d_v074_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_pctslope_63d_2d_v075_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_pctslope_252d_2d_v076_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_pctslope_21d_2d_v077_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_pctslope_63d_2d_v078_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_pctslope_252d_2d_v079_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_pctslope_21d_2d_v080_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_pctslope_63d_2d_v081_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_pctslope_252d_2d_v082_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_pctslope_21d_2d_v083_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_pctslope_63d_2d_v084_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_pctslope_252d_2d_v085_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_pctslope_21d_2d_v086_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_pctslope_63d_2d_v087_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_pctslope_252d_2d_v088_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_pctslope_21d_2d_v089_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_pctslope_63d_2d_v090_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_pctslope_252d_2d_v091_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sgnslope_21d_2d_v092_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sgnslope_63d_2d_v093_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_sgnslope_252d_2d_v094_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sgnslope_21d_2d_v095_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sgnslope_63d_2d_v096_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_sgnslope_252d_2d_v097_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sgnslope_21d_2d_v098_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sgnslope_63d_2d_v099_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_sgnslope_252d_2d_v100_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sgnslope_21d_2d_v101_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sgnslope_63d_2d_v102_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_sgnslope_252d_2d_v103_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sgnslope_21d_2d_v104_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sgnslope_63d_2d_v105_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_sgnslope_252d_2d_v106_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sgnslope_21d_2d_v107_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sgnslope_63d_2d_v108_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_sgnslope_252d_2d_v109_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sgnslope_21d_2d_v110_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sgnslope_63d_2d_v111_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_sgnslope_252d_2d_v112_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_logmagslope_21d_2d_v113_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_logmagslope_63d_2d_v114_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_logmagslope_252d_2d_v115_signal(ppnenet, closeadj):
    base = ppnenet
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_logmagslope_21d_2d_v116_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_logmagslope_63d_2d_v117_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_logmagslope_252d_2d_v118_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_logmagslope_21d_2d_v119_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_logmagslope_63d_2d_v120_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_logmagslope_252d_2d_v121_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_logmagslope_21d_2d_v122_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_logmagslope_63d_2d_v123_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_logmagslope_252d_2d_v124_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_logmagslope_21d_2d_v125_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_logmagslope_63d_2d_v126_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_logmagslope_252d_2d_v127_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_logmagslope_21d_2d_v128_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_logmagslope_63d_2d_v129_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_logmagslope_252d_2d_v130_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_logmagslope_21d_2d_v131_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_logmagslope_63d_2d_v132_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_logmagslope_252d_2d_v133_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ppne_lvl|
def f043ppe_f043_ppne_footprint_ppne_lvl_logslope_63d_2d_v134_signal(ppnenet, closeadj):
    base = np.log((ppnenet).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ppne_lvl|
def f043ppe_f043_ppne_footprint_ppne_lvl_logslope_252d_2d_v135_signal(ppnenet, closeadj):
    base = np.log((ppnenet).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ppne_to_asset|
def f043ppe_f043_ppne_footprint_ppne_to_asset_logslope_63d_2d_v136_signal(ppnenet, assets, closeadj):
    base = np.log((_f043_ppne_share(ppnenet, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ppne_to_asset|
def f043ppe_f043_ppne_footprint_ppne_to_asset_logslope_252d_2d_v137_signal(ppnenet, assets, closeadj):
    base = np.log((_f043_ppne_share(ppnenet, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ppne_yoy|
def f043ppe_f043_ppne_footprint_ppne_yoy_logslope_63d_2d_v138_signal(ppnenet, closeadj):
    base = np.log((ppnenet.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ppne_yoy|
def f043ppe_f043_ppne_footprint_ppne_yoy_logslope_252d_2d_v139_signal(ppnenet, closeadj):
    base = np.log((ppnenet.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|capex_to_ppne|
def f043ppe_f043_ppne_footprint_capex_to_ppne_logslope_63d_2d_v140_signal(capex, ppnenet, closeadj):
    base = np.log((capex.abs() / ppnenet.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|capex_to_ppne|
def f043ppe_f043_ppne_footprint_capex_to_ppne_logslope_252d_2d_v141_signal(capex, ppnenet, closeadj):
    base = np.log((capex.abs() / ppnenet.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ppne_per_share|
def f043ppe_f043_ppne_footprint_ppne_per_share_logslope_63d_2d_v142_signal(ppnenet, sharesbas, closeadj):
    base = np.log((ppnenet / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ppne_per_share|
def f043ppe_f043_ppne_footprint_ppne_per_share_logslope_252d_2d_v143_signal(ppnenet, sharesbas, closeadj):
    base = np.log((ppnenet / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ppne_to_rev|
def f043ppe_f043_ppne_footprint_ppne_to_rev_logslope_63d_2d_v144_signal(ppnenet, revenue, closeadj):
    base = np.log((ppnenet / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ppne_to_rev|
def f043ppe_f043_ppne_footprint_ppne_to_rev_logslope_252d_2d_v145_signal(ppnenet, revenue, closeadj):
    base = np.log((ppnenet / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ppne_to_equity|
def f043ppe_f043_ppne_footprint_ppne_to_equity_logslope_63d_2d_v146_signal(ppnenet, equity, closeadj):
    base = np.log((ppnenet / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ppne_to_equity|
def f043ppe_f043_ppne_footprint_ppne_to_equity_logslope_252d_2d_v147_signal(ppnenet, equity, closeadj):
    base = np.log((ppnenet / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

