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
def _f009_fcf_margin(fcf, revenue):
    return fcf / revenue.abs().replace(0, np.nan)


def _f009_fcf_yield(fcf, marketcap):
    return fcf / marketcap.replace(0, np.nan).abs()


def _f009_fcf_conv(fcf, netinc):
    return fcf / netinc.replace(0, np.nan).abs()


# 63d z-score of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_z_63d_base_v076_signal(fcf, closeadj):
    base = fcf
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_z_126d_base_v077_signal(fcf, closeadj):
    base = fcf
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_z_252d_base_v078_signal(fcf, closeadj):
    base = fcf
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_z_504d_base_v079_signal(fcf, closeadj):
    base = fcf
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_z_63d_base_v080_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_z_126d_base_v081_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_z_252d_base_v082_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_z_504d_base_v083_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_z_63d_base_v084_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_z_126d_base_v085_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_z_252d_base_v086_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_z_504d_base_v087_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_z_63d_base_v088_signal(fcfps, closeadj):
    base = fcfps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_z_126d_base_v089_signal(fcfps, closeadj):
    base = fcfps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_z_252d_base_v090_signal(fcfps, closeadj):
    base = fcfps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_z_504d_base_v091_signal(fcfps, closeadj):
    base = fcfps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_z_63d_base_v092_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_z_126d_base_v093_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_z_252d_base_v094_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_z_504d_base_v095_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_z_63d_base_v096_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_z_126d_base_v097_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_z_252d_base_v098_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_z_504d_base_v099_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_z_63d_base_v100_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_z_126d_base_v101_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_z_252d_base_v102_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_z_504d_base_v103_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_z_63d_base_v104_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_z_126d_base_v105_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_z_252d_base_v106_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_z_504d_base_v107_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_z_63d_base_v108_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_z_126d_base_v109_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_z_252d_base_v110_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_z_504d_base_v111_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_z_63d_base_v112_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_z_126d_base_v113_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_z_252d_base_v114_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_z_504d_base_v115_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_z_63d_base_v116_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_z_126d_base_v117_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_z_252d_base_v118_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_z_504d_base_v119_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_z_63d_base_v120_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_z_126d_base_v121_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_z_252d_base_v122_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_z_504d_base_v123_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_z_63d_base_v124_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_z_126d_base_v125_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_z_252d_base_v126_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_z_504d_base_v127_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_z_63d_base_v128_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_z_126d_base_v129_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_z_252d_base_v130_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_z_504d_base_v131_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_z_63d_base_v132_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_z_126d_base_v133_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_z_252d_base_v134_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_z_504d_base_v135_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_z_63d_base_v136_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_z_126d_base_v137_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_z_252d_base_v138_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_z_504d_base_v139_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_z_63d_base_v140_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_z_126d_base_v141_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_z_252d_base_v142_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_z_504d_base_v143_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_z_63d_base_v144_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_z_126d_base_v145_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_z_252d_base_v146_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_z_504d_base_v147_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_z_63d_base_v148_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_z_126d_base_v149_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_z_252d_base_v150_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_z_504d_base_v151_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_z_63d_base_v152_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_z_126d_base_v153_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_z_252d_base_v154_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_z_504d_base_v155_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_distmax_252d_base_v156_signal(fcf, closeadj):
    base = fcf
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_distmax_504d_base_v157_signal(fcf, closeadj):
    base = fcf
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_distmax_252d_base_v158_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_distmax_504d_base_v159_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_distmax_252d_base_v160_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_distmax_504d_base_v161_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_distmax_252d_base_v162_signal(fcfps, closeadj):
    base = fcfps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_distmax_504d_base_v163_signal(fcfps, closeadj):
    base = fcfps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_distmax_252d_base_v164_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_distmax_504d_base_v165_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_distmax_252d_base_v166_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_distmax_504d_base_v167_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_distmax_252d_base_v168_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_distmax_504d_base_v169_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_distmax_252d_base_v170_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_distmax_504d_base_v171_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_distmax_252d_base_v172_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_distmax_504d_base_v173_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_distmax_252d_base_v174_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_distmax_504d_base_v175_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

