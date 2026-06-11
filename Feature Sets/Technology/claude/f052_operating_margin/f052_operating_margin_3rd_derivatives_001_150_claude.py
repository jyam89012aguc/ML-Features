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


# 21d acceleration of opmargin
def f052opm_f052_operating_margin_opmargin_accel_21d_3d_v001_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opmargin
def f052opm_f052_operating_margin_opmargin_accel_63d_3d_v002_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opmargin
def f052opm_f052_operating_margin_opmargin_accel_126d_3d_v003_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opmargin
def f052opm_f052_operating_margin_opmargin_accel_252d_3d_v004_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_accel_21d_3d_v005_signal(opinc, closeadj):
    base = opinc
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_accel_63d_3d_v006_signal(opinc, closeadj):
    base = opinc
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_accel_126d_3d_v007_signal(opinc, closeadj):
    base = opinc
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_accel_252d_3d_v008_signal(opinc, closeadj):
    base = opinc
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_accel_21d_3d_v009_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_accel_63d_3d_v010_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_accel_126d_3d_v011_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_accel_252d_3d_v012_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_accel_21d_3d_v013_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_accel_63d_3d_v014_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_accel_126d_3d_v015_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_accel_252d_3d_v016_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_accel_21d_3d_v017_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_accel_63d_3d_v018_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_accel_126d_3d_v019_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_accel_252d_3d_v020_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_accel_21d_3d_v021_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_accel_63d_3d_v022_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_accel_126d_3d_v023_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_accel_252d_3d_v024_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opex_growth
def f052opm_f052_operating_margin_opex_growth_accel_21d_3d_v025_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_growth
def f052opm_f052_operating_margin_opex_growth_accel_63d_3d_v026_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opex_growth
def f052opm_f052_operating_margin_opex_growth_accel_126d_3d_v027_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_growth
def f052opm_f052_operating_margin_opex_growth_accel_252d_3d_v028_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_accel_21d_3d_v029_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_accel_63d_3d_v030_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_accel_126d_3d_v031_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_accel_252d_3d_v032_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_accel_21d_3d_v033_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_accel_63d_3d_v034_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_accel_126d_3d_v035_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_accel_252d_3d_v036_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_accel_21d_3d_v037_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_accel_63d_3d_v038_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_accel_126d_3d_v039_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_accel_252d_3d_v040_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_accel_21d_3d_v045_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_accel_63d_3d_v046_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_accel_126d_3d_v047_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_accel_252d_3d_v048_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_accel_21d_3d_v049_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_accel_63d_3d_v050_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_accel_126d_3d_v051_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_accel_252d_3d_v052_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opmargin
def f052opm_f052_operating_margin_opmargin_slopez_21d_z126_3d_v053_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opmargin
def f052opm_f052_operating_margin_opmargin_slopez_63d_z252_3d_v054_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opmargin
def f052opm_f052_operating_margin_opmargin_slopez_126d_z252_3d_v055_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opmargin
def f052opm_f052_operating_margin_opmargin_slopez_252d_z504_3d_v056_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slopez_21d_z126_3d_v057_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slopez_63d_z252_3d_v058_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slopez_126d_z252_3d_v059_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_slopez_252d_z504_3d_v060_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slopez_21d_z126_3d_v061_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slopez_63d_z252_3d_v062_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slopez_126d_z252_3d_v063_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_slopez_252d_z504_3d_v064_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slopez_21d_z126_3d_v065_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slopez_63d_z252_3d_v066_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slopez_126d_z252_3d_v067_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_slopez_252d_z504_3d_v068_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slopez_21d_z126_3d_v069_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slopez_63d_z252_3d_v070_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slopez_126d_z252_3d_v071_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_slopez_252d_z504_3d_v072_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slopez_21d_z126_3d_v073_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slopez_63d_z252_3d_v074_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slopez_126d_z252_3d_v075_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_slopez_252d_z504_3d_v076_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opex_growth
def f052opm_f052_operating_margin_opex_growth_slopez_21d_z126_3d_v077_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opex_growth
def f052opm_f052_operating_margin_opex_growth_slopez_63d_z252_3d_v078_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opex_growth
def f052opm_f052_operating_margin_opex_growth_slopez_126d_z252_3d_v079_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opex_growth
def f052opm_f052_operating_margin_opex_growth_slopez_252d_z504_3d_v080_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slopez_21d_z126_3d_v081_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slopez_63d_z252_3d_v082_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slopez_126d_z252_3d_v083_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_slopez_252d_z504_3d_v084_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slopez_21d_z126_3d_v085_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slopez_63d_z252_3d_v086_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slopez_126d_z252_3d_v087_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_slopez_252d_z504_3d_v088_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slopez_21d_z126_3d_v089_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slopez_63d_z252_3d_v090_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slopez_126d_z252_3d_v091_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_slopez_252d_z504_3d_v092_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opmargin
def f052opm_f052_operating_margin_opmargin_jerk_21d_3d_v105_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opmargin
def f052opm_f052_operating_margin_opmargin_jerk_63d_3d_v106_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opmargin
def f052opm_f052_operating_margin_opmargin_jerk_126d_3d_v107_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_jerk_21d_3d_v108_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_jerk_63d_3d_v109_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_jerk_126d_3d_v110_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_jerk_21d_3d_v111_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_jerk_63d_3d_v112_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_jerk_126d_3d_v113_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_jerk_21d_3d_v114_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_jerk_63d_3d_v115_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_jerk_126d_3d_v116_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_jerk_21d_3d_v117_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_jerk_63d_3d_v118_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_jerk_126d_3d_v119_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_jerk_21d_3d_v120_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_jerk_63d_3d_v121_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_jerk_126d_3d_v122_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opex_growth
def f052opm_f052_operating_margin_opex_growth_jerk_21d_3d_v123_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opex_growth
def f052opm_f052_operating_margin_opex_growth_jerk_63d_3d_v124_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opex_growth
def f052opm_f052_operating_margin_opex_growth_jerk_126d_3d_v125_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_jerk_21d_3d_v126_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_jerk_63d_3d_v127_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_jerk_126d_3d_v128_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_jerk_21d_3d_v129_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_jerk_63d_3d_v130_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_jerk_126d_3d_v131_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_jerk_21d_3d_v132_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_jerk_63d_3d_v133_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_jerk_126d_3d_v134_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_jerk_21d_3d_v138_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_jerk_63d_3d_v139_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_jerk_126d_3d_v140_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_jerk_21d_3d_v141_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_jerk_63d_3d_v142_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_jerk_126d_3d_v143_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opmargin smoothed over 252d
def f052opm_f052_operating_margin_opmargin_smoothaccel_63d_sm252_3d_v144_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opmargin smoothed over 504d
def f052opm_f052_operating_margin_opmargin_smoothaccel_252d_sm504_3d_v145_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opinc_lvl smoothed over 252d
def f052opm_f052_operating_margin_opinc_lvl_smoothaccel_63d_sm252_3d_v146_signal(opinc, closeadj):
    base = opinc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opinc_lvl smoothed over 504d
