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


# 21d acceleration of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_accel_21d_3d_v001_signal(fcf, closeadj):
    base = fcf
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_accel_63d_3d_v002_signal(fcf, closeadj):
    base = fcf
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_accel_126d_3d_v003_signal(fcf, closeadj):
    base = fcf
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_accel_252d_3d_v004_signal(fcf, closeadj):
    base = fcf
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_accel_21d_3d_v005_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_accel_63d_3d_v006_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_accel_126d_3d_v007_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_accel_252d_3d_v008_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_accel_21d_3d_v009_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_accel_63d_3d_v010_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_accel_126d_3d_v011_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_accel_252d_3d_v012_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_accel_21d_3d_v013_signal(fcfps, closeadj):
    base = fcfps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_accel_63d_3d_v014_signal(fcfps, closeadj):
    base = fcfps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_accel_126d_3d_v015_signal(fcfps, closeadj):
    base = fcfps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_accel_252d_3d_v016_signal(fcfps, closeadj):
    base = fcfps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_accel_21d_3d_v017_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_accel_63d_3d_v018_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_accel_126d_3d_v019_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_accel_252d_3d_v020_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_accel_21d_3d_v021_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_accel_63d_3d_v022_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_accel_126d_3d_v023_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_accel_252d_3d_v024_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_accel_21d_3d_v025_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_accel_63d_3d_v026_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_accel_126d_3d_v027_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_accel_252d_3d_v028_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_accel_21d_3d_v029_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_accel_63d_3d_v030_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_accel_126d_3d_v031_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_accel_252d_3d_v032_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_accel_21d_3d_v033_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_accel_63d_3d_v034_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_accel_126d_3d_v035_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_accel_252d_3d_v036_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_accel_21d_3d_v037_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_accel_63d_3d_v038_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_accel_126d_3d_v039_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_accel_252d_3d_v040_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_accel_21d_3d_v041_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_accel_63d_3d_v042_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_accel_126d_3d_v043_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_accel_252d_3d_v044_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_accel_21d_3d_v045_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_accel_63d_3d_v046_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_accel_126d_3d_v047_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_accel_252d_3d_v048_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_accel_21d_3d_v049_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_accel_63d_3d_v050_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_accel_126d_3d_v051_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_accel_252d_3d_v052_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_accel_21d_3d_v053_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_accel_63d_3d_v054_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_accel_126d_3d_v055_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_accel_252d_3d_v056_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_accel_21d_3d_v057_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_accel_63d_3d_v058_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_accel_126d_3d_v059_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_accel_252d_3d_v060_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_accel_21d_3d_v061_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_accel_63d_3d_v062_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_accel_126d_3d_v063_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_accel_252d_3d_v064_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_accel_21d_3d_v065_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_accel_63d_3d_v066_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_accel_126d_3d_v067_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_accel_252d_3d_v068_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_accel_21d_3d_v069_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_accel_63d_3d_v070_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_accel_126d_3d_v071_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_accel_252d_3d_v072_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_accel_21d_3d_v073_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_accel_63d_3d_v074_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_accel_126d_3d_v075_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_accel_252d_3d_v076_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_accel_21d_3d_v077_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_accel_63d_3d_v078_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_accel_126d_3d_v079_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_accel_252d_3d_v080_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slopez_21d_z126_3d_v081_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slopez_63d_z252_3d_v082_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slopez_126d_z252_3d_v083_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_slopez_252d_z504_3d_v084_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slopez_21d_z126_3d_v085_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slopez_63d_z252_3d_v086_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slopez_126d_z252_3d_v087_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_slopez_252d_z504_3d_v088_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slopez_21d_z126_3d_v089_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slopez_63d_z252_3d_v090_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slopez_126d_z252_3d_v091_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_slopez_252d_z504_3d_v092_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slopez_21d_z126_3d_v093_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slopez_63d_z252_3d_v094_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slopez_126d_z252_3d_v095_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_slopez_252d_z504_3d_v096_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slopez_21d_z126_3d_v097_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slopez_63d_z252_3d_v098_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slopez_126d_z252_3d_v099_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_slopez_252d_z504_3d_v100_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slopez_21d_z126_3d_v101_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slopez_63d_z252_3d_v102_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slopez_126d_z252_3d_v103_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_slopez_252d_z504_3d_v104_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slopez_21d_z126_3d_v105_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slopez_63d_z252_3d_v106_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slopez_126d_z252_3d_v107_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_slopez_252d_z504_3d_v108_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slopez_21d_z126_3d_v109_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slopez_63d_z252_3d_v110_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slopez_126d_z252_3d_v111_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_slopez_252d_z504_3d_v112_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slopez_21d_z126_3d_v113_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slopez_63d_z252_3d_v114_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slopez_126d_z252_3d_v115_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_slopez_252d_z504_3d_v116_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slopez_21d_z126_3d_v117_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slopez_63d_z252_3d_v118_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slopez_126d_z252_3d_v119_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_slopez_252d_z504_3d_v120_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slopez_21d_z126_3d_v121_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slopez_63d_z252_3d_v122_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slopez_126d_z252_3d_v123_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_slopez_252d_z504_3d_v124_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slopez_21d_z126_3d_v125_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slopez_63d_z252_3d_v126_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slopez_126d_z252_3d_v127_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_slopez_252d_z504_3d_v128_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slopez_21d_z126_3d_v129_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slopez_63d_z252_3d_v130_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slopez_126d_z252_3d_v131_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_slopez_252d_z504_3d_v132_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slopez_21d_z126_3d_v133_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slopez_63d_z252_3d_v134_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slopez_126d_z252_3d_v135_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_slopez_252d_z504_3d_v136_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slopez_21d_z126_3d_v137_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slopez_63d_z252_3d_v138_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slopez_126d_z252_3d_v139_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfy_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_dist_slopez_252d_z504_3d_v140_signal(fcf, marketcap, fcfy_sector_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slopez_21d_z126_3d_v141_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slopez_63d_z252_3d_v142_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slopez_126d_z252_3d_v143_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfy_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_z_slopez_252d_z504_3d_v144_signal(fcf, marketcap, fcfy_sector_med, fcfy_sector_std, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_sector_med) / fcfy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slopez_21d_z126_3d_v145_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slopez_63d_z252_3d_v146_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slopez_126d_z252_3d_v147_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfy_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_dist_slopez_252d_z504_3d_v148_signal(fcf, marketcap, fcfy_industry_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_industry_med) / fcfy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slopez_21d_z126_3d_v149_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slopez_63d_z252_3d_v150_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slopez_126d_z252_3d_v151_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfy_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfy_peer_mcap_bucket_dist_slopez_252d_z504_3d_v152_signal(fcf, marketcap, fcfy_mcap_med, closeadj):
    base = (_f009_fcf_yield(fcf, marketcap) - fcfy_mcap_med) / fcfy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slopez_21d_z126_3d_v153_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slopez_63d_z252_3d_v154_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slopez_126d_z252_3d_v155_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfy_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_sector_pctile_slopez_252d_z504_3d_v156_signal(fcfy_sector_pctile, closeadj):
    base = fcfy_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slopez_21d_z126_3d_v157_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slopez_63d_z252_3d_v158_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slopez_126d_z252_3d_v159_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfy_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfy_peer_industry_pctile_slopez_252d_z504_3d_v160_signal(fcfy_industry_pctile, closeadj):
    base = fcfy_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_jerk_21d_3d_v161_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_jerk_63d_3d_v162_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_lvl
def f009fcf_f009_free_cash_flow_fcf_lvl_jerk_126d_3d_v163_signal(fcf, closeadj):
    base = fcf
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_jerk_21d_3d_v164_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_jerk_63d_3d_v165_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_margin
def f009fcf_f009_free_cash_flow_fcf_margin_jerk_126d_3d_v166_signal(fcf, revenue, closeadj):
    base = _f009_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_jerk_21d_3d_v167_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_jerk_63d_3d_v168_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_yield
def f009fcf_f009_free_cash_flow_fcf_yield_jerk_126d_3d_v169_signal(fcf, marketcap, closeadj):
    base = _f009_fcf_yield(fcf, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_jerk_21d_3d_v170_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_jerk_63d_3d_v171_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfps_lvl
def f009fcf_f009_free_cash_flow_fcfps_lvl_jerk_126d_3d_v172_signal(fcfps, closeadj):
    base = fcfps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_jerk_21d_3d_v173_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_jerk_63d_3d_v174_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_to_asset
def f009fcf_f009_free_cash_flow_fcf_to_asset_jerk_126d_3d_v175_signal(fcf, assets, closeadj):
    base = fcf / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_jerk_21d_3d_v176_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_jerk_63d_3d_v177_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_conv
def f009fcf_f009_free_cash_flow_fcf_conv_jerk_126d_3d_v178_signal(fcf, netinc, closeadj):
    base = _f009_fcf_conv(fcf, netinc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_jerk_21d_3d_v179_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_jerk_63d_3d_v180_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_minus_ocf
def f009fcf_f009_free_cash_flow_fcf_minus_ocf_jerk_126d_3d_v181_signal(fcf, ncfo, closeadj):
    base = fcf - ncfo.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_jerk_21d_3d_v182_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_jerk_63d_3d_v183_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_ex_capex
def f009fcf_f009_free_cash_flow_fcf_ex_capex_jerk_126d_3d_v184_signal(fcf, capex, closeadj):
    base = fcf + capex.abs().fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_jerk_21d_3d_v185_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_jerk_63d_3d_v186_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfm_peer_sector_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_dist_jerk_126d_3d_v187_signal(fcf, revenue, fcfm_sector_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_jerk_21d_3d_v188_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_jerk_63d_3d_v189_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfm_peer_sector_z
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_z_jerk_126d_3d_v190_signal(fcf, revenue, fcfm_sector_med, fcfm_sector_std, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_sector_med) / fcfm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_jerk_21d_3d_v191_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_jerk_63d_3d_v192_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfm_peer_industry_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_dist_jerk_126d_3d_v193_signal(fcf, revenue, fcfm_industry_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_industry_med) / fcfm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_jerk_21d_3d_v194_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_jerk_63d_3d_v195_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfm_peer_mcap_bucket_dist
def f009fcf_f009_free_cash_flow_fcfm_peer_mcap_bucket_dist_jerk_126d_3d_v196_signal(fcf, revenue, fcfm_mcap_med, closeadj):
    base = (_f009_fcf_margin(fcf, revenue) - fcfm_mcap_med) / fcfm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_jerk_21d_3d_v197_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_jerk_63d_3d_v198_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcfm_peer_sector_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_sector_pctile_jerk_126d_3d_v199_signal(fcfm_sector_pctile, closeadj):
    base = fcfm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcfm_peer_industry_pctile
def f009fcf_f009_free_cash_flow_fcfm_peer_industry_pctile_jerk_21d_3d_v200_signal(fcfm_industry_pctile, closeadj):
    base = fcfm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

