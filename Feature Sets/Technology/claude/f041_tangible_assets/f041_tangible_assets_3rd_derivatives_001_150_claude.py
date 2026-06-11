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
def _f041_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan).abs()


# 21d acceleration of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_accel_21d_3d_v001_signal(tangibles, closeadj):
    base = tangibles
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_accel_63d_3d_v002_signal(tangibles, closeadj):
    base = tangibles
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_accel_126d_3d_v003_signal(tangibles, closeadj):
    base = tangibles
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_accel_252d_3d_v004_signal(tangibles, closeadj):
    base = tangibles
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_accel_21d_3d_v005_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_accel_63d_3d_v006_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_accel_126d_3d_v007_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_accel_252d_3d_v008_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_accel_21d_3d_v009_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_accel_63d_3d_v010_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_accel_126d_3d_v011_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_accel_252d_3d_v012_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_share
def f041tng_f041_tangible_assets_intang_share_accel_21d_3d_v013_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_share
def f041tng_f041_tangible_assets_intang_share_accel_63d_3d_v014_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_share
def f041tng_f041_tangible_assets_intang_share_accel_126d_3d_v015_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_share
def f041tng_f041_tangible_assets_intang_share_accel_252d_3d_v016_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_accel_21d_3d_v017_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_accel_63d_3d_v018_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_accel_126d_3d_v019_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_accel_252d_3d_v020_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_accel_21d_3d_v021_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_accel_63d_3d_v022_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_accel_126d_3d_v023_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_accel_252d_3d_v024_signal(tbvps, closeadj):
    base = tbvps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_accel_21d_3d_v025_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_accel_63d_3d_v026_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_accel_126d_3d_v027_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_accel_252d_3d_v028_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slopez_21d_z126_3d_v029_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slopez_63d_z252_3d_v030_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slopez_126d_z252_3d_v031_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slopez_252d_z504_3d_v032_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slopez_21d_z126_3d_v033_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slopez_63d_z252_3d_v034_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slopez_126d_z252_3d_v035_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slopez_252d_z504_3d_v036_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slopez_21d_z126_3d_v037_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slopez_63d_z252_3d_v038_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slopez_126d_z252_3d_v039_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slopez_252d_z504_3d_v040_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_share
