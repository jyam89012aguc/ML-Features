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


# 63d z-score of opmargin
def f052opm_f052_operating_margin_opmargin_z_63d_base_v076_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opmargin
def f052opm_f052_operating_margin_opmargin_z_126d_base_v077_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opmargin
def f052opm_f052_operating_margin_opmargin_z_252d_base_v078_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opmargin
def f052opm_f052_operating_margin_opmargin_z_504d_base_v079_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_z_63d_base_v080_signal(opinc, closeadj):
    base = opinc
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_z_126d_base_v081_signal(opinc, closeadj):
    base = opinc
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_z_252d_base_v082_signal(opinc, closeadj):
    base = opinc
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_z_504d_base_v083_signal(opinc, closeadj):
    base = opinc
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_z_63d_base_v084_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_z_126d_base_v085_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_z_252d_base_v086_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_z_504d_base_v087_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_z_63d_base_v088_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_z_126d_base_v089_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_z_252d_base_v090_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_z_504d_base_v091_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_z_63d_base_v092_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_z_126d_base_v093_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_z_252d_base_v094_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_z_504d_base_v095_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_z_63d_base_v096_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_z_126d_base_v097_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_z_252d_base_v098_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_z_504d_base_v099_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of opex_growth
def f052opm_f052_operating_margin_opex_growth_z_63d_base_v100_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opex_growth
def f052opm_f052_operating_margin_opex_growth_z_126d_base_v101_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opex_growth
def f052opm_f052_operating_margin_opex_growth_z_252d_base_v102_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opex_growth
def f052opm_f052_operating_margin_opex_growth_z_504d_base_v103_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_z_63d_base_v104_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_z_126d_base_v105_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_z_252d_base_v106_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_z_504d_base_v107_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_z_63d_base_v108_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_z_126d_base_v109_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_z_252d_base_v110_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_z_504d_base_v111_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_z_63d_base_v112_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_z_126d_base_v113_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_z_252d_base_v114_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_z_504d_base_v115_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_z_63d_base_v116_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_z_126d_base_v117_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_z_252d_base_v118_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_z_504d_base_v119_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_z_63d_base_v120_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_z_126d_base_v121_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_z_252d_base_v122_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_z_504d_base_v123_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_z_63d_base_v124_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_z_126d_base_v125_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_z_252d_base_v126_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_z_504d_base_v127_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opmargin
def f052opm_f052_operating_margin_opmargin_distmax_252d_base_v128_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opmargin
def f052opm_f052_operating_margin_opmargin_distmax_504d_base_v129_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_distmax_252d_base_v130_signal(opinc, closeadj):
    base = opinc
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_distmax_504d_base_v131_signal(opinc, closeadj):
    base = opinc
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_distmax_252d_base_v132_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_distmax_504d_base_v133_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_distmax_252d_base_v134_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_distmax_504d_base_v135_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_distmax_252d_base_v136_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_distmax_504d_base_v137_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_distmax_252d_base_v138_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_distmax_504d_base_v139_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opex_growth
def f052opm_f052_operating_margin_opex_growth_distmax_252d_base_v140_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opex_growth
def f052opm_f052_operating_margin_opex_growth_distmax_504d_base_v141_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_distmax_252d_base_v142_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_distmax_504d_base_v143_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_distmax_252d_base_v144_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_peer_sector_z
def f052opm_f052_operating_margin_om_peer_sector_z_distmax_504d_base_v145_signal(opinc, revenue, om_sector_med, om_sector_std, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_distmax_252d_base_v146_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_peer_industry_dist
def f052opm_f052_operating_margin_om_peer_industry_dist_distmax_504d_base_v147_signal(opinc, revenue, om_industry_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_industry_med) / om_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_peer_mcap_bucket_dist
def f052opm_f052_operating_margin_om_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(opinc, revenue, om_mcap_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_mcap_med) / om_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_distmax_252d_base_v150_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_peer_sector_pctile
def f052opm_f052_operating_margin_om_peer_sector_pctile_distmax_504d_base_v151_signal(om_sector_pctile, closeadj):
    base = om_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_distmax_252d_base_v152_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_peer_industry_pctile
def f052opm_f052_operating_margin_om_peer_industry_pctile_distmax_504d_base_v153_signal(om_industry_pctile, closeadj):
    base = om_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opmargin
def f052opm_f052_operating_margin_opmargin_distmed_126d_base_v154_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opmargin
def f052opm_f052_operating_margin_opmargin_distmed_252d_base_v155_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opmargin
def f052opm_f052_operating_margin_opmargin_distmed_504d_base_v156_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_distmed_126d_base_v157_signal(opinc, closeadj):
    base = opinc
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_distmed_252d_base_v158_signal(opinc, closeadj):
    base = opinc
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opinc_lvl
def f052opm_f052_operating_margin_opinc_lvl_distmed_504d_base_v159_signal(opinc, closeadj):
    base = opinc
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_distmed_126d_base_v160_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_distmed_252d_base_v161_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of op_lev_proxy
def f052opm_f052_operating_margin_op_lev_proxy_distmed_504d_base_v162_signal(opinc, revenue, closeadj):
    base = opinc.pct_change(periods=252) - revenue.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_distmed_126d_base_v163_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_distmed_252d_base_v164_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opex_to_rev
def f052opm_f052_operating_margin_opex_to_rev_distmed_504d_base_v165_signal(opex, revenue, closeadj):
    base = opex / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_distmed_126d_base_v166_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_distmed_252d_base_v167_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of om_yoy_chg
def f052opm_f052_operating_margin_om_yoy_chg_distmed_504d_base_v168_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_distmed_126d_base_v169_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_distmed_252d_base_v170_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of om_vol_252
def f052opm_f052_operating_margin_om_vol_252_distmed_504d_base_v171_signal(opinc, revenue, closeadj):
    base = _f052_om(opinc, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opex_growth
def f052opm_f052_operating_margin_opex_growth_distmed_126d_base_v172_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opex_growth
def f052opm_f052_operating_margin_opex_growth_distmed_252d_base_v173_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opex_growth
def f052opm_f052_operating_margin_opex_growth_distmed_504d_base_v174_signal(opex, closeadj):
    base = opex.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of om_peer_sector_dist
def f052opm_f052_operating_margin_om_peer_sector_dist_distmed_126d_base_v175_signal(opinc, revenue, om_sector_med, closeadj):
    base = (_f052_om(opinc, revenue) - om_sector_med) / om_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

