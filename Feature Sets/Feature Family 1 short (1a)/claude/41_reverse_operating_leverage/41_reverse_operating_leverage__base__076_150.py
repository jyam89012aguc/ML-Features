"""reverse_operating_leverage base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Lane: cost-structure rigidity / degree of operating leverage at multi-year peak.
Inputs: SF1 quarterly fundamentals only. PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N).
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


def _winsorize(s, lower=0.01, upper=0.99):
    lo = s.quantile(lower)
    hi = s.quantile(upper)
    return s.clip(lower=lo, upper=hi)


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ============================================================
#                    BASE FEATURES 076-150
# ============================================================

def f41_rolv_076_da_to_ebit_cv_2y(ebit: pd.Series, depamor: pd.Series) -> pd.Series:
    """CV of D&A/EBIT 2Y — stability of capital-charge burden."""
    r = _safe_div(depamor, ebit)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_077_da_growth_minus_rev_growth_1y(revenue: pd.Series, depamor: pd.Series) -> pd.Series:
    """D&A growth - revenue growth 1Y — locked-in depreciation vs sales."""
    gd = depamor.diff(YDAYS) / depamor.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gd - gr
    return expr

def f41_rolv_078_capex_intensity_level(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Capex/Revenue — capital intensity (high = high DOL)."""
    expr = _safe_div(capex.abs(), revenue)
    return expr

