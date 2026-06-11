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


# 63d z-score of gm
def f051gmp_f051_gross_margin_power_gm_z_63d_base_v076_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm
def f051gmp_f051_gross_margin_power_gm_z_126d_base_v077_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm
def f051gmp_f051_gross_margin_power_gm_z_252d_base_v078_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm
def f051gmp_f051_gross_margin_power_gm_z_504d_base_v079_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_z_63d_base_v080_signal(gp, closeadj):
    base = gp
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_z_126d_base_v081_signal(gp, closeadj):
    base = gp
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_z_252d_base_v082_signal(gp, closeadj):
    base = gp
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_z_504d_base_v083_signal(gp, closeadj):
    base = gp
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_z_63d_base_v084_signal(grossmargin, closeadj):
    base = grossmargin
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_z_126d_base_v085_signal(grossmargin, closeadj):
    base = grossmargin
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_z_252d_base_v086_signal(grossmargin, closeadj):
    base = grossmargin
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_z_504d_base_v087_signal(grossmargin, closeadj):
    base = grossmargin
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_z_63d_base_v088_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_z_126d_base_v089_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_z_252d_base_v090_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_z_504d_base_v091_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_z_63d_base_v092_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_z_126d_base_v093_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_z_252d_base_v094_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_z_504d_base_v095_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_z_63d_base_v096_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_z_126d_base_v097_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_z_252d_base_v098_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_z_504d_base_v099_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_z_63d_base_v100_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_z_126d_base_v101_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_z_252d_base_v102_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_z_504d_base_v103_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_z_63d_base_v104_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_z_126d_base_v105_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_z_252d_base_v106_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_z_504d_base_v107_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_z_63d_base_v108_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_z_126d_base_v109_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_z_252d_base_v110_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_z_504d_base_v111_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_z_63d_base_v112_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_z_126d_base_v113_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_z_252d_base_v114_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_z_504d_base_v115_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_z_63d_base_v116_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_z_126d_base_v117_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_z_252d_base_v118_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_z_504d_base_v119_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_z_63d_base_v120_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_z_126d_base_v121_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_z_252d_base_v122_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_z_504d_base_v123_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_z_63d_base_v124_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_z_126d_base_v125_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_z_252d_base_v126_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_z_504d_base_v127_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm
def f051gmp_f051_gross_margin_power_gm_distmax_252d_base_v128_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm
def f051gmp_f051_gross_margin_power_gm_distmax_504d_base_v129_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_distmax_252d_base_v130_signal(gp, closeadj):
    base = gp
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_distmax_504d_base_v131_signal(gp, closeadj):
    base = gp
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_distmax_252d_base_v132_signal(grossmargin, closeadj):
    base = grossmargin
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_distmax_504d_base_v133_signal(grossmargin, closeadj):
    base = grossmargin
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_distmax_252d_base_v134_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_distmax_504d_base_v135_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_distmax_252d_base_v136_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_distmax_504d_base_v137_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_distmax_252d_base_v138_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_distmax_504d_base_v139_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_distmax_252d_base_v140_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_distmax_504d_base_v141_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_distmax_252d_base_v142_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_distmax_504d_base_v143_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_distmax_252d_base_v144_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_peer_sector_z
def f051gmp_f051_gross_margin_power_gm_peer_sector_z_distmax_504d_base_v145_signal(gp, revenue, gm_sector_med, gm_sector_std, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_distmax_252d_base_v146_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_peer_industry_dist
def f051gmp_f051_gross_margin_power_gm_peer_industry_dist_distmax_504d_base_v147_signal(gp, revenue, gm_industry_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_industry_med) / gm_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_peer_mcap_bucket_dist
def f051gmp_f051_gross_margin_power_gm_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(gp, revenue, gm_mcap_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_mcap_med) / gm_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_distmax_252d_base_v150_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_peer_sector_pctile
def f051gmp_f051_gross_margin_power_gm_peer_sector_pctile_distmax_504d_base_v151_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_distmax_252d_base_v152_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_peer_industry_pctile
def f051gmp_f051_gross_margin_power_gm_peer_industry_pctile_distmax_504d_base_v153_signal(gm_industry_pctile, closeadj):
    base = gm_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gm
def f051gmp_f051_gross_margin_power_gm_distmed_126d_base_v154_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gm
def f051gmp_f051_gross_margin_power_gm_distmed_252d_base_v155_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gm
def f051gmp_f051_gross_margin_power_gm_distmed_504d_base_v156_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_distmed_126d_base_v157_signal(gp, closeadj):
    base = gp
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_distmed_252d_base_v158_signal(gp, closeadj):
    base = gp
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gp_lvl
def f051gmp_f051_gross_margin_power_gp_lvl_distmed_504d_base_v159_signal(gp, closeadj):
    base = gp
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_distmed_126d_base_v160_signal(grossmargin, closeadj):
    base = grossmargin
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_distmed_252d_base_v161_signal(grossmargin, closeadj):
    base = grossmargin
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of grossmargin_lvl
def f051gmp_f051_gross_margin_power_grossmargin_lvl_distmed_504d_base_v162_signal(grossmargin, closeadj):
    base = grossmargin
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_distmed_126d_base_v163_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_distmed_252d_base_v164_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gp_growth_y
def f051gmp_f051_gross_margin_power_gp_growth_y_distmed_504d_base_v165_signal(gp, closeadj):
    base = gp.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_distmed_126d_base_v166_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_distmed_252d_base_v167_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gm_yoy_chg
def f051gmp_f051_gross_margin_power_gm_yoy_chg_distmed_504d_base_v168_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_distmed_126d_base_v169_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_distmed_252d_base_v170_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gm_vol_252
def f051gmp_f051_gross_margin_power_gm_vol_252_distmed_504d_base_v171_signal(gp, revenue, closeadj):
    base = _f051_gm(gp, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_distmed_126d_base_v172_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_distmed_252d_base_v173_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gp_to_rnd
def f051gmp_f051_gross_margin_power_gp_to_rnd_distmed_504d_base_v174_signal(gp, rnd, closeadj):
    base = gp / rnd.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gm_peer_sector_dist
def f051gmp_f051_gross_margin_power_gm_peer_sector_dist_distmed_126d_base_v175_signal(gp, revenue, gm_sector_med, closeadj):
    base = (_f051_gm(gp, revenue) - gm_sector_med) / gm_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

