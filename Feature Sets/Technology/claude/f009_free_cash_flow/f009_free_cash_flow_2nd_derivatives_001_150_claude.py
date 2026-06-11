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
def _f009_fcf_margin(fcf, revenue):
    return fcf / revenue.abs().replace(0, np.nan)


def _f009_fcf_yield(fcf, marketcap):
    return fcf / marketcap.replace(0, np.nan).abs()


def _f009_fcf_conv(fcf, netinc):
    return fcf / netinc.replace(0, np.nan).abs()


# 21d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slope_21d_2d_v001_signal(fcf, closeadj):
    base = fcf
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slope_63d_2d_v002_signal(fcf, closeadj):
    base = fcf
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slope_126d_2d_v003_signal(fcf, closeadj):
    base = fcf
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slope_252d_2d_v004_signal(fcf, closeadj):
    base = fcf
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slope_504d_2d_v005_signal(fcf, closeadj):
    base = fcf
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slope_21d_2d_v006_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slope_63d_2d_v007_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slope_126d_2d_v008_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slope_252d_2d_v009_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slope_504d_2d_v010_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slope_21d_2d_v011_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slope_63d_2d_v012_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slope_126d_2d_v013_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slope_252d_2d_v014_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slope_504d_2d_v015_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slope_21d_2d_v016_signal(fcfps, closeadj):
    base = fcfps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slope_63d_2d_v017_signal(fcfps, closeadj):
    base = fcfps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slope_126d_2d_v018_signal(fcfps, closeadj):
    base = fcfps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slope_252d_2d_v019_signal(fcfps, closeadj):
    base = fcfps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slope_504d_2d_v020_signal(fcfps, closeadj):
    base = fcfps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slope_21d_2d_v021_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slope_63d_2d_v022_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slope_126d_2d_v023_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slope_252d_2d_v024_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slope_504d_2d_v025_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slope_21d_2d_v026_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slope_63d_2d_v027_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slope_126d_2d_v028_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slope_252d_2d_v029_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slope_504d_2d_v030_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slope_21d_2d_v031_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slope_63d_2d_v032_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slope_126d_2d_v033_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slope_252d_2d_v034_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slope_504d_2d_v035_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slope_21d_2d_v036_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slope_63d_2d_v037_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slope_126d_2d_v038_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slope_252d_2d_v039_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slope_504d_2d_v040_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slope_21d_2d_v041_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slope_63d_2d_v042_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slope_126d_2d_v043_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slope_252d_2d_v044_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slope_504d_2d_v045_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slope_21d_2d_v046_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slope_63d_2d_v047_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slope_126d_2d_v048_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slope_252d_2d_v049_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slope_504d_2d_v050_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slope_21d_2d_v051_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slope_63d_2d_v052_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slope_126d_2d_v053_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slope_252d_2d_v054_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slope_504d_2d_v055_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slope_21d_2d_v056_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slope_63d_2d_v057_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slope_126d_2d_v058_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slope_252d_2d_v059_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slope_504d_2d_v060_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slope_21d_2d_v061_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slope_63d_2d_v062_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slope_126d_2d_v063_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slope_252d_2d_v064_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slope_504d_2d_v065_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slope_21d_2d_v066_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slope_63d_2d_v067_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slope_126d_2d_v068_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slope_252d_2d_v069_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slope_504d_2d_v070_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slope_21d_2d_v071_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slope_63d_2d_v072_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slope_126d_2d_v073_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slope_252d_2d_v074_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slope_504d_2d_v075_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slope_21d_2d_v076_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slope_63d_2d_v077_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slope_126d_2d_v078_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slope_252d_2d_v079_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slope_504d_2d_v080_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slope_21d_2d_v081_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slope_63d_2d_v082_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slope_126d_2d_v083_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slope_252d_2d_v084_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slope_504d_2d_v085_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slope_21d_2d_v086_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slope_63d_2d_v087_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slope_126d_2d_v088_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slope_252d_2d_v089_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slope_504d_2d_v090_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slope_21d_2d_v091_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slope_63d_2d_v092_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slope_126d_2d_v093_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slope_252d_2d_v094_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slope_504d_2d_v095_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slope_21d_2d_v096_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slope_63d_2d_v097_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slope_126d_2d_v098_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slope_252d_2d_v099_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slope_504d_2d_v100_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_sm21_sl21_2d_v101_signal(fcf, closeadj):
    base = _mean(fcf, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_sm63_sl21_2d_v102_signal(fcf, closeadj):
    base = _mean(fcf, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_sm63_sl63_2d_v103_signal(fcf, closeadj):
    base = _mean(fcf, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_sm252_sl63_2d_v104_signal(fcf, closeadj):
    base = _mean(fcf, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_sm252_sl126_2d_v105_signal(fcf, closeadj):
    base = _mean(fcf, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_sm21_sl21_2d_v106_signal(fcf, revenue, closeadj):
    base = _mean(_f009_fcf_margin(fcf, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_sm63_sl21_2d_v107_signal(fcf, revenue, closeadj):
    base = _mean(_f009_fcf_margin(fcf, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_sm63_sl63_2d_v108_signal(fcf, revenue, closeadj):
    base = _mean(_f009_fcf_margin(fcf, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_sm252_sl63_2d_v109_signal(fcf, revenue, closeadj):
    base = _mean(_f009_fcf_margin(fcf, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_sm252_sl126_2d_v110_signal(fcf, revenue, closeadj):
    base = _mean(_f009_fcf_margin(fcf, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_sm21_sl21_2d_v111_signal(fcf, marketcap, closeadj):
    base = _mean(_f009_fcf_yield(fcf, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_sm63_sl21_2d_v112_signal(fcf, marketcap, closeadj):
    base = _mean(_f009_fcf_yield(fcf, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_sm63_sl63_2d_v113_signal(fcf, marketcap, closeadj):
    base = _mean(_f009_fcf_yield(fcf, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_sm252_sl63_2d_v114_signal(fcf, marketcap, closeadj):
    base = _mean(_f009_fcf_yield(fcf, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_sm252_sl126_2d_v115_signal(fcf, marketcap, closeadj):
    base = _mean(_f009_fcf_yield(fcf, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_sm21_sl21_2d_v116_signal(fcfps, closeadj):
    base = _mean(fcfps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_sm63_sl21_2d_v117_signal(fcfps, closeadj):
    base = _mean(fcfps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_sm63_sl63_2d_v118_signal(fcfps, closeadj):
    base = _mean(fcfps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_sm252_sl63_2d_v119_signal(fcfps, closeadj):
    base = _mean(fcfps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_sm252_sl126_2d_v120_signal(fcfps, closeadj):
    base = _mean(fcfps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_sm21_sl21_2d_v121_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_sm63_sl21_2d_v122_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_sm63_sl63_2d_v123_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_sm252_sl63_2d_v124_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_sm252_sl126_2d_v125_signal(fcf, assets, closeadj):
    base = _mean(fcf / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_sm21_sl21_2d_v126_signal(fcf, netinc, closeadj):
    base = _mean(_f009_fcf_conv(fcf, netinc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_sm63_sl21_2d_v127_signal(fcf, netinc, closeadj):
    base = _mean(_f009_fcf_conv(fcf, netinc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_sm63_sl63_2d_v128_signal(fcf, netinc, closeadj):
    base = _mean(_f009_fcf_conv(fcf, netinc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_sm252_sl63_2d_v129_signal(fcf, netinc, closeadj):
    base = _mean(_f009_fcf_conv(fcf, netinc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_sm252_sl126_2d_v130_signal(fcf, netinc, closeadj):
    base = _mean(_f009_fcf_conv(fcf, netinc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_sm21_sl21_2d_v131_signal(fcf, ncfo, closeadj):
    base = _mean(fcf - ncfo.fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_sm63_sl21_2d_v132_signal(fcf, ncfo, closeadj):
    base = _mean(fcf - ncfo.fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_sm63_sl63_2d_v133_signal(fcf, ncfo, closeadj):
    base = _mean(fcf - ncfo.fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_sm252_sl63_2d_v134_signal(fcf, ncfo, closeadj):
    base = _mean(fcf - ncfo.fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_sm252_sl126_2d_v135_signal(fcf, ncfo, closeadj):
    base = _mean(fcf - ncfo.fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_sm21_sl21_2d_v136_signal(fcf, capex, closeadj):
    base = _mean(fcf + capex.abs().fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_sm63_sl21_2d_v137_signal(fcf, capex, closeadj):
    base = _mean(fcf + capex.abs().fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_sm63_sl63_2d_v138_signal(fcf, capex, closeadj):
    base = _mean(fcf + capex.abs().fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_sm252_sl63_2d_v139_signal(fcf, capex, closeadj):
    base = _mean(fcf + capex.abs().fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_sm252_sl126_2d_v140_signal(fcf, capex, closeadj):
    base = _mean(fcf + capex.abs().fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_sm21_sl21_2d_v141_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_sm63_sl21_2d_v142_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_sm63_sl63_2d_v143_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_sm252_sl63_2d_v144_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_sm252_sl126_2d_v145_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_sm21_sl21_2d_v146_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_sm63_sl21_2d_v147_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_sm63_sl63_2d_v148_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_sm252_sl63_2d_v149_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_sm252_sl126_2d_v150_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_sm21_sl21_2d_v151_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_sm63_sl21_2d_v152_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_sm63_sl63_2d_v153_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_sm252_sl63_2d_v154_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_sm252_sl126_2d_v155_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_sm21_sl21_2d_v156_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_sm63_sl21_2d_v157_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_sm63_sl63_2d_v158_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_sm252_sl63_2d_v159_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_sm252_sl126_2d_v160_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = _mean((_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_sm21_sl21_2d_v161_signal(fcfm_sector_pctile, closeadj):
    base = _mean(fcfm_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_sm63_sl21_2d_v162_signal(fcfm_sector_pctile, closeadj):
    base = _mean(fcfm_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_sm63_sl63_2d_v163_signal(fcfm_sector_pctile, closeadj):
    base = _mean(fcfm_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_sm252_sl63_2d_v164_signal(fcfm_sector_pctile, closeadj):
    base = _mean(fcfm_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_sm252_sl126_2d_v165_signal(fcfm_sector_pctile, closeadj):
    base = _mean(fcfm_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_sm21_sl21_2d_v166_signal(fcfm_industry_pctile, closeadj):
    base = _mean(fcfm_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_sm63_sl21_2d_v167_signal(fcfm_industry_pctile, closeadj):
    base = _mean(fcfm_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_sm63_sl63_2d_v168_signal(fcfm_industry_pctile, closeadj):
    base = _mean(fcfm_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_sm252_sl63_2d_v169_signal(fcfm_industry_pctile, closeadj):
    base = _mean(fcfm_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_sm252_sl126_2d_v170_signal(fcfm_industry_pctile, closeadj):
    base = _mean(fcfm_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_sm21_sl21_2d_v171_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_sm63_sl21_2d_v172_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_sm63_sl63_2d_v173_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_sm252_sl63_2d_v174_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_sm252_sl126_2d_v175_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_sm21_sl21_2d_v176_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_sm63_sl21_2d_v177_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_sm63_sl63_2d_v178_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_sm252_sl63_2d_v179_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_sm252_sl126_2d_v180_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_sm21_sl21_2d_v181_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_sm63_sl21_2d_v182_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_sm63_sl63_2d_v183_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_sm252_sl63_2d_v184_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_sm252_sl126_2d_v185_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_sm21_sl21_2d_v186_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_sm63_sl21_2d_v187_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_sm63_sl63_2d_v188_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_sm252_sl63_2d_v189_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_sm252_sl126_2d_v190_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = _mean((_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_sm21_sl21_2d_v191_signal(fcfy_sector_pctile, closeadj):
    base = _mean(fcfy_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_sm63_sl21_2d_v192_signal(fcfy_sector_pctile, closeadj):
    base = _mean(fcfy_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_sm63_sl63_2d_v193_signal(fcfy_sector_pctile, closeadj):
    base = _mean(fcfy_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_sm252_sl63_2d_v194_signal(fcfy_sector_pctile, closeadj):
    base = _mean(fcfy_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_sm252_sl126_2d_v195_signal(fcfy_sector_pctile, closeadj):
    base = _mean(fcfy_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_sm21_sl21_2d_v196_signal(fcfy_industry_pctile, closeadj):
    base = _mean(fcfy_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_sm63_sl21_2d_v197_signal(fcfy_industry_pctile, closeadj):
    base = _mean(fcfy_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_sm63_sl63_2d_v198_signal(fcfy_industry_pctile, closeadj):
    base = _mean(fcfy_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_sm252_sl63_2d_v199_signal(fcfy_industry_pctile, closeadj):
    base = _mean(fcfy_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_sm252_sl126_2d_v200_signal(fcfy_industry_pctile, closeadj):
    base = _mean(fcfy_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