def f41_rolv_079_capex_intensity_cv_2y(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """CV of capex/revenue 2Y — capex-rhythm stability (fixed plan)."""
    r = _safe_div(capex.abs(), revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_080_capex_growth_minus_rev_growth_1y(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Capex growth - revenue growth 1Y — capex inflexibility."""
    gc = capex.abs().diff(YDAYS) / capex.abs().shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gc - gr
    return expr

def f41_rolv_081_capex_stickiness_on_decline_1y(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Capex growth / (-revenue growth) when revenue falls — capex commitment lag."""
    gc = capex.abs().diff(YDAYS) / capex.abs().shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gc.where(mask), -gr.where(mask))
    return expr

def f41_rolv_082_capex_to_da_ratio(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    """Capex/D&A — reinvestment intensity vs depreciation (locked maintenance burden)."""
    expr = _safe_div(capex.abs(), depamor)
    return expr

def f41_rolv_083_capex_to_ncfo_ratio(capex: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Capex/NCFO — cash committed to PP&E vs op cash flow."""
    expr = _safe_div(capex.abs(), ncfo)
    return expr

def f41_rolv_084_capex_intensity_z_5y(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Z-score of capex intensity vs 5Y own history."""
    r = _safe_div(capex.abs(), revenue)
    expr = _rolling_zscore(r, 1260)
    return expr

def f41_rolv_085_future_da_commitment_proxy(capex: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """(Capex_TTM4q sum)/PPNE_net — future depreciation acceleration proxy."""
    ttm = capex.abs().rolling(YDAYS, min_periods=QDAYS).sum()
    expr = _safe_div(ttm, ppnenet)
    return expr

def f41_rolv_086_ppne_to_rev_intensity(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """PPNE_net/Revenue — fixed asset intensity (fixed-cost generator)."""
    expr = _safe_div(ppnenet, revenue)
    return expr

def f41_rolv_087_ppne_to_assets_share(assets: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """PPNE_net/Assets — capital structure tilt."""
    expr = _safe_div(ppnenet, assets)
    return expr

def f41_rolv_088_asset_turnover_level(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Revenue/Assets — inverse capital intensity (low turnover = high DOL risk)."""
    expr = _safe_div(revenue, assets)
    return expr

def f41_rolv_089_asset_turnover_cv_2y(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """CV of asset turnover 2Y — stability of asset productivity."""
    r = _safe_div(revenue, assets)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_090_ppne_turnover_level(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """Revenue/PPNE_net — fixed-asset utilization."""
    expr = _safe_div(revenue, ppnenet)
    return expr

def f41_rolv_091_ppne_turnover_cv_2y(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """CV of revenue/PPNE_net 2Y — utilization stability."""
    r = _safe_div(revenue, ppnenet)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_092_ppne_growth_minus_rev_growth_1y(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    """PPNE growth - revenue growth 1Y — capital overhang growing."""
    gp_ = ppnenet.diff(YDAYS) / ppnenet.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gp_ - gr
    return expr

def f41_rolv_093_intangibles_to_assets_share(assets: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Intangibles/Assets — soft-asset share, harder-to-flex."""
    expr = _safe_div(intangibles, assets)
    return expr

def f41_rolv_094_intangibles_growth_minus_rev_growth_1y(revenue: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Intangibles growth - revenue growth 1Y — soft-asset overhang."""
    gi = intangibles.diff(YDAYS) / intangibles.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gi - gr
    return expr

def f41_rolv_095_invcap_to_rev_intensity(revenue: pd.Series, invcap: pd.Series) -> pd.Series:
    """Invested capital / Revenue — total capital intensity proxy."""
    expr = _safe_div(invcap, revenue)
    return expr

def f41_rolv_096_wc_to_rev_intensity(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Working capital / Revenue — WC tie-up per dollar of sales."""
    expr = _safe_div(workingcapital, revenue)
    return expr

def f41_rolv_097_wc_to_rev_cv_2y(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """CV of WC/Revenue 2Y — WC scheme rigidity."""
    r = _safe_div(workingcapital, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_098_wc_growth_minus_rev_growth_1y(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """WC growth - rev growth 1Y — WC inflating beyond sales (sticky working capital)."""
    gw = workingcapital.diff(YDAYS) / workingcapital.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gw - gr
    return expr

def f41_rolv_099_inventory_to_rev_level(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Inventory/Revenue — inventory days proxy."""
    expr = _safe_div(inventory, revenue)
    return expr

def f41_rolv_100_inventory_growth_minus_rev_growth_1y(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Inventory growth - revenue growth 1Y — unwanted inventory accumulation."""
    gi = inventory.diff(YDAYS) / inventory.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gi - gr
    return expr

def f41_rolv_101_inventory_buildup_on_decline_1y(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Inv growth / (-rev growth) when rev declines — inventory-revenue elasticity in stress."""
    gi = inventory.diff(YDAYS) / inventory.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gi.where(mask), -gr.where(mask))
    return expr

def f41_rolv_102_receivables_growth_minus_rev_growth_1y(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """Receivables growth - revenue growth 1Y — collection drag, sticky receivables."""
    gr_ = receivables.diff(YDAYS) / receivables.shift(YDAYS).replace(0, np.nan)
    gv = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gr_ - gv
    return expr

def f41_rolv_103_payables_growth_minus_cogs_growth_1y(cor: pd.Series, payables: pd.Series) -> pd.Series:
    """Payables growth - COGS growth 1Y — supplier-flex proxy (negative = supplier tightening)."""
    gp_ = payables.diff(YDAYS) / payables.shift(YDAYS).replace(0, np.nan)
    gc = cor.diff(YDAYS) / cor.shift(YDAYS).replace(0, np.nan)
    expr = gp_ - gc
    return expr

def f41_rolv_104_receivables_to_rev_level(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    """Receivables/Revenue — DSO proxy at peak."""
    expr = _safe_div(receivables, revenue)
    return expr

def f41_rolv_105_inventory_rev_elasticity_2y(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Rolling 2Y log-log slope d ln Inventory / d ln Revenue."""
    ln = _safe_log(inventory); lr = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=QDAYS).cov(lr)
    var = lr.rolling(2 * YDAYS, min_periods=QDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_106_sbc_to_rev_level(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """SBC/Revenue — equity-comp burden share."""
    expr = _safe_div(sbcomp, revenue)
    return expr

def f41_rolv_107_sbc_to_rev_cv_2y(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """CV of SBC/Revenue 2Y — SBC scheme rigidity."""
    r = _safe_div(sbcomp, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_108_sbc_growth_minus_rev_growth_1y(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """SBC growth - revenue growth 1Y — SBC accelerating vs sales (sticky comp)."""
    gs = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gs - gr
    return expr

def f41_rolv_109_sbc_stickiness_on_decline_1y(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """SBC growth / (-rev growth) on rev declines — SBC inflexibility."""
    gs = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gs.where(mask), -gr.where(mask))
    return expr

def f41_rolv_110_sbc_to_opex_share(opex: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """SBC/OPEX — share of opex tied to equity comp."""
    expr = _safe_div(sbcomp, opex)
    return expr

def f41_rolv_111_sbc_to_ncfo_addback_share(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """SBC/|NCFO| — SBC contribution to non-cash operating income (cosmetics on cash)."""
    expr = _safe_div(sbcomp, ncfo.abs())
    return expr

def f41_rolv_112_sbc_to_netinc_addback_share(sbcomp: pd.Series, netinc: pd.Series) -> pd.Series:
    """SBC/|NetInc| — SBC vs reported earnings."""
    expr = _safe_div(sbcomp, netinc.abs())
    return expr

def f41_rolv_113_sbc_rev_correlation_2y(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """Rolling 2Y corr dSBC vs dRevenue — coupling of SBC to sales."""
    ds = sbcomp.diff(QDAYS)
    dr = revenue.diff(QDAYS)
    expr = ds.rolling(2 * YDAYS, min_periods=QDAYS).corr(dr)
    return expr

def f41_rolv_114_sbc_growth_5y_avg(sbcomp: pd.Series) -> pd.Series:
    """TTM SBC growth average over 5Y — long-cycle SBC inflation trend."""
    g = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    expr = g.rolling(1260, min_periods=YDAYS).mean()
    return expr

def f41_rolv_115_sbc_to_shareswadil_growth_couple(sbcomp: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Corr 2Y between SBC growth and diluted-share growth — SBC-driven dilution coupling."""
    gs = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    gd = shareswadil.diff(YDAYS) / shareswadil.shift(YDAYS).replace(0, np.nan)
    expr = gs.rolling(2 * YDAYS, min_periods=QDAYS).corr(gd)
    return expr

def f41_rolv_116_dol_ebit_horizon_1q_z_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Z-score of 1-quarter DOL_EBIT vs 5Y — short-shock regime."""
    rn = ebit.diff(QDAYS) / ebit.shift(QDAYS).replace(0, np.nan)
    rd = revenue.diff(QDAYS) / revenue.shift(QDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_117_dol_ebit_horizon_1y_z_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Z-score of 1Y DOL_EBIT vs 5Y — annual regime."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_118_dol_ebit_horizon_2y_z_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Z-score of 2Y DOL_EBIT vs 5Y — multi-year regime."""
    rn = ebit.diff(2 * YDAYS) / ebit.shift(2 * YDAYS).replace(0, np.nan)
    rd = revenue.diff(2 * YDAYS) / revenue.shift(2 * YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_119_dol_ebitda_horizon_1q_z_5y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z of quarterly DOL_EBITDA vs 5Y."""
    rn = ebitda.diff(QDAYS) / ebitda.shift(QDAYS).replace(0, np.nan)
    rd = revenue.diff(QDAYS) / revenue.shift(QDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_120_dol_gp_horizon_1y_z_5y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Z of 1Y DOL_GP vs 5Y."""
    rn = gp.diff(YDAYS) / gp.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_121_dol_netinc_horizon_1y_z_5y(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Z of 1Y DOL_NetInc vs 5Y — total-leverage regime z."""
    rn = netinc.diff(YDAYS) / netinc.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_122_dol_ebit_above_threshold_rate_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Fraction of 2Y window where DOL_EBIT 1Y > 5 — high-leverage occupancy."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flag = (dol > 5.0).astype(float)
    expr = flag.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_123_dol_ebit_below_threshold_rate_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Fraction of 2Y window where DOL_EBIT < -2 — leverage-reversal regime."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flag = (dol < -2.0).astype(float)
    expr = flag.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_124_dol_sign_flip_count_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Count of DOL_EBIT sign flips over 5Y window — regime instability."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flips = (np.sign(dol) != np.sign(dol.shift(QDAYS))).astype(float)
    expr = flips.rolling(1260, min_periods=YDAYS).sum()
    return expr

def f41_rolv_125_dol_ebit_extreme_quantile_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """5Y rolling 95th percentile of |DOL_EBIT 1Y| — extreme operating leverage outliers."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd).abs()
    expr = dol.rolling(1260, min_periods=YDAYS).quantile(0.95)
    return expr

def f41_rolv_126_cost_flex_composite_z(revenue: pd.Series, sga: pd.Series, rnd: pd.Series, capex: pd.Series) -> pd.Series:
    """Cost-flex composite z (lower=more rigid): mean of -|stickiness| for SGA, RnD, Capex."""
    def stick(x):
        gx = x.diff(YDAYS) / x.shift(YDAYS).replace(0, np.nan)
        gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
        return _safe_div(gx.where(gr < 0), -gr.where(gr < 0))
    z1 = _rolling_zscore(stick(sga), 1260)
    z2 = _rolling_zscore(stick(rnd), 1260)
    z3 = _rolling_zscore(stick(capex.abs()), 1260)
    expr = (z1.fillna(0) + z2.fillna(0) + z3.fillna(0)) / 3.0
    return expr

def f41_rolv_127_sales_cost_convergence_speed_2y(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """Slope of (OPEX/Rev) over 2Y — speed at which cost share converges toward 1 (margin squeeze pace)."""
    r = _safe_div(opex, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return expr

def f41_rolv_128_sales_cost_convergence_speed_5y(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """Slope of (OPEX/Rev) 5Y — long-cycle cost-share creep."""
    r = _safe_div(opex, revenue)
    expr = _rolling_slope(r, 1260)
    return expr

def f41_rolv_129_sga_share_slope_2y(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """Slope of SGA/Revenue 2Y — secular SGA-creep."""
    r = _safe_div(sga, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return expr

def f41_rolv_130_rnd_share_slope_2y(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """Slope of RnD/Revenue 2Y."""
    r = _safe_div(rnd, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return expr

def f41_rolv_131_cogs_share_slope_2y(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Slope of COGS/Revenue 2Y — variable-cost share trajectory."""
    r = _safe_div(cor, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return expr

def f41_rolv_132_da_share_slope_2y(revenue: pd.Series, depamor: pd.Series) -> pd.Series:
    """Slope of D&A/Revenue 2Y."""
    r = _safe_div(depamor, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return expr

def f41_rolv_133_capex_share_slope_2y(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Slope of capex/Revenue 2Y."""
    r = _safe_div(capex.abs(), revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return expr

def f41_rolv_134_opex_share_above_one_indicator(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """Indicator: OPEX/Revenue > 1 (operating loss regime)."""
    r = _safe_div(opex, revenue)
    expr = (r > 1.0).astype(float)
    return expr

def f41_rolv_135_cost_share_dispersion_across_buckets(revenue: pd.Series, sga: pd.Series, cor: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    """Std across (SGA/Rev, COR/Rev, RnD/Rev, D&A/Rev) at each time — concentration vs spread."""
    r1 = _safe_div(sga, revenue)
    r2 = _safe_div(cor, revenue)
    r3 = _safe_div(rnd, revenue)
    r4 = _safe_div(depamor, revenue)
    df = pd.concat([r1, r2, r3, r4], axis=1)
    expr = df.std(axis=1)
    return expr

def f41_rolv_136_ebit_margin_quarterly_compression_rate(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Negative of dEBIT_margin per quarter — speed of margin compression."""
    m = _safe_div(ebit, revenue)
    expr = -m.diff(QDAYS)
    return expr

def f41_rolv_137_ebit_margin_annual_compression_rate(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Negative dEBIT_margin per year — annual compression rate."""
    m = _safe_div(ebit, revenue)
    expr = -m.diff(YDAYS)
    return expr

def f41_rolv_138_quarters_to_negative_ebit_linear(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """EBIT_margin / quarterly compression rate (positive = quarters to zero)."""
    m = _safe_div(ebit, revenue)
    comp = -m.diff(QDAYS).replace(0, np.nan)
    expr = _safe_div(m, comp)
    return expr

def f41_rolv_139_years_to_negative_ebit_linear(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """EBIT_margin / annual compression rate — years to zero EBIT."""
    m = _safe_div(ebit, revenue)
    comp = -m.diff(YDAYS).replace(0, np.nan)
    expr = _safe_div(m, comp)
    return expr

def f41_rolv_140_dupont_op_lev_ebit_x_assetturn(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """EBIT margin x asset turnover — operating ROA building block."""
    m = _safe_div(ebit, revenue)
    at = _safe_div(revenue, assets)
    expr = m * at
    return expr

def f41_rolv_141_dupont_op_lev_cv_2y(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """CV of (EBIT margin x asset turnover) 2Y — operating ROA stability."""
    m = _safe_div(ebit, revenue)
    at = _safe_div(revenue, assets)
    x = m * at
    mn = x.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = x.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / mn.replace(0, np.nan)
    return expr

def f41_rolv_142_financial_leverage_assets_to_equity(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Assets/Equity — financial leverage multiplier (compounds DOL into DTL)."""
    expr = _safe_div(assets, equity)
    return expr

def f41_rolv_143_total_leverage_dtl_proxy_1y(revenue: pd.Series, ebit: pd.Series, assets: pd.Series, equity: pd.Series) -> pd.Series:
    """DOL_EBIT(1Y) x Assets/Equity — degree of total leverage proxy."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flev = _safe_div(assets, equity)
    expr = dol * flev
    return expr

def f41_rolv_144_debt_to_invcap_share(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    """Debt/InvCap — financing share that fixes interest obligations."""
    expr = _safe_div(debt, invcap)
    return expr

def f41_rolv_145_interest_burden_to_ebit_proxy(ebit: pd.Series, ebt: pd.Series) -> pd.Series:
    """1 - EBT/EBIT — interest-burden complement (high=high fixed financial cost)."""
    expr = 1.0 - _safe_div(ebt, ebit)
    return expr

def f41_rolv_146_contribution_margin_vol_to_dol_ratio(revenue: pd.Series, ebit: pd.Series, gp: pd.Series) -> pd.Series:
    """Std(GP margin 2Y) / |DOL_EBIT 2Y| — vol-adjusted operating leverage."""
    gpm = _safe_div(gp, revenue)
    sd = gpm.rolling(2 * YDAYS, min_periods=QDAYS).std()
    rn = ebit.diff(2 * YDAYS) / ebit.shift(2 * YDAYS).replace(0, np.nan)
    rd = revenue.diff(2 * YDAYS) / revenue.shift(2 * YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd).abs()
    expr = _safe_div(sd, dol)
    return expr

def f41_rolv_147_ncfo_to_ebit_quality_gap(ebit: pd.Series, ncfo: pd.Series) -> pd.Series:
    """NCFO/EBIT — operating-cash conversion (low conversion + high DOL = blowup recipe)."""
    expr = _safe_div(ncfo, ebit)
    return expr

def f41_rolv_148_fcf_to_rev_cushion(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """FCF/Revenue — cash margin cushion (low cushion increases blowup risk under DOL)."""
    expr = _safe_div(fcf, revenue)
    return expr

def f41_rolv_149_op_lev_x_dilution_pressure(revenue: pd.Series, ebit: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """DOL_EBIT 1Y x sharesbas growth 1Y — leverage compounded by dilution pressure."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    g = sharesbas.diff(YDAYS) / sharesbas.shift(YDAYS).replace(0, np.nan)
    expr = dol * g
    return expr

def f41_rolv_150_reverse_op_lev_terminal_score(revenue: pd.Series, ebit: pd.Series, sga: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    """Composite z: high fixed-cost share, narrow breakeven, downside DOL_EBIT — terminal rigidity score."""
    fc = sga.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    fc_share = _safe_div(fc, revenue)
    m = _safe_div(ebit, revenue)
    drev = revenue.diff(YDAYS)
    debit = ebit.diff(YDAYS)
    dec = _safe_div(debit.where(drev < 0), drev.where(drev < 0))
    z1 = _rolling_zscore(fc_share, 1260)
    z2 = -_rolling_zscore(m, 1260)
    z3 = -_rolling_zscore(dec, 1260)
    expr = (z1.fillna(0) + z2.fillna(0) + z3.fillna(0)) / 3.0
    return expr


# ============================================================
#                        REGISTRY
# ============================================================

REVERSE_OPERATING_LEVERAGE_BASE_REGISTRY_076_150 = {
    "f41_rolv_076_da_to_ebit_cv_2y": {"inputs": ["ebit", "depamor"], "func": f41_rolv_076_da_to_ebit_cv_2y},
    "f41_rolv_077_da_growth_minus_rev_growth_1y": {"inputs": ["revenue", "depamor"], "func": f41_rolv_077_da_growth_minus_rev_growth_1y},
    "f41_rolv_078_capex_intensity_level": {"inputs": ["revenue", "capex"], "func": f41_rolv_078_capex_intensity_level},
    "f41_rolv_079_capex_intensity_cv_2y": {"inputs": ["revenue", "capex"], "func": f41_rolv_079_capex_intensity_cv_2y},
    "f41_rolv_080_capex_growth_minus_rev_growth_1y": {"inputs": ["revenue", "capex"], "func": f41_rolv_080_capex_growth_minus_rev_growth_1y},
    "f41_rolv_081_capex_stickiness_on_decline_1y": {"inputs": ["revenue", "capex"], "func": f41_rolv_081_capex_stickiness_on_decline_1y},
    "f41_rolv_082_capex_to_da_ratio": {"inputs": ["capex", "depamor"], "func": f41_rolv_082_capex_to_da_ratio},
    "f41_rolv_083_capex_to_ncfo_ratio": {"inputs": ["capex", "ncfo"], "func": f41_rolv_083_capex_to_ncfo_ratio},
    "f41_rolv_084_capex_intensity_z_5y": {"inputs": ["revenue", "capex"], "func": f41_rolv_084_capex_intensity_z_5y},
    "f41_rolv_085_future_da_commitment_proxy": {"inputs": ["capex", "ppnenet"], "func": f41_rolv_085_future_da_commitment_proxy},
    "f41_rolv_086_ppne_to_rev_intensity": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_086_ppne_to_rev_intensity},
    "f41_rolv_087_ppne_to_assets_share": {"inputs": ["assets", "ppnenet"], "func": f41_rolv_087_ppne_to_assets_share},
    "f41_rolv_088_asset_turnover_level": {"inputs": ["revenue", "assets"], "func": f41_rolv_088_asset_turnover_level},
    "f41_rolv_089_asset_turnover_cv_2y": {"inputs": ["revenue", "assets"], "func": f41_rolv_089_asset_turnover_cv_2y},
    "f41_rolv_090_ppne_turnover_level": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_090_ppne_turnover_level},
    "f41_rolv_091_ppne_turnover_cv_2y": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_091_ppne_turnover_cv_2y},
    "f41_rolv_092_ppne_growth_minus_rev_growth_1y": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_092_ppne_growth_minus_rev_growth_1y},
    "f41_rolv_093_intangibles_to_assets_share": {"inputs": ["assets", "intangibles"], "func": f41_rolv_093_intangibles_to_assets_share},
    "f41_rolv_094_intangibles_growth_minus_rev_growth_1y": {"inputs": ["revenue", "intangibles"], "func": f41_rolv_094_intangibles_growth_minus_rev_growth_1y},
    "f41_rolv_095_invcap_to_rev_intensity": {"inputs": ["revenue", "invcap"], "func": f41_rolv_095_invcap_to_rev_intensity},
    "f41_rolv_096_wc_to_rev_intensity": {"inputs": ["revenue", "workingcapital"], "func": f41_rolv_096_wc_to_rev_intensity},
    "f41_rolv_097_wc_to_rev_cv_2y": {"inputs": ["revenue", "workingcapital"], "func": f41_rolv_097_wc_to_rev_cv_2y},
    "f41_rolv_098_wc_growth_minus_rev_growth_1y": {"inputs": ["revenue", "workingcapital"], "func": f41_rolv_098_wc_growth_minus_rev_growth_1y},
    "f41_rolv_099_inventory_to_rev_level": {"inputs": ["revenue", "inventory"], "func": f41_rolv_099_inventory_to_rev_level},
    "f41_rolv_100_inventory_growth_minus_rev_growth_1y": {"inputs": ["revenue", "inventory"], "func": f41_rolv_100_inventory_growth_minus_rev_growth_1y},
    "f41_rolv_101_inventory_buildup_on_decline_1y": {"inputs": ["revenue", "inventory"], "func": f41_rolv_101_inventory_buildup_on_decline_1y},
    "f41_rolv_102_receivables_growth_minus_rev_growth_1y": {"inputs": ["revenue", "receivables"], "func": f41_rolv_102_receivables_growth_minus_rev_growth_1y},
    "f41_rolv_103_payables_growth_minus_cogs_growth_1y": {"inputs": ["cor", "payables"], "func": f41_rolv_103_payables_growth_minus_cogs_growth_1y},
    "f41_rolv_104_receivables_to_rev_level": {"inputs": ["revenue", "receivables"], "func": f41_rolv_104_receivables_to_rev_level},
    "f41_rolv_105_inventory_rev_elasticity_2y": {"inputs": ["revenue", "inventory"], "func": f41_rolv_105_inventory_rev_elasticity_2y},
    "f41_rolv_106_sbc_to_rev_level": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_106_sbc_to_rev_level},
    "f41_rolv_107_sbc_to_rev_cv_2y": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_107_sbc_to_rev_cv_2y},
    "f41_rolv_108_sbc_growth_minus_rev_growth_1y": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_108_sbc_growth_minus_rev_growth_1y},
    "f41_rolv_109_sbc_stickiness_on_decline_1y": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_109_sbc_stickiness_on_decline_1y},
    "f41_rolv_110_sbc_to_opex_share": {"inputs": ["opex", "sbcomp"], "func": f41_rolv_110_sbc_to_opex_share},
    "f41_rolv_111_sbc_to_ncfo_addback_share": {"inputs": ["sbcomp", "ncfo"], "func": f41_rolv_111_sbc_to_ncfo_addback_share},
    "f41_rolv_112_sbc_to_netinc_addback_share": {"inputs": ["sbcomp", "netinc"], "func": f41_rolv_112_sbc_to_netinc_addback_share},
    "f41_rolv_113_sbc_rev_correlation_2y": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_113_sbc_rev_correlation_2y},
    "f41_rolv_114_sbc_growth_5y_avg": {"inputs": ["sbcomp"], "func": f41_rolv_114_sbc_growth_5y_avg},
    "f41_rolv_115_sbc_to_shareswadil_growth_couple": {"inputs": ["sbcomp", "shareswadil"], "func": f41_rolv_115_sbc_to_shareswadil_growth_couple},
    "f41_rolv_116_dol_ebit_horizon_1q_z_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_116_dol_ebit_horizon_1q_z_5y},
    "f41_rolv_117_dol_ebit_horizon_1y_z_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_117_dol_ebit_horizon_1y_z_5y},
    "f41_rolv_118_dol_ebit_horizon_2y_z_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_118_dol_ebit_horizon_2y_z_5y},
    "f41_rolv_119_dol_ebitda_horizon_1q_z_5y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_119_dol_ebitda_horizon_1q_z_5y},
    "f41_rolv_120_dol_gp_horizon_1y_z_5y": {"inputs": ["revenue", "gp"], "func": f41_rolv_120_dol_gp_horizon_1y_z_5y},
    "f41_rolv_121_dol_netinc_horizon_1y_z_5y": {"inputs": ["revenue", "netinc"], "func": f41_rolv_121_dol_netinc_horizon_1y_z_5y},
    "f41_rolv_122_dol_ebit_above_threshold_rate_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_122_dol_ebit_above_threshold_rate_2y},
    "f41_rolv_123_dol_ebit_below_threshold_rate_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_123_dol_ebit_below_threshold_rate_2y},
    "f41_rolv_124_dol_sign_flip_count_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_124_dol_sign_flip_count_5y},
    "f41_rolv_125_dol_ebit_extreme_quantile_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_125_dol_ebit_extreme_quantile_5y},
    "f41_rolv_126_cost_flex_composite_z": {"inputs": ["revenue", "sga", "rnd", "capex"], "func": f41_rolv_126_cost_flex_composite_z},
    "f41_rolv_127_sales_cost_convergence_speed_2y": {"inputs": ["revenue", "opex"], "func": f41_rolv_127_sales_cost_convergence_speed_2y},
    "f41_rolv_128_sales_cost_convergence_speed_5y": {"inputs": ["revenue", "opex"], "func": f41_rolv_128_sales_cost_convergence_speed_5y},
    "f41_rolv_129_sga_share_slope_2y": {"inputs": ["revenue", "sga"], "func": f41_rolv_129_sga_share_slope_2y},
    "f41_rolv_130_rnd_share_slope_2y": {"inputs": ["revenue", "rnd"], "func": f41_rolv_130_rnd_share_slope_2y},
    "f41_rolv_131_cogs_share_slope_2y": {"inputs": ["revenue", "cor"], "func": f41_rolv_131_cogs_share_slope_2y},
    "f41_rolv_132_da_share_slope_2y": {"inputs": ["revenue", "depamor"], "func": f41_rolv_132_da_share_slope_2y},
    "f41_rolv_133_capex_share_slope_2y": {"inputs": ["revenue", "capex"], "func": f41_rolv_133_capex_share_slope_2y},
    "f41_rolv_134_opex_share_above_one_indicator": {"inputs": ["revenue", "opex"], "func": f41_rolv_134_opex_share_above_one_indicator},
    "f41_rolv_135_cost_share_dispersion_across_buckets": {"inputs": ["revenue", "sga", "cor", "rnd", "depamor"], "func": f41_rolv_135_cost_share_dispersion_across_buckets},
    "f41_rolv_136_ebit_margin_quarterly_compression_rate": {"inputs": ["revenue", "ebit"], "func": f41_rolv_136_ebit_margin_quarterly_compression_rate},
    "f41_rolv_137_ebit_margin_annual_compression_rate": {"inputs": ["revenue", "ebit"], "func": f41_rolv_137_ebit_margin_annual_compression_rate},
    "f41_rolv_138_quarters_to_negative_ebit_linear": {"inputs": ["revenue", "ebit"], "func": f41_rolv_138_quarters_to_negative_ebit_linear},
    "f41_rolv_139_years_to_negative_ebit_linear": {"inputs": ["revenue", "ebit"], "func": f41_rolv_139_years_to_negative_ebit_linear},
    "f41_rolv_140_dupont_op_lev_ebit_x_assetturn": {"inputs": ["revenue", "ebit", "assets"], "func": f41_rolv_140_dupont_op_lev_ebit_x_assetturn},
    "f41_rolv_141_dupont_op_lev_cv_2y": {"inputs": ["revenue", "ebit", "assets"], "func": f41_rolv_141_dupont_op_lev_cv_2y},
    "f41_rolv_142_financial_leverage_assets_to_equity": {"inputs": ["assets", "equity"], "func": f41_rolv_142_financial_leverage_assets_to_equity},
    "f41_rolv_143_total_leverage_dtl_proxy_1y": {"inputs": ["revenue", "ebit", "assets", "equity"], "func": f41_rolv_143_total_leverage_dtl_proxy_1y},
    "f41_rolv_144_debt_to_invcap_share": {"inputs": ["debt", "invcap"], "func": f41_rolv_144_debt_to_invcap_share},
    "f41_rolv_145_interest_burden_to_ebit_proxy": {"inputs": ["ebit", "ebt"], "func": f41_rolv_145_interest_burden_to_ebit_proxy},
    "f41_rolv_146_contribution_margin_vol_to_dol_ratio": {"inputs": ["revenue", "ebit", "gp"], "func": f41_rolv_146_contribution_margin_vol_to_dol_ratio},
    "f41_rolv_147_ncfo_to_ebit_quality_gap": {"inputs": ["ebit", "ncfo"], "func": f41_rolv_147_ncfo_to_ebit_quality_gap},
    "f41_rolv_148_fcf_to_rev_cushion": {"inputs": ["revenue", "fcf"], "func": f41_rolv_148_fcf_to_rev_cushion},
    "f41_rolv_149_op_lev_x_dilution_pressure": {"inputs": ["revenue", "ebit", "sharesbas"], "func": f41_rolv_149_op_lev_x_dilution_pressure},
    "f41_rolv_150_reverse_op_lev_terminal_score": {"inputs": ["revenue", "ebit", "sga", "rnd", "depamor"], "func": f41_rolv_150_reverse_op_lev_terminal_score},
}
