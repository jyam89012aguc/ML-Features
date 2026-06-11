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
def _f043_ppne_share(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan).abs()


# 21d mean of ppne_lvl scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_lvl_mean_21d_base_v001_signal(ppnenet, closeadj):
    base = ppnenet
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_lvl scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_lvl_mean_63d_base_v002_signal(ppnenet, closeadj):
    base = ppnenet
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_lvl scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_lvl_mean_126d_base_v003_signal(ppnenet, closeadj):
    base = ppnenet
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_lvl scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_lvl_mean_252d_base_v004_signal(ppnenet, closeadj):
    base = ppnenet
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_lvl scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_lvl_mean_504d_base_v005_signal(ppnenet, closeadj):
    base = ppnenet
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ppne_to_asset scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_asset_mean_21d_base_v006_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_to_asset scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_asset_mean_63d_base_v007_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_to_asset scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_asset_mean_126d_base_v008_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_to_asset scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_asset_mean_252d_base_v009_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_to_asset scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_asset_mean_504d_base_v010_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ppne_yoy scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_yoy_mean_21d_base_v011_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_yoy scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_yoy_mean_63d_base_v012_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_yoy scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_yoy_mean_126d_base_v013_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_yoy scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_yoy_mean_252d_base_v014_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_yoy scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_yoy_mean_504d_base_v015_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_ppne scaled by closeadj
def f043ppe_f043_ppne_footprint_capex_to_ppne_mean_21d_base_v016_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_ppne scaled by closeadj
def f043ppe_f043_ppne_footprint_capex_to_ppne_mean_63d_base_v017_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_ppne scaled by closeadj
def f043ppe_f043_ppne_footprint_capex_to_ppne_mean_126d_base_v018_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_ppne scaled by closeadj
def f043ppe_f043_ppne_footprint_capex_to_ppne_mean_252d_base_v019_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_ppne scaled by closeadj
def f043ppe_f043_ppne_footprint_capex_to_ppne_mean_504d_base_v020_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ppne_per_share scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_per_share_mean_21d_base_v021_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_per_share scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_per_share_mean_63d_base_v022_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_per_share scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_per_share_mean_126d_base_v023_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_per_share scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_per_share_mean_252d_base_v024_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_per_share scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_per_share_mean_504d_base_v025_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ppne_to_rev scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_rev_mean_21d_base_v026_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_to_rev scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_rev_mean_63d_base_v027_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_to_rev scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_rev_mean_126d_base_v028_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_to_rev scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_rev_mean_252d_base_v029_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_to_rev scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_rev_mean_504d_base_v030_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ppne_to_equity scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_equity_mean_21d_base_v031_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_to_equity scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_equity_mean_63d_base_v032_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_to_equity scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_equity_mean_126d_base_v033_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_to_equity scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_equity_mean_252d_base_v034_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_to_equity scaled by closeadj
def f043ppe_f043_ppne_footprint_ppne_to_equity_mean_504d_base_v035_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_median_63d_base_v036_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_median_252d_base_v037_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_median_504d_base_v038_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_median_63d_base_v039_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_median_252d_base_v040_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_median_504d_base_v041_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_median_63d_base_v042_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_median_252d_base_v043_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_median_504d_base_v044_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_median_63d_base_v045_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_median_252d_base_v046_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_median_504d_base_v047_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_median_63d_base_v048_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_median_252d_base_v049_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_median_504d_base_v050_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_median_63d_base_v051_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_median_252d_base_v052_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_median_504d_base_v053_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_median_63d_base_v054_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_median_252d_base_v055_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_median_504d_base_v056_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_rmax_252d_base_v057_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_rmax_504d_base_v058_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_rmax_252d_base_v059_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_rmax_504d_base_v060_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_rmax_252d_base_v061_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_rmax_504d_base_v062_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_rmax_252d_base_v063_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of capex_to_ppne
def f043ppe_f043_ppne_footprint_capex_to_ppne_rmax_504d_base_v064_signal(capex, ppnenet, closeadj):
    base = capex.abs() / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_rmax_252d_base_v065_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ppne_per_share
def f043ppe_f043_ppne_footprint_ppne_per_share_rmax_504d_base_v066_signal(ppnenet, sharesbas, closeadj):
    base = ppnenet / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_rmax_252d_base_v067_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ppne_to_rev
def f043ppe_f043_ppne_footprint_ppne_to_rev_rmax_504d_base_v068_signal(ppnenet, revenue, closeadj):
    base = ppnenet / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_rmax_252d_base_v069_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ppne_to_equity
def f043ppe_f043_ppne_footprint_ppne_to_equity_rmax_504d_base_v070_signal(ppnenet, equity, closeadj):
    base = ppnenet / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_rmin_252d_base_v071_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ppne_lvl
def f043ppe_f043_ppne_footprint_ppne_lvl_rmin_504d_base_v072_signal(ppnenet, closeadj):
    base = ppnenet
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_rmin_252d_base_v073_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ppne_to_asset
def f043ppe_f043_ppne_footprint_ppne_to_asset_rmin_504d_base_v074_signal(ppnenet, assets, closeadj):
    base = _f043_ppne_share(ppnenet, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ppne_yoy
def f043ppe_f043_ppne_footprint_ppne_yoy_rmin_252d_base_v075_signal(ppnenet, closeadj):
    base = ppnenet.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

