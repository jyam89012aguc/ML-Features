"""earnings_quality_divergence base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py. Same PIT discipline, same helpers.
Inputs: SF1 columns forward-filled to daily by binder. Trading-day windows.
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
#                    FEATURES 076-150
# ============================================================

# ---------- Earnings <-> sales-growth divergence (076-078, continued) ----------

def f40_eqdg_076_eps_growth_minus_revenue_growth_yoy(eps: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY EPS growth minus YoY Revenue growth — per-share quality wedge (buyback-aided)."""
    g_e = _safe_div(eps - eps.shift(YDAYS), eps.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_e - g_r


def f40_eqdg_077_gp_growth_minus_revenue_growth_yoy(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY GrossProfit growth minus YoY Revenue growth — margin direction."""
    g_g = _safe_div(gp - gp.shift(YDAYS), gp.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_g - g_r


def f40_eqdg_078_netinc_growth_minus_revenue_growth_2y(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y NI growth minus 2y Revenue growth — sustained earnings inflation vs sales."""
    win = 2 * YDAYS
    g_n = _safe_div(netinc - netinc.shift(win), netinc.shift(win).abs())
    g_r = _safe_div(revenue - revenue.shift(win), revenue.shift(win).abs())
    return g_n - g_r


# ---------- Receivables-quality / channel-stuffing (079-086) ----------

def f40_eqdg_079_receivables_to_revenue(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """AR / Revenue level — receivables intensity."""
    return _safe_div(receivables, revenue)


def f40_eqdg_080_dreceivables_to_drevenue(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """dAR / dRevenue (YoY) — incremental AR per incremental sale, channel-stuffing proxy."""
    dar = receivables.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return _safe_div(dar, dr)


def f40_eqdg_081_dso_change_yoy(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Days Sales Outstanding YoY change (DSO_t - DSO_{t-1y})."""
    dso = _safe_div(receivables, revenue) * 365.0
    return dso - dso.shift(YDAYS)


def f40_eqdg_082_dso_zscore_12q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """DSO z-score over 12q — abnormal AR-days extension."""
    dso = _safe_div(receivables, revenue) * 365.0
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = dso.rolling(win, min_periods=mp).mean()
    sd = dso.rolling(win, min_periods=mp).std()
    return _safe_div(dso - m, sd)


def f40_eqdg_083_receivables_growth_minus_revenue_growth(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY AR growth minus YoY Revenue growth — AR outpacing sales."""
    g_a = _safe_div(receivables - receivables.shift(YDAYS), receivables.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_a - g_r


def f40_eqdg_084_ar_growth_2y_minus_rev_growth_2y(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """2y AR growth minus 2y Revenue growth — multi-year AR build."""
    win = 2 * YDAYS
    g_a = _safe_div(receivables - receivables.shift(win), receivables.shift(win).abs())
    g_r = _safe_div(revenue - revenue.shift(win), revenue.shift(win).abs())
    return g_a - g_r


def f40_eqdg_085_dso_trend_slope_8q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Slope of (DSO - 8q_mean(DSO)) regressed on linear time — DSO trend."""
    dso = _safe_div(receivables, revenue) * 365.0
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    m = dso.rolling(win, min_periods=mp).mean()
    return (dso - m) / float(win)


def f40_eqdg_086_receivables_share_of_dassets(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """dAR / dAssets (YoY) — share of asset growth driven by AR."""
    dar = receivables.diff(YDAYS)
    da = assets.diff(YDAYS)
    return _safe_div(dar, da)


# ---------- Inventory-quality (087-092) ----------

def f40_eqdg_087_inventory_to_revenue(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory / Revenue — inventory intensity."""
    return _safe_div(inventory, revenue)


def f40_eqdg_088_dinventory_to_drevenue(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """dInv / dRevenue (YoY) — incremental inventory per dollar of incremental sales."""
    di = inventory.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return _safe_div(di, dr)


def f40_eqdg_089_dio_change_yoy(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Days Inventory Outstanding YoY change."""
    dio = _safe_div(inventory, cor) * 365.0
    return dio - dio.shift(YDAYS)


def f40_eqdg_090_dio_zscore_12q(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """DIO z-score over 12q — abnormal inventory build."""
    dio = _safe_div(inventory, cor) * 365.0
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = dio.rolling(win, min_periods=mp).mean()
    sd = dio.rolling(win, min_periods=mp).std()
    return _safe_div(dio - m, sd)


def f40_eqdg_091_inv_growth_minus_revenue_growth(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY Inventory growth minus YoY Revenue growth — channel-stuffing on inventory."""
    g_i = _safe_div(inventory - inventory.shift(YDAYS), inventory.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_i - g_r


def f40_eqdg_092_inv_share_of_dassets(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """dInv / dAssets (YoY) — share of asset growth from inventory build."""
    di = inventory.diff(YDAYS)
    da = assets.diff(YDAYS)
    return _safe_div(di, da)


# ---------- Deferred-revenue dynamics (093-096) ----------

def f40_eqdg_093_deferredrev_to_revenue(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """Deferred revenue / Revenue — billings ahead of recognition."""
    return _safe_div(deferredrev, revenue)


def f40_eqdg_094_ddeferredrev_to_revenue(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """dDeferredRev (YoY) / Revenue — change in billings vs revenue scale."""
    dd = deferredrev.diff(YDAYS)
    return _safe_div(dd, revenue)


def f40_eqdg_095_defrev_growth_minus_revenue_growth(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY DefRev growth minus YoY Revenue growth — billings deceleration signal when negative."""
    g_d = _safe_div(deferredrev - deferredrev.shift(YDAYS), deferredrev.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_d - g_r


def f40_eqdg_096_defrev_to_revenue_zscore_12q(deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """z-score of DefRev/Revenue over 12q — extreme billings vs recognition."""
    r = _safe_div(deferredrev, revenue)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = r.rolling(win, min_periods=mp).mean()
    sd = r.rolling(win, min_periods=mp).std()
    return _safe_div(r - m, sd)


# ---------- Operating vs non-operating split (097-102) ----------

def f40_eqdg_097_nonop_income_share(netinc: pd.Series, ebit: pd.Series, taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """(NetInc - EBIT*(1 - tax_rate)) / NetInc — non-operating share of net income."""
    etr = _safe_div(taxexp, ebt)
    ebit_at = ebit * (1.0 - etr)
    return _safe_div(netinc - ebit_at, netinc.abs())


def f40_eqdg_098_ebit_minus_netinc_to_revenue(ebit: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """(EBIT - NetInc) / Revenue — non-op + tax wedge scaled by sales."""
    return _safe_div(ebit - netinc, revenue)


def f40_eqdg_099_ebit_to_netinc_ratio(ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    """EBIT / NetInc — operating vs total earnings ratio."""
    return _safe_div(ebit, netinc)


def f40_eqdg_100_nonop_other_income_share(netinc: pd.Series, ebit: pd.Series) -> pd.Series:
    """(NetInc - EBIT) / |EBIT| — earnings boost beyond operations (signed)."""
    return _safe_div(netinc - ebit, ebit.abs())


def f40_eqdg_101_ebt_minus_ebit_to_revenue(ebt: pd.Series, ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """(EBT - EBIT) / Revenue — financing + non-op items intensity."""
    return _safe_div(ebt - ebit, revenue)


def f40_eqdg_102_pretax_to_post_tax_consistency(ebt: pd.Series, netinc: pd.Series) -> pd.Series:
    """NetInc / EBT — implied (1 - ETR). Sudden spike = tax-driven earnings."""
    return _safe_div(netinc, ebt)


# ---------- One-time / special items proxy (103-106) ----------

def f40_eqdg_103_netinc_minus_ebit_after_tax_spike_zscore(netinc: pd.Series, ebit: pd.Series, taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """z-score over 12q of (NetInc - EBIT*(1 - ETR)) — special-item spike detector."""
    etr = _safe_div(taxexp, ebt)
    diff = netinc - ebit * (1.0 - etr)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = diff.rolling(win, min_periods=mp).mean()
    sd = diff.rolling(win, min_periods=mp).std()
    return _safe_div(diff - m, sd)


def f40_eqdg_104_ebit_ebitda_gap_zscore(ebitda: pd.Series, ebit: pd.Series) -> pd.Series:
    """z-score of (EBITDA - EBIT) = D&A — spike detector for amortization/write-downs."""
    gap = ebitda - ebit
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = gap.rolling(win, min_periods=mp).mean()
    sd = gap.rolling(win, min_periods=mp).std()
    return _safe_div(gap - m, sd)


def f40_eqdg_105_special_items_proxy_residual(netinc: pd.Series, ebit: pd.Series, taxexp: pd.Series) -> pd.Series:
    """NetInc - (EBIT - TaxExp) — residual items beyond pure operating-after-tax."""
    return netinc - (ebit - taxexp)


def f40_eqdg_106_gp_minus_ebit_gap_anomaly(gp: pd.Series, ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """(GP - EBIT) / Revenue — operating overhead burden anomaly vs sales."""
    return _safe_div(gp - ebit, revenue)


# ---------- Gross margin quality (107-110) ----------

def f40_eqdg_107_gross_margin_cv_8q(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """8q coefficient of variation of GM = std/|mean|."""
    gm = _safe_div(revenue - cor, revenue)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    return _safe_div(gm.rolling(win, min_periods=mp).std(), gm.rolling(win, min_periods=mp).mean().abs())


def f40_eqdg_108_gross_margin_smoothness_vs_revenue(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """GM-std / Revenue-CV ratio over 8q — GM smoother than sales = managed."""
    gm = _safe_div(revenue - cor, revenue)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    gm_sd = gm.rolling(win, min_periods=mp).std()
    rv_cv = _safe_div(revenue.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).mean().abs())
    return _safe_div(gm_sd, rv_cv)


def f40_eqdg_109_gm_residual_from_revenue_regression(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """GM minus its 8q linear-trend estimate (mean) — instantaneous GM anomaly."""
    gm = _safe_div(revenue - cor, revenue)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    m = gm.rolling(win, min_periods=mp).mean()
    return gm - m


def f40_eqdg_110_gm_rolling_skew_12q(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """12q rolling skew of GM — asymmetric margin manipulation."""
    gm = _safe_div(revenue - cor, revenue)
    win = 12 * QDAYS
    return gm.rolling(win, min_periods=max(win // 3, QDAYS)).skew()


# ---------- Earnings vs FCF z-score divergence (111-116) ----------

def f40_eqdg_111_netinc_zscore_minus_fcf_zscore_12q(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """z(NetInc) - z(FCF) over 12q — accounting earnings extreme vs cash extreme."""
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    n_z = _safe_div(netinc - netinc.rolling(win, min_periods=mp).mean(), netinc.rolling(win, min_periods=mp).std())
    f_z = _safe_div(fcf - fcf.rolling(win, min_periods=mp).mean(), fcf.rolling(win, min_periods=mp).std())
    return n_z - f_z


def f40_eqdg_112_netinc_zscore_minus_cfo_zscore_12q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """z(NetInc) - z(CFO) over 12q — accounting vs operating-cash extreme."""
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    n_z = _safe_div(netinc - netinc.rolling(win, min_periods=mp).mean(), netinc.rolling(win, min_periods=mp).std())
    c_z = _safe_div(ncfo - ncfo.rolling(win, min_periods=mp).mean(), ncfo.rolling(win, min_periods=mp).std())
    return n_z - c_z


def f40_eqdg_113_eps_zscore_minus_fcf_per_share_zscore_12q(eps: pd.Series, fcf: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """z(EPS) - z(FCF per diluted share) — per-share quality divergence."""
    fcfps = _safe_div(fcf, shareswadil)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    e_z = _safe_div(eps - eps.rolling(win, min_periods=mp).mean(), eps.rolling(win, min_periods=mp).std())
    f_z = _safe_div(fcfps - fcfps.rolling(win, min_periods=mp).mean(), fcfps.rolling(win, min_periods=mp).std())
    return e_z - f_z


def f40_eqdg_114_ni_fcf_divergence_blended_8q(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Blended 8q divergence: rank-diff + z-diff midpoint of NI vs FCF."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    n_z = _safe_div(netinc - netinc.rolling(win, min_periods=mp).mean(), netinc.rolling(win, min_periods=mp).std())
    f_z = _safe_div(fcf - fcf.rolling(win, min_periods=mp).mean(), fcf.rolling(win, min_periods=mp).std())
    n_r = netinc.rolling(win, min_periods=mp).rank(pct=True)
    f_r = fcf.rolling(win, min_periods=mp).rank(pct=True)
    return 0.5 * (n_z - f_z) + 0.5 * (n_r - f_r)


def f40_eqdg_115_rolling_corr_ni_fcf_8q(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """8q rolling correlation of NetInc vs FCF — low/negative = quality break."""
    win = 8 * QDAYS
    return netinc.rolling(win, min_periods=max(win // 3, QDAYS)).corr(fcf)


def f40_eqdg_116_rolling_corr_ni_cfo_8q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """8q rolling correlation of NetInc vs CFO."""
    win = 8 * QDAYS
    return netinc.rolling(win, min_periods=max(win // 3, QDAYS)).corr(ncfo)


# ---------- Hidden operating leverage via accruals (117-120) ----------

def f40_eqdg_117_wc_delta_to_revenue_delta_ratio(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """dWC / dRevenue (YoY) — capital intensity per dollar of incremental sales."""
    dwc = workingcapital.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return _safe_div(dwc, dr)


def f40_eqdg_118_wc_to_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """WC / Revenue — capital tie-up in operations."""
    return _safe_div(workingcapital, revenue)


def f40_eqdg_119_dwc_share_of_dassets(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """dWC / dAssets (YoY) — share of asset growth from WC build."""
    dwc = workingcapital.diff(YDAYS)
    da = assets.diff(YDAYS)
    return _safe_div(dwc, da)


def f40_eqdg_120_wc_volatility_vs_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """8q std(WC) / 8q std(Revenue) — WC volatility relative to top-line."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    return _safe_div(workingcapital.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).std())


# ---------- Quality composite scores (121-130) ----------

def f40_eqdg_121_quality_composite_v1(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, fcf: pd.Series) -> pd.Series:
    """v1 = z(Sloan accruals) - z(FCF/Assets) — higher = worse quality."""
    sl = _safe_div(netinc - ncfo, assets)
    fa = _safe_div(fcf, assets)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    sl_z = _safe_div(sl - sl.rolling(win, min_periods=mp).mean(), sl.rolling(win, min_periods=mp).std())
    fa_z = _safe_div(fa - fa.rolling(win, min_periods=mp).mean(), fa.rolling(win, min_periods=mp).std())
    return sl_z - fa_z


def f40_eqdg_122_quality_composite_v2(ncfo: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """v2 = (1 - CFO/NI) + z(NI smoothness vs Rev) — cash-conv + smoothness blend."""
    nce = 1.0 - _safe_div(ncfo, netinc)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    ni_cv = _safe_div(netinc.rolling(win, min_periods=mp).std(), netinc.rolling(win, min_periods=mp).mean().abs())
    rv_cv = _safe_div(revenue.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).mean().abs())
    sm = _safe_div(ni_cv, rv_cv)
    return nce - sm


def f40_eqdg_123_aggressive_revenue_recognition_composite(receivables: pd.Series, deferredrev: pd.Series, revenue: pd.Series) -> pd.Series:
    """(AR/Rev YoY change) + (-dDefRev/Rev) — aggressive recognition compounding."""
    dso_chg = _safe_div(receivables, revenue) - _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS))
    drd = -_safe_div(deferredrev.diff(YDAYS), revenue)
    return dso_chg + drd


def f40_eqdg_124_cash_quality_composite(ncfo: pd.Series, fcf: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of CFO/NI, FCF/NI, FCF/Rev, CFO/Rev — average cash-conversion intensity."""
    a = _safe_div(ncfo, netinc)
    b = _safe_div(fcf, netinc)
    c = _safe_div(fcf, revenue)
    d = _safe_div(ncfo, revenue)
    return (a + b + c + d) / 4.0


def f40_eqdg_125_persistence_quality_composite(netinc: pd.Series, eps: pd.Series) -> pd.Series:
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
    return (_ac(netinc) + _ac(eps)) / 2.0


def f40_eqdg_126_noncash_inflation_composite(sbcomp: pd.Series, depamor: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    """(SBC + D&A) / max(EBITDA, |NI|) — total non-cash earnings inflation share."""
    den = pd.concat([ebitda, netinc.abs()], axis=1).max(axis=1)
    return _safe_div(sbcomp + depamor, den)


def f40_eqdg_127_receivables_quality_composite(receivables: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Composite: z(DSO) + dAR/dAssets — receivables-quality red-flag blend."""
    dso = _safe_div(receivables, revenue) * 365.0
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    z = _safe_div(dso - dso.rolling(win, min_periods=mp).mean(), dso.rolling(win, min_periods=mp).std())
    share = _safe_div(receivables.diff(YDAYS), assets.diff(YDAYS))
    return z + share


def f40_eqdg_128_composite_total_quality_score(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, sbcomp: pd.Series, receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Composite total quality: Sloan + SBC/Rev + DSO_yoy_chg — sum of three rotated red flags."""
    sl = _safe_div(netinc - ncfo, assets)
    sbc_r = _safe_div(sbcomp, revenue)
    dso = _safe_div(receivables, revenue) * 365.0
    return sl + sbc_r + (dso - dso.shift(YDAYS))


def f40_eqdg_129_composite_red_flag_count(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, sbcomp: pd.Series, receivables: pd.Series, revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Count of fired red flags: Sloan>0.10, SBC/Rev>0.05, NI>0 & FCF<0, dDSO>30, |CFO|<|NI|."""
    sl = _safe_div(netinc - ncfo, assets)
    sbc_r = _safe_div(sbcomp, revenue)
    dso = _safe_div(receivables, revenue) * 365.0
    ddso = dso - dso.shift(YDAYS)
    f1 = (sl > 0.10).astype(float)
    f2 = (sbc_r > 0.05).astype(float)
    f3 = ((netinc > 0) & (fcf < 0)).astype(float)
    f4 = (ddso > 30.0).astype(float)
    f5 = (ncfo.abs() < netinc.abs()).astype(float)
    return f1 + f2 + f3 + f4 + f5


def f40_eqdg_130_quality_residual_blend(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """(NI - CFO - SBC) / Revenue — residual non-cash earnings after stripping SBC."""
    return _safe_div(netinc - ncfo - sbcomp, revenue)


# ---------- Capex stickiness / hidden via WC (131-134) ----------

def f40_eqdg_131_capex_to_revenue_stickiness_8q_std(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """8q std of |capex|/Revenue — capex volatility vs sales (high = inconsistent reinvestment)."""
    r = _safe_div(capex.abs(), revenue)
    return r.rolling(8 * QDAYS, min_periods=2 * QDAYS).std()


def f40_eqdg_132_capex_to_cfo(capex: pd.Series, ncfo: pd.Series) -> pd.Series:
    """|capex| / CFO — reinvestment intensity relative to cash generation."""
    return _safe_div(capex.abs(), ncfo)


def f40_eqdg_133_capex_to_depamor_zscore_12q(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """z-score of |capex|/D&A over 12q — extreme over/under-investment."""
    r = _safe_div(capex.abs(), depamor)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = r.rolling(win, min_periods=mp).mean()
    sd = r.rolling(win, min_periods=mp).std()
    return _safe_div(r - m, sd)


def f40_eqdg_134_wc_bloat_minus_capex_underinvestment(workingcapital: pd.Series, capex: pd.Series, depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """(dWC/Rev) - ((|capex| - D&A)/Rev) — WC bloat + capex underinvestment combined."""
    dwc_r = _safe_div(workingcapital.diff(YDAYS), revenue)
    cx_r = _safe_div(capex.abs() - depamor, revenue)
    return dwc_r - cx_r


# ---------- Negative-quality flag indicator series (135-140) ----------

def f40_eqdg_135_cfo_neg_while_ni_pos_flag(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Indicator: CFO < 0 AND NetInc > 0 — classic accrual red flag."""
    flag = (ncfo < 0) & (netinc > 0)
    out = flag.astype(float)
    return out.where(netinc.notna() & ncfo.notna(), np.nan)


def f40_eqdg_136_sbc_exceeds_netinc_flag(sbcomp: pd.Series, netinc: pd.Series) -> pd.Series:
    """Indicator: SBC > NetInc (when NI > 0) — earnings entirely paid in dilution."""
    flag = (sbcomp > netinc) & (netinc > 0)
    out = flag.astype(float)
    return out.where(sbcomp.notna() & netinc.notna(), np.nan)


def f40_eqdg_137_accruals_top_decile_flag(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: Sloan accruals > 12q-rolling 90th percentile — extreme accrual flag."""
    sl = _safe_div(netinc - ncfo, assets)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    q90 = sl.rolling(win, min_periods=mp).quantile(0.90)
    flag = sl > q90
    out = flag.astype(float)
    return out.where(sl.notna() & q90.notna(), np.nan)


def f40_eqdg_138_dso_jumped_flag(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Indicator: DSO YoY change > +30 days — channel-stuffing burst flag."""
    dso = _safe_div(receivables, revenue) * 365.0
    chg = dso - dso.shift(YDAYS)
    out = (chg > 30.0).astype(float)
    return out.where(chg.notna(), np.nan)


def f40_eqdg_139_dio_jumped_flag(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """Indicator: DIO YoY change > +30 days — inventory build flag."""
    dio = _safe_div(inventory, cor) * 365.0
    chg = dio - dio.shift(YDAYS)
    out = (chg > 30.0).astype(float)
    return out.where(chg.notna(), np.nan)


def f40_eqdg_140_high_noncash_earnings_flag(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Indicator: (NI - CFO)/|NI| > 0.5 — majority of earnings is non-cash."""
    nce = _safe_div(netinc - ncfo, netinc.abs())
    out = (nce > 0.5).astype(float)
    return out.where(nce.notna(), np.nan)


# ---------- Extra distinct quality concepts (141-150) ----------

def f40_eqdg_141_fcf_coverage_of_netinc(ncfo: pd.Series, capex: pd.Series, netinc: pd.Series) -> pd.Series:
    """(CFO - |capex|) / NetInc — FCF coverage of accounting earnings."""
    return _safe_div(ncfo - capex.abs(), netinc)


def f40_eqdg_142_sga_to_revenue_quality(sga: pd.Series, revenue: pd.Series) -> pd.Series:
    """SGA / Revenue — overhead intensity (rising = quality erosion)."""
    return _safe_div(sga, revenue)


def f40_eqdg_143_rnd_to_revenue_capitalization_proxy(rnd: pd.Series, revenue: pd.Series, intangibles: pd.Series) -> pd.Series:
    """RnD/Revenue minus (dIntangibles/Revenue) — net expensed R&D adjusting for capitalized intangibles."""
    rd_r = _safe_div(rnd, revenue)
    cap_r = _safe_div(intangibles.diff(YDAYS), revenue)
    return rd_r - cap_r


def f40_eqdg_144_opex_to_revenue_efficiency(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """OpEx / Revenue — operating efficiency (rising = quality risk)."""
    return _safe_div(opex, revenue)


def f40_eqdg_145_retearn_growth_vs_netinc_consistency(retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """dRetEarn (YoY) / NetInc_sum_4q — retained-earnings flow vs trailing earnings sum."""
    dre = retearn.diff(YDAYS)
    ni_sum = netinc.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(dre, ni_sum)


def f40_eqdg_146_equity_quality_accoci_share(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """AOCI / Equity — accumulated other comprehensive income share of equity (FX/MTM noise)."""
    return _safe_div(accoci, equity)


def f40_eqdg_147_intangibles_to_assets_quality(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Intangibles / Assets — soft asset share."""
    return _safe_div(intangibles, assets)


def f40_eqdg_148_investments_to_assets(investments: pd.Series, assets: pd.Series) -> pd.Series:
    """Investments / Assets — non-operating capital allocation."""
    return _safe_div(investments, assets)


def f40_eqdg_149_ncfcommon_share_of_ncff(ncfcommon: pd.Series, ncff: pd.Series) -> pd.Series:
    """|NCFCommon| / |NCFF| — equity issuance/buyback share of financing flows."""
    return _safe_div(ncfcommon.abs(), ncff.abs())


def f40_eqdg_150_ncfdebt_minus_ncfcommon_to_assets(ncfdebt: pd.Series, ncfcommon: pd.Series, assets: pd.Series) -> pd.Series:
    """(NCFDebt - NCFCommon) / Assets — debt-vs-equity financing mix per asset base."""
    return _safe_div(ncfdebt - ncfcommon, assets)


# ============================================================
#                        REGISTRY
# ============================================================

EARNINGS_QUALITY_DIVERGENCE_BASE_REGISTRY_076_150 = {
    "f40_eqdg_076_eps_growth_minus_revenue_growth_yoy": {"inputs": ["eps", "revenue"], "func": f40_eqdg_076_eps_growth_minus_revenue_growth_yoy},
    "f40_eqdg_077_gp_growth_minus_revenue_growth_yoy": {"inputs": ["gp", "revenue"], "func": f40_eqdg_077_gp_growth_minus_revenue_growth_yoy},
    "f40_eqdg_078_netinc_growth_minus_revenue_growth_2y": {"inputs": ["netinc", "revenue"], "func": f40_eqdg_078_netinc_growth_minus_revenue_growth_2y},
    "f40_eqdg_079_receivables_to_revenue": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_079_receivables_to_revenue},
    "f40_eqdg_080_dreceivables_to_drevenue": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_080_dreceivables_to_drevenue},
    "f40_eqdg_081_dso_change_yoy": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_081_dso_change_yoy},
    "f40_eqdg_082_dso_zscore_12q": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_082_dso_zscore_12q},
    "f40_eqdg_083_receivables_growth_minus_revenue_growth": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_083_receivables_growth_minus_revenue_growth},
    "f40_eqdg_084_ar_growth_2y_minus_rev_growth_2y": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_084_ar_growth_2y_minus_rev_growth_2y},
    "f40_eqdg_085_dso_trend_slope_8q": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_085_dso_trend_slope_8q},
    "f40_eqdg_086_receivables_share_of_dassets": {"inputs": ["receivables", "assets"], "func": f40_eqdg_086_receivables_share_of_dassets},
    "f40_eqdg_087_inventory_to_revenue": {"inputs": ["inventory", "revenue"], "func": f40_eqdg_087_inventory_to_revenue},
    "f40_eqdg_088_dinventory_to_drevenue": {"inputs": ["inventory", "revenue"], "func": f40_eqdg_088_dinventory_to_drevenue},
    "f40_eqdg_089_dio_change_yoy": {"inputs": ["inventory", "cor"], "func": f40_eqdg_089_dio_change_yoy},
    "f40_eqdg_090_dio_zscore_12q": {"inputs": ["inventory", "cor"], "func": f40_eqdg_090_dio_zscore_12q},
    "f40_eqdg_091_inv_growth_minus_revenue_growth": {"inputs": ["inventory", "revenue"], "func": f40_eqdg_091_inv_growth_minus_revenue_growth},
    "f40_eqdg_092_inv_share_of_dassets": {"inputs": ["inventory", "assets"], "func": f40_eqdg_092_inv_share_of_dassets},
    "f40_eqdg_093_deferredrev_to_revenue": {"inputs": ["deferredrev", "revenue"], "func": f40_eqdg_093_deferredrev_to_revenue},
    "f40_eqdg_094_ddeferredrev_to_revenue": {"inputs": ["deferredrev", "revenue"], "func": f40_eqdg_094_ddeferredrev_to_revenue},
    "f40_eqdg_095_defrev_growth_minus_revenue_growth": {"inputs": ["deferredrev", "revenue"], "func": f40_eqdg_095_defrev_growth_minus_revenue_growth},
    "f40_eqdg_096_defrev_to_revenue_zscore_12q": {"inputs": ["deferredrev", "revenue"], "func": f40_eqdg_096_defrev_to_revenue_zscore_12q},
    "f40_eqdg_097_nonop_income_share": {"inputs": ["netinc", "ebit", "taxexp", "ebt"], "func": f40_eqdg_097_nonop_income_share},
    "f40_eqdg_098_ebit_minus_netinc_to_revenue": {"inputs": ["ebit", "netinc", "revenue"], "func": f40_eqdg_098_ebit_minus_netinc_to_revenue},
    "f40_eqdg_099_ebit_to_netinc_ratio": {"inputs": ["ebit", "netinc"], "func": f40_eqdg_099_ebit_to_netinc_ratio},
    "f40_eqdg_100_nonop_other_income_share": {"inputs": ["netinc", "ebit"], "func": f40_eqdg_100_nonop_other_income_share},
    "f40_eqdg_101_ebt_minus_ebit_to_revenue": {"inputs": ["ebt", "ebit", "revenue"], "func": f40_eqdg_101_ebt_minus_ebit_to_revenue},
    "f40_eqdg_102_pretax_to_post_tax_consistency": {"inputs": ["ebt", "netinc"], "func": f40_eqdg_102_pretax_to_post_tax_consistency},
    "f40_eqdg_103_netinc_minus_ebit_after_tax_spike_zscore": {"inputs": ["netinc", "ebit", "taxexp", "ebt"], "func": f40_eqdg_103_netinc_minus_ebit_after_tax_spike_zscore},
    "f40_eqdg_104_ebit_ebitda_gap_zscore": {"inputs": ["ebitda", "ebit"], "func": f40_eqdg_104_ebit_ebitda_gap_zscore},
    "f40_eqdg_105_special_items_proxy_residual": {"inputs": ["netinc", "ebit", "taxexp"], "func": f40_eqdg_105_special_items_proxy_residual},
    "f40_eqdg_106_gp_minus_ebit_gap_anomaly": {"inputs": ["gp", "ebit", "revenue"], "func": f40_eqdg_106_gp_minus_ebit_gap_anomaly},
    "f40_eqdg_107_gross_margin_cv_8q": {"inputs": ["revenue", "cor"], "func": f40_eqdg_107_gross_margin_cv_8q},
    "f40_eqdg_108_gross_margin_smoothness_vs_revenue": {"inputs": ["revenue", "cor"], "func": f40_eqdg_108_gross_margin_smoothness_vs_revenue},
    "f40_eqdg_109_gm_residual_from_revenue_regression": {"inputs": ["revenue", "cor"], "func": f40_eqdg_109_gm_residual_from_revenue_regression},
    "f40_eqdg_110_gm_rolling_skew_12q": {"inputs": ["revenue", "cor"], "func": f40_eqdg_110_gm_rolling_skew_12q},
    "f40_eqdg_111_netinc_zscore_minus_fcf_zscore_12q": {"inputs": ["netinc", "fcf"], "func": f40_eqdg_111_netinc_zscore_minus_fcf_zscore_12q},
    "f40_eqdg_112_netinc_zscore_minus_cfo_zscore_12q": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_112_netinc_zscore_minus_cfo_zscore_12q},
    "f40_eqdg_113_eps_zscore_minus_fcf_per_share_zscore_12q": {"inputs": ["eps", "fcf", "shareswadil"], "func": f40_eqdg_113_eps_zscore_minus_fcf_per_share_zscore_12q},
    "f40_eqdg_114_ni_fcf_divergence_blended_8q": {"inputs": ["netinc", "fcf"], "func": f40_eqdg_114_ni_fcf_divergence_blended_8q},
    "f40_eqdg_115_rolling_corr_ni_fcf_8q": {"inputs": ["netinc", "fcf"], "func": f40_eqdg_115_rolling_corr_ni_fcf_8q},
    "f40_eqdg_116_rolling_corr_ni_cfo_8q": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_116_rolling_corr_ni_cfo_8q},
    "f40_eqdg_117_wc_delta_to_revenue_delta_ratio": {"inputs": ["workingcapital", "revenue"], "func": f40_eqdg_117_wc_delta_to_revenue_delta_ratio},
    "f40_eqdg_118_wc_to_revenue": {"inputs": ["workingcapital", "revenue"], "func": f40_eqdg_118_wc_to_revenue},
    "f40_eqdg_119_dwc_share_of_dassets": {"inputs": ["workingcapital", "assets"], "func": f40_eqdg_119_dwc_share_of_dassets},
    "f40_eqdg_120_wc_volatility_vs_revenue": {"inputs": ["workingcapital", "revenue"], "func": f40_eqdg_120_wc_volatility_vs_revenue},
    "f40_eqdg_121_quality_composite_v1": {"inputs": ["netinc", "ncfo", "assets", "fcf"], "func": f40_eqdg_121_quality_composite_v1},
    "f40_eqdg_122_quality_composite_v2": {"inputs": ["ncfo", "netinc", "revenue"], "func": f40_eqdg_122_quality_composite_v2},
    "f40_eqdg_123_aggressive_revenue_recognition_composite": {"inputs": ["receivables", "deferredrev", "revenue"], "func": f40_eqdg_123_aggressive_revenue_recognition_composite},
    "f40_eqdg_124_cash_quality_composite": {"inputs": ["ncfo", "fcf", "netinc", "revenue"], "func": f40_eqdg_124_cash_quality_composite},
    "f40_eqdg_125_persistence_quality_composite": {"inputs": ["netinc", "eps"], "func": f40_eqdg_125_persistence_quality_composite},
    "f40_eqdg_126_noncash_inflation_composite": {"inputs": ["sbcomp", "depamor", "ebitda", "netinc"], "func": f40_eqdg_126_noncash_inflation_composite},
    "f40_eqdg_127_receivables_quality_composite": {"inputs": ["receivables", "revenue", "assets"], "func": f40_eqdg_127_receivables_quality_composite},
    "f40_eqdg_128_composite_total_quality_score": {"inputs": ["netinc", "ncfo", "assets", "sbcomp", "receivables", "revenue"], "func": f40_eqdg_128_composite_total_quality_score},
    "f40_eqdg_129_composite_red_flag_count": {"inputs": ["netinc", "ncfo", "assets", "sbcomp", "receivables", "revenue", "fcf"], "func": f40_eqdg_129_composite_red_flag_count},
    "f40_eqdg_130_quality_residual_blend": {"inputs": ["netinc", "ncfo", "revenue", "sbcomp"], "func": f40_eqdg_130_quality_residual_blend},
    "f40_eqdg_131_capex_to_revenue_stickiness_8q_std": {"inputs": ["capex", "revenue"], "func": f40_eqdg_131_capex_to_revenue_stickiness_8q_std},
    "f40_eqdg_132_capex_to_cfo": {"inputs": ["capex", "ncfo"], "func": f40_eqdg_132_capex_to_cfo},
    "f40_eqdg_133_capex_to_depamor_zscore_12q": {"inputs": ["capex", "depamor"], "func": f40_eqdg_133_capex_to_depamor_zscore_12q},
    "f40_eqdg_134_wc_bloat_minus_capex_underinvestment": {"inputs": ["workingcapital", "capex", "depamor", "revenue"], "func": f40_eqdg_134_wc_bloat_minus_capex_underinvestment},
    "f40_eqdg_135_cfo_neg_while_ni_pos_flag": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_135_cfo_neg_while_ni_pos_flag},
    "f40_eqdg_136_sbc_exceeds_netinc_flag": {"inputs": ["sbcomp", "netinc"], "func": f40_eqdg_136_sbc_exceeds_netinc_flag},
    "f40_eqdg_137_accruals_top_decile_flag": {"inputs": ["netinc", "ncfo", "assets"], "func": f40_eqdg_137_accruals_top_decile_flag},
    "f40_eqdg_138_dso_jumped_flag": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_138_dso_jumped_flag},
    "f40_eqdg_139_dio_jumped_flag": {"inputs": ["inventory", "cor"], "func": f40_eqdg_139_dio_jumped_flag},
    "f40_eqdg_140_high_noncash_earnings_flag": {"inputs": ["ncfo", "netinc"], "func": f40_eqdg_140_high_noncash_earnings_flag},
    "f40_eqdg_141_fcf_coverage_of_netinc": {"inputs": ["ncfo", "capex", "netinc"], "func": f40_eqdg_141_fcf_coverage_of_netinc},
    "f40_eqdg_142_sga_to_revenue_quality": {"inputs": ["sga", "revenue"], "func": f40_eqdg_142_sga_to_revenue_quality},
    "f40_eqdg_143_rnd_to_revenue_capitalization_proxy": {"inputs": ["rnd", "revenue", "intangibles"], "func": f40_eqdg_143_rnd_to_revenue_capitalization_proxy},
    "f40_eqdg_144_opex_to_revenue_efficiency": {"inputs": ["opex", "revenue"], "func": f40_eqdg_144_opex_to_revenue_efficiency},
    "f40_eqdg_145_retearn_growth_vs_netinc_consistency": {"inputs": ["retearn", "netinc"], "func": f40_eqdg_145_retearn_growth_vs_netinc_consistency},
    "f40_eqdg_146_equity_quality_accoci_share": {"inputs": ["accoci", "equity"], "func": f40_eqdg_146_equity_quality_accoci_share},
    "f40_eqdg_147_intangibles_to_assets_quality": {"inputs": ["intangibles", "assets"], "func": f40_eqdg_147_intangibles_to_assets_quality},
    "f40_eqdg_148_investments_to_assets": {"inputs": ["investments", "assets"], "func": f40_eqdg_148_investments_to_assets},
    "f40_eqdg_149_ncfcommon_share_of_ncff": {"inputs": ["ncfcommon", "ncff"], "func": f40_eqdg_149_ncfcommon_share_of_ncff},
    "f40_eqdg_150_ncfdebt_minus_ncfcommon_to_assets": {"inputs": ["ncfdebt", "ncfcommon", "assets"], "func": f40_eqdg_150_ncfdebt_minus_ncfcommon_to_assets},
}
