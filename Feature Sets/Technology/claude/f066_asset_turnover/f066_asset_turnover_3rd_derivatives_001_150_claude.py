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


# 21d acceleration of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_accel_21d_3d_v001_signal(assetturnover, closeadj):
    base = assetturnover
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_accel_63d_3d_v002_signal(assetturnover, closeadj):
    base = assetturnover
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_accel_126d_3d_v003_signal(assetturnover, closeadj):
    base = assetturnover
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_accel_252d_3d_v004_signal(assetturnover, closeadj):
    base = assetturnover
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_accel_21d_3d_v005_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_accel_63d_3d_v006_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_accel_126d_3d_v007_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_accel_252d_3d_v008_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_accel_21d_3d_v009_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_accel_63d_3d_v010_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_accel_126d_3d_v011_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_accel_252d_3d_v012_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_accel_21d_3d_v013_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_accel_63d_3d_v014_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_accel_126d_3d_v015_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_accel_252d_3d_v016_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_accel_21d_3d_v017_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_accel_63d_3d_v018_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_accel_126d_3d_v019_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_accel_252d_3d_v020_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_accel_21d_3d_v021_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_accel_63d_3d_v022_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_accel_126d_3d_v023_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_accel_252d_3d_v024_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_accel_21d_3d_v025_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_accel_63d_3d_v026_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_accel_126d_3d_v027_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_accel_252d_3d_v028_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slopez_21d_z126_3d_v029_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slopez_63d_z252_3d_v030_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slopez_126d_z252_3d_v031_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_slopez_252d_z504_3d_v032_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slopez_21d_z126_3d_v033_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slopez_63d_z252_3d_v034_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slopez_126d_z252_3d_v035_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_slopez_252d_z504_3d_v036_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slopez_21d_z126_3d_v037_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slopez_63d_z252_3d_v038_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slopez_126d_z252_3d_v039_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_slopez_252d_z504_3d_v040_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slopez_21d_z126_3d_v041_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slopez_63d_z252_3d_v042_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slopez_126d_z252_3d_v043_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_slopez_252d_z504_3d_v044_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slopez_21d_z126_3d_v045_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slopez_63d_z252_3d_v046_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slopez_126d_z252_3d_v047_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_slopez_252d_z504_3d_v048_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slopez_21d_z126_3d_v049_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slopez_63d_z252_3d_v050_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slopez_126d_z252_3d_v051_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_slopez_252d_z504_3d_v052_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slopez_21d_z126_3d_v053_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slopez_63d_z252_3d_v054_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slopez_126d_z252_3d_v055_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_slopez_252d_z504_3d_v056_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_jerk_21d_3d_v057_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_jerk_63d_3d_v058_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_jerk_126d_3d_v059_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_jerk_21d_3d_v060_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_jerk_63d_3d_v061_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_jerk_126d_3d_v062_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_jerk_21d_3d_v063_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_jerk_63d_3d_v064_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_jerk_126d_3d_v065_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_jerk_21d_3d_v066_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_jerk_63d_3d_v067_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_jerk_126d_3d_v068_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_jerk_21d_3d_v069_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_jerk_63d_3d_v070_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_jerk_126d_3d_v071_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_jerk_21d_3d_v072_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_jerk_63d_3d_v073_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_jerk_126d_3d_v074_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_jerk_21d_3d_v075_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_jerk_63d_3d_v076_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_jerk_126d_3d_v077_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of asset_turnover_lvl smoothed over 252d
def f066ato_f066_asset_turnover_asset_turnover_lvl_smoothaccel_63d_sm252_3d_v078_signal(assetturnover, closeadj):
    base = assetturnover
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of asset_turnover_lvl smoothed over 504d
def f066ato_f066_asset_turnover_asset_turnover_lvl_smoothaccel_252d_sm504_3d_v079_signal(assetturnover, closeadj):
    base = assetturnover
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of asset_turnover_calc smoothed over 252d
def f066ato_f066_asset_turnover_asset_turnover_calc_smoothaccel_63d_sm252_3d_v080_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of asset_turnover_calc smoothed over 504d
def f066ato_f066_asset_turnover_asset_turnover_calc_smoothaccel_252d_sm504_3d_v081_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of at_yoy_chg smoothed over 252d
def f066ato_f066_asset_turnover_at_yoy_chg_smoothaccel_63d_sm252_3d_v082_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of at_yoy_chg smoothed over 504d
def f066ato_f066_asset_turnover_at_yoy_chg_smoothaccel_252d_sm504_3d_v083_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_to_asset smoothed over 252d
def f066ato_f066_asset_turnover_rev_to_asset_smoothaccel_63d_sm252_3d_v084_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_to_asset smoothed over 504d
def f066ato_f066_asset_turnover_rev_to_asset_smoothaccel_252d_sm504_3d_v085_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of at_vol_252 smoothed over 252d
def f066ato_f066_asset_turnover_at_vol_252_smoothaccel_63d_sm252_3d_v086_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of at_vol_252 smoothed over 504d
def f066ato_f066_asset_turnover_at_vol_252_smoothaccel_252d_sm504_3d_v087_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_per_curr_asset smoothed over 252d
def f066ato_f066_asset_turnover_rev_per_curr_asset_smoothaccel_63d_sm252_3d_v088_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_per_curr_asset smoothed over 504d
def f066ato_f066_asset_turnover_rev_per_curr_asset_smoothaccel_252d_sm504_3d_v089_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_per_ppne smoothed over 252d
def f066ato_f066_asset_turnover_rev_per_ppne_smoothaccel_63d_sm252_3d_v090_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_per_ppne smoothed over 504d
def f066ato_f066_asset_turnover_rev_per_ppne_smoothaccel_252d_sm504_3d_v091_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_accelz_21d_z252_3d_v092_signal(assetturnover, closeadj):
    base = assetturnover
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_accelz_63d_z504_3d_v093_signal(assetturnover, closeadj):
    base = assetturnover
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_accelz_21d_z252_3d_v094_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_accelz_63d_z504_3d_v095_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_accelz_21d_z252_3d_v096_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_accelz_63d_z504_3d_v097_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_accelz_21d_z252_3d_v098_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_accelz_63d_z504_3d_v099_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_accelz_21d_z252_3d_v100_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_accelz_63d_z504_3d_v101_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_accelz_21d_z252_3d_v102_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_accelz_63d_z504_3d_v103_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_accelz_21d_z252_3d_v104_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_per_ppne
def f066ato_f066_asset_turnover_rev_per_ppne_accelz_63d_z504_3d_v105_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in asset_turnover_lvl (raw count, no price scaling)
def f066ato_f066_asset_turnover_asset_turnover_lvl_signflip_63d_3d_v106_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in asset_turnover_lvl (raw count, no price scaling)
def f066ato_f066_asset_turnover_asset_turnover_lvl_signflip_252d_3d_v107_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in asset_turnover_calc (raw count, no price scaling)
def f066ato_f066_asset_turnover_asset_turnover_calc_signflip_63d_3d_v108_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in asset_turnover_calc (raw count, no price scaling)
def f066ato_f066_asset_turnover_asset_turnover_calc_signflip_252d_3d_v109_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in at_yoy_chg (raw count, no price scaling)
def f066ato_f066_asset_turnover_at_yoy_chg_signflip_63d_3d_v110_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in at_yoy_chg (raw count, no price scaling)
def f066ato_f066_asset_turnover_at_yoy_chg_signflip_252d_3d_v111_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_to_asset (raw count, no price scaling)
def f066ato_f066_asset_turnover_rev_to_asset_signflip_63d_3d_v112_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_to_asset (raw count, no price scaling)
def f066ato_f066_asset_turnover_rev_to_asset_signflip_252d_3d_v113_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in at_vol_252 (raw count, no price scaling)
def f066ato_f066_asset_turnover_at_vol_252_signflip_63d_3d_v114_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in at_vol_252 (raw count, no price scaling)
def f066ato_f066_asset_turnover_at_vol_252_signflip_252d_3d_v115_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_per_curr_asset (raw count, no price scaling)
def f066ato_f066_asset_turnover_rev_per_curr_asset_signflip_63d_3d_v116_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_per_curr_asset (raw count, no price scaling)
def f066ato_f066_asset_turnover_rev_per_curr_asset_signflip_252d_3d_v117_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_per_ppne (raw count, no price scaling)
def f066ato_f066_asset_turnover_rev_per_ppne_signflip_63d_3d_v118_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_per_ppne (raw count, no price scaling)
def f066ato_f066_asset_turnover_rev_per_ppne_signflip_252d_3d_v119_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_turnover_lvl normalized by 252d range
def f066ato_f066_asset_turnover_asset_turnover_lvl_rngaccel_63d_r252_3d_v120_signal(assetturnover, closeadj):
    base = assetturnover
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_turnover_lvl normalized by 504d range
def f066ato_f066_asset_turnover_asset_turnover_lvl_rngaccel_252d_r504_3d_v121_signal(assetturnover, closeadj):
    base = assetturnover
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of asset_turnover_calc normalized by 252d range
def f066ato_f066_asset_turnover_asset_turnover_calc_rngaccel_63d_r252_3d_v122_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of asset_turnover_calc normalized by 504d range
def f066ato_f066_asset_turnover_asset_turnover_calc_rngaccel_252d_r504_3d_v123_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of at_yoy_chg normalized by 252d range
def f066ato_f066_asset_turnover_at_yoy_chg_rngaccel_63d_r252_3d_v124_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of at_yoy_chg normalized by 504d range
def f066ato_f066_asset_turnover_at_yoy_chg_rngaccel_252d_r504_3d_v125_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_to_asset normalized by 252d range
def f066ato_f066_asset_turnover_rev_to_asset_rngaccel_63d_r252_3d_v126_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_to_asset normalized by 504d range
def f066ato_f066_asset_turnover_rev_to_asset_rngaccel_252d_r504_3d_v127_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of at_vol_252 normalized by 252d range
def f066ato_f066_asset_turnover_at_vol_252_rngaccel_63d_r252_3d_v128_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of at_vol_252 normalized by 504d range
def f066ato_f066_asset_turnover_at_vol_252_rngaccel_252d_r504_3d_v129_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_curr_asset normalized by 252d range
def f066ato_f066_asset_turnover_rev_per_curr_asset_rngaccel_63d_r252_3d_v130_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_curr_asset normalized by 504d range
def f066ato_f066_asset_turnover_rev_per_curr_asset_rngaccel_252d_r504_3d_v131_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_ppne normalized by 252d range
def f066ato_f066_asset_turnover_rev_per_ppne_rngaccel_63d_r252_3d_v132_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_ppne normalized by 504d range
def f066ato_f066_asset_turnover_rev_per_ppne_rngaccel_252d_r504_3d_v133_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_cumslope_21d_3d_v134_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_cumslope_63d_3d_v135_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of asset_turnover_lvl
def f066ato_f066_asset_turnover_asset_turnover_lvl_cumslope_252d_3d_v136_signal(assetturnover, closeadj):
    base = assetturnover
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_cumslope_21d_3d_v137_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_cumslope_63d_3d_v138_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of asset_turnover_calc
def f066ato_f066_asset_turnover_asset_turnover_calc_cumslope_252d_3d_v139_signal(revenue, assetsavg, closeadj):
    base = _f066_at(revenue, assetsavg)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_cumslope_21d_3d_v140_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_cumslope_63d_3d_v141_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of at_yoy_chg
def f066ato_f066_asset_turnover_at_yoy_chg_cumslope_252d_3d_v142_signal(assetturnover, closeadj):
    base = assetturnover.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_cumslope_21d_3d_v143_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_cumslope_63d_3d_v144_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_to_asset
def f066ato_f066_asset_turnover_rev_to_asset_cumslope_252d_3d_v145_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_cumslope_21d_3d_v146_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_cumslope_63d_3d_v147_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of at_vol_252
def f066ato_f066_asset_turnover_at_vol_252_cumslope_252d_3d_v148_signal(assetturnover, closeadj):
    base = assetturnover.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_cumslope_21d_3d_v149_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_per_curr_asset
def f066ato_f066_asset_turnover_rev_per_curr_asset_cumslope_63d_3d_v150_signal(revenue, assetsc, closeadj):
    base = revenue / assetsc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

