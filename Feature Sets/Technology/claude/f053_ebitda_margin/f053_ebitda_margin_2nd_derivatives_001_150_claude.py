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
def _f053_ebm(ebitda, revenue):
    return ebitda / revenue.abs().replace(0, np.nan)


# 21d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slope_21d_2d_v001_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slope_63d_2d_v002_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slope_126d_2d_v003_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slope_252d_2d_v004_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slope_504d_2d_v005_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slope_21d_2d_v006_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slope_63d_2d_v007_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slope_126d_2d_v008_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slope_252d_2d_v009_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slope_504d_2d_v010_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slope_21d_2d_v011_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slope_63d_2d_v012_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slope_126d_2d_v013_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slope_252d_2d_v014_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slope_504d_2d_v015_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slope_21d_2d_v016_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slope_63d_2d_v017_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slope_126d_2d_v018_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slope_252d_2d_v019_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slope_504d_2d_v020_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slope_21d_2d_v021_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slope_63d_2d_v022_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slope_126d_2d_v023_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slope_252d_2d_v024_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slope_504d_2d_v025_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slope_21d_2d_v026_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slope_63d_2d_v027_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slope_126d_2d_v028_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slope_252d_2d_v029_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slope_504d_2d_v030_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slope_21d_2d_v031_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slope_63d_2d_v032_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slope_126d_2d_v033_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slope_252d_2d_v034_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slope_504d_2d_v035_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slope_21d_2d_v036_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slope_63d_2d_v037_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slope_126d_2d_v038_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slope_252d_2d_v039_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slope_504d_2d_v040_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slope_21d_2d_v041_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slope_63d_2d_v042_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slope_126d_2d_v043_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slope_252d_2d_v044_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slope_504d_2d_v045_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slope_21d_2d_v046_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slope_63d_2d_v047_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slope_126d_2d_v048_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slope_252d_2d_v049_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slope_504d_2d_v050_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slope_21d_2d_v056_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slope_63d_2d_v057_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slope_126d_2d_v058_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slope_252d_2d_v059_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slope_504d_2d_v060_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slope_21d_2d_v061_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slope_63d_2d_v062_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slope_126d_2d_v063_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slope_252d_2d_v064_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slope_504d_2d_v065_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sm21_sl21_2d_v066_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sm63_sl21_2d_v067_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sm63_sl63_2d_v068_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sm252_sl63_2d_v069_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sm252_sl126_2d_v070_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sm21_sl21_2d_v071_signal(ebitdamargin, closeadj):
    base = _mean(ebitdamargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sm63_sl21_2d_v072_signal(ebitdamargin, closeadj):
    base = _mean(ebitdamargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sm63_sl63_2d_v073_signal(ebitdamargin, closeadj):
    base = _mean(ebitdamargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sm252_sl63_2d_v074_signal(ebitdamargin, closeadj):
    base = _mean(ebitdamargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sm252_sl126_2d_v075_signal(ebitdamargin, closeadj):
    base = _mean(ebitdamargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sm21_sl21_2d_v076_signal(ebitda, closeadj):
    base = _mean(ebitda, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sm63_sl21_2d_v077_signal(ebitda, closeadj):
    base = _mean(ebitda, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sm63_sl63_2d_v078_signal(ebitda, closeadj):
    base = _mean(ebitda, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sm252_sl63_2d_v079_signal(ebitda, closeadj):
    base = _mean(ebitda, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sm252_sl126_2d_v080_signal(ebitda, closeadj):
    base = _mean(ebitda, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sm21_sl21_2d_v081_signal(ebitda, closeadj):
    base = _mean(ebitda.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sm63_sl21_2d_v082_signal(ebitda, closeadj):
    base = _mean(ebitda.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sm63_sl63_2d_v083_signal(ebitda, closeadj):
    base = _mean(ebitda.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sm252_sl63_2d_v084_signal(ebitda, closeadj):
    base = _mean(ebitda.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sm252_sl126_2d_v085_signal(ebitda, closeadj):
    base = _mean(ebitda.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sm21_sl21_2d_v086_signal(ebitda, fcf, closeadj):
    base = _mean(ebitda / fcf.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sm63_sl21_2d_v087_signal(ebitda, fcf, closeadj):
    base = _mean(ebitda / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sm63_sl63_2d_v088_signal(ebitda, fcf, closeadj):
    base = _mean(ebitda / fcf.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sm252_sl63_2d_v089_signal(ebitda, fcf, closeadj):
    base = _mean(ebitda / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sm252_sl126_2d_v090_signal(ebitda, fcf, closeadj):
    base = _mean(ebitda / fcf.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sm21_sl21_2d_v091_signal(ebitda, assets, closeadj):
    base = _mean(ebitda / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sm63_sl21_2d_v092_signal(ebitda, assets, closeadj):
    base = _mean(ebitda / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sm63_sl63_2d_v093_signal(ebitda, assets, closeadj):
    base = _mean(ebitda / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sm252_sl63_2d_v094_signal(ebitda, assets, closeadj):
    base = _mean(ebitda / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sm252_sl126_2d_v095_signal(ebitda, assets, closeadj):
    base = _mean(ebitda / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sm21_sl21_2d_v096_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sm63_sl21_2d_v097_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sm63_sl63_2d_v098_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sm252_sl63_2d_v099_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sm252_sl126_2d_v100_signal(ebitda, revenue, closeadj):
    base = _mean(_f053_ebm(ebitda, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sm21_sl21_2d_v101_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sm63_sl21_2d_v102_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sm63_sl63_2d_v103_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sm252_sl63_2d_v104_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sm252_sl126_2d_v105_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sm21_sl21_2d_v106_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sm63_sl21_2d_v107_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sm63_sl63_2d_v108_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sm252_sl63_2d_v109_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sm252_sl126_2d_v110_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sm21_sl21_2d_v111_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sm63_sl21_2d_v112_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sm63_sl63_2d_v113_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sm252_sl63_2d_v114_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sm252_sl126_2d_v115_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = _mean((_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_sm21_sl21_2d_v121_signal(ebm_sector_pctile, closeadj):
    base = _mean(ebm_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_sm63_sl21_2d_v122_signal(ebm_sector_pctile, closeadj):
    base = _mean(ebm_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_sm63_sl63_2d_v123_signal(ebm_sector_pctile, closeadj):
    base = _mean(ebm_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_sm252_sl63_2d_v124_signal(ebm_sector_pctile, closeadj):
    base = _mean(ebm_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_sm252_sl126_2d_v125_signal(ebm_sector_pctile, closeadj):
    base = _mean(ebm_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_sm21_sl21_2d_v126_signal(ebm_industry_pctile, closeadj):
    base = _mean(ebm_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_sm63_sl21_2d_v127_signal(ebm_industry_pctile, closeadj):
    base = _mean(ebm_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_sm63_sl63_2d_v128_signal(ebm_industry_pctile, closeadj):
    base = _mean(ebm_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_sm252_sl63_2d_v129_signal(ebm_industry_pctile, closeadj):
    base = _mean(ebm_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_sm252_sl126_2d_v130_signal(ebm_industry_pctile, closeadj):
    base = _mean(ebm_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_pctslope_21d_2d_v131_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_pctslope_63d_2d_v132_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_pctslope_252d_2d_v133_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_pctslope_21d_2d_v134_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_pctslope_63d_2d_v135_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_pctslope_252d_2d_v136_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_pctslope_21d_2d_v137_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_pctslope_63d_2d_v138_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_pctslope_252d_2d_v139_signal(ebitda, closeadj):
    base = ebitda
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_pctslope_21d_2d_v140_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_pctslope_63d_2d_v141_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_pctslope_252d_2d_v142_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_pctslope_21d_2d_v143_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_pctslope_63d_2d_v144_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_pctslope_252d_2d_v145_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_pctslope_21d_2d_v146_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_pctslope_63d_2d_v147_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_pctslope_252d_2d_v148_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_pctslope_21d_2d_v149_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_pctslope_63d_2d_v150_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_pctslope_252d_2d_v151_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_pctslope_21d_2d_v152_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_pctslope_63d_2d_v153_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_pctslope_252d_2d_v154_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_pctslope_21d_2d_v155_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_pctslope_63d_2d_v156_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_pctslope_252d_2d_v157_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_pctslope_21d_2d_v158_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_pctslope_63d_2d_v159_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_pctslope_252d_2d_v160_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_pctslope_21d_2d_v164_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_pctslope_63d_2d_v165_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_pctslope_252d_2d_v166_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_pctslope_21d_2d_v167_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_pctslope_63d_2d_v168_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_pctslope_252d_2d_v169_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sgnslope_21d_2d_v170_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sgnslope_63d_2d_v171_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_sgnslope_252d_2d_v172_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sgnslope_21d_2d_v173_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sgnslope_63d_2d_v174_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_sgnslope_252d_2d_v175_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sgnslope_21d_2d_v176_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sgnslope_63d_2d_v177_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_sgnslope_252d_2d_v178_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sgnslope_21d_2d_v179_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sgnslope_63d_2d_v180_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_sgnslope_252d_2d_v181_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sgnslope_21d_2d_v182_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sgnslope_63d_2d_v183_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_sgnslope_252d_2d_v184_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sgnslope_21d_2d_v185_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sgnslope_63d_2d_v186_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_sgnslope_252d_2d_v187_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sgnslope_21d_2d_v188_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sgnslope_63d_2d_v189_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_sgnslope_252d_2d_v190_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sgnslope_21d_2d_v191_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sgnslope_63d_2d_v192_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_sgnslope_252d_2d_v193_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sgnslope_21d_2d_v194_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sgnslope_63d_2d_v195_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_sgnslope_252d_2d_v196_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sgnslope_21d_2d_v197_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sgnslope_63d_2d_v198_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_sgnslope_252d_2d_v199_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

