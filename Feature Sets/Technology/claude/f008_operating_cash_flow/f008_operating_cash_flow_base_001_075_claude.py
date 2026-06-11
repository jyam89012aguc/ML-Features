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
def _f008_ocf_to_revenue(ncfo, revenue):
    return ncfo / revenue.abs().replace(0, np.nan)


def _f008_ocf_to_asset(ncfo, assets):
    return ncfo / assets.replace(0, np.nan).abs()


def _f008_ocf_yield(ncfo, marketcap):
    return ncfo / marketcap.replace(0, np.nan).abs()


# 21d mean of ocf_lvl scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_lvl_mean_21d_base_v001_signal(ncfo, closeadj):
    base = ncfo
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_lvl scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_lvl_mean_63d_base_v002_signal(ncfo, closeadj):
    base = ncfo
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_lvl scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_lvl_mean_126d_base_v003_signal(ncfo, closeadj):
    base = ncfo
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_lvl scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_lvl_mean_252d_base_v004_signal(ncfo, closeadj):
    base = ncfo
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_lvl scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_lvl_mean_504d_base_v005_signal(ncfo, closeadj):
    base = ncfo
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_rev scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_rev_mean_21d_base_v006_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_rev scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_rev_mean_63d_base_v007_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_rev scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_rev_mean_126d_base_v008_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_rev scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_rev_mean_252d_base_v009_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_rev scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_rev_mean_504d_base_v010_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_asset scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_asset_mean_21d_base_v011_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_asset scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_asset_mean_63d_base_v012_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_asset scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_asset_mean_126d_base_v013_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_asset scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_asset_mean_252d_base_v014_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_asset scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_asset_mean_504d_base_v015_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_yield scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_yield_mean_21d_base_v016_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_yield scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_yield_mean_63d_base_v017_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_yield scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_yield_mean_126d_base_v018_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_yield scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_yield_mean_252d_base_v019_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_yield scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_yield_mean_504d_base_v020_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_per_share scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_per_share_mean_21d_base_v021_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_per_share scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_per_share_mean_63d_base_v022_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_per_share scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_per_share_mean_126d_base_v023_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_per_share scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_per_share_mean_252d_base_v024_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_per_share scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_per_share_mean_504d_base_v025_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_opex scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_opex_mean_21d_base_v026_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_opex scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_opex_mean_63d_base_v027_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_opex scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_opex_mean_126d_base_v028_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_opex scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_opex_mean_252d_base_v029_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_opex scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_opex_mean_504d_base_v030_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_minus_ni scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_mean_21d_base_v031_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_minus_ni scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_mean_63d_base_v032_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_minus_ni scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_mean_126d_base_v033_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_minus_ni scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_mean_252d_base_v034_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_minus_ni scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_mean_504d_base_v035_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_to_ebitda scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_mean_21d_base_v036_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_to_ebitda scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_mean_63d_base_v037_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_to_ebitda scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_mean_126d_base_v038_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_to_ebitda scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_mean_252d_base_v039_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_to_ebitda scaled by closeadj
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_mean_504d_base_v040_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_median_63d_base_v041_signal(ncfo, closeadj):
    base = ncfo
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_median_252d_base_v042_signal(ncfo, closeadj):
    base = ncfo
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_median_504d_base_v043_signal(ncfo, closeadj):
    base = ncfo
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_median_63d_base_v044_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_median_252d_base_v045_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_median_504d_base_v046_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_median_63d_base_v047_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_median_252d_base_v048_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_median_504d_base_v049_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_median_63d_base_v050_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_median_252d_base_v051_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_median_504d_base_v052_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_median_63d_base_v053_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_median_252d_base_v054_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_median_504d_base_v055_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_median_63d_base_v056_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_median_252d_base_v057_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_median_504d_base_v058_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_median_63d_base_v059_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_median_252d_base_v060_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_median_504d_base_v061_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_median_63d_base_v062_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_median_252d_base_v063_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_median_504d_base_v064_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_rmax_252d_base_v065_signal(ncfo, closeadj):
    base = ncfo
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_rmax_504d_base_v066_signal(ncfo, closeadj):
    base = ncfo
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_rmax_252d_base_v067_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_rmax_504d_base_v068_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_rmax_252d_base_v069_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_rmax_504d_base_v070_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_rmax_252d_base_v071_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_rmax_504d_base_v072_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_rmax_252d_base_v073_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_rmax_504d_base_v074_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_rmax_252d_base_v075_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

