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


# 63d z-score of assets_lvl
def f040asb_f040_asset_base_assets_lvl_z_63d_base_v076_signal(assets, closeadj):
    base = assets
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assets_lvl
def f040asb_f040_asset_base_assets_lvl_z_126d_base_v077_signal(assets, closeadj):
    base = assets
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assets_lvl
def f040asb_f040_asset_base_assets_lvl_z_252d_base_v078_signal(assets, closeadj):
    base = assets
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assets_lvl
def f040asb_f040_asset_base_assets_lvl_z_504d_base_v079_signal(assets, closeadj):
    base = assets
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of log_assets
def f040asb_f040_asset_base_log_assets_z_63d_base_v080_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of log_assets
def f040asb_f040_asset_base_log_assets_z_126d_base_v081_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of log_assets
def f040asb_f040_asset_base_log_assets_z_252d_base_v082_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of log_assets
def f040asb_f040_asset_base_log_assets_z_504d_base_v083_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of assets_yoy
def f040asb_f040_asset_base_assets_yoy_z_63d_base_v084_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assets_yoy
def f040asb_f040_asset_base_assets_yoy_z_126d_base_v085_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assets_yoy
def f040asb_f040_asset_base_assets_yoy_z_252d_base_v086_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assets_yoy
def f040asb_f040_asset_base_assets_yoy_z_504d_base_v087_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of assetc_share
def f040asb_f040_asset_base_assetc_share_z_63d_base_v088_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assetc_share
def f040asb_f040_asset_base_assetc_share_z_126d_base_v089_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assetc_share
def f040asb_f040_asset_base_assetc_share_z_252d_base_v090_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assetc_share
def f040asb_f040_asset_base_assetc_share_z_504d_base_v091_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_z_63d_base_v092_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_z_126d_base_v093_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_z_252d_base_v094_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_z_504d_base_v095_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of asset_turn
def f040asb_f040_asset_base_asset_turn_z_63d_base_v096_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of asset_turn
def f040asb_f040_asset_base_asset_turn_z_126d_base_v097_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of asset_turn
def f040asb_f040_asset_base_asset_turn_z_252d_base_v098_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of asset_turn
def f040asb_f040_asset_base_asset_turn_z_504d_base_v099_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of asset_per_share
def f040asb_f040_asset_base_asset_per_share_z_63d_base_v100_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of asset_per_share
def f040asb_f040_asset_base_asset_per_share_z_126d_base_v101_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of asset_per_share
def f040asb_f040_asset_base_asset_per_share_z_252d_base_v102_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of asset_per_share
def f040asb_f040_asset_base_asset_per_share_z_504d_base_v103_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of assets_lvl
def f040asb_f040_asset_base_assets_lvl_distmax_252d_base_v104_signal(assets, closeadj):
    base = assets
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of assets_lvl
def f040asb_f040_asset_base_assets_lvl_distmax_504d_base_v105_signal(assets, closeadj):
    base = assets
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of log_assets
def f040asb_f040_asset_base_log_assets_distmax_252d_base_v106_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of log_assets
def f040asb_f040_asset_base_log_assets_distmax_504d_base_v107_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of assets_yoy
def f040asb_f040_asset_base_assets_yoy_distmax_252d_base_v108_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of assets_yoy
def f040asb_f040_asset_base_assets_yoy_distmax_504d_base_v109_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of assetc_share
def f040asb_f040_asset_base_assetc_share_distmax_252d_base_v110_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of assetc_share
def f040asb_f040_asset_base_assetc_share_distmax_504d_base_v111_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_distmax_252d_base_v112_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_distmax_504d_base_v113_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of asset_turn
def f040asb_f040_asset_base_asset_turn_distmax_252d_base_v114_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of asset_turn
def f040asb_f040_asset_base_asset_turn_distmax_504d_base_v115_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of asset_per_share
def f040asb_f040_asset_base_asset_per_share_distmax_252d_base_v116_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of asset_per_share
def f040asb_f040_asset_base_asset_per_share_distmax_504d_base_v117_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of assets_lvl
def f040asb_f040_asset_base_assets_lvl_distmed_126d_base_v118_signal(assets, closeadj):
    base = assets
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of assets_lvl
def f040asb_f040_asset_base_assets_lvl_distmed_252d_base_v119_signal(assets, closeadj):
    base = assets
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of assets_lvl
def f040asb_f040_asset_base_assets_lvl_distmed_504d_base_v120_signal(assets, closeadj):
    base = assets
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of log_assets
def f040asb_f040_asset_base_log_assets_distmed_126d_base_v121_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of log_assets
def f040asb_f040_asset_base_log_assets_distmed_252d_base_v122_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of log_assets
def f040asb_f040_asset_base_log_assets_distmed_504d_base_v123_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of assets_yoy
def f040asb_f040_asset_base_assets_yoy_distmed_126d_base_v124_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of assets_yoy
def f040asb_f040_asset_base_assets_yoy_distmed_252d_base_v125_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of assets_yoy
def f040asb_f040_asset_base_assets_yoy_distmed_504d_base_v126_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of assetc_share
def f040asb_f040_asset_base_assetc_share_distmed_126d_base_v127_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of assetc_share
def f040asb_f040_asset_base_assetc_share_distmed_252d_base_v128_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of assetc_share
def f040asb_f040_asset_base_assetc_share_distmed_504d_base_v129_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_distmed_126d_base_v130_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_distmed_252d_base_v131_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_distmed_504d_base_v132_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of asset_turn
def f040asb_f040_asset_base_asset_turn_distmed_126d_base_v133_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of asset_turn
def f040asb_f040_asset_base_asset_turn_distmed_252d_base_v134_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of asset_turn
def f040asb_f040_asset_base_asset_turn_distmed_504d_base_v135_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of asset_per_share
def f040asb_f040_asset_base_asset_per_share_distmed_126d_base_v136_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of asset_per_share
def f040asb_f040_asset_base_asset_per_share_distmed_252d_base_v137_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of asset_per_share
def f040asb_f040_asset_base_asset_per_share_distmed_504d_base_v138_signal(assets, sharesbas, closeadj):
    base = assets / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in assets_lvl
def f040asb_f040_asset_base_assets_lvl_chg_63d_base_v139_signal(assets, closeadj):
    base = assets
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in assets_lvl
def f040asb_f040_asset_base_assets_lvl_chg_252d_base_v140_signal(assets, closeadj):
    base = assets
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in log_assets
def f040asb_f040_asset_base_log_assets_chg_63d_base_v141_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in log_assets
def f040asb_f040_asset_base_log_assets_chg_252d_base_v142_signal(assets, closeadj):
    base = _f040_log_assets(assets)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in assets_yoy
def f040asb_f040_asset_base_assets_yoy_chg_63d_base_v143_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in assets_yoy
def f040asb_f040_asset_base_assets_yoy_chg_252d_base_v144_signal(assets, closeadj):
    base = assets.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in assetc_share
def f040asb_f040_asset_base_assetc_share_chg_63d_base_v145_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in assetc_share
def f040asb_f040_asset_base_assetc_share_chg_252d_base_v146_signal(assetsc, assets, closeadj):
    base = assetsc / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_chg_63d_base_v147_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in assetsnc_share
def f040asb_f040_asset_base_assetsnc_share_chg_252d_base_v148_signal(assetsnc, assets, closeadj):
    base = assetsnc / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in asset_turn
def f040asb_f040_asset_base_asset_turn_chg_63d_base_v149_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in asset_turn
def f040asb_f040_asset_base_asset_turn_chg_252d_base_v150_signal(revenue, assetsavg, closeadj):
    base = revenue / assetsavg.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

