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


# 21d mean of tang_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tang_lvl_mean_21d_base_v001_signal(tangibles, closeadj):
    base = tangibles
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tang_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tang_lvl_mean_63d_base_v002_signal(tangibles, closeadj):
    base = tangibles
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tang_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tang_lvl_mean_126d_base_v003_signal(tangibles, closeadj):
    base = tangibles
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tang_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tang_lvl_mean_252d_base_v004_signal(tangibles, closeadj):
    base = tangibles
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tang_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tang_lvl_mean_504d_base_v005_signal(tangibles, closeadj):
    base = tangibles
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tang_to_asset scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_asset_mean_21d_base_v006_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tang_to_asset scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_asset_mean_63d_base_v007_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tang_to_asset scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_asset_mean_126d_base_v008_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tang_to_asset scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_asset_mean_252d_base_v009_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tang_to_asset scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_asset_mean_504d_base_v010_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tang_per_share scaled by closeadj
def f041tng_f041_tangible_assets_tang_per_share_mean_21d_base_v011_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tang_per_share scaled by closeadj
def f041tng_f041_tangible_assets_tang_per_share_mean_63d_base_v012_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tang_per_share scaled by closeadj
def f041tng_f041_tangible_assets_tang_per_share_mean_126d_base_v013_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tang_per_share scaled by closeadj
def f041tng_f041_tangible_assets_tang_per_share_mean_252d_base_v014_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tang_per_share scaled by closeadj
def f041tng_f041_tangible_assets_tang_per_share_mean_504d_base_v015_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intang_share scaled by closeadj
def f041tng_f041_tangible_assets_intang_share_mean_21d_base_v016_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intang_share scaled by closeadj
def f041tng_f041_tangible_assets_intang_share_mean_63d_base_v017_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intang_share scaled by closeadj
def f041tng_f041_tangible_assets_intang_share_mean_126d_base_v018_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intang_share scaled by closeadj
def f041tng_f041_tangible_assets_intang_share_mean_252d_base_v019_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intang_share scaled by closeadj
def f041tng_f041_tangible_assets_intang_share_mean_504d_base_v020_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tang_to_equity scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_equity_mean_21d_base_v021_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tang_to_equity scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_equity_mean_63d_base_v022_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tang_to_equity scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_equity_mean_126d_base_v023_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tang_to_equity scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_equity_mean_252d_base_v024_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tang_to_equity scaled by closeadj
def f041tng_f041_tangible_assets_tang_to_equity_mean_504d_base_v025_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tbvps_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tbvps_lvl_mean_21d_base_v026_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tbvps_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tbvps_lvl_mean_63d_base_v027_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tbvps_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tbvps_lvl_mean_126d_base_v028_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tbvps_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tbvps_lvl_mean_252d_base_v029_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tbvps_lvl scaled by closeadj
def f041tng_f041_tangible_assets_tbvps_lvl_mean_504d_base_v030_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tang_minus_intang scaled by closeadj
def f041tng_f041_tangible_assets_tang_minus_intang_mean_21d_base_v031_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tang_minus_intang scaled by closeadj
def f041tng_f041_tangible_assets_tang_minus_intang_mean_63d_base_v032_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tang_minus_intang scaled by closeadj
def f041tng_f041_tangible_assets_tang_minus_intang_mean_126d_base_v033_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tang_minus_intang scaled by closeadj
def f041tng_f041_tangible_assets_tang_minus_intang_mean_252d_base_v034_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tang_minus_intang scaled by closeadj
def f041tng_f041_tangible_assets_tang_minus_intang_mean_504d_base_v035_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_median_63d_base_v036_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_median_252d_base_v037_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_median_504d_base_v038_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_median_63d_base_v039_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_median_252d_base_v040_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_median_504d_base_v041_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_median_63d_base_v042_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_median_252d_base_v043_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_median_504d_base_v044_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intang_share
def f041tng_f041_tangible_assets_intang_share_median_63d_base_v045_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intang_share
def f041tng_f041_tangible_assets_intang_share_median_252d_base_v046_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intang_share
def f041tng_f041_tangible_assets_intang_share_median_504d_base_v047_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_median_63d_base_v048_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_median_252d_base_v049_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_median_504d_base_v050_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_median_63d_base_v051_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_median_252d_base_v052_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_median_504d_base_v053_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_median_63d_base_v054_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_median_252d_base_v055_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_median_504d_base_v056_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_rmax_252d_base_v057_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_rmax_504d_base_v058_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_rmax_252d_base_v059_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_rmax_504d_base_v060_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_rmax_252d_base_v061_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_rmax_504d_base_v062_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intang_share
def f041tng_f041_tangible_assets_intang_share_rmax_252d_base_v063_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intang_share
def f041tng_f041_tangible_assets_intang_share_rmax_504d_base_v064_signal(intangibles, assets, closeadj):
    base = intangibles / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_rmax_252d_base_v065_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tang_to_equity
def f041tng_f041_tangible_assets_tang_to_equity_rmax_504d_base_v066_signal(tangibles, equity, closeadj):
    base = tangibles / equity.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_rmax_252d_base_v067_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tbvps_lvl
def f041tng_f041_tangible_assets_tbvps_lvl_rmax_504d_base_v068_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_rmax_252d_base_v069_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of tang_minus_intang
def f041tng_f041_tangible_assets_tang_minus_intang_rmax_504d_base_v070_signal(tangibles, intangibles, closeadj):
    base = tangibles - intangibles
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_rmin_252d_base_v071_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of tang_lvl
def f041tng_f041_tangible_assets_tang_lvl_rmin_504d_base_v072_signal(tangibles, closeadj):
    base = tangibles
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_rmin_252d_base_v073_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of tang_to_asset
def f041tng_f041_tangible_assets_tang_to_asset_rmin_504d_base_v074_signal(tangibles, assets, closeadj):
    base = _f041_tang_share(tangibles, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of tang_per_share
def f041tng_f041_tangible_assets_tang_per_share_rmin_252d_base_v075_signal(tangibles, sharesbas, closeadj):
    base = tangibles / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

