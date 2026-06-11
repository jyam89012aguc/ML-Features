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
def _f052_om(opinc, revenue):
    return opinc / revenue.abs().replace(0, np.nan)


# 21d mean of opmargin scaled by closeadj
def f052opm_f052_operating_margin_opmargin_mean_21d_base_v001_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opmargin scaled by closeadj
def f052opm_f052_operating_margin_opmargin_mean_63d_base_v002_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opmargin scaled by closeadj
def f052opm_f052_operating_margin_opmargin_mean_126d_base_v003_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opmargin scaled by closeadj
def f052opm_f052_operating_margin_opmargin_mean_252d_base_v004_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opmargin scaled by closeadj
def f052opm_f052_operating_margin_opmargin_mean_504d_base_v005_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opinc_lvl scaled by closeadj
def f052opm_f052_operating_margin_opinc_lvl_mean_21d_base_v006_signal(opinc, closeadj):
    base = opinc
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opinc_lvl scaled by closeadj
def f052opm_f052_operating_margin_opinc_lvl_mean_63d_base_v007_signal(opinc, closeadj):
    base = opinc
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opinc_lvl scaled by closeadj
def f052opm_f052_operating_margin_opinc_lvl_mean_126d_base_v008_signal(opinc, closeadj):
    base = opinc
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opinc_lvl scaled by closeadj
def f052opm_f052_operating_margin_opinc_lvl_mean_252d_base_v009_signal(opinc, closeadj):
    base = opinc
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opinc_lvl scaled by closeadj
def f052opm_f052_operating_margin_opinc_lvl_mean_504d_base_v010_signal(opinc, closeadj):
    base = opinc
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of op_lev_proxy scaled by closeadj
def f052opm_f052_operating_margin_op_lev_proxy_mean_21d_base_v011_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of op_lev_proxy scaled by closeadj
def f052opm_f052_operating_margin_op_lev_proxy_mean_63d_base_v012_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of op_lev_proxy scaled by closeadj
def f052opm_f052_operating_margin_op_lev_proxy_mean_126d_base_v013_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of op_lev_proxy scaled by closeadj
def f052opm_f052_operating_margin_op_lev_proxy_mean_252d_base_v014_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of op_lev_proxy scaled by closeadj
def f052opm_f052_operating_margin_op_lev_proxy_mean_504d_base_v015_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opex_to_rev scaled by closeadj
def f052opm_f052_operating_margin_opex_to_rev_mean_21d_base_v016_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opex_to_rev scaled by closeadj
def f052opm_f052_operating_margin_opex_to_rev_mean_63d_base_v017_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opex_to_rev scaled by closeadj
def f052opm_f052_operating_margin_opex_to_rev_mean_126d_base_v018_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opex_to_rev scaled by closeadj
def f052opm_f052_operating_margin_opex_to_rev_mean_252d_base_v019_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opex_to_rev scaled by closeadj
def f052opm_f052_operating_margin_opex_to_rev_mean_504d_base_v020_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_yoy_chg scaled by closeadj
def f052opm_f052_operating_margin_om_yoy_chg_mean_21d_base_v021_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_yoy_chg scaled by closeadj
def f052opm_f052_operating_margin_om_yoy_chg_mean_63d_base_v022_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_yoy_chg scaled by closeadj
def f052opm_f052_operating_margin_om_yoy_chg_mean_126d_base_v023_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_yoy_chg scaled by closeadj
def f052opm_f052_operating_margin_om_yoy_chg_mean_252d_base_v024_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_yoy_chg scaled by closeadj
def f052opm_f052_operating_margin_om_yoy_chg_mean_504d_base_v025_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_vol_252 scaled by closeadj
def f052opm_f052_operating_margin_om_vol_252_mean_21d_base_v026_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_vol_252 scaled by closeadj
def f052opm_f052_operating_margin_om_vol_252_mean_63d_base_v027_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_vol_252 scaled by closeadj
def f052opm_f052_operating_margin_om_vol_252_mean_126d_base_v028_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_vol_252 scaled by closeadj
def f052opm_f052_operating_margin_om_vol_252_mean_252d_base_v029_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_vol_252 scaled by closeadj
def f052opm_f052_operating_margin_om_vol_252_mean_504d_base_v030_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opex_growth scaled by closeadj
def f052opm_f052_operating_margin_opex_growth_mean_21d_base_v031_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opex_growth scaled by closeadj
def f052opm_f052_operating_margin_opex_growth_mean_63d_base_v032_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opex_growth scaled by closeadj
def f052opm_f052_operating_margin_opex_growth_mean_126d_base_v033_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opex_growth scaled by closeadj
def f052opm_f052_operating_margin_opex_growth_mean_252d_base_v034_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opex_growth scaled by closeadj
def f052opm_f052_operating_margin_opex_growth_mean_504d_base_v035_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_peer_sector_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_dist_mean_21d_base_v036_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_peer_sector_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_dist_mean_63d_base_v037_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_peer_sector_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_dist_mean_126d_base_v038_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_peer_sector_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_dist_mean_252d_base_v039_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_peer_sector_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_dist_mean_504d_base_v040_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_peer_sector_z scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_z_mean_21d_base_v041_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_peer_sector_z scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_z_mean_63d_base_v042_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_peer_sector_z scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_z_mean_126d_base_v043_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_peer_sector_z scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_z_mean_252d_base_v044_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_peer_sector_z scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_z_mean_504d_base_v045_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_peer_industry_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_dist_mean_21d_base_v046_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_peer_industry_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_dist_mean_63d_base_v047_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_peer_industry_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_dist_mean_126d_base_v048_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_peer_industry_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_dist_mean_252d_base_v049_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_peer_industry_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_dist_mean_504d_base_v050_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_peer_mcap_bucket_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_mean_21d_base_v051_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_peer_mcap_bucket_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_mean_63d_base_v052_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_peer_mcap_bucket_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_mean_126d_base_v053_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_peer_mcap_bucket_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_mean_252d_base_v054_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_peer_mcap_bucket_dist scaled by closeadj
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_mean_504d_base_v055_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_peer_sector_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_pctile_mean_21d_base_v056_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_peer_sector_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_pctile_mean_63d_base_v057_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_peer_sector_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_pctile_mean_126d_base_v058_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_peer_sector_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_pctile_mean_252d_base_v059_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_peer_sector_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_sector_pctile_mean_504d_base_v060_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_peer_industry_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_pctile_mean_21d_base_v061_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_peer_industry_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_pctile_mean_63d_base_v062_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_peer_industry_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_pctile_mean_126d_base_v063_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_peer_industry_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_pctile_mean_252d_base_v064_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_peer_industry_pctile scaled by closeadj
def f052opm_f052_operating_margin_om_peer_industry_pctile_mean_504d_base_v065_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opmargin
def f052opm_f052_operating_margin_opmargin_median_63d_base_v066_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opmargin
def f052opm_f052_operating_margin_opmargin_median_252d_base_v067_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opmargin
def f052opm_f052_operating_margin_opmargin_median_504d_base_v068_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_median_63d_base_v069_signal(opinc, closeadj):
    base = opinc
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_median_252d_base_v070_signal(opinc, closeadj):
    base = opinc
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_median_504d_base_v071_signal(opinc, closeadj):
    base = opinc
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_median_63d_base_v072_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_median_252d_base_v073_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_median_504d_base_v074_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_median_63d_base_v075_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_median_252d_base_v076_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_median_504d_base_v077_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_median_63d_base_v078_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_median_252d_base_v079_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_median_504d_base_v080_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_median_63d_base_v081_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_median_252d_base_v082_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_median_504d_base_v083_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opex_growth
def f052opm_f052_operating_margin_opex_growth_median_63d_base_v084_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opex_growth
def f052opm_f052_operating_margin_opex_growth_median_252d_base_v085_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opex_growth
def f052opm_f052_operating_margin_opex_growth_median_504d_base_v086_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_median_63d_base_v087_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_median_252d_base_v088_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_median_504d_base_v089_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_median_63d_base_v090_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_median_252d_base_v091_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_median_504d_base_v092_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_median_63d_base_v093_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_median_252d_base_v094_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_median_504d_base_v095_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_median_63d_base_v096_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_median_252d_base_v097_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_median_504d_base_v098_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_median_63d_base_v099_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_median_252d_base_v100_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

