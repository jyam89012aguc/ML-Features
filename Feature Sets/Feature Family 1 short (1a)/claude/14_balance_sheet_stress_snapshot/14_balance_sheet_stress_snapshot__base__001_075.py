"""balance_sheet_stress_snapshot base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct SF1 balance-sheet stress hypotheses (continued in __base__076_150.py for 150 total).
Inputs: SF1 quarterly fundamentals binder-forward-filled to daily index.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
Missing data => NaN. No zero-fill, no forward-fill across gaps unless that is the hypothesis.
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
#                    FEATURES 001-075
# ============================================================

# ---------- Leverage levels (001-015) ----------

def f14_bsss_001_debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Classic leverage: total debt / book equity."""
    return _safe_div(debt, equity)


def f14_bsss_002_log_debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Log of D/E to compress fat right tail of distressed names."""
    r = _safe_div(debt, equity)
    return _safe_log(r)


def f14_bsss_003_debt_to_assets(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Leverage relative to asset base — total D/A."""
    return _safe_div(debt, assets)


def f14_bsss_004_net_debt_to_equity(debt: pd.Series, cashneq: pd.Series, equity: pd.Series) -> pd.Series:
    """(debt - cash) / equity — net leverage."""
    return _safe_div(debt - cashneq, equity)


