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
def _f053_ebm(ebitda, revenue):
    return ebitda / revenue.abs().replace(0, np.nan)


# 63d z-score of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_z_63d_base_v076_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_z_126d_base_v077_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_z_252d_base_v078_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_z_504d_base_v079_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_z_63d_base_v080_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_z_126d_base_v081_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_z_252d_base_v082_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_z_504d_base_v083_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_z_63d_base_v084_signal(ebitda, closeadj):
    base = ebitda
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_z_126d_base_v085_signal(ebitda, closeadj):
    base = ebitda
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_z_252d_base_v086_signal(ebitda, closeadj):
    base = ebitda
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_z_504d_base_v087_signal(ebitda, closeadj):
    base = ebitda
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_z_63d_base_v088_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_z_126d_base_v089_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_z_252d_base_v090_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_z_504d_base_v091_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_z_63d_base_v092_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_z_126d_base_v093_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_z_252d_base_v094_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_z_504d_base_v095_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_z_63d_base_v096_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_z_126d_base_v097_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_z_252d_base_v098_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_z_504d_base_v099_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_z_63d_base_v100_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_z_126d_base_v101_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_z_252d_base_v102_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_z_504d_base_v103_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_z_63d_base_v104_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_z_126d_base_v105_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_z_252d_base_v106_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_z_504d_base_v107_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_z_63d_base_v108_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_z_126d_base_v109_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_z_252d_base_v110_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_z_504d_base_v111_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_z_63d_base_v112_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_z_126d_base_v113_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_z_252d_base_v114_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_z_504d_base_v115_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_z_63d_base_v116_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_z_126d_base_v117_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_z_252d_base_v118_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_z_504d_base_v119_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_z_63d_base_v120_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_z_126d_base_v121_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_z_252d_base_v122_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_z_504d_base_v123_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_z_63d_base_v124_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_z_126d_base_v125_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_z_252d_base_v126_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_z_504d_base_v127_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_distmax_252d_base_v128_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_distmax_504d_base_v129_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_distmax_252d_base_v130_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_distmax_504d_base_v131_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_distmax_252d_base_v132_signal(ebitda, closeadj):
    base = ebitda
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_distmax_504d_base_v133_signal(ebitda, closeadj):
    base = ebitda
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_distmax_252d_base_v134_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_distmax_504d_base_v135_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_distmax_252d_base_v136_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_distmax_504d_base_v137_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_distmax_252d_base_v138_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_distmax_504d_base_v139_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_distmax_252d_base_v140_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_distmax_504d_base_v141_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_distmax_252d_base_v142_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_distmax_504d_base_v143_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_distmax_252d_base_v144_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebm_peer_sector_z
def f053ebm_f053_ebitda_margin_ebm_peer_sector_z_distmax_504d_base_v145_signal(ebitda, revenue, ebm_sector_med, ebm_sector_std, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_distmax_252d_base_v146_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebm_peer_industry_dist
def f053ebm_f053_ebitda_margin_ebm_peer_industry_dist_distmax_504d_base_v147_signal(ebitda, revenue, ebm_industry_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_industry_med) / ebm_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebm_peer_mcap_bucket_dist
def f053ebm_f053_ebitda_margin_ebm_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(ebitda, revenue, ebm_mcap_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_mcap_med) / ebm_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_distmax_252d_base_v150_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebm_peer_sector_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_sector_pctile_distmax_504d_base_v151_signal(ebm_sector_pctile, closeadj):
    base = ebm_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_distmax_252d_base_v152_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ebm_peer_industry_pctile
def f053ebm_f053_ebitda_margin_ebm_peer_industry_pctile_distmax_504d_base_v153_signal(ebm_industry_pctile, closeadj):
    base = ebm_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_distmed_126d_base_v154_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_distmed_252d_base_v155_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitda_margin_calc
def f053ebm_f053_ebitda_margin_ebitda_margin_calc_distmed_504d_base_v156_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_distmed_126d_base_v157_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_distmed_252d_base_v158_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitdamargin
def f053ebm_f053_ebitda_margin_ebitdamargin_distmed_504d_base_v159_signal(ebitdamargin, closeadj):
    base = ebitdamargin
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_distmed_126d_base_v160_signal(ebitda, closeadj):
    base = ebitda
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_distmed_252d_base_v161_signal(ebitda, closeadj):
    base = ebitda
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitda_lvl
def f053ebm_f053_ebitda_margin_ebitda_lvl_distmed_504d_base_v162_signal(ebitda, closeadj):
    base = ebitda
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_distmed_126d_base_v163_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_distmed_252d_base_v164_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitda_growth
def f053ebm_f053_ebitda_margin_ebitda_growth_distmed_504d_base_v165_signal(ebitda, closeadj):
    base = ebitda.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_distmed_126d_base_v166_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_distmed_252d_base_v167_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitda_to_fcf
def f053ebm_f053_ebitda_margin_ebitda_to_fcf_distmed_504d_base_v168_signal(ebitda, fcf, closeadj):
    base = ebitda / fcf.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_distmed_126d_base_v169_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_distmed_252d_base_v170_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitda_to_asset
def f053ebm_f053_ebitda_margin_ebitda_to_asset_distmed_504d_base_v171_signal(ebitda, assets, closeadj):
    base = ebitda / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_distmed_126d_base_v172_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_distmed_252d_base_v173_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ebitda_yoy_chg
def f053ebm_f053_ebitda_margin_ebitda_yoy_chg_distmed_504d_base_v174_signal(ebitda, revenue, closeadj):
    base = _f053_ebm(ebitda, revenue).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ebm_peer_sector_dist
def f053ebm_f053_ebitda_margin_ebm_peer_sector_dist_distmed_126d_base_v175_signal(ebitda, revenue, ebm_sector_med, closeadj):
    base = (_f053_ebm(ebitda, revenue) - ebm_sector_med) / ebm_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

