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


# 21d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slope_21d_2d_v001_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slope_63d_2d_v002_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slope_126d_2d_v003_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slope_252d_2d_v004_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_slope_504d_2d_v005_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slope_21d_2d_v006_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slope_63d_2d_v007_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slope_126d_2d_v008_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slope_252d_2d_v009_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_slope_504d_2d_v010_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slope_21d_2d_v011_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slope_63d_2d_v012_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slope_126d_2d_v013_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slope_252d_2d_v014_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_slope_504d_2d_v015_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_slope_21d_2d_v016_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_slope_63d_2d_v017_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_slope_126d_2d_v018_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_slope_252d_2d_v019_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_slope_504d_2d_v020_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slope_21d_2d_v021_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slope_63d_2d_v022_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slope_126d_2d_v023_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slope_252d_2d_v024_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_slope_504d_2d_v025_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slope_21d_2d_v026_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slope_63d_2d_v027_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slope_126d_2d_v028_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slope_252d_2d_v029_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_slope_504d_2d_v030_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slope_21d_2d_v031_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slope_63d_2d_v032_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slope_126d_2d_v033_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slope_252d_2d_v034_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_slope_504d_2d_v035_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sm21_sl21_2d_v036_signal(tangibles, closeadj):
    base = _mean(tangibles, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sm63_sl21_2d_v037_signal(tangibles, closeadj):
    base = _mean(tangibles, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sm63_sl63_2d_v038_signal(tangibles, closeadj):
    base = _mean(tangibles, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sm252_sl63_2d_v039_signal(tangibles, closeadj):
    base = _mean(tangibles, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sm252_sl126_2d_v040_signal(tangibles, closeadj):
    base = _mean(tangibles, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sm21_sl21_2d_v041_signal(tangibles, assets, closeadj):
    base = _mean(_f041_tang_share(tangibles, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sm63_sl21_2d_v042_signal(tangibles, assets, closeadj):
    base = _mean(_f041_tang_share(tangibles, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sm63_sl63_2d_v043_signal(tangibles, assets, closeadj):
    base = _mean(_f041_tang_share(tangibles, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sm252_sl63_2d_v044_signal(tangibles, assets, closeadj):
    base = _mean(_f041_tang_share(tangibles, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sm252_sl126_2d_v045_signal(tangibles, assets, closeadj):
    base = _mean(_f041_tang_share(tangibles, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sm21_sl21_2d_v046_signal(tangibles, sharesbas, closeadj):
    base = _mean(tangibles / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sm63_sl21_2d_v047_signal(tangibles, sharesbas, closeadj):
    base = _mean(tangibles / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sm63_sl63_2d_v048_signal(tangibles, sharesbas, closeadj):
    base = _mean(tangibles / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sm252_sl63_2d_v049_signal(tangibles, sharesbas, closeadj):
    base = _mean(tangibles / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sm252_sl126_2d_v050_signal(tangibles, sharesbas, closeadj):
    base = _mean(tangibles / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sm21_sl21_2d_v051_signal(intangibles, assets, closeadj):
    base = _mean(intangibles / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sm63_sl21_2d_v052_signal(intangibles, assets, closeadj):
    base = _mean(intangibles / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sm63_sl63_2d_v053_signal(intangibles, assets, closeadj):
    base = _mean(intangibles / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sm252_sl63_2d_v054_signal(intangibles, assets, closeadj):
    base = _mean(intangibles / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sm252_sl126_2d_v055_signal(intangibles, assets, closeadj):
    base = _mean(intangibles / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sm21_sl21_2d_v056_signal(tangibles, equity, closeadj):
    base = _mean(tangibles / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sm63_sl21_2d_v057_signal(tangibles, equity, closeadj):
    base = _mean(tangibles / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sm63_sl63_2d_v058_signal(tangibles, equity, closeadj):
    base = _mean(tangibles / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sm252_sl63_2d_v059_signal(tangibles, equity, closeadj):
    base = _mean(tangibles / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sm252_sl126_2d_v060_signal(tangibles, equity, closeadj):
    base = _mean(tangibles / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sm21_sl21_2d_v061_signal(tbvps, closeadj):
    base = _mean(tbvps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sm63_sl21_2d_v062_signal(tbvps, closeadj):
    base = _mean(tbvps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sm63_sl63_2d_v063_signal(tbvps, closeadj):
    base = _mean(tbvps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sm252_sl63_2d_v064_signal(tbvps, closeadj):
    base = _mean(tbvps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sm252_sl126_2d_v065_signal(tbvps, closeadj):
    base = _mean(tbvps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sm21_sl21_2d_v066_signal(tangibles, intangibles, closeadj):
    base = _mean(tangibles - intangibles, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sm63_sl21_2d_v067_signal(tangibles, intangibles, closeadj):
    base = _mean(tangibles - intangibles, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sm63_sl63_2d_v068_signal(tangibles, intangibles, closeadj):
    base = _mean(tangibles - intangibles, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sm252_sl63_2d_v069_signal(tangibles, intangibles, closeadj):
    base = _mean(tangibles - intangibles, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sm252_sl126_2d_v070_signal(tangibles, intangibles, closeadj):
    base = _mean(tangibles - intangibles, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_pctslope_21d_2d_v071_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_pctslope_63d_2d_v072_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_pctslope_252d_2d_v073_signal(tangibles, closeadj):
    base = tangibles
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_pctslope_21d_2d_v074_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_pctslope_63d_2d_v075_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_pctslope_252d_2d_v076_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_pctslope_21d_2d_v077_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_pctslope_63d_2d_v078_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_pctslope_252d_2d_v079_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_share
def f041tng_f041_tangible_assets_intang_share_pctslope_21d_2d_v080_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_share
def f041tng_f041_tangible_assets_intang_share_pctslope_63d_2d_v081_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_share
def f041tng_f041_tangible_assets_intang_share_pctslope_252d_2d_v082_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_pctslope_21d_2d_v083_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_pctslope_63d_2d_v084_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_pctslope_252d_2d_v085_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_pctslope_21d_2d_v086_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_pctslope_63d_2d_v087_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_pctslope_252d_2d_v088_signal(tbvps, closeadj):
    base = tbvps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_pctslope_21d_2d_v089_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_pctslope_63d_2d_v090_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_pctslope_252d_2d_v091_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sgnslope_21d_2d_v092_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sgnslope_63d_2d_v093_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_sgnslope_252d_2d_v094_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sgnslope_21d_2d_v095_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sgnslope_63d_2d_v096_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_sgnslope_252d_2d_v097_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sgnslope_21d_2d_v098_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sgnslope_63d_2d_v099_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_sgnslope_252d_2d_v100_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sgnslope_21d_2d_v101_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sgnslope_63d_2d_v102_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_sgnslope_252d_2d_v103_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sgnslope_21d_2d_v104_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sgnslope_63d_2d_v105_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_sgnslope_252d_2d_v106_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sgnslope_21d_2d_v107_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sgnslope_63d_2d_v108_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_sgnslope_252d_2d_v109_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sgnslope_21d_2d_v110_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sgnslope_63d_2d_v111_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_sgnslope_252d_2d_v112_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_logmagslope_21d_2d_v113_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_logmagslope_63d_2d_v114_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_logmagslope_252d_2d_v115_signal(tangibles, closeadj):
    base = tangibles
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_logmagslope_21d_2d_v116_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_logmagslope_63d_2d_v117_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_logmagslope_252d_2d_v118_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_logmagslope_21d_2d_v119_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_logmagslope_63d_2d_v120_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_logmagslope_252d_2d_v121_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_logmagslope_21d_2d_v122_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_logmagslope_63d_2d_v123_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_share
def f041tng_f041_tangible_assets_intang_share_logmagslope_252d_2d_v124_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_logmagslope_21d_2d_v125_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_logmagslope_63d_2d_v126_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_logmagslope_252d_2d_v127_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_logmagslope_21d_2d_v128_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_logmagslope_63d_2d_v129_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_logmagslope_252d_2d_v130_signal(tbvps, closeadj):
    base = tbvps
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_logmagslope_21d_2d_v131_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_logmagslope_63d_2d_v132_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_logmagslope_252d_2d_v133_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tang_lvl|
def f041tng_f041_tangible_assets_tang_lvl_logslope_63d_2d_v134_signal(tangibles, closeadj):
    base = np.log((tangibles).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tang_lvl|
def f041tng_f041_tangible_assets_tang_lvl_logslope_252d_2d_v135_signal(tangibles, closeadj):
    base = np.log((tangibles).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tang_to_asset|
def f041tng_f041_tangible_assets_tang_to_asset_logslope_63d_2d_v136_signal(tangibles, assets, closeadj):
    base = np.log((_f041_tang_share(tangibles, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tang_to_asset|
def f041tng_f041_tangible_assets_tang_to_asset_logslope_252d_2d_v137_signal(tangibles, assets, closeadj):
    base = np.log((_f041_tang_share(tangibles, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tang_per_share|
def f041tng_f041_tangible_assets_tang_per_share_logslope_63d_2d_v138_signal(tangibles, sharesbas, closeadj):
    base = np.log((tangibles / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tang_per_share|
def f041tng_f041_tangible_assets_tang_per_share_logslope_252d_2d_v139_signal(tangibles, sharesbas, closeadj):
    base = np.log((tangibles / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_share|
def f041tng_f041_tangible_assets_intang_share_logslope_63d_2d_v140_signal(intangibles, assets, closeadj):
    base = np.log((intangibles / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_share|
def f041tng_f041_tangible_assets_intang_share_logslope_252d_2d_v141_signal(intangibles, assets, closeadj):
    base = np.log((intangibles / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tang_to_equity|
def f041tng_f041_tangible_assets_tang_to_equity_logslope_63d_2d_v142_signal(tangibles, equity, closeadj):
    base = np.log((tangibles / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tang_to_equity|
def f041tng_f041_tangible_assets_tang_to_equity_logslope_252d_2d_v143_signal(tangibles, equity, closeadj):
    base = np.log((tangibles / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tbvps_lvl|
def f041tng_f041_tangible_assets_tbvps_lvl_logslope_63d_2d_v144_signal(tbvps, closeadj):
    base = np.log((tbvps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tbvps_lvl|
def f041tng_f041_tangible_assets_tbvps_lvl_logslope_252d_2d_v145_signal(tbvps, closeadj):
    base = np.log((tbvps).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|tang_minus_intang|
def f041tng_f041_tangible_assets_tang_minus_intang_logslope_63d_2d_v146_signal(tangibles, intangibles, closeadj):
    base = np.log((tangibles - intangibles).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|tang_minus_intang|
def f041tng_f041_tangible_assets_tang_minus_intang_logslope_252d_2d_v147_signal(tangibles, intangibles, closeadj):
    base = np.log((tangibles - intangibles).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

