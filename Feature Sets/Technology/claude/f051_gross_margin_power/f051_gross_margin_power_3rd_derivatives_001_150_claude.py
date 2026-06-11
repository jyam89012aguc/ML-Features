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
def _f051_gm(gp, revenue):
    return gp / revenue.abs().replace(0, np.nan)


# 21d acceleration of gm
def f051gmp_f051_gross_margin_power_gm_accel_21d_3d_v001_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm
def f051gmp_f051_gross_margin_power_gm_accel_63d_3d_v002_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm
def f051gmp_f051_gross_margin_power_gm_accel_126d_3d_v003_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm
def f051gmp_f051_gross_margin_power_gm_accel_252d_3d_v004_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_accel_21d_3d_v005_signal(gp, closeadj):
    base = gp
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_accel_63d_3d_v006_signal(gp, closeadj):
    base = gp
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_accel_126d_3d_v007_signal(gp, closeadj):
    base = gp
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_accel_252d_3d_v008_signal(gp, closeadj):
    base = gp
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_accel_21d_3d_v009_signal(grossmargin, closeadj):
    base = grossmargin
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_accel_63d_3d_v010_signal(grossmargin, closeadj):
    base = grossmargin
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_accel_126d_3d_v011_signal(grossmargin, closeadj):
    base = grossmargin
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_accel_252d_3d_v012_signal(grossmargin, closeadj):
    base = grossmargin
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_accel_21d_3d_v013_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_accel_63d_3d_v014_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_accel_126d_3d_v015_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_accel_252d_3d_v016_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_accel_21d_3d_v017_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_accel_63d_3d_v018_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_accel_126d_3d_v019_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_accel_252d_3d_v020_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_accel_21d_3d_v021_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_accel_63d_3d_v022_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_accel_126d_3d_v023_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_accel_252d_3d_v024_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_accel_21d_3d_v025_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_accel_63d_3d_v026_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_accel_126d_3d_v027_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_accel_252d_3d_v028_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_accel_21d_3d_v029_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_accel_63d_3d_v030_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_accel_126d_3d_v031_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_accel_252d_3d_v032_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_accel_21d_3d_v033_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_accel_63d_3d_v034_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_accel_126d_3d_v035_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_accel_252d_3d_v036_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_accel_21d_3d_v037_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_accel_63d_3d_v038_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_accel_126d_3d_v039_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_accel_252d_3d_v040_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_accel_21d_3d_v045_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_accel_63d_3d_v046_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_accel_126d_3d_v047_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_accel_252d_3d_v048_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_accel_21d_3d_v049_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_accel_63d_3d_v050_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_accel_126d_3d_v051_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_accel_252d_3d_v052_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm
def f051gmp_f051_gross_margin_power_gm_slopez_21d_z126_3d_v053_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm
def f051gmp_f051_gross_margin_power_gm_slopez_63d_z252_3d_v054_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm
def f051gmp_f051_gross_margin_power_gm_slopez_126d_z252_3d_v055_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm
def f051gmp_f051_gross_margin_power_gm_slopez_252d_z504_3d_v056_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slopez_21d_z126_3d_v057_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slopez_63d_z252_3d_v058_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slopez_126d_z252_3d_v059_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slopez_252d_z504_3d_v060_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slopez_21d_z126_3d_v061_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slopez_63d_z252_3d_v062_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slopez_126d_z252_3d_v063_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slopez_252d_z504_3d_v064_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slopez_21d_z126_3d_v065_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slopez_63d_z252_3d_v066_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slopez_126d_z252_3d_v067_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slopez_252d_z504_3d_v068_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slopez_21d_z126_3d_v069_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slopez_63d_z252_3d_v070_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slopez_126d_z252_3d_v071_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slopez_252d_z504_3d_v072_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slopez_21d_z126_3d_v073_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slopez_63d_z252_3d_v074_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slopez_126d_z252_3d_v075_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slopez_252d_z504_3d_v076_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slopez_21d_z126_3d_v077_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slopez_63d_z252_3d_v078_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slopez_126d_z252_3d_v079_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slopez_252d_z504_3d_v080_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slopez_21d_z126_3d_v081_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slopez_63d_z252_3d_v082_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slopez_126d_z252_3d_v083_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slopez_252d_z504_3d_v084_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slopez_21d_z126_3d_v085_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slopez_63d_z252_3d_v086_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slopez_126d_z252_3d_v087_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slopez_252d_z504_3d_v088_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slopez_21d_z126_3d_v089_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slopez_63d_z252_3d_v090_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slopez_126d_z252_3d_v091_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slopez_252d_z504_3d_v092_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm
def f051gmp_f051_gross_margin_power_gm_jerk_21d_3d_v105_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm
def f051gmp_f051_gross_margin_power_gm_jerk_63d_3d_v106_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm
def f051gmp_f051_gross_margin_power_gm_jerk_126d_3d_v107_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_jerk_21d_3d_v108_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_jerk_63d_3d_v109_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_jerk_126d_3d_v110_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_jerk_21d_3d_v111_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_jerk_63d_3d_v112_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_jerk_126d_3d_v113_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_jerk_21d_3d_v114_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_jerk_63d_3d_v115_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_jerk_126d_3d_v116_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_jerk_21d_3d_v117_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_jerk_63d_3d_v118_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_jerk_126d_3d_v119_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_jerk_21d_3d_v120_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_jerk_63d_3d_v121_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_jerk_126d_3d_v122_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_jerk_21d_3d_v123_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_jerk_63d_3d_v124_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_jerk_126d_3d_v125_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_jerk_21d_3d_v126_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_jerk_63d_3d_v127_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_jerk_126d_3d_v128_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_jerk_21d_3d_v129_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_jerk_63d_3d_v130_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_jerk_126d_3d_v131_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_jerk_21d_3d_v132_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_jerk_63d_3d_v133_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_jerk_126d_3d_v134_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_jerk_21d_3d_v138_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_jerk_63d_3d_v139_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_jerk_126d_3d_v140_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_jerk_21d_3d_v141_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_jerk_63d_3d_v142_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_jerk_126d_3d_v143_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_smoothaccel_63d_sm252_3d_v144_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_smoothaccel_252d_sm504_3d_v145_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_lvl smoothed over 252d
def f051gmp_f051_gross_margin_power_gp_lvl_smoothaccel_63d_sm252_3d_v146_signal(gp, closeadj):
    base = gp
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_lvl smoothed over 504d
def f051gmp_f051_gross_margin_power_gp_lvl_smoothaccel_252d_sm504_3d_v147_signal(gp, closeadj):
    base = gp
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of grossmargin_lvl smoothed over 252d
def f051gmp_f051_gross_margin_power_grossmargin_lvl_smoothaccel_63d_sm252_3d_v148_signal(grossmargin, closeadj):
    base = grossmargin
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of grossmargin_lvl smoothed over 504d
def f051gmp_f051_gross_margin_power_grossmargin_lvl_smoothaccel_252d_sm504_3d_v149_signal(grossmargin, closeadj):
    base = grossmargin
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_growth_y smoothed over 252d
def f051gmp_f051_gross_margin_power_gp_growth_y_smoothaccel_63d_sm252_3d_v150_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_growth_y smoothed over 504d
def f051gmp_f051_gross_margin_power_gp_growth_y_smoothaccel_252d_sm504_3d_v151_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_yoy_chg smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_yoy_chg_smoothaccel_63d_sm252_3d_v152_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_yoy_chg smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_yoy_chg_smoothaccel_252d_sm504_3d_v153_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_vol_252 smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_vol_252_smoothaccel_63d_sm252_3d_v154_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_vol_252 smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_vol_252_smoothaccel_252d_sm504_3d_v155_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_to_rnd smoothed over 252d
def f051gmp_f051_gross_margin_power_gp_to_rnd_smoothaccel_63d_sm252_3d_v156_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_to_rnd smoothed over 504d
def f051gmp_f051_gross_margin_power_gp_to_rnd_smoothaccel_252d_sm504_3d_v157_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_peer_sector_dist smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_peer_sector_dist smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_peer_sector_z smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_peer_sector_z smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_peer_industry_dist smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_peer_industry_dist smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_peer_mcap_bucket_dist smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_peer_mcap_bucket_dist smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_peer_sector_pctile smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_peer_sector_pctile smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_peer_industry_pctile smoothed over 252d
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_peer_industry_pctile smoothed over 504d
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm
def f051gmp_f051_gross_margin_power_gm_accelz_21d_z252_3d_v170_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm
def f051gmp_f051_gross_margin_power_gm_accelz_63d_z504_3d_v171_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_accelz_21d_z252_3d_v172_signal(gp, closeadj):
    base = gp
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_accelz_63d_z504_3d_v173_signal(gp, closeadj):
    base = gp
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_accelz_21d_z252_3d_v174_signal(grossmargin, closeadj):
    base = grossmargin
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_accelz_63d_z504_3d_v175_signal(grossmargin, closeadj):
    base = grossmargin
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_accelz_21d_z252_3d_v176_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_accelz_63d_z504_3d_v177_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_accelz_21d_z252_3d_v178_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_accelz_63d_z504_3d_v179_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_accelz_21d_z252_3d_v180_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_accelz_63d_z504_3d_v181_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_accelz_21d_z252_3d_v182_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_accelz_63d_z504_3d_v183_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_accelz_21d_z252_3d_v184_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_accelz_63d_z504_3d_v185_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_accelz_21d_z252_3d_v186_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_accelz_63d_z504_3d_v187_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_accelz_21d_z252_3d_v188_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_accelz_63d_z504_3d_v189_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gm (raw count, no price scaling)
def f051gmp_f051_gross_margin_power_gm_signflip_63d_3d_v196_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gm (raw count, no price scaling)
def f051gmp_f051_gross_margin_power_gm_signflip_252d_3d_v197_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gp_lvl (raw count, no price scaling)
def f051gmp_f051_gross_margin_power_gp_lvl_signflip_63d_3d_v198_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gp_lvl (raw count, no price scaling)
def f051gmp_f051_gross_margin_power_gp_lvl_signflip_252d_3d_v199_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in grossmargin_lvl (raw count, no price scaling)
def f051gmp_f051_gross_margin_power_grossmargin_lvl_signflip_63d_3d_v200_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

