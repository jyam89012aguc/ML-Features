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
def _f051_gm(gp, revenue):
    return gp / revenue.abs().replace(0, np.nan)


# 21d mean of gm scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_mean_21d_base_v001_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_mean_63d_base_v002_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_mean_126d_base_v003_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_mean_252d_base_v004_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_mean_504d_base_v005_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_lvl_mean_21d_base_v006_signal(gp, closeadj):
    base = gp
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_lvl_mean_63d_base_v007_signal(gp, closeadj):
    base = gp
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_lvl_mean_126d_base_v008_signal(gp, closeadj):
    base = gp
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_lvl_mean_252d_base_v009_signal(gp, closeadj):
    base = gp
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_lvl_mean_504d_base_v010_signal(gp, closeadj):
    base = gp
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of grossmargin_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_grossmargin_lvl_mean_21d_base_v011_signal(grossmargin, closeadj):
    base = grossmargin
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of grossmargin_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_grossmargin_lvl_mean_63d_base_v012_signal(grossmargin, closeadj):
    base = grossmargin
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of grossmargin_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_grossmargin_lvl_mean_126d_base_v013_signal(grossmargin, closeadj):
    base = grossmargin
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of grossmargin_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_grossmargin_lvl_mean_252d_base_v014_signal(grossmargin, closeadj):
    base = grossmargin
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of grossmargin_lvl scaled by closeadj
def f051gmp_f051_gross_margin_power_grossmargin_lvl_mean_504d_base_v015_signal(grossmargin, closeadj):
    base = grossmargin
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_growth_y scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_growth_y_mean_21d_base_v016_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_growth_y scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_growth_y_mean_63d_base_v017_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_growth_y scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_growth_y_mean_126d_base_v018_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_growth_y scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_growth_y_mean_252d_base_v019_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_growth_y scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_growth_y_mean_504d_base_v020_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_yoy_chg scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_yoy_chg_mean_21d_base_v021_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_yoy_chg scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_yoy_chg_mean_63d_base_v022_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_yoy_chg scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_yoy_chg_mean_126d_base_v023_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_yoy_chg scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_yoy_chg_mean_252d_base_v024_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_yoy_chg scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_yoy_chg_mean_504d_base_v025_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_vol_252 scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_vol_252_mean_21d_base_v026_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_vol_252 scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_vol_252_mean_63d_base_v027_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_vol_252 scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_vol_252_mean_126d_base_v028_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_vol_252 scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_vol_252_mean_252d_base_v029_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_vol_252 scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_vol_252_mean_504d_base_v030_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gp_to_rnd scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_to_rnd_mean_21d_base_v031_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gp_to_rnd scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_to_rnd_mean_63d_base_v032_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gp_to_rnd scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_to_rnd_mean_126d_base_v033_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gp_to_rnd scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_to_rnd_mean_252d_base_v034_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gp_to_rnd scaled by closeadj
def f051gmp_f051_gross_margin_power_gp_to_rnd_mean_504d_base_v035_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_peer_sector_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_mean_21d_base_v036_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_peer_sector_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_mean_63d_base_v037_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_peer_sector_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_mean_126d_base_v038_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_peer_sector_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_mean_252d_base_v039_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_peer_sector_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_mean_504d_base_v040_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_peer_sector_z scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_mean_21d_base_v041_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_peer_sector_z scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_mean_63d_base_v042_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_peer_sector_z scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_mean_126d_base_v043_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_peer_sector_z scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_mean_252d_base_v044_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_peer_sector_z scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_mean_504d_base_v045_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_peer_industry_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_mean_21d_base_v046_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_peer_industry_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_mean_63d_base_v047_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_peer_industry_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_mean_126d_base_v048_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_peer_industry_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_mean_252d_base_v049_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_peer_industry_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_mean_504d_base_v050_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_peer_mcap_bucket_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_mean_21d_base_v051_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_peer_mcap_bucket_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_mean_63d_base_v052_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_peer_mcap_bucket_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_mean_126d_base_v053_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_peer_mcap_bucket_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_mean_252d_base_v054_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_peer_mcap_bucket_dist scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_mean_504d_base_v055_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_peer_sector_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_mean_21d_base_v056_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_peer_sector_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_mean_63d_base_v057_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_peer_sector_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_mean_126d_base_v058_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_peer_sector_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_mean_252d_base_v059_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_peer_sector_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_mean_504d_base_v060_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_peer_industry_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_mean_21d_base_v061_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_peer_industry_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_mean_63d_base_v062_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_peer_industry_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_mean_126d_base_v063_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_peer_industry_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_mean_252d_base_v064_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_peer_industry_pctile scaled by closeadj
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_mean_504d_base_v065_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm
def f051gmp_f051_gross_margin_power_gm_median_63d_base_v066_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm
def f051gmp_f051_gross_margin_power_gm_median_252d_base_v067_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm
def f051gmp_f051_gross_margin_power_gm_median_504d_base_v068_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_median_63d_base_v069_signal(gp, closeadj):
    base = gp
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_median_252d_base_v070_signal(gp, closeadj):
    base = gp
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_median_504d_base_v071_signal(gp, closeadj):
    base = gp
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_median_63d_base_v072_signal(grossmargin, closeadj):
    base = grossmargin
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_median_252d_base_v073_signal(grossmargin, closeadj):
    base = grossmargin
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_median_504d_base_v074_signal(grossmargin, closeadj):
    base = grossmargin
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_median_63d_base_v075_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_median_252d_base_v076_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_median_504d_base_v077_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_median_63d_base_v078_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_median_252d_base_v079_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_median_504d_base_v080_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_median_63d_base_v081_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_median_252d_base_v082_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_median_504d_base_v083_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_median_63d_base_v084_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_median_252d_base_v085_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_median_504d_base_v086_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_median_63d_base_v087_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_median_252d_base_v088_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_median_504d_base_v089_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_median_63d_base_v090_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_median_252d_base_v091_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_median_504d_base_v092_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_median_63d_base_v093_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_median_252d_base_v094_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_median_504d_base_v095_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_median_63d_base_v096_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_median_252d_base_v097_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_median_504d_base_v098_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_median_63d_base_v099_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_median_252d_base_v100_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

