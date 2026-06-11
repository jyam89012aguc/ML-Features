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
def _f066_at(revenue, assetsavg):
    return revenue / assetsavg.replace(0, np.nan).abs()


# 21d mean of asset_turnover_lvl scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_lvl_mean_21d_base_v001_signal(assetturnover, closeadj):
    base = assetturnover
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of asset_turnover_lvl scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_lvl_mean_63d_base_v002_signal(assetturnover, closeadj):
    base = assetturnover
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of asset_turnover_lvl scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_lvl_mean_126d_base_v003_signal(assetturnover, closeadj):
    base = assetturnover
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of asset_turnover_lvl scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_lvl_mean_252d_base_v004_signal(assetturnover, closeadj):
    base = assetturnover
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of asset_turnover_lvl scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_lvl_mean_504d_base_v005_signal(assetturnover, closeadj):
    base = assetturnover
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of asset_turnover_calc scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_calc_mean_21d_base_v006_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of asset_turnover_calc scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_calc_mean_63d_base_v007_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of asset_turnover_calc scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_calc_mean_126d_base_v008_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of asset_turnover_calc scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_calc_mean_252d_base_v009_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of asset_turnover_calc scaled by closeadj
def f066ato_f066_asset_turnover_asset_turnover_calc_mean_504d_base_v010_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of at_yoy_chg scaled by closeadj
def f066ato_f066_asset_turnover_at_yoy_chg_mean_21d_base_v011_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of at_yoy_chg scaled by closeadj
def f066ato_f066_asset_turnover_at_yoy_chg_mean_63d_base_v012_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of at_yoy_chg scaled by closeadj
def f066ato_f066_asset_turnover_at_yoy_chg_mean_126d_base_v013_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of at_yoy_chg scaled by closeadj
def f066ato_f066_asset_turnover_at_yoy_chg_mean_252d_base_v014_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of at_yoy_chg scaled by closeadj
def f066ato_f066_asset_turnover_at_yoy_chg_mean_504d_base_v015_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_to_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_to_asset_mean_21d_base_v016_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_to_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_to_asset_mean_63d_base_v017_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_to_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_to_asset_mean_126d_base_v018_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_to_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_to_asset_mean_252d_base_v019_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_to_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_to_asset_mean_504d_base_v020_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of at_vol_252 scaled by closeadj
def f066ato_f066_asset_turnover_at_vol_252_mean_21d_base_v021_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of at_vol_252 scaled by closeadj
def f066ato_f066_asset_turnover_at_vol_252_mean_63d_base_v022_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of at_vol_252 scaled by closeadj
def f066ato_f066_asset_turnover_at_vol_252_mean_126d_base_v023_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of at_vol_252 scaled by closeadj
def f066ato_f066_asset_turnover_at_vol_252_mean_252d_base_v024_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of at_vol_252 scaled by closeadj
def f066ato_f066_asset_turnover_at_vol_252_mean_504d_base_v025_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_per_curr_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_curr_asset_mean_21d_base_v026_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_per_curr_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_curr_asset_mean_63d_base_v027_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_per_curr_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_curr_asset_mean_126d_base_v028_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_per_curr_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_curr_asset_mean_252d_base_v029_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_per_curr_asset scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_curr_asset_mean_504d_base_v030_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_per_ppne scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_ppne_mean_21d_base_v031_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_per_ppne scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_ppne_mean_63d_base_v032_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_per_ppne scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_ppne_mean_126d_base_v033_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_per_ppne scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_ppne_mean_252d_base_v034_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_per_ppne scaled by closeadj
def f066ato_f066_asset_turnover_rev_per_ppne_mean_504d_base_v035_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_median_63d_base_v036_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_median_252d_base_v037_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_median_504d_base_v038_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_median_63d_base_v039_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_median_252d_base_v040_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_median_504d_base_v041_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_median_63d_base_v042_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_median_252d_base_v043_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_median_504d_base_v044_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_median_63d_base_v045_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_median_252d_base_v046_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_median_504d_base_v047_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_median_63d_base_v048_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_median_252d_base_v049_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_median_504d_base_v050_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_median_63d_base_v051_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_median_252d_base_v052_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_median_504d_base_v053_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_median_63d_base_v054_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_median_252d_base_v055_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_median_504d_base_v056_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_rmax_252d_base_v057_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_rmax_504d_base_v058_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_rmax_252d_base_v059_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_rmax_504d_base_v060_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_rmax_252d_base_v061_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_rmax_504d_base_v062_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_rmax_252d_base_v063_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_rmax_504d_base_v064_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_rmax_252d_base_v065_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_rmax_504d_base_v066_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_rmax_252d_base_v067_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_rmax_504d_base_v068_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_rmax_252d_base_v069_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_rmax_504d_base_v070_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_rmin_252d_base_v071_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_rmin_504d_base_v072_signal(assetturnover, closeadj):
    base = assetturnover
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_rmin_252d_base_v073_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_rmin_504d_base_v074_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_rmin_252d_base_v075_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

