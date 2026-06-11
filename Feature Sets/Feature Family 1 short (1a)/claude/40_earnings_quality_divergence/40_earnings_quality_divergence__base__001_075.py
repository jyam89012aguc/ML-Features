"""earnings_quality_divergence base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses (continued in __base__076_150.py for 150 total).
Inputs: SF1 columns forward-filled to daily cadence by binder. Trading-day windows.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows,
no .shift(-N). Missing-data contract: return pd.Series(np.nan, index=...).
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
#                    FEATURES 001-075
# ============================================================

# ---------- Total accruals (001-012) ----------

def f40_eqdg_001_sloan_accruals_to_assets(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Sloan accruals: (NetInc - CFO) / Assets — classic accrual-quality red flag."""
    return _safe_div(netinc - ncfo, assets)


def f40_eqdg_002_sloan_accruals_to_equity(netinc: pd.Series, ncfo: pd.Series, equity: pd.Series) -> pd.Series:
    """(NetInc - CFO) / Equity — accrual loading on book equity."""
    return _safe_div(netinc - ncfo, equity)


def f40_eqdg_003_sloan_accruals_to_revenue(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """(NetInc - CFO) / Revenue — accruals as share of top-line."""
    return _safe_div(netinc - ncfo, revenue)


def f40_eqdg_004_cfo_minus_ni_to_assets(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """(CFO - NetInc) / Assets — inverted Sloan; negative = poor cash backing."""
    return _safe_div(ncfo - netinc, assets)


def f40_eqdg_005_bs_accruals_wc_to_assets(workingcapital: pd.Series, cashneq: pd.Series, debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Balance-sheet accruals: (dWC - dCash - dSTdebt_proxy)/Assets via 4Q diff (~252 trading days)."""
    dwc = workingcapital.diff(YDAYS)
    dcash = cashneq.diff(YDAYS)
    ddebt = debt.diff(YDAYS)
    return _safe_div(dwc - dcash - ddebt, assets)


def f40_eqdg_006_bs_accruals_wc_to_equity(workingcapital: pd.Series, cashneq: pd.Series, debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Balance-sheet accruals normalized by equity."""
    dwc = workingcapital.diff(YDAYS)
    dcash = cashneq.diff(YDAYS)
    ddebt = debt.diff(YDAYS)
    return _safe_div(dwc - dcash - ddebt, equity)


def f40_eqdg_007_bs_accruals_wc_to_revenue(workingcapital: pd.Series, cashneq: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Balance-sheet accruals normalized by revenue."""
    dwc = workingcapital.diff(YDAYS)
    dcash = cashneq.diff(YDAYS)
    ddebt = debt.diff(YDAYS)
    return _safe_div(dwc - dcash - ddebt, revenue)


def f40_eqdg_008_dassets_minus_dcash_to_assets(assets: pd.Series, cashneq: pd.Series) -> pd.Series:
    """(dAssets - dCash) / Assets over 4Q — non-cash asset build."""
    da = assets.diff(YDAYS)
    dc = cashneq.diff(YDAYS)
    return _safe_div(da - dc, assets)


def f40_eqdg_009_dnoncash_wc_to_revenue(receivables: pd.Series, inventory: pd.Series, payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """(dAR + dInv - dAP) / Revenue — non-cash WC investment per dollar of sales."""
    dar = receivables.diff(YDAYS)
    di = inventory.diff(YDAYS)
    dap = payables.diff(YDAYS)
    return _safe_div(dar + di - dap, revenue)


def f40_eqdg_010_dar_plus_dinv_minus_dap_to_drevenue(receivables: pd.Series, inventory: pd.Series, payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """(dAR + dInv - dAP) / dRevenue — incremental WC needed per incremental sale."""
    dar = receivables.diff(YDAYS)
    di = inventory.diff(YDAYS)
    dap = payables.diff(YDAYS)
    dr = revenue.diff(YDAYS)
    return _safe_div(dar + di - dap, dr)


def f40_eqdg_011_modified_jones_residual_proxy(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series, receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Total accruals scaled by lagged assets minus revenue-growth-net-of-AR explanation."""
    ta = _safe_div(netinc - ncfo, assets.shift(YDAYS))
    drev = revenue.diff(YDAYS)
    dar = receivables.diff(YDAYS)
    explained = _safe_div(drev - dar, assets.shift(YDAYS))
    return ta - explained


def f40_eqdg_012_discretionary_accruals_ppne_adjusted(netinc: pd.Series, ncfo: pd.Series, ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """Accruals minus PPNE-loading proxy = discretionary accruals approximation."""
    ta = _safe_div(netinc - ncfo, assets.shift(YDAYS))
    ppne_load = _safe_div(ppnenet, assets.shift(YDAYS))
    return ta - 0.05 * ppne_load


# ---------- Cash conversion ratios (013-022) ----------

def f40_eqdg_013_cfo_to_netinc(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """CFO / NetInc — primary cash-conversion ratio. <1 = accrual-heavy earnings."""
    return _safe_div(ncfo, netinc)


def f40_eqdg_014_fcf_to_netinc(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """FCF / NetInc — free-cash conversion of accounting earnings."""
    return _safe_div(fcf, netinc)


def f40_eqdg_015_ocf_to_ebitda(ncfo: pd.Series, ebitda: pd.Series) -> pd.Series:
    """CFO / EBITDA — operating-cash backing of cash EBITDA."""
    return _safe_div(ncfo, ebitda)


def f40_eqdg_016_cfo_to_revenue(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """CFO / Revenue — operating-cash margin."""
    return _safe_div(ncfo, revenue)


def f40_eqdg_017_fcf_to_revenue(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """FCF / Revenue — free-cash margin."""
    return _safe_div(fcf, revenue)


def f40_eqdg_018_cfo_to_assets(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """CFO / Assets — cash return on assets."""
    return _safe_div(ncfo, assets)


def f40_eqdg_019_fcf_to_assets(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """FCF / Assets — free-cash return on assets."""
    return _safe_div(fcf, assets)


def f40_eqdg_020_cfo_to_ebit(ncfo: pd.Series, ebit: pd.Series) -> pd.Series:
    """CFO / EBIT — cash conversion of operating profit."""
    return _safe_div(ncfo, ebit)


def f40_eqdg_021_cfo_to_equity(ncfo: pd.Series, equity: pd.Series) -> pd.Series:
    """CFO / Equity — cash ROE proxy."""
    return _safe_div(ncfo, equity)


def f40_eqdg_022_one_minus_cfo_over_ni(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """1 - CFO/NetInc — accrual share of earnings (clipped). High = low cash backing."""
    r = _safe_div(ncfo, netinc)
    return 1.0 - r


# ---------- Non-cash earnings inflation (023-032) ----------

def f40_eqdg_023_depamor_to_ebitda(depamor: pd.Series, ebitda: pd.Series) -> pd.Series:
    """D&A / EBITDA — share of EBITDA explained purely by non-cash charges."""
    return _safe_div(depamor, ebitda)


def f40_eqdg_024_depamor_to_ebit(depamor: pd.Series, ebit: pd.Series) -> pd.Series:
    """D&A / EBIT — depreciation intensity vs operating profit."""
    return _safe_div(depamor, ebit)


def f40_eqdg_025_sbcomp_to_revenue(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """SBC / Revenue — stock-based-comp dilution drag."""
    return _safe_div(sbcomp, revenue)


def f40_eqdg_026_sbcomp_to_netinc(sbcomp: pd.Series, netinc: pd.Series) -> pd.Series:
    """SBC / NetInc — SBC as a fraction of reported earnings."""
    return _safe_div(sbcomp, netinc)


def f40_eqdg_027_sbcomp_to_cfo(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """SBC / CFO — SBC vs operating cash."""
    return _safe_div(sbcomp, ncfo)


def f40_eqdg_028_sbcomp_to_opex(sbcomp: pd.Series, opex: pd.Series) -> pd.Series:
    """SBC / OpEx — SBC share of operating cost structure."""
    return _safe_div(sbcomp, opex)


def f40_eqdg_029_capex_minus_depamor_to_assets(capex: pd.Series, depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """(|capex| - D&A) / Assets — underinvestment when negative (capex < D&A)."""
    return _safe_div(capex.abs() - depamor, assets)


def f40_eqdg_030_capex_to_depamor(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """|capex| / D&A — reinvestment ratio. <1 sustained = underinvestment."""
    return _safe_div(capex.abs(), depamor)


def f40_eqdg_031_depamor_to_ppnenet(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """D&A / PPNE — implied depreciation rate; sudden drops can flag manipulation."""
    return _safe_div(depamor, ppnenet)


def f40_eqdg_032_noncash_earnings_share(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """(NetInc - CFO) / |NetInc| — signed non-cash share of earnings."""
    return _safe_div(netinc - ncfo, netinc.abs())


# ---------- Earnings persistence (033-040) ----------

def f40_eqdg_033_netinc_autocorr_1lag_8q(netinc: pd.Series) -> pd.Series:
    """Rolling 8q (504-day) autocorr of NetInc at lag 1 — earnings persistence."""
    n = netinc
    lag = n.shift(QDAYS)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    nm = n.rolling(win, min_periods=mp).mean()
    lm = lag.rolling(win, min_periods=mp).mean()
    cov = ((n - nm) * (lag - lm)).rolling(win, min_periods=mp).mean()
    sn = n.rolling(win, min_periods=mp).std()
    sl = lag.rolling(win, min_periods=mp).std()
    return _safe_div(cov, sn * sl)


def f40_eqdg_034_eps_autocorr_1lag_8q(eps: pd.Series) -> pd.Series:
    """Rolling 8q autocorr of EPS at 1q lag — EPS persistence."""
    s = eps
    lag = s.shift(QDAYS)
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    nm = s.rolling(win, min_periods=mp).mean()
    lm = lag.rolling(win, min_periods=mp).mean()
    cov = ((s - nm) * (lag - lm)).rolling(win, min_periods=mp).mean()
    ss = s.rolling(win, min_periods=mp).std()
    sl = lag.rolling(win, min_periods=mp).std()
    return _safe_div(cov, ss * sl)


def f40_eqdg_035_netinc_growth_std_8q(netinc: pd.Series) -> pd.Series:
    """8q std of YoY NetInc growth — earnings volatility."""
    g = _safe_div(netinc - netinc.shift(YDAYS), netinc.shift(YDAYS).abs())
    return g.rolling(8 * QDAYS, min_periods=2 * QDAYS).std()


def f40_eqdg_036_eps_growth_std_8q(eps: pd.Series) -> pd.Series:
    """8q std of YoY EPS growth."""
    g = _safe_div(eps - eps.shift(YDAYS), eps.shift(YDAYS).abs())
    return g.rolling(8 * QDAYS, min_periods=2 * QDAYS).std()


def f40_eqdg_037_netinc_trend_residual_std_12q(netinc: pd.Series) -> pd.Series:
    """12q std of NetInc minus its 12q rolling mean (de-trended noise)."""
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = netinc.rolling(win, min_periods=mp).mean()
    resid = netinc - m
    return resid.rolling(win, min_periods=mp).std()


def f40_eqdg_038_netinc_ar1_coef_proxy_12q(netinc: pd.Series) -> pd.Series:
    """AR(1) coefficient proxy: cov(NI_t, NI_{t-1q}) / var(NI_{t-1q}) over 12q."""
    lag = netinc.shift(QDAYS)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    lm = lag.rolling(win, min_periods=mp).mean()
    nm = netinc.rolling(win, min_periods=mp).mean()
    cov = ((netinc - nm) * (lag - lm)).rolling(win, min_periods=mp).mean()
    var = ((lag - lm) ** 2).rolling(win, min_periods=mp).mean()
    return _safe_div(cov, var)


def f40_eqdg_039_revenue_ar1_coef_proxy_12q(revenue: pd.Series) -> pd.Series:
    """Revenue AR(1) coefficient proxy over 12q."""
    lag = revenue.shift(QDAYS)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    lm = lag.rolling(win, min_periods=mp).mean()
    nm = revenue.rolling(win, min_periods=mp).mean()
    cov = ((revenue - nm) * (lag - lm)).rolling(win, min_periods=mp).mean()
    var = ((lag - lm) ** 2).rolling(win, min_periods=mp).mean()
    return _safe_div(cov, var)


def f40_eqdg_040_ebit_ar1_coef_proxy_12q(ebit: pd.Series) -> pd.Series:
    """EBIT AR(1) coefficient proxy over 12q."""
    lag = ebit.shift(QDAYS)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    lm = lag.rolling(win, min_periods=mp).mean()
    nm = ebit.rolling(win, min_periods=mp).mean()
    cov = ((ebit - nm) * (lag - lm)).rolling(win, min_periods=mp).mean()
    var = ((lag - lm) ** 2).rolling(win, min_periods=mp).mean()
    return _safe_div(cov, var)


# ---------- Earnings smoothness manipulation (041-048) ----------

def f40_eqdg_041_ni_cv_to_cfo_cv_ratio_8q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """(std(NI)/|mean(NI)|) / (std(CFO)/|mean(CFO)|) over 8q. <1 = NI smoother than cash flow (red flag)."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    ni_cv = _safe_div(netinc.rolling(win, min_periods=mp).std(), netinc.rolling(win, min_periods=mp).mean().abs())
    cfo_cv = _safe_div(ncfo.rolling(win, min_periods=mp).std(), ncfo.rolling(win, min_periods=mp).mean().abs())
    return _safe_div(ni_cv, cfo_cv)


def f40_eqdg_042_ni_cv_to_revenue_cv_ratio_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """NI CV vs Revenue CV. Very low = suspiciously smooth earnings vs sales."""
    win = 8 * QDAYS
    mp = max(win // 3, QDAYS)
    ni_cv = _safe_div(netinc.rolling(win, min_periods=mp).std(), netinc.rolling(win, min_periods=mp).mean().abs())
    rv_cv = _safe_div(revenue.rolling(win, min_periods=mp).std(), revenue.rolling(win, min_periods=mp).mean().abs())
    return _safe_div(ni_cv, rv_cv)


def f40_eqdg_043_netinc_rolling_skew_12q(netinc: pd.Series) -> pd.Series:
    """12q rolling skew of NetInc — big-bath / cookie-jar asymmetry."""
    win = 12 * QDAYS
    return netinc.rolling(win, min_periods=max(win // 3, QDAYS)).skew()


def f40_eqdg_044_netinc_rolling_kurtosis_12q(netinc: pd.Series) -> pd.Series:
    """12q rolling kurtosis of NetInc — fat-tailed earnings prints."""
    win = 12 * QDAYS
    return netinc.rolling(win, min_periods=max(win // 3, QDAYS)).kurt()


def f40_eqdg_045_cfo_rolling_skew_12q(ncfo: pd.Series) -> pd.Series:
    """12q rolling skew of CFO — cash-flow asymmetry."""
    win = 12 * QDAYS
    return ncfo.rolling(win, min_periods=max(win // 3, QDAYS)).skew()


def f40_eqdg_046_cfo_rolling_kurtosis_12q(ncfo: pd.Series) -> pd.Series:
    """12q rolling kurtosis of CFO."""
    win = 12 * QDAYS
    return ncfo.rolling(win, min_periods=max(win // 3, QDAYS)).kurt()


def f40_eqdg_047_ni_minus_cfo_smoothness_zscore_12q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """z-score of (NI - CFO) over 12q — magnitude of accrual divergence relative to history."""
    diff = netinc - ncfo
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = diff.rolling(win, min_periods=mp).mean()
    sd = diff.rolling(win, min_periods=mp).std()
    return _safe_div(diff - m, sd)


def f40_eqdg_048_eps_smoothness_z_vs_revenue(eps: pd.Series, revenue: pd.Series) -> pd.Series:
    """(EPS-vol z) - (Revenue-vol z) over 12q — earnings smoother than top-line."""
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    e_sd = eps.rolling(win, min_periods=mp).std()
    r_sd = revenue.rolling(win, min_periods=mp).std()
    e_z = _safe_div(e_sd - e_sd.rolling(win, min_periods=mp).mean(), e_sd.rolling(win, min_periods=mp).std())
    r_z = _safe_div(r_sd - r_sd.rolling(win, min_periods=mp).mean(), r_sd.rolling(win, min_periods=mp).std())
    return e_z - r_z


# ---------- Tax-rate anomalies (049-054) ----------

def f40_eqdg_049_effective_tax_rate_level(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """ETR = TaxExp / Pretax income."""
    return _safe_div(taxexp, ebt)


def f40_eqdg_050_etr_rolling_std_8q(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """8q rolling std of ETR — tax volatility."""
    etr = _safe_div(taxexp, ebt)
    return etr.rolling(8 * QDAYS, min_periods=2 * QDAYS).std()


def f40_eqdg_051_etr_minus_4q_mean(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """ETR - trailing 4q (252-day) mean ETR — sudden rate change flag."""
    etr = _safe_div(taxexp, ebt)
    return etr - etr.rolling(YDAYS, min_periods=QDAYS).mean()


def f40_eqdg_052_etr_zscore_12q(taxexp: pd.Series, ebt: pd.Series) -> pd.Series:
    """ETR z-score over 12q — extreme tax anomalies."""
    etr = _safe_div(taxexp, ebt)
    win = 12 * QDAYS
    mp = max(win // 3, QDAYS)
    m = etr.rolling(win, min_periods=mp).mean()
    sd = etr.rolling(win, min_periods=mp).std()
    return _safe_div(etr - m, sd)


def f40_eqdg_053_taxexp_to_revenue(taxexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Tax expense / Revenue — tax intensity per top-line dollar."""
    return _safe_div(taxexp, revenue)


def f40_eqdg_054_taxliab_to_taxexp_ratio(taxliabilities: pd.Series, taxexp: pd.Series) -> pd.Series:
    """Deferred tax liability / TaxExp — accrued vs paid tax mismatch."""
    return _safe_div(taxliabilities, taxexp)


# ---------- Beneish M-Score components + full (055-064) ----------

def f40_eqdg_055_dsri_beneish(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """DSRI = (AR_t/Rev_t) / (AR_{t-1y}/Rev_{t-1y}) — channel-stuffing index."""
    cur = _safe_div(receivables, revenue)
    prv = _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS))
    return _safe_div(cur, prv)


def f40_eqdg_056_gmi_beneish(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """GMI = GM_{t-1y} / GM_t — gross-margin deterioration index."""
    gm = _safe_div(revenue - cor, revenue)
    return _safe_div(gm.shift(YDAYS), gm)


def f40_eqdg_057_aqi_beneish(assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """AQI = (1 - (CA + PPE)/Assets)_t / same_{t-1y} — softness-of-assets index."""
    nq = 1.0 - _safe_div(assetsc + ppnenet, assets)
    return _safe_div(nq, nq.shift(YDAYS))


def f40_eqdg_058_sgi_beneish(revenue: pd.Series) -> pd.Series:
    """SGI = Revenue_t / Revenue_{t-1y} — sales growth index."""
    return _safe_div(revenue, revenue.shift(YDAYS))


def f40_eqdg_059_depi_beneish(depamor: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """DEPI = DepRate_{t-1y} / DepRate_t — slowed depreciation flag."""
    dr = _safe_div(depamor, depamor + ppnenet)
    return _safe_div(dr.shift(YDAYS), dr)


def f40_eqdg_060_sgai_beneish(sga: pd.Series, revenue: pd.Series) -> pd.Series:
    """SGAI = (SGA/Rev)_t / same_{t-1y} — SGA bloat index."""
    cur = _safe_div(sga, revenue)
    return _safe_div(cur, cur.shift(YDAYS))


def f40_eqdg_061_tata_beneish(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """TATA = (NI - CFO) / Assets — total accruals to total assets."""
    return _safe_div(netinc - ncfo, assets)


def f40_eqdg_062_lvgi_beneish(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """LVGI = Leverage_t / Leverage_{t-1y} — leverage index."""
    lev = _safe_div(liabilities, assets)
    return _safe_div(lev, lev.shift(YDAYS))


def f40_eqdg_063_beneish_m_score_full(receivables: pd.Series, revenue: pd.Series, cor: pd.Series, assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series, depamor: pd.Series, sga: pd.Series, netinc: pd.Series, ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Beneish 8-factor M-score: -4.84 + 0.92*DSRI + 0.528*GMI + 0.404*AQI + 0.892*SGI + 0.115*DEPI - 0.172*SGAI + 4.679*TATA - 0.327*LVGI."""
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS)))
    gm = _safe_div(revenue - cor, revenue)
    gmi = _safe_div(gm.shift(YDAYS), gm)
    nq = 1.0 - _safe_div(assetsc + ppnenet, assets)
    aqi = _safe_div(nq, nq.shift(YDAYS))
    sgi = _safe_div(revenue, revenue.shift(YDAYS))
    dr = _safe_div(depamor, depamor + ppnenet)
    depi = _safe_div(dr.shift(YDAYS), dr)
    sga_r = _safe_div(sga, revenue)
    sgai = _safe_div(sga_r, sga_r.shift(YDAYS))
    tata = _safe_div(netinc - ncfo, assets)
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(YDAYS))
    return -4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi


def f40_eqdg_064_beneish_high_risk_flag(receivables: pd.Series, revenue: pd.Series, cor: pd.Series, assets: pd.Series, assetsc: pd.Series, ppnenet: pd.Series, depamor: pd.Series, sga: pd.Series, netinc: pd.Series, ncfo: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Beneish high-risk flag: M-score > -1.78 (classic threshold)."""
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(YDAYS), revenue.shift(YDAYS)))
    gm = _safe_div(revenue - cor, revenue)
    gmi = _safe_div(gm.shift(YDAYS), gm)
    nq = 1.0 - _safe_div(assetsc + ppnenet, assets)
    aqi = _safe_div(nq, nq.shift(YDAYS))
    sgi = _safe_div(revenue, revenue.shift(YDAYS))
    dr = _safe_div(depamor, depamor + ppnenet)
    depi = _safe_div(dr.shift(YDAYS), dr)
    sga_r = _safe_div(sga, revenue)
    sgai = _safe_div(sga_r, sga_r.shift(YDAYS))
    tata = _safe_div(netinc - ncfo, assets)
    lev = _safe_div(liabilities, assets)
    lvgi = _safe_div(lev, lev.shift(YDAYS))
    m = -4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi
    return (m > -1.78).astype(float)


# ---------- Earnings <-> CFO sign divergence (065-072) ----------

def f40_eqdg_065_ni_pos_cfo_neg_indicator(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Indicator: NetInc > 0 AND CFO < 0 — classic accrual-flagged earnings."""
    flag = (netinc > 0) & (ncfo < 0)
    out = flag.astype(float)
    return out.where(netinc.notna() & ncfo.notna(), np.nan)


def f40_eqdg_066_ni_neg_cfo_pos_indicator(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Indicator: NetInc < 0 AND CFO > 0 — kitchen-sink reverse case."""
    flag = (netinc < 0) & (ncfo > 0)
    out = flag.astype(float)
    return out.where(netinc.notna() & ncfo.notna(), np.nan)


def f40_eqdg_067_signed_divergence_magnitude(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """|NI - CFO| / (|NI| + |CFO|) — normalized accrual divergence magnitude."""
    return _safe_div((netinc - ncfo).abs(), netinc.abs() + ncfo.abs())


def f40_eqdg_068_ni_cfo_rank_divergence_8q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Rolling 8q rank difference of NI vs CFO — divergence in distributional position."""
    win = 8 * QDAYS
    ni_r = netinc.rolling(win, min_periods=QDAYS).rank(pct=True)
    cf_r = ncfo.rolling(win, min_periods=QDAYS).rank(pct=True)
    return ni_r - cf_r


def f40_eqdg_069_ni_cfo_sign_disagree_streak(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Consecutive days of NI/CFO sign disagreement."""
    disagree = (np.sign(netinc) != np.sign(ncfo)).astype(float)
    disagree = disagree.where(netinc.notna() & ncfo.notna(), 0.0)
    grp = (disagree == 0).cumsum()
    return disagree.groupby(grp).cumsum()


def f40_eqdg_070_ni_cfo_sign_disagree_count_8q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Count of days in 8q where NI and CFO disagree in sign."""
    disagree = (np.sign(netinc) != np.sign(ncfo)).astype(float)
    disagree = disagree.where(netinc.notna() & ncfo.notna(), np.nan)
    return disagree.rolling(8 * QDAYS, min_periods=QDAYS).sum()


def f40_eqdg_071_ni_minus_fcf_sign_divergence(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Indicator: NI > 0 AND FCF < 0 — earnings-vs-FCF divergence."""
    flag = (netinc > 0) & (fcf < 0)
    out = flag.astype(float)
    return out.where(netinc.notna() & fcf.notna(), np.nan)


def f40_eqdg_072_ebit_minus_cfo_sign_divergence(ebit: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Indicator: EBIT > 0 AND CFO < 0."""
    flag = (ebit > 0) & (ncfo < 0)
    out = flag.astype(float)
    return out.where(ebit.notna() & ncfo.notna(), np.nan)


# ---------- Earnings <-> sales-growth divergence (073-075) ----------

def f40_eqdg_073_netinc_growth_minus_revenue_growth_yoy(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY NetInc growth minus YoY Revenue growth — NI growing faster than sales = quality risk."""
    g_ni = _safe_div(netinc - netinc.shift(YDAYS), netinc.shift(YDAYS).abs())
    g_rv = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_ni - g_rv


def f40_eqdg_074_ebit_growth_minus_revenue_growth_yoy(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY EBIT growth minus YoY Revenue growth — operating leverage proxy."""
    g_e = _safe_div(ebit - ebit.shift(YDAYS), ebit.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_e - g_r


def f40_eqdg_075_ebitda_growth_minus_revenue_growth_yoy(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY EBITDA growth minus YoY Revenue growth."""
    g_e = _safe_div(ebitda - ebitda.shift(YDAYS), ebitda.shift(YDAYS).abs())
    g_r = _safe_div(revenue - revenue.shift(YDAYS), revenue.shift(YDAYS).abs())
    return g_e - g_r


# ============================================================
#                        REGISTRY
# ============================================================

EARNINGS_QUALITY_DIVERGENCE_BASE_REGISTRY_001_075 = {
    "f40_eqdg_001_sloan_accruals_to_assets": {"inputs": ["netinc", "ncfo", "assets"], "func": f40_eqdg_001_sloan_accruals_to_assets},
    "f40_eqdg_002_sloan_accruals_to_equity": {"inputs": ["netinc", "ncfo", "equity"], "func": f40_eqdg_002_sloan_accruals_to_equity},
    "f40_eqdg_003_sloan_accruals_to_revenue": {"inputs": ["netinc", "ncfo", "revenue"], "func": f40_eqdg_003_sloan_accruals_to_revenue},
    "f40_eqdg_004_cfo_minus_ni_to_assets": {"inputs": ["netinc", "ncfo", "assets"], "func": f40_eqdg_004_cfo_minus_ni_to_assets},
    "f40_eqdg_005_bs_accruals_wc_to_assets": {"inputs": ["workingcapital", "cashneq", "debt", "assets"], "func": f40_eqdg_005_bs_accruals_wc_to_assets},
    "f40_eqdg_006_bs_accruals_wc_to_equity": {"inputs": ["workingcapital", "cashneq", "debt", "equity"], "func": f40_eqdg_006_bs_accruals_wc_to_equity},
    "f40_eqdg_007_bs_accruals_wc_to_revenue": {"inputs": ["workingcapital", "cashneq", "debt", "revenue"], "func": f40_eqdg_007_bs_accruals_wc_to_revenue},
    "f40_eqdg_008_dassets_minus_dcash_to_assets": {"inputs": ["assets", "cashneq"], "func": f40_eqdg_008_dassets_minus_dcash_to_assets},
    "f40_eqdg_009_dnoncash_wc_to_revenue": {"inputs": ["receivables", "inventory", "payables", "revenue"], "func": f40_eqdg_009_dnoncash_wc_to_revenue},
    "f40_eqdg_010_dar_plus_dinv_minus_dap_to_drevenue": {"inputs": ["receivables", "inventory", "payables", "revenue"], "func": f40_eqdg_010_dar_plus_dinv_minus_dap_to_drevenue},
    "f40_eqdg_011_modified_jones_residual_proxy": {"inputs": ["netinc", "ncfo", "revenue", "receivables", "assets"], "func": f40_eqdg_011_modified_jones_residual_proxy},
    "f40_eqdg_012_discretionary_accruals_ppne_adjusted": {"inputs": ["netinc", "ncfo", "ppnenet", "assets"], "func": f40_eqdg_012_discretionary_accruals_ppne_adjusted},
    "f40_eqdg_013_cfo_to_netinc": {"inputs": ["ncfo", "netinc"], "func": f40_eqdg_013_cfo_to_netinc},
    "f40_eqdg_014_fcf_to_netinc": {"inputs": ["fcf", "netinc"], "func": f40_eqdg_014_fcf_to_netinc},
    "f40_eqdg_015_ocf_to_ebitda": {"inputs": ["ncfo", "ebitda"], "func": f40_eqdg_015_ocf_to_ebitda},
    "f40_eqdg_016_cfo_to_revenue": {"inputs": ["ncfo", "revenue"], "func": f40_eqdg_016_cfo_to_revenue},
    "f40_eqdg_017_fcf_to_revenue": {"inputs": ["fcf", "revenue"], "func": f40_eqdg_017_fcf_to_revenue},
    "f40_eqdg_018_cfo_to_assets": {"inputs": ["ncfo", "assets"], "func": f40_eqdg_018_cfo_to_assets},
    "f40_eqdg_019_fcf_to_assets": {"inputs": ["fcf", "assets"], "func": f40_eqdg_019_fcf_to_assets},
    "f40_eqdg_020_cfo_to_ebit": {"inputs": ["ncfo", "ebit"], "func": f40_eqdg_020_cfo_to_ebit},
    "f40_eqdg_021_cfo_to_equity": {"inputs": ["ncfo", "equity"], "func": f40_eqdg_021_cfo_to_equity},
    "f40_eqdg_022_one_minus_cfo_over_ni": {"inputs": ["ncfo", "netinc"], "func": f40_eqdg_022_one_minus_cfo_over_ni},
    "f40_eqdg_023_depamor_to_ebitda": {"inputs": ["depamor", "ebitda"], "func": f40_eqdg_023_depamor_to_ebitda},
    "f40_eqdg_024_depamor_to_ebit": {"inputs": ["depamor", "ebit"], "func": f40_eqdg_024_depamor_to_ebit},
    "f40_eqdg_025_sbcomp_to_revenue": {"inputs": ["sbcomp", "revenue"], "func": f40_eqdg_025_sbcomp_to_revenue},
    "f40_eqdg_026_sbcomp_to_netinc": {"inputs": ["sbcomp", "netinc"], "func": f40_eqdg_026_sbcomp_to_netinc},
    "f40_eqdg_027_sbcomp_to_cfo": {"inputs": ["sbcomp", "ncfo"], "func": f40_eqdg_027_sbcomp_to_cfo},
    "f40_eqdg_028_sbcomp_to_opex": {"inputs": ["sbcomp", "opex"], "func": f40_eqdg_028_sbcomp_to_opex},
    "f40_eqdg_029_capex_minus_depamor_to_assets": {"inputs": ["capex", "depamor", "assets"], "func": f40_eqdg_029_capex_minus_depamor_to_assets},
    "f40_eqdg_030_capex_to_depamor": {"inputs": ["capex", "depamor"], "func": f40_eqdg_030_capex_to_depamor},
    "f40_eqdg_031_depamor_to_ppnenet": {"inputs": ["depamor", "ppnenet"], "func": f40_eqdg_031_depamor_to_ppnenet},
    "f40_eqdg_032_noncash_earnings_share": {"inputs": ["ncfo", "netinc"], "func": f40_eqdg_032_noncash_earnings_share},
    "f40_eqdg_033_netinc_autocorr_1lag_8q": {"inputs": ["netinc"], "func": f40_eqdg_033_netinc_autocorr_1lag_8q},
    "f40_eqdg_034_eps_autocorr_1lag_8q": {"inputs": ["eps"], "func": f40_eqdg_034_eps_autocorr_1lag_8q},
    "f40_eqdg_035_netinc_growth_std_8q": {"inputs": ["netinc"], "func": f40_eqdg_035_netinc_growth_std_8q},
    "f40_eqdg_036_eps_growth_std_8q": {"inputs": ["eps"], "func": f40_eqdg_036_eps_growth_std_8q},
    "f40_eqdg_037_netinc_trend_residual_std_12q": {"inputs": ["netinc"], "func": f40_eqdg_037_netinc_trend_residual_std_12q},
    "f40_eqdg_038_netinc_ar1_coef_proxy_12q": {"inputs": ["netinc"], "func": f40_eqdg_038_netinc_ar1_coef_proxy_12q},
    "f40_eqdg_039_revenue_ar1_coef_proxy_12q": {"inputs": ["revenue"], "func": f40_eqdg_039_revenue_ar1_coef_proxy_12q},
    "f40_eqdg_040_ebit_ar1_coef_proxy_12q": {"inputs": ["ebit"], "func": f40_eqdg_040_ebit_ar1_coef_proxy_12q},
    "f40_eqdg_041_ni_cv_to_cfo_cv_ratio_8q": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_041_ni_cv_to_cfo_cv_ratio_8q},
    "f40_eqdg_042_ni_cv_to_revenue_cv_ratio_8q": {"inputs": ["netinc", "revenue"], "func": f40_eqdg_042_ni_cv_to_revenue_cv_ratio_8q},
    "f40_eqdg_043_netinc_rolling_skew_12q": {"inputs": ["netinc"], "func": f40_eqdg_043_netinc_rolling_skew_12q},
    "f40_eqdg_044_netinc_rolling_kurtosis_12q": {"inputs": ["netinc"], "func": f40_eqdg_044_netinc_rolling_kurtosis_12q},
    "f40_eqdg_045_cfo_rolling_skew_12q": {"inputs": ["ncfo"], "func": f40_eqdg_045_cfo_rolling_skew_12q},
    "f40_eqdg_046_cfo_rolling_kurtosis_12q": {"inputs": ["ncfo"], "func": f40_eqdg_046_cfo_rolling_kurtosis_12q},
    "f40_eqdg_047_ni_minus_cfo_smoothness_zscore_12q": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_047_ni_minus_cfo_smoothness_zscore_12q},
    "f40_eqdg_048_eps_smoothness_z_vs_revenue": {"inputs": ["eps", "revenue"], "func": f40_eqdg_048_eps_smoothness_z_vs_revenue},
    "f40_eqdg_049_effective_tax_rate_level": {"inputs": ["taxexp", "ebt"], "func": f40_eqdg_049_effective_tax_rate_level},
    "f40_eqdg_050_etr_rolling_std_8q": {"inputs": ["taxexp", "ebt"], "func": f40_eqdg_050_etr_rolling_std_8q},
    "f40_eqdg_051_etr_minus_4q_mean": {"inputs": ["taxexp", "ebt"], "func": f40_eqdg_051_etr_minus_4q_mean},
    "f40_eqdg_052_etr_zscore_12q": {"inputs": ["taxexp", "ebt"], "func": f40_eqdg_052_etr_zscore_12q},
    "f40_eqdg_053_taxexp_to_revenue": {"inputs": ["taxexp", "revenue"], "func": f40_eqdg_053_taxexp_to_revenue},
    "f40_eqdg_054_taxliab_to_taxexp_ratio": {"inputs": ["taxliabilities", "taxexp"], "func": f40_eqdg_054_taxliab_to_taxexp_ratio},
    "f40_eqdg_055_dsri_beneish": {"inputs": ["receivables", "revenue"], "func": f40_eqdg_055_dsri_beneish},
    "f40_eqdg_056_gmi_beneish": {"inputs": ["revenue", "cor"], "func": f40_eqdg_056_gmi_beneish},
    "f40_eqdg_057_aqi_beneish": {"inputs": ["assets", "assetsc", "ppnenet"], "func": f40_eqdg_057_aqi_beneish},
    "f40_eqdg_058_sgi_beneish": {"inputs": ["revenue"], "func": f40_eqdg_058_sgi_beneish},
    "f40_eqdg_059_depi_beneish": {"inputs": ["depamor", "ppnenet"], "func": f40_eqdg_059_depi_beneish},
    "f40_eqdg_060_sgai_beneish": {"inputs": ["sga", "revenue"], "func": f40_eqdg_060_sgai_beneish},
    "f40_eqdg_061_tata_beneish": {"inputs": ["netinc", "ncfo", "assets"], "func": f40_eqdg_061_tata_beneish},
    "f40_eqdg_062_lvgi_beneish": {"inputs": ["liabilities", "assets"], "func": f40_eqdg_062_lvgi_beneish},
    "f40_eqdg_063_beneish_m_score_full": {"inputs": ["receivables", "revenue", "cor", "assets", "assetsc", "ppnenet", "depamor", "sga", "netinc", "ncfo", "liabilities"], "func": f40_eqdg_063_beneish_m_score_full},
    "f40_eqdg_064_beneish_high_risk_flag": {"inputs": ["receivables", "revenue", "cor", "assets", "assetsc", "ppnenet", "depamor", "sga", "netinc", "ncfo", "liabilities"], "func": f40_eqdg_064_beneish_high_risk_flag},
    "f40_eqdg_065_ni_pos_cfo_neg_indicator": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_065_ni_pos_cfo_neg_indicator},
    "f40_eqdg_066_ni_neg_cfo_pos_indicator": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_066_ni_neg_cfo_pos_indicator},
    "f40_eqdg_067_signed_divergence_magnitude": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_067_signed_divergence_magnitude},
    "f40_eqdg_068_ni_cfo_rank_divergence_8q": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_068_ni_cfo_rank_divergence_8q},
    "f40_eqdg_069_ni_cfo_sign_disagree_streak": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_069_ni_cfo_sign_disagree_streak},
    "f40_eqdg_070_ni_cfo_sign_disagree_count_8q": {"inputs": ["netinc", "ncfo"], "func": f40_eqdg_070_ni_cfo_sign_disagree_count_8q},
    "f40_eqdg_071_ni_minus_fcf_sign_divergence": {"inputs": ["netinc", "fcf"], "func": f40_eqdg_071_ni_minus_fcf_sign_divergence},
    "f40_eqdg_072_ebit_minus_cfo_sign_divergence": {"inputs": ["ebit", "ncfo"], "func": f40_eqdg_072_ebit_minus_cfo_sign_divergence},
    "f40_eqdg_073_netinc_growth_minus_revenue_growth_yoy": {"inputs": ["netinc", "revenue"], "func": f40_eqdg_073_netinc_growth_minus_revenue_growth_yoy},
    "f40_eqdg_074_ebit_growth_minus_revenue_growth_yoy": {"inputs": ["ebit", "revenue"], "func": f40_eqdg_074_ebit_growth_minus_revenue_growth_yoy},
    "f40_eqdg_075_ebitda_growth_minus_revenue_growth_yoy": {"inputs": ["ebitda", "revenue"], "func": f40_eqdg_075_ebitda_growth_minus_revenue_growth_yoy},
}
