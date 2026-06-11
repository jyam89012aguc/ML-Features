"""balance_sheet_stress_snapshot base features 076-150 — continuation of 001-075.

Covers intangibles/tangible book, equity composition, coverage & solvency,
Altman/Beneish/Ohlson distress models, negative-flag composites.
PIT-clean SF1 quarterly inputs forward-filled to daily index.
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
#                    FEATURES 076-150
# ============================================================

# ---------- Intangibles / tangible book (076-090) ----------

def f14_bsss_076_intangibles_to_assets(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Goodwill+intangibles share of asset base — bloat exposure."""
    return _safe_div(intangibles, assets)


def f14_bsss_077_intangibles_to_equity(intangibles: pd.Series, equity: pd.Series) -> pd.Series:
    """How much of book equity is non-tangible — write-down vulnerability."""
    return _safe_div(intangibles, equity)


def f14_bsss_078_intangibles_to_tangibles(intangibles: pd.Series, tangibles: pd.Series) -> pd.Series:
    """Intangible vs tangible asset balance — quality of the asset mix."""
    return _safe_div(intangibles, tangibles)


def f14_bsss_079_tangibles_to_assets(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Tangible asset share — collateral quality."""
    return _safe_div(tangibles, assets)


def f14_bsss_080_tangible_equity_ratio(equity: pd.Series, intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """(Equity - intangibles) / assets — tangible equity cushion."""
    return _safe_div(equity - intangibles, assets)


def f14_bsss_081_tangible_book_to_total_book(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Tangible book / total book — quality of book equity."""
    return _safe_div(equity - intangibles, equity)


def f14_bsss_082_neg_tangible_equity_flag(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """1 if equity - intangibles < 0 else 0; NaN where inputs NaN."""
    te = equity - intangibles
    out = (te < 0).astype(float)
    return out.where(te.notna(), np.nan)


def f14_bsss_083_intangibles_growth_yoy(intangibles: pd.Series) -> pd.Series:
    """YoY pct change in intangibles — acquisition/goodwill build-up."""
    return _yoy_pct(intangibles, YDAYS)


def f14_bsss_084_intangibles_to_invcap(intangibles: pd.Series, invcap: pd.Series) -> pd.Series:
    """Intangible share of invested capital."""
    return _safe_div(intangibles, invcap)


def f14_bsss_085_intangibles_minus_equity_impairment_proxy(intangibles: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    """(Intangibles - equity) / assets — > 0 means write-down would wipe equity."""
    return _safe_div(intangibles - equity, assets)


def f14_bsss_086_asset_quality_index(assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Beneish-style AQI numerator: (assets - CA - PPE - intangibles)/assets — opaque assets share."""
    return _safe_div(assets - assetsc - ppnenet - intangibles, assets)


def f14_bsss_087_ppnenet_to_assets(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """Net PP&E share of assets — capital-intensity proxy."""
    return _safe_div(ppnenet, assets)


def f14_bsss_088_investments_to_assets(investments: pd.Series, assets: pd.Series) -> pd.Series:
    """Long-term investments share of assets."""
    return _safe_div(investments, assets)


def f14_bsss_089_investments_to_liquid_assets(investments: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Investments vs raw cash — composition of liquid holdings."""
    return _safe_div(investments, cashneq + investments)


def f14_bsss_090_non_operating_asset_share(assets: pd.Series, ppnenet: pd.Series, receivables: pd.Series, inventory: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Share of assets outside core operating buckets — opacity signal."""
    return _safe_div(assets - ppnenet - receivables - inventory - cashneq, assets)


# ---------- Equity composition (091-105) ----------

def f14_bsss_091_retearn_to_equity(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Retained earnings share of equity — earned-vs-paid-in mix."""
    return _safe_div(retearn, equity)


def f14_bsss_092_retearn_to_assets(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman X2 input — RE/assets, deficit accumulation."""
    return _safe_div(retearn, assets)


def f14_bsss_093_negative_retearn_flag(retearn: pd.Series) -> pd.Series:
    """1 if retained earnings < 0 (accumulated deficit)."""
    out = (retearn < 0).astype(float)
    return out.where(retearn.notna(), np.nan)


def f14_bsss_094_retearn_growth_yoy_assets_norm(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY delta in retained earnings normalized by assets."""
    return _safe_div(retearn - retearn.shift(YDAYS), assets)


def f14_bsss_095_sharefactor_drift_abs(sharefactor: pd.Series) -> pd.Series:
    """|sharefactor - 1| trailing-mean: cumulative split/treasury drift."""
    drift = (sharefactor - 1.0).abs()
    return drift.rolling(YDAYS, min_periods=QDAYS).mean()


def f14_bsss_096_accoci_to_equity(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """AOCI share of equity — pension/FX/hedge mark stress."""
    return _safe_div(accoci, equity)


def f14_bsss_097_accoci_to_assets(accoci: pd.Series, assets: pd.Series) -> pd.Series:
    """AOCI scaled by assets."""
    return _safe_div(accoci, assets)


def f14_bsss_098_retained_burn_intensity(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Negative-only RE change / assets — burn-rate of retained earnings."""
    d = retearn - retearn.shift(YDAYS)
    burn = d.where(d < 0, 0.0)
    return _safe_div(burn, assets)


def f14_bsss_099_equity_to_liabilities(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Altman X4 numerator-like for private/non-mfg variant."""
    return _safe_div(equity, liabilities)


def f14_bsss_100_equity_growth_yoy(equity: pd.Series) -> pd.Series:
    """YoY pct change in book equity — dilution-or-burn signal."""
    return _yoy_pct(equity, YDAYS)


def f14_bsss_101_equity_zscore_504d(equity: pd.Series) -> pd.Series:
    """Two-year rolling z-score of equity level."""
    return _rolling_zscore(equity, 504)


def f14_bsss_102_paid_in_capital_proxy(equity: pd.Series, retearn: pd.Series, accoci: pd.Series) -> pd.Series:
    """Equity - retearn - AOCI ≈ contributed (paid-in) capital."""
    return equity - retearn - accoci


def f14_bsss_103_paid_in_to_equity(equity: pd.Series, retearn: pd.Series, accoci: pd.Series) -> pd.Series:
    """Paid-in share of total equity — dilution-dependence indicator."""
    paid_in = equity - retearn - accoci
    return _safe_div(paid_in, equity)


def f14_bsss_104_retearn_to_paid_in_ratio(retearn: pd.Series, equity: pd.Series, accoci: pd.Series) -> pd.Series:
    """RE / paid-in capital — internally-generated vs externally-funded."""
    paid_in = equity - retearn - accoci
    return _safe_div(retearn, paid_in)


def f14_bsss_105_neg_equity_flag(equity: pd.Series) -> pd.Series:
    """1 if book equity < 0 (technically insolvent)."""
    out = (equity < 0).astype(float)
    return out.where(equity.notna(), np.nan)


# ---------- Coverage & solvency (106-120) ----------

def f14_bsss_106_ebitda_to_debt(ebitda: pd.Series, debt: pd.Series) -> pd.Series:
    """EBITDA / debt — inverse of D/EBITDA, coverage flavor."""
    return _safe_div(ebitda, debt)


def f14_bsss_107_ebit_to_debt(ebit: pd.Series, debt: pd.Series) -> pd.Series:
    """EBIT / debt — interest-coverage proxy (no interest column directly)."""
    return _safe_div(ebit, debt)


def f14_bsss_108_fcf_to_debt(fcf: pd.Series, debt: pd.Series) -> pd.Series:
    """Free cash flow / debt — toughest coverage flavor."""
    return _safe_div(fcf, debt)


def f14_bsss_109_cfo_to_debt(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """CFO / debt — operational coverage of total obligations."""
    return _safe_div(ncfo, debt)


def f14_bsss_110_ebitda_to_debtc(ebitda: pd.Series, debtc: pd.Series) -> pd.Series:
    """EBITDA coverage of short-term debt only."""
    return _safe_div(ebitda, debtc)


def f14_bsss_111_fcf_to_debtc(fcf: pd.Series, debtc: pd.Series) -> pd.Series:
    """FCF coverage of short-term debt only."""
    return _safe_div(fcf, debtc)


def f14_bsss_112_asset_turnover(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Revenue / assets — productivity intensity (Altman X5)."""
    return _safe_div(revenue, assets)


def f14_bsss_113_asset_turnover_zscore_504d(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Two-year z-score of asset turnover — productivity drift."""
    at = _safe_div(revenue, assets)
    return _rolling_zscore(at, 504)


def f14_bsss_114_capex_to_ppne(capex: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """Capex / net PP&E — reinvestment rate."""
    return _safe_div(capex.abs(), ppnenet)


def f14_bsss_115_capex_to_revenue(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Capex intensity vs revenue."""
    return _safe_div(capex.abs(), revenue)


def f14_bsss_116_ppne_yoy_decay(ppnenet: pd.Series) -> pd.Series:
    """YoY pct change in net PP&E — depreciation-vs-capex net signal."""
    return _yoy_pct(ppnenet, YDAYS)


def f14_bsss_117_roa_simple(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Return on assets — earnings power per asset dollar."""
    return _safe_div(netinc, assets)


def f14_bsss_118_roe_simple(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """Return on equity — for negative-equity firms this can be misleading by design."""
    return _safe_div(netinc, equity)


def f14_bsss_119_roic_proxy(netinc: pd.Series, invcap: pd.Series) -> pd.Series:
    """Return on invested capital proxy using net income / invcap."""
    return _safe_div(netinc, invcap)


def f14_bsss_120_cfo_to_revenue(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Cash conversion margin — operating cash per revenue dollar."""
    return _safe_div(ncfo, revenue)


# ---------- Altman, Beneish, Ohlson distress (121-135) ----------

def f14_bsss_121_altman_x1(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman X1 = WC / assets."""
    return _safe_div(workingcapital, assets)


def f14_bsss_122_altman_x2(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman X2 = retained earnings / assets."""
    return _safe_div(retearn, assets)


def f14_bsss_123_altman_x3(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman X3 = EBIT / assets."""
    return _safe_div(ebit, assets)


def f14_bsss_124_altman_x4_book(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Altman X4 book-equity variant = equity / liabilities."""
    return _safe_div(equity, liabilities)


def f14_bsss_125_altman_x5(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman X5 = revenue / assets — asset turnover."""
    return _safe_div(revenue, assets)


def f14_bsss_126_altman_z_full(workingcapital: pd.Series, retearn: pd.Series, ebit: pd.Series, equity: pd.Series, liabilities: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z' (book-equity variant): 0.717X1 + 0.847X2 + 3.107X3 + 0.420X4 + 0.998X5."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    x5 = _safe_div(revenue, assets)
    return 0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4 + 0.998 * x5


def f14_bsss_127_altman_z_prime_nonmfg(workingcapital: pd.Series, retearn: pd.Series, ebit: pd.Series, equity: pd.Series, liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' non-manufacturing: 6.56X1 + 3.26X2 + 6.72X3 + 1.05X4 (no asset turnover)."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def f14_bsss_128_beneish_dsri(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Days sales in receivables index: (AR_t/Rev_t) / (AR_{t-1y}/Rev_{t-1y})."""
    cur = _safe_div(receivables, revenue)
    prev = _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS))
    return _safe_div(cur, prev)


def f14_bsss_129_beneish_aqi(assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Asset quality index: AQI_t / AQI_{t-1y} where AQI = (assets-CA-PPE-intangibles)/assets."""
    aqi = _safe_div(assets - assetsc - ppnenet - intangibles, assets)
    return _safe_div(aqi, aqi.shift(YDAYS))


def f14_bsss_130_beneish_sgai(sga: pd.Series, revenue: pd.Series) -> pd.Series:
    """SG&A index: (SGA_t/Rev_t) / (SGA_{t-1y}/Rev_{t-1y})."""
    cur = _safe_div(sga, revenue)
    prev = _safe_div(sga.shift(YDAYS), revenue.shift(YDAYS))
    return _safe_div(cur, prev)


def f14_bsss_131_beneish_tata(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Total accruals to total assets: (NI - CFO) / assets — Beneish TATA."""
    return _safe_div(netinc - ncfo, assets)


def f14_bsss_132_ohlson_tlta_flag(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """1 if total liabilities > total assets (insolvency by Ohlson definition)."""
    r = _safe_div(liabilities, assets)
    out = (r > 1.0).astype(float)
    return out.where(r.notna(), np.nan)


def f14_bsss_133_ohlson_chin(netinc: pd.Series) -> pd.Series:
    """Ohlson chin: (NI_t - NI_{t-1y}) / (|NI_t| + |NI_{t-1y}|)."""
    prev = netinc.shift(YDAYS)
    denom = netinc.abs() + prev.abs()
    return _safe_div(netinc - prev, denom)


def f14_bsss_134_ohlson_oneg_two_consecutive(netinc: pd.Series) -> pd.Series:
    """Ohlson OENEG: 1 if both NI_t<0 and NI_{t-1y}<0 else 0."""
    cur_neg = (netinc < 0).astype(float)
    prev_neg = (netinc.shift(YDAYS) < 0).astype(float)
    both = cur_neg * prev_neg
    return both.where(netinc.notna() & netinc.shift(YDAYS).notna(), np.nan)


def f14_bsss_135_ohlson_tlta_ratio(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson TLTA = liabilities / assets — continuous distress lever (distinct from flag)."""
    return _safe_div(liabilities, assets)


# ---------- Negative flags + composite z-scores (136-150) ----------

def f14_bsss_136_neg_equity_or_tangible_flag(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """1 if book equity OR tangible equity is negative."""
    te = equity - intangibles
    out = ((equity < 0) | (te < 0)).astype(float)
    return out.where(equity.notna() & intangibles.notna(), np.nan)


def f14_bsss_137_neg_workingcapital_flag(workingcapital: pd.Series) -> pd.Series:
    """1 if working capital < 0."""
    out = (workingcapital < 0).astype(float)
    return out.where(workingcapital.notna(), np.nan)


def f14_bsss_138_neg_fcf_flag(fcf: pd.Series) -> pd.Series:
    """1 if free cash flow < 0."""
    out = (fcf < 0).astype(float)
    return out.where(fcf.notna(), np.nan)


def f14_bsss_139_neg_cfo_flag(ncfo: pd.Series) -> pd.Series:
    """1 if operating cash flow < 0."""
    out = (ncfo < 0).astype(float)
    return out.where(ncfo.notna(), np.nan)


def f14_bsss_140_neg_netinc_flag(netinc: pd.Series) -> pd.Series:
    """1 if net income < 0."""
    out = (netinc < 0).astype(float)
    return out.where(netinc.notna(), np.nan)


def f14_bsss_141_distress_flag_count(equity: pd.Series, workingcapital: pd.Series, fcf: pd.Series, ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Sum of binary distress flags across 5 metrics (NaN-aware)."""
    a = (equity < 0).astype(float).where(equity.notna(), np.nan)
    b = (workingcapital < 0).astype(float).where(workingcapital.notna(), np.nan)
    c = (fcf < 0).astype(float).where(fcf.notna(), np.nan)
    d = (ncfo < 0).astype(float).where(ncfo.notna(), np.nan)
    e = (netinc < 0).astype(float).where(netinc.notna(), np.nan)
    return a + b + c + d + e


def f14_bsss_142_composite_z_leverage(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Mean z-score of D/E, D/A, D/EBITDA (504d window)."""
    de = _rolling_zscore(_safe_div(debt, equity), 504)
    da = _rolling_zscore(_safe_div(debt, assets), 504)
    db = _rolling_zscore(_safe_div(debt, ebitda), 504)
    return pd.concat([de, da, db], axis=1).mean(axis=1)


def f14_bsss_143_composite_z_liquidity(assetsc: pd.Series, liabilitiesc: pd.Series, cashneq: pd.Series, inventory: pd.Series) -> pd.Series:
    """Negative mean z-score of current, quick, cash ratios (so HIGH = stressed)."""
    cur = _rolling_zscore(_safe_div(assetsc, liabilitiesc), 504)
    qk = _rolling_zscore(_safe_div(assetsc - inventory, liabilitiesc), 504)
    csh = _rolling_zscore(_safe_div(cashneq, liabilitiesc), 504)
    return -pd.concat([cur, qk, csh], axis=1).mean(axis=1)


def f14_bsss_144_composite_z_solvency(ebitda: pd.Series, debt: pd.Series, fcf: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Negative mean z-score of EBITDA/D, FCF/D, CFO/D — HIGH = stressed."""
    eb = _rolling_zscore(_safe_div(ebitda, debt), 504)
    fc = _rolling_zscore(_safe_div(fcf, debt), 504)
    cf = _rolling_zscore(_safe_div(ncfo, debt), 504)
    return -pd.concat([eb, fc, cf], axis=1).mean(axis=1)


def f14_bsss_145_composite_z_asset_quality(intangibles: pd.Series, assets: pd.Series, ppnenet: pd.Series, equity: pd.Series) -> pd.Series:
    """Mean z-score of intangibles/assets, intangibles/equity, opaque assets share."""
    a = _rolling_zscore(_safe_div(intangibles, assets), 504)
    b = _rolling_zscore(_safe_div(intangibles, equity), 504)
    opaque = _safe_div(assets - ppnenet - intangibles, assets)
    c = _rolling_zscore(opaque, 504)
    return pd.concat([a, b, c], axis=1).mean(axis=1)


def f14_bsss_146_composite_z_dilution_dependence(equity: pd.Series, retearn: pd.Series, accoci: pd.Series, assets: pd.Series) -> pd.Series:
    """Mean z-score of paid-in/equity and -retearn/assets (HIGH = relies on dilution, low earned base)."""
    paid_in = equity - retearn - accoci
    a = _rolling_zscore(_safe_div(paid_in, equity), 504)
    b = _rolling_zscore(_safe_div(-retearn, assets), 504)
    return pd.concat([a, b], axis=1).mean(axis=1)


def f14_bsss_147_composite_z_accrual_quality(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, assetsc: pd.Series, cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Mean z-score of Sloan accruals and operating-WC accruals — HIGH = aggressive earnings."""
    sloan = _safe_div(netinc - ncfo, assets)
    op_wc = assetsc - cashneq - liabilitiesc
    op_accr = _safe_div(op_wc - op_wc.shift(YDAYS), assets)
    a = _rolling_zscore(sloan, 504)
    b = _rolling_zscore(op_accr, 504)
    return pd.concat([a, b], axis=1).mean(axis=1)


def f14_bsss_148_composite_z_ccc_stress(receivables: pd.Series, inventory: pd.Series, payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Mean z-score of DSO, DIO, -DPO (HIGH = capital tied up longer)."""
    dso = _safe_div(receivables * 91.25, revenue)
    dio = _safe_div(inventory * 91.25, cor)
    dpo = _safe_div(payables * 91.25, cor)
    a = _rolling_zscore(dso, 504)
    b = _rolling_zscore(dio, 504)
    c = _rolling_zscore(-dpo, 504)
    return pd.concat([a, b, c], axis=1).mean(axis=1)


def f14_bsss_149_distance_to_distress_merton_lite(equity: pd.Series, debt: pd.Series) -> pd.Series:
    """Merton-lite proxy: equity / (equity + debt) — book-only DD surrogate."""
    return _safe_div(equity, equity + debt)


def f14_bsss_150_composite_z_balance_sheet_stress(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series, assetsc: pd.Series, liabilitiesc: pd.Series, cashneq: pd.Series, inventory: pd.Series, fcf: pd.Series, ncfo: pd.Series, intangibles: pd.Series, retearn: pd.Series) -> pd.Series:
    """Overall stress composite: average of leverage(+) liquidity(-) solvency(-) asset-quality(+) deficit(+)."""
    lev = _rolling_zscore(_safe_div(debt, assets), 504)
    liq = -_rolling_zscore(_safe_div(assetsc - inventory, liabilitiesc), 504)
    sol = -_rolling_zscore(_safe_div(fcf, debt), 504)
    aq = _rolling_zscore(_safe_div(intangibles, assets), 504)
    deficit = _rolling_zscore(_safe_div(-retearn, assets), 504)
    return pd.concat([lev, liq, sol, aq, deficit], axis=1).mean(axis=1)


# ============================================================
#                        REGISTRY
# ============================================================

BALANCE_SHEET_STRESS_SNAPSHOT_BASE_REGISTRY_076_150 = {
    "f14_bsss_076_intangibles_to_assets": {"inputs": ["intangibles", "assets"], "func": f14_bsss_076_intangibles_to_assets},
    "f14_bsss_077_intangibles_to_equity": {"inputs": ["intangibles", "equity"], "func": f14_bsss_077_intangibles_to_equity},
    "f14_bsss_078_intangibles_to_tangibles": {"inputs": ["intangibles", "tangibles"], "func": f14_bsss_078_intangibles_to_tangibles},
    "f14_bsss_079_tangibles_to_assets": {"inputs": ["tangibles", "assets"], "func": f14_bsss_079_tangibles_to_assets},
    "f14_bsss_080_tangible_equity_ratio": {"inputs": ["equity", "intangibles", "assets"], "func": f14_bsss_080_tangible_equity_ratio},
    "f14_bsss_081_tangible_book_to_total_book": {"inputs": ["equity", "intangibles"], "func": f14_bsss_081_tangible_book_to_total_book},
    "f14_bsss_082_neg_tangible_equity_flag": {"inputs": ["equity", "intangibles"], "func": f14_bsss_082_neg_tangible_equity_flag},
    "f14_bsss_083_intangibles_growth_yoy": {"inputs": ["intangibles"], "func": f14_bsss_083_intangibles_growth_yoy},
    "f14_bsss_084_intangibles_to_invcap": {"inputs": ["intangibles", "invcap"], "func": f14_bsss_084_intangibles_to_invcap},
    "f14_bsss_085_intangibles_minus_equity_impairment_proxy": {"inputs": ["intangibles", "equity", "assets"], "func": f14_bsss_085_intangibles_minus_equity_impairment_proxy},
    "f14_bsss_086_asset_quality_index": {"inputs": ["assets", "assetsc", "ppnenet", "intangibles"], "func": f14_bsss_086_asset_quality_index},
    "f14_bsss_087_ppnenet_to_assets": {"inputs": ["ppnenet", "assets"], "func": f14_bsss_087_ppnenet_to_assets},
    "f14_bsss_088_investments_to_assets": {"inputs": ["investments", "assets"], "func": f14_bsss_088_investments_to_assets},
    "f14_bsss_089_investments_to_liquid_assets": {"inputs": ["investments", "cashneq"], "func": f14_bsss_089_investments_to_liquid_assets},
    "f14_bsss_090_non_operating_asset_share": {"inputs": ["assets", "ppnenet", "receivables", "inventory", "cashneq"], "func": f14_bsss_090_non_operating_asset_share},
    "f14_bsss_091_retearn_to_equity": {"inputs": ["retearn", "equity"], "func": f14_bsss_091_retearn_to_equity},
    "f14_bsss_092_retearn_to_assets": {"inputs": ["retearn", "assets"], "func": f14_bsss_092_retearn_to_assets},
    "f14_bsss_093_negative_retearn_flag": {"inputs": ["retearn"], "func": f14_bsss_093_negative_retearn_flag},
    "f14_bsss_094_retearn_growth_yoy_assets_norm": {"inputs": ["retearn", "assets"], "func": f14_bsss_094_retearn_growth_yoy_assets_norm},
    "f14_bsss_095_sharefactor_drift_abs": {"inputs": ["sharefactor"], "func": f14_bsss_095_sharefactor_drift_abs},
    "f14_bsss_096_accoci_to_equity": {"inputs": ["accoci", "equity"], "func": f14_bsss_096_accoci_to_equity},
    "f14_bsss_097_accoci_to_assets": {"inputs": ["accoci", "assets"], "func": f14_bsss_097_accoci_to_assets},
    "f14_bsss_098_retained_burn_intensity": {"inputs": ["retearn", "assets"], "func": f14_bsss_098_retained_burn_intensity},
    "f14_bsss_099_equity_to_liabilities": {"inputs": ["equity", "liabilities"], "func": f14_bsss_099_equity_to_liabilities},
    "f14_bsss_100_equity_growth_yoy": {"inputs": ["equity"], "func": f14_bsss_100_equity_growth_yoy},
    "f14_bsss_101_equity_zscore_504d": {"inputs": ["equity"], "func": f14_bsss_101_equity_zscore_504d},
    "f14_bsss_102_paid_in_capital_proxy": {"inputs": ["equity", "retearn", "accoci"], "func": f14_bsss_102_paid_in_capital_proxy},
    "f14_bsss_103_paid_in_to_equity": {"inputs": ["equity", "retearn", "accoci"], "func": f14_bsss_103_paid_in_to_equity},
    "f14_bsss_104_retearn_to_paid_in_ratio": {"inputs": ["retearn", "equity", "accoci"], "func": f14_bsss_104_retearn_to_paid_in_ratio},
    "f14_bsss_105_neg_equity_flag": {"inputs": ["equity"], "func": f14_bsss_105_neg_equity_flag},
    "f14_bsss_106_ebitda_to_debt": {"inputs": ["ebitda", "debt"], "func": f14_bsss_106_ebitda_to_debt},
    "f14_bsss_107_ebit_to_debt": {"inputs": ["ebit", "debt"], "func": f14_bsss_107_ebit_to_debt},
    "f14_bsss_108_fcf_to_debt": {"inputs": ["fcf", "debt"], "func": f14_bsss_108_fcf_to_debt},
    "f14_bsss_109_cfo_to_debt": {"inputs": ["ncfo", "debt"], "func": f14_bsss_109_cfo_to_debt},
    "f14_bsss_110_ebitda_to_debtc": {"inputs": ["ebitda", "debtc"], "func": f14_bsss_110_ebitda_to_debtc},
    "f14_bsss_111_fcf_to_debtc": {"inputs": ["fcf", "debtc"], "func": f14_bsss_111_fcf_to_debtc},
    "f14_bsss_112_asset_turnover": {"inputs": ["revenue", "assets"], "func": f14_bsss_112_asset_turnover},
    "f14_bsss_113_asset_turnover_zscore_504d": {"inputs": ["revenue", "assets"], "func": f14_bsss_113_asset_turnover_zscore_504d},
    "f14_bsss_114_capex_to_ppne": {"inputs": ["capex", "ppnenet"], "func": f14_bsss_114_capex_to_ppne},
    "f14_bsss_115_capex_to_revenue": {"inputs": ["capex", "revenue"], "func": f14_bsss_115_capex_to_revenue},
    "f14_bsss_116_ppne_yoy_decay": {"inputs": ["ppnenet"], "func": f14_bsss_116_ppne_yoy_decay},
    "f14_bsss_117_roa_simple": {"inputs": ["netinc", "assets"], "func": f14_bsss_117_roa_simple},
    "f14_bsss_118_roe_simple": {"inputs": ["netinc", "equity"], "func": f14_bsss_118_roe_simple},
    "f14_bsss_119_roic_proxy": {"inputs": ["netinc", "invcap"], "func": f14_bsss_119_roic_proxy},
    "f14_bsss_120_cfo_to_revenue": {"inputs": ["ncfo", "revenue"], "func": f14_bsss_120_cfo_to_revenue},
    "f14_bsss_121_altman_x1": {"inputs": ["workingcapital", "assets"], "func": f14_bsss_121_altman_x1},
    "f14_bsss_122_altman_x2": {"inputs": ["retearn", "assets"], "func": f14_bsss_122_altman_x2},
    "f14_bsss_123_altman_x3": {"inputs": ["ebit", "assets"], "func": f14_bsss_123_altman_x3},
    "f14_bsss_124_altman_x4_book": {"inputs": ["equity", "liabilities"], "func": f14_bsss_124_altman_x4_book},
    "f14_bsss_125_altman_x5": {"inputs": ["revenue", "assets"], "func": f14_bsss_125_altman_x5},
    "f14_bsss_126_altman_z_full": {"inputs": ["workingcapital", "retearn", "ebit", "equity", "liabilities", "revenue", "assets"], "func": f14_bsss_126_altman_z_full},
    "f14_bsss_127_altman_z_prime_nonmfg": {"inputs": ["workingcapital", "retearn", "ebit", "equity", "liabilities", "assets"], "func": f14_bsss_127_altman_z_prime_nonmfg},
    "f14_bsss_128_beneish_dsri": {"inputs": ["receivables", "revenue"], "func": f14_bsss_128_beneish_dsri},
    "f14_bsss_129_beneish_aqi": {"inputs": ["assets", "assetsc", "ppnenet", "intangibles"], "func": f14_bsss_129_beneish_aqi},
    "f14_bsss_130_beneish_sgai": {"inputs": ["sga", "revenue"], "func": f14_bsss_130_beneish_sgai},
    "f14_bsss_131_beneish_tata": {"inputs": ["netinc", "ncfo", "assets"], "func": f14_bsss_131_beneish_tata},
    "f14_bsss_132_ohlson_tlta_flag": {"inputs": ["liabilities", "assets"], "func": f14_bsss_132_ohlson_tlta_flag},
    "f14_bsss_133_ohlson_chin": {"inputs": ["netinc"], "func": f14_bsss_133_ohlson_chin},
    "f14_bsss_134_ohlson_oneg_two_consecutive": {"inputs": ["netinc"], "func": f14_bsss_134_ohlson_oneg_two_consecutive},
    "f14_bsss_135_ohlson_tlta_ratio": {"inputs": ["liabilities", "assets"], "func": f14_bsss_135_ohlson_tlta_ratio},
    "f14_bsss_136_neg_equity_or_tangible_flag": {"inputs": ["equity", "intangibles"], "func": f14_bsss_136_neg_equity_or_tangible_flag},
    "f14_bsss_137_neg_workingcapital_flag": {"inputs": ["workingcapital"], "func": f14_bsss_137_neg_workingcapital_flag},
    "f14_bsss_138_neg_fcf_flag": {"inputs": ["fcf"], "func": f14_bsss_138_neg_fcf_flag},
    "f14_bsss_139_neg_cfo_flag": {"inputs": ["ncfo"], "func": f14_bsss_139_neg_cfo_flag},
    "f14_bsss_140_neg_netinc_flag": {"inputs": ["netinc"], "func": f14_bsss_140_neg_netinc_flag},
    "f14_bsss_141_distress_flag_count": {"inputs": ["equity", "workingcapital", "fcf", "ncfo", "netinc"], "func": f14_bsss_141_distress_flag_count},
    "f14_bsss_142_composite_z_leverage": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": f14_bsss_142_composite_z_leverage},
    "f14_bsss_143_composite_z_liquidity": {"inputs": ["assetsc", "liabilitiesc", "cashneq", "inventory"], "func": f14_bsss_143_composite_z_liquidity},
    "f14_bsss_144_composite_z_solvency": {"inputs": ["ebitda", "debt", "fcf", "ncfo"], "func": f14_bsss_144_composite_z_solvency},
    "f14_bsss_145_composite_z_asset_quality": {"inputs": ["intangibles", "assets", "ppnenet", "equity"], "func": f14_bsss_145_composite_z_asset_quality},
    "f14_bsss_146_composite_z_dilution_dependence": {"inputs": ["equity", "retearn", "accoci", "assets"], "func": f14_bsss_146_composite_z_dilution_dependence},
    "f14_bsss_147_composite_z_accrual_quality": {"inputs": ["netinc", "ncfo", "assets", "assetsc", "cashneq", "liabilitiesc"], "func": f14_bsss_147_composite_z_accrual_quality},
    "f14_bsss_148_composite_z_ccc_stress": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f14_bsss_148_composite_z_ccc_stress},
    "f14_bsss_149_distance_to_distress_merton_lite": {"inputs": ["equity", "debt"], "func": f14_bsss_149_distance_to_distress_merton_lite},
    "f14_bsss_150_composite_z_balance_sheet_stress": {"inputs": ["debt", "equity", "assets", "ebitda", "assetsc", "liabilitiesc", "cashneq", "inventory", "fcf", "ncfo", "intangibles", "retearn"], "func": f14_bsss_150_composite_z_balance_sheet_stress},
}
