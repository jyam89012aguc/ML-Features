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


# 63d z-score of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_z_63d_base_v076_signal(ncfo, closeadj):
    base = ncfo
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_z_126d_base_v077_signal(ncfo, closeadj):
    base = ncfo
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_z_252d_base_v078_signal(ncfo, closeadj):
    base = ncfo
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_z_504d_base_v079_signal(ncfo, closeadj):
    base = ncfo
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_z_63d_base_v080_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_z_126d_base_v081_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_z_252d_base_v082_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_z_504d_base_v083_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_z_63d_base_v084_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_z_126d_base_v085_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_z_252d_base_v086_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_z_504d_base_v087_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_z_63d_base_v088_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_z_126d_base_v089_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_z_252d_base_v090_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_z_504d_base_v091_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_z_63d_base_v092_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_z_126d_base_v093_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_z_252d_base_v094_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_z_504d_base_v095_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_z_63d_base_v096_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_z_126d_base_v097_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_z_252d_base_v098_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_z_504d_base_v099_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_z_63d_base_v100_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_z_126d_base_v101_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_z_252d_base_v102_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_z_504d_base_v103_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_z_63d_base_v104_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_z_126d_base_v105_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_z_252d_base_v106_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_z_504d_base_v107_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_distmax_252d_base_v108_signal(ncfo, closeadj):
    base = ncfo
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_distmax_504d_base_v109_signal(ncfo, closeadj):
    base = ncfo
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_distmax_252d_base_v110_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_distmax_504d_base_v111_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_distmax_252d_base_v112_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_distmax_504d_base_v113_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_distmax_252d_base_v114_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_distmax_504d_base_v115_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_distmax_252d_base_v116_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_distmax_504d_base_v117_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_distmax_252d_base_v118_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_distmax_504d_base_v119_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_distmax_252d_base_v120_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_distmax_504d_base_v121_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_distmax_252d_base_v122_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_distmax_504d_base_v123_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_distmed_126d_base_v124_signal(ncfo, closeadj):
    base = ncfo
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_distmed_252d_base_v125_signal(ncfo, closeadj):
    base = ncfo
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_distmed_504d_base_v126_signal(ncfo, closeadj):
    base = ncfo
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_distmed_126d_base_v127_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_distmed_252d_base_v128_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_distmed_504d_base_v129_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_distmed_126d_base_v130_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_distmed_252d_base_v131_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_to_asset
def f008ocf_f008_operating_cash_flow_ocf_to_asset_distmed_504d_base_v132_signal(ncfo, assets, closeadj):
    base = _f008_ocf_to_asset(ncfo, assets)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_distmed_126d_base_v133_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_distmed_252d_base_v134_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_yield
def f008ocf_f008_operating_cash_flow_ocf_yield_distmed_504d_base_v135_signal(ncfo, marketcap, closeadj):
    base = _f008_ocf_yield(ncfo, marketcap)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_distmed_126d_base_v136_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_distmed_252d_base_v137_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_per_share
def f008ocf_f008_operating_cash_flow_ocf_per_share_distmed_504d_base_v138_signal(ncfo, sharesbas, closeadj):
    base = ncfo / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_distmed_126d_base_v139_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_distmed_252d_base_v140_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_to_opex
def f008ocf_f008_operating_cash_flow_ocf_to_opex_distmed_504d_base_v141_signal(ncfo, opex, closeadj):
    base = ncfo / opex.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_distmed_126d_base_v142_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_distmed_252d_base_v143_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_minus_ni
def f008ocf_f008_operating_cash_flow_ocf_minus_ni_distmed_504d_base_v144_signal(ncfo, netinc, closeadj):
    base = ncfo - netinc.fillna(0)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_distmed_126d_base_v145_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_distmed_252d_base_v146_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_to_ebitda
def f008ocf_f008_operating_cash_flow_ocf_to_ebitda_distmed_504d_base_v147_signal(ncfo, ebitda, closeadj):
    base = ncfo / ebitda.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_chg_63d_base_v148_signal(ncfo, closeadj):
    base = ncfo
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ocf_lvl
def f008ocf_f008_operating_cash_flow_ocf_lvl_chg_252d_base_v149_signal(ncfo, closeadj):
    base = ncfo
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ocf_to_rev
def f008ocf_f008_operating_cash_flow_ocf_to_rev_chg_63d_base_v150_signal(ncfo, revenue, closeadj):
    base = _f008_ocf_to_revenue(ncfo, revenue)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

