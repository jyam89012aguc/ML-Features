"""balance_sheet_stress_snapshot d2 features 001_075 - second-derivative (acceleration) wrappers.

Each function inlines the corresponding base computation and appends .diff().diff() to
produce the second-derivative (acceleration) of that signal. Inputs and PIT discipline match the base file.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _winsorize(s, lower=0.01, upper=0.99, window=YDAYS):
    mp = max(window // 3, 2)
    lo = s.rolling(window, min_periods=mp).quantile(lower)
    hi = s.rolling(window, min_periods=mp).quantile(upper)
    return s.clip(lower=lo, upper=hi)


def _yoy_change(s, n=YDAYS):
    return s - s.shift(n)


def _yoy_pct(s, n=YDAYS):
    prev = s.shift(n).replace(0, np.nan)
    return (s - prev) / prev.abs()


# ============================================================
#                D2 FEATURES 001_075
# ============================================================

def f14_bsss_001_debt_to_equity_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(debt, equity)).diff().diff()


def f14_bsss_002_log_debt_to_equity_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(debt, equity)
    return (_safe_log(r)).diff().diff()


def f14_bsss_003_debt_to_assets_d2(debt: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(debt, assets)).diff().diff()


def f14_bsss_004_net_debt_to_equity_d2(debt: pd.Series, cashneq: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(debt - cashneq, equity)).diff().diff()


def f14_bsss_005_net_debt_to_assets_d2(debt: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(debt - cashneq, assets)).diff().diff()


def f14_bsss_006_debt_to_ebitda_d2(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    return (_safe_div(debt, ebitda)).diff().diff()


def f14_bsss_007_debt_to_ebit_d2(debt: pd.Series, ebit: pd.Series) -> pd.Series:
    return (_safe_div(debt, ebit)).diff().diff()


def f14_bsss_008_debt_to_cfo_d2(debt: pd.Series, ncfo: pd.Series) -> pd.Series:
    return (_safe_div(debt, ncfo)).diff().diff()


def f14_bsss_009_debt_to_fcf_d2(debt: pd.Series, fcf: pd.Series) -> pd.Series:
    return (_safe_div(debt, fcf)).diff().diff()


def f14_bsss_010_debt_to_invcap_d2(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    return (_safe_div(debt, invcap)).diff().diff()


def f14_bsss_011_debt_to_total_capital_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(debt, debt + equity)).diff().diff()


def f14_bsss_012_log_debt_to_ebitda_d2(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    r = _safe_div(debt, ebitda)
    return (_safe_log(r)).diff().diff()


def f14_bsss_013_equity_to_assets_d2(equity: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(equity, assets)).diff().diff()


def f14_bsss_014_liabilities_to_assets_d2(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(liabilities, assets)).diff().diff()


def f14_bsss_015_liabilities_to_equity_d2(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(liabilities, equity)).diff().diff()


def f14_bsss_016_debtc_share_of_total_debt_d2(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(debtc, debt)).diff().diff()


def f14_bsss_017_debtnc_share_of_total_debt_d2(debtnc: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(debtnc, debt)).diff().diff()


def f14_bsss_018_debtc_to_cashneq_d2(debtc: pd.Series, cashneq: pd.Series) -> pd.Series:
    return (_safe_div(debtc, cashneq)).diff().diff()


def f14_bsss_019_debtc_to_cfo_d2(debtc: pd.Series, ncfo: pd.Series) -> pd.Series:
    return (_safe_div(debtc, ncfo)).diff().diff()


def f14_bsss_020_debtc_to_fcf_d2(debtc: pd.Series, fcf: pd.Series) -> pd.Series:
    return (_safe_div(debtc, fcf)).diff().diff()


def f14_bsss_021_debtc_minus_cashneq_to_assets_d2(debtc: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(debtc - cashneq, assets)).diff().diff()


def f14_bsss_022_debtc_to_assetsc_d2(debtc: pd.Series, assetsc: pd.Series) -> pd.Series:
    return (_safe_div(debtc, assetsc)).diff().diff()


def f14_bsss_023_current_ratio_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (_safe_div(assetsc, liabilitiesc)).diff().diff()


def f14_bsss_024_quick_ratio_d2(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (_safe_div(assetsc - inventory, liabilitiesc)).diff().diff()


def f14_bsss_025_cash_ratio_d2(cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, liabilitiesc)).diff().diff()


def f14_bsss_026_defensive_interval_days_d2(cashneq: pd.Series, receivables: pd.Series, opex: pd.Series) -> pd.Series:
    daily_opex = _safe_div(opex, 90.0)
    return (_safe_div(cashneq + receivables, daily_opex)).diff().diff()


def f14_bsss_027_current_ratio_ex_cash_d2(assetsc: pd.Series, cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (_safe_div(assetsc - cashneq, liabilitiesc)).diff().diff()


def f14_bsss_028_net_current_to_assets_d2(assetsc: pd.Series, liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(assetsc - liabilitiesc, assets)).diff().diff()


def f14_bsss_029_cashneq_to_liabilitiesc_d2(cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, liabilitiesc)).diff().diff()


def f14_bsss_030_cashneq_to_total_liabilities_d2(cashneq: pd.Series, liabilities: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, liabilities)).diff().diff()


def f14_bsss_031_cashneq_to_total_debt_d2(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, debt)).diff().diff()


def f14_bsss_032_cashneq_to_assets_d2(cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, assets)).diff().diff()


def f14_bsss_033_cashneq_to_assetsc_d2(cashneq: pd.Series, assetsc: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, assetsc)).diff().diff()


def f14_bsss_034_liabilitiesc_to_assetsc_d2(liabilitiesc: pd.Series, assetsc: pd.Series) -> pd.Series:
    return (_safe_div(liabilitiesc, assetsc)).diff().diff()


def f14_bsss_035_quick_ex_receivables_d2(cashneq: pd.Series, investments: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return (_safe_div(cashneq + investments, liabilitiesc)).diff().diff()


def f14_bsss_036_cashneq_to_equity_d2(cashneq: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, equity)).diff().diff()


def f14_bsss_037_cashneq_minus_debt_to_assets_d2(cashneq: pd.Series, debt: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(cashneq - debt, assets)).diff().diff()


def f14_bsss_038_net_cash_position_d2(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    return (cashneq - debt).diff().diff()


def f14_bsss_039_cash_runway_quarters_cfo_d2(cashneq: pd.Series, ncfo: pd.Series) -> pd.Series:
    burn = (-ncfo).where(ncfo < 0, np.nan)
    return (_safe_div(cashneq, burn)).diff().diff()


def f14_bsss_040_cash_runway_capex_burn_d2(cashneq: pd.Series, capex: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, capex.abs())).diff().diff()


def f14_bsss_041_cash_runway_fcf_burn_d2(cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    burn = (-fcf).where(fcf < 0, np.nan)
    return (_safe_div(cashneq, burn)).diff().diff()


def f14_bsss_042_cash_to_total_capital_d2(cashneq: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, debt + equity)).diff().diff()


def f14_bsss_043_cashneq_to_opex_d2(cashneq: pd.Series, opex: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, opex)).diff().diff()


def f14_bsss_044_cashneq_growth_yoy_d2(cashneq: pd.Series) -> pd.Series:
    return (_yoy_pct(cashneq, YDAYS)).diff().diff()


def f14_bsss_045_cashneq_minus_debtc_to_assets_d2(cashneq: pd.Series, debtc: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(cashneq - debtc, assets)).diff().diff()


def f14_bsss_046_cashneq_change_1y_to_assets_d2(cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(cashneq - cashneq.shift(YDAYS), assets)).diff().diff()


def f14_bsss_047_cashneq_share_of_assetsc_d2(cashneq: pd.Series, assetsc: pd.Series) -> pd.Series:
    return (_safe_div(cashneq, assetsc)).diff().diff()


def f14_bsss_048_cash_burn_intensity_d2(cashneq: pd.Series, ncfo: pd.Series) -> pd.Series:
    burn = (-ncfo).where(ncfo < 0, 0.0)
    return (_safe_div(burn, cashneq)).diff().diff()


def f14_bsss_049_wc_to_assets_d2(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital, assets)).diff().diff()


def f14_bsss_050_wc_to_revenue_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital, revenue)).diff().diff()


def f14_bsss_051_wc_to_equity_d2(workingcapital: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital, equity)).diff().diff()


def f14_bsss_052_wc_growth_yoy_assets_norm_d2(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital - workingcapital.shift(YDAYS), assets)).diff().diff()


def f14_bsss_053_wc_zscore_504d_d2(workingcapital: pd.Series) -> pd.Series:
    return (_rolling_zscore(workingcapital, 504)).diff().diff()


def f14_bsss_054_accruals_to_assets_d2(assets: pd.Series, ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    return (_safe_div(netinc - ncfo, assets)).diff().diff()


def f14_bsss_055_op_accruals_change_norm_d2(assetsc: pd.Series, cashneq: pd.Series, liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    op_wc = assetsc - cashneq - liabilitiesc
    return (_safe_div(op_wc - op_wc.shift(YDAYS), assets)).diff().diff()


def f14_bsss_056_wc_ex_cash_to_revenue_d2(workingcapital: pd.Series, cashneq: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital - cashneq, revenue)).diff().diff()


def f14_bsss_057_wc_ex_inventory_to_revenue_d2(workingcapital: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital - inventory, revenue)).diff().diff()


def f14_bsss_058_wc_to_capex_d2(workingcapital: pd.Series, capex: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital, capex.abs())).diff().diff()


def f14_bsss_059_wc_velocity_d2(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    return (_safe_div(revenue, workingcapital)).diff().diff()


def f14_bsss_060_negative_wc_flag_d2(workingcapital: pd.Series) -> pd.Series:
    out = (workingcapital < 0).astype(float)
    return (out.where(workingcapital.notna(), np.nan)).diff().diff()


def f14_bsss_061_dso_days_outstanding_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(receivables * 91.25, revenue)).diff().diff()


def f14_bsss_062_dso_zscore_504d_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    dso = _safe_div(receivables * 91.25, revenue)
    return (_rolling_zscore(dso, 504)).diff().diff()


def f14_bsss_063_ar_to_revenue_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(receivables, revenue)).diff().diff()


def f14_bsss_064_ar_growth_minus_rev_growth_yoy_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    ar_g = _yoy_pct(receivables, YDAYS)
    rev_g = _yoy_pct(revenue, YDAYS)
    return (ar_g - rev_g).diff().diff()


def f14_bsss_065_ar_to_assets_d2(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(receivables, assets)).diff().diff()


def f14_bsss_066_dio_inventory_days_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(inventory * 91.25, cor)).diff().diff()


def f14_bsss_067_inventory_to_revenue_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(inventory, revenue)).diff().diff()


def f14_bsss_068_inventory_to_assets_d2(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(inventory, assets)).diff().diff()


def f14_bsss_069_inv_growth_minus_rev_growth_yoy_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    inv_g = _yoy_pct(inventory, YDAYS)
    rev_g = _yoy_pct(revenue, YDAYS)
    return (inv_g - rev_g).diff().diff()


def f14_bsss_070_dpo_payables_days_d2(payables: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(payables * 91.25, cor)).diff().diff()


def f14_bsss_071_payables_to_revenue_d2(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(payables, revenue)).diff().diff()


def f14_bsss_072_payables_to_cor_d2(payables: pd.Series, cor: pd.Series) -> pd.Series:
    return (_safe_div(payables, cor)).diff().diff()


def f14_bsss_073_ccc_dso_plus_dio_minus_dpo_d2(receivables: pd.Series, inventory: pd.Series, payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    dso = _safe_div(receivables * 91.25, revenue)
    dio = _safe_div(inventory * 91.25, cor)
    dpo = _safe_div(payables * 91.25, cor)
    return (dso + dio - dpo).diff().diff()


def f14_bsss_074_deferredrev_to_revenue_d2(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(deferredrev, revenue)).diff().diff()


def f14_bsss_075_deposits_to_liabilities_d2(deposits: pd.Series, liabilities: pd.Series) -> pd.Series:
    return (_safe_div(deposits, liabilities)).diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

BALANCE_SHEET_STRESS_SNAPSHOT_D2_REGISTRY_001_075 = {
    "f14_bsss_001_debt_to_equity_d2": {"inputs": ["debt", "equity"], "func": f14_bsss_001_debt_to_equity_d2},
    "f14_bsss_002_log_debt_to_equity_d2": {"inputs": ["debt", "equity"], "func": f14_bsss_002_log_debt_to_equity_d2},
    "f14_bsss_003_debt_to_assets_d2": {"inputs": ["debt", "assets"], "func": f14_bsss_003_debt_to_assets_d2},
    "f14_bsss_004_net_debt_to_equity_d2": {"inputs": ["debt", "cashneq", "equity"], "func": f14_bsss_004_net_debt_to_equity_d2},
    "f14_bsss_005_net_debt_to_assets_d2": {"inputs": ["debt", "cashneq", "assets"], "func": f14_bsss_005_net_debt_to_assets_d2},
    "f14_bsss_006_debt_to_ebitda_d2": {"inputs": ["debt", "ebitda"], "func": f14_bsss_006_debt_to_ebitda_d2},
    "f14_bsss_007_debt_to_ebit_d2": {"inputs": ["debt", "ebit"], "func": f14_bsss_007_debt_to_ebit_d2},
    "f14_bsss_008_debt_to_cfo_d2": {"inputs": ["debt", "ncfo"], "func": f14_bsss_008_debt_to_cfo_d2},
    "f14_bsss_009_debt_to_fcf_d2": {"inputs": ["debt", "fcf"], "func": f14_bsss_009_debt_to_fcf_d2},
    "f14_bsss_010_debt_to_invcap_d2": {"inputs": ["debt", "invcap"], "func": f14_bsss_010_debt_to_invcap_d2},
    "f14_bsss_011_debt_to_total_capital_d2": {"inputs": ["debt", "equity"], "func": f14_bsss_011_debt_to_total_capital_d2},
    "f14_bsss_012_log_debt_to_ebitda_d2": {"inputs": ["debt", "ebitda"], "func": f14_bsss_012_log_debt_to_ebitda_d2},
    "f14_bsss_013_equity_to_assets_d2": {"inputs": ["equity", "assets"], "func": f14_bsss_013_equity_to_assets_d2},
    "f14_bsss_014_liabilities_to_assets_d2": {"inputs": ["liabilities", "assets"], "func": f14_bsss_014_liabilities_to_assets_d2},
    "f14_bsss_015_liabilities_to_equity_d2": {"inputs": ["liabilities", "equity"], "func": f14_bsss_015_liabilities_to_equity_d2},
    "f14_bsss_016_debtc_share_of_total_debt_d2": {"inputs": ["debtc", "debt"], "func": f14_bsss_016_debtc_share_of_total_debt_d2},
    "f14_bsss_017_debtnc_share_of_total_debt_d2": {"inputs": ["debtnc", "debt"], "func": f14_bsss_017_debtnc_share_of_total_debt_d2},
    "f14_bsss_018_debtc_to_cashneq_d2": {"inputs": ["debtc", "cashneq"], "func": f14_bsss_018_debtc_to_cashneq_d2},
    "f14_bsss_019_debtc_to_cfo_d2": {"inputs": ["debtc", "ncfo"], "func": f14_bsss_019_debtc_to_cfo_d2},
    "f14_bsss_020_debtc_to_fcf_d2": {"inputs": ["debtc", "fcf"], "func": f14_bsss_020_debtc_to_fcf_d2},
    "f14_bsss_021_debtc_minus_cashneq_to_assets_d2": {"inputs": ["debtc", "cashneq", "assets"], "func": f14_bsss_021_debtc_minus_cashneq_to_assets_d2},
    "f14_bsss_022_debtc_to_assetsc_d2": {"inputs": ["debtc", "assetsc"], "func": f14_bsss_022_debtc_to_assetsc_d2},
    "f14_bsss_023_current_ratio_d2": {"inputs": ["assetsc", "liabilitiesc"], "func": f14_bsss_023_current_ratio_d2},
    "f14_bsss_024_quick_ratio_d2": {"inputs": ["assetsc", "inventory", "liabilitiesc"], "func": f14_bsss_024_quick_ratio_d2},
    "f14_bsss_025_cash_ratio_d2": {"inputs": ["cashneq", "liabilitiesc"], "func": f14_bsss_025_cash_ratio_d2},
    "f14_bsss_026_defensive_interval_days_d2": {"inputs": ["cashneq", "receivables", "opex"], "func": f14_bsss_026_defensive_interval_days_d2},
    "f14_bsss_027_current_ratio_ex_cash_d2": {"inputs": ["assetsc", "cashneq", "liabilitiesc"], "func": f14_bsss_027_current_ratio_ex_cash_d2},
    "f14_bsss_028_net_current_to_assets_d2": {"inputs": ["assetsc", "liabilitiesc", "assets"], "func": f14_bsss_028_net_current_to_assets_d2},
    "f14_bsss_029_cashneq_to_liabilitiesc_d2": {"inputs": ["cashneq", "liabilitiesc"], "func": f14_bsss_029_cashneq_to_liabilitiesc_d2},
    "f14_bsss_030_cashneq_to_total_liabilities_d2": {"inputs": ["cashneq", "liabilities"], "func": f14_bsss_030_cashneq_to_total_liabilities_d2},
    "f14_bsss_031_cashneq_to_total_debt_d2": {"inputs": ["cashneq", "debt"], "func": f14_bsss_031_cashneq_to_total_debt_d2},
    "f14_bsss_032_cashneq_to_assets_d2": {"inputs": ["cashneq", "assets"], "func": f14_bsss_032_cashneq_to_assets_d2},
    "f14_bsss_033_cashneq_to_assetsc_d2": {"inputs": ["cashneq", "assetsc"], "func": f14_bsss_033_cashneq_to_assetsc_d2},
    "f14_bsss_034_liabilitiesc_to_assetsc_d2": {"inputs": ["liabilitiesc", "assetsc"], "func": f14_bsss_034_liabilitiesc_to_assetsc_d2},
    "f14_bsss_035_quick_ex_receivables_d2": {"inputs": ["cashneq", "investments", "liabilitiesc"], "func": f14_bsss_035_quick_ex_receivables_d2},
    "f14_bsss_036_cashneq_to_equity_d2": {"inputs": ["cashneq", "equity"], "func": f14_bsss_036_cashneq_to_equity_d2},
    "f14_bsss_037_cashneq_minus_debt_to_assets_d2": {"inputs": ["cashneq", "debt", "assets"], "func": f14_bsss_037_cashneq_minus_debt_to_assets_d2},
    "f14_bsss_038_net_cash_position_d2": {"inputs": ["cashneq", "debt"], "func": f14_bsss_038_net_cash_position_d2},
    "f14_bsss_039_cash_runway_quarters_cfo_d2": {"inputs": ["cashneq", "ncfo"], "func": f14_bsss_039_cash_runway_quarters_cfo_d2},
    "f14_bsss_040_cash_runway_capex_burn_d2": {"inputs": ["cashneq", "capex"], "func": f14_bsss_040_cash_runway_capex_burn_d2},
    "f14_bsss_041_cash_runway_fcf_burn_d2": {"inputs": ["cashneq", "fcf"], "func": f14_bsss_041_cash_runway_fcf_burn_d2},
    "f14_bsss_042_cash_to_total_capital_d2": {"inputs": ["cashneq", "debt", "equity"], "func": f14_bsss_042_cash_to_total_capital_d2},
    "f14_bsss_043_cashneq_to_opex_d2": {"inputs": ["cashneq", "opex"], "func": f14_bsss_043_cashneq_to_opex_d2},
    "f14_bsss_044_cashneq_growth_yoy_d2": {"inputs": ["cashneq"], "func": f14_bsss_044_cashneq_growth_yoy_d2},
    "f14_bsss_045_cashneq_minus_debtc_to_assets_d2": {"inputs": ["cashneq", "debtc", "assets"], "func": f14_bsss_045_cashneq_minus_debtc_to_assets_d2},
    "f14_bsss_046_cashneq_change_1y_to_assets_d2": {"inputs": ["cashneq", "assets"], "func": f14_bsss_046_cashneq_change_1y_to_assets_d2},
    "f14_bsss_047_cashneq_share_of_assetsc_d2": {"inputs": ["cashneq", "assetsc"], "func": f14_bsss_047_cashneq_share_of_assetsc_d2},
    "f14_bsss_048_cash_burn_intensity_d2": {"inputs": ["cashneq", "ncfo"], "func": f14_bsss_048_cash_burn_intensity_d2},
    "f14_bsss_049_wc_to_assets_d2": {"inputs": ["workingcapital", "assets"], "func": f14_bsss_049_wc_to_assets_d2},
    "f14_bsss_050_wc_to_revenue_d2": {"inputs": ["workingcapital", "revenue"], "func": f14_bsss_050_wc_to_revenue_d2},
    "f14_bsss_051_wc_to_equity_d2": {"inputs": ["workingcapital", "equity"], "func": f14_bsss_051_wc_to_equity_d2},
    "f14_bsss_052_wc_growth_yoy_assets_norm_d2": {"inputs": ["workingcapital", "assets"], "func": f14_bsss_052_wc_growth_yoy_assets_norm_d2},
    "f14_bsss_053_wc_zscore_504d_d2": {"inputs": ["workingcapital"], "func": f14_bsss_053_wc_zscore_504d_d2},
    "f14_bsss_054_accruals_to_assets_d2": {"inputs": ["assets", "ncfo", "netinc"], "func": f14_bsss_054_accruals_to_assets_d2},
    "f14_bsss_055_op_accruals_change_norm_d2": {"inputs": ["assetsc", "cashneq", "liabilitiesc", "assets"], "func": f14_bsss_055_op_accruals_change_norm_d2},
    "f14_bsss_056_wc_ex_cash_to_revenue_d2": {"inputs": ["workingcapital", "cashneq", "revenue"], "func": f14_bsss_056_wc_ex_cash_to_revenue_d2},
    "f14_bsss_057_wc_ex_inventory_to_revenue_d2": {"inputs": ["workingcapital", "inventory", "revenue"], "func": f14_bsss_057_wc_ex_inventory_to_revenue_d2},
    "f14_bsss_058_wc_to_capex_d2": {"inputs": ["workingcapital", "capex"], "func": f14_bsss_058_wc_to_capex_d2},
    "f14_bsss_059_wc_velocity_d2": {"inputs": ["revenue", "workingcapital"], "func": f14_bsss_059_wc_velocity_d2},
    "f14_bsss_060_negative_wc_flag_d2": {"inputs": ["workingcapital"], "func": f14_bsss_060_negative_wc_flag_d2},
    "f14_bsss_061_dso_days_outstanding_d2": {"inputs": ["receivables", "revenue"], "func": f14_bsss_061_dso_days_outstanding_d2},
    "f14_bsss_062_dso_zscore_504d_d2": {"inputs": ["receivables", "revenue"], "func": f14_bsss_062_dso_zscore_504d_d2},
    "f14_bsss_063_ar_to_revenue_d2": {"inputs": ["receivables", "revenue"], "func": f14_bsss_063_ar_to_revenue_d2},
    "f14_bsss_064_ar_growth_minus_rev_growth_yoy_d2": {"inputs": ["receivables", "revenue"], "func": f14_bsss_064_ar_growth_minus_rev_growth_yoy_d2},
    "f14_bsss_065_ar_to_assets_d2": {"inputs": ["receivables", "assets"], "func": f14_bsss_065_ar_to_assets_d2},
    "f14_bsss_066_dio_inventory_days_d2": {"inputs": ["inventory", "cor"], "func": f14_bsss_066_dio_inventory_days_d2},
    "f14_bsss_067_inventory_to_revenue_d2": {"inputs": ["inventory", "revenue"], "func": f14_bsss_067_inventory_to_revenue_d2},
    "f14_bsss_068_inventory_to_assets_d2": {"inputs": ["inventory", "assets"], "func": f14_bsss_068_inventory_to_assets_d2},
    "f14_bsss_069_inv_growth_minus_rev_growth_yoy_d2": {"inputs": ["inventory", "revenue"], "func": f14_bsss_069_inv_growth_minus_rev_growth_yoy_d2},
    "f14_bsss_070_dpo_payables_days_d2": {"inputs": ["payables", "cor"], "func": f14_bsss_070_dpo_payables_days_d2},
    "f14_bsss_071_payables_to_revenue_d2": {"inputs": ["payables", "revenue"], "func": f14_bsss_071_payables_to_revenue_d2},
    "f14_bsss_072_payables_to_cor_d2": {"inputs": ["payables", "cor"], "func": f14_bsss_072_payables_to_cor_d2},
    "f14_bsss_073_ccc_dso_plus_dio_minus_dpo_d2": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f14_bsss_073_ccc_dso_plus_dio_minus_dpo_d2},
    "f14_bsss_074_deferredrev_to_revenue_d2": {"inputs": ["deferredrev", "revenue"], "func": f14_bsss_074_deferredrev_to_revenue_d2},
    "f14_bsss_075_deposits_to_liabilities_d2": {"inputs": ["deposits", "liabilities"], "func": f14_bsss_075_deposits_to_liabilities_d2},
}
