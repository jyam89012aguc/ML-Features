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
# Every primitive expresses a revenue-vs-profit GROWTH sensitivity. NO plain
# margin levels/z/trends/amplitude (those belong to f25). All formulas relate a
# CHANGE in profit to a CHANGE in revenue.
def _f26ol_dgrow(s, w):
    # period delta (level change), used as numerator/denominator of leverage ratios
    return s - s.shift(w)


def _f26ol_pctg(s, w):
    # arithmetic percent change over window (for %d-op / %d-rev DOL forms)
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f26ol_loggrow(s, w):
    # symmetric log growth magnitude over window
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f26ol_dol(profit, revenue, w):
    # degree of operating leverage: %change profit / %change revenue
    gp = profit / profit.shift(w).replace(0, np.nan) - 1.0
    gr = revenue / revenue.shift(w).replace(0, np.nan) - 1.0
    return gp / gr.replace(0, np.nan)


def _f26ol_incmargin(profit, revenue, w):
    # incremental margin = delta profit / delta revenue (NOT a margin level)
    dp = profit - profit.shift(w)
    dr = revenue - revenue.shift(w)
    return dp / dr.replace(0, np.nan)


def _f26ol_growthspread(profit, revenue, w):
    # log profit-growth minus log revenue-growth (operating-leverage spread)
    return _f26ol_loggrow(profit, w) - _f26ol_loggrow(revenue, w)


