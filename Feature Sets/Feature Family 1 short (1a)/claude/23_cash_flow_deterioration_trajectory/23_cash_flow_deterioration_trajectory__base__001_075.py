"""cash_flow_deterioration_trajectory base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about the cash-flow deterioration ARC: how operating cash flow,
free cash flow, cash position, and cash conversion turn negative or weaken over multiple
quarters BEFORE the price peak (continued in __base__076_150.py).
Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no forward-looking shifts. Functions consume named pandas Series whose
index is the family-agnostic time index supplied by the harness.
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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


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


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: OCF level & trajectory (001-015) ----

def f23_cfdt_001_ncfo_ttm_to_assets(ncfo, assets):
    return _safe_div(_ttm(ncfo), assets)


def f23_cfdt_002_ncfo_margin_ttm(ncfo, revenue):
    return _safe_div(_ttm(ncfo), _ttm(revenue))


def f23_cfdt_003_ncfo_q_to_revenue_q(ncfo, revenue):
    return _safe_div(ncfo, revenue)


def f23_cfdt_004_ncfo_yoy_pct_ttm(ncfo):
    return _yoy_pct(_ttm(ncfo))


def f23_cfdt_005_ncfo_qoq_pct(ncfo):
    return _qoq_pct(ncfo)


def f23_cfdt_006_ncfo_ttm_trend_slope_8q(ncfo):
    ttm = _ttm(ncfo)
    m = ttm.rolling(8, min_periods=3).mean()
    return _safe_div(ttm - m, m.abs())


def f23_cfdt_007_ncfo_margin_decay_yoy(ncfo, revenue):
    m_now = _safe_div(_ttm(ncfo), _ttm(revenue))
    return m_now - m_now.shift(4)


def f23_cfdt_008_ncfo_minus_netinc_to_assets(ncfo, netinc, assets):
    return _safe_div(_ttm(ncfo) - _ttm(netinc), assets)


def f23_cfdt_009_log_abs_ncfo_ttm(ncfo):
    return _safe_log_abs(_ttm(ncfo))


def f23_cfdt_010_neg_ncfo_streak_4q(ncfo):
    neg = (ncfo < 0).astype(float)
    return neg.rolling(4, min_periods=1).sum()


def f23_cfdt_011_ncfo_avg4_to_avg4_lagged(ncfo):
    a = _avg4(ncfo)
    return _safe_div(a, a.shift(4).abs())


def f23_cfdt_012_ncfo_share_of_ebitda(ncfo, ebitda):
    return _safe_div(_ttm(ncfo), _ttm(ebitda).abs())


def f23_cfdt_013_ncfo_to_equity(ncfo, equity):
    return _safe_div(_ttm(ncfo), equity)


def f23_cfdt_014_ncfo_to_liabilities(ncfo, liabilities):
    return _safe_div(_ttm(ncfo), liabilities)


def f23_cfdt_015_ncfo_per_share(ncfo, shareswadil):
    return _safe_div(_ttm(ncfo), shareswadil)


# ---- Block B: FCF level & trajectory (016-030) ----

def f23_cfdt_016_fcf_margin_ttm(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue))


def f23_cfdt_017_fcf_to_assets(fcf, assets):
    return _safe_div(_ttm(fcf), assets)


def f23_cfdt_018_fcf_yield_proxy_to_equity(fcf, equity):
    return _safe_div(_ttm(fcf), equity)


def f23_cfdt_019_fcf_to_invested_capital(fcf, equity, debt):
    return _safe_div(_ttm(fcf), equity + debt)


def f23_cfdt_020_fcf_per_share(fcf, shareswadil):
    return _safe_div(_ttm(fcf), shareswadil)


def f23_cfdt_021_fcf_yoy_pct_ttm(fcf):
    return _yoy_pct(_ttm(fcf))


def f23_cfdt_022_fcf_qoq_pct(fcf):
    return _qoq_pct(fcf)


def f23_cfdt_023_neg_fcf_streak_4q(fcf):
    neg = (fcf < 0).astype(float)
    return neg.rolling(4, min_periods=1).sum()


def f23_cfdt_024_neg_fcf_streak_8q(fcf):
    neg = (fcf < 0).astype(float)
    return neg.rolling(8, min_periods=2).sum()


def f23_cfdt_025_fcf_margin_minus_4q_lag(fcf, revenue):
    m_now = _safe_div(_ttm(fcf), _ttm(revenue))
    return m_now - m_now.shift(4)


def f23_cfdt_026_fcf_to_debt(fcf, debt):
    return _safe_div(_ttm(fcf), debt)


def f23_cfdt_027_fcf_to_marketcap_proxy(fcf, equity):
    return _safe_div(_ttm(fcf), equity.abs())


def f23_cfdt_028_fcf_ttm_zscore_8q(fcf):
    return _rolling_zscore(_ttm(fcf), 8, min_periods=3)


def f23_cfdt_029_fcf_avg4_decay_yoy(fcf):
    a = _avg4(fcf)
    return _safe_div(a - a.shift(4), a.shift(4).abs())


def f23_cfdt_030_log_abs_fcf_ttm(fcf):
    return _safe_log_abs(_ttm(fcf))


# ---- Block C: capex burn & under-investment (031-045) ----

def f23_cfdt_031_capex_to_revenue_ttm(capex, revenue):
    return _safe_div(_ttm(capex).abs(), _ttm(revenue))


def f23_cfdt_032_capex_to_depamor_ttm(capex, depamor):
    return _safe_div(_ttm(capex).abs(), _ttm(depamor))


def f23_cfdt_033_capex_to_assets(capex, assets):
    return _safe_div(_ttm(capex).abs(), assets)


def f23_cfdt_034_capex_minus_depamor_to_assets(capex, depamor, assets):
    return _safe_div(_ttm(capex).abs() - _ttm(depamor), assets)


def f23_cfdt_035_capex_ttm_yoy_pct(capex):
    return _yoy_pct(_ttm(capex).abs())


def f23_cfdt_036_capex_to_ncfo(capex, ncfo):
    return _safe_div(_ttm(capex).abs(), _ttm(ncfo).abs())


def f23_cfdt_037_depamor_minus_capex_to_revenue(capex, depamor, revenue):
    return _safe_div(_ttm(depamor) - _ttm(capex).abs(), _ttm(revenue))


def f23_cfdt_038_capex_share_of_opex(capex, opex):
    return _safe_div(_ttm(capex).abs(), _ttm(opex))


def f23_cfdt_039_capex_to_ppnenet(capex, ppnenet):
    return _safe_div(_ttm(capex).abs(), ppnenet)


def f23_cfdt_040_capex_q_to_revenue_q(capex, revenue):
    return _safe_div(capex.abs(), revenue)


def f23_cfdt_041_capex_qoq_jump(capex):
    return capex.abs().diff()


def f23_cfdt_042_capex_intensity_vs_4q_mean(capex, revenue):
    r = _safe_div(capex.abs(), revenue)
    return r - r.rolling(4, min_periods=2).mean()


def f23_cfdt_043_capex_growth_minus_revenue_growth_yoy(capex, revenue):
    return _yoy_pct(_ttm(capex).abs()) - _yoy_pct(_ttm(revenue))


def f23_cfdt_044_capex_ttm_zscore_12q(capex):
    return _rolling_zscore(_ttm(capex).abs(), 12, min_periods=4)


def f23_cfdt_045_under_investment_gap_ratio(capex, depamor):
    return _safe_div(_ttm(depamor) - _ttm(capex).abs(), _ttm(depamor).abs())


# ---- Block D: accruals & cash quality (046-060) ----

def f23_cfdt_046_accrual_ratio_balance_sheet(netinc, ncfo, assets):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), assets)


def f23_cfdt_047_accrual_ratio_to_revenue(netinc, ncfo, revenue):
    return _safe_div(_ttm(netinc) - _ttm(ncfo), _ttm(revenue).abs())


def f23_cfdt_048_ncfo_to_netinc_quality(ncfo, netinc):
    return _safe_div(_ttm(ncfo), _ttm(netinc).abs())


def f23_cfdt_049_fcf_to_netinc_conversion(fcf, netinc):
    return _safe_div(_ttm(fcf), _ttm(netinc).abs())


def f23_cfdt_050_fcf_to_ebitda_conversion(fcf, ebitda):
    return _safe_div(_ttm(fcf), _ttm(ebitda).abs())


def f23_cfdt_051_ncfo_to_ebitda_conversion(ncfo, ebitda):
    return _safe_div(_ttm(ncfo), _ttm(ebitda).abs())


def f23_cfdt_052_ncfo_to_opinc_conversion(ncfo, opinc):
    return _safe_div(_ttm(ncfo), _ttm(opinc).abs())


def f23_cfdt_053_accrual_widening_yoy(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return a - a.shift(4)


def f23_cfdt_054_accrual_zscore_8q(netinc, ncfo, assets):
    a = _safe_div(_ttm(netinc) - _ttm(ncfo), assets)
    return _rolling_zscore(a, 8, min_periods=3)


def f23_cfdt_055_cash_conversion_decay_4q(fcf, netinc):
    c = _safe_div(_ttm(fcf), _ttm(netinc).abs())
    return c - c.shift(4)


def f23_cfdt_056_sbcomp_offset_to_ncfo(sbcomp, ncfo):
    return _safe_div(_ttm(sbcomp), _ttm(ncfo).abs())


def f23_cfdt_057_sbcomp_share_of_revenue(sbcomp, revenue):
    return _safe_div(_ttm(sbcomp), _ttm(revenue))


def f23_cfdt_058_ncfo_ex_sbcomp_margin(ncfo, sbcomp, revenue):
    return _safe_div(_ttm(ncfo) - _ttm(sbcomp), _ttm(revenue))


def f23_cfdt_059_sbcomp_growth_minus_ncfo_growth_yoy(sbcomp, ncfo):
    return _yoy_pct(_ttm(sbcomp)) - _yoy_pct(_ttm(ncfo).abs())


def f23_cfdt_060_accrual_to_avg_assets(netinc, ncfo, assets):
    avg_a = _avg4(assets)
    return _safe_div(_ttm(netinc) - _ttm(ncfo), avg_a)


# ---- Block E: working-capital cash drag (061-075) ----

def f23_cfdt_061_deltawc_to_revenue_ttm(deltawc, revenue):
    return _safe_div(_ttm(deltawc), _ttm(revenue))


def f23_cfdt_062_deltawc_to_ncfo(deltawc, ncfo):
    return _safe_div(_ttm(deltawc), _ttm(ncfo).abs())


def f23_cfdt_063_deltawc_persistent_drag_4q(deltawc):
    drag = (deltawc > 0).astype(float)
    return drag.rolling(4, min_periods=1).sum()


def f23_cfdt_064_workingcapital_qoq_change_to_revenue(workingcapital, revenue):
    return _safe_div(workingcapital.diff(), _ttm(revenue))


def f23_cfdt_065_receivables_absorbing_cash_to_revenue(receivables, revenue):
    return _safe_div(receivables.diff(), _ttm(revenue))


def f23_cfdt_066_inventory_absorbing_cash_to_revenue(inventory, revenue):
    return _safe_div(inventory.diff(), _ttm(revenue))


def f23_cfdt_067_payables_giving_up_cash_to_revenue(payables, revenue):
    return _safe_div(-payables.diff(), _ttm(revenue))


def f23_cfdt_068_wc_components_cash_drag_sum(receivables, inventory, payables, revenue):
    drag = receivables.diff() + inventory.diff() - payables.diff()
    return _safe_div(drag, _ttm(revenue))


def f23_cfdt_069_deltawc_growth_yoy(deltawc):
    return _yoy_pct(_ttm(deltawc))


def f23_cfdt_070_workingcapital_share_of_ncfo(workingcapital, ncfo):
    return _safe_div(workingcapital, _ttm(ncfo).abs())


def f23_cfdt_071_wc_to_revenue_decay_4q(workingcapital, revenue):
    r = _safe_div(workingcapital, _ttm(revenue))
    return r - r.shift(4)


def f23_cfdt_072_deltawc_zscore_8q(deltawc):
    return _rolling_zscore(deltawc, 8, min_periods=3)


def f23_cfdt_073_receivables_inventory_growth_minus_revenue(receivables, inventory, revenue):
    return _yoy_pct(receivables + inventory) - _yoy_pct(_ttm(revenue))


def f23_cfdt_074_wc_intensity_qoq_jump(workingcapital, revenue):
    return _safe_div(workingcapital, _ttm(revenue)).diff()


def f23_cfdt_075_persistent_wc_buildup_8q(workingcapital):
    pos = (workingcapital.diff() > 0).astype(float)
    return pos.rolling(8, min_periods=2).sum()


# ============================================================
#                        REGISTRY
# ============================================================

CASH_FLOW_DETERIORATION_TRAJECTORY_BASE_REGISTRY_001_075 = {
    "f23_cfdt_001_ncfo_ttm_to_assets": {"inputs": ["ncfo", "assets"], "func": f23_cfdt_001_ncfo_ttm_to_assets},
    "f23_cfdt_002_ncfo_margin_ttm": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_002_ncfo_margin_ttm},
    "f23_cfdt_003_ncfo_q_to_revenue_q": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_003_ncfo_q_to_revenue_q},
    "f23_cfdt_004_ncfo_yoy_pct_ttm": {"inputs": ["ncfo"], "func": f23_cfdt_004_ncfo_yoy_pct_ttm},
    "f23_cfdt_005_ncfo_qoq_pct": {"inputs": ["ncfo"], "func": f23_cfdt_005_ncfo_qoq_pct},
    "f23_cfdt_006_ncfo_ttm_trend_slope_8q": {"inputs": ["ncfo"], "func": f23_cfdt_006_ncfo_ttm_trend_slope_8q},
    "f23_cfdt_007_ncfo_margin_decay_yoy": {"inputs": ["ncfo", "revenue"], "func": f23_cfdt_007_ncfo_margin_decay_yoy},
    "f23_cfdt_008_ncfo_minus_netinc_to_assets": {"inputs": ["ncfo", "netinc", "assets"], "func": f23_cfdt_008_ncfo_minus_netinc_to_assets},
    "f23_cfdt_009_log_abs_ncfo_ttm": {"inputs": ["ncfo"], "func": f23_cfdt_009_log_abs_ncfo_ttm},
    "f23_cfdt_010_neg_ncfo_streak_4q": {"inputs": ["ncfo"], "func": f23_cfdt_010_neg_ncfo_streak_4q},
    "f23_cfdt_011_ncfo_avg4_to_avg4_lagged": {"inputs": ["ncfo"], "func": f23_cfdt_011_ncfo_avg4_to_avg4_lagged},
    "f23_cfdt_012_ncfo_share_of_ebitda": {"inputs": ["ncfo", "ebitda"], "func": f23_cfdt_012_ncfo_share_of_ebitda},
    "f23_cfdt_013_ncfo_to_equity": {"inputs": ["ncfo", "equity"], "func": f23_cfdt_013_ncfo_to_equity},
    "f23_cfdt_014_ncfo_to_liabilities": {"inputs": ["ncfo", "liabilities"], "func": f23_cfdt_014_ncfo_to_liabilities},
    "f23_cfdt_015_ncfo_per_share": {"inputs": ["ncfo", "shareswadil"], "func": f23_cfdt_015_ncfo_per_share},
    "f23_cfdt_016_fcf_margin_ttm": {"inputs": ["fcf", "revenue"], "func": f23_cfdt_016_fcf_margin_ttm},
    "f23_cfdt_017_fcf_to_assets": {"inputs": ["fcf", "assets"], "func": f23_cfdt_017_fcf_to_assets},
    "f23_cfdt_018_fcf_yield_proxy_to_equity": {"inputs": ["fcf", "equity"], "func": f23_cfdt_018_fcf_yield_proxy_to_equity},
    "f23_cfdt_019_fcf_to_invested_capital": {"inputs": ["fcf", "equity", "debt"], "func": f23_cfdt_019_fcf_to_invested_capital},
    "f23_cfdt_020_fcf_per_share": {"inputs": ["fcf", "shareswadil"], "func": f23_cfdt_020_fcf_per_share},
    "f23_cfdt_021_fcf_yoy_pct_ttm": {"inputs": ["fcf"], "func": f23_cfdt_021_fcf_yoy_pct_ttm},
    "f23_cfdt_022_fcf_qoq_pct": {"inputs": ["fcf"], "func": f23_cfdt_022_fcf_qoq_pct},
    "f23_cfdt_023_neg_fcf_streak_4q": {"inputs": ["fcf"], "func": f23_cfdt_023_neg_fcf_streak_4q},
    "f23_cfdt_024_neg_fcf_streak_8q": {"inputs": ["fcf"], "func": f23_cfdt_024_neg_fcf_streak_8q},
    "f23_cfdt_025_fcf_margin_minus_4q_lag": {"inputs": ["fcf", "revenue"], "func": f23_cfdt_025_fcf_margin_minus_4q_lag},
    "f23_cfdt_026_fcf_to_debt": {"inputs": ["fcf", "debt"], "func": f23_cfdt_026_fcf_to_debt},
    "f23_cfdt_027_fcf_to_marketcap_proxy": {"inputs": ["fcf", "equity"], "func": f23_cfdt_027_fcf_to_marketcap_proxy},
    "f23_cfdt_028_fcf_ttm_zscore_8q": {"inputs": ["fcf"], "func": f23_cfdt_028_fcf_ttm_zscore_8q},
    "f23_cfdt_029_fcf_avg4_decay_yoy": {"inputs": ["fcf"], "func": f23_cfdt_029_fcf_avg4_decay_yoy},
    "f23_cfdt_030_log_abs_fcf_ttm": {"inputs": ["fcf"], "func": f23_cfdt_030_log_abs_fcf_ttm},
    "f23_cfdt_031_capex_to_revenue_ttm": {"inputs": ["capex", "revenue"], "func": f23_cfdt_031_capex_to_revenue_ttm},
    "f23_cfdt_032_capex_to_depamor_ttm": {"inputs": ["capex", "depamor"], "func": f23_cfdt_032_capex_to_depamor_ttm},
    "f23_cfdt_033_capex_to_assets": {"inputs": ["capex", "assets"], "func": f23_cfdt_033_capex_to_assets},
    "f23_cfdt_034_capex_minus_depamor_to_assets": {"inputs": ["capex", "depamor", "assets"], "func": f23_cfdt_034_capex_minus_depamor_to_assets},
    "f23_cfdt_035_capex_ttm_yoy_pct": {"inputs": ["capex"], "func": f23_cfdt_035_capex_ttm_yoy_pct},
    "f23_cfdt_036_capex_to_ncfo": {"inputs": ["capex", "ncfo"], "func": f23_cfdt_036_capex_to_ncfo},
    "f23_cfdt_037_depamor_minus_capex_to_revenue": {"inputs": ["capex", "depamor", "revenue"], "func": f23_cfdt_037_depamor_minus_capex_to_revenue},
    "f23_cfdt_038_capex_share_of_opex": {"inputs": ["capex", "opex"], "func": f23_cfdt_038_capex_share_of_opex},
    "f23_cfdt_039_capex_to_ppnenet": {"inputs": ["capex", "ppnenet"], "func": f23_cfdt_039_capex_to_ppnenet},
    "f23_cfdt_040_capex_q_to_revenue_q": {"inputs": ["capex", "revenue"], "func": f23_cfdt_040_capex_q_to_revenue_q},
    "f23_cfdt_041_capex_qoq_jump": {"inputs": ["capex"], "func": f23_cfdt_041_capex_qoq_jump},
    "f23_cfdt_042_capex_intensity_vs_4q_mean": {"inputs": ["capex", "revenue"], "func": f23_cfdt_042_capex_intensity_vs_4q_mean},
    "f23_cfdt_043_capex_growth_minus_revenue_growth_yoy": {"inputs": ["capex", "revenue"], "func": f23_cfdt_043_capex_growth_minus_revenue_growth_yoy},
    "f23_cfdt_044_capex_ttm_zscore_12q": {"inputs": ["capex"], "func": f23_cfdt_044_capex_ttm_zscore_12q},
    "f23_cfdt_045_under_investment_gap_ratio": {"inputs": ["capex", "depamor"], "func": f23_cfdt_045_under_investment_gap_ratio},
    "f23_cfdt_046_accrual_ratio_balance_sheet": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_046_accrual_ratio_balance_sheet},
    "f23_cfdt_047_accrual_ratio_to_revenue": {"inputs": ["netinc", "ncfo", "revenue"], "func": f23_cfdt_047_accrual_ratio_to_revenue},
    "f23_cfdt_048_ncfo_to_netinc_quality": {"inputs": ["ncfo", "netinc"], "func": f23_cfdt_048_ncfo_to_netinc_quality},
    "f23_cfdt_049_fcf_to_netinc_conversion": {"inputs": ["fcf", "netinc"], "func": f23_cfdt_049_fcf_to_netinc_conversion},
    "f23_cfdt_050_fcf_to_ebitda_conversion": {"inputs": ["fcf", "ebitda"], "func": f23_cfdt_050_fcf_to_ebitda_conversion},
    "f23_cfdt_051_ncfo_to_ebitda_conversion": {"inputs": ["ncfo", "ebitda"], "func": f23_cfdt_051_ncfo_to_ebitda_conversion},
    "f23_cfdt_052_ncfo_to_opinc_conversion": {"inputs": ["ncfo", "opinc"], "func": f23_cfdt_052_ncfo_to_opinc_conversion},
    "f23_cfdt_053_accrual_widening_yoy": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_053_accrual_widening_yoy},
    "f23_cfdt_054_accrual_zscore_8q": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_054_accrual_zscore_8q},
    "f23_cfdt_055_cash_conversion_decay_4q": {"inputs": ["fcf", "netinc"], "func": f23_cfdt_055_cash_conversion_decay_4q},
    "f23_cfdt_056_sbcomp_offset_to_ncfo": {"inputs": ["sbcomp", "ncfo"], "func": f23_cfdt_056_sbcomp_offset_to_ncfo},
    "f23_cfdt_057_sbcomp_share_of_revenue": {"inputs": ["sbcomp", "revenue"], "func": f23_cfdt_057_sbcomp_share_of_revenue},
    "f23_cfdt_058_ncfo_ex_sbcomp_margin": {"inputs": ["ncfo", "sbcomp", "revenue"], "func": f23_cfdt_058_ncfo_ex_sbcomp_margin},
    "f23_cfdt_059_sbcomp_growth_minus_ncfo_growth_yoy": {"inputs": ["sbcomp", "ncfo"], "func": f23_cfdt_059_sbcomp_growth_minus_ncfo_growth_yoy},
    "f23_cfdt_060_accrual_to_avg_assets": {"inputs": ["netinc", "ncfo", "assets"], "func": f23_cfdt_060_accrual_to_avg_assets},
    "f23_cfdt_061_deltawc_to_revenue_ttm": {"inputs": ["deltawc", "revenue"], "func": f23_cfdt_061_deltawc_to_revenue_ttm},
    "f23_cfdt_062_deltawc_to_ncfo": {"inputs": ["deltawc", "ncfo"], "func": f23_cfdt_062_deltawc_to_ncfo},
    "f23_cfdt_063_deltawc_persistent_drag_4q": {"inputs": ["deltawc"], "func": f23_cfdt_063_deltawc_persistent_drag_4q},
    "f23_cfdt_064_workingcapital_qoq_change_to_revenue": {"inputs": ["workingcapital", "revenue"], "func": f23_cfdt_064_workingcapital_qoq_change_to_revenue},
    "f23_cfdt_065_receivables_absorbing_cash_to_revenue": {"inputs": ["receivables", "revenue"], "func": f23_cfdt_065_receivables_absorbing_cash_to_revenue},
    "f23_cfdt_066_inventory_absorbing_cash_to_revenue": {"inputs": ["inventory", "revenue"], "func": f23_cfdt_066_inventory_absorbing_cash_to_revenue},
    "f23_cfdt_067_payables_giving_up_cash_to_revenue": {"inputs": ["payables", "revenue"], "func": f23_cfdt_067_payables_giving_up_cash_to_revenue},
    "f23_cfdt_068_wc_components_cash_drag_sum": {"inputs": ["receivables", "inventory", "payables", "revenue"], "func": f23_cfdt_068_wc_components_cash_drag_sum},
    "f23_cfdt_069_deltawc_growth_yoy": {"inputs": ["deltawc"], "func": f23_cfdt_069_deltawc_growth_yoy},
    "f23_cfdt_070_workingcapital_share_of_ncfo": {"inputs": ["workingcapital", "ncfo"], "func": f23_cfdt_070_workingcapital_share_of_ncfo},
    "f23_cfdt_071_wc_to_revenue_decay_4q": {"inputs": ["workingcapital", "revenue"], "func": f23_cfdt_071_wc_to_revenue_decay_4q},
    "f23_cfdt_072_deltawc_zscore_8q": {"inputs": ["deltawc"], "func": f23_cfdt_072_deltawc_zscore_8q},
    "f23_cfdt_073_receivables_inventory_growth_minus_revenue": {"inputs": ["receivables", "inventory", "revenue"], "func": f23_cfdt_073_receivables_inventory_growth_minus_revenue},
    "f23_cfdt_074_wc_intensity_qoq_jump": {"inputs": ["workingcapital", "revenue"], "func": f23_cfdt_074_wc_intensity_qoq_jump},
    "f23_cfdt_075_persistent_wc_buildup_8q": {"inputs": ["workingcapital"], "func": f23_cfdt_075_persistent_wc_buildup_8q},
}
