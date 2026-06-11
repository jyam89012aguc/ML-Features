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
def _f052_om(opinc, revenue):
    return opinc / revenue.abs().replace(0, np.nan)


# 21d slope of opmargin
def f052opm_f052_operating_margin_opmargin_slope_21d_2d_v001_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opmargin
def f052opm_f052_operating_margin_opmargin_slope_63d_2d_v002_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opmargin
def f052opm_f052_operating_margin_opmargin_slope_126d_2d_v003_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opmargin
def f052opm_f052_operating_margin_opmargin_slope_252d_2d_v004_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opmargin
def f052opm_f052_operating_margin_opmargin_slope_504d_2d_v005_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slope_21d_2d_v006_signal(opinc, closeadj):
    base = opinc
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slope_63d_2d_v007_signal(opinc, closeadj):
    base = opinc
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slope_126d_2d_v008_signal(opinc, closeadj):
    base = opinc
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slope_252d_2d_v009_signal(opinc, closeadj):
    base = opinc
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slope_504d_2d_v010_signal(opinc, closeadj):
    base = opinc
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slope_21d_2d_v011_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slope_63d_2d_v012_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slope_126d_2d_v013_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slope_252d_2d_v014_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slope_504d_2d_v015_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slope_21d_2d_v016_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slope_63d_2d_v017_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slope_126d_2d_v018_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slope_252d_2d_v019_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slope_504d_2d_v020_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slope_21d_2d_v021_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slope_63d_2d_v022_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slope_126d_2d_v023_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slope_252d_2d_v024_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slope_504d_2d_v025_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slope_21d_2d_v026_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slope_63d_2d_v027_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slope_126d_2d_v028_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slope_252d_2d_v029_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slope_504d_2d_v030_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_slope_21d_2d_v031_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_slope_63d_2d_v032_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_slope_126d_2d_v033_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_slope_252d_2d_v034_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_slope_504d_2d_v035_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slope_21d_2d_v036_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slope_63d_2d_v037_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slope_126d_2d_v038_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slope_252d_2d_v039_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slope_504d_2d_v040_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slope_21d_2d_v041_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slope_63d_2d_v042_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slope_126d_2d_v043_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slope_252d_2d_v044_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slope_504d_2d_v045_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slope_21d_2d_v046_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slope_63d_2d_v047_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slope_126d_2d_v048_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slope_252d_2d_v049_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slope_504d_2d_v050_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slope_21d_2d_v056_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slope_63d_2d_v057_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slope_126d_2d_v058_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slope_252d_2d_v059_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slope_504d_2d_v060_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slope_21d_2d_v061_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slope_63d_2d_v062_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slope_126d_2d_v063_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slope_252d_2d_v064_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slope_504d_2d_v065_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sm21_sl21_2d_v066_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sm63_sl21_2d_v067_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sm63_sl63_2d_v068_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sm252_sl63_2d_v069_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sm252_sl126_2d_v070_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sm21_sl21_2d_v071_signal(opinc, closeadj):
    base = _mean(opinc, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sm63_sl21_2d_v072_signal(opinc, closeadj):
    base = _mean(opinc, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sm63_sl63_2d_v073_signal(opinc, closeadj):
    base = _mean(opinc, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sm252_sl63_2d_v074_signal(opinc, closeadj):
    base = _mean(opinc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sm252_sl126_2d_v075_signal(opinc, closeadj):
    base = _mean(opinc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sm21_sl21_2d_v076_signal(opinc, revenue, closeadj):
    base = _mean(opinc.pct_change(periods=252) - revenue.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sm63_sl21_2d_v077_signal(opinc, revenue, closeadj):
    base = _mean(opinc.pct_change(periods=252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sm63_sl63_2d_v078_signal(opinc, revenue, closeadj):
    base = _mean(opinc.pct_change(periods=252) - revenue.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sm252_sl63_2d_v079_signal(opinc, revenue, closeadj):
    base = _mean(opinc.pct_change(periods=252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sm252_sl126_2d_v080_signal(opinc, revenue, closeadj):
    base = _mean(opinc.pct_change(periods=252) - revenue.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sm21_sl21_2d_v081_signal(opex, revenue, closeadj):
    base = _mean(opex / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sm63_sl21_2d_v082_signal(opex, revenue, closeadj):
    base = _mean(opex / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sm63_sl63_2d_v083_signal(opex, revenue, closeadj):
    base = _mean(opex / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sm252_sl63_2d_v084_signal(opex, revenue, closeadj):
    base = _mean(opex / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sm252_sl126_2d_v085_signal(opex, revenue, closeadj):
    base = _mean(opex / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sm21_sl21_2d_v086_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sm63_sl21_2d_v087_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sm63_sl63_2d_v088_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sm252_sl63_2d_v089_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sm252_sl126_2d_v090_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sm21_sl21_2d_v091_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sm63_sl21_2d_v092_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sm63_sl63_2d_v093_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sm252_sl63_2d_v094_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sm252_sl126_2d_v095_signal(opinc, revenue, closeadj):
    base = _mean(_f052_om(opinc, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sm21_sl21_2d_v096_signal(opex, closeadj):
    base = _mean(opex.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sm63_sl21_2d_v097_signal(opex, closeadj):
    base = _mean(opex.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sm63_sl63_2d_v098_signal(opex, closeadj):
    base = _mean(opex.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sm252_sl63_2d_v099_signal(opex, closeadj):
    base = _mean(opex.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sm252_sl126_2d_v100_signal(opex, closeadj):
    base = _mean(opex.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sm21_sl21_2d_v101_signal(opinc, revenue, om_sector_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sm63_sl21_2d_v102_signal(opinc, revenue, om_sector_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sm63_sl63_2d_v103_signal(opinc, revenue, om_sector_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sm252_sl63_2d_v104_signal(opinc, revenue, om_sector_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sm252_sl126_2d_v105_signal(opinc, revenue, om_sector_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sm21_sl21_2d_v106_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sm63_sl21_2d_v107_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sm63_sl63_2d_v108_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sm252_sl63_2d_v109_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sm252_sl126_2d_v110_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sm21_sl21_2d_v111_signal(opinc, revenue, om_industry_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sm63_sl21_2d_v112_signal(opinc, revenue, om_industry_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sm63_sl63_2d_v113_signal(opinc, revenue, om_industry_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sm252_sl63_2d_v114_signal(opinc, revenue, om_industry_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sm252_sl126_2d_v115_signal(opinc, revenue, om_industry_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(opinc, revenue, om_mcap_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(opinc, revenue, om_mcap_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(opinc, revenue, om_mcap_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(opinc, revenue, om_mcap_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(opinc, revenue, om_mcap_med, closeadj):
    base = _mean((_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_sm21_sl21_2d_v121_signal(om_sector_pctile, closeadj):
    base = _mean(om_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_sm63_sl21_2d_v122_signal(om_sector_pctile, closeadj):
    base = _mean(om_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_sm63_sl63_2d_v123_signal(om_sector_pctile, closeadj):
    base = _mean(om_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_sm252_sl63_2d_v124_signal(om_sector_pctile, closeadj):
    base = _mean(om_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_sm252_sl126_2d_v125_signal(om_sector_pctile, closeadj):
    base = _mean(om_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_sm21_sl21_2d_v126_signal(om_industry_pctile, closeadj):
    base = _mean(om_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_sm63_sl21_2d_v127_signal(om_industry_pctile, closeadj):
    base = _mean(om_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_sm63_sl63_2d_v128_signal(om_industry_pctile, closeadj):
    base = _mean(om_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_sm252_sl63_2d_v129_signal(om_industry_pctile, closeadj):
    base = _mean(om_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_sm252_sl126_2d_v130_signal(om_industry_pctile, closeadj):
    base = _mean(om_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opmargin
def f052opm_f052_operating_margin_opmargin_pctslope_21d_2d_v131_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opmargin
def f052opm_f052_operating_margin_opmargin_pctslope_63d_2d_v132_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opmargin
def f052opm_f052_operating_margin_opmargin_pctslope_252d_2d_v133_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_pctslope_21d_2d_v134_signal(opinc, closeadj):
    base = opinc
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_pctslope_63d_2d_v135_signal(opinc, closeadj):
    base = opinc
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_pctslope_252d_2d_v136_signal(opinc, closeadj):
    base = opinc
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_pctslope_21d_2d_v137_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_pctslope_63d_2d_v138_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_pctslope_252d_2d_v139_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_pctslope_21d_2d_v140_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_pctslope_63d_2d_v141_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_pctslope_252d_2d_v142_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_pctslope_21d_2d_v143_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_pctslope_63d_2d_v144_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_pctslope_252d_2d_v145_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_pctslope_21d_2d_v146_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_pctslope_63d_2d_v147_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_pctslope_252d_2d_v148_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_pctslope_21d_2d_v149_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_pctslope_63d_2d_v150_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_pctslope_252d_2d_v151_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_pctslope_21d_2d_v152_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_pctslope_63d_2d_v153_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_pctslope_252d_2d_v154_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_pctslope_21d_2d_v155_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_pctslope_63d_2d_v156_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_pctslope_252d_2d_v157_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_pctslope_21d_2d_v158_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_pctslope_63d_2d_v159_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_pctslope_252d_2d_v160_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_pctslope_21d_2d_v164_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_pctslope_63d_2d_v165_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_pctslope_252d_2d_v166_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_pctslope_21d_2d_v167_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_pctslope_63d_2d_v168_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_pctslope_252d_2d_v169_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sgnslope_21d_2d_v170_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sgnslope_63d_2d_v171_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opmargin
def f052opm_f052_operating_margin_opmargin_sgnslope_252d_2d_v172_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sgnslope_21d_2d_v173_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sgnslope_63d_2d_v174_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_sgnslope_252d_2d_v175_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sgnslope_21d_2d_v176_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sgnslope_63d_2d_v177_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_sgnslope_252d_2d_v178_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sgnslope_21d_2d_v179_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sgnslope_63d_2d_v180_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_sgnslope_252d_2d_v181_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sgnslope_21d_2d_v182_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sgnslope_63d_2d_v183_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_sgnslope_252d_2d_v184_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sgnslope_21d_2d_v185_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sgnslope_63d_2d_v186_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_sgnslope_252d_2d_v187_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sgnslope_21d_2d_v188_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sgnslope_63d_2d_v189_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opex_growth
def f052opm_f052_operating_margin_opex_growth_sgnslope_252d_2d_v190_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sgnslope_21d_2d_v191_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sgnslope_63d_2d_v192_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_sgnslope_252d_2d_v193_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sgnslope_21d_2d_v194_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sgnslope_63d_2d_v195_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_sgnslope_252d_2d_v196_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sgnslope_21d_2d_v197_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sgnslope_63d_2d_v198_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_sgnslope_252d_2d_v199_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

