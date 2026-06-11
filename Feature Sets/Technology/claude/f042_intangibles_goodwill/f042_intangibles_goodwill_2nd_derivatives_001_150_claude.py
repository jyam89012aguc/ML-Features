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
def _f042_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan).abs()


# 21d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slope_21d_2d_v001_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slope_63d_2d_v002_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slope_126d_2d_v003_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slope_252d_2d_v004_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_slope_504d_2d_v005_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slope_21d_2d_v006_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slope_63d_2d_v007_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slope_126d_2d_v008_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slope_252d_2d_v009_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_slope_504d_2d_v010_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slope_21d_2d_v011_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slope_63d_2d_v012_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slope_126d_2d_v013_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slope_252d_2d_v014_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_slope_504d_2d_v015_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slope_21d_2d_v016_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slope_63d_2d_v017_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slope_126d_2d_v018_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slope_252d_2d_v019_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_slope_504d_2d_v020_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slope_21d_2d_v021_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slope_63d_2d_v022_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slope_126d_2d_v023_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slope_252d_2d_v024_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_slope_504d_2d_v025_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slope_21d_2d_v026_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slope_63d_2d_v027_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slope_126d_2d_v028_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slope_252d_2d_v029_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_slope_504d_2d_v030_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slope_21d_2d_v031_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slope_63d_2d_v032_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slope_126d_2d_v033_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slope_252d_2d_v034_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_slope_504d_2d_v035_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sm21_sl21_2d_v036_signal(intangibles, closeadj):
    base = _mean(intangibles, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sm63_sl21_2d_v037_signal(intangibles, closeadj):
    base = _mean(intangibles, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sm63_sl63_2d_v038_signal(intangibles, closeadj):
    base = _mean(intangibles, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sm252_sl63_2d_v039_signal(intangibles, closeadj):
    base = _mean(intangibles, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sm252_sl126_2d_v040_signal(intangibles, closeadj):
    base = _mean(intangibles, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sm21_sl21_2d_v041_signal(intangibles, assets, closeadj):
    base = _mean(_f042_intang_share(intangibles, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sm63_sl21_2d_v042_signal(intangibles, assets, closeadj):
    base = _mean(_f042_intang_share(intangibles, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sm63_sl63_2d_v043_signal(intangibles, assets, closeadj):
    base = _mean(_f042_intang_share(intangibles, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sm252_sl63_2d_v044_signal(intangibles, assets, closeadj):
    base = _mean(_f042_intang_share(intangibles, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sm252_sl126_2d_v045_signal(intangibles, assets, closeadj):
    base = _mean(_f042_intang_share(intangibles, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sm21_sl21_2d_v046_signal(intangibles, equity, closeadj):
    base = _mean(intangibles / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sm63_sl21_2d_v047_signal(intangibles, equity, closeadj):
    base = _mean(intangibles / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sm63_sl63_2d_v048_signal(intangibles, equity, closeadj):
    base = _mean(intangibles / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sm252_sl63_2d_v049_signal(intangibles, equity, closeadj):
    base = _mean(intangibles / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sm252_sl126_2d_v050_signal(intangibles, equity, closeadj):
    base = _mean(intangibles / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sm21_sl21_2d_v051_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sm63_sl21_2d_v052_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sm63_sl63_2d_v053_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sm252_sl63_2d_v054_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sm252_sl126_2d_v055_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sm21_sl21_2d_v056_signal(intangibles, sharesbas, closeadj):
    base = _mean(intangibles / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sm63_sl21_2d_v057_signal(intangibles, sharesbas, closeadj):
    base = _mean(intangibles / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sm63_sl63_2d_v058_signal(intangibles, sharesbas, closeadj):
    base = _mean(intangibles / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sm252_sl63_2d_v059_signal(intangibles, sharesbas, closeadj):
    base = _mean(intangibles / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sm252_sl126_2d_v060_signal(intangibles, sharesbas, closeadj):
    base = _mean(intangibles / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sm21_sl21_2d_v061_signal(intangibles, closeadj):
    base = _mean(intangibles.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sm63_sl21_2d_v062_signal(intangibles, closeadj):
    base = _mean(intangibles.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sm63_sl63_2d_v063_signal(intangibles, closeadj):
    base = _mean(intangibles.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sm252_sl63_2d_v064_signal(intangibles, closeadj):
    base = _mean(intangibles.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sm252_sl126_2d_v065_signal(intangibles, closeadj):
    base = _mean(intangibles.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sm21_sl21_2d_v066_signal(intangibles, marketcap, closeadj):
    base = _mean(intangibles / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sm63_sl21_2d_v067_signal(intangibles, marketcap, closeadj):
    base = _mean(intangibles / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sm63_sl63_2d_v068_signal(intangibles, marketcap, closeadj):
    base = _mean(intangibles / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sm252_sl63_2d_v069_signal(intangibles, marketcap, closeadj):
    base = _mean(intangibles / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sm252_sl126_2d_v070_signal(intangibles, marketcap, closeadj):
    base = _mean(intangibles / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_pctslope_21d_2d_v071_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_pctslope_63d_2d_v072_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_pctslope_252d_2d_v073_signal(intangibles, closeadj):
    base = intangibles
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_pctslope_21d_2d_v074_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_pctslope_63d_2d_v075_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_pctslope_252d_2d_v076_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_pctslope_21d_2d_v077_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_pctslope_63d_2d_v078_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_pctslope_252d_2d_v079_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_pctslope_21d_2d_v080_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_pctslope_63d_2d_v081_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_pctslope_252d_2d_v082_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_pctslope_21d_2d_v083_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_pctslope_63d_2d_v084_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_pctslope_252d_2d_v085_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_pctslope_21d_2d_v086_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_pctslope_63d_2d_v087_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_pctslope_252d_2d_v088_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_pctslope_21d_2d_v089_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_pctslope_63d_2d_v090_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_pctslope_252d_2d_v091_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sgnslope_21d_2d_v092_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sgnslope_63d_2d_v093_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_sgnslope_252d_2d_v094_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sgnslope_21d_2d_v095_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sgnslope_63d_2d_v096_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_sgnslope_252d_2d_v097_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sgnslope_21d_2d_v098_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sgnslope_63d_2d_v099_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_sgnslope_252d_2d_v100_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sgnslope_21d_2d_v101_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sgnslope_63d_2d_v102_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_sgnslope_252d_2d_v103_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sgnslope_21d_2d_v104_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sgnslope_63d_2d_v105_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_sgnslope_252d_2d_v106_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sgnslope_21d_2d_v107_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sgnslope_63d_2d_v108_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_sgnslope_252d_2d_v109_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sgnslope_21d_2d_v110_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sgnslope_63d_2d_v111_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_sgnslope_252d_2d_v112_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_logmagslope_21d_2d_v113_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_logmagslope_63d_2d_v114_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_lvl
def f042itg_f042_intangibles_goodwill_intang_lvl_logmagslope_252d_2d_v115_signal(intangibles, closeadj):
    base = intangibles
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_logmagslope_21d_2d_v116_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_logmagslope_63d_2d_v117_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_to_asset
def f042itg_f042_intangibles_goodwill_intang_to_asset_logmagslope_252d_2d_v118_signal(intangibles, assets, closeadj):
    base = _f042_intang_share(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_logmagslope_21d_2d_v119_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_logmagslope_63d_2d_v120_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_to_equity
def f042itg_f042_intangibles_goodwill_intang_to_equity_logmagslope_252d_2d_v121_signal(intangibles, equity, closeadj):
    base = intangibles / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_logmagslope_21d_2d_v122_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_logmagslope_63d_2d_v123_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of amort_to_intang
def f042itg_f042_intangibles_goodwill_amort_to_intang_logmagslope_252d_2d_v124_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_logmagslope_21d_2d_v125_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_logmagslope_63d_2d_v126_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_per_share
def f042itg_f042_intangibles_goodwill_intang_per_share_logmagslope_252d_2d_v127_signal(intangibles, sharesbas, closeadj):
    base = intangibles / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_logmagslope_21d_2d_v128_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_logmagslope_63d_2d_v129_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_yoy
def f042itg_f042_intangibles_goodwill_intang_yoy_logmagslope_252d_2d_v130_signal(intangibles, closeadj):
    base = intangibles.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_logmagslope_21d_2d_v131_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_logmagslope_63d_2d_v132_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_to_mcap
def f042itg_f042_intangibles_goodwill_intang_to_mcap_logmagslope_252d_2d_v133_signal(intangibles, marketcap, closeadj):
    base = intangibles / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_lvl|
def f042itg_f042_intangibles_goodwill_intang_lvl_logslope_63d_2d_v134_signal(intangibles, closeadj):
    base = np.log((intangibles).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_lvl|
def f042itg_f042_intangibles_goodwill_intang_lvl_logslope_252d_2d_v135_signal(intangibles, closeadj):
    base = np.log((intangibles).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_to_asset|
def f042itg_f042_intangibles_goodwill_intang_to_asset_logslope_63d_2d_v136_signal(intangibles, assets, closeadj):
    base = np.log((_f042_intang_share(intangibles, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_to_asset|
def f042itg_f042_intangibles_goodwill_intang_to_asset_logslope_252d_2d_v137_signal(intangibles, assets, closeadj):
    base = np.log((_f042_intang_share(intangibles, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_to_equity|
def f042itg_f042_intangibles_goodwill_intang_to_equity_logslope_63d_2d_v138_signal(intangibles, equity, closeadj):
    base = np.log((intangibles / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_to_equity|
def f042itg_f042_intangibles_goodwill_intang_to_equity_logslope_252d_2d_v139_signal(intangibles, equity, closeadj):
    base = np.log((intangibles / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|amort_to_intang|
def f042itg_f042_intangibles_goodwill_amort_to_intang_logslope_63d_2d_v140_signal(depamor, intangibles, closeadj):
    base = np.log((depamor / intangibles.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|amort_to_intang|
def f042itg_f042_intangibles_goodwill_amort_to_intang_logslope_252d_2d_v141_signal(depamor, intangibles, closeadj):
    base = np.log((depamor / intangibles.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_per_share|
def f042itg_f042_intangibles_goodwill_intang_per_share_logslope_63d_2d_v142_signal(intangibles, sharesbas, closeadj):
    base = np.log((intangibles / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_per_share|
def f042itg_f042_intangibles_goodwill_intang_per_share_logslope_252d_2d_v143_signal(intangibles, sharesbas, closeadj):
    base = np.log((intangibles / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_yoy|
def f042itg_f042_intangibles_goodwill_intang_yoy_logslope_63d_2d_v144_signal(intangibles, closeadj):
    base = np.log((intangibles.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_yoy|
def f042itg_f042_intangibles_goodwill_intang_yoy_logslope_252d_2d_v145_signal(intangibles, closeadj):
    base = np.log((intangibles.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_to_mcap|
def f042itg_f042_intangibles_goodwill_intang_to_mcap_logslope_63d_2d_v146_signal(intangibles, marketcap, closeadj):
    base = np.log((intangibles / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_to_mcap|
def f042itg_f042_intangibles_goodwill_intang_to_mcap_logslope_252d_2d_v147_signal(intangibles, marketcap, closeadj):
    base = np.log((intangibles / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

