import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives — OPERATING-LEVERAGE MECHANICS ONLY =====
def _f26ol_dgrow(s, w):
    return s - s.shift(w)


def _f26ol_pctg(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f26ol_loggrow(s, w):
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f26ol_dol(profit, revenue, w):
    gp = profit / profit.shift(w).replace(0, np.nan) - 1.0
    gr = revenue / revenue.shift(w).replace(0, np.nan) - 1.0
    return gp / gr.replace(0, np.nan)


def _f26ol_incmargin(profit, revenue, w):
    dp = profit - profit.shift(w)
    dr = revenue - revenue.shift(w)
    return dp / dr.replace(0, np.nan)


def _f26ol_growthspread(profit, revenue, w):
    return _f26ol_loggrow(profit, w) - _f26ol_loggrow(revenue, w)


# ============================================================
# === LONG-HORIZON DOL FACETS ===
# DOL over a two-year super-cycle, smoothed (structural leverage level)
def f26ol_f26_operating_leverage_cycle_dol_504d_base_v076_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 504).clip(-15, 15)
    result = _mean(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL distributional skew over the cycle: asymmetry of the leverage multiplier (252d)
def f26ol_f26_operating_leverage_cycle_dolskew_252d_base_v077_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    result = d.rolling(252, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT DOL over a half-year, z-scored vs its own history (de-trended below-line leverage)
def f26ol_f26_operating_leverage_cycle_doleb_126d_base_v078_signal(ebit, revenue):
    d = _f26ol_dol(ebit, revenue, 126).clip(-15, 15)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit DOL over a quarter, tanh-bounded (short variable-cost leverage)
def f26ol_f26_operating_leverage_cycle_dolgp_63d_base_v079_signal(gp, revenue):
    d = _f26ol_dol(gp, revenue, 63)
    result = np.tanh(0.5 * d)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL long-vs-short term structure: 504d DOL minus 126d DOL (structural minus cyclical)
def f26ol_f26_operating_leverage_cycle_dolterml_base_v080_signal(opinc, revenue):
    dl = _f26ol_dol(opinc, revenue, 504).clip(-15, 15)
    ds = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    result = dl - ds
    return result.replace([np.inf, -np.inf], np.nan)


# DOL acceleration: 126d DOL change now minus a quarter ago (leverage 2nd-order shift)
def f26ol_f26_operating_leverage_cycle_dolaccel_base_v081_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    dd = d - d.shift(63)
    result = dd - dd.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL excess over 1: how far the leverage multiplier exceeds neutral, root-compressed
def f26ol_f26_operating_leverage_cycle_dolexc_252d_base_v082_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 252).clip(-15, 15) - 1.0
    result = np.sign(d) * (d.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL ratio EBIT-to-opinc: how much extra gearing is below the operating line
def f26ol_f26_operating_leverage_cycle_dolratio_252d_base_v083_signal(ebit, opinc, revenue):
    deb = _f26ol_dol(ebit, revenue, 252).clip(-15, 15)
    dop = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    result = (deb / dop.replace(0, np.nan)).clip(-15, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute DOL vol-of-vol: instability of the leverage multiplier over the cycle
def f26ol_f26_operating_leverage_cycle_dolvov_504d_base_v084_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    inst = _std(d, 126)
    result = _std(inst, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL sign-flip frequency: how often the leverage multiplier changes direction
def f26ol_f26_operating_leverage_cycle_dolflip_252d_base_v085_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63)
    flip = (np.sign(d) != np.sign(d.shift(21))).astype(float)
    result = flip.rolling(252, min_periods=63).mean() - 0.25
    return result.replace([np.inf, -np.inf], np.nan)


# === LONG-HORIZON INCREMENTAL-MARGIN FACETS ===
# incremental operating margin over a two-year cycle (structural leverage capture)
def f26ol_f26_operating_leverage_cycle_incop_504d_base_v086_signal(opinc, revenue):
    result = _f26ol_incmargin(opinc, revenue, 504).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin over a half-year, z-scored (contribution capture state)
def f26ol_f26_operating_leverage_cycle_incgp_126d_base_v087_signal(gp, revenue):
    inc = _f26ol_incmargin(gp, revenue, 126).clip(-3, 3)
    result = _z(inc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental EBIT margin over a half-year, smoothed
def f26ol_f26_operating_leverage_cycle_inceb_126d_base_v088_signal(ebit, revenue):
    inc = _f26ol_incmargin(ebit, revenue, 126).clip(-5, 5)
    result = _mean(inc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin dispersion across 63/126/252 horizons (capture disagreement)
def f26ol_f26_operating_leverage_cycle_incdisp_base_v089_signal(opinc, revenue):
    i1 = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    i2 = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    i3 = _f26ol_incmargin(opinc, revenue, 252).clip(-5, 5)
    result = pd.concat([i1, i2, i3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin term structure: short minus long inc-margin (capture maturing)
def f26ol_f26_operating_leverage_cycle_incterm_base_v090_signal(opinc, revenue):
    isr = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    ilr = _f26ol_incmargin(opinc, revenue, 252).clip(-5, 5)
    result = isr - ilr
    return result.replace([np.inf, -np.inf], np.nan)


# incremental-margin tanh oscillator: inc-margin minus its 252d trend, bounded
def f26ol_f26_operating_leverage_cycle_incosc_base_v091_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    osc = inc - inc.rolling(252, min_periods=63).mean()
    result = np.tanh(2.0 * osc)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental contribution-margin acceleration over a year (variable-cost capture shift)
def f26ol_f26_operating_leverage_cycle_inccmaccel_base_v092_signal(gp, revenue):
    inc = _f26ol_incmargin(gp, revenue, 126).clip(-3, 3)
    result = inc - inc.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin positive-streak length (sustained leverage capture run)
def f26ol_f26_operating_leverage_cycle_incstreak_base_v093_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 63)
    pos = (inc > 0).astype(float)
    streak = pos.groupby((pos != pos.shift()).cumsum()).cumcount() + 1
    result = (streak * pos).rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage beta on revenue-growth conditioned high vs low growth (convex gearing)
# regress opinc-growth on revenue-growth separately in fast vs slow revenue regimes
def f26ol_f26_operating_leverage_cycle_incshare_base_v094_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 21)
    grev = _f26ol_loggrow(revenue, 21)
    hi = grev > grev.rolling(252, min_periods=63).median()
    beta_hi = gop.where(hi).rolling(252, min_periods=42).cov(grev.where(hi)) / \
        grev.where(hi).rolling(252, min_periods=42).var().replace(0, np.nan)
    beta_lo = gop.where(~hi).rolling(252, min_periods=42).cov(grev.where(~hi)) / \
        grev.where(~hi).rolling(252, min_periods=42).var().replace(0, np.nan)
    result = (beta_hi - beta_lo).clip(-25, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin de-meaned vs 504d mid (cyclical excess leverage capture)
def f26ol_f26_operating_leverage_cycle_incexc_504d_base_v095_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    result = inc - inc.rolling(504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# === LONG-HORIZON GROWTH-SPREAD FACETS ===
# operating-leverage spread over a two-year cycle (structural amplification)
def f26ol_f26_operating_leverage_cycle_gap_504d_base_v096_signal(opinc, revenue):
    result = _f26ol_growthspread(opinc, revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage spread over a 504d super-cycle, ranked vs 1260d history (long state)
def f26ol_f26_operating_leverage_cycle_gap_1260d_base_v097_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 504)
    result = g.rolling(1260, min_periods=378).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread trend: how the leverage spread is slope-changing over a half-year
def f26ol_f26_operating_leverage_cycle_gaptrend_base_v098_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread smoothed via slow EMA (persistent leverage amplification)
def f26ol_f26_operating_leverage_cycle_gapema_base_v099_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    result = g.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT growth-spread over a half-year (below-line amplification)
def f26ol_f26_operating_leverage_cycle_gapeb_126d_base_v100_signal(ebit, revenue):
    result = _f26ol_growthspread(ebit, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth-spread over a half-year (variable-cost amplification)
def f26ol_f26_operating_leverage_cycle_gapgp_126d_base_v101_signal(gp, revenue):
    result = _f26ol_growthspread(gp, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread upside semi-deviation (only above-mean amplification excursions)
def f26ol_f26_operating_leverage_cycle_gapupdev_base_v102_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 63)
    mu = g.rolling(252, min_periods=63).mean()
    up = (g - mu).clip(lower=0)
    result = (up ** 2).rolling(252, min_periods=63).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread downside semi-deviation (de-leveraging shock magnitude)
def f26ol_f26_operating_leverage_cycle_gapdndev_base_v103_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 63)
    mu = g.rolling(252, min_periods=63).mean()
    dn = (mu - g).clip(lower=0)
    result = (dn ** 2).rolling(252, min_periods=63).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread year-over-year change (cyclical amplification shift)
def f26ol_f26_operating_leverage_cycle_gapyoy_base_v104_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 252)
    result = g - g.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# tri-line growth-spread dispersion: disagreement among gp/opinc/ebit spreads
def f26ol_f26_operating_leverage_cycle_stackdisp_base_v105_signal(gp, opinc, ebit, revenue):
    g_gp = _f26ol_growthspread(gp, revenue, 252)
    g_op = _f26ol_growthspread(opinc, revenue, 252)
    g_eb = _f26ol_growthspread(ebit, revenue, 252)
    result = pd.concat([g_gp, g_op, g_eb], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# === SWING-AMPLITUDE / ASYMMETRY (long & alternate) FACETS ===
# leverage swing ratio over a two-year cycle (structural opinc-vs-rev volatility ratio)
def f26ol_f26_operating_leverage_cycle_swing_504d_base_v106_signal(opinc, revenue):
    op_sw = _std(_f26ol_loggrow(opinc, 63), 504)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 504)
    result = (op_sw / rev_sw.replace(0, np.nan)).clip(0, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# swing-ratio percentile rank vs 504d cycle (where the amplification sits)
def f26ol_f26_operating_leverage_cycle_swingrank_base_v107_signal(opinc, revenue):
    op_sw = _std(_f26ol_loggrow(opinc, 63), 252)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 252)
    sr = (op_sw / rev_sw.replace(0, np.nan)).clip(0, 25)
    result = _rank(sr, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute-spread amplitude: mean |growth-spread| over the cycle (raw swing size)
def f26ol_f26_operating_leverage_cycle_gapamp_252d_base_v108_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 63)
    result = g.abs().rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage response asymmetry of DOL: DOL on rev-up minus DOL on rev-down
def f26ol_f26_operating_leverage_cycle_dolasym_base_v109_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 63)
    up = d.where(grev > 0).rolling(252, min_periods=42).mean()
    dn = d.where(grev < 0).rolling(252, min_periods=42).mean()
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# upside vs downside incremental-margin asymmetry (capture better on the way up?)
def f26ol_f26_operating_leverage_cycle_incasym_base_v110_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 63)
    up = inc.where(grev > 0).rolling(252, min_periods=42).mean()
    dn = inc.where(grev < 0).rolling(252, min_periods=42).mean()
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# beta of ebit-growth on revenue-growth (below-line operating-leverage beta)
def f26ol_f26_operating_leverage_cycle_betaeb_base_v111_signal(ebit, revenue):
    geb = _f26ol_loggrow(ebit, 21)
    grev = _f26ol_loggrow(revenue, 21)
    cov = geb.rolling(252, min_periods=63).cov(grev)
    var = grev.rolling(252, min_periods=63).var()
    result = (cov / var.replace(0, np.nan)).clip(-25, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# beta of gp-growth on revenue-growth (contribution beta)
def f26ol_f26_operating_leverage_cycle_betagp_base_v112_signal(gp, revenue):
    ggp = _f26ol_loggrow(gp, 21)
    grev = _f26ol_loggrow(revenue, 21)
    cov = ggp.rolling(252, min_periods=63).cov(grev)
    var = grev.rolling(252, min_periods=63).var()
    result = (cov / var.replace(0, np.nan)).clip(-25, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# beta momentum: operating-leverage beta now minus a half-year ago (gearing shift)
def f26ol_f26_operating_leverage_cycle_betamom_base_v113_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 21)
    grev = _f26ol_loggrow(revenue, 21)
    cov = gop.rolling(252, min_periods=63).cov(grev)
    var = grev.rolling(252, min_periods=63).var()
    beta = (cov / var.replace(0, np.nan)).clip(-25, 25)
    result = beta - beta.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of opinc-growth on revenue-growth (how revenue-driven the profit swings are)
def f26ol_f26_operating_leverage_cycle_levrsq_base_v114_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 21)
    grev = _f26ol_loggrow(revenue, 21)
    r = gop.rolling(252, min_periods=63).corr(grev)
    result = (r ** 2) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# === FIXED-COST ABSORPTION (long & alternate) FACETS ===
# fixed-cost absorption over a two-year cycle (structural overhead dilution)
def f26ol_f26_operating_leverage_cycle_fixabs_504d_base_v115_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    result = ratio.shift(504) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# absorption elasticity over a half-year: Δ(opex/rev) per unit revenue-growth
def f26ol_f26_operating_leverage_cycle_absel_126d_base_v116_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    d_ratio = ratio - ratio.shift(126)
    grev = _f26ol_loggrow(revenue, 126)
    result = (d_ratio / grev.replace(0, np.nan)).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# cost elasticity to sales over a half-year (%Δopex / %Δrev), z-scored
def f26ol_f26_operating_leverage_cycle_costelas_base_v117_signal(opex, revenue):
    e = _f26ol_dol(opex, revenue, 126).clip(-15, 15)
    result = _z(e, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# opex-vs-revenue growth-spread over a half-year (cost dilution speed)
def f26ol_f26_operating_leverage_cycle_opexgap_126d_base_v118_signal(opex, revenue):
    result = _f26ol_growthspread(opex, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# downside cost stickiness over a half-year (opex that won't fall when revenue falls)
def f26ol_f26_operating_leverage_cycle_stick_126d_base_v119_signal(opex, revenue):
    gox = _f26ol_loggrow(opex, 126)
    grev = _f26ol_loggrow(revenue, 126)
    sticky = gox.where(grev < 0, 0.0)
    result = sticky.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# absorption acceleration: 126d absorption change now minus a half-year ago
def f26ol_f26_operating_leverage_cycle_absaccel_base_v120_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    fa = ratio.shift(126) - ratio
    dfa = fa - fa.shift(63)
    result = dfa - dfa.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental opex per incremental revenue: Δopex / Δrevenue (marginal cost rate)
def f26ol_f26_operating_leverage_cycle_incopex_252d_base_v121_signal(opex, revenue):
    result = _f26ol_incmargin(opex, revenue, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# absorption asymmetry: opex-gap on expansion minus on contraction (half-year window)
def f26ol_f26_operating_leverage_cycle_absasym_126d_base_v122_signal(opex, revenue):
    g = _f26ol_growthspread(opex, revenue, 126)
    grev = _f26ol_loggrow(revenue, 126)
    up = g.where(grev > 0).rolling(252, min_periods=42).mean()
    dn = g.where(grev < 0).rolling(252, min_periods=42).mean()
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# cost-elasticity dispersion across 63/126/252 (multi-horizon cost-gearing disagreement)
def f26ol_f26_operating_leverage_cycle_eldisp_base_v123_signal(opex, revenue):
    e1 = _f26ol_dol(opex, revenue, 63).clip(-15, 15)
    e2 = _f26ol_dol(opex, revenue, 126).clip(-15, 15)
    e3 = _f26ol_dol(opex, revenue, 252).clip(-15, 15)
    result = pd.concat([e1, e2, e3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental overhead leakage over a half-year: Δ(gp-opinc) / Δgp
def f26ol_f26_operating_leverage_cycle_incovh_126d_base_v124_signal(gp, opinc):
    overhead = gp - opinc
    dovh = _f26ol_dgrow(overhead, 126)
    dgp = _f26ol_dgrow(gp, 126)
    result = (dovh / dgp.replace(0, np.nan)).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# === BREAK-EVEN / MARGIN-OF-SAFETY (long & alternate) FACETS ===
# margin-of-safety over a two-year cycle, smoothed (structural cushion)
def f26ol_f26_operating_leverage_cycle_mos_504d_base_v125_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    result = _mean(mos, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-of-safety half-year momentum (cushion building/eroding faster window)
def f26ol_f26_operating_leverage_cycle_mosmom_126d_base_v126_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    result = mos - mos.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage gearing factor (1/MoS) smoothed (raw leverage multiplier level)
def f26ol_f26_operating_leverage_cycle_gear_252d_base_v127_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gearing = (revenue / (revenue - be_rev).replace(0, np.nan)).clip(-50, 50)
    result = _mean(gearing, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gearing momentum: change in leverage multiplier over a year
def f26ol_f26_operating_leverage_cycle_gearmom_252d_base_v128_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gearing = (revenue / (revenue - be_rev).replace(0, np.nan)).clip(-50, 50)
    result = gearing - gearing.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# break-even outrun ratio over a half-year: rev-growth / break-even-growth (z-scored)
def f26ol_f26_operating_leverage_cycle_begap_126d_base_v129_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gr = _f26ol_pctg(revenue, 126)
    gb = _f26ol_pctg(be_rev, 126)
    ratio = (gr / gb.replace(0, np.nan)).clip(-15, 15)
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# contribution coverage of incremental fixed cost over a half-year: Δgp / Δopex
def f26ol_f26_operating_leverage_cycle_covinc_126d_base_v130_signal(gp, opex):
    dgp = _f26ol_dgrow(gp, 126)
    dox = _f26ol_dgrow(opex, 126)
    result = (dgp / dox.replace(0, np.nan)).clip(-15, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-of-safety vol-of-cushion: instability of the break-even cushion change
def f26ol_f26_operating_leverage_cycle_mosvol_252d_base_v131_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    dmos = mos - mos.shift(21)
    result = _std(dmos, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gearing-driven thrust over a half-year: leverage multiplier x revenue-growth
def f26ol_f26_operating_leverage_cycle_geardrive_126d_base_v132_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gearing = (revenue / (revenue - be_rev).replace(0, np.nan)).clip(-50, 50)
    result = gearing * _f26ol_loggrow(revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# break-even crossing depth-weighted: cushion sign-flips x flip magnitude
def f26ol_f26_operating_leverage_cycle_becrossd_base_v133_signal(gp, opex, revenue):
    cushion = (gp - opex) / revenue.replace(0, np.nan)
    flip = (np.sign(cushion) != np.sign(cushion.shift(21))).astype(float)
    depth = (cushion - cushion.shift(21)).abs()
    result = (flip * depth).rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# break-even sensitivity: Δbreak-even-rev per Δcontribution-rate (gearing-to-margin link)
def f26ol_f26_operating_leverage_cycle_besens_base_v134_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    d_be = _f26ol_loggrow(be_rev, 126)
    d_cm = cm_rate - cm_rate.shift(126)
    result = (d_be / d_cm.replace(0, np.nan)).clip(-20, 20)
    return result.replace([np.inf, -np.inf], np.nan)


# === COMPOSITE / INTERACTION (alternate) FACETS ===
# leverage thrust over a half-year: incremental margin x revenue-growth magnitude
def f26ol_f26_operating_leverage_cycle_incthrust_126d_base_v135_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 126).abs()
    result = inc * grev
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-capture slippage over a half-year: realized spread minus DOL-implied spread
def f26ol_f26_operating_leverage_cycle_capeff_126d_base_v136_signal(opinc, revenue):
    realized = _f26ol_growthspread(opinc, revenue, 126)
    dol = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 126)
    implied = (dol - 1.0) * grev
    result = (realized - implied).clip(-10, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# below-line leakage ratio Δebit/Δopinc over a half-year (interest/D&A amplification)
def f26ol_f26_operating_leverage_cycle_ebleak_126d_base_v137_signal(ebit, opinc):
    deb = _f26ol_dgrow(ebit, 126)
    dop = _f26ol_dgrow(opinc, 126)
    result = (deb / dop.replace(0, np.nan)).clip(-15, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# defensive leverage over a half-year: opinc up while revenue down, depth-weighted
def f26ol_f26_operating_leverage_cycle_defens_126d_base_v138_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 126)
    grev = _f26ol_loggrow(revenue, 126)
    flag = ((gop > 0) & (grev < 0)).astype(float)
    result = flag.rolling(252, min_periods=63).mean() + 0.25 * gop.clip(-2, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# loaded-leverage over a half-year: incremental contribution slope x low margin-of-safety
def f26ol_f26_operating_leverage_cycle_loaded_126d_base_v139_signal(gp, opex, revenue):
    inc_cm = _f26ol_incmargin(gp, revenue, 63).clip(-3, 3)
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    result = inc_cm * (1.0 - mos)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread per unit revenue-growth vol over a half-year (risk-adjusted amplification)
def f26ol_f26_operating_leverage_cycle_gapvol_126d_base_v140_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    vol = _std(_f26ol_loggrow(revenue, 63), 252)
    result = (g / vol.replace(0, np.nan)).clip(-25, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT DOL on expansion minus on contraction (below-line gearing asymmetry)
def f26ol_f26_operating_leverage_cycle_geargasym_base_v141_signal(ebit, revenue):
    d = _f26ol_dol(ebit, revenue, 63).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 63)
    up = d.where(grev > 0).rolling(252, min_periods=42).mean()
    dn = d.where(grev < 0).rolling(252, min_periods=42).mean()
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# incremental EBIT-margin to revenue-growth corr (below-line capture tracking)
def f26ol_f26_operating_leverage_cycle_inccorr_eb_base_v142_signal(ebit, revenue):
    inc = _f26ol_incmargin(ebit, revenue, 21).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 21)
    result = inc.rolling(252, min_periods=63).corr(grev)
    return result.replace([np.inf, -np.inf], np.nan)


# excess DOL over trailing median, quarter window (short de-trended leverage extremity)
def f26ol_f26_operating_leverage_cycle_excessel_126d_base_v143_signal(opinc, revenue):
    raw = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    result = raw - raw.rolling(252, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-spread positive-streak mean over a year (sustained amplification run, half window)
def f26ol_f26_operating_leverage_cycle_gapstreak_126d_base_v144_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    pos = (g > 0).astype(float)
    streak = pos.groupby((pos != pos.shift()).cumsum()).cumcount() + 1
    result = (streak * pos).rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# operating vs gross growth-spread cascade over a half-year (overhead amplification)
def f26ol_f26_operating_leverage_cycle_gapcascade_126d_base_v145_signal(gp, opinc, revenue):
    g_op = _f26ol_growthspread(opinc, revenue, 126)
    g_gp = _f26ol_growthspread(gp, revenue, 126)
    result = g_op - g_gp
    return result.replace([np.inf, -np.inf], np.nan)


# DOL conditioned on contraction over a quarter base (downside gearing, short window)
def f26ol_f26_operating_leverage_cycle_doldn_126d_base_v146_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 63)
    result = d.where(grev < 0).rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# DOL conditioned on expansion over a quarter base (upside gearing, short window)
def f26ol_f26_operating_leverage_cycle_dolup_126d_base_v147_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 63)
    result = d.where(grev > 0).rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-capture efficiency rank: realized minus DOL-implied spread, ranked vs cycle
def f26ol_f26_operating_leverage_cycle_capeffrank_base_v148_signal(opinc, revenue):
    realized = _f26ol_growthspread(opinc, revenue, 252)
    dol = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 252)
    slip = (realized - (dol - 1.0) * grev).clip(-10, 10)
    result = _rank(slip, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# tri-line incremental-margin stack mean (composite leverage capture across gp/opinc/ebit)
def f26ol_f26_operating_leverage_cycle_incstack_base_v149_signal(gp, opinc, ebit, revenue):
    i_gp = _f26ol_incmargin(gp, revenue, 252).clip(-3, 3)
    i_op = _f26ol_incmargin(opinc, revenue, 252).clip(-5, 5)
    i_eb = _f26ol_incmargin(ebit, revenue, 252).clip(-5, 5)
    result = pd.concat([i_gp, i_op, i_eb], axis=1).mean(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-amplification convexity: 2nd-difference of the growth-spread path (gearing curvature)
def f26ol_f26_operating_leverage_cycle_gapconvex_base_v150_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    d2 = g - 2.0 * g.shift(63) + g.shift(126)
    result = d2.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ol_f26_operating_leverage_cycle_dol_504d_base_v076_signal,
    f26ol_f26_operating_leverage_cycle_dolskew_252d_base_v077_signal,
    f26ol_f26_operating_leverage_cycle_doleb_126d_base_v078_signal,
    f26ol_f26_operating_leverage_cycle_dolgp_63d_base_v079_signal,
    f26ol_f26_operating_leverage_cycle_dolterml_base_v080_signal,
    f26ol_f26_operating_leverage_cycle_dolaccel_base_v081_signal,
    f26ol_f26_operating_leverage_cycle_dolexc_252d_base_v082_signal,
    f26ol_f26_operating_leverage_cycle_dolratio_252d_base_v083_signal,
    f26ol_f26_operating_leverage_cycle_dolvov_504d_base_v084_signal,
    f26ol_f26_operating_leverage_cycle_dolflip_252d_base_v085_signal,
    f26ol_f26_operating_leverage_cycle_incop_504d_base_v086_signal,
    f26ol_f26_operating_leverage_cycle_incgp_126d_base_v087_signal,
    f26ol_f26_operating_leverage_cycle_inceb_126d_base_v088_signal,
    f26ol_f26_operating_leverage_cycle_incdisp_base_v089_signal,
    f26ol_f26_operating_leverage_cycle_incterm_base_v090_signal,
    f26ol_f26_operating_leverage_cycle_incosc_base_v091_signal,
    f26ol_f26_operating_leverage_cycle_inccmaccel_base_v092_signal,
    f26ol_f26_operating_leverage_cycle_incstreak_base_v093_signal,
    f26ol_f26_operating_leverage_cycle_incshare_base_v094_signal,
    f26ol_f26_operating_leverage_cycle_incexc_504d_base_v095_signal,
    f26ol_f26_operating_leverage_cycle_gap_504d_base_v096_signal,
    f26ol_f26_operating_leverage_cycle_gap_1260d_base_v097_signal,
    f26ol_f26_operating_leverage_cycle_gaptrend_base_v098_signal,
    f26ol_f26_operating_leverage_cycle_gapema_base_v099_signal,
    f26ol_f26_operating_leverage_cycle_gapeb_126d_base_v100_signal,
    f26ol_f26_operating_leverage_cycle_gapgp_126d_base_v101_signal,
    f26ol_f26_operating_leverage_cycle_gapupdev_base_v102_signal,
    f26ol_f26_operating_leverage_cycle_gapdndev_base_v103_signal,
    f26ol_f26_operating_leverage_cycle_gapyoy_base_v104_signal,
    f26ol_f26_operating_leverage_cycle_stackdisp_base_v105_signal,
    f26ol_f26_operating_leverage_cycle_swing_504d_base_v106_signal,
    f26ol_f26_operating_leverage_cycle_swingrank_base_v107_signal,
    f26ol_f26_operating_leverage_cycle_gapamp_252d_base_v108_signal,
    f26ol_f26_operating_leverage_cycle_dolasym_base_v109_signal,
    f26ol_f26_operating_leverage_cycle_incasym_base_v110_signal,
    f26ol_f26_operating_leverage_cycle_betaeb_base_v111_signal,
    f26ol_f26_operating_leverage_cycle_betagp_base_v112_signal,
    f26ol_f26_operating_leverage_cycle_betamom_base_v113_signal,
    f26ol_f26_operating_leverage_cycle_levrsq_base_v114_signal,
    f26ol_f26_operating_leverage_cycle_fixabs_504d_base_v115_signal,
    f26ol_f26_operating_leverage_cycle_absel_126d_base_v116_signal,
    f26ol_f26_operating_leverage_cycle_costelas_base_v117_signal,
    f26ol_f26_operating_leverage_cycle_opexgap_126d_base_v118_signal,
    f26ol_f26_operating_leverage_cycle_stick_126d_base_v119_signal,
    f26ol_f26_operating_leverage_cycle_absaccel_base_v120_signal,
    f26ol_f26_operating_leverage_cycle_incopex_252d_base_v121_signal,
    f26ol_f26_operating_leverage_cycle_absasym_126d_base_v122_signal,
    f26ol_f26_operating_leverage_cycle_eldisp_base_v123_signal,
    f26ol_f26_operating_leverage_cycle_incovh_126d_base_v124_signal,
    f26ol_f26_operating_leverage_cycle_mos_504d_base_v125_signal,
    f26ol_f26_operating_leverage_cycle_mosmom_126d_base_v126_signal,
    f26ol_f26_operating_leverage_cycle_gear_252d_base_v127_signal,
    f26ol_f26_operating_leverage_cycle_gearmom_252d_base_v128_signal,
    f26ol_f26_operating_leverage_cycle_begap_126d_base_v129_signal,
    f26ol_f26_operating_leverage_cycle_covinc_126d_base_v130_signal,
    f26ol_f26_operating_leverage_cycle_mosvol_252d_base_v131_signal,
    f26ol_f26_operating_leverage_cycle_geardrive_126d_base_v132_signal,
    f26ol_f26_operating_leverage_cycle_becrossd_base_v133_signal,
    f26ol_f26_operating_leverage_cycle_besens_base_v134_signal,
    f26ol_f26_operating_leverage_cycle_incthrust_126d_base_v135_signal,
    f26ol_f26_operating_leverage_cycle_capeff_126d_base_v136_signal,
    f26ol_f26_operating_leverage_cycle_ebleak_126d_base_v137_signal,
    f26ol_f26_operating_leverage_cycle_defens_126d_base_v138_signal,
    f26ol_f26_operating_leverage_cycle_loaded_126d_base_v139_signal,
    f26ol_f26_operating_leverage_cycle_gapvol_126d_base_v140_signal,
    f26ol_f26_operating_leverage_cycle_geargasym_base_v141_signal,
    f26ol_f26_operating_leverage_cycle_inccorr_eb_base_v142_signal,
    f26ol_f26_operating_leverage_cycle_excessel_126d_base_v143_signal,
    f26ol_f26_operating_leverage_cycle_gapstreak_126d_base_v144_signal,
    f26ol_f26_operating_leverage_cycle_gapcascade_126d_base_v145_signal,
    f26ol_f26_operating_leverage_cycle_doldn_126d_base_v146_signal,
    f26ol_f26_operating_leverage_cycle_dolup_126d_base_v147_signal,
    f26ol_f26_operating_leverage_cycle_capeffrank_base_v148_signal,
    f26ol_f26_operating_leverage_cycle_incstack_base_v149_signal,
    f26ol_f26_operating_leverage_cycle_gapconvex_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_OPERATING_LEVERAGE_CYCLE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    revenue = _fund(101, base=2e8, drift=0.01, vol=0.10).rename("revenue")
    opex = _fund(102, base=6e7, drift=0.005, vol=0.07).rename("opex")
    gp = _fund(103, base=9e7, drift=0.008, vol=0.11).rename("gp")
    opinc = _fund(104, base=5e7, drift=0.004, vol=0.16, allow_neg=True).rename("opinc")
    ebit = _fund(105, base=4.5e7, drift=0.004, vol=0.17, allow_neg=True).rename("ebit")

    cols = {"revenue": revenue, "opex": opex, "gp": gp, "opinc": opinc, "ebit": ebit}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f26_operating_leverage_cycle_base_076_150_claude: %d features pass" % n_features)
