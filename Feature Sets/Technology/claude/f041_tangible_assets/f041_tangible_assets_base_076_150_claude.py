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
def _f041_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan).abs()


# 63d z-score of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_z_63d_base_v076_signal(tangibles, closeadj):
    base = tangibles
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_z_126d_base_v077_signal(tangibles, closeadj):
    base = tangibles
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_z_252d_base_v078_signal(tangibles, closeadj):
    base = tangibles
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_z_504d_base_v079_signal(tangibles, closeadj):
    base = tangibles
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_z_63d_base_v080_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_z_126d_base_v081_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_z_252d_base_v082_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_z_504d_base_v083_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_z_63d_base_v084_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_z_126d_base_v085_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_z_252d_base_v086_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_z_504d_base_v087_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of intang_share
def f041tng_f041_tangible_assets_intang_share_z_63d_base_v088_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of intang_share
def f041tng_f041_tangible_assets_intang_share_z_126d_base_v089_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of intang_share
def f041tng_f041_tangible_assets_intang_share_z_252d_base_v090_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of intang_share
def f041tng_f041_tangible_assets_intang_share_z_504d_base_v091_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_z_63d_base_v092_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_z_126d_base_v093_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_z_252d_base_v094_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_z_504d_base_v095_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_z_63d_base_v096_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_z_126d_base_v097_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_z_252d_base_v098_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_z_504d_base_v099_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_z_63d_base_v100_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_z_126d_base_v101_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_z_252d_base_v102_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_z_504d_base_v103_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_distmax_252d_base_v104_signal(tangibles, closeadj):
    base = tangibles
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_distmax_504d_base_v105_signal(tangibles, closeadj):
    base = tangibles
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_distmax_252d_base_v106_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_distmax_504d_base_v107_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_distmax_252d_base_v108_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_distmax_504d_base_v109_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of intang_share
def f041tng_f041_tangible_assets_intang_share_distmax_252d_base_v110_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of intang_share
def f041tng_f041_tangible_assets_intang_share_distmax_504d_base_v111_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_distmax_252d_base_v112_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_distmax_504d_base_v113_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_distmax_252d_base_v114_signal(tbvps, closeadj):
    base = tbvps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_distmax_504d_base_v115_signal(tbvps, closeadj):
    base = tbvps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_distmax_252d_base_v116_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_distmax_504d_base_v117_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_distmed_126d_base_v118_signal(tangibles, closeadj):
    base = tangibles
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_distmed_252d_base_v119_signal(tangibles, closeadj):
    base = tangibles
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_distmed_504d_base_v120_signal(tangibles, closeadj):
    base = tangibles
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_distmed_126d_base_v121_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_distmed_252d_base_v122_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_distmed_504d_base_v123_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_distmed_126d_base_v124_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_distmed_252d_base_v125_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_distmed_504d_base_v126_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of intang_share
def f041tng_f041_tangible_assets_intang_share_distmed_126d_base_v127_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of intang_share
def f041tng_f041_tangible_assets_intang_share_distmed_252d_base_v128_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of intang_share
def f041tng_f041_tangible_assets_intang_share_distmed_504d_base_v129_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_distmed_126d_base_v130_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_distmed_252d_base_v131_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_distmed_504d_base_v132_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_distmed_126d_base_v133_signal(tbvps, closeadj):
    base = tbvps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_distmed_252d_base_v134_signal(tbvps, closeadj):
    base = tbvps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_distmed_504d_base_v135_signal(tbvps, closeadj):
    base = tbvps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_distmed_126d_base_v136_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_distmed_252d_base_v137_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_distmed_504d_base_v138_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_chg_63d_base_v139_signal(tangibles, closeadj):
    base = tangibles
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_chg_252d_base_v140_signal(tangibles, closeadj):
    base = tangibles
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_chg_63d_base_v141_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_chg_252d_base_v142_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_chg_63d_base_v143_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_chg_252d_base_v144_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in intang_share
def f041tng_f041_tangible_assets_intang_share_chg_63d_base_v145_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in intang_share
def f041tng_f041_tangible_assets_intang_share_chg_252d_base_v146_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_chg_63d_base_v147_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_chg_252d_base_v148_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_chg_63d_base_v149_signal(tbvps, closeadj):
    base = tbvps
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_chg_252d_base_v150_signal(tbvps, closeadj):
    base = tbvps
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