def f14_bsss_005_net_debt_to_assets(debt: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    """(debt - cash) / assets — net leverage on the asset base."""
    return _safe_div(debt - cashneq, assets)


def f14_bsss_006_debt_to_ebitda(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Years of EBITDA to repay total debt — cash-flow leverage."""
    return _safe_div(debt, ebitda)


def f14_bsss_007_debt_to_ebit(debt: pd.Series, ebit: pd.Series) -> pd.Series:
    """EBIT-based payback metric, ignoring D&A add-back."""
    return _safe_div(debt, ebit)


def f14_bsss_008_debt_to_cfo(debt: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Years of operating cash flow to repay debt."""
    return _safe_div(debt, ncfo)


def f14_bsss_009_debt_to_fcf(debt: pd.Series, fcf: pd.Series) -> pd.Series:
    """Years of free cash flow to retire debt — strictest payback measure."""
    return _safe_div(debt, fcf)


def f14_bsss_010_debt_to_invcap(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    """Debt share of invested capital."""
    return _safe_div(debt, invcap)


def f14_bsss_011_debt_to_total_capital(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D / (D + E) — leverage as fraction of total capital structure."""
    return _safe_div(debt, debt + equity)


def f14_bsss_012_log_debt_to_ebitda(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Log of debt/EBITDA — compress distress tails."""
    r = _safe_div(debt, ebitda)
    return _safe_log(r)


def f14_bsss_013_equity_to_assets(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Thinness of equity cushion against the asset base."""
    return _safe_div(equity, assets)


def f14_bsss_014_liabilities_to_assets(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Total liabilities share — broader than debt-only leverage."""
    return _safe_div(liabilities, assets)


def f14_bsss_015_liabilities_to_equity(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Total claim leverage including non-debt obligations."""
    return _safe_div(liabilities, equity)


# ---------- ST vs LT debt mix / maturity wall (016-022) ----------

def f14_bsss_016_debtc_share_of_total_debt(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Short-term portion of total debt — refinance risk weighting."""
    return _safe_div(debtc, debt)


def f14_bsss_017_debtnc_share_of_total_debt(debtnc: pd.Series, debt: pd.Series) -> pd.Series:
    """Long-term portion of total debt — duration profile."""
    return _safe_div(debtnc, debt)


def f14_bsss_018_debtc_to_cashneq(debtc: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Maturity-wall coverage — ST debt covered by cash on hand."""
    return _safe_div(debtc, cashneq)


def f14_bsss_019_debtc_to_cfo(debtc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """ST debt covered by operating cash flow."""
    return _safe_div(debtc, ncfo)


def f14_bsss_020_debtc_to_fcf(debtc: pd.Series, fcf: pd.Series) -> pd.Series:
    """ST debt covered by free cash flow — strictest refi check."""
    return _safe_div(debtc, fcf)


def f14_bsss_021_debtc_minus_cashneq_to_assets(debtc: pd.Series, cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    """Uncovered ST debt scaled by assets — funding-gap proxy."""
    return _safe_div(debtc - cashneq, assets)


def f14_bsss_022_debtc_to_assetsc(debtc: pd.Series, assetsc: pd.Series) -> pd.Series:
    """ST debt vs current assets — gross matched-funding ratio."""
    return _safe_div(debtc, assetsc)


# ---------- Liquidity (023-035) ----------

def f14_bsss_023_current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Classic current ratio."""
    return _safe_div(assetsc, liabilitiesc)


def f14_bsss_024_quick_ratio(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """(Current assets - inventory) / current liabilities."""
    return _safe_div(assetsc - inventory, liabilitiesc)


def f14_bsss_025_cash_ratio(cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash and equivalents / current liabilities."""
    return _safe_div(cashneq, liabilitiesc)


def f14_bsss_026_defensive_interval_days(cashneq: pd.Series, receivables: pd.Series, opex: pd.Series) -> pd.Series:
    """Days of opex covered by (cash + receivables) — quarterly opex annualized."""
    daily_opex = _safe_div(opex, 90.0)
    return _safe_div(cashneq + receivables, daily_opex)


def f14_bsss_027_current_ratio_ex_cash(assetsc: pd.Series, cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Liquidity excluding cash — operating-liquidity-only flavor."""
    return _safe_div(assetsc - cashneq, liabilitiesc)


def f14_bsss_028_net_current_to_assets(assetsc: pd.Series, liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    """(Current assets - current liabs) / total assets — net WC over assets."""
    return _safe_div(assetsc - liabilitiesc, assets)


def f14_bsss_029_cashneq_to_liabilitiesc(cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Same as cash ratio but kept distinct: alternate cash-coverage hypothesis."""
    return _safe_div(cashneq, liabilitiesc)


def f14_bsss_030_cashneq_to_total_liabilities(cashneq: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Cash against ALL liabilities (incl. long term)."""
    return _safe_div(cashneq, liabilities)


def f14_bsss_031_cashneq_to_total_debt(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Cash against total debt — net-debt seed."""
    return _safe_div(cashneq, debt)


def f14_bsss_032_cashneq_to_assets(cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    """Cash share of asset base — liquidity intensity."""
    return _safe_div(cashneq, assets)


def f14_bsss_033_cashneq_to_assetsc(cashneq: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Cash share of current assets — composition of short-term assets."""
    return _safe_div(cashneq, assetsc)


def f14_bsss_034_liabilitiesc_to_assetsc(liabilitiesc: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Current liabilities pressure vs current assets — inverse current ratio."""
    return _safe_div(liabilitiesc, assetsc)


def f14_bsss_035_quick_ex_receivables(cashneq: pd.Series, investments: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """(Cash + ST investments) / current liabs — strict liquid coverage."""
    return _safe_div(cashneq + investments, liabilitiesc)


# ---------- Cash positioning & runway (036-048) ----------

def f14_bsss_036_cashneq_to_equity(cashneq: pd.Series, equity: pd.Series) -> pd.Series:
    """Cash as fraction of book equity — quality-of-equity proxy."""
    return _safe_div(cashneq, equity)


def f14_bsss_037_cashneq_minus_debt_to_assets(cashneq: pd.Series, debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Net cash position scaled by assets — balance-sheet flexibility."""
    return _safe_div(cashneq - debt, assets)


def f14_bsss_038_net_cash_position(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Absolute net cash (cash minus debt) — raw flexibility level."""
    return cashneq - debt


def f14_bsss_039_cash_runway_quarters_cfo(cashneq: pd.Series, ncfo: pd.Series) -> pd.Series:
    """If CFO is negative, cash / |CFO per quarter|; if positive, NaN."""
    burn = (-ncfo).where(ncfo < 0, np.nan)
    return _safe_div(cashneq, burn)


def f14_bsss_040_cash_runway_capex_burn(cashneq: pd.Series, capex: pd.Series) -> pd.Series:
    """Cash / quarterly capex outflow (capex stored negative or positive — use abs)."""
    return _safe_div(cashneq, capex.abs())


def f14_bsss_041_cash_runway_fcf_burn(cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    """If FCF is negative, cash / |FCF|; else NaN — pure-burn runway."""
    burn = (-fcf).where(fcf < 0, np.nan)
    return _safe_div(cashneq, burn)


def f14_bsss_042_cash_to_total_capital(cashneq: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Cash / (debt + equity) — share of total capital sitting in cash."""
    return _safe_div(cashneq, debt + equity)


def f14_bsss_043_cashneq_to_opex(cashneq: pd.Series, opex: pd.Series) -> pd.Series:
    """Quarters of operating expense covered by cash."""
    return _safe_div(cashneq, opex)


def f14_bsss_044_cashneq_growth_yoy(cashneq: pd.Series) -> pd.Series:
    """Year-on-year cash level pct change — survival-cash trend."""
    return _yoy_pct(cashneq, YDAYS)


def f14_bsss_045_cashneq_minus_debtc_to_assets(cashneq: pd.Series, debtc: pd.Series, assets: pd.Series) -> pd.Series:
    """Excess cash over near-term debt scaled by assets."""
    return _safe_div(cashneq - debtc, assets)


def f14_bsss_046_cashneq_change_1y_to_assets(cashneq: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in cash level normalized by assets."""
    return _safe_div(cashneq - cashneq.shift(YDAYS), assets)


def f14_bsss_047_cashneq_share_of_assetsc(cashneq: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Composition: how much of working liquidity is pure cash."""
    return _safe_div(cashneq, assetsc)


def f14_bsss_048_cash_burn_intensity(cashneq: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Reciprocal of CFO-runway: |CFO|/cash when CFO < 0; else 0."""
    burn = (-ncfo).where(ncfo < 0, 0.0)
    return _safe_div(burn, cashneq)


# ---------- Working capital concepts (049-060) ----------

def f14_bsss_049_wc_to_assets(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman X1-style scaling of working capital."""
    return _safe_div(workingcapital, assets)


def f14_bsss_050_wc_to_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """WC intensity per revenue dollar."""
    return _safe_div(workingcapital, revenue)


def f14_bsss_051_wc_to_equity(workingcapital: pd.Series, equity: pd.Series) -> pd.Series:
    """WC as fraction of book equity."""
    return _safe_div(workingcapital, equity)


def f14_bsss_052_wc_growth_yoy_assets_norm(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in WC scaled by assets — capital-tying-up signal."""
    return _safe_div(workingcapital - workingcapital.shift(YDAYS), assets)


def f14_bsss_053_wc_zscore_504d(workingcapital: pd.Series) -> pd.Series:
    """Two-year rolling z-score of WC level."""
    return _rolling_zscore(workingcapital, 504)


def f14_bsss_054_accruals_to_assets(assets: pd.Series, ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Sloan accruals proxy: (NI - CFO) / assets — earnings quality stress."""
    return _safe_div(netinc - ncfo, assets)


def f14_bsss_055_op_accruals_change_norm(assetsc: pd.Series, cashneq: pd.Series, liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    """Balance-sheet accruals YoY: change in (CA-cash-CL) / assets."""
    op_wc = assetsc - cashneq - liabilitiesc
    return _safe_div(op_wc - op_wc.shift(YDAYS), assets)


def f14_bsss_056_wc_ex_cash_to_revenue(workingcapital: pd.Series, cashneq: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating WC (ex cash) per revenue dollar."""
    return _safe_div(workingcapital - cashneq, revenue)


def f14_bsss_057_wc_ex_inventory_to_revenue(workingcapital: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """WC excluding inventory drag, scaled by revenue."""
    return _safe_div(workingcapital - inventory, revenue)


def f14_bsss_058_wc_to_capex(workingcapital: pd.Series, capex: pd.Series) -> pd.Series:
    """WC coverage of recurring capex outflow."""
    return _safe_div(workingcapital, capex.abs())


def f14_bsss_059_wc_velocity(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Revenue per WC dollar — high velocity ≈ thin capital base."""
    return _safe_div(revenue, workingcapital)


def f14_bsss_060_negative_wc_flag(workingcapital: pd.Series) -> pd.Series:
    """Float flag: 1 if WC<0 else 0; NaN where input NaN."""
    out = (workingcapital < 0).astype(float)
    return out.where(workingcapital.notna(), np.nan)


# ---------- CCC components (061-075) ----------

def f14_bsss_061_dso_days_outstanding(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Days sales outstanding using quarterly revenue (annualized via *365/4)."""
    return _safe_div(receivables * 91.25, revenue)


def f14_bsss_062_dso_zscore_504d(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of DSO over trailing 504 trading days."""
    dso = _safe_div(receivables * 91.25, revenue)
    return _rolling_zscore(dso, 504)


def f14_bsss_063_ar_to_revenue(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Receivables intensity — channel-stuffing red flag when rising."""
    return _safe_div(receivables, revenue)


def f14_bsss_064_ar_growth_minus_rev_growth_yoy(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """AR-growth minus revenue-growth YoY — Beneish-DSRI flavor difference."""
    ar_g = _yoy_pct(receivables, YDAYS)
    rev_g = _yoy_pct(revenue, YDAYS)
    return ar_g - rev_g


def f14_bsss_065_ar_to_assets(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Receivables share of total assets."""
    return _safe_div(receivables, assets)


def f14_bsss_066_dio_inventory_days(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Days inventory outstanding using cost of revenue."""
    return _safe_div(inventory * 91.25, cor)


def f14_bsss_067_inventory_to_revenue(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory intensity — pile-up signal for hardware/retail."""
    return _safe_div(inventory, revenue)


def f14_bsss_068_inventory_to_assets(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """Inventory share of asset base."""
    return _safe_div(inventory, assets)


def f14_bsss_069_inv_growth_minus_rev_growth_yoy(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory growth in excess of revenue growth — demand-mismatch flag."""
    inv_g = _yoy_pct(inventory, YDAYS)
    rev_g = _yoy_pct(revenue, YDAYS)
    return inv_g - rev_g


def f14_bsss_070_dpo_payables_days(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """Days payables outstanding — stretching suppliers signal."""
    return _safe_div(payables * 91.25, cor)


def f14_bsss_071_payables_to_revenue(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trade payables intensity vs revenue."""
    return _safe_div(payables, revenue)


def f14_bsss_072_payables_to_cor(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """Payables relative to cost base — supplier-funding share."""
    return _safe_div(payables, cor)


def f14_bsss_073_ccc_dso_plus_dio_minus_dpo(receivables: pd.Series, inventory: pd.Series, payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Cash conversion cycle days = DSO + DIO - DPO."""
    dso = _safe_div(receivables * 91.25, revenue)
    dio = _safe_div(inventory * 91.25, cor)
    dpo = _safe_div(payables * 91.25, cor)
    return dso + dio - dpo


def f14_bsss_074_deferredrev_to_revenue(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """Deferred revenue intensity — quality of backlog liability."""
    return _safe_div(deferredrev, revenue)


def f14_bsss_075_deposits_to_liabilities(deposits: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Customer/banking deposits share of total liabilities."""
    return _safe_div(deposits, liabilities)


# ============================================================
#                        REGISTRY
# ============================================================

BALANCE_SHEET_STRESS_SNAPSHOT_BASE_REGISTRY_001_075 = {
    "f14_bsss_001_debt_to_equity": {"inputs": ["debt", "equity"], "func": f14_bsss_001_debt_to_equity},
    "f14_bsss_002_log_debt_to_equity": {"inputs": ["debt", "equity"], "func": f14_bsss_002_log_debt_to_equity},
    "f14_bsss_003_debt_to_assets": {"inputs": ["debt", "assets"], "func": f14_bsss_003_debt_to_assets},
    "f14_bsss_004_net_debt_to_equity": {"inputs": ["debt", "cashneq", "equity"], "func": f14_bsss_004_net_debt_to_equity},
    "f14_bsss_005_net_debt_to_assets": {"inputs": ["debt", "cashneq", "assets"], "func": f14_bsss_005_net_debt_to_assets},
    "f14_bsss_006_debt_to_ebitda": {"inputs": ["debt", "ebitda"], "func": f14_bsss_006_debt_to_ebitda},
    "f14_bsss_007_debt_to_ebit": {"inputs": ["debt", "ebit"], "func": f14_bsss_007_debt_to_ebit},
    "f14_bsss_008_debt_to_cfo": {"inputs": ["debt", "ncfo"], "func": f14_bsss_008_debt_to_cfo},
    "f14_bsss_009_debt_to_fcf": {"inputs": ["debt", "fcf"], "func": f14_bsss_009_debt_to_fcf},
    "f14_bsss_010_debt_to_invcap": {"inputs": ["debt", "invcap"], "func": f14_bsss_010_debt_to_invcap},
    "f14_bsss_011_debt_to_total_capital": {"inputs": ["debt", "equity"], "func": f14_bsss_011_debt_to_total_capital},
    "f14_bsss_012_log_debt_to_ebitda": {"inputs": ["debt", "ebitda"], "func": f14_bsss_012_log_debt_to_ebitda},
    "f14_bsss_013_equity_to_assets": {"inputs": ["equity", "assets"], "func": f14_bsss_013_equity_to_assets},
    "f14_bsss_014_liabilities_to_assets": {"inputs": ["liabilities", "assets"], "func": f14_bsss_014_liabilities_to_assets},
    "f14_bsss_015_liabilities_to_equity": {"inputs": ["liabilities", "equity"], "func": f14_bsss_015_liabilities_to_equity},
    "f14_bsss_016_debtc_share_of_total_debt": {"inputs": ["debtc", "debt"], "func": f14_bsss_016_debtc_share_of_total_debt},
    "f14_bsss_017_debtnc_share_of_total_debt": {"inputs": ["debtnc", "debt"], "func": f14_bsss_017_debtnc_share_of_total_debt},
    "f14_bsss_018_debtc_to_cashneq": {"inputs": ["debtc", "cashneq"], "func": f14_bsss_018_debtc_to_cashneq},
    "f14_bsss_019_debtc_to_cfo": {"inputs": ["debtc", "ncfo"], "func": f14_bsss_019_debtc_to_cfo},
    "f14_bsss_020_debtc_to_fcf": {"inputs": ["debtc", "fcf"], "func": f14_bsss_020_debtc_to_fcf},
    "f14_bsss_021_debtc_minus_cashneq_to_assets": {"inputs": ["debtc", "cashneq", "assets"], "func": f14_bsss_021_debtc_minus_cashneq_to_assets},
    "f14_bsss_022_debtc_to_assetsc": {"inputs": ["debtc", "assetsc"], "func": f14_bsss_022_debtc_to_assetsc},
    "f14_bsss_023_current_ratio": {"inputs": ["assetsc", "liabilitiesc"], "func": f14_bsss_023_current_ratio},
    "f14_bsss_024_quick_ratio": {"inputs": ["assetsc", "inventory", "liabilitiesc"], "func": f14_bsss_024_quick_ratio},
    "f14_bsss_025_cash_ratio": {"inputs": ["cashneq", "liabilitiesc"], "func": f14_bsss_025_cash_ratio},
    "f14_bsss_026_defensive_interval_days": {"inputs": ["cashneq", "receivables", "opex"], "func": f14_bsss_026_defensive_interval_days},
    "f14_bsss_027_current_ratio_ex_cash": {"inputs": ["assetsc", "cashneq", "liabilitiesc"], "func": f14_bsss_027_current_ratio_ex_cash},
    "f14_bsss_028_net_current_to_assets": {"inputs": ["assetsc", "liabilitiesc", "assets"], "func": f14_bsss_028_net_current_to_assets},
    "f14_bsss_029_cashneq_to_liabilitiesc": {"inputs": ["cashneq", "liabilitiesc"], "func": f14_bsss_029_cashneq_to_liabilitiesc},
    "f14_bsss_030_cashneq_to_total_liabilities": {"inputs": ["cashneq", "liabilities"], "func": f14_bsss_030_cashneq_to_total_liabilities},
    "f14_bsss_031_cashneq_to_total_debt": {"inputs": ["cashneq", "debt"], "func": f14_bsss_031_cashneq_to_total_debt},
    "f14_bsss_032_cashneq_to_assets": {"inputs": ["cashneq", "assets"], "func": f14_bsss_032_cashneq_to_assets},
    "f14_bsss_033_cashneq_to_assetsc": {"inputs": ["cashneq", "assetsc"], "func": f14_bsss_033_cashneq_to_assetsc},
    "f14_bsss_034_liabilitiesc_to_assetsc": {"inputs": ["liabilitiesc", "assetsc"], "func": f14_bsss_034_liabilitiesc_to_assetsc},
    "f14_bsss_035_quick_ex_receivables": {"inputs": ["cashneq", "investments", "liabilitiesc"], "func": f14_bsss_035_quick_ex_receivables},
    "f14_bsss_036_cashneq_to_equity": {"inputs": ["cashneq", "equity"], "func": f14_bsss_036_cashneq_to_equity},
    "f14_bsss_037_cashneq_minus_debt_to_assets": {"inputs": ["cashneq", "debt", "assets"], "func": f14_bsss_037_cashneq_minus_debt_to_assets},
    "f14_bsss_038_net_cash_position": {"inputs": ["cashneq", "debt"], "func": f14_bsss_038_net_cash_position},
    "f14_bsss_039_cash_runway_quarters_cfo": {"inputs": ["cashneq", "ncfo"], "func": f14_bsss_039_cash_runway_quarters_cfo},
    "f14_bsss_040_cash_runway_capex_burn": {"inputs": ["cashneq", "capex"], "func": f14_bsss_040_cash_runway_capex_burn},
    "f14_bsss_041_cash_runway_fcf_burn": {"inputs": ["cashneq", "fcf"], "func": f14_bsss_041_cash_runway_fcf_burn},
    "f14_bsss_042_cash_to_total_capital": {"inputs": ["cashneq", "debt", "equity"], "func": f14_bsss_042_cash_to_total_capital},
    "f14_bsss_043_cashneq_to_opex": {"inputs": ["cashneq", "opex"], "func": f14_bsss_043_cashneq_to_opex},
    "f14_bsss_044_cashneq_growth_yoy": {"inputs": ["cashneq"], "func": f14_bsss_044_cashneq_growth_yoy},
    "f14_bsss_045_cashneq_minus_debtc_to_assets": {"inputs": ["cashneq", "debtc", "assets"], "func": f14_bsss_045_cashneq_minus_debtc_to_assets},
    "f14_bsss_046_cashneq_change_1y_to_assets": {"inputs": ["cashneq", "assets"], "func": f14_bsss_046_cashneq_change_1y_to_assets},
    "f14_bsss_047_cashneq_share_of_assetsc": {"inputs": ["cashneq", "assetsc"], "func": f14_bsss_047_cashneq_share_of_assetsc},
    "f14_bsss_048_cash_burn_intensity": {"inputs": ["cashneq", "ncfo"], "func": f14_bsss_048_cash_burn_intensity},
    "f14_bsss_049_wc_to_assets": {"inputs": ["workingcapital", "assets"], "func": f14_bsss_049_wc_to_assets},
    "f14_bsss_050_wc_to_revenue": {"inputs": ["workingcapital", "revenue"], "func": f14_bsss_050_wc_to_revenue},
    "f14_bsss_051_wc_to_equity": {"inputs": ["workingcapital", "equity"], "func": f14_bsss_051_wc_to_equity},
    "f14_bsss_052_wc_growth_yoy_assets_norm": {"inputs": ["workingcapital", "assets"], "func": f14_bsss_052_wc_growth_yoy_assets_norm},
    "f14_bsss_053_wc_zscore_504d": {"inputs": ["workingcapital"], "func": f14_bsss_053_wc_zscore_504d},
    "f14_bsss_054_accruals_to_assets": {"inputs": ["assets", "ncfo", "netinc"], "func": f14_bsss_054_accruals_to_assets},
    "f14_bsss_055_op_accruals_change_norm": {"inputs": ["assetsc", "cashneq", "liabilitiesc", "assets"], "func": f14_bsss_055_op_accruals_change_norm},
    "f14_bsss_056_wc_ex_cash_to_revenue": {"inputs": ["workingcapital", "cashneq", "revenue"], "func": f14_bsss_056_wc_ex_cash_to_revenue},
    "f14_bsss_057_wc_ex_inventory_to_revenue": {"inputs": ["workingcapital", "inventory", "revenue"], "func": f14_bsss_057_wc_ex_inventory_to_revenue},
    "f14_bsss_058_wc_to_capex": {"inputs": ["workingcapital", "capex"], "func": f14_bsss_058_wc_to_capex},
    "f14_bsss_059_wc_velocity": {"inputs": ["revenue", "workingcapital"], "func": f14_bsss_059_wc_velocity},
    "f14_bsss_060_negative_wc_flag": {"inputs": ["workingcapital"], "func": f14_bsss_060_negative_wc_flag},
    "f14_bsss_061_dso_days_outstanding": {"inputs": ["receivables", "revenue"], "func": f14_bsss_061_dso_days_outstanding},
    "f14_bsss_062_dso_zscore_504d": {"inputs": ["receivables", "revenue"], "func": f14_bsss_062_dso_zscore_504d},
    "f14_bsss_063_ar_to_revenue": {"inputs": ["receivables", "revenue"], "func": f14_bsss_063_ar_to_revenue},
    "f14_bsss_064_ar_growth_minus_rev_growth_yoy": {"inputs": ["receivables", "revenue"], "func": f14_bsss_064_ar_growth_minus_rev_growth_yoy},
    "f14_bsss_065_ar_to_assets": {"inputs": ["receivables", "assets"], "func": f14_bsss_065_ar_to_assets},
    "f14_bsss_066_dio_inventory_days": {"inputs": ["inventory", "cor"], "func": f14_bsss_066_dio_inventory_days},
    "f14_bsss_067_inventory_to_revenue": {"inputs": ["inventory", "revenue"], "func": f14_bsss_067_inventory_to_revenue},
    "f14_bsss_068_inventory_to_assets": {"inputs": ["inventory", "assets"], "func": f14_bsss_068_inventory_to_assets},
    "f14_bsss_069_inv_growth_minus_rev_growth_yoy": {"inputs": ["inventory", "revenue"], "func": f14_bsss_069_inv_growth_minus_rev_growth_yoy},
    "f14_bsss_070_dpo_payables_days": {"inputs": ["payables", "cor"], "func": f14_bsss_070_dpo_payables_days},
    "f14_bsss_071_payables_to_revenue": {"inputs": ["payables", "revenue"], "func": f14_bsss_071_payables_to_revenue},
    "f14_bsss_072_payables_to_cor": {"inputs": ["payables", "cor"], "func": f14_bsss_072_payables_to_cor},
    "f14_bsss_073_ccc_dso_plus_dio_minus_dpo": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f14_bsss_073_ccc_dso_plus_dio_minus_dpo},
    "f14_bsss_074_deferredrev_to_revenue": {"inputs": ["deferredrev", "revenue"], "func": f14_bsss_074_deferredrev_to_revenue},
    "f14_bsss_075_deposits_to_liabilities": {"inputs": ["deposits", "liabilities"], "func": f14_bsss_075_deposits_to_liabilities},
}
