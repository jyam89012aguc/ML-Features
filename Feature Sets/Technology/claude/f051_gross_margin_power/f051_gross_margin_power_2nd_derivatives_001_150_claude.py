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


# 21d slope of gm
def f051gmp_f051_gross_margin_power_gm_slope_21d_2d_v001_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm
def f051gmp_f051_gross_margin_power_gm_slope_63d_2d_v002_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm
def f051gmp_f051_gross_margin_power_gm_slope_126d_2d_v003_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm
def f051gmp_f051_gross_margin_power_gm_slope_252d_2d_v004_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm
def f051gmp_f051_gross_margin_power_gm_slope_504d_2d_v005_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slope_21d_2d_v006_signal(gp, closeadj):
    base = gp
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slope_63d_2d_v007_signal(gp, closeadj):
    base = gp
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slope_126d_2d_v008_signal(gp, closeadj):
    base = gp
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slope_252d_2d_v009_signal(gp, closeadj):
    base = gp
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_slope_504d_2d_v010_signal(gp, closeadj):
    base = gp
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slope_21d_2d_v011_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slope_63d_2d_v012_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slope_126d_2d_v013_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slope_252d_2d_v014_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_slope_504d_2d_v015_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slope_21d_2d_v016_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slope_63d_2d_v017_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slope_126d_2d_v018_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slope_252d_2d_v019_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_slope_504d_2d_v020_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slope_21d_2d_v021_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slope_63d_2d_v022_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slope_126d_2d_v023_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slope_252d_2d_v024_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_slope_504d_2d_v025_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slope_21d_2d_v026_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slope_63d_2d_v027_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slope_126d_2d_v028_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slope_252d_2d_v029_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_slope_504d_2d_v030_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slope_21d_2d_v031_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slope_63d_2d_v032_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slope_126d_2d_v033_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slope_252d_2d_v034_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_slope_504d_2d_v035_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slope_21d_2d_v036_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slope_63d_2d_v037_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slope_126d_2d_v038_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slope_252d_2d_v039_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_slope_504d_2d_v040_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slope_21d_2d_v041_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slope_63d_2d_v042_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slope_126d_2d_v043_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slope_252d_2d_v044_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_slope_504d_2d_v045_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slope_21d_2d_v046_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slope_63d_2d_v047_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slope_126d_2d_v048_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slope_252d_2d_v049_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_slope_504d_2d_v050_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slope_21d_2d_v056_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slope_63d_2d_v057_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slope_126d_2d_v058_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slope_252d_2d_v059_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_slope_504d_2d_v060_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slope_21d_2d_v061_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slope_63d_2d_v062_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slope_126d_2d_v063_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slope_252d_2d_v064_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_slope_504d_2d_v065_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm
def f051gmp_f051_gross_margin_power_gm_sm21_sl21_2d_v066_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm
def f051gmp_f051_gross_margin_power_gm_sm63_sl21_2d_v067_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm
def f051gmp_f051_gross_margin_power_gm_sm63_sl63_2d_v068_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm
def f051gmp_f051_gross_margin_power_gm_sm252_sl63_2d_v069_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm
def f051gmp_f051_gross_margin_power_gm_sm252_sl126_2d_v070_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sm21_sl21_2d_v071_signal(gp, closeadj):
    base = _mean(gp, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sm63_sl21_2d_v072_signal(gp, closeadj):
    base = _mean(gp, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sm63_sl63_2d_v073_signal(gp, closeadj):
    base = _mean(gp, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sm252_sl63_2d_v074_signal(gp, closeadj):
    base = _mean(gp, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sm252_sl126_2d_v075_signal(gp, closeadj):
    base = _mean(gp, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sm21_sl21_2d_v076_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sm63_sl21_2d_v077_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sm63_sl63_2d_v078_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sm252_sl63_2d_v079_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sm252_sl126_2d_v080_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sm21_sl21_2d_v081_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sm63_sl21_2d_v082_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sm63_sl63_2d_v083_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sm252_sl63_2d_v084_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sm252_sl126_2d_v085_signal(gp, closeadj):
    base = _mean(gp.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sm21_sl21_2d_v086_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sm63_sl21_2d_v087_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sm63_sl63_2d_v088_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sm252_sl63_2d_v089_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sm252_sl126_2d_v090_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sm21_sl21_2d_v091_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sm63_sl21_2d_v092_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sm63_sl63_2d_v093_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sm252_sl63_2d_v094_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sm252_sl126_2d_v095_signal(gp, revenue, closeadj):
    base = _mean(_f051_gm(gp, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sm21_sl21_2d_v096_signal(gp, rnd, closeadj):
    base = _mean(gp / rnd.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sm63_sl21_2d_v097_signal(gp, rnd, closeadj):
    base = _mean(gp / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sm63_sl63_2d_v098_signal(gp, rnd, closeadj):
    base = _mean(gp / rnd.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sm252_sl63_2d_v099_signal(gp, rnd, closeadj):
    base = _mean(gp / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sm252_sl126_2d_v100_signal(gp, rnd, closeadj):
    base = _mean(gp / rnd.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sm21_sl21_2d_v101_signal(gp, revenue, gm_sector_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sm63_sl21_2d_v102_signal(gp, revenue, gm_sector_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sm63_sl63_2d_v103_signal(gp, revenue, gm_sector_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sm252_sl63_2d_v104_signal(gp, revenue, gm_sector_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sm252_sl126_2d_v105_signal(gp, revenue, gm_sector_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sm21_sl21_2d_v106_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sm63_sl21_2d_v107_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sm63_sl63_2d_v108_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sm252_sl63_2d_v109_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sm252_sl126_2d_v110_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sm21_sl21_2d_v111_signal(gp, revenue, gm_industry_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sm63_sl21_2d_v112_signal(gp, revenue, gm_industry_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sm63_sl63_2d_v113_signal(gp, revenue, gm_industry_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sm252_sl63_2d_v114_signal(gp, revenue, gm_industry_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sm252_sl126_2d_v115_signal(gp, revenue, gm_industry_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(gp, revenue, gm_mcap_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(gp, revenue, gm_mcap_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(gp, revenue, gm_mcap_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(gp, revenue, gm_mcap_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(gp, revenue, gm_mcap_med, closeadj):
    base = _mean((_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_sm21_sl21_2d_v121_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_sm63_sl21_2d_v122_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_sm63_sl63_2d_v123_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_sm252_sl63_2d_v124_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_sm252_sl126_2d_v125_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_sm21_sl21_2d_v126_signal(gm_industry_pctile, closeadj):
    base = _mean(gm_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_sm63_sl21_2d_v127_signal(gm_industry_pctile, closeadj):
    base = _mean(gm_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_sm63_sl63_2d_v128_signal(gm_industry_pctile, closeadj):
    base = _mean(gm_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_sm252_sl63_2d_v129_signal(gm_industry_pctile, closeadj):
    base = _mean(gm_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_sm252_sl126_2d_v130_signal(gm_industry_pctile, closeadj):
    base = _mean(gm_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm
def f051gmp_f051_gross_margin_power_gm_pctslope_21d_2d_v131_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm
def f051gmp_f051_gross_margin_power_gm_pctslope_63d_2d_v132_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm
def f051gmp_f051_gross_margin_power_gm_pctslope_252d_2d_v133_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_pctslope_21d_2d_v134_signal(gp, closeadj):
    base = gp
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_pctslope_63d_2d_v135_signal(gp, closeadj):
    base = gp
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_pctslope_252d_2d_v136_signal(gp, closeadj):
    base = gp
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_pctslope_21d_2d_v137_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_pctslope_63d_2d_v138_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_pctslope_252d_2d_v139_signal(grossmargin, closeadj):
    base = grossmargin
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_pctslope_21d_2d_v140_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_pctslope_63d_2d_v141_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_pctslope_252d_2d_v142_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_pctslope_21d_2d_v143_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_pctslope_63d_2d_v144_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_pctslope_252d_2d_v145_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_pctslope_21d_2d_v146_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_pctslope_63d_2d_v147_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_pctslope_252d_2d_v148_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_pctslope_21d_2d_v149_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_pctslope_63d_2d_v150_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_pctslope_252d_2d_v151_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_pctslope_21d_2d_v152_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_pctslope_63d_2d_v153_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_pctslope_252d_2d_v154_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_pctslope_21d_2d_v155_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_pctslope_63d_2d_v156_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_pctslope_252d_2d_v157_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_pctslope_21d_2d_v158_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_pctslope_63d_2d_v159_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_pctslope_252d_2d_v160_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_pctslope_21d_2d_v164_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_pctslope_63d_2d_v165_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_pctslope_252d_2d_v166_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_pctslope_21d_2d_v167_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_pctslope_63d_2d_v168_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_pctslope_252d_2d_v169_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm
def f051gmp_f051_gross_margin_power_gm_sgnslope_21d_2d_v170_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm
def f051gmp_f051_gross_margin_power_gm_sgnslope_63d_2d_v171_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm
def f051gmp_f051_gross_margin_power_gm_sgnslope_252d_2d_v172_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sgnslope_21d_2d_v173_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sgnslope_63d_2d_v174_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_sgnslope_252d_2d_v175_signal(gp, closeadj):
    base = gp
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sgnslope_21d_2d_v176_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sgnslope_63d_2d_v177_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_sgnslope_252d_2d_v178_signal(grossmargin, closeadj):
    base = grossmargin
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sgnslope_21d_2d_v179_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sgnslope_63d_2d_v180_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_sgnslope_252d_2d_v181_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sgnslope_21d_2d_v182_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sgnslope_63d_2d_v183_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_sgnslope_252d_2d_v184_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sgnslope_21d_2d_v185_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sgnslope_63d_2d_v186_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_sgnslope_252d_2d_v187_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sgnslope_21d_2d_v188_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sgnslope_63d_2d_v189_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_sgnslope_252d_2d_v190_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sgnslope_21d_2d_v191_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sgnslope_63d_2d_v192_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_sgnslope_252d_2d_v193_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sgnslope_21d_2d_v194_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sgnslope_63d_2d_v195_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_sgnslope_252d_2d_v196_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sgnslope_21d_2d_v197_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sgnslope_63d_2d_v198_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_sgnslope_252d_2d_v199_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

