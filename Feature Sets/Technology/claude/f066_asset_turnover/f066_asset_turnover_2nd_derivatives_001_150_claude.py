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
def _f066_at(revenue, assetsavg):
    return revenue / assetsavg.replace(0, np.nan).abs()


# 21d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slope_21d_2d_v001_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slope_63d_2d_v002_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slope_126d_2d_v003_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slope_252d_2d_v004_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slope_504d_2d_v005_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slope_21d_2d_v006_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slope_63d_2d_v007_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slope_126d_2d_v008_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slope_252d_2d_v009_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slope_504d_2d_v010_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slope_21d_2d_v011_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slope_63d_2d_v012_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slope_126d_2d_v013_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slope_252d_2d_v014_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slope_504d_2d_v015_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slope_21d_2d_v016_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slope_63d_2d_v017_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slope_126d_2d_v018_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slope_252d_2d_v019_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slope_504d_2d_v020_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slope_21d_2d_v021_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slope_63d_2d_v022_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slope_126d_2d_v023_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slope_252d_2d_v024_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slope_504d_2d_v025_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slope_21d_2d_v026_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slope_63d_2d_v027_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slope_126d_2d_v028_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slope_252d_2d_v029_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slope_504d_2d_v030_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slope_21d_2d_v031_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slope_63d_2d_v032_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slope_126d_2d_v033_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slope_252d_2d_v034_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slope_504d_2d_v035_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sm21_sl21_2d_v036_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sm63_sl21_2d_v037_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sm63_sl63_2d_v038_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sm252_sl63_2d_v039_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sm252_sl126_2d_v040_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sm21_sl21_2d_v041_signal(revenue, assetsavg, closeadj):
    base = _mean(_f066_at(revenue, assetsavg), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sm63_sl21_2d_v042_signal(revenue, assetsavg, closeadj):
    base = _mean(_f066_at(revenue, assetsavg), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sm63_sl63_2d_v043_signal(revenue, assetsavg, closeadj):
    base = _mean(_f066_at(revenue, assetsavg), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sm252_sl63_2d_v044_signal(revenue, assetsavg, closeadj):
    base = _mean(_f066_at(revenue, assetsavg), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sm252_sl126_2d_v045_signal(revenue, assetsavg, closeadj):
    base = _mean(_f066_at(revenue, assetsavg), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sm21_sl21_2d_v046_signal(assetturnover, closeadj):
    base = _mean(assetturnover.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sm63_sl21_2d_v047_signal(assetturnover, closeadj):
    base = _mean(assetturnover.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sm63_sl63_2d_v048_signal(assetturnover, closeadj):
    base = _mean(assetturnover.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sm252_sl63_2d_v049_signal(assetturnover, closeadj):
    base = _mean(assetturnover.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sm252_sl126_2d_v050_signal(assetturnover, closeadj):
    base = _mean(assetturnover.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sm21_sl21_2d_v051_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sm63_sl21_2d_v052_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sm63_sl63_2d_v053_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sm252_sl63_2d_v054_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sm252_sl126_2d_v055_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sm21_sl21_2d_v056_signal(assetturnover, closeadj):
    base = _mean(assetturnover.rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sm63_sl21_2d_v057_signal(assetturnover, closeadj):
    base = _mean(assetturnover.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sm63_sl63_2d_v058_signal(assetturnover, closeadj):
    base = _mean(assetturnover.rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sm252_sl63_2d_v059_signal(assetturnover, closeadj):
    base = _mean(assetturnover.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sm252_sl126_2d_v060_signal(assetturnover, closeadj):
    base = _mean(assetturnover.rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sm21_sl21_2d_v061_signal(revenue, assetsc, closeadj):
    base = _mean(revenue / assetsc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sm63_sl21_2d_v062_signal(revenue, assetsc, closeadj):
    base = _mean(revenue / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sm63_sl63_2d_v063_signal(revenue, assetsc, closeadj):
    base = _mean(revenue / assetsc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sm252_sl63_2d_v064_signal(revenue, assetsc, closeadj):
    base = _mean(revenue / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sm252_sl126_2d_v065_signal(revenue, assetsc, closeadj):
    base = _mean(revenue / assetsc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sm21_sl21_2d_v066_signal(revenue, ppnenet, closeadj):
    base = _mean(revenue / ppnenet.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sm63_sl21_2d_v067_signal(revenue, ppnenet, closeadj):
    base = _mean(revenue / ppnenet.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sm63_sl63_2d_v068_signal(revenue, ppnenet, closeadj):
    base = _mean(revenue / ppnenet.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sm252_sl63_2d_v069_signal(revenue, ppnenet, closeadj):
    base = _mean(revenue / ppnenet.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sm252_sl126_2d_v070_signal(revenue, ppnenet, closeadj):
    base = _mean(revenue / ppnenet.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_pctslope_21d_2d_v071_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_pctslope_63d_2d_v072_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_pctslope_252d_2d_v073_signal(assetturnover, closeadj):
    base = assetturnover
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_pctslope_21d_2d_v074_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_pctslope_63d_2d_v075_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_pctslope_252d_2d_v076_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_pctslope_21d_2d_v077_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_pctslope_63d_2d_v078_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_pctslope_252d_2d_v079_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_pctslope_21d_2d_v080_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_pctslope_63d_2d_v081_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_pctslope_252d_2d_v082_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_pctslope_21d_2d_v083_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_pctslope_63d_2d_v084_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_pctslope_252d_2d_v085_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_pctslope_21d_2d_v086_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_pctslope_63d_2d_v087_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_pctslope_252d_2d_v088_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_pctslope_21d_2d_v089_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_pctslope_63d_2d_v090_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_pctslope_252d_2d_v091_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sgnslope_21d_2d_v092_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sgnslope_63d_2d_v093_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_sgnslope_252d_2d_v094_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sgnslope_21d_2d_v095_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sgnslope_63d_2d_v096_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_sgnslope_252d_2d_v097_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sgnslope_21d_2d_v098_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sgnslope_63d_2d_v099_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_sgnslope_252d_2d_v100_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sgnslope_21d_2d_v101_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sgnslope_63d_2d_v102_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_sgnslope_252d_2d_v103_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sgnslope_21d_2d_v104_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sgnslope_63d_2d_v105_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_sgnslope_252d_2d_v106_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sgnslope_21d_2d_v107_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sgnslope_63d_2d_v108_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_sgnslope_252d_2d_v109_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sgnslope_21d_2d_v110_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sgnslope_63d_2d_v111_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_sgnslope_252d_2d_v112_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_logmagslope_21d_2d_v113_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_logmagslope_63d_2d_v114_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_logmagslope_252d_2d_v115_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_logmagslope_21d_2d_v116_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_logmagslope_63d_2d_v117_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_logmagslope_252d_2d_v118_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_logmagslope_21d_2d_v119_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_logmagslope_63d_2d_v120_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_logmagslope_252d_2d_v121_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_logmagslope_21d_2d_v122_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_logmagslope_63d_2d_v123_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_logmagslope_252d_2d_v124_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_logmagslope_21d_2d_v125_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_logmagslope_63d_2d_v126_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_logmagslope_252d_2d_v127_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_logmagslope_21d_2d_v128_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_logmagslope_63d_2d_v129_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_logmagslope_252d_2d_v130_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_logmagslope_21d_2d_v131_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_logmagslope_63d_2d_v132_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_logmagslope_252d_2d_v133_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|asset_turnover_lvl|
def f066ato_f066_asset_turnover_asset_turnover_lvl_logslope_63d_2d_v134_signal(assetturnover, closeadj):
    base = np.log((assetturnover).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|asset_turnover_lvl|
def f066ato_f066_asset_turnover_asset_turnover_lvl_logslope_252d_2d_v135_signal(assetturnover, closeadj):
    base = np.log((assetturnover).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|asset_turnover_calc|
def f066ato_f066_asset_turnover_asset_turnover_calc_logslope_63d_2d_v136_signal(revenue, assetsavg, closeadj):
    base = np.log((_f066_at(revenue, assetsavg)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|asset_turnover_calc|
def f066ato_f066_asset_turnover_asset_turnover_calc_logslope_252d_2d_v137_signal(revenue, assetsavg, closeadj):
    base = np.log((_f066_at(revenue, assetsavg)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|at_yoy_chg|
def f066ato_f066_asset_turnover_at_yoy_chg_logslope_63d_2d_v138_signal(assetturnover, closeadj):
    base = np.log((assetturnover.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|at_yoy_chg|
def f066ato_f066_asset_turnover_at_yoy_chg_logslope_252d_2d_v139_signal(assetturnover, closeadj):
    base = np.log((assetturnover.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_to_asset|
def f066ato_f066_asset_turnover_rev_to_asset_logslope_63d_2d_v140_signal(revenue, assets, closeadj):
    base = np.log((revenue / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_to_asset|
def f066ato_f066_asset_turnover_rev_to_asset_logslope_252d_2d_v141_signal(revenue, assets, closeadj):
    base = np.log((revenue / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|at_vol_252|
def f066ato_f066_asset_turnover_at_vol_252_logslope_63d_2d_v142_signal(assetturnover, closeadj):
    base = np.log((assetturnover.rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|at_vol_252|
def f066ato_f066_asset_turnover_at_vol_252_logslope_252d_2d_v143_signal(assetturnover, closeadj):
    base = np.log((assetturnover.rolling(252, min_periods=63).std()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_per_curr_asset|
def f066ato_f066_asset_turnover_rev_per_curr_asset_logslope_63d_2d_v144_signal(revenue, assetsc, closeadj):
    base = np.log((revenue / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_per_curr_asset|
def f066ato_f066_asset_turnover_rev_per_curr_asset_logslope_252d_2d_v145_signal(revenue, assetsc, closeadj):
    base = np.log((revenue / assetsc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_per_ppne|
def f066ato_f066_asset_turnover_rev_per_ppne_logslope_63d_2d_v146_signal(revenue, ppnenet, closeadj):
    base = np.log((revenue / ppnenet.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_per_ppne|
def f066ato_f066_asset_turnover_rev_per_ppne_logslope_252d_2d_v147_signal(revenue, ppnenet, closeadj):
    base = np.log((revenue / ppnenet.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