def f052opm_f052_operating_margin_opinc_lvl_smoothaccel_252d_sm504_3d_v147_signal(opinc, closeadj):
    base = opinc
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of op_lev_proxy smoothed over 252d
def f052opm_f052_operating_margin_op_lev_proxy_smoothaccel_63d_sm252_3d_v148_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of op_lev_proxy smoothed over 504d
def f052opm_f052_operating_margin_op_lev_proxy_smoothaccel_252d_sm504_3d_v149_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opex_to_rev smoothed over 252d
def f052opm_f052_operating_margin_opex_to_rev_smoothaccel_63d_sm252_3d_v150_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opex_to_rev smoothed over 504d
def f052opm_f052_operating_margin_opex_to_rev_smoothaccel_252d_sm504_3d_v151_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_yoy_chg smoothed over 252d
def f052opm_f052_operating_margin_om_yoy_chg_smoothaccel_63d_sm252_3d_v152_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_yoy_chg smoothed over 504d
def f052opm_f052_operating_margin_om_yoy_chg_smoothaccel_252d_sm504_3d_v153_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_vol_252 smoothed over 252d
def f052opm_f052_operating_margin_om_vol_252_smoothaccel_63d_sm252_3d_v154_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_vol_252 smoothed over 504d
def f052opm_f052_operating_margin_om_vol_252_smoothaccel_252d_sm504_3d_v155_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opex_growth smoothed over 252d
def f052opm_f052_operating_margin_opex_growth_smoothaccel_63d_sm252_3d_v156_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opex_growth smoothed over 504d
def f052opm_f052_operating_margin_opex_growth_smoothaccel_252d_sm504_3d_v157_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_peer_sector_dist smoothed over 252d
def f052opm_f052_operating_margin_om_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_peer_sector_dist smoothed over 504d
def f052opm_f052_operating_margin_om_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_peer_sector_z smoothed over 252d
def f052opm_f052_operating_margin_om_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_peer_sector_z smoothed over 504d
def f052opm_f052_operating_margin_om_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_peer_industry_dist smoothed over 252d
def f052opm_f052_operating_margin_om_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_peer_industry_dist smoothed over 504d
def f052opm_f052_operating_margin_om_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_peer_mcap_bucket_dist smoothed over 252d
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_peer_mcap_bucket_dist smoothed over 504d
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_peer_sector_pctile smoothed over 252d
def f052opm_f052_operating_margin_om_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_peer_sector_pctile smoothed over 504d
def f052opm_f052_operating_margin_om_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_peer_industry_pctile smoothed over 252d
def f052opm_f052_operating_margin_om_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_peer_industry_pctile smoothed over 504d
def f052opm_f052_operating_margin_om_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opmargin
def f052opm_f052_operating_margin_opmargin_accelz_21d_z252_3d_v170_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opmargin
def f052opm_f052_operating_margin_opmargin_accelz_63d_z504_3d_v171_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_accelz_21d_z252_3d_v172_signal(opinc, closeadj):
    base = opinc
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_accelz_63d_z504_3d_v173_signal(opinc, closeadj):
    base = opinc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_accelz_21d_z252_3d_v174_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_accelz_63d_z504_3d_v175_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_accelz_21d_z252_3d_v176_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_accelz_63d_z504_3d_v177_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_accelz_21d_z252_3d_v178_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_accelz_63d_z504_3d_v179_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_accelz_21d_z252_3d_v180_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_accelz_63d_z504_3d_v181_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opex_growth
def f052opm_f052_operating_margin_opex_growth_accelz_21d_z252_3d_v182_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opex_growth
def f052opm_f052_operating_margin_opex_growth_accelz_63d_z504_3d_v183_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_accelz_21d_z252_3d_v184_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_accelz_63d_z504_3d_v185_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_accelz_21d_z252_3d_v186_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_accelz_63d_z504_3d_v187_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_accelz_21d_z252_3d_v188_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_accelz_63d_z504_3d_v189_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opmargin (raw count, no price scaling)
def f052opm_f052_operating_margin_opmargin_signflip_63d_3d_v196_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opmargin (raw count, no price scaling)
def f052opm_f052_operating_margin_opmargin_signflip_252d_3d_v197_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opinc_lvl (raw count, no price scaling)
def f052opm_f052_operating_margin_opinc_lvl_signflip_63d_3d_v198_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opinc_lvl (raw count, no price scaling)
def f052opm_f052_operating_margin_opinc_lvl_signflip_252d_3d_v199_signal(opinc, closeadj):
    base = opinc
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in op_lev_proxy (raw count, no price scaling)
def f052opm_f052_operating_margin_op_lev_proxy_signflip_63d_3d_v200_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

