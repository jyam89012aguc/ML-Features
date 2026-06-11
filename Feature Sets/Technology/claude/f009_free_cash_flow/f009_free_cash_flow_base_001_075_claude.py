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


# 21d mean of fcf_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_lvl_mean_21d_base_v001_signal(fcf, closeadj):
    base = fcf
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_lvl_mean_63d_base_v002_signal(fcf, closeadj):
    base = fcf
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_lvl_mean_126d_base_v003_signal(fcf, closeadj):
    base = fcf
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_lvl_mean_252d_base_v004_signal(fcf, closeadj):
    base = fcf
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_lvl_mean_504d_base_v005_signal(fcf, closeadj):
    base = fcf
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_margin scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_margin_mean_21d_base_v006_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_margin scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_margin_mean_63d_base_v007_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_margin scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_margin_mean_126d_base_v008_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_margin scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_margin_mean_252d_base_v009_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_margin scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_margin_mean_504d_base_v010_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_yield scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_yield_mean_21d_base_v011_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_yield scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_yield_mean_63d_base_v012_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_yield scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_yield_mean_126d_base_v013_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_yield scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_yield_mean_252d_base_v014_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_yield scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_yield_mean_504d_base_v015_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfps_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfps_lvl_mean_21d_base_v016_signal(fcfps, closeadj):
    base = fcfps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfps_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfps_lvl_mean_63d_base_v017_signal(fcfps, closeadj):
    base = fcfps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfps_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfps_lvl_mean_126d_base_v018_signal(fcfps, closeadj):
    base = fcfps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfps_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfps_lvl_mean_252d_base_v019_signal(fcfps, closeadj):
    base = fcfps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfps_lvl scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfps_lvl_mean_504d_base_v020_signal(fcfps, closeadj):
    base = fcfps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_to_asset scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_to_asset_mean_21d_base_v021_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_to_asset scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_to_asset_mean_63d_base_v022_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_to_asset scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_to_asset_mean_126d_base_v023_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_to_asset scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_to_asset_mean_252d_base_v024_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_to_asset scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_to_asset_mean_504d_base_v025_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_conv scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_conv_mean_21d_base_v026_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_conv scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_conv_mean_63d_base_v027_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_conv scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_conv_mean_126d_base_v028_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_conv scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_conv_mean_252d_base_v029_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_conv scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_conv_mean_504d_base_v030_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_minus_ocf scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_mean_21d_base_v031_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_minus_ocf scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_mean_63d_base_v032_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_minus_ocf scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_mean_126d_base_v033_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_minus_ocf scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_mean_252d_base_v034_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_minus_ocf scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_mean_504d_base_v035_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_ex_capex scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_ex_capex_mean_21d_base_v036_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_ex_capex scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_ex_capex_mean_63d_base_v037_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_ex_capex scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_ex_capex_mean_126d_base_v038_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_ex_capex scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_ex_capex_mean_252d_base_v039_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_ex_capex scaled by closeadj
def f009fcf_f009_free_cash_flow_fcf_ex_capex_mean_504d_base_v040_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_mean_21d_base_v041_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_mean_63d_base_v042_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_mean_126d_base_v043_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_mean_252d_base_v044_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_mean_504d_base_v045_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_mean_21d_base_v046_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_mean_63d_base_v047_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_mean_126d_base_v048_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_mean_252d_base_v049_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_mean_504d_base_v050_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_mean_21d_base_v051_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_mean_63d_base_v052_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_mean_126d_base_v053_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_mean_252d_base_v054_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_mean_504d_base_v055_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_mean_21d_base_v056_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_mean_63d_base_v057_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_mean_126d_base_v058_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_mean_252d_base_v059_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_mean_504d_base_v060_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_mean_21d_base_v061_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_mean_63d_base_v062_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_mean_126d_base_v063_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_mean_252d_base_v064_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_mean_504d_base_v065_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfm_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_mean_21d_base_v066_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfm_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_mean_63d_base_v067_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfm_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_mean_126d_base_v068_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfm_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_mean_252d_base_v069_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfm_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_mean_504d_base_v070_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfy_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_mean_21d_base_v071_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfy_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_mean_63d_base_v072_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfy_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_mean_126d_base_v073_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfy_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_mean_252d_base_v074_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfy_peer_sector_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_mean_504d_base_v075_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfy_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_mean_21d_base_v076_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfy_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_mean_63d_base_v077_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfy_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_mean_126d_base_v078_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfy_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_mean_252d_base_v079_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfy_peer_sector_z scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_mean_504d_base_v080_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfy_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_mean_21d_base_v081_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfy_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_mean_63d_base_v082_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfy_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_mean_126d_base_v083_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfy_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_mean_252d_base_v084_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfy_peer_industry_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_mean_504d_base_v085_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfy_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_mean_21d_base_v086_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfy_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_mean_63d_base_v087_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfy_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_mean_126d_base_v088_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfy_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_mean_252d_base_v089_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfy_peer_mcap_bucket_dist scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_mean_504d_base_v090_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfy_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_mean_21d_base_v091_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfy_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_mean_63d_base_v092_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfy_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_mean_126d_base_v093_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfy_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_mean_252d_base_v094_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfy_peer_sector_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_mean_504d_base_v095_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcfy_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_mean_21d_base_v096_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcfy_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_mean_63d_base_v097_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcfy_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_mean_126d_base_v098_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcfy_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_mean_252d_base_v099_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcfy_peer_industry_pctile scaled by closeadj
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_mean_504d_base_v100_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

