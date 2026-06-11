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


# 21d acceleration of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_accel_21d_3d_v001_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_accel_63d_3d_v002_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_accel_126d_3d_v003_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_accel_252d_3d_v004_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_accel_21d_3d_v005_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_accel_63d_3d_v006_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_accel_126d_3d_v007_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_accel_252d_3d_v008_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_accel_21d_3d_v009_signal(ebitda, closeadj):
    base = ebitda
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_accel_63d_3d_v010_signal(ebitda, closeadj):
    base = ebitda
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_accel_126d_3d_v011_signal(ebitda, closeadj):
    base = ebitda
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_accel_252d_3d_v012_signal(ebitda, closeadj):
    base = ebitda
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_accel_21d_3d_v013_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_accel_63d_3d_v014_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_accel_126d_3d_v015_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_accel_252d_3d_v016_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_accel_21d_3d_v017_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_accel_63d_3d_v018_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_accel_126d_3d_v019_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_accel_252d_3d_v020_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_accel_21d_3d_v021_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_accel_63d_3d_v022_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_accel_126d_3d_v023_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_accel_252d_3d_v024_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_accel_21d_3d_v025_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_accel_63d_3d_v026_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_accel_126d_3d_v027_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_accel_252d_3d_v028_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_accel_21d_3d_v029_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_accel_63d_3d_v030_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_accel_126d_3d_v031_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_accel_252d_3d_v032_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_accel_21d_3d_v033_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_accel_63d_3d_v034_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_accel_126d_3d_v035_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_accel_252d_3d_v036_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_accel_21d_3d_v037_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_accel_63d_3d_v038_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_accel_126d_3d_v039_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_accel_252d_3d_v040_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_accel_21d_3d_v045_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_accel_63d_3d_v046_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_accel_126d_3d_v047_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_accel_252d_3d_v048_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_accel_21d_3d_v049_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_accel_63d_3d_v050_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_accel_126d_3d_v051_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_accel_252d_3d_v052_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slopez_21d_z126_3d_v053_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slopez_63d_z252_3d_v054_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slopez_126d_z252_3d_v055_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_slopez_252d_z504_3d_v056_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slopez_21d_z126_3d_v057_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slopez_63d_z252_3d_v058_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slopez_126d_z252_3d_v059_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_slopez_252d_z504_3d_v060_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slopez_21d_z126_3d_v061_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slopez_63d_z252_3d_v062_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slopez_126d_z252_3d_v063_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_slopez_252d_z504_3d_v064_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slopez_21d_z126_3d_v065_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slopez_63d_z252_3d_v066_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slopez_126d_z252_3d_v067_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_slopez_252d_z504_3d_v068_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slopez_21d_z126_3d_v069_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slopez_63d_z252_3d_v070_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slopez_126d_z252_3d_v071_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_slopez_252d_z504_3d_v072_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slopez_21d_z126_3d_v073_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slopez_63d_z252_3d_v074_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slopez_126d_z252_3d_v075_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_slopez_252d_z504_3d_v076_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slopez_21d_z126_3d_v077_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slopez_63d_z252_3d_v078_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slopez_126d_z252_3d_v079_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_slopez_252d_z504_3d_v080_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slopez_21d_z126_3d_v081_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slopez_63d_z252_3d_v082_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slopez_126d_z252_3d_v083_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_slopez_252d_z504_3d_v084_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slopez_21d_z126_3d_v085_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slopez_63d_z252_3d_v086_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slopez_126d_z252_3d_v087_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_slopez_252d_z504_3d_v088_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slopez_21d_z126_3d_v089_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slopez_63d_z252_3d_v090_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slopez_126d_z252_3d_v091_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_slopez_252d_z504_3d_v092_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_jerk_21d_3d_v105_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_jerk_63d_3d_v106_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_jerk_126d_3d_v107_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_jerk_21d_3d_v108_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_jerk_63d_3d_v109_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_jerk_126d_3d_v110_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_jerk_21d_3d_v111_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_jerk_63d_3d_v112_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_jerk_126d_3d_v113_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_jerk_21d_3d_v114_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_jerk_63d_3d_v115_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_jerk_126d_3d_v116_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_jerk_21d_3d_v117_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_jerk_63d_3d_v118_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_jerk_126d_3d_v119_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_jerk_21d_3d_v120_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_jerk_63d_3d_v121_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_jerk_126d_3d_v122_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_jerk_21d_3d_v123_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_jerk_63d_3d_v124_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_jerk_126d_3d_v125_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_jerk_21d_3d_v126_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_jerk_63d_3d_v127_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_jerk_126d_3d_v128_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_jerk_21d_3d_v129_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_jerk_63d_3d_v130_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_jerk_126d_3d_v131_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_jerk_21d_3d_v132_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_jerk_63d_3d_v133_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_jerk_126d_3d_v134_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_jerk_21d_3d_v138_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_jerk_63d_3d_v139_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_jerk_126d_3d_v140_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_jerk_21d_3d_v141_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_jerk_63d_3d_v142_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_jerk_126d_3d_v143_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_margin_calc smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_smoothaccel_63d_sm252_3d_v144_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_margin_calc smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_smoothaccel_252d_sm504_3d_v145_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitdamargin smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitdamargin_smoothaccel_63d_sm252_3d_v146_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitdamargin smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitdamargin_smoothaccel_252d_sm504_3d_v147_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_lvl smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitda_lvl_smoothaccel_63d_sm252_3d_v148_signal(ebitda, closeadj):
    base = ebitda
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_lvl smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitda_lvl_smoothaccel_252d_sm504_3d_v149_signal(ebitda, closeadj):
    base = ebitda
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_growth smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitda_growth_smoothaccel_63d_sm252_3d_v150_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_growth smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitda_growth_smoothaccel_252d_sm504_3d_v151_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_to_fcf smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_smoothaccel_63d_sm252_3d_v152_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_to_fcf smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_smoothaccel_252d_sm504_3d_v153_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_to_asset smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitda_to_asset_smoothaccel_63d_sm252_3d_v154_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_to_asset smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitda_to_asset_smoothaccel_252d_sm504_3d_v155_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_yoy_chg smoothed over 252d
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_smoothaccel_63d_sm252_3d_v156_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_yoy_chg smoothed over 504d
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_smoothaccel_252d_sm504_3d_v157_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebm_peer_sector_dist smoothed over 252d
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebm_peer_sector_dist smoothed over 504d
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebm_peer_sector_z smoothed over 252d
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebm_peer_sector_z smoothed over 504d
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebm_peer_industry_dist smoothed over 252d
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebm_peer_industry_dist smoothed over 504d
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebm_peer_mcap_bucket_dist smoothed over 252d
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebm_peer_mcap_bucket_dist smoothed over 504d
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebm_peer_sector_pctile smoothed over 252d
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebm_peer_sector_pctile smoothed over 504d
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebm_peer_industry_pctile smoothed over 252d
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebm_peer_industry_pctile smoothed over 504d
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_accelz_21d_z252_3d_v170_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_accelz_63d_z504_3d_v171_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_accelz_21d_z252_3d_v172_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_accelz_63d_z504_3d_v173_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_accelz_21d_z252_3d_v174_signal(ebitda, closeadj):
    base = ebitda
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_accelz_63d_z504_3d_v175_signal(ebitda, closeadj):
    base = ebitda
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_accelz_21d_z252_3d_v176_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_accelz_63d_z504_3d_v177_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_accelz_21d_z252_3d_v178_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_accelz_63d_z504_3d_v179_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_accelz_21d_z252_3d_v180_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_accelz_63d_z504_3d_v181_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_accelz_21d_z252_3d_v182_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_accelz_63d_z504_3d_v183_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_accelz_21d_z252_3d_v184_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_accelz_63d_z504_3d_v185_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_accelz_21d_z252_3d_v186_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_accelz_63d_z504_3d_v187_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_accelz_21d_z252_3d_v188_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_accelz_63d_z504_3d_v189_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebitda_margin_calc (raw count, no price scaling)
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_signflip_63d_3d_v196_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ebitda_margin_calc (raw count, no price scaling)
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_signflip_252d_3d_v197_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebitdamargin (raw count, no price scaling)
def f053ebm_f053_ebitda_margin_ebitdamargin_signflip_63d_3d_v198_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ebitdamargin (raw count, no price scaling)
def f053ebm_f053_ebitda_margin_ebitdamargin_signflip_252d_3d_v199_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebitda_lvl (raw count, no price scaling)
def f053ebm_f053_ebitda_margin_ebitda_lvl_signflip_63d_3d_v200_signal(ebitda, closeadj):
    base = ebitda
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