def f041tng_f041_tangible_assets_intang_share_slopez_21d_z126_3d_v041_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_share
def f041tng_f041_tangible_assets_intang_share_slopez_63d_z252_3d_v042_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_share
def f041tng_f041_tangible_assets_intang_share_slopez_126d_z252_3d_v043_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_share
def f041tng_f041_tangible_assets_intang_share_slopez_252d_z504_3d_v044_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slopez_21d_z126_3d_v045_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slopez_63d_z252_3d_v046_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slopez_126d_z252_3d_v047_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slopez_252d_z504_3d_v048_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slopez_21d_z126_3d_v049_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slopez_63d_z252_3d_v050_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slopez_126d_z252_3d_v051_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slopez_252d_z504_3d_v052_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slopez_21d_z126_3d_v053_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slopez_63d_z252_3d_v054_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slopez_126d_z252_3d_v055_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slopez_252d_z504_3d_v056_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_jerk_21d_3d_v057_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_jerk_63d_3d_v058_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_jerk_126d_3d_v059_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_jerk_21d_3d_v060_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_jerk_63d_3d_v061_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_jerk_126d_3d_v062_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_jerk_21d_3d_v063_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_jerk_63d_3d_v064_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_jerk_126d_3d_v065_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_share
def f041tng_f041_tangible_assets_intang_share_jerk_21d_3d_v066_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_share
def f041tng_f041_tangible_assets_intang_share_jerk_63d_3d_v067_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_share
def f041tng_f041_tangible_assets_intang_share_jerk_126d_3d_v068_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_jerk_21d_3d_v069_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_jerk_63d_3d_v070_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_jerk_126d_3d_v071_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_jerk_21d_3d_v072_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_jerk_63d_3d_v073_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_jerk_126d_3d_v074_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_jerk_21d_3d_v075_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_jerk_63d_3d_v076_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_jerk_126d_3d_v077_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tang_lvl smoothed over 252d
def f041tng_f041_tangible_assets_tang_lvl_smoothaccel_63d_sm252_3d_v078_signal(tangibles, closeadj):
    base = tangibles
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tang_lvl smoothed over 504d
def f041tng_f041_tangible_assets_tang_lvl_smoothaccel_252d_sm504_3d_v079_signal(tangibles, closeadj):
    base = tangibles
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tang_to_asset smoothed over 252d
def f041tng_f041_tangible_assets_tang_to_asset_smoothaccel_63d_sm252_3d_v080_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tang_to_asset smoothed over 504d
def f041tng_f041_tangible_assets_tang_to_asset_smoothaccel_252d_sm504_3d_v081_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tang_per_share smoothed over 252d
def f041tng_f041_tangible_assets_tang_per_share_smoothaccel_63d_sm252_3d_v082_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tang_per_share smoothed over 504d
def f041tng_f041_tangible_assets_tang_per_share_smoothaccel_252d_sm504_3d_v083_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_share smoothed over 252d
def f041tng_f041_tangible_assets_intang_share_smoothaccel_63d_sm252_3d_v084_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_share smoothed over 504d
def f041tng_f041_tangible_assets_intang_share_smoothaccel_252d_sm504_3d_v085_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tang_to_equity smoothed over 252d
def f041tng_f041_tangible_assets_tang_to_equity_smoothaccel_63d_sm252_3d_v086_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tang_to_equity smoothed over 504d
def f041tng_f041_tangible_assets_tang_to_equity_smoothaccel_252d_sm504_3d_v087_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tbvps_lvl smoothed over 252d
def f041tng_f041_tangible_assets_tbvps_lvl_smoothaccel_63d_sm252_3d_v088_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tbvps_lvl smoothed over 504d
def f041tng_f041_tangible_assets_tbvps_lvl_smoothaccel_252d_sm504_3d_v089_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of tang_minus_intang smoothed over 252d
def f041tng_f041_tangible_assets_tang_minus_intang_smoothaccel_63d_sm252_3d_v090_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of tang_minus_intang smoothed over 504d
def f041tng_f041_tangible_assets_tang_minus_intang_smoothaccel_252d_sm504_3d_v091_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_accelz_21d_z252_3d_v092_signal(tangibles, closeadj):
    base = tangibles
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_accelz_63d_z504_3d_v093_signal(tangibles, closeadj):
    base = tangibles
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_accelz_21d_z252_3d_v094_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_accelz_63d_z504_3d_v095_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_accelz_21d_z252_3d_v096_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_accelz_63d_z504_3d_v097_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_share
def f041tng_f041_tangible_assets_intang_share_accelz_21d_z252_3d_v098_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_share
def f041tng_f041_tangible_assets_intang_share_accelz_63d_z504_3d_v099_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_accelz_21d_z252_3d_v100_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_accelz_63d_z504_3d_v101_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_accelz_21d_z252_3d_v102_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_accelz_63d_z504_3d_v103_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_accelz_21d_z252_3d_v104_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_accelz_63d_z504_3d_v105_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tang_lvl (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_lvl_signflip_63d_3d_v106_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tang_lvl (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_lvl_signflip_252d_3d_v107_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tang_to_asset (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_to_asset_signflip_63d_3d_v108_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tang_to_asset (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_to_asset_signflip_252d_3d_v109_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tang_per_share (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_per_share_signflip_63d_3d_v110_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tang_per_share (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_per_share_signflip_252d_3d_v111_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_share (raw count, no price scaling)
def f041tng_f041_tangible_assets_intang_share_signflip_63d_3d_v112_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_share (raw count, no price scaling)
def f041tng_f041_tangible_assets_intang_share_signflip_252d_3d_v113_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tang_to_equity (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_to_equity_signflip_63d_3d_v114_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tang_to_equity (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_to_equity_signflip_252d_3d_v115_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tbvps_lvl (raw count, no price scaling)
def f041tng_f041_tangible_assets_tbvps_lvl_signflip_63d_3d_v116_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tbvps_lvl (raw count, no price scaling)
def f041tng_f041_tangible_assets_tbvps_lvl_signflip_252d_3d_v117_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in tang_minus_intang (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_minus_intang_signflip_63d_3d_v118_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in tang_minus_intang (raw count, no price scaling)
def f041tng_f041_tangible_assets_tang_minus_intang_signflip_252d_3d_v119_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_lvl normalized by 252d range
def f041tng_f041_tangible_assets_tang_lvl_rngaccel_63d_r252_3d_v120_signal(tangibles, closeadj):
    base = tangibles
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_lvl normalized by 504d range
def f041tng_f041_tangible_assets_tang_lvl_rngaccel_252d_r504_3d_v121_signal(tangibles, closeadj):
    base = tangibles
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_to_asset normalized by 252d range
def f041tng_f041_tangible_assets_tang_to_asset_rngaccel_63d_r252_3d_v122_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_to_asset normalized by 504d range
def f041tng_f041_tangible_assets_tang_to_asset_rngaccel_252d_r504_3d_v123_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_per_share normalized by 252d range
def f041tng_f041_tangible_assets_tang_per_share_rngaccel_63d_r252_3d_v124_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_per_share normalized by 504d range
def f041tng_f041_tangible_assets_tang_per_share_rngaccel_252d_r504_3d_v125_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_share normalized by 252d range
def f041tng_f041_tangible_assets_intang_share_rngaccel_63d_r252_3d_v126_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_share normalized by 504d range
def f041tng_f041_tangible_assets_intang_share_rngaccel_252d_r504_3d_v127_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_to_equity normalized by 252d range
def f041tng_f041_tangible_assets_tang_to_equity_rngaccel_63d_r252_3d_v128_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_to_equity normalized by 504d range
def f041tng_f041_tangible_assets_tang_to_equity_rngaccel_252d_r504_3d_v129_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tbvps_lvl normalized by 252d range
def f041tng_f041_tangible_assets_tbvps_lvl_rngaccel_63d_r252_3d_v130_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tbvps_lvl normalized by 504d range
def f041tng_f041_tangible_assets_tbvps_lvl_rngaccel_252d_r504_3d_v131_signal(tbvps, closeadj):
    base = tbvps
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of tang_minus_intang normalized by 252d range
def f041tng_f041_tangible_assets_tang_minus_intang_rngaccel_63d_r252_3d_v132_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of tang_minus_intang normalized by 504d range
def f041tng_f041_tangible_assets_tang_minus_intang_rngaccel_252d_r504_3d_v133_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_cumslope_21d_3d_v134_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_cumslope_63d_3d_v135_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_cumslope_252d_3d_v136_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_cumslope_21d_3d_v137_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_cumslope_63d_3d_v138_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_cumslope_252d_3d_v139_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_cumslope_21d_3d_v140_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_cumslope_63d_3d_v141_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_cumslope_252d_3d_v142_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_share
def f041tng_f041_tangible_assets_intang_share_cumslope_21d_3d_v143_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_share
def f041tng_f041_tangible_assets_intang_share_cumslope_63d_3d_v144_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_share
def f041tng_f041_tangible_assets_intang_share_cumslope_252d_3d_v145_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_cumslope_21d_3d_v146_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_cumslope_63d_3d_v147_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_cumslope_252d_3d_v148_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_cumslope_21d_3d_v149_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_cumslope_63d_3d_v150_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

