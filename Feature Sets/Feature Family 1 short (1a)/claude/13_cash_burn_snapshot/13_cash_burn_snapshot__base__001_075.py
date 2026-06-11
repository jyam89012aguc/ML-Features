"""cash_burn_snapshot base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about cash burn, runway, and liquidity at the price peak
(continued in __base__076_150.py). Inputs: SF1 quarterly fundamentals.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no
forward-looking shifts.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _signed_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.sign(s) * np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.sign(s) * np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: FCF / OCF level (001-015) ----

def f13_cbsp_001_signed_log_fcf_ttm(fcf):
    return _signed_log_abs(_ttm(fcf))


def f13_cbsp_002_fcf_to_assets_ttm(fcf, assets):
    return _safe_div(_ttm(fcf), assets)


def f13_cbsp_003_fcf_q_to_assets(fcf, assets):
    return _safe_div(fcf * 4.0, assets)


def f13_cbsp_004_fcf_q_to_revenue(fcf, revenue):
    return _safe_div(fcf, revenue)


def f13_cbsp_005_ocf_to_assets_ttm(ncfo, assets):
    return _safe_div(_ttm(ncfo), assets)


def f13_cbsp_006_ocf_to_equity_ttm(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity)


def f13_cbsp_007_signed_log_ncfo_ttm(ncfo):
    return _signed_log_abs(_ttm(ncfo))


def f13_cbsp_008_capex_to_ocf_ratio(capex, ncfo):
    return _safe_div(_ttm(capex).abs(), _ttm(ncfo).abs())


def f13_cbsp_009_fcf_to_ocf_ratio(fcf, ncfo):
    return _safe_div(_ttm(fcf), _ttm(ncfo).abs())


def f13_cbsp_010_ocf_to_netinc_ratio(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs())


def f13_cbsp_011_burn_intensity_to_assets(fcf, assets):
    return -_safe_div(_ttm(fcf).clip(upper=0).abs(), assets)


def f13_cbsp_012_ncfo_to_equity_proxy(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity.abs())


def f13_cbsp_013_growth_capex_to_assets(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets)


def f13_cbsp_014_discretionary_cash_to_revenue(ncfo, capex, intexp, revenue):
    return _safe_div(_ttm(ncfo) - _ttm(capex).abs() - _ttm(intexp).abs(), _ttm(revenue).abs())


def f13_cbsp_015_fcf_q_share_of_4q(fcf):
    return _safe_div(fcf, _ttm(fcf).abs())


# ---- Block B: cash runway / liquidity (016-040) ----

def f13_cbsp_016_cash_to_equity(cashneq, equity):
    return _safe_div(cashneq, equity.abs())


def f13_cbsp_017_cash_to_assets(cashneq, assets):
    return _safe_div(cashneq, assets)


def f13_cbsp_018_cash_to_currentassets(cashneq, assetsc):
    return _safe_div(cashneq, assetsc)


def f13_cbsp_019_cash_to_currentliabilities(cashneq, liabilitiesc):
    return _safe_div(cashneq, liabilitiesc)


def f13_cbsp_020_cash_to_debt(cashneq, debt):
    return _safe_div(cashneq, debt)


def f13_cbsp_021_cash_to_debt_current(cashneq, debtc):
    return _safe_div(cashneq, debtc)


def f13_cbsp_022_quick_ratio(cashneq, receivables, liabilitiesc):
    return _safe_div(cashneq + receivables, liabilitiesc)


def f13_cbsp_023_current_ratio(assetsc, liabilitiesc):
    return _safe_div(assetsc, liabilitiesc)


def f13_cbsp_024_workingcapital_to_revenue_ttm(workingcapital, revenue):
    return _safe_div(workingcapital, _ttm(revenue))


def f13_cbsp_025_workingcapital_to_assets(workingcapital, assets):
    return _safe_div(workingcapital, assets)


def f13_cbsp_026_cash_runway_q_from_fcf(cashneq, fcf):
    burn = (-_ttm(fcf) / 4.0).clip(lower=1e-6)
    return _safe_div(cashneq, burn).clip(upper=40.0)


def f13_cbsp_027_cash_runway_q_from_ocf(cashneq, ncfo):
    burn = (-_ttm(ncfo) / 4.0).clip(lower=1e-6)
    return _safe_div(cashneq, burn).clip(upper=40.0)


def f13_cbsp_028_net_cash_to_equity(cashneq, debt, equity):
    return _safe_div(cashneq - debt, equity.abs())


def f13_cbsp_029_liquid_assets_to_q_burn(cashneq, receivables, fcf):
    burn = (-_ttm(fcf) / 4.0).clip(lower=1e-6)
    return _safe_div(cashneq + receivables, burn).clip(upper=40.0)


def f13_cbsp_030_net_cash_log_abs(cashneq, debt):
    return _signed_log_abs(cashneq - debt)


def f13_cbsp_031_net_cash_to_assets(cashneq, debt, assets):
    return _safe_div(cashneq - debt, assets)


def f13_cbsp_032_cash_zscore_8q(cashneq):
    return _rolling_zscore(cashneq, 8, 3)


def f13_cbsp_033_cash_qoq_pct(cashneq):
    return _qoq_pct(cashneq)


def f13_cbsp_034_cash_yoy_pct(cashneq):
    return _yoy_pct(cashneq)


def f13_cbsp_035_cash_to_revenue_ttm(cashneq, revenue):
    return _safe_div(cashneq, _ttm(revenue))


def f13_cbsp_036_cash_minus_currentliabilities_to_assets(cashneq, liabilitiesc, assets):
    return _safe_div(cashneq - liabilitiesc, assets)


def f13_cbsp_037_cash_to_4q_burn_rate(cashneq, fcf):
    burn4 = _ttm(fcf).clip(upper=-1e-6).abs()
    return _safe_div(cashneq, burn4).clip(upper=40.0)


def f13_cbsp_038_cash_to_8q_burn_rate(cashneq, fcf):
    burn8 = fcf.rolling(8, min_periods=4).sum().clip(upper=-1e-6).abs()
    return _safe_div(cashneq, burn8).clip(upper=40.0)


def f13_cbsp_039_cash_share_of_currentassets(cashneq, assetsc):
    return _safe_div(cashneq, assetsc)


def f13_cbsp_040_liquidity_composite(cashneq, receivables, liabilitiesc):
    return _safe_div(cashneq + receivables, liabilitiesc)


# ---- Block C: capex / investment burden (041-060) ----

def f13_cbsp_041_capex_to_revenue_ttm(capex, revenue):
    return _safe_div(_ttm(capex).abs(), _ttm(revenue))


def f13_cbsp_042_capex_to_assets(capex, assets):
    return _safe_div(_ttm(capex).abs(), assets)


def f13_cbsp_043_capex_to_ppe(capex, ppnenet):
    return _safe_div(_ttm(capex).abs(), ppnenet)


def f13_cbsp_044_capex_to_depamor(capex, depamor):
    return _safe_div(_ttm(capex).abs(), _ttm(depamor))


def f13_cbsp_045_capex_yoy_pct(capex):
    return _yoy_pct(_ttm(capex).abs())


def f13_cbsp_046_capex_qoq_pct(capex):
    return _qoq_pct(capex.abs())


def f13_cbsp_047_capex_to_ocf_ttm(capex, ncfo):
    return _safe_div(_ttm(capex).abs(), _ttm(ncfo).abs())


def f13_cbsp_048_capex_intensity_zscore_8q(capex, assets):
    return _rolling_zscore(_safe_div(_ttm(capex).abs(), assets), 8, 3)


def f13_cbsp_049_capex_q_minus_4q_avg_to_4q_avg(capex):
    m = capex.abs().rolling(4, min_periods=2).mean()
    return _safe_div(capex.abs() - m, m)


def f13_cbsp_050_growth_capex_proxy(capex, depamor):
    return _ttm(capex).abs() - _ttm(depamor)


def f13_cbsp_051_growth_capex_to_assets(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets)


def f13_cbsp_052_growth_capex_to_revenue(capex, depamor, revenue):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), _ttm(revenue))


def f13_cbsp_053_ncfi_to_assets(ncfi, assets):
    return _safe_div(_ttm(ncfi), assets)


def f13_cbsp_054_ncfi_to_revenue_ttm(ncfi, revenue):
    return _safe_div(_ttm(ncfi), _ttm(revenue))


def f13_cbsp_055_ncfi_qoq_change(ncfi):
    return ncfi.diff()


def f13_cbsp_056_capex_minus_ocf_to_assets(capex, ncfo, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(ncfo), assets)


def f13_cbsp_057_ncfi_share_of_total_outflows(ncfi, ncfo, ncff):
    total = ncfi.abs() + ncfo.abs() + ncff.abs()
    return _safe_div(ncfi.abs(), total)


def f13_cbsp_058_capex_consistency_8q(capex, assets):
    r = _safe_div(_ttm(capex).abs(), assets)
    return r.rolling(8, min_periods=3).std()


def f13_cbsp_059_capex_to_invcap(capex, equity, debt):
    return _safe_div(_ttm(capex).abs(), equity + debt)


def f13_cbsp_060_growth_capex_yoy(capex, depamor):
    return _yoy(_ttm(capex).abs() - _ttm(depamor))


# ---- Block D: working capital draw / cash drain (061-075) ----

def f13_cbsp_061_workingcapital_qoq_change(workingcapital):
    return workingcapital.diff()


def f13_cbsp_062_workingcapital_qoq_change_to_assets(workingcapital, assets):
    return _safe_div(workingcapital.diff(), assets)


def f13_cbsp_063_workingcapital_yoy_change(workingcapital):
    return _yoy(workingcapital)


def f13_cbsp_064_delta_receivables_to_revenue(receivables, revenue):
    return _safe_div(receivables.diff(), revenue.abs())


def f13_cbsp_065_delta_inventory_to_revenue(inventory, revenue):
    return _safe_div(inventory.diff(), revenue.abs())


def f13_cbsp_066_delta_payables_to_revenue(payables, revenue):
    return _safe_div(payables.diff(), revenue.abs())


def f13_cbsp_067_workingcapital_change_to_ocf(workingcapital, ncfo):
    return _safe_div(workingcapital.diff(), ncfo.abs())


def f13_cbsp_068_wc_swing_8q_std(workingcapital):
    return workingcapital.diff().rolling(8, min_periods=3).std()


def f13_cbsp_069_wc_cumulative_4q_change_to_assets(workingcapital, assets):
    return _safe_div(workingcapital.diff().rolling(4, min_periods=2).sum(), assets)


def f13_cbsp_070_delta_wc_minus_delta_revenue_to_assets(workingcapital, revenue, assets):
    return _safe_div(workingcapital.diff() - revenue.diff(), assets)


def f13_cbsp_071_delta_receivables_share_of_ocf(receivables, ncfo):
    return _safe_div(receivables.diff(), ncfo.abs())


def f13_cbsp_072_delta_inventory_share_of_ocf(inventory, ncfo):
    return _safe_div(inventory.diff(), ncfo.abs())


def f13_cbsp_073_delta_deferredrev_to_revenue(deferredrev, revenue):
    return _safe_div(deferredrev.diff(), revenue.abs())


def f13_cbsp_074_cash_drain_q_count_8q(cashneq):
    return (cashneq.diff() < 0).rolling(8, min_periods=3).sum()


def f13_cbsp_075_delta_currentassets_minus_delta_currentliabs_to_assets(assetsc, liabilitiesc, assets):
    return _safe_div(assetsc.diff() - liabilitiesc.diff(), assets)


# ============================================================
#                        REGISTRY
# ============================================================

CASH_BURN_SNAPSHOT_BASE_REGISTRY_001_075 = {
    "f13_cbsp_001_signed_log_fcf_ttm": {"inputs": ["fcf"], "func": f13_cbsp_001_signed_log_fcf_ttm},
    "f13_cbsp_002_fcf_to_assets_ttm": {"inputs": ["fcf", "assets"], "func": f13_cbsp_002_fcf_to_assets_ttm},
    "f13_cbsp_003_fcf_q_to_assets": {"inputs": ["fcf", "assets"], "func": f13_cbsp_003_fcf_q_to_assets},
    "f13_cbsp_004_fcf_q_to_revenue": {"inputs": ["fcf", "revenue"], "func": f13_cbsp_004_fcf_q_to_revenue},
    "f13_cbsp_005_ocf_to_assets_ttm": {"inputs": ["ncfo", "assets"], "func": f13_cbsp_005_ocf_to_assets_ttm},
    "f13_cbsp_006_ocf_to_equity_ttm": {"inputs": ["ncfo", "equity"], "func": f13_cbsp_006_ocf_to_equity_ttm},
    "f13_cbsp_007_signed_log_ncfo_ttm": {"inputs": ["ncfo"], "func": f13_cbsp_007_signed_log_ncfo_ttm},
    "f13_cbsp_008_capex_to_ocf_ratio": {"inputs": ["capex", "ncfo"], "func": f13_cbsp_008_capex_to_ocf_ratio},
    "f13_cbsp_009_fcf_to_ocf_ratio": {"inputs": ["fcf", "ncfo"], "func": f13_cbsp_009_fcf_to_ocf_ratio},
    "f13_cbsp_010_ocf_to_netinc_ratio": {"inputs": ["ncfo", "netinc"], "func": f13_cbsp_010_ocf_to_netinc_ratio},
    "f13_cbsp_011_burn_intensity_to_assets": {"inputs": ["fcf", "assets"], "func": f13_cbsp_011_burn_intensity_to_assets},
    "f13_cbsp_012_ncfo_to_equity_proxy": {"inputs": ["ncfo", "equity"], "func": f13_cbsp_012_ncfo_to_equity_proxy},
    "f13_cbsp_013_growth_capex_to_assets": {"inputs": ["capex", "depamor", "assets"], "func": f13_cbsp_013_growth_capex_to_assets},
    "f13_cbsp_014_discretionary_cash_to_revenue": {"inputs": ["ncfo", "capex", "intexp", "revenue"], "func": f13_cbsp_014_discretionary_cash_to_revenue},
    "f13_cbsp_015_fcf_q_share_of_4q": {"inputs": ["fcf"], "func": f13_cbsp_015_fcf_q_share_of_4q},
    "f13_cbsp_016_cash_to_equity": {"inputs": ["cashneq", "equity"], "func": f13_cbsp_016_cash_to_equity},
    "f13_cbsp_017_cash_to_assets": {"inputs": ["cashneq", "assets"], "func": f13_cbsp_017_cash_to_assets},
    "f13_cbsp_018_cash_to_currentassets": {"inputs": ["cashneq", "assetsc"], "func": f13_cbsp_018_cash_to_currentassets},
    "f13_cbsp_019_cash_to_currentliabilities": {"inputs": ["cashneq", "liabilitiesc"], "func": f13_cbsp_019_cash_to_currentliabilities},
    "f13_cbsp_020_cash_to_debt": {"inputs": ["cashneq", "debt"], "func": f13_cbsp_020_cash_to_debt},
    "f13_cbsp_021_cash_to_debt_current": {"inputs": ["cashneq", "debtc"], "func": f13_cbsp_021_cash_to_debt_current},
    "f13_cbsp_022_quick_ratio": {"inputs": ["cashneq", "receivables", "liabilitiesc"], "func": f13_cbsp_022_quick_ratio},
    "f13_cbsp_023_current_ratio": {"inputs": ["assetsc", "liabilitiesc"], "func": f13_cbsp_023_current_ratio},
    "f13_cbsp_024_workingcapital_to_revenue_ttm": {"inputs": ["workingcapital", "revenue"], "func": f13_cbsp_024_workingcapital_to_revenue_ttm},
    "f13_cbsp_025_workingcapital_to_assets": {"inputs": ["workingcapital", "assets"], "func": f13_cbsp_025_workingcapital_to_assets},
    "f13_cbsp_026_cash_runway_q_from_fcf": {"inputs": ["cashneq", "fcf"], "func": f13_cbsp_026_cash_runway_q_from_fcf},
    "f13_cbsp_027_cash_runway_q_from_ocf": {"inputs": ["cashneq", "ncfo"], "func": f13_cbsp_027_cash_runway_q_from_ocf},
    "f13_cbsp_028_net_cash_to_equity": {"inputs": ["cashneq", "debt", "equity"], "func": f13_cbsp_028_net_cash_to_equity},
    "f13_cbsp_029_liquid_assets_to_q_burn": {"inputs": ["cashneq", "receivables", "fcf"], "func": f13_cbsp_029_liquid_assets_to_q_burn},
    "f13_cbsp_030_net_cash_log_abs": {"inputs": ["cashneq", "debt"], "func": f13_cbsp_030_net_cash_log_abs},
    "f13_cbsp_031_net_cash_to_assets": {"inputs": ["cashneq", "debt", "assets"], "func": f13_cbsp_031_net_cash_to_assets},
    "f13_cbsp_032_cash_zscore_8q": {"inputs": ["cashneq"], "func": f13_cbsp_032_cash_zscore_8q},
    "f13_cbsp_033_cash_qoq_pct": {"inputs": ["cashneq"], "func": f13_cbsp_033_cash_qoq_pct},
    "f13_cbsp_034_cash_yoy_pct": {"inputs": ["cashneq"], "func": f13_cbsp_034_cash_yoy_pct},
    "f13_cbsp_035_cash_to_revenue_ttm": {"inputs": ["cashneq", "revenue"], "func": f13_cbsp_035_cash_to_revenue_ttm},
    "f13_cbsp_036_cash_minus_currentliabilities_to_assets": {"inputs": ["cashneq", "liabilitiesc", "assets"], "func": f13_cbsp_036_cash_minus_currentliabilities_to_assets},
    "f13_cbsp_037_cash_to_4q_burn_rate": {"inputs": ["cashneq", "fcf"], "func": f13_cbsp_037_cash_to_4q_burn_rate},
    "f13_cbsp_038_cash_to_8q_burn_rate": {"inputs": ["cashneq", "fcf"], "func": f13_cbsp_038_cash_to_8q_burn_rate},
    "f13_cbsp_039_cash_share_of_currentassets": {"inputs": ["cashneq", "assetsc"], "func": f13_cbsp_039_cash_share_of_currentassets},
    "f13_cbsp_040_liquidity_composite": {"inputs": ["cashneq", "receivables", "liabilitiesc"], "func": f13_cbsp_040_liquidity_composite},
    "f13_cbsp_041_capex_to_revenue_ttm": {"inputs": ["capex", "revenue"], "func": f13_cbsp_041_capex_to_revenue_ttm},
    "f13_cbsp_042_capex_to_assets": {"inputs": ["capex", "assets"], "func": f13_cbsp_042_capex_to_assets},
    "f13_cbsp_043_capex_to_ppe": {"inputs": ["capex", "ppnenet"], "func": f13_cbsp_043_capex_to_ppe},
    "f13_cbsp_044_capex_to_depamor": {"inputs": ["capex", "depamor"], "func": f13_cbsp_044_capex_to_depamor},
    "f13_cbsp_045_capex_yoy_pct": {"inputs": ["capex"], "func": f13_cbsp_045_capex_yoy_pct},
    "f13_cbsp_046_capex_qoq_pct": {"inputs": ["capex"], "func": f13_cbsp_046_capex_qoq_pct},
    "f13_cbsp_047_capex_to_ocf_ttm": {"inputs": ["capex", "ncfo"], "func": f13_cbsp_047_capex_to_ocf_ttm},
    "f13_cbsp_048_capex_intensity_zscore_8q": {"inputs": ["capex", "assets"], "func": f13_cbsp_048_capex_intensity_zscore_8q},
    "f13_cbsp_049_capex_q_minus_4q_avg_to_4q_avg": {"inputs": ["capex"], "func": f13_cbsp_049_capex_q_minus_4q_avg_to_4q_avg},
    "f13_cbsp_050_growth_capex_proxy": {"inputs": ["capex", "depamor"], "func": f13_cbsp_050_growth_capex_proxy},
    "f13_cbsp_051_growth_capex_to_assets": {"inputs": ["capex", "depamor", "assets"], "func": f13_cbsp_051_growth_capex_to_assets},
    "f13_cbsp_052_growth_capex_to_revenue": {"inputs": ["capex", "depamor", "revenue"], "func": f13_cbsp_052_growth_capex_to_revenue},
    "f13_cbsp_053_ncfi_to_assets": {"inputs": ["ncfi", "assets"], "func": f13_cbsp_053_ncfi_to_assets},
    "f13_cbsp_054_ncfi_to_revenue_ttm": {"inputs": ["ncfi", "revenue"], "func": f13_cbsp_054_ncfi_to_revenue_ttm},
    "f13_cbsp_055_ncfi_qoq_change": {"inputs": ["ncfi"], "func": f13_cbsp_055_ncfi_qoq_change},
    "f13_cbsp_056_capex_minus_ocf_to_assets": {"inputs": ["capex", "ncfo", "assets"], "func": f13_cbsp_056_capex_minus_ocf_to_assets},
    "f13_cbsp_057_ncfi_share_of_total_outflows": {"inputs": ["ncfi", "ncfo", "ncff"], "func": f13_cbsp_057_ncfi_share_of_total_outflows},
    "f13_cbsp_058_capex_consistency_8q": {"inputs": ["capex", "assets"], "func": f13_cbsp_058_capex_consistency_8q},
    "f13_cbsp_059_capex_to_invcap": {"inputs": ["capex", "equity", "debt"], "func": f13_cbsp_059_capex_to_invcap},
    "f13_cbsp_060_growth_capex_yoy": {"inputs": ["capex", "depamor"], "func": f13_cbsp_060_growth_capex_yoy},
    "f13_cbsp_061_workingcapital_qoq_change": {"inputs": ["workingcapital"], "func": f13_cbsp_061_workingcapital_qoq_change},
    "f13_cbsp_062_workingcapital_qoq_change_to_assets": {"inputs": ["workingcapital", "assets"], "func": f13_cbsp_062_workingcapital_qoq_change_to_assets},
    "f13_cbsp_063_workingcapital_yoy_change": {"inputs": ["workingcapital"], "func": f13_cbsp_063_workingcapital_yoy_change},
    "f13_cbsp_064_delta_receivables_to_revenue": {"inputs": ["receivables", "revenue"], "func": f13_cbsp_064_delta_receivables_to_revenue},
    "f13_cbsp_065_delta_inventory_to_revenue": {"inputs": ["inventory", "revenue"], "func": f13_cbsp_065_delta_inventory_to_revenue},
    "f13_cbsp_066_delta_payables_to_revenue": {"inputs": ["payables", "revenue"], "func": f13_cbsp_066_delta_payables_to_revenue},
    "f13_cbsp_067_workingcapital_change_to_ocf": {"inputs": ["workingcapital", "ncfo"], "func": f13_cbsp_067_workingcapital_change_to_ocf},
    "f13_cbsp_068_wc_swing_8q_std": {"inputs": ["workingcapital"], "func": f13_cbsp_068_wc_swing_8q_std},
    "f13_cbsp_069_wc_cumulative_4q_change_to_assets": {"inputs": ["workingcapital", "assets"], "func": f13_cbsp_069_wc_cumulative_4q_change_to_assets},
    "f13_cbsp_070_delta_wc_minus_delta_revenue_to_assets": {"inputs": ["workingcapital", "revenue", "assets"], "func": f13_cbsp_070_delta_wc_minus_delta_revenue_to_assets},
    "f13_cbsp_071_delta_receivables_share_of_ocf": {"inputs": ["receivables", "ncfo"], "func": f13_cbsp_071_delta_receivables_share_of_ocf},
    "f13_cbsp_072_delta_inventory_share_of_ocf": {"inputs": ["inventory", "ncfo"], "func": f13_cbsp_072_delta_inventory_share_of_ocf},
    "f13_cbsp_073_delta_deferredrev_to_revenue": {"inputs": ["deferredrev", "revenue"], "func": f13_cbsp_073_delta_deferredrev_to_revenue},
    "f13_cbsp_074_cash_drain_q_count_8q": {"inputs": ["cashneq"], "func": f13_cbsp_074_cash_drain_q_count_8q},
    "f13_cbsp_075_delta_currentassets_minus_delta_currentliabs_to_assets": {"inputs": ["assetsc", "liabilitiesc", "assets"], "func": f13_cbsp_075_delta_currentassets_minus_delta_currentliabs_to_assets},
}
