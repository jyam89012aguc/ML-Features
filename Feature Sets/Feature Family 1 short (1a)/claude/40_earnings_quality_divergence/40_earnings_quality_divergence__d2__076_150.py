"""earnings_quality_divergence d2 features 076-150 — second-derivative wrappers.

Each function inlines the corresponding base computation and appends .diff().diff()
to produce the second difference (acceleration) of that signal. Inputs and PIT discipline are identical to
__base__076_150.py.
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


def _winsorize(s, lo=0.01, hi=0.99):
    if not isinstance(s, pd.Series):
        return s
    ql = s.quantile(lo)
    qh = s.quantile(hi)
    return s.clip(lower=ql, upper=qh)


# ============================================================
#                    D2 FEATURES 076-150
# ============================================================

def f40_eqdg_076_eps_growth_minus_revenue_growth_yoy_d2(eps: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY EPS growth minus YoY Revenue growth — per-share quality wedge (buyback-aided)."""
    g_e = _safe_div(eps - eps.shift(YDAYS), eps.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return (g_e - g_r).diff().diff()


def f40_eqdg_077_gp_growth_minus_revenue_growth_yoy_d2(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY GrossProfit growth minus YoY Revenue growth — margin direction."""
    g_g = _safe_div(gp - gp.shift(YDAYS), gp.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return (g_g - g_r).diff().diff()


def f40_eqdg_078_netinc_growth_minus_revenue_growth_2y_d2(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y NI growth minus 2y Revenue growth — sustained earnings inflation vs sales."""
    win = 2 * YDAYS
    g_n = _safe_div(netinc - netinc.shift(win), netinc.shift(win).abs())
    g_r = _safe_div(revenue - revenue.shift(win), revenue.shift(win).abs())
    return (g_n - g_r).diff().diff()


def f40_eqdg_079_receivables_to_revenue_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """AR / Revenue level — receivables intensity."""
    return (_safe_div(receivables, revenue)).diff().diff()


def f40_eqdg_080_dreceivables_to_drevenue_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """dAR / dRevenue (YoY) — incremental AR per incremental sale, channel-stuffing proxy."""
    dar = receivables.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return (_safe_div(dar, dr)).diff().diff()


def f40_eqdg_081_dso_change_yoy_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Days Sales Outstanding YoY change (DSO_t - DSO_{t-1y})."""
    dso = _safe_div(receivables, revenue) * 365.0
    return (dso - dso.shift(YDAYS)).diff().diff()


def f40_eqdg_082_dso_zscore_12q_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """DSO z-score over 12q — abnormal AR-days extension."""
    dso = _safe_div(receivables, revenue) * 365.0
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = dso.rolling(win, min_periods=mp).mean()
    sd = dso.rolling(win, min_periods=mp).std()
    return (_safe_div(dso - m, sd)).diff().diff()


def f40_eqdg_083_receivables_growth_minus_revenue_growth_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY AR growth minus YoY Revenue growth — AR outpacing sales."""
    g_a = _safe_div(receivables - receivables.shift(YDAYS), receivables.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return (g_a - g_r).diff().diff()


def f40_eqdg_084_ar_growth_2y_minus_rev_growth_2y_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y AR growth minus 2y Revenue growth — multi-year AR build."""
    win = 2 * YDAYS
    g_a = _safe_div(receivables - receivables.shift(win), receivables.shift(win).abs())
    g_r = _safe_div(revenue - revenue.shift(win), revenue.shift(win).abs())
    return (g_a - g_r).diff().diff()


def f40_eqdg_085_dso_trend_slope_8q_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Slope of (DSO - 8q_mean(DSO)) regressed on linear time — DSO trend."""
    dso = _safe_div(receivables, revenue) * 365.0
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    m = dso.rolling(win, min_periods=mp).mean()
    return ((dso - m) / float(win)).diff().diff()


def f40_eqdg_086_receivables_share_of_dassets_d2(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """dAR / dAssets (YoY) — share of asset growth driven by AR."""
    dar = receivables.diff(YDAYS)
    da = assets.diff(YDAYS)
    return (_safe_div(dar, da)).diff().diff()


def f40_eqdg_087_inventory_to_revenue_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory / Revenue — inventory intensity."""
    return (_safe_div(inventory, revenue)).diff().diff()


def f40_eqdg_088_dinventory_to_drevenue_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """dInv / dRevenue (YoY) — incremental inventory per dollar of incremental sales."""
    di = inventory.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return (_safe_div(di, dr)).diff().diff()


def f40_eqdg_089_dio_change_yoy_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Days Inventory Outstanding YoY change."""
    dio = _safe_div(inventory, cor) * 365.0
    return (dio - dio.shift(YDAYS)).diff().diff()


def f40_eqdg_090_dio_zscore_12q_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """DIO z-score over 12q — abnormal inventory build."""
    dio = _safe_div(inventory, cor) * 365.0
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = dio.rolling(win, min_periods=mp).mean()
    sd = dio.rolling(win, min_periods=mp).std()
    return (_safe_div(dio - m, sd)).diff().diff()


def f40_eqdg_091_inv_growth_minus_revenue_growth_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY Inventory growth minus YoY Revenue growth — channel-stuffing on inventory."""
    g_i = _safe_div(inventory - inventory.shift(YDAYS), inventory.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return (g_i - g_r).diff().diff()


def f40_eqdg_092_inv_share_of_dassets_d2(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """dInv / dAssets (YoY) — share of asset growth from inventory build."""
    di = inventory.diff(YDAYS)
    da = assets.diff(YDAYS)
    return (_safe_div(di, da)).diff().diff()


def f40_eqdg_093_deferredrev_to_revenue_d2(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """Deferred revenue / Revenue — billings ahead of recognition."""
    return (_safe_div(deferredrev, revenue)).diff().diff()


def f40_eqdg_094_ddeferredrev_to_revenue_d2(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """dDeferredRev (YoY) / Revenue — change in billings vs revenue scale."""
    dd = deferredrev.diff(YDAYS)
    return (_safe_div(dd, revenue)).diff().diff()


def f40_eqdg_095_defrev_growth_minus_revenue_growth_d2(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY DefRev growth minus YoY Revenue growth — billings deceleration signal when negative."""
    g_d = _safe_div(deferredrev - deferredrev.shift(YDAYS), deferredrev.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return (g_d - g_r).diff().diff()


def f40_eqdg_096_defrev_to_revenue_zscore_12q_d2(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """z-score of DefRev/Revenue over 12q — extreme billings vs recognition."""
    r = _safe_div(deferredrev, revenue)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = r.rolling(win, min_periods=mp).mean()
    sd = r.rolling(win, min_periods=mp).std()
    return (_safe_div(r - m, sd)).diff().diff()


def f40_eqdg_097_nonop_income_share_d2(netinc: pd.Series, ebit: pd.Series, taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """(NetInc - EBIT*(1 - tax_rate)) / NetInc — non-operating share of net income."""
    etr = _safe_div(taxexp, ebt)
    ebit_at = ebit * (1.0 - etr)
    return (_safe_div(netinc - ebit_at, netinc.abs())).diff().diff()


def f40_eqdg_098_ebit_minus_netinc_to_revenue_d2(ebit: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """(EBIT - NetInc) / Revenue — non-op + tax wedge scaled by sales."""
    return (_safe_div(ebit - netinc, revenue)).diff().diff()


def f40_eqdg_099_ebit_to_netinc_ratio_d2(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """EBIT / NetInc — operating vs total earnings ratio."""
    return (_safe_div(ebit, netinc)).diff().diff()


def f40_eqdg_100_nonop_other_income_share_d2(netinc: pd.Series, ebit: pd.Series) -> pd.Series:
    """(NetInc - EBIT) / |EBIT| — earnings boost beyond operations (signed)."""
    return (_safe_div(netinc - ebit, ebit.abs())).diff().diff()


def f40_eqdg_101_ebt_minus_ebit_to_revenue_d2(ebt: pd.Series, ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """(EBT - EBIT) / Revenue — financing + non-op items intensity."""
    return (_safe_div(ebt - ebit, revenue)).diff().diff()


def f40_eqdg_102_pretax_to_post_tax_consistency_d2(ebt: pd.Series, netinc: pd.Series) -> pd.Series:
    """NetInc / EBT — implied (1 - ETR). Sudden spike = tax-driven earnings."""
    return (_safe_div(netinc, ebt)).diff().diff()


def f40_eqdg_103_netinc_minus_ebit_after_tax_spike_zscore_d2(netinc: pd.Series, ebit: pd.Series, taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """z-score over 12q of (NetInc - EBIT*(1 - ETR)) — special-item spike detector."""
    etr = _safe_div(taxexp, ebt)
    diff = netinc - ebit * (1.0 - etr)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = diff.rolling(win, min_periods=mp).mean()
    sd = diff.rolling(win, min_periods=mp).std()
    return (_safe_div(diff - m, sd)).diff().diff()


def f40_eqdg_104_ebit_ebitda_gap_zscore_d2(ebitda: pd.Series, ebit: pd.Series) -> pd.Series:
    """z-score of (EBITDA - EBIT) = D&A — spike detector for amortization/write-downs."""
    gap = ebitda - ebit
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = gap.rolling(win, min_periods=mp).mean()
    sd = gap.rolling(win, min_periods=mp).std()
    return (_safe_div(gap - m, sd)).diff().diff()


def f40_eqdg_105_special_items_proxy_residual_d2(netinc: pd.Series, ebit: pd.Series, taxexp: pd.Series) -> pd.Series:
    """NetInc - (EBIT - TaxExp) — residual items beyond pure operating-after-tax."""
    return (netinc - (ebit - taxexp)).diff().diff()


def f40_eqdg_106_gp_minus_ebit_gap_anomaly_d2(gp: pd.Series, ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """(GP - EBIT) / Revenue — operating overhead burden anomaly vs sales."""
    return (_safe_div(gp - ebit, revenue)).diff().diff()


def f40_eqdg_107_gross_margin_cv_8q_d2(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """8q coefficient of variation of GM = std/|mean|."""
    gm = _safe_div(revenue - cor, revenue)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    return (_safe_div(gm.rolling(win, min_periods=mp).std(), gm.rolling(win, min_periods=mp).mean().abs())).diff().diff()


def f40_eqdg_108_gross_margin_smoothness_vs_revenue_d2(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """GM-std / Revenue-CV ratio over 8q — GM smoother than sales = managed."""
    gm = _safe_div(revenue - cor, revenue)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    gm_sd = gm.rolling(win, min_periods=mp).std()
    rv_cv = _safe_div(revenue.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).mean().abs())
    return (_safe_div(gm_sd, rv_cv)).diff().diff()


def f40_eqdg_109_gm_residual_from_revenue_regression_d2(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """GM minus its 8q linear-trend estimate (mean) — instantaneous GM anomaly."""
    gm = _safe_div(revenue - cor, revenue)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    m = gm.rolling(win, min_periods=mp).mean()
    return (gm - m).diff().diff()


def f40_eqdg_110_gm_rolling_skew_12q_d2(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """12q rolling skew of GM — asymmetric margin manipulation."""
    gm = _safe_div(revenue - cor, revenue)
    win = 12 * QDAYS
    return (gm.rolling(win, min_periods=max(win // 3, QDAYS)).skew()).diff().diff()


def f40_eqdg_111_netinc_zscore_minus_fcf_zscore_12q_d2(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """z(NetInc) - z(FCF) over 12q — accounting earnings extreme vs cash extreme."""
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    n_z = _safe_div(netinc - netinc.rolling(win, min_periods=mp).mean(), netinc.rolling(win, min_periods=mp).std())
    f_z = _safe_div(fcf - fcf.rolling(win, min_periods=mp).mean(), fcf.rolling(win, min_periods=mp).std())
    return (n_z - f_z).diff().diff()


def f40_eqdg_112_netinc_zscore_minus_cfo_zscore_12q_d2(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """z(NetInc) - z(CFO) over 12q — accounting vs operating-cash extreme."""
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    n_z = _safe_div(netinc - netinc.rolling(win, min_periods=mp).mean(), netinc.rolling(win, min_periods=mp).std())
    c_z = _safe_div(ncfo - ncfo.rolling(win, min_periods=mp).mean(), ncfo.rolling(win, min_periods=mp).std())
    return (n_z - c_z).diff().diff()


def f40_eqdg_113_eps_zscore_minus_fcf_per_share_zscore_12q_d2(eps: pd.Series, fcf: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """z(EPS) - z(FCF per diluted share) — per-share quality divergence."""
    fcfps = _safe_div(fcf, shareswadil)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    e_z = _safe_div(eps - eps.rolling(win, min_periods=mp).mean(), eps.rolling(win, min_periods=mp).std())
    f_z = _safe_div(fcfps - fcfps.rolling(win, min_periods=mp).mean(), fcfps.rolling(win, min_periods=mp).std())
    return (e_z - f_z).diff().diff()


def f40_eqdg_114_ni_fcf_divergence_blended_8q_d2(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Blended 8q divergence: rank-diff + z-diff midpoint of NI vs FCF."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    n_z = _safe_div(netinc - netinc.rolling(win, min_periods=mp).mean(), netinc.rolling(win, min_periods=mp).std())
    f_z = _safe_div(fcf - fcf.rolling(win, min_periods=mp).mean(), fcf.rolling(win, min_periods=mp).std())
    n_r = netinc.rolling(win, min_periods=mp).rank(pct=True)
    f_r = fcf.rolling(win, min_periods=mp).rank(pct=True)
    return (0.5 * (n_z - f_z) + 0.5 * (n_r - f_r)).diff().diff()


def f40_eqdg_115_rolling_corr_ni_fcf_8q_d2(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """8q rolling correlation of NetInc vs FCF — low/negative = quality break."""
    win = 8 * QDAYS
    return (netinc.rolling(win, min_periods=max(win // 3, QDAYS)).corr(fcf)).diff().diff()


def f40_eqdg_116_rolling_corr_ni_cfo_8q_d2(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """8q rolling correlation of NetInc vs CFO."""
    win = 8 * QDAYS
    return (netinc.rolling(win, min_periods=max(win // 3, QDAYS)).corr(ncfo)).diff().diff()


def f40_eqdg_117_wc_delta_to_revenue_delta_ratio_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """dWC / dRevenue (YoY) — capital intensity per dollar of incremental sales."""
    dwc = workingcapital.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return (_safe_div(dwc, dr)).diff().diff()


def f40_eqdg_118_wc_to_revenue_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """WC / Revenue — capital tie-up in operations."""
    return (_safe_div(workingcapital, revenue)).diff().diff()


def f40_eqdg_119_dwc_share_of_dassets_d2(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """dWC / dAssets (YoY) — share of asset growth from WC build."""
    dwc = workingcapital.diff(YDAYS)
    da = assets.diff(YDAYS)
    return (_safe_div(dwc, da)).diff().diff()


def f40_eqdg_120_wc_volatility_vs_revenue_d2(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """8q std(WC) / 8q std(Revenue) — WC volatility relative to top-line."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    return (_safe_div(workingcapital.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).std())).diff().diff()


def f40_eqdg_121_quality_composite_v1_d2(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, fcf: pd.Series) -> pd.Series:
    """v1 = z(Sloan accruals) - z(FCF/Assets) — higher = worse quality."""
    sl = _safe_div(netinc - ncfo, assets)
    fa = _safe_div(fcf, assets)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    sl_z = _safe_div(sl - sl.rolling(win, min_periods=mp).mean(), sl.rolling(win, min_periods=mp).std())
    fa_z = _safe_div(fa - fa.rolling(win, min_periods=mp).mean(), fa.rolling(win, min_periods=mp).std())
    return (sl_z - fa_z).diff().diff()


def f40_eqdg_122_quality_composite_v2_d2(ncfo: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """v2 = (1 - CFO/NI) + z(NI smoothness vs Rev) — cash-conv + smoothness blend."""
    nce = 1.0 - _safe_div(ncfo, netinc)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    ni_cv = _safe_div(netinc.rolling(win, min_periods=mp).std(), netinc.rolling(win, min_periods=mp).mean().abs())
    rv_cv = _safe_div(revenue.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).mean().abs())
    sm = _safe_div(ni_cv, rv_cv)
    return (nce - sm).diff().diff()


def f40_eqdg_123_aggressive_revenue_recognition_composite_d2(receivables: pd.Series, deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """(AR/Rev YoY change) + (-dDefRev/Rev) — aggressive recognition compounding."""
    dso_chg = _safe_div(receivables, revenue) - _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS))
    drd = -_safe_div(deferredrev.diff(YDAYS), revenue)
    return (dso_chg + drd).diff().diff()


def f40_eqdg_124_cash_quality_composite_d2(ncfo: pd.Series, fcf: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of CFO/NI, FCF/NI, FCF/Rev, CFO/Rev — average cash-conversion intensity."""
    a = _safe_div(ncfo, netinc)
    b = _safe_div(fcf, netinc)
    c = _safe_div(fcf, revenue)
    d = _safe_div(ncfo, revenue)
    return ((a + b + c + d) / 4.0).diff().diff()


def f40_eqdg_125_persistence_quality_composite_d2(netinc: pd.Series, eps: pd.Series) -> pd.Series:
    """Mean of NI and EPS AR(1)-proxy autocorrelations over 8q."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    def _ac(s):
        lag = s.shift(QDAYS)
        nm = s.rolling(win, min_periods=mp).mean()
        lm = lag.rolling(win, min_periods=mp).mean()
        cov = ((s - nm) * (lag - lm)).rolling(win, min_periods=mp).mean()
        ss = s.rolling(win, min_periods=mp).std()
        sl = lag.rolling(win, min_periods=mp).std()
        return _safe_div(cov, ss * sl)
    return ((_ac(netinc) + _ac(eps)) / 2.0).diff().diff()


def f40_eqdg_126_noncash_inflation_composite_d2(sbcomp: pd.Series, depamor: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """(SBC + D&A) / max(EBITDA, |NI|) — total non-cash earnings inflation share."""
    den = pd.concat([ebitda, netinc.abs()], axis=1).max(axis=1)
    return (_safe_div(sbcomp + depamor, den)).diff().diff()


def f40_eqdg_127_receivables_quality_composite_d2(receivables: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Composite: z(DSO) + dAR/dAssets — receivables-quality red-flag blend."""
    dso = _safe_div(receivables, revenue) * 365.0
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    z = _safe_div(dso - dso.rolling(win, min_periods=mp).mean(), dso.rolling(win, min_periods=mp).std())
    share = _safe_div(receivables.diff(YDAYS), assets.diff(YDAYS))
    return (z + share).diff().diff()


def f40_eqdg_128_composite_total_quality_score_d2(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, sbcomp: pd.Series, receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Composite total quality: Sloan + SBC/Rev + DSO_yoy_chg — sum of three rotated red flags."""
    sl = _safe_div(netinc - ncfo, assets)
    sbc_r = _safe_div(sbcomp, revenue)
    dso = _safe_div(receivables, revenue) * 365.0
    return (sl + sbc_r + (dso - dso.shift(YDAYS))).diff().diff()


def f40_eqdg_129_composite_red_flag_count_d2(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, sbcomp: pd.Series, receivables: pd.Series, revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Count of fired red flags: Sloan>0.10, SBC/Rev>0.05, NI>0 & FCF<0, dDSO>30, |CFO|<|NI|."""
    sl = _safe_div(netinc - ncfo, assets)
    sbc_r = _safe_div(sbcomp, revenue)
    dso = _safe_div(receivables, revenue) * 365.0
    ddso = dso - dso.shift(YDAYS)
    f1 = (sl > 0.1).astype(float)
    f2 = (sbc_r > 0.05).astype(float)
    f3 = ((netinc > 0) & (fcf < 0)).astype(float)
    f4 = (ddso > 30.0).astype(float)
    f5 = (ncfo.abs() < netinc.abs()).astype(float)
    return (f1 + f2 + f3 + f4 + f5).diff().diff()


def f40_eqdg_130_quality_residual_blend_d2(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """(NI - CFO - SBC) / Revenue — residual non-cash earnings after stripping SBC."""
    return (_safe_div(netinc - ncfo - sbcomp, revenue)).diff().diff()


def f40_eqdg_131_capex_to_revenue_stickiness_8q_std_d2(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """8q std of |capex|/Revenue — capex volatility vs sales (high = inconsistent reinvestment)."""
    r = _safe_div(capex.abs(), revenue)
    return (r.rolling(8 * QDAYS, min_periods=2 * QDAYS).std()).diff().diff()


def f40_eqdg_132_capex_to_cfo_d2(capex: pd.Series, ncfo: pd.Series) -> pd.Series:
    """|capex| / CFO — reinvestment intensity relative to cash generation."""
    return (_safe_div(capex.abs(), ncfo)).diff().diff()


def f40_eqdg_133_capex_to_depamor_zscore_12q_d2(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """z-score of |capex|/D&A over 12q — extreme over/under-investment."""
    r = _safe_div(capex.abs(), depamor)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = r.rolling(win, min_periods=mp).mean()
    sd = r.rolling(win, min_periods=mp).std()
    return (_safe_div(r - m, sd)).diff().diff()


def f40_eqdg_134_wc_bloat_minus_capex_underinvestment_d2(workingcapital: pd.Series, capex: pd.Series, depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """(dWC/Rev) - ((|capex| - D&A)/Rev) — WC bloat + capex underinvestment combined."""
    dwc_r = _safe_div(workingcapital.diff(YDAYS), revenue)
    cx_r = _safe_div(capex.abs() - depamor, revenue)
    return (dwc_r - cx_r).diff().diff()


def f40_eqdg_135_cfo_neg_while_ni_pos_flag_d2(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Indicator: CFO < 0 AND NetInc > 0 — classic accrual red flag."""
    flag = (ncfo < 0) & (netinc > 0)
    out = flag.astype(float)
    return (out.where(netinc.notna() & ncfo.notna(), np.nan)).diff().diff()


def f40_eqdg_136_sbc_exceeds_netinc_flag_d2(sbcomp: pd.Series, netinc: pd.Series) -> pd.Series:
    """Indicator: SBC > NetInc (when NI > 0) — earnings entirely paid in dilution."""
    flag = (sbcomp > netinc) & (netinc > 0)
    out = flag.astype(float)
    return (out.where(sbcomp.notna() & netinc.notna(), np.nan)).diff().diff()


def f40_eqdg_137_accruals_top_decile_flag_d2(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: Sloan accruals > 12q-rolling 90th percentile — extreme accrual flag."""
    sl = _safe_div(netinc - ncfo, assets)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    q90 = sl.rolling(win, min_periods=mp).quantile(0.9)
    flag = sl > q90
    out = flag.astype(float)
    return (out.where(sl.notna() & q90.notna(), np.nan)).diff().diff()


def f40_eqdg_138_dso_jumped_flag_d2(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Indicator: DSO YoY change > +30 days — channel-stuffing burst flag."""
    dso = _safe_div(receivables, revenue) * 365.0
    chg = dso - dso.shift(YDAYS)
    out = (chg > 30.0).astype(float)
    return (out.where(chg.notna(), np.nan)).diff().diff()


def f40_eqdg_139_dio_jumped_flag_d2(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Indicator: DIO YoY change > +30 days — inventory build flag."""
    dio = _safe_div(inventory, cor) * 365.0
    chg = dio - dio.shift(YDAYS)
    out = (chg > 30.0).astype(float)
    return (out.where(chg.notna(), np.nan)).diff().diff()


def f40_eqdg_140_high_noncash_earnings_flag_d2(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Indicator: (NI - CFO)/|NI| > 0.5 — majority of earnings is non-cash."""
    nce = _safe_div(netinc - ncfo, netinc.abs())
    out = (nce > 0.5).astype(float)
    return (out.where(nce.notna(), np.nan)).diff().diff()


def f40_eqdg_141_fcf_coverage_of_netinc_d2(ncfo: pd.Series, capex: pd.Series, netinc: pd.Series) -> pd.Series:
    """(CFO - |capex|) / NetInc — FCF coverage of accounting earnings."""
    return (_safe_div(ncfo - capex.abs(), netinc)).diff().diff()


def f40_eqdg_142_sga_to_revenue_quality_d2(sga: pd.Series, revenue: pd.Series) -> pd.Series:
    """SGA / Revenue — overhead intensity (rising = quality erosion)."""
    return (_safe_div(sga, revenue)).diff().diff()


def f40_eqdg_143_rnd_to_revenue_capitalization_proxy_d2(rnd: pd.Series, revenue: pd.Series, intangibles: pd.Series) -> pd.Series:
    """RnD/Revenue minus (dIntangibles/Revenue) — net expensed R&D adjusting for capitalized intangibles."""
    rd_r = _safe_div(rnd, revenue)
    cap_r = _safe_div(intangibles.diff(YDAYS), revenue)
    return (rd_r - cap_r).diff().diff()


def f40_eqdg_144_opex_to_revenue_efficiency_d2(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """OpEx / Revenue — operating efficiency (rising = quality risk)."""
    return (_safe_div(opex, revenue)).diff().diff()


def f40_eqdg_145_retearn_growth_vs_netinc_consistency_d2(retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """dRetEarn (YoY) / NetInc_sum_4q — retained-earnings flow vs trailing earnings sum."""
    dre = retearn.diff(YDAYS)
    ni_sum = netinc.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(dre, ni_sum)).diff().diff()


def f40_eqdg_146_equity_quality_accoci_share_d2(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """AOCI / Equity — accumulated other comprehensive income share of equity (FX/MTM noise)."""
    return (_safe_div(accoci, equity)).diff().diff()


def f40_eqdg_147_intangibles_to_assets_quality_d2(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Intangibles / Assets — soft asset share."""
    return (_safe_div(intangibles, assets)).diff().diff()


def f40_eqdg_148_investments_to_assets_d2(investments: pd.Series, assets: pd.Series) -> pd.Series:
    """Investments / Assets — non-operating capital allocation."""
    return (_safe_div(investments, assets)).diff().diff()


def f40_eqdg_149_ncfcommon_share_of_ncff_d2(ncfcommon: pd.Series, ncff: pd.Series) -> pd.Series:
    """|NCFCommon| / |NCFF| — equity issuance/buyback share of financing flows."""
    return (_safe_div(ncfcommon.abs(), ncff.abs())).diff().diff()


def f40_eqdg_150_ncfdebt_minus_ncfcommon_to_assets_d2(ncfdebt: pd.Series, ncfcommon: pd.Series, assets: pd.Series) -> pd.Series:
    """(NCFDebt - NCFCommon) / Assets — debt-vs-equity financing mix per asset base."""
    return (_safe_div(ncfdebt - ncfcommon, assets)).diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

EARNINGS_QUALITY_DIVERGENCE_D2_REGISTRY_076_150 = {
    "f40_eqdg_076_eps_growth_minus_revenue_growth_yoy_d2": {"inputs": ['eps', 'revenue'], "func": f40_eqdg_076_eps_growth_minus_revenue_growth_yoy_d2},
    "f40_eqdg_077_gp_growth_minus_revenue_growth_yoy_d2": {"inputs": ['gp', 'revenue'], "func": f40_eqdg_077_gp_growth_minus_revenue_growth_yoy_d2},
    "f40_eqdg_078_netinc_growth_minus_revenue_growth_2y_d2": {"inputs": ['netinc', 'revenue'], "func": f40_eqdg_078_netinc_growth_minus_revenue_growth_2y_d2},
    "f40_eqdg_079_receivables_to_revenue_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_079_receivables_to_revenue_d2},
    "f40_eqdg_080_dreceivables_to_drevenue_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_080_dreceivables_to_drevenue_d2},
    "f40_eqdg_081_dso_change_yoy_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_081_dso_change_yoy_d2},
    "f40_eqdg_082_dso_zscore_12q_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_082_dso_zscore_12q_d2},
    "f40_eqdg_083_receivables_growth_minus_revenue_growth_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_083_receivables_growth_minus_revenue_growth_d2},
    "f40_eqdg_084_ar_growth_2y_minus_rev_growth_2y_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_084_ar_growth_2y_minus_rev_growth_2y_d2},
    "f40_eqdg_085_dso_trend_slope_8q_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_085_dso_trend_slope_8q_d2},
    "f40_eqdg_086_receivables_share_of_dassets_d2": {"inputs": ['receivables', 'assets'], "func": f40_eqdg_086_receivables_share_of_dassets_d2},
    "f40_eqdg_087_inventory_to_revenue_d2": {"inputs": ['inventory', 'revenue'], "func": f40_eqdg_087_inventory_to_revenue_d2},
    "f40_eqdg_088_dinventory_to_drevenue_d2": {"inputs": ['inventory', 'revenue'], "func": f40_eqdg_088_dinventory_to_drevenue_d2},
    "f40_eqdg_089_dio_change_yoy_d2": {"inputs": ['inventory', 'cor'], "func": f40_eqdg_089_dio_change_yoy_d2},
    "f40_eqdg_090_dio_zscore_12q_d2": {"inputs": ['inventory', 'cor'], "func": f40_eqdg_090_dio_zscore_12q_d2},
    "f40_eqdg_091_inv_growth_minus_revenue_growth_d2": {"inputs": ['inventory', 'revenue'], "func": f40_eqdg_091_inv_growth_minus_revenue_growth_d2},
    "f40_eqdg_092_inv_share_of_dassets_d2": {"inputs": ['inventory', 'assets'], "func": f40_eqdg_092_inv_share_of_dassets_d2},
    "f40_eqdg_093_deferredrev_to_revenue_d2": {"inputs": ['deferredrev', 'revenue'], "func": f40_eqdg_093_deferredrev_to_revenue_d2},
    "f40_eqdg_094_ddeferredrev_to_revenue_d2": {"inputs": ['deferredrev', 'revenue'], "func": f40_eqdg_094_ddeferredrev_to_revenue_d2},
    "f40_eqdg_095_defrev_growth_minus_revenue_growth_d2": {"inputs": ['deferredrev', 'revenue'], "func": f40_eqdg_095_defrev_growth_minus_revenue_growth_d2},
    "f40_eqdg_096_defrev_to_revenue_zscore_12q_d2": {"inputs": ['deferredrev', 'revenue'], "func": f40_eqdg_096_defrev_to_revenue_zscore_12q_d2},
    "f40_eqdg_097_nonop_income_share_d2": {"inputs": ['netinc', 'ebit', 'taxexp', 'ebt'], "func": f40_eqdg_097_nonop_income_share_d2},
    "f40_eqdg_098_ebit_minus_netinc_to_revenue_d2": {"inputs": ['ebit', 'netinc', 'revenue'], "func": f40_eqdg_098_ebit_minus_netinc_to_revenue_d2},
    "f40_eqdg_099_ebit_to_netinc_ratio_d2": {"inputs": ['ebit', 'netinc'], "func": f40_eqdg_099_ebit_to_netinc_ratio_d2},
    "f40_eqdg_100_nonop_other_income_share_d2": {"inputs": ['netinc', 'ebit'], "func": f40_eqdg_100_nonop_other_income_share_d2},
    "f40_eqdg_101_ebt_minus_ebit_to_revenue_d2": {"inputs": ['ebt', 'ebit', 'revenue'], "func": f40_eqdg_101_ebt_minus_ebit_to_revenue_d2},
    "f40_eqdg_102_pretax_to_post_tax_consistency_d2": {"inputs": ['ebt', 'netinc'], "func": f40_eqdg_102_pretax_to_post_tax_consistency_d2},
    "f40_eqdg_103_netinc_minus_ebit_after_tax_spike_zscore_d2": {"inputs": ['netinc', 'ebit', 'taxexp', 'ebt'], "func": f40_eqdg_103_netinc_minus_ebit_after_tax_spike_zscore_d2},
    "f40_eqdg_104_ebit_ebitda_gap_zscore_d2": {"inputs": ['ebitda', 'ebit'], "func": f40_eqdg_104_ebit_ebitda_gap_zscore_d2},
    "f40_eqdg_105_special_items_proxy_residual_d2": {"inputs": ['netinc', 'ebit', 'taxexp'], "func": f40_eqdg_105_special_items_proxy_residual_d2},
    "f40_eqdg_106_gp_minus_ebit_gap_anomaly_d2": {"inputs": ['gp', 'ebit', 'revenue'], "func": f40_eqdg_106_gp_minus_ebit_gap_anomaly_d2},
    "f40_eqdg_107_gross_margin_cv_8q_d2": {"inputs": ['revenue', 'cor'], "func": f40_eqdg_107_gross_margin_cv_8q_d2},
    "f40_eqdg_108_gross_margin_smoothness_vs_revenue_d2": {"inputs": ['revenue', 'cor'], "func": f40_eqdg_108_gross_margin_smoothness_vs_revenue_d2},
    "f40_eqdg_109_gm_residual_from_revenue_regression_d2": {"inputs": ['revenue', 'cor'], "func": f40_eqdg_109_gm_residual_from_revenue_regression_d2},
    "f40_eqdg_110_gm_rolling_skew_12q_d2": {"inputs": ['revenue', 'cor'], "func": f40_eqdg_110_gm_rolling_skew_12q_d2},
    "f40_eqdg_111_netinc_zscore_minus_fcf_zscore_12q_d2": {"inputs": ['netinc', 'fcf'], "func": f40_eqdg_111_netinc_zscore_minus_fcf_zscore_12q_d2},
    "f40_eqdg_112_netinc_zscore_minus_cfo_zscore_12q_d2": {"inputs": ['netinc', 'ncfo'], "func": f40_eqdg_112_netinc_zscore_minus_cfo_zscore_12q_d2},
    "f40_eqdg_113_eps_zscore_minus_fcf_per_share_zscore_12q_d2": {"inputs": ['eps', 'fcf', 'shareswadil'], "func": f40_eqdg_113_eps_zscore_minus_fcf_per_share_zscore_12q_d2},
    "f40_eqdg_114_ni_fcf_divergence_blended_8q_d2": {"inputs": ['netinc', 'fcf'], "func": f40_eqdg_114_ni_fcf_divergence_blended_8q_d2},
    "f40_eqdg_115_rolling_corr_ni_fcf_8q_d2": {"inputs": ['netinc', 'fcf'], "func": f40_eqdg_115_rolling_corr_ni_fcf_8q_d2},
    "f40_eqdg_116_rolling_corr_ni_cfo_8q_d2": {"inputs": ['netinc', 'ncfo'], "func": f40_eqdg_116_rolling_corr_ni_cfo_8q_d2},
    "f40_eqdg_117_wc_delta_to_revenue_delta_ratio_d2": {"inputs": ['workingcapital', 'revenue'], "func": f40_eqdg_117_wc_delta_to_revenue_delta_ratio_d2},
    "f40_eqdg_118_wc_to_revenue_d2": {"inputs": ['workingcapital', 'revenue'], "func": f40_eqdg_118_wc_to_revenue_d2},
    "f40_eqdg_119_dwc_share_of_dassets_d2": {"inputs": ['workingcapital', 'assets'], "func": f40_eqdg_119_dwc_share_of_dassets_d2},
    "f40_eqdg_120_wc_volatility_vs_revenue_d2": {"inputs": ['workingcapital', 'revenue'], "func": f40_eqdg_120_wc_volatility_vs_revenue_d2},
    "f40_eqdg_121_quality_composite_v1_d2": {"inputs": ['netinc', 'ncfo', 'assets', 'fcf'], "func": f40_eqdg_121_quality_composite_v1_d2},
    "f40_eqdg_122_quality_composite_v2_d2": {"inputs": ['ncfo', 'netinc', 'revenue'], "func": f40_eqdg_122_quality_composite_v2_d2},
    "f40_eqdg_123_aggressive_revenue_recognition_composite_d2": {"inputs": ['receivables', 'deferredrev', 'revenue'], "func": f40_eqdg_123_aggressive_revenue_recognition_composite_d2},
    "f40_eqdg_124_cash_quality_composite_d2": {"inputs": ['ncfo', 'fcf', 'netinc', 'revenue'], "func": f40_eqdg_124_cash_quality_composite_d2},
    "f40_eqdg_125_persistence_quality_composite_d2": {"inputs": ['netinc', 'eps'], "func": f40_eqdg_125_persistence_quality_composite_d2},
    "f40_eqdg_126_noncash_inflation_composite_d2": {"inputs": ['sbcomp', 'depamor', 'ebitda', 'netinc'], "func": f40_eqdg_126_noncash_inflation_composite_d2},
    "f40_eqdg_127_receivables_quality_composite_d2": {"inputs": ['receivables', 'revenue', 'assets'], "func": f40_eqdg_127_receivables_quality_composite_d2},
    "f40_eqdg_128_composite_total_quality_score_d2": {"inputs": ['netinc', 'ncfo', 'assets', 'sbcomp', 'receivables', 'revenue'], "func": f40_eqdg_128_composite_total_quality_score_d2},
    "f40_eqdg_129_composite_red_flag_count_d2": {"inputs": ['netinc', 'ncfo', 'assets', 'sbcomp', 'receivables', 'revenue', 'fcf'], "func": f40_eqdg_129_composite_red_flag_count_d2},
    "f40_eqdg_130_quality_residual_blend_d2": {"inputs": ['netinc', 'ncfo', 'revenue', 'sbcomp'], "func": f40_eqdg_130_quality_residual_blend_d2},
    "f40_eqdg_131_capex_to_revenue_stickiness_8q_std_d2": {"inputs": ['capex', 'revenue'], "func": f40_eqdg_131_capex_to_revenue_stickiness_8q_std_d2},
    "f40_eqdg_132_capex_to_cfo_d2": {"inputs": ['capex', 'ncfo'], "func": f40_eqdg_132_capex_to_cfo_d2},
    "f40_eqdg_133_capex_to_depamor_zscore_12q_d2": {"inputs": ['capex', 'depamor'], "func": f40_eqdg_133_capex_to_depamor_zscore_12q_d2},
    "f40_eqdg_134_wc_bloat_minus_capex_underinvestment_d2": {"inputs": ['workingcapital', 'capex', 'depamor', 'revenue'], "func": f40_eqdg_134_wc_bloat_minus_capex_underinvestment_d2},
    "f40_eqdg_135_cfo_neg_while_ni_pos_flag_d2": {"inputs": ['netinc', 'ncfo'], "func": f40_eqdg_135_cfo_neg_while_ni_pos_flag_d2},
    "f40_eqdg_136_sbc_exceeds_netinc_flag_d2": {"inputs": ['sbcomp', 'netinc'], "func": f40_eqdg_136_sbc_exceeds_netinc_flag_d2},
    "f40_eqdg_137_accruals_top_decile_flag_d2": {"inputs": ['netinc', 'ncfo', 'assets'], "func": f40_eqdg_137_accruals_top_decile_flag_d2},
    "f40_eqdg_138_dso_jumped_flag_d2": {"inputs": ['receivables', 'revenue'], "func": f40_eqdg_138_dso_jumped_flag_d2},
    "f40_eqdg_139_dio_jumped_flag_d2": {"inputs": ['inventory', 'cor'], "func": f40_eqdg_139_dio_jumped_flag_d2},
    "f40_eqdg_140_high_noncash_earnings_flag_d2": {"inputs": ['ncfo', 'netinc'], "func": f40_eqdg_140_high_noncash_earnings_flag_d2},
    "f40_eqdg_141_fcf_coverage_of_netinc_d2": {"inputs": ['ncfo', 'capex', 'netinc'], "func": f40_eqdg_141_fcf_coverage_of_netinc_d2},
    "f40_eqdg_142_sga_to_revenue_quality_d2": {"inputs": ['sga', 'revenue'], "func": f40_eqdg_142_sga_to_revenue_quality_d2},
    "f40_eqdg_143_rnd_to_revenue_capitalization_proxy_d2": {"inputs": ['rnd', 'revenue', 'intangibles'], "func": f40_eqdg_143_rnd_to_revenue_capitalization_proxy_d2},
    "f40_eqdg_144_opex_to_revenue_efficiency_d2": {"inputs": ['opex', 'revenue'], "func": f40_eqdg_144_opex_to_revenue_efficiency_d2},
    "f40_eqdg_145_retearn_growth_vs_netinc_consistency_d2": {"inputs": ['retearn', 'netinc'], "func": f40_eqdg_145_retearn_growth_vs_netinc_consistency_d2},
    "f40_eqdg_146_equity_quality_accoci_share_d2": {"inputs": ['accoci', 'equity'], "func": f40_eqdg_146_equity_quality_accoci_share_d2},
    "f40_eqdg_147_intangibles_to_assets_quality_d2": {"inputs": ['intangibles', 'assets'], "func": f40_eqdg_147_intangibles_to_assets_quality_d2},
    "f40_eqdg_148_investments_to_assets_d2": {"inputs": ['investments', 'assets'], "func": f40_eqdg_148_investments_to_assets_d2},
    "f40_eqdg_149_ncfcommon_share_of_ncff_d2": {"inputs": ['ncfcommon', 'ncff'], "func": f40_eqdg_149_ncfcommon_share_of_ncff_d2},
    "f40_eqdg_150_ncfdebt_minus_ncfcommon_to_assets_d2": {"inputs": ['ncfdebt', 'ncfcommon', 'assets'], "func": f40_eqdg_150_ncfdebt_minus_ncfcommon_to_assets_d2},
}
