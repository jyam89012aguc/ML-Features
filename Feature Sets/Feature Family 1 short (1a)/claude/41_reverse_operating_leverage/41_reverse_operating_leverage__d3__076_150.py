"""reverse_operating_leverage D3 features 076-150 — third-derivative wrappers.

Each function inlines the corresponding base body and appends the appropriate
.diff() chain. Inputs and PIT discipline match __base__076_150.py.
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
#                    D3 FEATURES 076-150
# ============================================================

def f41_rolv_076_da_to_ebit_cv_2y_d3(ebit: pd.Series, depamor: pd.Series) -> pd.Series:
    r = _safe_div(depamor, ebit)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_077_da_growth_minus_rev_growth_1y_d3(revenue: pd.Series, depamor: pd.Series) -> pd.Series:
    gd = depamor.diff(YDAYS) / depamor.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gd - gr
    return (expr).diff().diff().diff()

def f41_rolv_078_capex_intensity_level_d3(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    expr = _safe_div(capex.abs(), revenue)
    return (expr).diff().diff().diff()

def f41_rolv_079_capex_intensity_cv_2y_d3(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    r = _safe_div(capex.abs(), revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_080_capex_growth_minus_rev_growth_1y_d3(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    gc = capex.abs().diff(YDAYS) / capex.abs().shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gc - gr
    return (expr).diff().diff().diff()

def f41_rolv_081_capex_stickiness_on_decline_1y_d3(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    gc = capex.abs().diff(YDAYS) / capex.abs().shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gc.where(mask), -gr.where(mask))
    return (expr).diff().diff().diff()

def f41_rolv_082_capex_to_da_ratio_d3(capex: pd.Series, depamor: pd.Series) -> pd.Series:
    expr = _safe_div(capex.abs(), depamor)
    return (expr).diff().diff().diff()

def f41_rolv_083_capex_to_ncfo_ratio_d3(capex: pd.Series, ncfo: pd.Series) -> pd.Series:
    expr = _safe_div(capex.abs(), ncfo)
    return (expr).diff().diff().diff()

def f41_rolv_084_capex_intensity_z_5y_d3(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    r = _safe_div(capex.abs(), revenue)
    expr = _rolling_zscore(r, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_085_future_da_commitment_proxy_d3(capex: pd.Series, ppnenet: pd.Series) -> pd.Series:
    ttm = capex.abs().rolling(YDAYS, min_periods=QDAYS).sum()
    expr = _safe_div(ttm, ppnenet)
    return (expr).diff().diff().diff()

def f41_rolv_086_ppne_to_rev_intensity_d3(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    expr = _safe_div(ppnenet, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_087_ppne_to_assets_share_d3(assets: pd.Series, ppnenet: pd.Series) -> pd.Series:
    expr = _safe_div(ppnenet, assets)
    return (expr).diff().diff().diff()

def f41_rolv_088_asset_turnover_level_d3(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    expr = _safe_div(revenue, assets)
    return (expr).diff().diff().diff()

def f41_rolv_089_asset_turnover_cv_2y_d3(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    r = _safe_div(revenue, assets)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_090_ppne_turnover_level_d3(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    expr = _safe_div(revenue, ppnenet)
    return (expr).diff().diff().diff()

def f41_rolv_091_ppne_turnover_cv_2y_d3(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    r = _safe_div(revenue, ppnenet)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_092_ppne_growth_minus_rev_growth_1y_d3(revenue: pd.Series, ppnenet: pd.Series) -> pd.Series:
    gp_ = ppnenet.diff(YDAYS) / ppnenet.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gp_ - gr
    return (expr).diff().diff().diff()

def f41_rolv_093_intangibles_to_assets_share_d3(assets: pd.Series, intangibles: pd.Series) -> pd.Series:
    expr = _safe_div(intangibles, assets)
    return (expr).diff().diff().diff()

def f41_rolv_094_intangibles_growth_minus_rev_growth_1y_d3(revenue: pd.Series, intangibles: pd.Series) -> pd.Series:
    gi = intangibles.diff(YDAYS) / intangibles.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gi - gr
    return (expr).diff().diff().diff()

def f41_rolv_095_invcap_to_rev_intensity_d3(revenue: pd.Series, invcap: pd.Series) -> pd.Series:
    expr = _safe_div(invcap, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_096_wc_to_rev_intensity_d3(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    expr = _safe_div(workingcapital, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_097_wc_to_rev_cv_2y_d3(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    r = _safe_div(workingcapital, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_098_wc_growth_minus_rev_growth_1y_d3(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    gw = workingcapital.diff(YDAYS) / workingcapital.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gw - gr
    return (expr).diff().diff().diff()

def f41_rolv_099_inventory_to_rev_level_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    expr = _safe_div(inventory, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_100_inventory_growth_minus_rev_growth_1y_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    gi = inventory.diff(YDAYS) / inventory.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gi - gr
    return (expr).diff().diff().diff()

def f41_rolv_101_inventory_buildup_on_decline_1y_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    gi = inventory.diff(YDAYS) / inventory.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gi.where(mask), -gr.where(mask))
    return (expr).diff().diff().diff()

def f41_rolv_102_receivables_growth_minus_rev_growth_1y_d3(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    gr_ = receivables.diff(YDAYS) / receivables.shift(YDAYS).replace(0, np.nan)
    gv = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gr_ - gv
    return (expr).diff().diff().diff()

def f41_rolv_103_payables_growth_minus_cogs_growth_1y_d3(cor: pd.Series, payables: pd.Series) -> pd.Series:
    gp_ = payables.diff(YDAYS) / payables.shift(YDAYS).replace(0, np.nan)
    gc = cor.diff(YDAYS) / cor.shift(YDAYS).replace(0, np.nan)
    expr = gp_ - gc
    return (expr).diff().diff().diff()

def f41_rolv_104_receivables_to_rev_level_d3(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    expr = _safe_div(receivables, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_105_inventory_rev_elasticity_2y_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    ln = _safe_log(inventory); lr = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=QDAYS).cov(lr)
    var = lr.rolling(2 * YDAYS, min_periods=QDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_106_sbc_to_rev_level_d3(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    expr = _safe_div(sbcomp, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_107_sbc_to_rev_cv_2y_d3(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    r = _safe_div(sbcomp, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_108_sbc_growth_minus_rev_growth_1y_d3(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    gs = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gs - gr
    return (expr).diff().diff().diff()

def f41_rolv_109_sbc_stickiness_on_decline_1y_d3(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    gs = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gs.where(mask), -gr.where(mask))
    return (expr).diff().diff().diff()

def f41_rolv_110_sbc_to_opex_share_d3(opex: pd.Series, sbcomp: pd.Series) -> pd.Series:
    expr = _safe_div(sbcomp, opex)
    return (expr).diff().diff().diff()

def f41_rolv_111_sbc_to_ncfo_addback_share_d3(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    expr = _safe_div(sbcomp, ncfo.abs())
    return (expr).diff().diff().diff()

def f41_rolv_112_sbc_to_netinc_addback_share_d3(sbcomp: pd.Series, netinc: pd.Series) -> pd.Series:
    expr = _safe_div(sbcomp, netinc.abs())
    return (expr).diff().diff().diff()

def f41_rolv_113_sbc_rev_correlation_2y_d3(revenue: pd.Series, sbcomp: pd.Series) -> pd.Series:
    ds = sbcomp.diff(QDAYS)
    dr = revenue.diff(QDAYS)
    expr = ds.rolling(2 * YDAYS, min_periods=QDAYS).corr(dr)
    return (expr).diff().diff().diff()

def f41_rolv_114_sbc_growth_5y_avg_d3(sbcomp: pd.Series) -> pd.Series:
    g = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    expr = g.rolling(1260, min_periods=YDAYS).mean()
    return (expr).diff().diff().diff()

def f41_rolv_115_sbc_to_shareswadil_growth_couple_d3(sbcomp: pd.Series, shareswadil: pd.Series) -> pd.Series:
    gs = sbcomp.diff(YDAYS) / sbcomp.shift(YDAYS).replace(0, np.nan)
    gd = shareswadil.diff(YDAYS) / shareswadil.shift(YDAYS).replace(0, np.nan)
    expr = gs.rolling(2 * YDAYS, min_periods=QDAYS).corr(gd)
    return (expr).diff().diff().diff()

def f41_rolv_116_dol_ebit_horizon_1q_z_5y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(QDAYS) / ebit.shift(QDAYS).replace(0, np.nan)
    rd = revenue.diff(QDAYS) / revenue.shift(QDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_117_dol_ebit_horizon_1y_z_5y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_118_dol_ebit_horizon_2y_z_5y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(2 * YDAYS) / ebit.shift(2 * YDAYS).replace(0, np.nan)
    rd = revenue.diff(2 * YDAYS) / revenue.shift(2 * YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_119_dol_ebitda_horizon_1q_z_5y_d3(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    rn = ebitda.diff(QDAYS) / ebitda.shift(QDAYS).replace(0, np.nan)
    rd = revenue.diff(QDAYS) / revenue.shift(QDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_120_dol_gp_horizon_1y_z_5y_d3(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    rn = gp.diff(YDAYS) / gp.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_121_dol_netinc_horizon_1y_z_5y_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    rn = netinc.diff(YDAYS) / netinc.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_122_dol_ebit_above_threshold_rate_2y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flag = (dol > 5.0).astype(float)
    expr = flag.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return (expr).diff().diff().diff()

def f41_rolv_123_dol_ebit_below_threshold_rate_2y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flag = (dol < -2.0).astype(float)
    expr = flag.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return (expr).diff().diff().diff()

def f41_rolv_124_dol_sign_flip_count_5y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flips = (np.sign(dol) != np.sign(dol.shift(QDAYS))).astype(float)
    expr = flips.rolling(1260, min_periods=YDAYS).sum()
    return (expr).diff().diff().diff()

def f41_rolv_125_dol_ebit_extreme_quantile_5y_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd).abs()
    expr = dol.rolling(1260, min_periods=YDAYS).quantile(0.95)
    return (expr).diff().diff().diff()

def f41_rolv_126_cost_flex_composite_z_d3(revenue: pd.Series, sga: pd.Series, rnd: pd.Series, capex: pd.Series) -> pd.Series:
    def stick(x):
        gx = x.diff(YDAYS) / x.shift(YDAYS).replace(0, np.nan)
        gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
        return _safe_div(gx.where(gr < 0), -gr.where(gr < 0))
    z1 = _rolling_zscore(stick(sga), 1260)
    z2 = _rolling_zscore(stick(rnd), 1260)
    z3 = _rolling_zscore(stick(capex.abs()), 1260)
    expr = (z1.fillna(0) + z2.fillna(0) + z3.fillna(0)) / 3.0
    return (expr).diff().diff().diff()

def f41_rolv_127_sales_cost_convergence_speed_2y_d3(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    r = _safe_div(opex, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_128_sales_cost_convergence_speed_5y_d3(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    r = _safe_div(opex, revenue)
    expr = _rolling_slope(r, 1260)
    return (expr).diff().diff().diff()

def f41_rolv_129_sga_share_slope_2y_d3(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    r = _safe_div(sga, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_130_rnd_share_slope_2y_d3(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    r = _safe_div(rnd, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_131_cogs_share_slope_2y_d3(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    r = _safe_div(cor, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_132_da_share_slope_2y_d3(revenue: pd.Series, depamor: pd.Series) -> pd.Series:
    r = _safe_div(depamor, revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_133_capex_share_slope_2y_d3(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    r = _safe_div(capex.abs(), revenue)
    expr = _rolling_slope(r, 2 * YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_134_opex_share_above_one_indicator_d3(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    r = _safe_div(opex, revenue)
    expr = (r > 1.0).astype(float)
    return (expr).diff().diff().diff()

def f41_rolv_135_cost_share_dispersion_across_buckets_d3(revenue: pd.Series, sga: pd.Series, cor: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    r1 = _safe_div(sga, revenue)
    r2 = _safe_div(cor, revenue)
    r3 = _safe_div(rnd, revenue)
    r4 = _safe_div(depamor, revenue)
    df = pd.concat([r1, r2, r3, r4], axis=1)
    expr = df.std(axis=1)
    return (expr).diff().diff().diff()

def f41_rolv_136_ebit_margin_quarterly_compression_rate_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    m = _safe_div(ebit, revenue)
    expr = -m.diff(QDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_137_ebit_margin_annual_compression_rate_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    m = _safe_div(ebit, revenue)
    expr = -m.diff(YDAYS)
    return (expr).diff().diff().diff()

def f41_rolv_138_quarters_to_negative_ebit_linear_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    m = _safe_div(ebit, revenue)
    comp = -m.diff(QDAYS).replace(0, np.nan)
    expr = _safe_div(m, comp)
    return (expr).diff().diff().diff()

def f41_rolv_139_years_to_negative_ebit_linear_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    m = _safe_div(ebit, revenue)
    comp = -m.diff(YDAYS).replace(0, np.nan)
    expr = _safe_div(m, comp)
    return (expr).diff().diff().diff()

def f41_rolv_140_dupont_op_lev_ebit_x_assetturn_d3(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    m = _safe_div(ebit, revenue)
    at = _safe_div(revenue, assets)
    expr = m * at
    return (expr).diff().diff().diff()

def f41_rolv_141_dupont_op_lev_cv_2y_d3(revenue: pd.Series, ebit: pd.Series, assets: pd.Series) -> pd.Series:
    m = _safe_div(ebit, revenue)
    at = _safe_div(revenue, assets)
    x = m * at
    mn = x.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = x.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / mn.replace(0, np.nan)
    return (expr).diff().diff().diff()

def f41_rolv_142_financial_leverage_assets_to_equity_d3(assets: pd.Series, equity: pd.Series) -> pd.Series:
    expr = _safe_div(assets, equity)
    return (expr).diff().diff().diff()

def f41_rolv_143_total_leverage_dtl_proxy_1y_d3(revenue: pd.Series, ebit: pd.Series, assets: pd.Series, equity: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    flev = _safe_div(assets, equity)
    expr = dol * flev
    return (expr).diff().diff().diff()

def f41_rolv_144_debt_to_invcap_share_d3(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    expr = _safe_div(debt, invcap)
    return (expr).diff().diff().diff()

def f41_rolv_145_interest_burden_to_ebit_proxy_d3(ebit: pd.Series, ebt: pd.Series) -> pd.Series:
    expr = 1.0 - _safe_div(ebt, ebit)
    return (expr).diff().diff().diff()

def f41_rolv_146_contribution_margin_vol_to_dol_ratio_d3(revenue: pd.Series, ebit: pd.Series, gp: pd.Series) -> pd.Series:
    gpm = _safe_div(gp, revenue)
    sd = gpm.rolling(2 * YDAYS, min_periods=QDAYS).std()
    rn = ebit.diff(2 * YDAYS) / ebit.shift(2 * YDAYS).replace(0, np.nan)
    rd = revenue.diff(2 * YDAYS) / revenue.shift(2 * YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd).abs()
    expr = _safe_div(sd, dol)
    return (expr).diff().diff().diff()

def f41_rolv_147_ncfo_to_ebit_quality_gap_d3(ebit: pd.Series, ncfo: pd.Series) -> pd.Series:
    expr = _safe_div(ncfo, ebit)
    return (expr).diff().diff().diff()

def f41_rolv_148_fcf_to_rev_cushion_d3(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    expr = _safe_div(fcf, revenue)
    return (expr).diff().diff().diff()

def f41_rolv_149_op_lev_x_dilution_pressure_d3(revenue: pd.Series, ebit: pd.Series, sharesbas: pd.Series) -> pd.Series:
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    g = sharesbas.diff(YDAYS) / sharesbas.shift(YDAYS).replace(0, np.nan)
    expr = dol * g
    return (expr).diff().diff().diff()

def f41_rolv_150_reverse_op_lev_terminal_score_d3(revenue: pd.Series, ebit: pd.Series, sga: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
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
    return (expr).diff().diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

REVERSE_OPERATING_LEVERAGE_D3_REGISTRY_076_150 = {
    "f41_rolv_076_da_to_ebit_cv_2y_d3": {"inputs": ["ebit", "depamor"], "func": f41_rolv_076_da_to_ebit_cv_2y_d3},
    "f41_rolv_077_da_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "depamor"], "func": f41_rolv_077_da_growth_minus_rev_growth_1y_d3},
    "f41_rolv_078_capex_intensity_level_d3": {"inputs": ["revenue", "capex"], "func": f41_rolv_078_capex_intensity_level_d3},
    "f41_rolv_079_capex_intensity_cv_2y_d3": {"inputs": ["revenue", "capex"], "func": f41_rolv_079_capex_intensity_cv_2y_d3},
    "f41_rolv_080_capex_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "capex"], "func": f41_rolv_080_capex_growth_minus_rev_growth_1y_d3},
    "f41_rolv_081_capex_stickiness_on_decline_1y_d3": {"inputs": ["revenue", "capex"], "func": f41_rolv_081_capex_stickiness_on_decline_1y_d3},
    "f41_rolv_082_capex_to_da_ratio_d3": {"inputs": ["capex", "depamor"], "func": f41_rolv_082_capex_to_da_ratio_d3},
    "f41_rolv_083_capex_to_ncfo_ratio_d3": {"inputs": ["capex", "ncfo"], "func": f41_rolv_083_capex_to_ncfo_ratio_d3},
    "f41_rolv_084_capex_intensity_z_5y_d3": {"inputs": ["revenue", "capex"], "func": f41_rolv_084_capex_intensity_z_5y_d3},
    "f41_rolv_085_future_da_commitment_proxy_d3": {"inputs": ["capex", "ppnenet"], "func": f41_rolv_085_future_da_commitment_proxy_d3},
    "f41_rolv_086_ppne_to_rev_intensity_d3": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_086_ppne_to_rev_intensity_d3},
    "f41_rolv_087_ppne_to_assets_share_d3": {"inputs": ["assets", "ppnenet"], "func": f41_rolv_087_ppne_to_assets_share_d3},
    "f41_rolv_088_asset_turnover_level_d3": {"inputs": ["revenue", "assets"], "func": f41_rolv_088_asset_turnover_level_d3},
    "f41_rolv_089_asset_turnover_cv_2y_d3": {"inputs": ["revenue", "assets"], "func": f41_rolv_089_asset_turnover_cv_2y_d3},
    "f41_rolv_090_ppne_turnover_level_d3": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_090_ppne_turnover_level_d3},
    "f41_rolv_091_ppne_turnover_cv_2y_d3": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_091_ppne_turnover_cv_2y_d3},
    "f41_rolv_092_ppne_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "ppnenet"], "func": f41_rolv_092_ppne_growth_minus_rev_growth_1y_d3},
    "f41_rolv_093_intangibles_to_assets_share_d3": {"inputs": ["assets", "intangibles"], "func": f41_rolv_093_intangibles_to_assets_share_d3},
    "f41_rolv_094_intangibles_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "intangibles"], "func": f41_rolv_094_intangibles_growth_minus_rev_growth_1y_d3},
    "f41_rolv_095_invcap_to_rev_intensity_d3": {"inputs": ["revenue", "invcap"], "func": f41_rolv_095_invcap_to_rev_intensity_d3},
    "f41_rolv_096_wc_to_rev_intensity_d3": {"inputs": ["revenue", "workingcapital"], "func": f41_rolv_096_wc_to_rev_intensity_d3},
    "f41_rolv_097_wc_to_rev_cv_2y_d3": {"inputs": ["revenue", "workingcapital"], "func": f41_rolv_097_wc_to_rev_cv_2y_d3},
    "f41_rolv_098_wc_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "workingcapital"], "func": f41_rolv_098_wc_growth_minus_rev_growth_1y_d3},
    "f41_rolv_099_inventory_to_rev_level_d3": {"inputs": ["revenue", "inventory"], "func": f41_rolv_099_inventory_to_rev_level_d3},
    "f41_rolv_100_inventory_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "inventory"], "func": f41_rolv_100_inventory_growth_minus_rev_growth_1y_d3},
    "f41_rolv_101_inventory_buildup_on_decline_1y_d3": {"inputs": ["revenue", "inventory"], "func": f41_rolv_101_inventory_buildup_on_decline_1y_d3},
    "f41_rolv_102_receivables_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "receivables"], "func": f41_rolv_102_receivables_growth_minus_rev_growth_1y_d3},
    "f41_rolv_103_payables_growth_minus_cogs_growth_1y_d3": {"inputs": ["cor", "payables"], "func": f41_rolv_103_payables_growth_minus_cogs_growth_1y_d3},
    "f41_rolv_104_receivables_to_rev_level_d3": {"inputs": ["revenue", "receivables"], "func": f41_rolv_104_receivables_to_rev_level_d3},
    "f41_rolv_105_inventory_rev_elasticity_2y_d3": {"inputs": ["revenue", "inventory"], "func": f41_rolv_105_inventory_rev_elasticity_2y_d3},
    "f41_rolv_106_sbc_to_rev_level_d3": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_106_sbc_to_rev_level_d3},
    "f41_rolv_107_sbc_to_rev_cv_2y_d3": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_107_sbc_to_rev_cv_2y_d3},
    "f41_rolv_108_sbc_growth_minus_rev_growth_1y_d3": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_108_sbc_growth_minus_rev_growth_1y_d3},
    "f41_rolv_109_sbc_stickiness_on_decline_1y_d3": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_109_sbc_stickiness_on_decline_1y_d3},
    "f41_rolv_110_sbc_to_opex_share_d3": {"inputs": ["opex", "sbcomp"], "func": f41_rolv_110_sbc_to_opex_share_d3},
    "f41_rolv_111_sbc_to_ncfo_addback_share_d3": {"inputs": ["sbcomp", "ncfo"], "func": f41_rolv_111_sbc_to_ncfo_addback_share_d3},
    "f41_rolv_112_sbc_to_netinc_addback_share_d3": {"inputs": ["sbcomp", "netinc"], "func": f41_rolv_112_sbc_to_netinc_addback_share_d3},
    "f41_rolv_113_sbc_rev_correlation_2y_d3": {"inputs": ["revenue", "sbcomp"], "func": f41_rolv_113_sbc_rev_correlation_2y_d3},
    "f41_rolv_114_sbc_growth_5y_avg_d3": {"inputs": ["sbcomp"], "func": f41_rolv_114_sbc_growth_5y_avg_d3},
    "f41_rolv_115_sbc_to_shareswadil_growth_couple_d3": {"inputs": ["sbcomp", "shareswadil"], "func": f41_rolv_115_sbc_to_shareswadil_growth_couple_d3},
    "f41_rolv_116_dol_ebit_horizon_1q_z_5y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_116_dol_ebit_horizon_1q_z_5y_d3},
    "f41_rolv_117_dol_ebit_horizon_1y_z_5y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_117_dol_ebit_horizon_1y_z_5y_d3},
    "f41_rolv_118_dol_ebit_horizon_2y_z_5y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_118_dol_ebit_horizon_2y_z_5y_d3},
    "f41_rolv_119_dol_ebitda_horizon_1q_z_5y_d3": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_119_dol_ebitda_horizon_1q_z_5y_d3},
    "f41_rolv_120_dol_gp_horizon_1y_z_5y_d3": {"inputs": ["revenue", "gp"], "func": f41_rolv_120_dol_gp_horizon_1y_z_5y_d3},
    "f41_rolv_121_dol_netinc_horizon_1y_z_5y_d3": {"inputs": ["revenue", "netinc"], "func": f41_rolv_121_dol_netinc_horizon_1y_z_5y_d3},
    "f41_rolv_122_dol_ebit_above_threshold_rate_2y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_122_dol_ebit_above_threshold_rate_2y_d3},
    "f41_rolv_123_dol_ebit_below_threshold_rate_2y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_123_dol_ebit_below_threshold_rate_2y_d3},
    "f41_rolv_124_dol_sign_flip_count_5y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_124_dol_sign_flip_count_5y_d3},
    "f41_rolv_125_dol_ebit_extreme_quantile_5y_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_125_dol_ebit_extreme_quantile_5y_d3},
    "f41_rolv_126_cost_flex_composite_z_d3": {"inputs": ["revenue", "sga", "rnd", "capex"], "func": f41_rolv_126_cost_flex_composite_z_d3},
    "f41_rolv_127_sales_cost_convergence_speed_2y_d3": {"inputs": ["revenue", "opex"], "func": f41_rolv_127_sales_cost_convergence_speed_2y_d3},
    "f41_rolv_128_sales_cost_convergence_speed_5y_d3": {"inputs": ["revenue", "opex"], "func": f41_rolv_128_sales_cost_convergence_speed_5y_d3},
    "f41_rolv_129_sga_share_slope_2y_d3": {"inputs": ["revenue", "sga"], "func": f41_rolv_129_sga_share_slope_2y_d3},
    "f41_rolv_130_rnd_share_slope_2y_d3": {"inputs": ["revenue", "rnd"], "func": f41_rolv_130_rnd_share_slope_2y_d3},
    "f41_rolv_131_cogs_share_slope_2y_d3": {"inputs": ["revenue", "cor"], "func": f41_rolv_131_cogs_share_slope_2y_d3},
    "f41_rolv_132_da_share_slope_2y_d3": {"inputs": ["revenue", "depamor"], "func": f41_rolv_132_da_share_slope_2y_d3},
    "f41_rolv_133_capex_share_slope_2y_d3": {"inputs": ["revenue", "capex"], "func": f41_rolv_133_capex_share_slope_2y_d3},
    "f41_rolv_134_opex_share_above_one_indicator_d3": {"inputs": ["revenue", "opex"], "func": f41_rolv_134_opex_share_above_one_indicator_d3},
    "f41_rolv_135_cost_share_dispersion_across_buckets_d3": {"inputs": ["revenue", "sga", "cor", "rnd", "depamor"], "func": f41_rolv_135_cost_share_dispersion_across_buckets_d3},
    "f41_rolv_136_ebit_margin_quarterly_compression_rate_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_136_ebit_margin_quarterly_compression_rate_d3},
    "f41_rolv_137_ebit_margin_annual_compression_rate_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_137_ebit_margin_annual_compression_rate_d3},
    "f41_rolv_138_quarters_to_negative_ebit_linear_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_138_quarters_to_negative_ebit_linear_d3},
    "f41_rolv_139_years_to_negative_ebit_linear_d3": {"inputs": ["revenue", "ebit"], "func": f41_rolv_139_years_to_negative_ebit_linear_d3},
    "f41_rolv_140_dupont_op_lev_ebit_x_assetturn_d3": {"inputs": ["revenue", "ebit", "assets"], "func": f41_rolv_140_dupont_op_lev_ebit_x_assetturn_d3},
    "f41_rolv_141_dupont_op_lev_cv_2y_d3": {"inputs": ["revenue", "ebit", "assets"], "func": f41_rolv_141_dupont_op_lev_cv_2y_d3},
    "f41_rolv_142_financial_leverage_assets_to_equity_d3": {"inputs": ["assets", "equity"], "func": f41_rolv_142_financial_leverage_assets_to_equity_d3},
    "f41_rolv_143_total_leverage_dtl_proxy_1y_d3": {"inputs": ["revenue", "ebit", "assets", "equity"], "func": f41_rolv_143_total_leverage_dtl_proxy_1y_d3},
    "f41_rolv_144_debt_to_invcap_share_d3": {"inputs": ["debt", "invcap"], "func": f41_rolv_144_debt_to_invcap_share_d3},
    "f41_rolv_145_interest_burden_to_ebit_proxy_d3": {"inputs": ["ebit", "ebt"], "func": f41_rolv_145_interest_burden_to_ebit_proxy_d3},
    "f41_rolv_146_contribution_margin_vol_to_dol_ratio_d3": {"inputs": ["revenue", "ebit", "gp"], "func": f41_rolv_146_contribution_margin_vol_to_dol_ratio_d3},
    "f41_rolv_147_ncfo_to_ebit_quality_gap_d3": {"inputs": ["ebit", "ncfo"], "func": f41_rolv_147_ncfo_to_ebit_quality_gap_d3},
    "f41_rolv_148_fcf_to_rev_cushion_d3": {"inputs": ["revenue", "fcf"], "func": f41_rolv_148_fcf_to_rev_cushion_d3},
    "f41_rolv_149_op_lev_x_dilution_pressure_d3": {"inputs": ["revenue", "ebit", "sharesbas"], "func": f41_rolv_149_op_lev_x_dilution_pressure_d3},
    "f41_rolv_150_reverse_op_lev_terminal_score_d3": {"inputs": ["revenue", "ebit", "sga", "rnd", "depamor"], "func": f41_rolv_150_reverse_op_lev_terminal_score_d3},
}
