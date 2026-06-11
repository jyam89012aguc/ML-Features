"""balance_sheet_stress_snapshot d2 features 076_150 - second-derivative (acceleration) wrappers.

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
#                D2 FEATURES 076_150
# ============================================================

def f14_bsss_076_intangibles_to_assets_d2(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(intangibles, assets)).diff().diff()


def f14_bsss_077_intangibles_to_equity_d2(intangibles: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(intangibles, equity)).diff().diff()


def f14_bsss_078_intangibles_to_tangibles_d2(intangibles: pd.Series, tangibles: pd.Series) -> pd.Series:
    return (_safe_div(intangibles, tangibles)).diff().diff()


def f14_bsss_079_tangibles_to_assets_d2(tangibles: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(tangibles, assets)).diff().diff()


def f14_bsss_080_tangible_equity_ratio_d2(equity: pd.Series, intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(equity - intangibles, assets)).diff().diff()


def f14_bsss_081_tangible_book_to_total_book_d2(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    return (_safe_div(equity - intangibles, equity)).diff().diff()


def f14_bsss_082_neg_tangible_equity_flag_d2(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    te = equity - intangibles
    out = (te < 0).astype(float)
    return (out.where(te.notna(), np.nan)).diff().diff()


def f14_bsss_083_intangibles_growth_yoy_d2(intangibles: pd.Series) -> pd.Series:
    return (_yoy_pct(intangibles, YDAYS)).diff().diff()


def f14_bsss_084_intangibles_to_invcap_d2(intangibles: pd.Series, invcap: pd.Series) -> pd.Series:
    return (_safe_div(intangibles, invcap)).diff().diff()


def f14_bsss_085_intangibles_minus_equity_impairment_proxy_d2(intangibles: pd.Series, equity: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(intangibles - equity, assets)).diff().diff()


def f14_bsss_086_asset_quality_index_d2(assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series, intangibles: pd.Series) -> pd.Series:
    return (_safe_div(assets - assetsc - ppnenet - intangibles, assets)).diff().diff()


def f14_bsss_087_ppnenet_to_assets_d2(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(ppnenet, assets)).diff().diff()


def f14_bsss_088_investments_to_assets_d2(investments: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(investments, assets)).diff().diff()


def f14_bsss_089_investments_to_liquid_assets_d2(investments: pd.Series, cashneq: pd.Series) -> pd.Series:
    return (_safe_div(investments, cashneq + investments)).diff().diff()


def f14_bsss_090_non_operating_asset_share_d2(assets: pd.Series, ppnenet: pd.Series, receivables: pd.Series, inventory: pd.Series, cashneq: pd.Series) -> pd.Series:
    return (_safe_div(assets - ppnenet - receivables - inventory - cashneq, assets)).diff().diff()


def f14_bsss_091_retearn_to_equity_d2(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(retearn, equity)).diff().diff()


def f14_bsss_092_retearn_to_assets_d2(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(retearn, assets)).diff().diff()


def f14_bsss_093_negative_retearn_flag_d2(retearn: pd.Series) -> pd.Series:
    out = (retearn < 0).astype(float)
    return (out.where(retearn.notna(), np.nan)).diff().diff()


def f14_bsss_094_retearn_growth_yoy_assets_norm_d2(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(retearn - retearn.shift(YDAYS), assets)).diff().diff()


def f14_bsss_095_sharefactor_drift_abs_d2(sharefactor: pd.Series) -> pd.Series:
    drift = (sharefactor - 1.0).abs()
    return (drift.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()


def f14_bsss_096_accoci_to_equity_d2(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(accoci, equity)).diff().diff()


def f14_bsss_097_accoci_to_assets_d2(accoci: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(accoci, assets)).diff().diff()


def f14_bsss_098_retained_burn_intensity_d2(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    d = retearn - retearn.shift(YDAYS)
    burn = d.where(d < 0, 0.0)
    return (_safe_div(burn, assets)).diff().diff()


def f14_bsss_099_equity_to_liabilities_d2(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    return (_safe_div(equity, liabilities)).diff().diff()


def f14_bsss_100_equity_growth_yoy_d2(equity: pd.Series) -> pd.Series:
    return (_yoy_pct(equity, YDAYS)).diff().diff()


def f14_bsss_101_equity_zscore_504d_d2(equity: pd.Series) -> pd.Series:
    return (_rolling_zscore(equity, 504)).diff().diff()


def f14_bsss_102_paid_in_capital_proxy_d2(equity: pd.Series, retearn: pd.Series, accoci: pd.Series) -> pd.Series:
    return (equity - retearn - accoci).diff().diff()


def f14_bsss_103_paid_in_to_equity_d2(equity: pd.Series, retearn: pd.Series, accoci: pd.Series) -> pd.Series:
    paid_in = equity - retearn - accoci
    return (_safe_div(paid_in, equity)).diff().diff()


def f14_bsss_104_retearn_to_paid_in_ratio_d2(retearn: pd.Series, equity: pd.Series, accoci: pd.Series) -> pd.Series:
    paid_in = equity - retearn - accoci
    return (_safe_div(retearn, paid_in)).diff().diff()


def f14_bsss_105_neg_equity_flag_d2(equity: pd.Series) -> pd.Series:
    out = (equity < 0).astype(float)
    return (out.where(equity.notna(), np.nan)).diff().diff()


def f14_bsss_106_ebitda_to_debt_d2(ebitda: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(ebitda, debt)).diff().diff()


def f14_bsss_107_ebit_to_debt_d2(ebit: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(ebit, debt)).diff().diff()


def f14_bsss_108_fcf_to_debt_d2(fcf: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(fcf, debt)).diff().diff()


def f14_bsss_109_cfo_to_debt_d2(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(ncfo, debt)).diff().diff()


def f14_bsss_110_ebitda_to_debtc_d2(ebitda: pd.Series, debtc: pd.Series) -> pd.Series:
    return (_safe_div(ebitda, debtc)).diff().diff()


def f14_bsss_111_fcf_to_debtc_d2(fcf: pd.Series, debtc: pd.Series) -> pd.Series:
    return (_safe_div(fcf, debtc)).diff().diff()


def f14_bsss_112_asset_turnover_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(revenue, assets)).diff().diff()


def f14_bsss_113_asset_turnover_zscore_504d_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    at = _safe_div(revenue, assets)
    return (_rolling_zscore(at, 504)).diff().diff()


def f14_bsss_114_capex_to_ppne_d2(capex: pd.Series, ppnenet: pd.Series) -> pd.Series:
    return (_safe_div(capex.abs(), ppnenet)).diff().diff()


def f14_bsss_115_capex_to_revenue_d2(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(capex.abs(), revenue)).diff().diff()


def f14_bsss_116_ppne_yoy_decay_d2(ppnenet: pd.Series) -> pd.Series:
    return (_yoy_pct(ppnenet, YDAYS)).diff().diff()


def f14_bsss_117_roa_simple_d2(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(netinc, assets)).diff().diff()


def f14_bsss_118_roe_simple_d2(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    return (_safe_div(netinc, equity)).diff().diff()


def f14_bsss_119_roic_proxy_d2(netinc: pd.Series, invcap: pd.Series) -> pd.Series:
    return (_safe_div(netinc, invcap)).diff().diff()


def f14_bsss_120_cfo_to_revenue_d2(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_div(ncfo, revenue)).diff().diff()


def f14_bsss_121_altman_x1_d2(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(workingcapital, assets)).diff().diff()


def f14_bsss_122_altman_x2_d2(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(retearn, assets)).diff().diff()


def f14_bsss_123_altman_x3_d2(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(ebit, assets)).diff().diff()


def f14_bsss_124_altman_x4_book_d2(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    return (_safe_div(equity, liabilities)).diff().diff()


def f14_bsss_125_altman_x5_d2(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(revenue, assets)).diff().diff()


def f14_bsss_126_altman_z_full_d2(workingcapital: pd.Series, retearn: pd.Series, ebit: pd.Series, equity: pd.Series, liabilities: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    x5 = _safe_div(revenue, assets)
    return (0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4 + 0.998 * x5).diff().diff()


def f14_bsss_127_altman_z_prime_nonmfg_d2(workingcapital: pd.Series, retearn: pd.Series, ebit: pd.Series, equity: pd.Series, liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return (6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4).diff().diff()


def f14_bsss_128_beneish_dsri_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    cur = _safe_div(receivables, revenue)
    prev = _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS))
    return (_safe_div(cur, prev)).diff().diff()


def f14_bsss_129_beneish_aqi_d2(assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series, intangibles: pd.Series) -> pd.Series:
    aqi = _safe_div(assets - assetsc - ppnenet - intangibles, assets)
    return (_safe_div(aqi, aqi.shift(YDAYS))).diff().diff()


def f14_bsss_130_beneish_sgai_d2(sga: pd.Series, revenue: pd.Series) -> pd.Series:
    cur = _safe_div(sga, revenue)
    prev = _safe_div(sga.shift(YDAYS), revenue.shift(YDAYS))
    return (_safe_div(cur, prev)).diff().diff()


def f14_bsss_131_beneish_tata_d2(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(netinc - ncfo, assets)).diff().diff()


def f14_bsss_132_ohlson_tlta_flag_d2(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    r = _safe_div(liabilities, assets)
    out = (r > 1.0).astype(float)
    return (out.where(r.notna(), np.nan)).diff().diff()


def f14_bsss_133_ohlson_chin_d2(netinc: pd.Series) -> pd.Series:
    prev = netinc.shift(YDAYS)
    denom = netinc.abs() + prev.abs()
    return (_safe_div(netinc - prev, denom)).diff().diff()


def f14_bsss_134_ohlson_oneg_two_consecutive_d2(netinc: pd.Series) -> pd.Series:
    cur_neg = (netinc < 0).astype(float)
    prev_neg = (netinc.shift(YDAYS) < 0).astype(float)
    both = cur_neg * prev_neg
    return (both.where(netinc.notna() & netinc.shift(YDAYS).notna(), np.nan)).diff().diff()


def f14_bsss_135_ohlson_tlta_ratio_d2(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    return (_safe_div(liabilities, assets)).diff().diff()


def f14_bsss_136_neg_equity_or_tangible_flag_d2(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    te = equity - intangibles
    out = ((equity < 0) | (te < 0)).astype(float)
    return (out.where(equity.notna() & intangibles.notna(), np.nan)).diff().diff()


def f14_bsss_137_neg_workingcapital_flag_d2(workingcapital: pd.Series) -> pd.Series:
    out = (workingcapital < 0).astype(float)
    return (out.where(workingcapital.notna(), np.nan)).diff().diff()


def f14_bsss_138_neg_fcf_flag_d2(fcf: pd.Series) -> pd.Series:
    out = (fcf < 0).astype(float)
    return (out.where(fcf.notna(), np.nan)).diff().diff()


def f14_bsss_139_neg_cfo_flag_d2(ncfo: pd.Series) -> pd.Series:
    out = (ncfo < 0).astype(float)
    return (out.where(ncfo.notna(), np.nan)).diff().diff()


def f14_bsss_140_neg_netinc_flag_d2(netinc: pd.Series) -> pd.Series:
    out = (netinc < 0).astype(float)
    return (out.where(netinc.notna(), np.nan)).diff().diff()


def f14_bsss_141_distress_flag_count_d2(equity: pd.Series, workingcapital: pd.Series, fcf: pd.Series, ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    a = (equity < 0).astype(float).where(equity.notna(), np.nan)
    b = (workingcapital < 0).astype(float).where(workingcapital.notna(), np.nan)
    c = (fcf < 0).astype(float).where(fcf.notna(), np.nan)
    d = (ncfo < 0).astype(float).where(ncfo.notna(), np.nan)
    e = (netinc < 0).astype(float).where(netinc.notna(), np.nan)
    return (a + b + c + d + e).diff().diff()


def f14_bsss_142_composite_z_leverage_d2(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    de = _rolling_zscore(_safe_div(debt, equity), 504)
    da = _rolling_zscore(_safe_div(debt, assets), 504)
    db = _rolling_zscore(_safe_div(debt, ebitda), 504)
    return (pd.concat([de, da, db], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_143_composite_z_liquidity_d2(assetsc: pd.Series, liabilitiesc: pd.Series, cashneq: pd.Series, inventory: pd.Series) -> pd.Series:
    cur = _rolling_zscore(_safe_div(assetsc, liabilitiesc), 504)
    qk = _rolling_zscore(_safe_div(assetsc - inventory, liabilitiesc), 504)
    csh = _rolling_zscore(_safe_div(cashneq, liabilitiesc), 504)
    return (-pd.concat([cur, qk, csh], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_144_composite_z_solvency_d2(ebitda: pd.Series, debt: pd.Series, fcf: pd.Series, ncfo: pd.Series) -> pd.Series:
    eb = _rolling_zscore(_safe_div(ebitda, debt), 504)
    fc = _rolling_zscore(_safe_div(fcf, debt), 504)
    cf = _rolling_zscore(_safe_div(ncfo, debt), 504)
    return (-pd.concat([eb, fc, cf], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_145_composite_z_asset_quality_d2(intangibles: pd.Series, assets: pd.Series, ppnenet: pd.Series, equity: pd.Series) -> pd.Series:
    a = _rolling_zscore(_safe_div(intangibles, assets), 504)
    b = _rolling_zscore(_safe_div(intangibles, equity), 504)
    opaque = _safe_div(assets - ppnenet - intangibles, assets)
    c = _rolling_zscore(opaque, 504)
    return (pd.concat([a, b, c], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_146_composite_z_dilution_dependence_d2(equity: pd.Series, retearn: pd.Series, accoci: pd.Series, assets: pd.Series) -> pd.Series:
    paid_in = equity - retearn - accoci
    a = _rolling_zscore(_safe_div(paid_in, equity), 504)
    b = _rolling_zscore(_safe_div(-retearn, assets), 504)
    return (pd.concat([a, b], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_147_composite_z_accrual_quality_d2(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, assetsc: pd.Series, cashneq: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    sloan = _safe_div(netinc - ncfo, assets)
    op_wc = assetsc - cashneq - liabilitiesc
    op_accr = _safe_div(op_wc - op_wc.shift(YDAYS), assets)
    a = _rolling_zscore(sloan, 504)
    b = _rolling_zscore(op_accr, 504)
    return (pd.concat([a, b], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_148_composite_z_ccc_stress_d2(receivables: pd.Series, inventory: pd.Series, payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    dso = _safe_div(receivables * 91.25, revenue)
    dio = _safe_div(inventory * 91.25, cor)
    dpo = _safe_div(payables * 91.25, cor)
    a = _rolling_zscore(dso, 504)
    b = _rolling_zscore(dio, 504)
    c = _rolling_zscore(-dpo, 504)
    return (pd.concat([a, b, c], axis=1).mean(axis=1)).diff().diff()


def f14_bsss_149_distance_to_distress_merton_lite_d2(equity: pd.Series, debt: pd.Series) -> pd.Series:
    return (_safe_div(equity, equity + debt)).diff().diff()


def f14_bsss_150_composite_z_balance_sheet_stress_d2(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series, assetsc: pd.Series, liabilitiesc: pd.Series, cashneq: pd.Series, inventory: pd.Series, fcf: pd.Series, ncfo: pd.Series, intangibles: pd.Series, retearn: pd.Series) -> pd.Series:
    lev = _rolling_zscore(_safe_div(debt, assets), 504)
    liq = -_rolling_zscore(_safe_div(assetsc - inventory, liabilitiesc), 504)
    sol = -_rolling_zscore(_safe_div(fcf, debt), 504)
    aq = _rolling_zscore(_safe_div(intangibles, assets), 504)
    deficit = _rolling_zscore(_safe_div(-retearn, assets), 504)
    return (pd.concat([lev, liq, sol, aq, deficit], axis=1).mean(axis=1)).diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

BALANCE_SHEET_STRESS_SNAPSHOT_D2_REGISTRY_076_150 = {
    "f14_bsss_076_intangibles_to_assets_d2": {"inputs": ["intangibles", "assets"], "func": f14_bsss_076_intangibles_to_assets_d2},
    "f14_bsss_077_intangibles_to_equity_d2": {"inputs": ["intangibles", "equity"], "func": f14_bsss_077_intangibles_to_equity_d2},
    "f14_bsss_078_intangibles_to_tangibles_d2": {"inputs": ["intangibles", "tangibles"], "func": f14_bsss_078_intangibles_to_tangibles_d2},
    "f14_bsss_079_tangibles_to_assets_d2": {"inputs": ["tangibles", "assets"], "func": f14_bsss_079_tangibles_to_assets_d2},
    "f14_bsss_080_tangible_equity_ratio_d2": {"inputs": ["equity", "intangibles", "assets"], "func": f14_bsss_080_tangible_equity_ratio_d2},
    "f14_bsss_081_tangible_book_to_total_book_d2": {"inputs": ["equity", "intangibles"], "func": f14_bsss_081_tangible_book_to_total_book_d2},
    "f14_bsss_082_neg_tangible_equity_flag_d2": {"inputs": ["equity", "intangibles"], "func": f14_bsss_082_neg_tangible_equity_flag_d2},
    "f14_bsss_083_intangibles_growth_yoy_d2": {"inputs": ["intangibles"], "func": f14_bsss_083_intangibles_growth_yoy_d2},
    "f14_bsss_084_intangibles_to_invcap_d2": {"inputs": ["intangibles", "invcap"], "func": f14_bsss_084_intangibles_to_invcap_d2},
    "f14_bsss_085_intangibles_minus_equity_impairment_proxy_d2": {"inputs": ["intangibles", "equity", "assets"], "func": f14_bsss_085_intangibles_minus_equity_impairment_proxy_d2},
    "f14_bsss_086_asset_quality_index_d2": {"inputs": ["assets", "assetsc", "ppnenet", "intangibles"], "func": f14_bsss_086_asset_quality_index_d2},
    "f14_bsss_087_ppnenet_to_assets_d2": {"inputs": ["ppnenet", "assets"], "func": f14_bsss_087_ppnenet_to_assets_d2},
    "f14_bsss_088_investments_to_assets_d2": {"inputs": ["investments", "assets"], "func": f14_bsss_088_investments_to_assets_d2},
    "f14_bsss_089_investments_to_liquid_assets_d2": {"inputs": ["investments", "cashneq"], "func": f14_bsss_089_investments_to_liquid_assets_d2},
    "f14_bsss_090_non_operating_asset_share_d2": {"inputs": ["assets", "ppnenet", "receivables", "inventory", "cashneq"], "func": f14_bsss_090_non_operating_asset_share_d2},
    "f14_bsss_091_retearn_to_equity_d2": {"inputs": ["retearn", "equity"], "func": f14_bsss_091_retearn_to_equity_d2},
    "f14_bsss_092_retearn_to_assets_d2": {"inputs": ["retearn", "assets"], "func": f14_bsss_092_retearn_to_assets_d2},
    "f14_bsss_093_negative_retearn_flag_d2": {"inputs": ["retearn"], "func": f14_bsss_093_negative_retearn_flag_d2},
    "f14_bsss_094_retearn_growth_yoy_assets_norm_d2": {"inputs": ["retearn", "assets"], "func": f14_bsss_094_retearn_growth_yoy_assets_norm_d2},
    "f14_bsss_095_sharefactor_drift_abs_d2": {"inputs": ["sharefactor"], "func": f14_bsss_095_sharefactor_drift_abs_d2},
    "f14_bsss_096_accoci_to_equity_d2": {"inputs": ["accoci", "equity"], "func": f14_bsss_096_accoci_to_equity_d2},
    "f14_bsss_097_accoci_to_assets_d2": {"inputs": ["accoci", "assets"], "func": f14_bsss_097_accoci_to_assets_d2},
    "f14_bsss_098_retained_burn_intensity_d2": {"inputs": ["retearn", "assets"], "func": f14_bsss_098_retained_burn_intensity_d2},
    "f14_bsss_099_equity_to_liabilities_d2": {"inputs": ["equity", "liabilities"], "func": f14_bsss_099_equity_to_liabilities_d2},
    "f14_bsss_100_equity_growth_yoy_d2": {"inputs": ["equity"], "func": f14_bsss_100_equity_growth_yoy_d2},
    "f14_bsss_101_equity_zscore_504d_d2": {"inputs": ["equity"], "func": f14_bsss_101_equity_zscore_504d_d2},
    "f14_bsss_102_paid_in_capital_proxy_d2": {"inputs": ["equity", "retearn", "accoci"], "func": f14_bsss_102_paid_in_capital_proxy_d2},
    "f14_bsss_103_paid_in_to_equity_d2": {"inputs": ["equity", "retearn", "accoci"], "func": f14_bsss_103_paid_in_to_equity_d2},
    "f14_bsss_104_retearn_to_paid_in_ratio_d2": {"inputs": ["retearn", "equity", "accoci"], "func": f14_bsss_104_retearn_to_paid_in_ratio_d2},
    "f14_bsss_105_neg_equity_flag_d2": {"inputs": ["equity"], "func": f14_bsss_105_neg_equity_flag_d2},
    "f14_bsss_106_ebitda_to_debt_d2": {"inputs": ["ebitda", "debt"], "func": f14_bsss_106_ebitda_to_debt_d2},
    "f14_bsss_107_ebit_to_debt_d2": {"inputs": ["ebit", "debt"], "func": f14_bsss_107_ebit_to_debt_d2},
    "f14_bsss_108_fcf_to_debt_d2": {"inputs": ["fcf", "debt"], "func": f14_bsss_108_fcf_to_debt_d2},
    "f14_bsss_109_cfo_to_debt_d2": {"inputs": ["ncfo", "debt"], "func": f14_bsss_109_cfo_to_debt_d2},
    "f14_bsss_110_ebitda_to_debtc_d2": {"inputs": ["ebitda", "debtc"], "func": f14_bsss_110_ebitda_to_debtc_d2},
    "f14_bsss_111_fcf_to_debtc_d2": {"inputs": ["fcf", "debtc"], "func": f14_bsss_111_fcf_to_debtc_d2},
    "f14_bsss_112_asset_turnover_d2": {"inputs": ["revenue", "assets"], "func": f14_bsss_112_asset_turnover_d2},
    "f14_bsss_113_asset_turnover_zscore_504d_d2": {"inputs": ["revenue", "assets"], "func": f14_bsss_113_asset_turnover_zscore_504d_d2},
    "f14_bsss_114_capex_to_ppne_d2": {"inputs": ["capex", "ppnenet"], "func": f14_bsss_114_capex_to_ppne_d2},
    "f14_bsss_115_capex_to_revenue_d2": {"inputs": ["capex", "revenue"], "func": f14_bsss_115_capex_to_revenue_d2},
    "f14_bsss_116_ppne_yoy_decay_d2": {"inputs": ["ppnenet"], "func": f14_bsss_116_ppne_yoy_decay_d2},
    "f14_bsss_117_roa_simple_d2": {"inputs": ["netinc", "assets"], "func": f14_bsss_117_roa_simple_d2},
    "f14_bsss_118_roe_simple_d2": {"inputs": ["netinc", "equity"], "func": f14_bsss_118_roe_simple_d2},
    "f14_bsss_119_roic_proxy_d2": {"inputs": ["netinc", "invcap"], "func": f14_bsss_119_roic_proxy_d2},
    "f14_bsss_120_cfo_to_revenue_d2": {"inputs": ["ncfo", "revenue"], "func": f14_bsss_120_cfo_to_revenue_d2},
    "f14_bsss_121_altman_x1_d2": {"inputs": ["workingcapital", "assets"], "func": f14_bsss_121_altman_x1_d2},
    "f14_bsss_122_altman_x2_d2": {"inputs": ["retearn", "assets"], "func": f14_bsss_122_altman_x2_d2},
    "f14_bsss_123_altman_x3_d2": {"inputs": ["ebit", "assets"], "func": f14_bsss_123_altman_x3_d2},
    "f14_bsss_124_altman_x4_book_d2": {"inputs": ["equity", "liabilities"], "func": f14_bsss_124_altman_x4_book_d2},
    "f14_bsss_125_altman_x5_d2": {"inputs": ["revenue", "assets"], "func": f14_bsss_125_altman_x5_d2},
    "f14_bsss_126_altman_z_full_d2": {"inputs": ["workingcapital", "retearn", "ebit", "equity", "liabilities", "revenue", "assets"], "func": f14_bsss_126_altman_z_full_d2},
    "f14_bsss_127_altman_z_prime_nonmfg_d2": {"inputs": ["workingcapital", "retearn", "ebit", "equity", "liabilities", "assets"], "func": f14_bsss_127_altman_z_prime_nonmfg_d2},
    "f14_bsss_128_beneish_dsri_d2": {"inputs": ["receivables", "revenue"], "func": f14_bsss_128_beneish_dsri_d2},
    "f14_bsss_129_beneish_aqi_d2": {"inputs": ["assets", "assetsc", "ppnenet", "intangibles"], "func": f14_bsss_129_beneish_aqi_d2},
    "f14_bsss_130_beneish_sgai_d2": {"inputs": ["sga", "revenue"], "func": f14_bsss_130_beneish_sgai_d2},
    "f14_bsss_131_beneish_tata_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f14_bsss_131_beneish_tata_d2},
    "f14_bsss_132_ohlson_tlta_flag_d2": {"inputs": ["liabilities", "assets"], "func": f14_bsss_132_ohlson_tlta_flag_d2},
    "f14_bsss_133_ohlson_chin_d2": {"inputs": ["netinc"], "func": f14_bsss_133_ohlson_chin_d2},
    "f14_bsss_134_ohlson_oneg_two_consecutive_d2": {"inputs": ["netinc"], "func": f14_bsss_134_ohlson_oneg_two_consecutive_d2},
    "f14_bsss_135_ohlson_tlta_ratio_d2": {"inputs": ["liabilities", "assets"], "func": f14_bsss_135_ohlson_tlta_ratio_d2},
    "f14_bsss_136_neg_equity_or_tangible_flag_d2": {"inputs": ["equity", "intangibles"], "func": f14_bsss_136_neg_equity_or_tangible_flag_d2},
    "f14_bsss_137_neg_workingcapital_flag_d2": {"inputs": ["workingcapital"], "func": f14_bsss_137_neg_workingcapital_flag_d2},
    "f14_bsss_138_neg_fcf_flag_d2": {"inputs": ["fcf"], "func": f14_bsss_138_neg_fcf_flag_d2},
    "f14_bsss_139_neg_cfo_flag_d2": {"inputs": ["ncfo"], "func": f14_bsss_139_neg_cfo_flag_d2},
    "f14_bsss_140_neg_netinc_flag_d2": {"inputs": ["netinc"], "func": f14_bsss_140_neg_netinc_flag_d2},
    "f14_bsss_141_distress_flag_count_d2": {"inputs": ["equity", "workingcapital", "fcf", "ncfo", "netinc"], "func": f14_bsss_141_distress_flag_count_d2},
    "f14_bsss_142_composite_z_leverage_d2": {"inputs": ["debt", "equity", "assets", "ebitda"], "func": f14_bsss_142_composite_z_leverage_d2},
    "f14_bsss_143_composite_z_liquidity_d2": {"inputs": ["assetsc", "liabilitiesc", "cashneq", "inventory"], "func": f14_bsss_143_composite_z_liquidity_d2},
    "f14_bsss_144_composite_z_solvency_d2": {"inputs": ["ebitda", "debt", "fcf", "ncfo"], "func": f14_bsss_144_composite_z_solvency_d2},
    "f14_bsss_145_composite_z_asset_quality_d2": {"inputs": ["intangibles", "assets", "ppnenet", "equity"], "func": f14_bsss_145_composite_z_asset_quality_d2},
    "f14_bsss_146_composite_z_dilution_dependence_d2": {"inputs": ["equity", "retearn", "accoci", "assets"], "func": f14_bsss_146_composite_z_dilution_dependence_d2},
    "f14_bsss_147_composite_z_accrual_quality_d2": {"inputs": ["netinc", "ncfo", "assets", "assetsc", "cashneq", "liabilitiesc"], "func": f14_bsss_147_composite_z_accrual_quality_d2},
    "f14_bsss_148_composite_z_ccc_stress_d2": {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"], "func": f14_bsss_148_composite_z_ccc_stress_d2},
    "f14_bsss_149_distance_to_distress_merton_lite_d2": {"inputs": ["equity", "debt"], "func": f14_bsss_149_distance_to_distress_merton_lite_d2},
    "f14_bsss_150_composite_z_balance_sheet_stress_d2": {"inputs": ["debt", "equity", "assets", "ebitda", "assetsc", "liabilitiesc", "cashneq", "inventory", "fcf", "ncfo", "intangibles", "retearn"], "func": f14_bsss_150_composite_z_balance_sheet_stress_d2},
}
