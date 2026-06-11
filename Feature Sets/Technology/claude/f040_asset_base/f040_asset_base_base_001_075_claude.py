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
def _f040_log_assets(assets):
    return np.log(assets.abs().replace(0, np.nan))


# 21d mean of assets_lvl scaled by closeadj
def f040asb_f040_asset_base_assets_lvl_mean_21d_base_v001_signal(assets, closeadj):
    base = assets
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of assets_lvl scaled by closeadj
def f040asb_f040_asset_base_assets_lvl_mean_63d_base_v002_signal(assets, closeadj):
    base = assets
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of assets_lvl scaled by closeadj
def f040asb_f040_asset_base_assets_lvl_mean_126d_base_v003_signal(assets, closeadj):
    base = assets
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of assets_lvl scaled by closeadj
def f040asb_f040_asset_base_assets_lvl_mean_252d_base_v004_signal(assets, closeadj):
    base = assets
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of assets_lvl scaled by closeadj
def f040asb_f040_asset_base_assets_lvl_mean_504d_base_v005_signal(assets, closeadj):
    base = assets
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_assets scaled by closeadj
def f040asb_f040_asset_base_log_assets_mean_21d_base_v006_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_assets scaled by closeadj
def f040asb_f040_asset_base_log_assets_mean_63d_base_v007_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_assets scaled by closeadj
def f040asb_f040_asset_base_log_assets_mean_126d_base_v008_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_assets scaled by closeadj
def f040asb_f040_asset_base_log_assets_mean_252d_base_v009_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_assets scaled by closeadj
def f040asb_f040_asset_base_log_assets_mean_504d_base_v010_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of assets_yoy scaled by closeadj
def f040asb_f040_asset_base_assets_yoy_mean_21d_base_v011_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of assets_yoy scaled by closeadj
def f040asb_f040_asset_base_assets_yoy_mean_63d_base_v012_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of assets_yoy scaled by closeadj
def f040asb_f040_asset_base_assets_yoy_mean_126d_base_v013_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of assets_yoy scaled by closeadj
def f040asb_f040_asset_base_assets_yoy_mean_252d_base_v014_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of assets_yoy scaled by closeadj
def f040asb_f040_asset_base_assets_yoy_mean_504d_base_v015_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of assetc_share scaled by closeadj
def f040asb_f040_asset_base_assetc_share_mean_21d_base_v016_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of assetc_share scaled by closeadj
def f040asb_f040_asset_base_assetc_share_mean_63d_base_v017_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of assetc_share scaled by closeadj
def f040asb_f040_asset_base_assetc_share_mean_126d_base_v018_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of assetc_share scaled by closeadj
def f040asb_f040_asset_base_assetc_share_mean_252d_base_v019_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of assetc_share scaled by closeadj
def f040asb_f040_asset_base_assetc_share_mean_504d_base_v020_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of assetsnc_share scaled by closeadj
def f040asb_f040_asset_base_assetsnc_share_mean_21d_base_v021_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of assetsnc_share scaled by closeadj
def f040asb_f040_asset_base_assetsnc_share_mean_63d_base_v022_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of assetsnc_share scaled by closeadj
def f040asb_f040_asset_base_assetsnc_share_mean_126d_base_v023_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of assetsnc_share scaled by closeadj
def f040asb_f040_asset_base_assetsnc_share_mean_252d_base_v024_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of assetsnc_share scaled by closeadj
def f040asb_f040_asset_base_assetsnc_share_mean_504d_base_v025_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of asset_turn scaled by closeadj
def f040asb_f040_asset_base_asset_turn_mean_21d_base_v026_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of asset_turn scaled by closeadj
def f040asb_f040_asset_base_asset_turn_mean_63d_base_v027_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of asset_turn scaled by closeadj
def f040asb_f040_asset_base_asset_turn_mean_126d_base_v028_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of asset_turn scaled by closeadj
def f040asb_f040_asset_base_asset_turn_mean_252d_base_v029_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of asset_turn scaled by closeadj
def f040asb_f040_asset_base_asset_turn_mean_504d_base_v030_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of asset_per_share scaled by closeadj
def f040asb_f040_asset_base_asset_per_share_mean_21d_base_v031_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of asset_per_share scaled by closeadj
def f040asb_f040_asset_base_asset_per_share_mean_63d_base_v032_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of asset_per_share scaled by closeadj
def f040asb_f040_asset_base_asset_per_share_mean_126d_base_v033_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of asset_per_share scaled by closeadj
def f040asb_f040_asset_base_asset_per_share_mean_252d_base_v034_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of asset_per_share scaled by closeadj
def f040asb_f040_asset_base_asset_per_share_mean_504d_base_v035_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of assets_lvl
def f040asb_f040_asset_base_assets_lvl_median_63d_base_v036_signal(assets, closeadj):
    base = assets
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of assets_lvl
def f040asb_f040_asset_base_assets_lvl_median_252d_base_v037_signal(assets, closeadj):
    base = assets
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of assets_lvl
def f040asb_f040_asset_base_assets_lvl_median_504d_base_v038_signal(assets, closeadj):
    base = assets
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_assets
def f040asb_f040_asset_base_log_assets_median_63d_base_v039_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_assets
def f040asb_f040_asset_base_log_assets_median_252d_base_v040_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_assets
def f040asb_f040_asset_base_log_assets_median_504d_base_v041_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of assets_yoy
def f040asb_f040_asset_base_assets_yoy_median_63d_base_v042_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of assets_yoy
def f040asb_f040_asset_base_assets_yoy_median_252d_base_v043_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of assets_yoy
def f040asb_f040_asset_base_assets_yoy_median_504d_base_v044_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of assetc_share
def f040asb_f040_asset_base_assetc_share_median_63d_base_v045_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of assetc_share
def f040asb_f040_asset_base_assetc_share_median_252d_base_v046_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of assetc_share
def f040asb_f040_asset_base_assetc_share_median_504d_base_v047_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_median_63d_base_v048_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_median_252d_base_v049_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_median_504d_base_v050_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of asset_turn
def f040asb_f040_asset_base_asset_turn_median_63d_base_v051_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of asset_turn
def f040asb_f040_asset_base_asset_turn_median_252d_base_v052_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of asset_turn
def f040asb_f040_asset_base_asset_turn_median_504d_base_v053_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of asset_per_share
def f040asb_f040_asset_base_asset_per_share_median_63d_base_v054_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of asset_per_share
def f040asb_f040_asset_base_asset_per_share_median_252d_base_v055_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of asset_per_share
def f040asb_f040_asset_base_asset_per_share_median_504d_base_v056_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of assets_lvl
def f040asb_f040_asset_base_assets_lvl_rmax_252d_base_v057_signal(assets, closeadj):
    base = assets
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of assets_lvl
def f040asb_f040_asset_base_assets_lvl_rmax_504d_base_v058_signal(assets, closeadj):
    base = assets
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of log_assets
def f040asb_f040_asset_base_log_assets_rmax_252d_base_v059_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of log_assets
def f040asb_f040_asset_base_log_assets_rmax_504d_base_v060_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of assets_yoy
def f040asb_f040_asset_base_assets_yoy_rmax_252d_base_v061_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of assets_yoy
def f040asb_f040_asset_base_assets_yoy_rmax_504d_base_v062_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of assetc_share
def f040asb_f040_asset_base_assetc_share_rmax_252d_base_v063_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of assetc_share
def f040asb_f040_asset_base_assetc_share_rmax_504d_base_v064_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_rmax_252d_base_v065_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_rmax_504d_base_v066_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of asset_turn
def f040asb_f040_asset_base_asset_turn_rmax_252d_base_v067_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of asset_turn
def f040asb_f040_asset_base_asset_turn_rmax_504d_base_v068_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of asset_per_share
def f040asb_f040_asset_base_asset_per_share_rmax_252d_base_v069_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of asset_per_share
def f040asb_f040_asset_base_asset_per_share_rmax_504d_base_v070_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of assets_lvl
def f040asb_f040_asset_base_assets_lvl_rmin_252d_base_v071_signal(assets, closeadj):
    base = assets
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of assets_lvl
def f040asb_f040_asset_base_assets_lvl_rmin_504d_base_v072_signal(assets, closeadj):
    base = assets
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of log_assets
def f040asb_f040_asset_base_log_assets_rmin_252d_base_v073_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of log_assets
def f040asb_f040_asset_base_log_assets_rmin_504d_base_v074_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of assets_yoy
def f040asb_f040_asset_base_assets_yoy_rmin_252d_base_v075_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

