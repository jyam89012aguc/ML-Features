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
def _f008_ocf_to_revenue(ncfo, revenue):
    return ncfo / revenue.abs().replace(0, np.nan)


def _f008_ocf_to_asset(ncfo, assets):
    return ncfo / assets.replace(0, np.nan).abs()


def _f008_ocf_yield(ncfo, marketcap):
    return ncfo / marketcap.replace(0, np.nan).abs()


# 21d acceleration of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_accel_21d_3d_v001_signal(ncfo, closeadj):
    base = ncfo
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_accel_63d_3d_v002_signal(ncfo, closeadj):
    base = ncfo
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_accel_126d_3d_v003_signal(ncfo, closeadj):
    base = ncfo
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_accel_252d_3d_v004_signal(ncfo, closeadj):
    base = ncfo
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_accel_21d_3d_v005_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_accel_63d_3d_v006_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_accel_126d_3d_v007_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_accel_252d_3d_v008_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_accel_21d_3d_v009_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_accel_63d_3d_v010_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_accel_126d_3d_v011_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_accel_252d_3d_v012_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_accel_21d_3d_v013_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_accel_63d_3d_v014_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_accel_126d_3d_v015_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_accel_252d_3d_v016_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_accel_21d_3d_v017_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_accel_63d_3d_v018_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_accel_126d_3d_v019_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_accel_252d_3d_v020_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_accel_21d_3d_v021_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_accel_63d_3d_v022_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_accel_126d_3d_v023_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_accel_252d_3d_v024_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_accel_21d_3d_v025_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_accel_63d_3d_v026_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_accel_126d_3d_v027_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_accel_252d_3d_v028_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_accel_21d_3d_v029_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_accel_63d_3d_v030_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_accel_126d_3d_v031_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_accel_252d_3d_v032_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slopez_21d_z126_3d_v033_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slopez_63d_z252_3d_v034_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slopez_126d_z252_3d_v035_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slopez_252d_z504_3d_v036_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slopez_21d_z126_3d_v037_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slopez_63d_z252_3d_v038_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slopez_126d_z252_3d_v039_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slopez_252d_z504_3d_v040_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slopez_21d_z126_3d_v041_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slopez_63d_z252_3d_v042_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slopez_126d_z252_3d_v043_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slopez_252d_z504_3d_v044_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slopez_21d_z126_3d_v045_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slopez_63d_z252_3d_v046_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slopez_126d_z252_3d_v047_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slopez_252d_z504_3d_v048_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slopez_21d_z126_3d_v049_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slopez_63d_z252_3d_v050_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slopez_126d_z252_3d_v051_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slopez_252d_z504_3d_v052_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slopez_21d_z126_3d_v053_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slopez_63d_z252_3d_v054_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slopez_126d_z252_3d_v055_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slopez_252d_z504_3d_v056_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slopez_21d_z126_3d_v057_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slopez_63d_z252_3d_v058_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slopez_126d_z252_3d_v059_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slopez_252d_z504_3d_v060_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slopez_21d_z126_3d_v061_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slopez_63d_z252_3d_v062_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slopez_126d_z252_3d_v063_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slopez_252d_z504_3d_v064_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_jerk_21d_3d_v065_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_jerk_63d_3d_v066_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_jerk_126d_3d_v067_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_jerk_21d_3d_v068_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_jerk_63d_3d_v069_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_jerk_126d_3d_v070_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_jerk_21d_3d_v071_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_jerk_63d_3d_v072_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_jerk_126d_3d_v073_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_jerk_21d_3d_v074_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_jerk_63d_3d_v075_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_jerk_126d_3d_v076_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_jerk_21d_3d_v077_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_jerk_63d_3d_v078_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_jerk_126d_3d_v079_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_jerk_21d_3d_v080_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_jerk_63d_3d_v081_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_jerk_126d_3d_v082_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_jerk_21d_3d_v083_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_jerk_63d_3d_v084_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_jerk_126d_3d_v085_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_jerk_21d_3d_v086_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_jerk_63d_3d_v087_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_jerk_126d_3d_v088_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_lvl smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_lvl_smoothaccel_63d_sm252_3d_v089_signal(ncfo, closeadj):
    base = ncfo
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_lvl smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_lvl_smoothaccel_252d_sm504_3d_v090_signal(ncfo, closeadj):
    base = ncfo
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_rev smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_to_rev_smoothaccel_63d_sm252_3d_v091_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_rev smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_to_rev_smoothaccel_252d_sm504_3d_v092_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_asset smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_to_asset_smoothaccel_63d_sm252_3d_v093_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_asset smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_to_asset_smoothaccel_252d_sm504_3d_v094_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_yield smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_yield_smoothaccel_63d_sm252_3d_v095_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_yield smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_yield_smoothaccel_252d_sm504_3d_v096_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_per_share smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_per_share_smoothaccel_63d_sm252_3d_v097_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_per_share smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_per_share_smoothaccel_252d_sm504_3d_v098_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_opex smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_to_opex_smoothaccel_63d_sm252_3d_v099_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_opex smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_to_opex_smoothaccel_252d_sm504_3d_v100_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_minus_ni smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_smoothaccel_63d_sm252_3d_v101_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_minus_ni smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_smoothaccel_252d_sm504_3d_v102_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_ebitda smoothed over 252d
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_smoothaccel_63d_sm252_3d_v103_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_ebitda smoothed over 504d
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_smoothaccel_252d_sm504_3d_v104_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_accelz_21d_z252_3d_v105_signal(ncfo, closeadj):
    base = ncfo
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_accelz_63d_z504_3d_v106_signal(ncfo, closeadj):
    base = ncfo
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_accelz_21d_z252_3d_v107_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_accelz_63d_z504_3d_v108_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_accelz_21d_z252_3d_v109_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_accelz_63d_z504_3d_v110_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_accelz_21d_z252_3d_v111_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_accelz_63d_z504_3d_v112_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_accelz_21d_z252_3d_v113_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_accelz_63d_z504_3d_v114_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_accelz_21d_z252_3d_v115_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_accelz_63d_z504_3d_v116_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_accelz_21d_z252_3d_v117_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_accelz_63d_z504_3d_v118_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_accelz_21d_z252_3d_v119_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_accelz_63d_z504_3d_v120_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_lvl (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_lvl_signflip_63d_3d_v121_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_lvl (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_lvl_signflip_252d_3d_v122_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_rev (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_rev_signflip_63d_3d_v123_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_rev (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_rev_signflip_252d_3d_v124_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_asset (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_asset_signflip_63d_3d_v125_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_asset (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_asset_signflip_252d_3d_v126_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_yield (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_yield_signflip_63d_3d_v127_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_yield (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_yield_signflip_252d_3d_v128_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_per_share (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_per_share_signflip_63d_3d_v129_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_per_share (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_per_share_signflip_252d_3d_v130_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_opex (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_opex_signflip_63d_3d_v131_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_opex (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_opex_signflip_252d_3d_v132_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_minus_ni (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_signflip_63d_3d_v133_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_minus_ni (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_signflip_252d_3d_v134_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_ebitda (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_signflip_63d_3d_v135_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_ebitda (raw count, no price scaling)
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_signflip_252d_3d_v136_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_lvl normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_lvl_rngaccel_63d_r252_3d_v137_signal(ncfo, closeadj):
    base = ncfo
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_lvl normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_lvl_rngaccel_252d_r504_3d_v138_signal(ncfo, closeadj):
    base = ncfo
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_rev normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_to_rev_rngaccel_63d_r252_3d_v139_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_rev normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_to_rev_rngaccel_252d_r504_3d_v140_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_asset normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_to_asset_rngaccel_63d_r252_3d_v141_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_asset normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_to_asset_rngaccel_252d_r504_3d_v142_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_yield normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_yield_rngaccel_63d_r252_3d_v143_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_yield normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_yield_rngaccel_252d_r504_3d_v144_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_per_share normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_per_share_rngaccel_63d_r252_3d_v145_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_per_share normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_per_share_rngaccel_252d_r504_3d_v146_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_opex normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_to_opex_rngaccel_63d_r252_3d_v147_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_opex normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_to_opex_rngaccel_252d_r504_3d_v148_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_minus_ni normalized by 252d range
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_rngaccel_63d_r252_3d_v149_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_minus_ni normalized by 504d range
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_rngaccel_252d_r504_3d_v150_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