# ============================================================
# === DEGREE-OF-OPERATING-LEVERAGE (%Δopinc / %Δrevenue) FAMILY ===
# DOL over a year, percentile-ranked vs its 504d history (cyclical leverage state)
def f26ol_f26_operating_leverage_cycle_dol_252d_base_v001_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    result = _rank(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL over a half-year, smoothed over a quarter (sustained leverage magnitude)
def f26ol_f26_operating_leverage_cycle_dol_126d_base_v002_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    result = _mean(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL over a quarter, z-scored vs its own 252d history (de-trended leverage)
def f26ol_f26_operating_leverage_cycle_dol_63d_base_v003_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    result = _z(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-based DOL over a year (%Δebit / %Δrevenue), tanh-bounded
def f26ol_f26_operating_leverage_cycle_doleb_252d_base_v004_signal(ebit, revenue):
    d = _f26ol_dol(ebit, revenue, 252)
    result = np.tanh(0.5 * d)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit DOL over a year (%Δgp / %Δrevenue) — variable-cost leverage
def f26ol_f26_operating_leverage_cycle_dolgp_252d_base_v005_signal(gp, revenue):
    d = _f26ol_dol(gp, revenue, 252).clip(-15, 15)
    result = _mean(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL term-structure: short-horizon DOL minus long-horizon DOL (leverage horizon gap)
def f26ol_f26_operating_leverage_cycle_dolterm_base_v006_signal(opinc, revenue):
    ds = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    dl = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    result = ds - dl
    return result.replace([np.inf, -np.inf], np.nan)


# absolute DOL magnitude (how amplified, regardless of sign), smoothed
def f26ol_f26_operating_leverage_cycle_dolmag_252d_base_v007_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 252).abs().clip(0, 15)
    result = _mean(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL momentum: current 126d DOL minus its level a half-year ago
def f26ol_f26_operating_leverage_cycle_dolmom_126d_base_v008_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    result = d - d.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL dispersion across 63/126/252 windows (multi-horizon leverage disagreement)
def f26ol_f26_operating_leverage_cycle_doldisp_base_v009_signal(opinc, revenue):
    d1 = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    d2 = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    d3 = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    result = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# DOL sign-consistency: fraction of trailing year DOL stayed > 1 (truly levered regime)
def f26ol_f26_operating_leverage_cycle_dollever_252d_base_v010_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 126)
    levered = (d > 1.0).astype(float)
    result = levered.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# === INCREMENTAL / CONTRIBUTION MARGIN (Δprofit / Δrevenue) FAMILY ===
# incremental operating margin over a quarter (Δopinc / Δrevenue)
def f26ol_f26_operating_leverage_cycle_incop_63d_base_v011_signal(opinc, revenue):
    result = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin over a year (Δopinc / Δrevenue)
def f26ol_f26_operating_leverage_cycle_incop_252d_base_v012_signal(opinc, revenue):
    result = _f26ol_incmargin(opinc, revenue, 252).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin over a year (Δgp / Δrevenue) — contribution margin
def f26ol_f26_operating_leverage_cycle_incgp_252d_base_v013_signal(gp, revenue):
    result = _f26ol_incmargin(gp, revenue, 252).clip(-3, 3)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental EBIT margin over a year (Δebit / Δrevenue)
def f26ol_f26_operating_leverage_cycle_inceb_252d_base_v014_signal(ebit, revenue):
    result = _f26ol_incmargin(ebit, revenue, 252).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin smoothed via EMA (sustained leverage capture)
def f26ol_f26_operating_leverage_cycle_incema_252d_base_v015_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    result = inc.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# incremental-margin spread: contribution (Δgp/Δrev) minus operating (Δopinc/Δrev)
# = the incremental overhead absorbed between gross and operating line
def f26ol_f26_operating_leverage_cycle_incspread_252d_base_v016_signal(gp, opinc, revenue):
    icm = _f26ol_incmargin(gp, revenue, 252).clip(-3, 3)
    iom = _f26ol_incmargin(opinc, revenue, 252).clip(-3, 3)
    result = icm - iom
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin percentile-ranked vs its own 504d history (leverage capture state)
def f26ol_f26_operating_leverage_cycle_incrank_252d_base_v017_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    result = _rank(inc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin acceleration: 126d inc-margin now minus a year ago
def f26ol_f26_operating_leverage_cycle_incaccel_252d_base_v018_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 126).clip(-5, 5)
    result = inc - inc.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental-margin consistency: fraction of trailing year Δopinc and Δrevenue same sign
def f26ol_f26_operating_leverage_cycle_inccons_252d_base_v019_signal(opinc, revenue):
    dop = _f26ol_dgrow(opinc, 63)
    drv = _f26ol_dgrow(revenue, 63)
    agree = (np.sign(dop) == np.sign(drv)).astype(float)
    result = agree.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin beats trailing operating margin: leverage-surprise frequency
def f26ol_f26_operating_leverage_cycle_incsurp_252d_base_v020_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    base_om = _mean(opinc / revenue.replace(0, np.nan), 63)
    beats = (inc > base_om).astype(float)
    result = beats.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# === PROFIT-GROWTH MINUS REVENUE-GROWTH SPREAD FAMILY ===
# operating-leverage spread over a year (log opinc-growth minus log revenue-growth)
def f26ol_f26_operating_leverage_cycle_gap_252d_base_v021_signal(opinc, revenue):
    result = _f26ol_growthspread(opinc, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage spread over a half-year
def f26ol_f26_operating_leverage_cycle_gap_126d_base_v022_signal(opinc, revenue):
    result = _f26ol_growthspread(opinc, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage spread over a quarter
def f26ol_f26_operating_leverage_cycle_gap_63d_base_v023_signal(opinc, revenue):
    result = _f26ol_growthspread(opinc, revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT growth-spread over a year (ebit-growth minus revenue-growth)
def f26ol_f26_operating_leverage_cycle_gapeb_252d_base_v024_signal(ebit, revenue):
    result = _f26ol_growthspread(ebit, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth-spread over a year (gp-growth minus revenue-growth)
def f26ol_f26_operating_leverage_cycle_gapgp_252d_base_v025_signal(gp, revenue):
    result = _f26ol_growthspread(gp, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread percentile-ranked vs its own 504d history (leverage capture cycle)
def f26ol_f26_operating_leverage_cycle_gaprank_252d_base_v026_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 252)
    result = _rank(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread oscillator: spread minus its own 252d mean, tanh-bounded
def f26ol_f26_operating_leverage_cycle_gaposc_126d_base_v027_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    osc = g - g.rolling(252, min_periods=63).mean()
    result = np.tanh(3.0 * osc)
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of the leverage spread (root-compressed amplification)
def f26ol_f26_operating_leverage_cycle_gapsignmag_252d_base_v028_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 252)
    result = np.sign(g) * (g.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread dispersion across 63/126/252 horizons (leverage horizon disagreement)
def f26ol_f26_operating_leverage_cycle_gapdisp_base_v029_signal(opinc, revenue):
    g1 = _f26ol_growthspread(opinc, revenue, 63)
    g2 = _f26ol_growthspread(opinc, revenue, 126)
    g3 = _f26ol_growthspread(opinc, revenue, 252)
    result = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between operating leverage-spread and gross leverage-spread (overhead leverage)
def f26ol_f26_operating_leverage_cycle_gapcascade_252d_base_v030_signal(gp, opinc, revenue):
    g_op = _f26ol_growthspread(opinc, revenue, 252)
    g_gp = _f26ol_growthspread(gp, revenue, 252)
    result = g_op - g_gp
    return result.replace([np.inf, -np.inf], np.nan)


# === SWING-AMPLITUDE / ASYMMETRY OF LEVERAGE RESPONSE FAMILY ===
# leverage swing ratio: amplitude of opinc-growth vs amplitude of revenue-growth
def f26ol_f26_operating_leverage_cycle_swing_252d_base_v031_signal(opinc, revenue):
    op_sw = _std(_f26ol_loggrow(opinc, 63), 252)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 252)
    result = (op_sw / rev_sw.replace(0, np.nan)).clip(0, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT swing ratio: amplitude of ebit-growth vs revenue-growth amplitude
def f26ol_f26_operating_leverage_cycle_swingeb_252d_base_v032_signal(ebit, revenue):
    eb_sw = _std(_f26ol_loggrow(ebit, 63), 252)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 252)
    result = (eb_sw / rev_sw.replace(0, np.nan)).clip(0, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit swing ratio: gp-growth amplitude vs revenue-growth amplitude
def f26ol_f26_operating_leverage_cycle_swinggp_252d_base_v033_signal(gp, revenue):
    gp_sw = _std(_f26ol_loggrow(gp, 63), 252)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 252)
    result = (gp_sw / rev_sw.replace(0, np.nan)).clip(0, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# inverse swing ratio (cost rigidity): revenue-growth amplitude vs opinc-growth amplitude
def f26ol_f26_operating_leverage_cycle_rigid_252d_base_v034_signal(opinc, revenue):
    op_sw = _std(_f26ol_loggrow(opinc, 63), 252)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 252)
    result = (rev_sw / op_sw.replace(0, np.nan)).clip(0, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage upside vs downside asymmetry: growth-spread on rev-up minus on rev-down
def f26ol_f26_operating_leverage_cycle_asym_252d_base_v035_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 63)
    grev = _f26ol_loggrow(revenue, 63)
    up = g.where(grev > 0)
    dn = g.where(grev < 0)
    result = up.rolling(252, min_periods=42).mean() - dn.rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# upside leverage thrust: incremental margin captured only when revenue is rising
def f26ol_f26_operating_leverage_cycle_upthrust_252d_base_v036_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 63)
    up_inc = inc.where(grev > 0)
    result = up_inc.rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# downside leverage resilience: incremental margin retained when revenue is falling
def f26ol_f26_operating_leverage_cycle_downresil_252d_base_v037_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 63).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 63)
    dn_inc = inc.where(grev < 0)
    result = dn_inc.rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage swing amplitude trend: how the swing-ratio is widening/narrowing (slope)
def f26ol_f26_operating_leverage_cycle_swingtrend_base_v038_signal(opinc, revenue):
    op_sw = _std(_f26ol_loggrow(opinc, 63), 126)
    rev_sw = _std(_f26ol_loggrow(revenue, 63), 126)
    sr = (op_sw / rev_sw.replace(0, np.nan)).clip(0, 25)
    result = sr - sr.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# co-movement of opinc-growth with revenue-growth (rolling corr) — how tightly levered
def f26ol_f26_operating_leverage_cycle_comove_252d_base_v039_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 21)
    grev = _f26ol_loggrow(revenue, 21)
    result = gop.rolling(252, min_periods=63).corr(grev)
    return result.replace([np.inf, -np.inf], np.nan)


# beta of opinc-growth on revenue-growth (cov/var) — operating-leverage beta
def f26ol_f26_operating_leverage_cycle_beta_252d_base_v040_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 21)
    grev = _f26ol_loggrow(revenue, 21)
    cov = gop.rolling(252, min_periods=63).cov(grev)
    var = grev.rolling(252, min_periods=63).var()
    result = (cov / var.replace(0, np.nan)).clip(-25, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# === FIXED-COST ABSORPTION FAMILY (Δ in cost-intensity driven by revenue) ===
# fixed-cost absorption gap: revenue-growth minus opex-growth (operating-leverage relief)
# >0 means sales outgrew costs -> fixed costs being absorbed/diluted, ranked vs cycle
def f26ol_f26_operating_leverage_cycle_fixabs_252d_base_v041_signal(opex, revenue):
    gap = _f26ol_loggrow(revenue, 252) - _f26ol_loggrow(opex, 252)
    result = _rank(gap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost absorption over a quarter (short-run operating-leverage relief)
def f26ol_f26_operating_leverage_cycle_fixabs_63d_base_v042_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    result = ratio.shift(63) - ratio
    return result.replace([np.inf, -np.inf], np.nan)


# absorption elasticity: Δ(opex/revenue) per unit revenue-growth (cost dilution rate)
def f26ol_f26_operating_leverage_cycle_absel_252d_base_v043_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    d_ratio = ratio - ratio.shift(252)
    grev = _f26ol_loggrow(revenue, 252)
    result = (d_ratio / grev.replace(0, np.nan)).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# cost elasticity to sales: %Δopex / %Δrevenue (variable-cost ratio; <1 = operating leverage)
def f26ol_f26_operating_leverage_cycle_opexgap_252d_base_v044_signal(opex, revenue):
    e = _f26ol_dol(opex, revenue, 252).clip(-15, 15)
    result = _mean(e, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost stickiness: opex-growth that fails to fall when revenue falls (downside rigidity)
def f26ol_f26_operating_leverage_cycle_stick_252d_base_v045_signal(opex, revenue):
    gox = _f26ol_loggrow(opex, 252)
    grev = _f26ol_loggrow(revenue, 252)
    sticky = gox.where(grev < 0, 0.0)
    result = sticky.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# absorption asymmetry: opex-vs-rev gap on expansion minus on contraction
def f26ol_f26_operating_leverage_cycle_absasym_252d_base_v046_signal(opex, revenue):
    g = _f26ol_growthspread(opex, revenue, 63)
    grev = _f26ol_loggrow(revenue, 63)
    up = g.where(grev > 0).rolling(252, min_periods=42).mean()
    dn = g.where(grev < 0).rolling(252, min_periods=42).mean()
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost absorption (level drop in opex/revenue over a year), z-scored vs history
def f26ol_f26_operating_leverage_cycle_absrank_252d_base_v047_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    fa = ratio.shift(252) - ratio
    result = _z(fa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# variable-cost elasticity: %ΔCOGS / %Δrevenue (incremental COGS gearing vs sales)
def f26ol_f26_operating_leverage_cycle_varcost_252d_base_v048_signal(gp, revenue):
    cogs = revenue - gp
    e = _f26ol_dol(cogs, revenue, 252).clip(-10, 10)
    result = _z(e, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental overhead leakage: fraction of incremental gross profit eaten by overhead
# = Δ(gp-opinc) / Δgp (0 = all incremental GP flows to operating income; 1 = all absorbed)
def f26ol_f26_operating_leverage_cycle_incovh_252d_base_v049_signal(gp, opinc):
    overhead = gp - opinc
    dovh = _f26ol_dgrow(overhead, 252)
    dgp = _f26ol_dgrow(gp, 252)
    result = (dovh / dgp.replace(0, np.nan)).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# absorption momentum: 126d absorption now minus its level a half-year ago
def f26ol_f26_operating_leverage_cycle_absmom_126d_base_v050_signal(opex, revenue):
    ratio = opex / revenue.replace(0, np.nan)
    fa = ratio.shift(126) - ratio
    result = fa - fa.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# === BREAK-EVEN / MARGIN-OF-SAFETY (growth-relative, not level) FAMILY ===
# margin-of-safety = revenue headroom above break-even revenue (1 - BE/rev), growth-form
def f26ol_f26_operating_leverage_cycle_mos_252d_base_v051_signal(gp, opex, revenue):
    cm_rate = (gp / revenue.replace(0, np.nan))  # contribution rate
    be_rev = opex / cm_rate.replace(0, np.nan)   # break-even revenue = fixed / contrib-rate
    mos = 1.0 - be_rev / revenue.replace(0, np.nan)
    result = _mean(mos.clip(-5, 5), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-of-safety momentum: change in MoS over a year (cushion building/eroding)
def f26ol_f26_operating_leverage_cycle_mosmom_252d_base_v052_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    result = mos - mos.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# break-even outrun ratio: actual revenue-growth divided by break-even-revenue growth
# (>1 = pulling away from break-even faster than the bar is rising), ranked vs cycle
def f26ol_f26_operating_leverage_cycle_begap_252d_base_v053_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gr = _f26ol_pctg(revenue, 252)
    gb = _f26ol_pctg(be_rev, 252)
    ratio = (gr / gb.replace(0, np.nan)).clip(-15, 15)
    result = _rank(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue distance above break-even per unit contribution rate (leverage gearing now vs trend)
def f26ol_f26_operating_leverage_cycle_gearing_252d_base_v054_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gearing = revenue / (revenue - be_rev).replace(0, np.nan)  # = 1/MoS = leverage factor
    result = _z(gearing.clip(-50, 50), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-of-safety percentile rank vs 504d cycle (break-even cushion state)
def f26ol_f26_operating_leverage_cycle_mosrank_504d_base_v055_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    result = _rank(mos, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# break-even crossing frequency: fraction of trailing year operating cushion flipped sign
def f26ol_f26_operating_leverage_cycle_becross_252d_base_v056_signal(gp, opex):
    cushion = gp - opex
    flip = (np.sign(cushion) != np.sign(cushion.shift(21))).astype(float)
    result = flip.rolling(252, min_periods=63).mean() - 0.25
    return result.replace([np.inf, -np.inf], np.nan)


# contribution coverage of fixed cost: Δgp relative to Δopex (incremental coverage)
def f26ol_f26_operating_leverage_cycle_covinc_252d_base_v057_signal(gp, opex):
    dgp = _f26ol_dgrow(gp, 252)
    dox = _f26ol_dgrow(opex, 252)
    result = (dgp / dox.replace(0, np.nan)).clip(-15, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# operating cushion drawdown from its 504d peak in growth-terms (margin-of-safety erosion)
def f26ol_f26_operating_leverage_cycle_cushdd_504d_base_v058_signal(gp, opex, revenue):
    cushion = (gp - opex) / revenue.replace(0, np.nan)
    dcush = cushion - cushion.shift(126)  # change, not level
    peak = _rmax(dcush, 504)
    result = dcush - peak
    return result.replace([np.inf, -np.inf], np.nan)


# break-even revenue gap momentum (how fast revenue is escaping break-even)
def f26ol_f26_operating_leverage_cycle_bemom_126d_base_v059_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gap = _f26ol_loggrow(revenue, 126) - _f26ol_loggrow(be_rev, 126)
    result = gap - gap.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# gearing factor times revenue-growth = leverage-amplified expected profit thrust
def f26ol_f26_operating_leverage_cycle_geardrive_252d_base_v060_signal(gp, opex, revenue):
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    gearing = (revenue / (revenue - be_rev).replace(0, np.nan)).clip(-50, 50)
    result = gearing * _f26ol_loggrow(revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# === INTERACTION / COMPOSITE OPERATING-LEVERAGE FAMILY ===
# leverage thrust: incremental margin times revenue-growth magnitude (realized amplification)
def f26ol_f26_operating_leverage_cycle_incthrust_252d_base_v061_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 252).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 252).abs()
    result = inc * grev
    return result.replace([np.inf, -np.inf], np.nan)


# DOL conditioned on expansion: DOL only when revenue is growing (upside gearing)
def f26ol_f26_operating_leverage_cycle_dolup_252d_base_v062_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 126)
    result = d.where(grev > 0).rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# DOL conditioned on contraction: DOL only when revenue is shrinking (downside gearing)
def f26ol_f26_operating_leverage_cycle_doldn_252d_base_v063_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 126)
    result = d.where(grev < 0).rolling(252, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage spread per unit revenue-growth volatility (risk-adjusted leverage capture)
def f26ol_f26_operating_leverage_cycle_gapvol_252d_base_v064_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 252)
    vol = _std(_f26ol_loggrow(revenue, 63), 252)
    result = (g / vol.replace(0, np.nan)).clip(-25, 25)
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-vs-opinc incremental leverage: Δebit / Δopinc (below-the-line amplification)
def f26ol_f26_operating_leverage_cycle_ebleak_252d_base_v065_signal(ebit, opinc):
    deb = _f26ol_dgrow(ebit, 252)
    dop = _f26ol_dgrow(opinc, 252)
    result = (deb / dop.replace(0, np.nan)).clip(-15, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage spread minus its slow EMA (operating-leverage MACD on the spread)
def f26ol_f26_operating_leverage_cycle_gapmacd_base_v066_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 126)
    result = g.ewm(span=63, min_periods=21).mean() - g.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# defensive leverage flag: opinc growing while revenue falling, depth-weighted
def f26ol_f26_operating_leverage_cycle_defens_252d_base_v067_signal(opinc, revenue):
    gop = _f26ol_loggrow(opinc, 252)
    grev = _f26ol_loggrow(revenue, 252)
    flag = ((gop > 0) & (grev < 0)).astype(float)
    result = flag.rolling(252, min_periods=63).mean() + 0.25 * gop.clip(-2, 2)
    return result.replace([np.inf, -np.inf], np.nan)


# loaded leverage: high contribution slope AND low margin-of-safety (primed to swing)
def f26ol_f26_operating_leverage_cycle_loaded_252d_base_v068_signal(gp, opex, revenue):
    inc_cm = _f26ol_incmargin(gp, revenue, 126).clip(-3, 3)
    cm_rate = gp / revenue.replace(0, np.nan)
    be_rev = opex / cm_rate.replace(0, np.nan)
    mos = (1.0 - be_rev / revenue.replace(0, np.nan)).clip(-5, 5)
    result = inc_cm * (1.0 - mos)
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity stability: rolling std of DOL (how unstable the leverage relationship is)
def f26ol_f26_operating_leverage_cycle_dolinstab_252d_base_v069_signal(opinc, revenue):
    d = _f26ol_dol(opinc, revenue, 63).clip(-15, 15)
    result = _std(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage capture efficiency: realized growth-spread vs DOL-implied spread (slippage)
def f26ol_f26_operating_leverage_cycle_capeff_252d_base_v070_signal(opinc, revenue):
    realized = _f26ol_growthspread(opinc, revenue, 252)
    dol = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    grev = _f26ol_loggrow(revenue, 252)
    implied = (dol - 1.0) * grev
    result = (realized - implied).clip(-10, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# incremental-margin to revenue-growth correlation (does leverage capture track growth)
def f26ol_f26_operating_leverage_cycle_inccorr_252d_base_v071_signal(opinc, revenue):
    inc = _f26ol_incmargin(opinc, revenue, 21).clip(-5, 5)
    grev = _f26ol_loggrow(revenue, 21)
    result = inc.rolling(252, min_periods=63).corr(grev)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-line amplification ratio: opinc-DOL divided by gp-DOL, rank vs 504d cycle
# (how much MORE the operating line is geared than the gross line)
def f26ol_f26_operating_leverage_cycle_doldiverge_252d_base_v072_signal(gp, opinc, revenue):
    dgp = _f26ol_dol(gp, revenue, 252).clip(-15, 15)
    dop = _f26ol_dol(opinc, revenue, 252).clip(-15, 15)
    ratio = (dop / dgp.replace(0, np.nan)).clip(-15, 15)
    result = _rank(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-spread streak: consecutive quarters opinc-growth beat revenue-growth
def f26ol_f26_operating_leverage_cycle_gapstreak_252d_base_v073_signal(opinc, revenue):
    g = _f26ol_growthspread(opinc, revenue, 63)
    pos = (g > 0).astype(float)
    streak = pos.groupby((pos != pos.shift()).cumsum()).cumcount() + 1
    result = (streak * pos).rolling(252, min_periods=63).max()
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth-conditioned profit elasticity vs its trailing typical (excess leverage)
def f26ol_f26_operating_leverage_cycle_excessel_252d_base_v074_signal(opinc, revenue):
    raw = _f26ol_dol(opinc, revenue, 126).clip(-15, 15)
    result = raw - raw.rolling(252, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# tri-line leverage stack: average of gp/opinc/ebit growth-spreads (composite gearing)
def f26ol_f26_operating_leverage_cycle_stackgap_252d_base_v075_signal(gp, opinc, ebit, revenue):
    g_gp = _f26ol_growthspread(gp, revenue, 252)
    g_op = _f26ol_growthspread(opinc, revenue, 252)
    g_eb = _f26ol_growthspread(ebit, revenue, 252)
    result = pd.concat([g_gp, g_op, g_eb], axis=1).mean(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ol_f26_operating_leverage_cycle_dol_252d_base_v001_signal,
    f26ol_f26_operating_leverage_cycle_dol_126d_base_v002_signal,
    f26ol_f26_operating_leverage_cycle_dol_63d_base_v003_signal,
    f26ol_f26_operating_leverage_cycle_doleb_252d_base_v004_signal,
    f26ol_f26_operating_leverage_cycle_dolgp_252d_base_v005_signal,
    f26ol_f26_operating_leverage_cycle_dolterm_base_v006_signal,
    f26ol_f26_operating_leverage_cycle_dolmag_252d_base_v007_signal,
    f26ol_f26_operating_leverage_cycle_dolmom_126d_base_v008_signal,
    f26ol_f26_operating_leverage_cycle_doldisp_base_v009_signal,
    f26ol_f26_operating_leverage_cycle_dollever_252d_base_v010_signal,
    f26ol_f26_operating_leverage_cycle_incop_63d_base_v011_signal,
    f26ol_f26_operating_leverage_cycle_incop_252d_base_v012_signal,
    f26ol_f26_operating_leverage_cycle_incgp_252d_base_v013_signal,
    f26ol_f26_operating_leverage_cycle_inceb_252d_base_v014_signal,
    f26ol_f26_operating_leverage_cycle_incema_252d_base_v015_signal,
    f26ol_f26_operating_leverage_cycle_incspread_252d_base_v016_signal,
    f26ol_f26_operating_leverage_cycle_incrank_252d_base_v017_signal,
    f26ol_f26_operating_leverage_cycle_incaccel_252d_base_v018_signal,
    f26ol_f26_operating_leverage_cycle_inccons_252d_base_v019_signal,
    f26ol_f26_operating_leverage_cycle_incsurp_252d_base_v020_signal,
    f26ol_f26_operating_leverage_cycle_gap_252d_base_v021_signal,
    f26ol_f26_operating_leverage_cycle_gap_126d_base_v022_signal,
    f26ol_f26_operating_leverage_cycle_gap_63d_base_v023_signal,
    f26ol_f26_operating_leverage_cycle_gapeb_252d_base_v024_signal,
    f26ol_f26_operating_leverage_cycle_gapgp_252d_base_v025_signal,
    f26ol_f26_operating_leverage_cycle_gaprank_252d_base_v026_signal,
    f26ol_f26_operating_leverage_cycle_gaposc_126d_base_v027_signal,
    f26ol_f26_operating_leverage_cycle_gapsignmag_252d_base_v028_signal,
    f26ol_f26_operating_leverage_cycle_gapdisp_base_v029_signal,
    f26ol_f26_operating_leverage_cycle_gapcascade_252d_base_v030_signal,
    f26ol_f26_operating_leverage_cycle_swing_252d_base_v031_signal,
    f26ol_f26_operating_leverage_cycle_swingeb_252d_base_v032_signal,
    f26ol_f26_operating_leverage_cycle_swinggp_252d_base_v033_signal,
    f26ol_f26_operating_leverage_cycle_rigid_252d_base_v034_signal,
    f26ol_f26_operating_leverage_cycle_asym_252d_base_v035_signal,
    f26ol_f26_operating_leverage_cycle_upthrust_252d_base_v036_signal,
    f26ol_f26_operating_leverage_cycle_downresil_252d_base_v037_signal,
    f26ol_f26_operating_leverage_cycle_swingtrend_base_v038_signal,
    f26ol_f26_operating_leverage_cycle_comove_252d_base_v039_signal,
    f26ol_f26_operating_leverage_cycle_beta_252d_base_v040_signal,
    f26ol_f26_operating_leverage_cycle_fixabs_252d_base_v041_signal,
    f26ol_f26_operating_leverage_cycle_fixabs_63d_base_v042_signal,
    f26ol_f26_operating_leverage_cycle_absel_252d_base_v043_signal,
    f26ol_f26_operating_leverage_cycle_opexgap_252d_base_v044_signal,
    f26ol_f26_operating_leverage_cycle_stick_252d_base_v045_signal,
    f26ol_f26_operating_leverage_cycle_absasym_252d_base_v046_signal,
    f26ol_f26_operating_leverage_cycle_absrank_252d_base_v047_signal,
    f26ol_f26_operating_leverage_cycle_varcost_252d_base_v048_signal,
    f26ol_f26_operating_leverage_cycle_incovh_252d_base_v049_signal,
    f26ol_f26_operating_leverage_cycle_absmom_126d_base_v050_signal,
    f26ol_f26_operating_leverage_cycle_mos_252d_base_v051_signal,
    f26ol_f26_operating_leverage_cycle_mosmom_252d_base_v052_signal,
    f26ol_f26_operating_leverage_cycle_begap_252d_base_v053_signal,
    f26ol_f26_operating_leverage_cycle_gearing_252d_base_v054_signal,
    f26ol_f26_operating_leverage_cycle_mosrank_504d_base_v055_signal,
    f26ol_f26_operating_leverage_cycle_becross_252d_base_v056_signal,
    f26ol_f26_operating_leverage_cycle_covinc_252d_base_v057_signal,
    f26ol_f26_operating_leverage_cycle_cushdd_504d_base_v058_signal,
    f26ol_f26_operating_leverage_cycle_bemom_126d_base_v059_signal,
    f26ol_f26_operating_leverage_cycle_geardrive_252d_base_v060_signal,
    f26ol_f26_operating_leverage_cycle_incthrust_252d_base_v061_signal,
    f26ol_f26_operating_leverage_cycle_dolup_252d_base_v062_signal,
    f26ol_f26_operating_leverage_cycle_doldn_252d_base_v063_signal,
    f26ol_f26_operating_leverage_cycle_gapvol_252d_base_v064_signal,
    f26ol_f26_operating_leverage_cycle_ebleak_252d_base_v065_signal,
    f26ol_f26_operating_leverage_cycle_gapmacd_base_v066_signal,
    f26ol_f26_operating_leverage_cycle_defens_252d_base_v067_signal,
    f26ol_f26_operating_leverage_cycle_loaded_252d_base_v068_signal,
    f26ol_f26_operating_leverage_cycle_dolinstab_252d_base_v069_signal,
    f26ol_f26_operating_leverage_cycle_capeff_252d_base_v070_signal,
    f26ol_f26_operating_leverage_cycle_inccorr_252d_base_v071_signal,
    f26ol_f26_operating_leverage_cycle_doldiverge_252d_base_v072_signal,
    f26ol_f26_operating_leverage_cycle_gapstreak_252d_base_v073_signal,
    f26ol_f26_operating_leverage_cycle_excessel_252d_base_v074_signal,
    f26ol_f26_operating_leverage_cycle_stackgap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_OPERATING_LEVERAGE_CYCLE_REGISTRY_001_075 = REGISTRY


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

    print("OK f26_operating_leverage_cycle_base_001_075_claude: %d features pass" % n_features)
