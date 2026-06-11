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


# 21d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slope_21d_2d_v001_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slope_63d_2d_v002_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slope_126d_2d_v003_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slope_252d_2d_v004_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_slope_504d_2d_v005_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slope_21d_2d_v006_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slope_63d_2d_v007_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slope_126d_2d_v008_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slope_252d_2d_v009_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_slope_504d_2d_v010_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slope_21d_2d_v011_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slope_63d_2d_v012_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slope_126d_2d_v013_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slope_252d_2d_v014_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_slope_504d_2d_v015_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slope_21d_2d_v016_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slope_63d_2d_v017_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slope_126d_2d_v018_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slope_252d_2d_v019_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_slope_504d_2d_v020_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slope_21d_2d_v021_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slope_63d_2d_v022_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slope_126d_2d_v023_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slope_252d_2d_v024_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_slope_504d_2d_v025_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slope_21d_2d_v026_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slope_63d_2d_v027_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slope_126d_2d_v028_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slope_252d_2d_v029_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_slope_504d_2d_v030_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slope_21d_2d_v031_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slope_63d_2d_v032_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slope_126d_2d_v033_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slope_252d_2d_v034_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_slope_504d_2d_v035_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slope_21d_2d_v036_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slope_63d_2d_v037_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slope_126d_2d_v038_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slope_252d_2d_v039_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_slope_504d_2d_v040_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sm21_sl21_2d_v041_signal(ncfo, closeadj):
    base = _mean(ncfo, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sm63_sl21_2d_v042_signal(ncfo, closeadj):
    base = _mean(ncfo, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sm63_sl63_2d_v043_signal(ncfo, closeadj):
    base = _mean(ncfo, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sm252_sl63_2d_v044_signal(ncfo, closeadj):
    base = _mean(ncfo, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sm252_sl126_2d_v045_signal(ncfo, closeadj):
    base = _mean(ncfo, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sm21_sl21_2d_v046_signal(ncfo, revenue, closeadj):
    base = _mean(_f008_ocf_to_revenue(ncfo, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sm63_sl21_2d_v047_signal(ncfo, revenue, closeadj):
    base = _mean(_f008_ocf_to_revenue(ncfo, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sm63_sl63_2d_v048_signal(ncfo, revenue, closeadj):
    base = _mean(_f008_ocf_to_revenue(ncfo, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sm252_sl63_2d_v049_signal(ncfo, revenue, closeadj):
    base = _mean(_f008_ocf_to_revenue(ncfo, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sm252_sl126_2d_v050_signal(ncfo, revenue, closeadj):
    base = _mean(_f008_ocf_to_revenue(ncfo, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sm21_sl21_2d_v051_signal(ncfo, assets, closeadj):
    base = _mean(_f008_ocf_to_asset(ncfo, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sm63_sl21_2d_v052_signal(ncfo, assets, closeadj):
    base = _mean(_f008_ocf_to_asset(ncfo, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sm63_sl63_2d_v053_signal(ncfo, assets, closeadj):
    base = _mean(_f008_ocf_to_asset(ncfo, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sm252_sl63_2d_v054_signal(ncfo, assets, closeadj):
    base = _mean(_f008_ocf_to_asset(ncfo, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sm252_sl126_2d_v055_signal(ncfo, assets, closeadj):
    base = _mean(_f008_ocf_to_asset(ncfo, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sm21_sl21_2d_v056_signal(ncfo, marketcap, closeadj):
    base = _mean(_f008_ocf_yield(ncfo, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sm63_sl21_2d_v057_signal(ncfo, marketcap, closeadj):
    base = _mean(_f008_ocf_yield(ncfo, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sm63_sl63_2d_v058_signal(ncfo, marketcap, closeadj):
    base = _mean(_f008_ocf_yield(ncfo, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sm252_sl63_2d_v059_signal(ncfo, marketcap, closeadj):
    base = _mean(_f008_ocf_yield(ncfo, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sm252_sl126_2d_v060_signal(ncfo, marketcap, closeadj):
    base = _mean(_f008_ocf_yield(ncfo, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sm21_sl21_2d_v061_signal(ncfo, sharesbas, closeadj):
    base = _mean(ncfo / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sm63_sl21_2d_v062_signal(ncfo, sharesbas, closeadj):
    base = _mean(ncfo / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sm63_sl63_2d_v063_signal(ncfo, sharesbas, closeadj):
    base = _mean(ncfo / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sm252_sl63_2d_v064_signal(ncfo, sharesbas, closeadj):
    base = _mean(ncfo / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sm252_sl126_2d_v065_signal(ncfo, sharesbas, closeadj):
    base = _mean(ncfo / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sm21_sl21_2d_v066_signal(ncfo, opex, closeadj):
    base = _mean(ncfo / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sm63_sl21_2d_v067_signal(ncfo, opex, closeadj):
    base = _mean(ncfo / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sm63_sl63_2d_v068_signal(ncfo, opex, closeadj):
    base = _mean(ncfo / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sm252_sl63_2d_v069_signal(ncfo, opex, closeadj):
    base = _mean(ncfo / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sm252_sl126_2d_v070_signal(ncfo, opex, closeadj):
    base = _mean(ncfo / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sm21_sl21_2d_v071_signal(ncfo, netinc, closeadj):
    base = _mean(ncfo - netinc.fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sm63_sl21_2d_v072_signal(ncfo, netinc, closeadj):
    base = _mean(ncfo - netinc.fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sm63_sl63_2d_v073_signal(ncfo, netinc, closeadj):
    base = _mean(ncfo - netinc.fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sm252_sl63_2d_v074_signal(ncfo, netinc, closeadj):
    base = _mean(ncfo - netinc.fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sm252_sl126_2d_v075_signal(ncfo, netinc, closeadj):
    base = _mean(ncfo - netinc.fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sm21_sl21_2d_v076_signal(ncfo, ebitda, closeadj):
    base = _mean(ncfo / ebitda.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sm63_sl21_2d_v077_signal(ncfo, ebitda, closeadj):
    base = _mean(ncfo / ebitda.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sm63_sl63_2d_v078_signal(ncfo, ebitda, closeadj):
    base = _mean(ncfo / ebitda.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sm252_sl63_2d_v079_signal(ncfo, ebitda, closeadj):
    base = _mean(ncfo / ebitda.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sm252_sl126_2d_v080_signal(ncfo, ebitda, closeadj):
    base = _mean(ncfo / ebitda.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_pctslope_21d_2d_v081_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_pctslope_63d_2d_v082_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_pctslope_252d_2d_v083_signal(ncfo, closeadj):
    base = ncfo
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_pctslope_21d_2d_v084_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_pctslope_63d_2d_v085_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_pctslope_252d_2d_v086_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_pctslope_21d_2d_v087_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_pctslope_63d_2d_v088_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_pctslope_252d_2d_v089_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_pctslope_21d_2d_v090_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_pctslope_63d_2d_v091_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_pctslope_252d_2d_v092_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_pctslope_21d_2d_v093_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_pctslope_63d_2d_v094_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_pctslope_252d_2d_v095_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_pctslope_21d_2d_v096_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_pctslope_63d_2d_v097_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_pctslope_252d_2d_v098_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_pctslope_21d_2d_v099_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_pctslope_63d_2d_v100_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_pctslope_252d_2d_v101_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_pctslope_21d_2d_v102_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_pctslope_63d_2d_v103_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_pctslope_252d_2d_v104_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sgnslope_21d_2d_v105_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sgnslope_63d_2d_v106_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_sgnslope_252d_2d_v107_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sgnslope_21d_2d_v108_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sgnslope_63d_2d_v109_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_sgnslope_252d_2d_v110_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sgnslope_21d_2d_v111_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sgnslope_63d_2d_v112_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_sgnslope_252d_2d_v113_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sgnslope_21d_2d_v114_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sgnslope_63d_2d_v115_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_sgnslope_252d_2d_v116_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sgnslope_21d_2d_v117_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sgnslope_63d_2d_v118_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_sgnslope_252d_2d_v119_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sgnslope_21d_2d_v120_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sgnslope_63d_2d_v121_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_sgnslope_252d_2d_v122_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sgnslope_21d_2d_v123_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sgnslope_63d_2d_v124_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_sgnslope_252d_2d_v125_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sgnslope_21d_2d_v126_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sgnslope_63d_2d_v127_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_sgnslope_252d_2d_v128_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_logmagslope_21d_2d_v129_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_logmagslope_63d_2d_v130_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_logmagslope_252d_2d_v131_signal(ncfo, closeadj):
    base = ncfo
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_logmagslope_21d_2d_v132_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_logmagslope_63d_2d_v133_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_logmagslope_252d_2d_v134_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_logmagslope_21d_2d_v135_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_logmagslope_63d_2d_v136_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_logmagslope_252d_2d_v137_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_logmagslope_21d_2d_v138_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_logmagslope_63d_2d_v139_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_logmagslope_252d_2d_v140_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_logmagslope_21d_2d_v141_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_logmagslope_63d_2d_v142_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_logmagslope_252d_2d_v143_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_logmagslope_21d_2d_v144_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_logmagslope_63d_2d_v145_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_logmagslope_252d_2d_v146_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_logmagslope_21d_2d_v147_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_logmagslope_63d_2d_v148_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_logmagslope_252d_2d_v149_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_logmagslope_21d_2d_v150_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

