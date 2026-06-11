"""reverse_operating_leverage base features 001-075 — Pipeline 1a-inverse short-side blowup family.

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
#                    BASE FEATURES 001-075
# ============================================================

def f41_rolv_001_dol_ebit_to_rev_ratio_1y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """DOL_EBIT = %dEBIT / %dRev over 1Y — annual op-lev sensitivity."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_002_dol_ebit_to_rev_ratio_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """DOL_EBIT %d-ratio over 2Y — multi-year operating leverage."""
    rn = ebit.diff(2 * YDAYS) / ebit.shift(2 * YDAYS).replace(0, np.nan)
    rd = revenue.diff(2 * YDAYS) / revenue.shift(2 * YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_003_dol_ebit_loglog_slope_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Rolling log-log slope d ln EBIT / d ln Rev — DOL_EBIT regression."""
    ln = _safe_log(ebit)
    ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_004_dol_ebit_loglog_slope_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """5Y log-log DOL_EBIT — secular operating leverage regime."""
    ln = _safe_log(ebit)
    ld = _safe_log(revenue)
    cov = ln.rolling(1260, min_periods=max(1260//3, 2)).cov(ld)
    var = ld.rolling(1260, min_periods=max(1260//3, 2)).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_005_dol_ebitda_to_rev_ratio_1y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """DOL_EBITDA %d-ratio 1Y — pre-D&A op-lev sensitivity."""
    rn = ebitda.diff(YDAYS) / ebitda.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_006_dol_ebitda_loglog_slope_2y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Log-log DOL_EBITDA 2Y — regression form."""
    ln = _safe_log(ebitda)
    ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_007_dol_gp_to_rev_ratio_1y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Gross-profit DOL — contribution-margin sensitivity to revenue."""
    rn = gp.diff(YDAYS) / gp.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_008_dol_gp_loglog_slope_2y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Log-log slope d ln GP / d ln Rev — contribution leverage."""
    ln = _safe_log(gp)
    ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_009_dol_netinc_to_rev_ratio_1y(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Net-income DOL 1Y — bottom-line sensitivity including financing."""
    rn = netinc.diff(YDAYS) / netinc.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_010_dol_netinc_loglog_slope_2y(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Log-log DOL_NetInc 2Y — total-leverage regression."""
    ln = _safe_log(netinc)
    ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=max(2 * YDAYS//3, 2)).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_011_dol_ebt_to_rev_ratio_1y(revenue: pd.Series, ebt: pd.Series) -> pd.Series:
    """Pretax DOL 1Y — pretax sensitivity."""
    rn = ebt.diff(YDAYS) / ebt.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_012_dol_ncfo_to_rev_ratio_1y(revenue: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Operating cash flow DOL — cash earnings sensitivity."""
    rn = ncfo.diff(YDAYS) / ncfo.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_013_decremental_dol_ebit_1y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Decremental EBIT/Rev change ratio when dRev<0 over 1Y (downside DOL)."""
    drev = revenue.diff(YDAYS)
    debit = ebit.diff(YDAYS)
    mask = drev < 0
    expr = _safe_div(debit.where(mask), drev.where(mask))
    return expr

def f41_rolv_014_decremental_dol_ebitda_1y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Decremental EBITDA on Rev decline 1Y."""
    drev = revenue.diff(YDAYS)
    debitda = ebitda.diff(YDAYS)
    mask = drev < 0
    expr = _safe_div(debitda.where(mask), drev.where(mask))
    return expr

def f41_rolv_015_decremental_dol_gp_1y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Decremental GP/Rev change ratio on Rev declines — contribution-margin under stress."""
    drev = revenue.diff(YDAYS)
    dgp = gp.diff(YDAYS)
    mask = drev < 0
    expr = _safe_div(dgp.where(mask), drev.where(mask))
    return expr

def f41_rolv_016_upside_dol_ebit_1y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Upside DOL: dEBIT/dRev when dRev>0 — operating-lev asymmetry numerator."""
    drev = revenue.diff(YDAYS)
    debit = ebit.diff(YDAYS)
    mask = drev > 0
    expr = _safe_div(debit.where(mask), drev.where(mask))
    return expr

def f41_rolv_017_dol_ebit_asymmetry_up_minus_down(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Upside minus downside DOL_EBIT (1Y) — asymmetric operating leverage."""
    drev = revenue.diff(YDAYS)
    debit = ebit.diff(YDAYS)
    up = _safe_div(debit.where(drev > 0), drev.where(drev > 0))
    dn = _safe_div(debit.where(drev < 0), drev.where(drev < 0))
    expr = up.rolling(YDAYS, min_periods=QDAYS).mean() - dn.rolling(YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_018_dol_ebit_loglog_slope_z_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Z-score of log-log DOL_EBIT 2Y vs own 5Y history."""
    ln = _safe_log(ebit); ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=QDAYS).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=QDAYS).var()
    dol = cov / var.replace(0, np.nan)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_019_dol_ebitda_loglog_slope_z_2y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of log-log DOL_EBITDA 2Y vs own 5Y."""
    ln = _safe_log(ebitda); ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=QDAYS).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=QDAYS).var()
    dol = cov / var.replace(0, np.nan)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_020_high_dol_regime_indicator_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Indicator: DOL_EBIT > 3 sustained over 1Y window (high-leverage regime flag)."""
    ln = _safe_log(ebit); ld = _safe_log(revenue)
    cov = ln.rolling(2 * YDAYS, min_periods=QDAYS).cov(ld)
    var = ld.rolling(2 * YDAYS, min_periods=QDAYS).var()
    dol = cov / var.replace(0, np.nan)
    flag = (dol > 3.0).astype(float)
    expr = flag.rolling(YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_021_dol_ebit_dispersion_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Rolling std of 1Y DOL_EBIT over a 2Y window — leverage instability."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = dol.rolling(2 * YDAYS, min_periods=QDAYS).std()
    return expr

def f41_rolv_022_dol_netinc_dispersion_2y(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling std of 1Y DOL_NetInc over 2Y — total-leverage instability."""
    rn = netinc.diff(YDAYS) / netinc.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = dol.rolling(2 * YDAYS, min_periods=QDAYS).std()
    return expr

def f41_rolv_023_dol_ebit_one_quarter_shock_ratio(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Quarterly DOL_EBIT: %dQ EBIT / %dQ Rev — shortest-horizon leverage shock."""
    rn = ebit.diff(QDAYS) / ebit.shift(QDAYS).replace(0, np.nan)
    rd = revenue.diff(QDAYS) / revenue.shift(QDAYS).replace(0, np.nan)
    expr = _safe_div(rn, rd)
    return expr

def f41_rolv_024_dol_ebit_quarterly_z_vs_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Z-score of quarterly DOL_EBIT vs 5Y history."""
    rn = ebit.diff(QDAYS) / ebit.shift(QDAYS).replace(0, np.nan)
    rd = revenue.diff(QDAYS) / revenue.shift(QDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    expr = _rolling_zscore(dol, 1260)
    return expr

def f41_rolv_025_sga_rev_ratio_cv_2y(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """CV of SGA/Revenue over 2Y — SGA stickiness as fixed-cost proxy."""
    r = _safe_div(sga, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_026_sga_growth_minus_rev_growth_1y(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """SGA growth minus revenue growth 1Y — sticky SGA when revenue rolls."""
    gs = sga.diff(YDAYS) / sga.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gs - gr
    return expr

def f41_rolv_027_sga_stickiness_on_decline_1y(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """When dRev<0, SGA growth divided by (-dRev growth) — sticky SGA indicator."""
    gs = sga.diff(YDAYS) / sga.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gs.where(mask), -gr.where(mask))
    return expr

def f41_rolv_028_rnd_rev_ratio_cv_2y(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """CV of RnD/Revenue 2Y — RnD-spend stickiness."""
    r = _safe_div(rnd, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_029_rnd_growth_minus_rev_growth_1y(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """RnD growth minus revenue growth 1Y — RnD inflexibility."""
    gn = rnd.diff(YDAYS) / rnd.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gn - gr
    return expr

def f41_rolv_030_rnd_stickiness_on_decline_1y(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """RnD growth / (-revenue growth) when revenue declines."""
    gn = rnd.diff(YDAYS) / rnd.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gn.where(mask), -gr.where(mask))
    return expr

def f41_rolv_031_opex_rev_ratio_cv_2y(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """CV of OPEX/Revenue 2Y — overall opex stickiness."""
    r = _safe_div(opex, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_032_opex_growth_minus_rev_growth_1y(revenue: pd.Series, opex: pd.Series) -> pd.Series:
    """OPEX growth minus revenue growth — broad cost inflexibility."""
    go = opex.diff(YDAYS) / opex.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = go - gr
    return expr

def f41_rolv_033_sga_to_opex_share(sga: pd.Series, opex: pd.Series) -> pd.Series:
    """Share of SGA in total OPEX — fixed-cost-component share."""
    expr = _safe_div(sga, opex)
    return expr

def f41_rolv_034_rnd_to_opex_share(rnd: pd.Series, opex: pd.Series) -> pd.Series:
    """RnD share of OPEX — long-term commitment share."""
    expr = _safe_div(rnd, opex)
    return expr

def f41_rolv_035_cogs_rev_ratio_cv_2y(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """CV of COGS/Revenue 2Y — variable-cost stickiness vs slot 022 (different denom)."""
    r = _safe_div(cor, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_036_cogs_growth_minus_rev_growth_1y(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """COGS growth - Revenue growth 1Y — supply-side stickiness signal."""
    gc = cor.diff(YDAYS) / cor.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gc - gr
    return expr

def f41_rolv_037_cogs_stickiness_on_decline_1y(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """COGS growth / (-revenue growth) on declines — inability to cut COGS."""
    gc = cor.diff(YDAYS) / cor.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    mask = gr < 0
    expr = _safe_div(gc.where(mask), -gr.where(mask))
    return expr

def f41_rolv_038_gp_share_of_rev_level(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """GP/Revenue level — contribution margin proxy (high=variable cost share lower)."""
    expr = _safe_div(gp, revenue)
    return expr

def f41_rolv_039_gp_share_of_rev_cv_2y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Stability of GP/Revenue over 2Y — contribution-margin volatility."""
    r = _safe_div(gp, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_040_gp_growth_minus_rev_growth_1y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """GP growth - revenue growth — contribution-margin decay."""
    gg = gp.diff(YDAYS) / gp.shift(YDAYS).replace(0, np.nan)
    gr = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    expr = gg - gr
    return expr

def f41_rolv_041_cogs_share_of_rev_level(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """COGS/Revenue level — variable-cost share proxy."""
    expr = _safe_div(cor, revenue)
    return expr

def f41_rolv_042_contribution_margin_growth_asymmetry(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Up-period vs down-period mean delta(GP/Rev) — asymmetric contribution."""
    r = _safe_div(gp, revenue)
    drev = revenue.diff(YDAYS)
    dr = r.diff(YDAYS)
    up = dr.where(drev > 0).rolling(2 * YDAYS, min_periods=QDAYS).mean()
    dn = dr.where(drev < 0).rolling(2 * YDAYS, min_periods=QDAYS).mean()
    expr = up - dn
    return expr

def f41_rolv_043_cogs_rev_correlation_2y(revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Rolling 2Y Pearson corr between dCOGS and dRevenue — variable-cost coupling."""
    dc = cor.diff(QDAYS)
    dr = revenue.diff(QDAYS)
    expr = dc.rolling(2 * YDAYS, min_periods=QDAYS).corr(dr)
    return expr

def f41_rolv_044_sga_rev_correlation_2y(revenue: pd.Series, sga: pd.Series) -> pd.Series:
    """Rolling 2Y Pearson corr dSGA vs dRevenue — fixed-cost coupling (low=fixed)."""
    ds = sga.diff(QDAYS)
    dr = revenue.diff(QDAYS)
    expr = ds.rolling(2 * YDAYS, min_periods=QDAYS).corr(dr)
    return expr

def f41_rolv_045_sga_share_of_sga_plus_cogs(sga: pd.Series, cor: pd.Series) -> pd.Series:
    """SGA/(SGA+COGS) — fixed-cost share proxy."""
    expr = _safe_div(sga, sga + cor)
    return expr

def f41_rolv_046_rnd_share_of_rev_level(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """RnD/Revenue level — long-cycle fixed-cost share."""
    expr = _safe_div(rnd, revenue)
    return expr

def f41_rolv_047_da_to_rev_level(revenue: pd.Series, depamor: pd.Series) -> pd.Series:
    """D&A/Revenue level — capital-intensity fixed-cost share."""
    expr = _safe_div(depamor, revenue)
    return expr

def f41_rolv_048_da_to_ebit_level(ebit: pd.Series, depamor: pd.Series) -> pd.Series:
    """D&A/EBIT — fixed-cost magnitude relative to operating income."""
    expr = _safe_div(depamor, ebit)
    return expr

def f41_rolv_049_da_to_opex_level(opex: pd.Series, depamor: pd.Series) -> pd.Series:
    """D&A/OPEX — D&A burden inside opex."""
    expr = _safe_div(depamor, opex)
    return expr

def f41_rolv_050_fixed_cost_proxy_share(revenue: pd.Series, sga: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    """(SGA+RnD+D&A)/Revenue — composite fixed-cost intensity."""
    fc = sga.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    expr = _safe_div(fc, revenue)
    return expr

def f41_rolv_051_fixed_cost_proxy_share_cv_2y(revenue: pd.Series, sga: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    """Stability (CV) of fixed-cost share over 2Y — structural rigidity."""
    fc = sga.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    r = _safe_div(fc, revenue)
    m = r.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / m.replace(0, np.nan)
    return expr

def f41_rolv_052_sga_to_gp_share(sga: pd.Series, gp: pd.Series) -> pd.Series:
    """SGA/GP — fixed share of contribution profit."""
    expr = _safe_div(sga, gp)
    return expr

def f41_rolv_053_rnd_to_gp_share(rnd: pd.Series, gp: pd.Series) -> pd.Series:
    """RnD/GP — research commitment vs contribution."""
    expr = _safe_div(rnd, gp)
    return expr

def f41_rolv_054_sga_plus_rnd_to_gp_share(sga: pd.Series, rnd: pd.Series, gp: pd.Series) -> pd.Series:
    """(SGA+RnD)/GP — discretionary-fixed share of contribution."""
    expr = _safe_div(sga.fillna(0) + rnd.fillna(0), gp)
    return expr

def f41_rolv_055_opmargin_elasticity_to_logrev_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Rolling 2Y regression slope of (EBIT/Rev) on log(Rev) — margin elasticity."""
    m = _safe_div(ebit, revenue)
    lr = _safe_log(revenue)
    cov = m.rolling(2 * YDAYS, min_periods=QDAYS).cov(lr)
    var = lr.rolling(2 * YDAYS, min_periods=QDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_056_opmargin_elasticity_to_logrev_5y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """5Y regression slope (EBIT/Rev) on log(Rev) — long-cycle elasticity."""
    m = _safe_div(ebit, revenue)
    lr = _safe_log(revenue)
    cov = m.rolling(1260, min_periods=YDAYS).cov(lr)
    var = lr.rolling(1260, min_periods=YDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_057_ebitda_margin_elasticity_to_logrev_2y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """EBITDA/Rev vs log(Rev) slope 2Y — pre-D&A elasticity."""
    m = _safe_div(ebitda, revenue)
    lr = _safe_log(revenue)
    cov = m.rolling(2 * YDAYS, min_periods=QDAYS).cov(lr)
    var = lr.rolling(2 * YDAYS, min_periods=QDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_058_gp_margin_elasticity_to_logrev_2y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """GP margin vs log(Rev) slope 2Y — contribution elasticity."""
    m = _safe_div(gp, revenue)
    lr = _safe_log(revenue)
    cov = m.rolling(2 * YDAYS, min_periods=QDAYS).cov(lr)
    var = lr.rolling(2 * YDAYS, min_periods=QDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_059_netmargin_elasticity_to_logrev_2y(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Net margin vs log(Rev) slope 2Y — total elasticity."""
    m = _safe_div(netinc, revenue)
    lr = _safe_log(revenue)
    cov = m.rolling(2 * YDAYS, min_periods=QDAYS).cov(lr)
    var = lr.rolling(2 * YDAYS, min_periods=QDAYS).var()
    expr = cov / var.replace(0, np.nan)
    return expr

def f41_rolv_060_opmargin_vs_rev_rank_corr_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Rolling Spearman (rank) corr of EBIT margin and revenue over 2Y — direction-agnostic elasticity."""
    m = _safe_div(ebit, revenue)
    expr = m.rolling(2 * YDAYS, min_periods=QDAYS).corr(revenue.rank(pct=True))
    return expr

def f41_rolv_061_opmargin_drawdown_in_rev_decline_1y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Mean drop of EBIT margin during 1Y revenue declines — decremental margin proxy."""
    m = _safe_div(ebit, revenue)
    drev = revenue.diff(YDAYS)
    dm = m.diff(YDAYS)
    expr = dm.where(drev < 0).rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_062_ebitda_margin_drawdown_in_rev_decline_1y(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Mean drop of EBITDA margin during rev declines 1Y."""
    m = _safe_div(ebitda, revenue)
    drev = revenue.diff(YDAYS)
    dm = m.diff(YDAYS)
    expr = dm.where(drev < 0).rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_063_gp_margin_drawdown_in_rev_decline_1y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Mean drop of GP margin during rev declines 1Y."""
    m = _safe_div(gp, revenue)
    drev = revenue.diff(YDAYS)
    dm = m.diff(YDAYS)
    expr = dm.where(drev < 0).rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_064_netmargin_drawdown_in_rev_decline_1y(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Mean drop of net margin during rev declines 1Y."""
    m = _safe_div(netinc, revenue)
    drev = revenue.diff(YDAYS)
    dm = m.diff(YDAYS)
    expr = dm.where(drev < 0).rolling(2 * YDAYS, min_periods=QDAYS).mean()
    return expr

def f41_rolv_065_decremental_margin_ebit_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Sum(dEBIT)/Sum(dRev) over the 2Y subset where dRev<0 — pooled decremental margin."""
    drev = revenue.diff(QDAYS)
    debit = ebit.diff(QDAYS)
    mask = drev < 0
    num = debit.where(mask).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    den = drev.where(mask).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    expr = _safe_div(num, den)
    return expr

def f41_rolv_066_decremental_margin_gp_2y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Pooled 2Y dGP/dRev when dRev<0 — pooled contribution decremental."""
    drev = revenue.diff(QDAYS)
    dgp = gp.diff(QDAYS)
    mask = drev < 0
    num = dgp.where(mask).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    den = drev.where(mask).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    expr = _safe_div(num, den)
    return expr

def f41_rolv_067_decremental_minus_incremental_margin(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Pooled decremental dEBIT/dRev minus pooled incremental — asymmetric leverage."""
    drev = revenue.diff(QDAYS)
    debit = ebit.diff(QDAYS)
    md = drev < 0; mu = drev > 0
    num_d = debit.where(md).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    den_d = drev.where(md).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    num_u = debit.where(mu).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    den_u = drev.where(mu).rolling(2 * YDAYS, min_periods=QDAYS).sum()
    expr = _safe_div(num_d, den_d) - _safe_div(num_u, den_u)
    return expr

def f41_rolv_068_breakeven_distance_pct(revenue: pd.Series, sga: pd.Series, rnd: pd.Series, depamor: pd.Series) -> pd.Series:
    """(Revenue - SGA - RnD - D&A)/Revenue — distance from fixed-cost breakeven."""
    fc = sga.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    expr = _safe_div(revenue - fc, revenue)
    return expr

def f41_rolv_069_breakeven_distance_via_ebit_margin(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """EBIT/Revenue — 1-period distance to negative EBIT (operating-breakeven distance)."""
    expr = _safe_div(ebit, revenue)
    return expr

def f41_rolv_070_breakeven_distance_via_ebitda_margin(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """EBITDA/Revenue — EBITDA breakeven distance."""
    expr = _safe_div(ebitda, revenue)
    return expr

def f41_rolv_071_breakeven_quarters_via_dol(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Quarters until EBIT hits zero at current decremental margin: -EBIT_margin / dEBIT_margin_per_quarter."""
    m = _safe_div(ebit, revenue)
    dm = m.diff(QDAYS)
    expr = -m / dm.replace(0, np.nan)
    return expr

def f41_rolv_072_breakeven_distance_to_gp_zero(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """GP/Revenue — distance until cogs > revenue (gross-margin breakeven)."""
    expr = _safe_div(gp, revenue)
    return expr

def f41_rolv_073_breakeven_distance_cv_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """CV of breakeven distance over 2Y — stability of margin headroom."""
    m = _safe_div(ebit, revenue)
    mn = m.rolling(2 * YDAYS, min_periods=QDAYS).mean()
    sd = m.rolling(2 * YDAYS, min_periods=QDAYS).std()
    expr = sd / mn.replace(0, np.nan)
    return expr

def f41_rolv_074_breakeven_distance_min_2y(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Minimum of EBIT/Rev over 2Y — worst-case headroom in recent regime."""
    m = _safe_div(ebit, revenue)
    expr = m.rolling(2 * YDAYS, min_periods=QDAYS).min()
    return expr

def f41_rolv_075_operating_leverage_composite_score(revenue: pd.Series, ebit: pd.Series, sga: pd.Series, rnd: pd.Series, depamor: pd.Series, gp: pd.Series) -> pd.Series:
    """Composite z-blend: DOL_EBIT 2Y, fixed-cost share, GP margin instability — overall rigidity score."""
    rn = ebit.diff(YDAYS) / ebit.shift(YDAYS).replace(0, np.nan)
    rd = revenue.diff(YDAYS) / revenue.shift(YDAYS).replace(0, np.nan)
    dol = _safe_div(rn, rd)
    fc = sga.fillna(0) + rnd.fillna(0) + depamor.fillna(0)
    fc_share = _safe_div(fc, revenue)
    gpm = _safe_div(gp, revenue)
    gpm_cv = gpm.rolling(2 * YDAYS, min_periods=QDAYS).std() / gpm.rolling(2 * YDAYS, min_periods=QDAYS).mean().replace(0, np.nan)
    z1 = _rolling_zscore(dol, 1260)
    z2 = _rolling_zscore(fc_share, 1260)
    z3 = _rolling_zscore(gpm_cv, 1260)
    expr = (z1.fillna(0) + z2.fillna(0) + z3.fillna(0)) / 3.0
    return expr


# ============================================================
#                        REGISTRY
# ============================================================

REVERSE_OPERATING_LEVERAGE_BASE_REGISTRY_001_075 = {
    "f41_rolv_001_dol_ebit_to_rev_ratio_1y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_001_dol_ebit_to_rev_ratio_1y},
    "f41_rolv_002_dol_ebit_to_rev_ratio_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_002_dol_ebit_to_rev_ratio_2y},
    "f41_rolv_003_dol_ebit_loglog_slope_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_003_dol_ebit_loglog_slope_2y},
    "f41_rolv_004_dol_ebit_loglog_slope_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_004_dol_ebit_loglog_slope_5y},
    "f41_rolv_005_dol_ebitda_to_rev_ratio_1y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_005_dol_ebitda_to_rev_ratio_1y},
    "f41_rolv_006_dol_ebitda_loglog_slope_2y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_006_dol_ebitda_loglog_slope_2y},
    "f41_rolv_007_dol_gp_to_rev_ratio_1y": {"inputs": ["revenue", "gp"], "func": f41_rolv_007_dol_gp_to_rev_ratio_1y},
    "f41_rolv_008_dol_gp_loglog_slope_2y": {"inputs": ["revenue", "gp"], "func": f41_rolv_008_dol_gp_loglog_slope_2y},
    "f41_rolv_009_dol_netinc_to_rev_ratio_1y": {"inputs": ["revenue", "netinc"], "func": f41_rolv_009_dol_netinc_to_rev_ratio_1y},
    "f41_rolv_010_dol_netinc_loglog_slope_2y": {"inputs": ["revenue", "netinc"], "func": f41_rolv_010_dol_netinc_loglog_slope_2y},
    "f41_rolv_011_dol_ebt_to_rev_ratio_1y": {"inputs": ["revenue", "ebt"], "func": f41_rolv_011_dol_ebt_to_rev_ratio_1y},
    "f41_rolv_012_dol_ncfo_to_rev_ratio_1y": {"inputs": ["revenue", "ncfo"], "func": f41_rolv_012_dol_ncfo_to_rev_ratio_1y},
    "f41_rolv_013_decremental_dol_ebit_1y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_013_decremental_dol_ebit_1y},
    "f41_rolv_014_decremental_dol_ebitda_1y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_014_decremental_dol_ebitda_1y},
    "f41_rolv_015_decremental_dol_gp_1y": {"inputs": ["revenue", "gp"], "func": f41_rolv_015_decremental_dol_gp_1y},
    "f41_rolv_016_upside_dol_ebit_1y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_016_upside_dol_ebit_1y},
    "f41_rolv_017_dol_ebit_asymmetry_up_minus_down": {"inputs": ["revenue", "ebit"], "func": f41_rolv_017_dol_ebit_asymmetry_up_minus_down},
    "f41_rolv_018_dol_ebit_loglog_slope_z_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_018_dol_ebit_loglog_slope_z_2y},
    "f41_rolv_019_dol_ebitda_loglog_slope_z_2y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_019_dol_ebitda_loglog_slope_z_2y},
    "f41_rolv_020_high_dol_regime_indicator_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_020_high_dol_regime_indicator_2y},
    "f41_rolv_021_dol_ebit_dispersion_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_021_dol_ebit_dispersion_2y},
    "f41_rolv_022_dol_netinc_dispersion_2y": {"inputs": ["revenue", "netinc"], "func": f41_rolv_022_dol_netinc_dispersion_2y},
    "f41_rolv_023_dol_ebit_one_quarter_shock_ratio": {"inputs": ["revenue", "ebit"], "func": f41_rolv_023_dol_ebit_one_quarter_shock_ratio},
    "f41_rolv_024_dol_ebit_quarterly_z_vs_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_024_dol_ebit_quarterly_z_vs_5y},
    "f41_rolv_025_sga_rev_ratio_cv_2y": {"inputs": ["revenue", "sga"], "func": f41_rolv_025_sga_rev_ratio_cv_2y},
    "f41_rolv_026_sga_growth_minus_rev_growth_1y": {"inputs": ["revenue", "sga"], "func": f41_rolv_026_sga_growth_minus_rev_growth_1y},
    "f41_rolv_027_sga_stickiness_on_decline_1y": {"inputs": ["revenue", "sga"], "func": f41_rolv_027_sga_stickiness_on_decline_1y},
    "f41_rolv_028_rnd_rev_ratio_cv_2y": {"inputs": ["revenue", "rnd"], "func": f41_rolv_028_rnd_rev_ratio_cv_2y},
    "f41_rolv_029_rnd_growth_minus_rev_growth_1y": {"inputs": ["revenue", "rnd"], "func": f41_rolv_029_rnd_growth_minus_rev_growth_1y},
    "f41_rolv_030_rnd_stickiness_on_decline_1y": {"inputs": ["revenue", "rnd"], "func": f41_rolv_030_rnd_stickiness_on_decline_1y},
    "f41_rolv_031_opex_rev_ratio_cv_2y": {"inputs": ["revenue", "opex"], "func": f41_rolv_031_opex_rev_ratio_cv_2y},
    "f41_rolv_032_opex_growth_minus_rev_growth_1y": {"inputs": ["revenue", "opex"], "func": f41_rolv_032_opex_growth_minus_rev_growth_1y},
    "f41_rolv_033_sga_to_opex_share": {"inputs": ["sga", "opex"], "func": f41_rolv_033_sga_to_opex_share},
    "f41_rolv_034_rnd_to_opex_share": {"inputs": ["rnd", "opex"], "func": f41_rolv_034_rnd_to_opex_share},
    "f41_rolv_035_cogs_rev_ratio_cv_2y": {"inputs": ["revenue", "cor"], "func": f41_rolv_035_cogs_rev_ratio_cv_2y},
    "f41_rolv_036_cogs_growth_minus_rev_growth_1y": {"inputs": ["revenue", "cor"], "func": f41_rolv_036_cogs_growth_minus_rev_growth_1y},
    "f41_rolv_037_cogs_stickiness_on_decline_1y": {"inputs": ["revenue", "cor"], "func": f41_rolv_037_cogs_stickiness_on_decline_1y},
    "f41_rolv_038_gp_share_of_rev_level": {"inputs": ["revenue", "gp"], "func": f41_rolv_038_gp_share_of_rev_level},
    "f41_rolv_039_gp_share_of_rev_cv_2y": {"inputs": ["revenue", "gp"], "func": f41_rolv_039_gp_share_of_rev_cv_2y},
    "f41_rolv_040_gp_growth_minus_rev_growth_1y": {"inputs": ["revenue", "gp"], "func": f41_rolv_040_gp_growth_minus_rev_growth_1y},
    "f41_rolv_041_cogs_share_of_rev_level": {"inputs": ["revenue", "cor"], "func": f41_rolv_041_cogs_share_of_rev_level},
    "f41_rolv_042_contribution_margin_growth_asymmetry": {"inputs": ["revenue", "gp"], "func": f41_rolv_042_contribution_margin_growth_asymmetry},
    "f41_rolv_043_cogs_rev_correlation_2y": {"inputs": ["revenue", "cor"], "func": f41_rolv_043_cogs_rev_correlation_2y},
    "f41_rolv_044_sga_rev_correlation_2y": {"inputs": ["revenue", "sga"], "func": f41_rolv_044_sga_rev_correlation_2y},
    "f41_rolv_045_sga_share_of_sga_plus_cogs": {"inputs": ["sga", "cor"], "func": f41_rolv_045_sga_share_of_sga_plus_cogs},
    "f41_rolv_046_rnd_share_of_rev_level": {"inputs": ["revenue", "rnd"], "func": f41_rolv_046_rnd_share_of_rev_level},
    "f41_rolv_047_da_to_rev_level": {"inputs": ["revenue", "depamor"], "func": f41_rolv_047_da_to_rev_level},
    "f41_rolv_048_da_to_ebit_level": {"inputs": ["ebit", "depamor"], "func": f41_rolv_048_da_to_ebit_level},
    "f41_rolv_049_da_to_opex_level": {"inputs": ["opex", "depamor"], "func": f41_rolv_049_da_to_opex_level},
    "f41_rolv_050_fixed_cost_proxy_share": {"inputs": ["revenue", "sga", "rnd", "depamor"], "func": f41_rolv_050_fixed_cost_proxy_share},
    "f41_rolv_051_fixed_cost_proxy_share_cv_2y": {"inputs": ["revenue", "sga", "rnd", "depamor"], "func": f41_rolv_051_fixed_cost_proxy_share_cv_2y},
    "f41_rolv_052_sga_to_gp_share": {"inputs": ["sga", "gp"], "func": f41_rolv_052_sga_to_gp_share},
    "f41_rolv_053_rnd_to_gp_share": {"inputs": ["rnd", "gp"], "func": f41_rolv_053_rnd_to_gp_share},
    "f41_rolv_054_sga_plus_rnd_to_gp_share": {"inputs": ["sga", "rnd", "gp"], "func": f41_rolv_054_sga_plus_rnd_to_gp_share},
    "f41_rolv_055_opmargin_elasticity_to_logrev_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_055_opmargin_elasticity_to_logrev_2y},
    "f41_rolv_056_opmargin_elasticity_to_logrev_5y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_056_opmargin_elasticity_to_logrev_5y},
    "f41_rolv_057_ebitda_margin_elasticity_to_logrev_2y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_057_ebitda_margin_elasticity_to_logrev_2y},
    "f41_rolv_058_gp_margin_elasticity_to_logrev_2y": {"inputs": ["revenue", "gp"], "func": f41_rolv_058_gp_margin_elasticity_to_logrev_2y},
    "f41_rolv_059_netmargin_elasticity_to_logrev_2y": {"inputs": ["revenue", "netinc"], "func": f41_rolv_059_netmargin_elasticity_to_logrev_2y},
    "f41_rolv_060_opmargin_vs_rev_rank_corr_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_060_opmargin_vs_rev_rank_corr_2y},
    "f41_rolv_061_opmargin_drawdown_in_rev_decline_1y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_061_opmargin_drawdown_in_rev_decline_1y},
    "f41_rolv_062_ebitda_margin_drawdown_in_rev_decline_1y": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_062_ebitda_margin_drawdown_in_rev_decline_1y},
    "f41_rolv_063_gp_margin_drawdown_in_rev_decline_1y": {"inputs": ["revenue", "gp"], "func": f41_rolv_063_gp_margin_drawdown_in_rev_decline_1y},
    "f41_rolv_064_netmargin_drawdown_in_rev_decline_1y": {"inputs": ["revenue", "netinc"], "func": f41_rolv_064_netmargin_drawdown_in_rev_decline_1y},
    "f41_rolv_065_decremental_margin_ebit_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_065_decremental_margin_ebit_2y},
    "f41_rolv_066_decremental_margin_gp_2y": {"inputs": ["revenue", "gp"], "func": f41_rolv_066_decremental_margin_gp_2y},
    "f41_rolv_067_decremental_minus_incremental_margin": {"inputs": ["revenue", "ebit"], "func": f41_rolv_067_decremental_minus_incremental_margin},
    "f41_rolv_068_breakeven_distance_pct": {"inputs": ["revenue", "sga", "rnd", "depamor"], "func": f41_rolv_068_breakeven_distance_pct},
    "f41_rolv_069_breakeven_distance_via_ebit_margin": {"inputs": ["revenue", "ebit"], "func": f41_rolv_069_breakeven_distance_via_ebit_margin},
    "f41_rolv_070_breakeven_distance_via_ebitda_margin": {"inputs": ["revenue", "ebitda"], "func": f41_rolv_070_breakeven_distance_via_ebitda_margin},
    "f41_rolv_071_breakeven_quarters_via_dol": {"inputs": ["revenue", "ebit"], "func": f41_rolv_071_breakeven_quarters_via_dol},
    "f41_rolv_072_breakeven_distance_to_gp_zero": {"inputs": ["revenue", "gp"], "func": f41_rolv_072_breakeven_distance_to_gp_zero},
    "f41_rolv_073_breakeven_distance_cv_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_073_breakeven_distance_cv_2y},
    "f41_rolv_074_breakeven_distance_min_2y": {"inputs": ["revenue", "ebit"], "func": f41_rolv_074_breakeven_distance_min_2y},
    "f41_rolv_075_operating_leverage_composite_score": {"inputs": ["revenue", "ebit", "sga", "rnd", "depamor", "gp"], "func": f41_rolv_075_operating_leverage_composite_score},
}
