"""revenue_quality_level base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about revenue quality at peak (continued in __base__076_150.py).
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

# ---- Block A: revenue scale & turnover (001-015) ----

def f11_rqlv_001_log_revenue_ttm(revenue):
    return _safe_log(_ttm(revenue))


def f11_rqlv_002_revenue_ttm_to_assets(revenue, assets):
    return _safe_div(_ttm(revenue), assets)


def f11_rqlv_003_revenue_ttm_to_equity(revenue, equity):
    return _safe_div(_ttm(revenue), equity)


def f11_rqlv_004_revenue_ttm_to_invested_capital(revenue, equity, debt):
    return _safe_div(_ttm(revenue), equity + debt)


def f11_rqlv_005_revenue_ttm_to_workingcapital(revenue, workingcapital):
    return _safe_div(_ttm(revenue), workingcapital.abs())


def f11_rqlv_006_revenue_ttm_to_ppnenet(revenue, ppnenet):
    return _safe_div(_ttm(revenue), ppnenet)


def f11_rqlv_007_revenue_ttm_to_intangibles(revenue, intangibles):
    return _safe_div(_ttm(revenue), intangibles)


def f11_rqlv_008_revenue_ttm_to_opex(revenue, opex):
    return _safe_div(_ttm(revenue), _ttm(opex))


def f11_rqlv_009_revenue_per_share_ttm(revenue, shareswadil):
    return _safe_div(_ttm(revenue), shareswadil)


def f11_rqlv_010_revenue_per_basic_share_ttm(revenue, shareswa):
    return _safe_div(_ttm(revenue), shareswa)


def f11_rqlv_011_revenue_q_annualized_to_assets(revenue, assets):
    return _safe_div(revenue * 4.0, assets)


def f11_rqlv_012_revenue_q_annualized_minus_ttm_to_ttm(revenue):
    rev_ttm = _ttm(revenue)
    return _safe_div(revenue * 4.0 - rev_ttm, rev_ttm.abs())


def f11_rqlv_013_latest_q_share_of_ttm(revenue):
    return _safe_div(revenue, _ttm(revenue))


def f11_rqlv_014_revenue_4q_concentration_hhi(revenue):
    shares = []
    rev_ttm = _ttm(revenue).replace(0, np.nan)
    for lag in range(4):
        shares.append((revenue.shift(lag) / rev_ttm) ** 2)
    return sum(shares)


def f11_rqlv_015_revenue_ttm_to_total_capital(revenue, equity, debt, cashneq):
    return _safe_div(_ttm(revenue), equity + debt - cashneq)


# ---- Block B: receivables / channel stuffing (016-030) ----

def f11_rqlv_016_receivables_to_revenue_ttm(receivables, revenue):
    return _safe_div(receivables, _ttm(revenue))


def f11_rqlv_017_days_sales_outstanding_ttm(receivables, revenue):
    return _safe_div(365.0 * receivables, _ttm(revenue))


def f11_rqlv_018_receivables_to_revenue_q(receivables, revenue):
    return _safe_div(receivables, revenue)


def f11_rqlv_019_receivables_growth_minus_revenue_growth_yoy(receivables, revenue):
    return _yoy_pct(receivables) - _yoy_pct(_ttm(revenue))


def f11_rqlv_020_receivables_share_of_assets(receivables, assets):
    return _safe_div(receivables, assets)


def f11_rqlv_021_delta_receivables_to_delta_revenue_yoy(receivables, revenue):
    rev_ttm = _ttm(revenue)
    return _safe_div(_yoy(receivables), _yoy(rev_ttm).abs())


def f11_rqlv_022_receivables_to_currentassets(receivables, assetsc):
    return _safe_div(receivables, assetsc)


def f11_rqlv_023_receivables_to_workingcapital(receivables, workingcapital):
    return _safe_div(receivables, workingcapital.abs())


def f11_rqlv_024_receivables_to_cash(receivables, cashneq):
    return _safe_div(receivables, cashneq)


def f11_rqlv_025_dso_qoq_jump(receivables, revenue):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    return dso.diff()


def f11_rqlv_026_receivables_zscore_4q(receivables):
    return _rolling_zscore(receivables, 4, min_periods=2)


def f11_rqlv_027_receivables_share_q_minus_ttm_mean(receivables, revenue):
    share_q = _safe_div(receivables, revenue)
    return share_q - share_q.rolling(4, min_periods=2).mean()


def f11_rqlv_028_receivables_to_revenue_q_zscore_8q(receivables, revenue):
    ratio = _safe_div(receivables, revenue)
    return _rolling_zscore(ratio, 8, min_periods=3)


def f11_rqlv_029_revenue_minus_opcf_to_revenue(revenue, ncfo):
    return _safe_div(_ttm(revenue) - _ttm(ncfo), _ttm(revenue).abs())


def f11_rqlv_030_accrual_revenue_share(revenue, ncfo):
    return 1.0 - _safe_div(_ttm(ncfo), _ttm(revenue).abs())


# ---- Block C: deferred revenue / recurring (031-040) ----

def f11_rqlv_031_deferredrev_to_revenue_ttm(deferredrev, revenue):
    return _safe_div(deferredrev, _ttm(revenue))


def f11_rqlv_032_deferredrev_qoq_change_to_revenue(deferredrev, revenue):
    return _safe_div(deferredrev.diff(), revenue.abs())


def f11_rqlv_033_deferredrev_to_currentliabilities(deferredrev, liabilitiesc):
    return _safe_div(deferredrev, liabilitiesc)


def f11_rqlv_034_deferredrev_growth_minus_revenue_growth_yoy(deferredrev, revenue):
    return _yoy_pct(deferredrev) - _yoy_pct(_ttm(revenue))


def f11_rqlv_035_deferredrev_share_of_liabilities(deferredrev, liabilities):
    return _safe_div(deferredrev, liabilities)


def f11_rqlv_036_deferredrev_zscore_8q(deferredrev):
    return _rolling_zscore(deferredrev, 8, min_periods=3)


def f11_rqlv_037_deferredrev_to_marketcap_proxy(deferredrev, equity):
    return _safe_div(deferredrev, equity)


def f11_rqlv_038_deferredrev_qoq_pct(deferredrev):
    return _qoq_pct(deferredrev)


def f11_rqlv_039_deferredrev_decay_4q(deferredrev):
    return _safe_div(deferredrev - deferredrev.shift(4), deferredrev.shift(4).abs())


def f11_rqlv_040_recurring_revenue_proxy(deferredrev, revenue):
    return _safe_div(deferredrev * 4.0, _ttm(revenue))


# ---- Block D: gross margin / cost structure (041-055) ----

def f11_rqlv_041_gross_margin_ttm(gp, revenue):
    return _safe_div(_ttm(gp), _ttm(revenue))


def f11_rqlv_042_gross_margin_q(gp, revenue):
    return _safe_div(gp, revenue)


def f11_rqlv_043_gross_margin_q_minus_ttm(gp, revenue):
    return _safe_div(gp, revenue) - _safe_div(_ttm(gp), _ttm(revenue))


def f11_rqlv_044_cogs_share_of_revenue_ttm(cor, revenue):
    return _safe_div(_ttm(cor), _ttm(revenue))


def f11_rqlv_045_cogs_share_of_revenue_q(cor, revenue):
    return _safe_div(cor, revenue)


def f11_rqlv_046_sgna_to_revenue_ttm(sgna, revenue):
    return _safe_div(_ttm(sgna), _ttm(revenue))


def f11_rqlv_047_rnd_to_revenue_ttm(rnd, revenue):
    return _safe_div(_ttm(rnd), _ttm(revenue))


def f11_rqlv_048_opex_to_revenue_ttm(opex, revenue):
    return _safe_div(_ttm(opex), _ttm(revenue))


def f11_rqlv_049_operating_margin_ttm(opinc, revenue):
    return _safe_div(_ttm(opinc), _ttm(revenue))


def f11_rqlv_050_ebitda_margin_ttm(ebitda, revenue):
    return _safe_div(_ttm(ebitda), _ttm(revenue))


def f11_rqlv_051_ebit_margin_ttm(ebit, revenue):
    return _safe_div(_ttm(ebit), _ttm(revenue))


def f11_rqlv_052_fcf_margin_ttm(fcf, revenue):
    return _safe_div(_ttm(fcf), _ttm(revenue))


def f11_rqlv_053_revenue_minus_opex_share_ttm(revenue, opex):
    return _safe_div(_ttm(revenue) - _ttm(opex), _ttm(revenue).abs())


def f11_rqlv_054_sgna_growth_minus_revenue_growth_yoy(sgna, revenue):
    return _yoy_pct(_ttm(sgna)) - _yoy_pct(_ttm(revenue))


def f11_rqlv_055_rnd_growth_minus_revenue_growth_yoy(rnd, revenue):
    return _yoy_pct(_ttm(rnd)) - _yoy_pct(_ttm(revenue))


# ---- Block E: working capital intensity (056-070) ----

def f11_rqlv_056_workingcapital_to_revenue_ttm(workingcapital, revenue):
    return _safe_div(workingcapital, _ttm(revenue))


def f11_rqlv_057_inventory_to_revenue_ttm(inventory, revenue):
    return _safe_div(inventory, _ttm(revenue))


def f11_rqlv_058_days_inventory_ttm(inventory, cor):
    return _safe_div(365.0 * inventory, _ttm(cor))


def f11_rqlv_059_inventory_to_revenue_q(inventory, revenue):
    return _safe_div(inventory, revenue)


def f11_rqlv_060_inventory_growth_minus_revenue_growth_yoy(inventory, revenue):
    return _yoy_pct(inventory) - _yoy_pct(_ttm(revenue))


def f11_rqlv_061_payables_to_revenue_ttm(payables, revenue):
    return _safe_div(payables, _ttm(revenue))


def f11_rqlv_062_days_payable_ttm(payables, cor):
    return _safe_div(365.0 * payables, _ttm(cor))


def f11_rqlv_063_cash_conversion_cycle_ttm(receivables, inventory, payables, revenue, cor):
    dso = _safe_div(365.0 * receivables, _ttm(revenue))
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    dpo = _safe_div(365.0 * payables, _ttm(cor))
    return dso + dio - dpo


def f11_rqlv_064_inventory_share_of_currentassets(inventory, assetsc):
    return _safe_div(inventory, assetsc)


def f11_rqlv_065_inventory_zscore_8q(inventory):
    return _rolling_zscore(inventory, 8, min_periods=3)


def f11_rqlv_066_receivables_plus_inventory_to_revenue_ttm(receivables, inventory, revenue):
    return _safe_div(receivables + inventory, _ttm(revenue))


def f11_rqlv_067_workingcapital_share_of_assets(workingcapital, assets):
    return _safe_div(workingcapital, assets)


def f11_rqlv_068_inventory_obsolescence_proxy(inventory, revenue):
    return _yoy_pct(inventory) - _yoy_pct(_ttm(revenue))


def f11_rqlv_069_dio_qoq_jump(inventory, cor):
    dio = _safe_div(365.0 * inventory, _ttm(cor))
    return dio.diff()


def f11_rqlv_070_dpo_qoq_jump(payables, cor):
    dpo = _safe_div(365.0 * payables, _ttm(cor))
    return dpo.diff()


# ---- Block F (start): revenue volatility / smoothness — first 5 (071-075) ----

def f11_rqlv_071_revenue_qoq_stddev_4q(revenue):
    return revenue.diff().rolling(4, min_periods=2).std()


def f11_rqlv_072_revenue_qoq_stddev_8q(revenue):
    return revenue.diff().rolling(8, min_periods=3).std()


def f11_rqlv_073_revenue_yoy_stddev_8q(revenue):
    return _yoy(_ttm(revenue)).rolling(8, min_periods=3).std()


def f11_rqlv_074_revenue_cv_8q(revenue):
    m = revenue.rolling(8, min_periods=3).mean()
    sd = revenue.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs())


def f11_rqlv_075_revenue_qoq_max_drop_8q(revenue):
    return revenue.diff().rolling(8, min_periods=3).min()


# ============================================================
#                        REGISTRY
# ============================================================

REVENUE_QUALITY_LEVEL_BASE_REGISTRY_001_075 = {
    "f11_rqlv_001_log_revenue_ttm": {"inputs": ["revenue"], "func": f11_rqlv_001_log_revenue_ttm},
    "f11_rqlv_002_revenue_ttm_to_assets": {"inputs": ["revenue", "assets"], "func": f11_rqlv_002_revenue_ttm_to_assets},
    "f11_rqlv_003_revenue_ttm_to_equity": {"inputs": ["revenue", "equity"], "func": f11_rqlv_003_revenue_ttm_to_equity},
    "f11_rqlv_004_revenue_ttm_to_invested_capital": {"inputs": ["revenue", "equity", "debt"], "func": f11_rqlv_004_revenue_ttm_to_invested_capital},
    "f11_rqlv_005_revenue_ttm_to_workingcapital": {"inputs": ["revenue", "workingcapital"], "func": f11_rqlv_005_revenue_ttm_to_workingcapital},
    "f11_rqlv_006_revenue_ttm_to_ppnenet": {"inputs": ["revenue", "ppnenet"], "func": f11_rqlv_006_revenue_ttm_to_ppnenet},
    "f11_rqlv_007_revenue_ttm_to_intangibles": {"inputs": ["revenue", "intangibles"], "func": f11_rqlv_007_revenue_ttm_to_intangibles},
    "f11_rqlv_008_revenue_ttm_to_opex": {"inputs": ["revenue", "opex"], "func": f11_rqlv_008_revenue_ttm_to_opex},
    "f11_rqlv_009_revenue_per_share_ttm": {"inputs": ["revenue", "shareswadil"], "func": f11_rqlv_009_revenue_per_share_ttm},
    "f11_rqlv_010_revenue_per_basic_share_ttm": {"inputs": ["revenue", "shareswa"], "func": f11_rqlv_010_revenue_per_basic_share_ttm},
    "f11_rqlv_011_revenue_q_annualized_to_assets": {"inputs": ["revenue", "assets"], "func": f11_rqlv_011_revenue_q_annualized_to_assets},
    "f11_rqlv_012_revenue_q_annualized_minus_ttm_to_ttm": {"inputs": ["revenue"], "func": f11_rqlv_012_revenue_q_annualized_minus_ttm_to_ttm},
    "f11_rqlv_013_latest_q_share_of_ttm": {"inputs": ["revenue"], "func": f11_rqlv_013_latest_q_share_of_ttm},
    "f11_rqlv_014_revenue_4q_concentration_hhi": {"inputs": ["revenue"], "func": f11_rqlv_014_revenue_4q_concentration_hhi},
    "f11_rqlv_015_revenue_ttm_to_total_capital": {"inputs": ["revenue", "equity", "debt", "cashneq"], "func": f11_rqlv_015_revenue_ttm_to_total_capital},
    "f11_rqlv_016_receivables_to_revenue_ttm": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_016_receivables_to_revenue_ttm},
    "f11_rqlv_017_days_sales_outstanding_ttm": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_017_days_sales_outstanding_ttm},
    "f11_rqlv_018_receivables_to_revenue_q": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_018_receivables_to_revenue_q},
    "f11_rqlv_019_receivables_growth_minus_revenue_growth_yoy": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_019_receivables_growth_minus_revenue_growth_yoy},
    "f11_rqlv_020_receivables_share_of_assets": {"inputs": ["receivables", "assets"], "func": f11_rqlv_020_receivables_share_of_assets},
    "f11_rqlv_021_delta_receivables_to_delta_revenue_yoy": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_021_delta_receivables_to_delta_revenue_yoy},
    "f11_rqlv_022_receivables_to_currentassets": {"inputs": ["receivables", "assetsc"], "func": f11_rqlv_022_receivables_to_currentassets},
    "f11_rqlv_023_receivables_to_workingcapital": {"inputs": ["receivables", "workingcapital"], "func": f11_rqlv_023_receivables_to_workingcapital},
    "f11_rqlv_024_receivables_to_cash": {"inputs": ["receivables", "cashneq"], "func": f11_rqlv_024_receivables_to_cash},
    "f11_rqlv_025_dso_qoq_jump": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_025_dso_qoq_jump},
    "f11_rqlv_026_receivables_zscore_4q": {"inputs": ["receivables"], "func": f11_rqlv_026_receivables_zscore_4q},
    "f11_rqlv_027_receivables_share_q_minus_ttm_mean": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_027_receivables_share_q_minus_ttm_mean},
    "f11_rqlv_028_receivables_to_revenue_q_zscore_8q": {"inputs": ["receivables", "revenue"], "func": f11_rqlv_028_receivables_to_revenue_q_zscore_8q},
    "f11_rqlv_029_revenue_minus_opcf_to_revenue": {"inputs": ["revenue", "ncfo"], "func": f11_rqlv_029_revenue_minus_opcf_to_revenue},
    "f11_rqlv_030_accrual_revenue_share": {"inputs": ["revenue", "ncfo"], "func": f11_rqlv_030_accrual_revenue_share},
    "f11_rqlv_031_deferredrev_to_revenue_ttm": {"inputs": ["deferredrev", "revenue"], "func": f11_rqlv_031_deferredrev_to_revenue_ttm},
    "f11_rqlv_032_deferredrev_qoq_change_to_revenue": {"inputs": ["deferredrev", "revenue"], "func": f11_rqlv_032_deferredrev_qoq_change_to_revenue},
    "f11_rqlv_033_deferredrev_to_currentliabilities": {"inputs": ["deferredrev", "liabilitiesc"], "func": f11_rqlv_033_deferredrev_to_currentliabilities},
    "f11_rqlv_034_deferredrev_growth_minus_revenue_growth_yoy": {"inputs": ["deferredrev", "revenue"], "func": f11_rqlv_034_deferredrev_growth_minus_revenue_growth_yoy},
    "f11_rqlv_035_deferredrev_share_of_liabilities": {"inputs": ["deferredrev", "liabilities"], "func": f11_rqlv_035_deferredrev_share_of_liabilities},
    "f11_rqlv_036_deferredrev_zscore_8q": {"inputs": ["deferredrev"], "func": f11_rqlv_036_deferredrev_zscore_8q},
    "f11_rqlv_037_deferredrev_to_marketcap_proxy": {"inputs": ["deferredrev", "equity"], "func": f11_rqlv_037_deferredrev_to_marketcap_proxy},
    "f11_rqlv_038_deferredrev_qoq_pct": {"inputs": ["deferredrev"], "func": f11_rqlv_038_deferredrev_qoq_pct},
    "f11_rqlv_039_deferredrev_decay_4q": {"inputs": ["deferredrev"], "func": f11_rqlv_039_deferredrev_decay_4q},
    "f11_rqlv_040_recurring_revenue_proxy": {"inputs": ["deferredrev", "revenue"], "func": f11_rqlv_040_recurring_revenue_proxy},
    "f11_rqlv_041_gross_margin_ttm": {"inputs": ["gp", "revenue"], "func": f11_rqlv_041_gross_margin_ttm},
    "f11_rqlv_042_gross_margin_q": {"inputs": ["gp", "revenue"], "func": f11_rqlv_042_gross_margin_q},
    "f11_rqlv_043_gross_margin_q_minus_ttm": {"inputs": ["gp", "revenue"], "func": f11_rqlv_043_gross_margin_q_minus_ttm},
    "f11_rqlv_044_cogs_share_of_revenue_ttm": {"inputs": ["cor", "revenue"], "func": f11_rqlv_044_cogs_share_of_revenue_ttm},
    "f11_rqlv_045_cogs_share_of_revenue_q": {"inputs": ["cor", "revenue"], "func": f11_rqlv_045_cogs_share_of_revenue_q},
    "f11_rqlv_046_sgna_to_revenue_ttm": {"inputs": ["sgna", "revenue"], "func": f11_rqlv_046_sgna_to_revenue_ttm},
    "f11_rqlv_047_rnd_to_revenue_ttm": {"inputs": ["rnd", "revenue"], "func": f11_rqlv_047_rnd_to_revenue_ttm},
    "f11_rqlv_048_opex_to_revenue_ttm": {"inputs": ["opex", "revenue"], "func": f11_rqlv_048_opex_to_revenue_ttm},
    "f11_rqlv_049_operating_margin_ttm": {"inputs": ["opinc", "revenue"], "func": f11_rqlv_049_operating_margin_ttm},
    "f11_rqlv_050_ebitda_margin_ttm": {"inputs": ["ebitda", "revenue"], "func": f11_rqlv_050_ebitda_margin_ttm},
    "f11_rqlv_051_ebit_margin_ttm": {"inputs": ["ebit", "revenue"], "func": f11_rqlv_051_ebit_margin_ttm},
    "f11_rqlv_052_fcf_margin_ttm": {"inputs": ["fcf", "revenue"], "func": f11_rqlv_052_fcf_margin_ttm},
    "f11_rqlv_053_revenue_minus_opex_share_ttm": {"inputs": ["revenue", "opex"], "func": f11_rqlv_053_revenue_minus_opex_share_ttm},
    "f11_rqlv_054_sgna_growth_minus_revenue_growth_yoy": {"inputs": ["sgna", "revenue"], "func": f11_rqlv_054_sgna_growth_minus_revenue_growth_yoy},
    "f11_rqlv_055_rnd_growth_minus_revenue_growth_yoy": {"inputs": ["rnd", "revenue"], "func": f11_rqlv_055_rnd_growth_minus_revenue_growth_yoy},
    "f11_rqlv_056_workingcapital_to_revenue_ttm": {"inputs": ["workingcapital", "revenue"], "func": f11_rqlv_056_workingcapital_to_revenue_ttm},
    "f11_rqlv_057_inventory_to_revenue_ttm": {"inputs": ["inventory", "revenue"], "func": f11_rqlv_057_inventory_to_revenue_ttm},
    "f11_rqlv_058_days_inventory_ttm": {"inputs": ["inventory", "cor"], "func": f11_rqlv_058_days_inventory_ttm},
    "f11_rqlv_059_inventory_to_revenue_q": {"inputs": ["inventory", "revenue"], "func": f11_rqlv_059_inventory_to_revenue_q},
    "f11_rqlv_060_inventory_growth_minus_revenue_growth_yoy": {"inputs": ["inventory", "revenue"], "func": f11_rqlv_060_inventory_growth_minus_revenue_growth_yoy},
    "f11_rqlv_061_payables_to_revenue_ttm": {"inputs": ["payables", "revenue"], "func": f11_rqlv_061_payables_to_revenue_ttm},
    "f11_rqlv_062_days_payable_ttm": {"inputs": ["payables", "cor"], "func": f11_rqlv_062_days_payable_ttm},
    "f11_rqlv_063_cash_conversion_cycle_ttm": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f11_rqlv_063_cash_conversion_cycle_ttm},
    "f11_rqlv_064_inventory_share_of_currentassets": {"inputs": ["inventory", "assetsc"], "func": f11_rqlv_064_inventory_share_of_currentassets},
    "f11_rqlv_065_inventory_zscore_8q": {"inputs": ["inventory"], "func": f11_rqlv_065_inventory_zscore_8q},
    "f11_rqlv_066_receivables_plus_inventory_to_revenue_ttm": {"inputs": ["receivables", "inventory", "revenue"], "func": f11_rqlv_066_receivables_plus_inventory_to_revenue_ttm},
    "f11_rqlv_067_workingcapital_share_of_assets": {"inputs": ["workingcapital", "assets"], "func": f11_rqlv_067_workingcapital_share_of_assets},
    "f11_rqlv_068_inventory_obsolescence_proxy": {"inputs": ["inventory", "revenue"], "func": f11_rqlv_068_inventory_obsolescence_proxy},
    "f11_rqlv_069_dio_qoq_jump": {"inputs": ["inventory", "cor"], "func": f11_rqlv_069_dio_qoq_jump},
    "f11_rqlv_070_dpo_qoq_jump": {"inputs": ["payables", "cor"], "func": f11_rqlv_070_dpo_qoq_jump},
    "f11_rqlv_071_revenue_qoq_stddev_4q": {"inputs": ["revenue"], "func": f11_rqlv_071_revenue_qoq_stddev_4q},
    "f11_rqlv_072_revenue_qoq_stddev_8q": {"inputs": ["revenue"], "func": f11_rqlv_072_revenue_qoq_stddev_8q},
    "f11_rqlv_073_revenue_yoy_stddev_8q": {"inputs": ["revenue"], "func": f11_rqlv_073_revenue_yoy_stddev_8q},
    "f11_rqlv_074_revenue_cv_8q": {"inputs": ["revenue"], "func": f11_rqlv_074_revenue_cv_8q},
    "f11_rqlv_075_revenue_qoq_max_drop_8q": {"inputs": ["revenue"], "func": f11_rqlv_075_revenue_qoq_max_drop_8q},
}
