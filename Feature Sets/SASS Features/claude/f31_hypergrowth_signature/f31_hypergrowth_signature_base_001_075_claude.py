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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s vs time over window w
    def _f(a):
        k = len(a)
        idx = np.arange(k, dtype=float)
        idx = idx - idx.mean()
        denom = (idx * idx).sum()
        if denom == 0:
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (hypergrowth signature: growth x margin x reinvestment) =====
def _f31_growth(s, w):
    # log growth of a positive fundamental level over window w (trajectory of the level)
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f31_pct_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f31_gross_margin(gp, revenue):
    # gross-margin LEVEL from gp / revenue (an economics distinct from growth)
    return gp / revenue.replace(0, np.nan)


def _f31_rnd_intensity(rnd, revenue):
    # reinvestment intensity (R&D-funded growth fuel)
    return rnd / revenue.replace(0, np.nan)


def _f31_ocf_margin(ncfo, revenue):
    # operating-cash-flow margin (cash quality of growth)
    return ncfo / revenue.replace(0, np.nan)


def _f31_rule40(rev_growth, ocf_margin):
    # Rule-of-40: growth-rate + cash-margin (two distinct economics summed)
    return rev_growth + ocf_margin


def _f31_margin_expansion(margin, w):
    # change in a margin level over window w (margin trajectory)
    return margin - margin.shift(w)


# ============================================================
# revenue-growth x gross-margin-LEVEL (the canonical hypergrowth signature)
def f31hg_f31_hypergrowth_signature_grthmargin_252d_base_v001_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    b = g * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x gross-margin-level over 504d horizon
def f31hg_f31_hypergrowth_signature_grthmargin_504d_base_v002_signal(revenue, gp):
    g = _f31_growth(revenue, 504)
    m = _f31_gross_margin(gp, revenue)
    b = g * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x reported grossmargin column (independent margin source)
def f31hg_f31_hypergrowth_signature_grthgm_252d_base_v003_signal(revenue, grossmargin):
    g = _f31_growth(revenue, 252)
    b = g * grossmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-WITH-expanding-margin: revenue growth times the margin's own slope
def f31hg_f31_hypergrowth_signature_grthexpand_252d_base_v004_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = g * dm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth with expanding reported-grossmargin (both trajectories aligned)
def f31hg_f31_hypergrowth_signature_grthexpgm_252d_base_v005_signal(revenue, grossmargin):
    g = _f31_growth(revenue, 252)
    dm = _f31_margin_expansion(grossmargin, 126)
    b = g * dm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40: 252d revenue growth + OCF margin (growth + cash-margin)
def f31hg_f31_hypergrowth_signature_rule40_252d_base_v006_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = _f31_rule40(g, om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 over 504d horizon
def f31hg_f31_hypergrowth_signature_rule40_504d_base_v007_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 504)
    om = _f31_ocf_margin(ncfo, revenue)
    b = g + om
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 excess driven by cash-margin volatility (cash-quality regime, not raw growth)
def f31hg_f31_hypergrowth_signature_rule40excess_252d_base_v008_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 63)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    b = (om - _mean(om, 252)) + 0.3 * (r40 - _mean(r40, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth: revenue growth x R&D intensity (growth fueled by R&D)
def f31hg_f31_hypergrowth_signature_reinvgrowth_252d_base_v009_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = g * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth over 504d
def f31hg_f31_hypergrowth_signature_reinvgrowth_504d_base_v010_signal(revenue, rnd):
    g = _f31_growth(revenue, 504)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = g * ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R&D-growth leading revenue: rnd growth times current gross margin (seed-of-future)
def f31hg_f31_hypergrowth_signature_rndlead_252d_base_v011_signal(rnd, gp, revenue):
    gr = _f31_growth(rnd, 252)
    m = _f31_gross_margin(gp, revenue)
    b = gr * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite: gp growth x ocf margin (durable profit growth + cash backing)
def f31hg_f31_hypergrowth_signature_durable_252d_base_v012_signal(gp, ncfo, revenue):
    gg = _f31_growth(gp, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = gg * (1.0 + om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality interaction: revenue growth x cash-conversion DEVIATION (ncfo / gp)
def f31hg_f31_hypergrowth_signature_grthquality_252d_base_v013_signal(revenue, ncfo, gp):
    g = _f31_growth(revenue, 252)
    cc = ncfo / gp.replace(0, np.nan)
    ccdev = cc - _mean(cc, 252)
    b = g * cc + 3.0 * g * ccdev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth interacted with margin-level deviation (margin-surprise profit growth)
def f31hg_f31_hypergrowth_signature_gpgrowth_252d_base_v014_signal(gp, revenue):
    gg = _f31_growth(gp, 126)
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    b = gg * (m + 6.0 * mdev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth minus revenue growth (margin-driven outgrowth)
def f31hg_f31_hypergrowth_signature_gpvsrev_252d_base_v015_signal(gp, revenue):
    gg = _f31_growth(gp, 252)
    rg = _f31_growth(revenue, 252)
    b = gg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x margin, z-scored vs its own 252d history (de-trended signature)
def f31hg_f31_hypergrowth_signature_grthmarginz_252d_base_v016_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    b = _z(g * m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 z-scored vs its own history (relative overheat)
def f31hg_f31_hypergrowth_signature_rule40z_252d_base_v017_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = _z(g + om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth ranked vs own 504d history (percentile signature)
def f31hg_f31_hypergrowth_signature_reinvrank_252d_base_v018_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _rank(g * ri, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth composite: growth x margin x cash-margin-DEVIATION (cash-surprise weighted)
def f31hg_f31_hypergrowth_signature_triple_252d_base_v019_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    omdev = om - _mean(om, 252)
    b = g * m + 4.0 * g * m * omdev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin-reinvestment triad sum (balanced hypergrowth score)
def f31hg_f31_hypergrowth_signature_triad_252d_base_v020_signal(revenue, gp, rnd):
    g = _f31_pct_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = g + m + ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth stability x margin: growth divided by its own dispersion, scaled by margin
def f31hg_f31_hypergrowth_signature_stabmargin_252d_base_v021_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    disp = _std(g, 252).replace(0, np.nan)
    m = _f31_gross_margin(gp, revenue)
    b = (g / disp) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 stability: rule-of-40 level scaled by inverse of its own volatility
def f31hg_f31_hypergrowth_signature_rule40stab_252d_base_v022_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    vol = _std(r40, 252).replace(0, np.nan)
    b = r40 / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-weighted growth acceleration: change in (growth x margin) over a quarter
def f31hg_f31_hypergrowth_signature_grthmargmom_252d_base_v023_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    b = gm - gm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment efficiency: revenue growth per unit of R&D intensity (growth bang-per-buck)
def f31hg_f31_hypergrowth_signature_reinveff_252d_base_v024_signal(revenue, rnd):
    g = _f31_pct_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    b = g / ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-funded reinvestment growth: reinvestment intensity scaled by cash-margin coverage
def f31hg_f31_hypergrowth_signature_cashreinv_252d_base_v025_signal(revenue, rnd, ncfo):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    b = ri * np.tanh(4.0 * om) + 0.4 * ri * np.tanh(4.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion funded by reinvestment: margin slope x rnd-intensity DEVIATION
def f31hg_f31_hypergrowth_signature_marginreinv_252d_base_v026_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    ri = _f31_rnd_intensity(rnd, revenue)
    ridev = ri - _mean(ri, 252)
    b = dm * ri + 8.0 * dm * ridev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-with-expanding-margin (504d): growth x reported-grossmargin EXPANSION (pure expansion)
def f31hg_f31_hypergrowth_signature_dualmargexp_504d_base_v027_signal(revenue, gp, grossmargin):
    g = _f31_growth(revenue, 504)
    dm_gp = _f31_margin_expansion(_f31_gross_margin(gp, revenue), 252)
    dm_rep = _f31_margin_expansion(grossmargin, 252)
    b = g * (dm_gp + dm_rep) + 5.0 * dm_gp * dm_rep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF growth x gross margin (cash-flow growth quality)
def f31hg_f31_hypergrowth_signature_ocfgrowth_252d_base_v028_signal(ncfo, gp, revenue):
    og = _f31_growth(ncfo.abs() + 1.0, 252)
    m = _f31_gross_margin(gp, revenue)
    b = og * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable growth: min of revenue-growth and gp-growth, scaled by margin (weakest-link quality)
def f31hg_f31_hypergrowth_signature_weaklink_252d_base_v029_signal(revenue, gp):
    rg = _f31_growth(revenue, 252)
    gg = _f31_growth(gp, 252)
    m = _f31_gross_margin(gp, revenue)
    b = pd.concat([rg, gg], axis=1).min(axis=1) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding ratio trajectory: change in cash-margin-vs-reinvestment, growth-sign gated
def f31hg_f31_hypergrowth_signature_selfffund_252d_base_v030_signal(revenue, ncfo, rnd):
    g = _f31_growth(revenue, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    selffund = np.tanh(om / ri)
    dsf = selffund - selffund.shift(126)
    b = dsf * np.sign(g) + 0.3 * (selffund - _mean(selffund, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 momentum: change in rule-of-40 over a half year (improving signature)
def f31hg_f31_hypergrowth_signature_rule40mom_504d_base_v031_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    b = r40 - r40.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth x margin x reinvestment composite, ranked (full hypergrowth percentile)
def f31hg_f31_hypergrowth_signature_fullrank_252d_base_v032_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = _rank(g * m * (1.0 + ri), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accelerating growth with positive margin: revenue growth slope x margin level
def f31hg_f31_hypergrowth_signature_accelmargin_126d_base_v033_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    accel = g - g.shift(63)
    m = _f31_gross_margin(gp, revenue)
    b = accel * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin level gated by growth sign: margin only counts when growing (regime signature)
def f31hg_f31_hypergrowth_signature_growthgate_252d_base_v034_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    b = m * np.tanh(8.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment growth gated by cash-margin trajectory (improving self-funding of R&D)
def f31hg_f31_hypergrowth_signature_cashgate_252d_base_v035_signal(rnd, revenue, ncfo):
    rg = _f31_growth(rnd, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(126)
    b = rg * np.tanh(8.0 * dom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-margin trajectory x revenue growth trajectory dot-product (aligned improvement)
def f31hg_f31_hypergrowth_signature_aligned_252d_base_v036_signal(revenue, gp):
    rg = _f31_growth(revenue, 126)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    b = np.sign(rg) * np.sign(dm) * (rg.abs() * dm.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 using gp-growth instead of revenue-growth (profit-based rule of 40)
def f31hg_f31_hypergrowth_signature_rule40gp_252d_base_v037_signal(gp, revenue, ncfo):
    gg = _f31_pct_growth(gp, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = gg + om
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity slope x revenue growth (ramping investment behind growth)
def f31hg_f31_hypergrowth_signature_rampinvest_252d_base_v038_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(252)
    g = _f31_growth(revenue, 252)
    b = dri * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-quality: revenue growth weighted by the SPREAD of cash-conversion over reinvestment
def f31hg_f31_hypergrowth_signature_qualbalance_252d_base_v039_signal(revenue, ncfo, rnd, gp):
    g = _f31_growth(revenue, 126)
    cc = ncfo / gp.replace(0, np.nan)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = g * (cc - 3.0 * ri)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable margin-growth: margin-stability premium times margin-expansion times growth
def f31hg_f31_hypergrowth_signature_durmargin_504d_base_v040_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    mvol = _std(m, 252)
    dm = _f31_margin_expansion(m, 252)
    g = _f31_growth(revenue, 504)
    stab = 1.0 / (1.0 + 30.0 * mvol)
    b = stab * (dm + 0.5 * g * m)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth x margin, smoothed with an EMA (persistent signature)
def f31hg_f31_hypergrowth_signature_grthmargema_252d_base_v041_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    b = (g * m).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 EMA-smoothed (durable rule-of-40 regime)
def f31hg_f31_hypergrowth_signature_rule40ema_252d_base_v042_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = (g + om).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth x margin minus its slow EMA (signature displacement / surprise)
def f31hg_f31_hypergrowth_signature_grthmargdisp_252d_base_v043_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    b = gm - gm.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-funded-by-reinvestment ratio: revenue growth divided by R&D growth (leverage)
def f31hg_f31_hypergrowth_signature_grthrndlev_252d_base_v044_signal(revenue, rnd, gp):
    rg = _f31_growth(revenue, 252)
    rdg = _f31_growth(rnd, 252).replace(0, np.nan)
    m = _f31_gross_margin(gp, revenue)
    b = (rg / rdg) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite signature: harmonic blend of growth, margin and cash-margin
def f31hg_f31_hypergrowth_signature_harmonic_252d_base_v045_signal(revenue, gp, ncfo):
    g = _f31_pct_growth(revenue, 252).clip(lower=-0.9) + 1.0
    m = _f31_gross_margin(gp, revenue).clip(lower=0.01)
    om = (1.0 + _f31_ocf_margin(ncfo, revenue)).clip(lower=0.01)
    b = 3.0 / (1.0 / g + 1.0 / m + 1.0 / om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-adjusted revenue growth z-score interaction (relative hypergrowth)
def f31hg_f31_hypergrowth_signature_relgrth_252d_base_v046_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    gz = _z(g, 504)
    m = _f31_gross_margin(gp, revenue)
    mz = _z(m, 504)
    b = gz * mz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth z-interaction
def f31hg_f31_hypergrowth_signature_relreinv_252d_base_v047_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    gz = _z(g, 504)
    ri = _f31_rnd_intensity(rnd, revenue)
    riz = _z(ri, 504)
    b = gz * riz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 cross-check: growth-z plus cash-margin-z (standardized rule of 40)
def f31hg_f31_hypergrowth_signature_relrule40_252d_base_v048_signal(revenue, ncfo):
    g = _f31_pct_growth(revenue, 252)
    gz = _z(g, 504)
    om = _f31_ocf_margin(ncfo, revenue)
    omz = _z(om, 504)
    b = gz + omz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin convexity: penalize when growth high but margin compressing
def f31hg_f31_hypergrowth_signature_convexity_252d_base_v049_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = g * m + 2.0 * g * dm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin-funded growth runway: ocf margin x revenue growth / rnd intensity
def f31hg_f31_hypergrowth_signature_runway_252d_base_v050_signal(revenue, ncfo, rnd):
    om = _f31_ocf_margin(ncfo, revenue)
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    b = (om * g) / ri
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth: 252d revenue growth gated by gp-margin being above its own average
def f31hg_f31_hypergrowth_signature_marggated_252d_base_v051_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    above = m - _mean(m, 252)
    b = g * np.tanh(15.0 * above)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth gated by improving margin (compounding signature)
def f31hg_f31_hypergrowth_signature_compound_252d_base_v052_signal(revenue, rnd, gp):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = g * ri * np.tanh(20.0 * dm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product per unit of its own dispersion (signal-to-noise signature)
def f31hg_f31_hypergrowth_signature_snr_252d_base_v053_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    b = _mean(gm, 252) / _std(gm, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 hit-rate: fraction of last year rule-of-40 exceeded threshold, x margin
def f31hg_f31_hypergrowth_signature_rule40hit_252d_base_v054_signal(revenue, ncfo, gp):
    g = _f31_pct_growth(revenue, 63)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    margin_above = (r40 - _mean(r40, 252)).rolling(126, min_periods=63).mean()
    m = _f31_gross_margin(gp, revenue)
    b = margin_above * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment ramp vs margin defense (investing while protecting margin)
def f31hg_f31_hypergrowth_signature_rampdefend_252d_base_v055_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    b = dri * np.tanh(20.0 * dm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin-reinvestment principal blend of STANDARDIZED components (z-blend)
def f31hg_f31_hypergrowth_signature_blend_252d_base_v056_signal(revenue, gp, rnd, ncfo):
    g = _f31_pct_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    b = 0.4 * _z(g, 252) + 0.3 * _z(m, 252) + 0.15 * _z(ri, 252) + 0.15 * _z(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-dollar growth x cash-margin DEVIATION (cash-surprise on profit growth)
def f31hg_f31_hypergrowth_signature_gpcash_252d_base_v057_signal(gp, ncfo, revenue):
    gg = _f31_growth(gp, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    omdev = om - _mean(om, 252)
    b = gg * omdev + 0.2 * np.sign(gg) * om.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion x cash-margin (profitable scaling without burning cash)
def f31hg_f31_hypergrowth_signature_profscale_252d_base_v058_signal(gp, revenue, ncfo):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    domt = om - om.shift(126)
    b = np.sign(dm) * np.sign(domt) * (dm.abs() * domt.abs()) ** 0.5 + 0.3 * dm * om
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth dispersion-penalized x margin (smooth growers favored)
def f31hg_f31_hypergrowth_signature_smoothgrow_252d_base_v059_signal(revenue, gp):
    g = _f31_growth(revenue, 21)
    smoothpen = 1.0 / (1.0 + 5.0 * _std(g, 126))
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    b = _mean(g, 126) * smoothpen * (m + 4.0 * mdev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 with R&D fuel: reinvestment-intensity trajectory modulated by rule-of-40 sign
def f31hg_f31_hypergrowth_signature_rule40fuel_252d_base_v060_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    b = dri * np.sign(g + om) + 0.5 * (ri - _mean(ri, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-weighted YoY growth change (year-over-year hypergrowth acceleration)
def f31hg_f31_hypergrowth_signature_yoyaccel_252d_base_v061_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    accel = g - g.shift(252)
    m = _f31_gross_margin(gp, revenue)
    b = accel * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-to-cash ratio TRAJECTORY x revenue growth (rising cash-funding pressure)
def f31hg_f31_hypergrowth_signature_reinvcash_252d_base_v062_signal(rnd, ncfo, revenue):
    rc = rnd / ncfo.replace(0, np.nan)
    drc = np.tanh(rc) - np.tanh(rc).shift(126)
    g = _f31_growth(revenue, 126)
    b = drc * (1.0 + g) + 0.3 * np.tanh(rc) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin x revenue-growth-rank cross (high-margin fast-growers)
def f31hg_f31_hypergrowth_signature_marggrowthrank_252d_base_v063_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    grank = _rank(g, 504)
    m = _f31_gross_margin(gp, revenue)
    b = (grank + 0.5) * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-growth: geometric mean of revenue growth and gp growth, x margin
def f31hg_f31_hypergrowth_signature_geodur_252d_base_v064_signal(revenue, gp):
    rg = (1.0 + _f31_pct_growth(revenue, 252)).clip(lower=0.01)
    gg = (1.0 + _f31_pct_growth(gp, 252)).clip(lower=0.01)
    m = _f31_gross_margin(gp, revenue)
    b = (rg * gg) ** 0.5 * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ocf-margin trajectory x revenue growth (improving cash quality of growth)
def f31hg_f31_hypergrowth_signature_cashtraj_252d_base_v065_signal(ncfo, revenue):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    g = _f31_growth(revenue, 252)
    b = dom * g + om * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite signature slope: OLS slope of (growth x margin) over a half year
def f31hg_f31_hypergrowth_signature_gmtrend_126d_base_v066_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    b = _slope(g * m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment intensity x gp-growth (R&D translating into profit growth)
def f31hg_f31_hypergrowth_signature_rndprofit_252d_base_v067_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    gg = _f31_growth(gp, 252)
    b = ri * gg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net hypergrowth signature: reinvestment-drag deviation scaled by growth (drag-dominant)
def f31hg_f31_hypergrowth_signature_netsig_252d_base_v068_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    g = _f31_growth(revenue, 126)
    ridev = ri - _mean(ri, 252)
    b = g * (m - 5.0 * ridev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow growth x margin-expansion (self-funding margin improvement)
def f31hg_f31_hypergrowth_signature_cashmargexp_252d_base_v069_signal(ncfo, gp, revenue):
    og = _f31_growth(ncfo.abs() + 1.0, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    b = og * dm + 0.1 * og
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-trajectory alignment: signs of revenue-growth, margin-slope, cash-margin-slope
def f31hg_f31_hypergrowth_signature_tripalign_252d_base_v070_signal(revenue, gp, ncfo):
    rg = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    b = (np.sign(rg) + np.sign(dm) + np.sign(dom)) * rg.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 vs reinvestment trade-off: cash-margin minus reinvestment burden, growth-gated
def f31hg_f31_hypergrowth_signature_r40net_252d_base_v071_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    b = (om - 0.5 * ri) * (1.0 + np.tanh(4.0 * g))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-margin product percentile-ranked, then differenced (rotation signature)
def f31hg_f31_hypergrowth_signature_gmrotate_252d_base_v072_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    r = _rank(g * m, 252)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x margin-level with a cash-conversion multiplier (full quality stack)
def f31hg_f31_hypergrowth_signature_qualstack_252d_base_v073_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    cc = ncfo / gp.replace(0, np.nan)
    b = g * m * (0.5 + cc.clip(lower=-0.5, upper=2.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-funded growth EMA-smoothed and z-scored (durable reinvestment signature)
def f31hg_f31_hypergrowth_signature_reinvdur_252d_base_v074_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    raw = (g * ri).ewm(span=63, min_periods=21).mean()
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# integrated hypergrowth score: sum of standardized growth, margin-expansion, cash-margin
def f31hg_f31_hypergrowth_signature_integscore_252d_base_v075_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    b = _z(g, 504) + _z(dm, 504) + _z(om, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31hg_f31_hypergrowth_signature_grthmargin_252d_base_v001_signal,
    f31hg_f31_hypergrowth_signature_grthmargin_504d_base_v002_signal,
    f31hg_f31_hypergrowth_signature_grthgm_252d_base_v003_signal,
    f31hg_f31_hypergrowth_signature_grthexpand_252d_base_v004_signal,
    f31hg_f31_hypergrowth_signature_grthexpgm_252d_base_v005_signal,
    f31hg_f31_hypergrowth_signature_rule40_252d_base_v006_signal,
    f31hg_f31_hypergrowth_signature_rule40_504d_base_v007_signal,
    f31hg_f31_hypergrowth_signature_rule40excess_252d_base_v008_signal,
    f31hg_f31_hypergrowth_signature_reinvgrowth_252d_base_v009_signal,
    f31hg_f31_hypergrowth_signature_reinvgrowth_504d_base_v010_signal,
    f31hg_f31_hypergrowth_signature_rndlead_252d_base_v011_signal,
    f31hg_f31_hypergrowth_signature_durable_252d_base_v012_signal,
    f31hg_f31_hypergrowth_signature_grthquality_252d_base_v013_signal,
    f31hg_f31_hypergrowth_signature_gpgrowth_252d_base_v014_signal,
    f31hg_f31_hypergrowth_signature_gpvsrev_252d_base_v015_signal,
    f31hg_f31_hypergrowth_signature_grthmarginz_252d_base_v016_signal,
    f31hg_f31_hypergrowth_signature_rule40z_252d_base_v017_signal,
    f31hg_f31_hypergrowth_signature_reinvrank_252d_base_v018_signal,
    f31hg_f31_hypergrowth_signature_triple_252d_base_v019_signal,
    f31hg_f31_hypergrowth_signature_triad_252d_base_v020_signal,
    f31hg_f31_hypergrowth_signature_stabmargin_252d_base_v021_signal,
    f31hg_f31_hypergrowth_signature_rule40stab_252d_base_v022_signal,
    f31hg_f31_hypergrowth_signature_grthmargmom_252d_base_v023_signal,
    f31hg_f31_hypergrowth_signature_reinveff_252d_base_v024_signal,
    f31hg_f31_hypergrowth_signature_cashreinv_252d_base_v025_signal,
    f31hg_f31_hypergrowth_signature_marginreinv_252d_base_v026_signal,
    f31hg_f31_hypergrowth_signature_dualmargexp_504d_base_v027_signal,
    f31hg_f31_hypergrowth_signature_ocfgrowth_252d_base_v028_signal,
    f31hg_f31_hypergrowth_signature_weaklink_252d_base_v029_signal,
    f31hg_f31_hypergrowth_signature_selfffund_252d_base_v030_signal,
    f31hg_f31_hypergrowth_signature_rule40mom_504d_base_v031_signal,
    f31hg_f31_hypergrowth_signature_fullrank_252d_base_v032_signal,
    f31hg_f31_hypergrowth_signature_accelmargin_126d_base_v033_signal,
    f31hg_f31_hypergrowth_signature_growthgate_252d_base_v034_signal,
    f31hg_f31_hypergrowth_signature_cashgate_252d_base_v035_signal,
    f31hg_f31_hypergrowth_signature_aligned_252d_base_v036_signal,
    f31hg_f31_hypergrowth_signature_rule40gp_252d_base_v037_signal,
    f31hg_f31_hypergrowth_signature_rampinvest_252d_base_v038_signal,
    f31hg_f31_hypergrowth_signature_qualbalance_252d_base_v039_signal,
    f31hg_f31_hypergrowth_signature_durmargin_504d_base_v040_signal,
    f31hg_f31_hypergrowth_signature_grthmargema_252d_base_v041_signal,
    f31hg_f31_hypergrowth_signature_rule40ema_252d_base_v042_signal,
    f31hg_f31_hypergrowth_signature_grthmargdisp_252d_base_v043_signal,
    f31hg_f31_hypergrowth_signature_grthrndlev_252d_base_v044_signal,
    f31hg_f31_hypergrowth_signature_harmonic_252d_base_v045_signal,
    f31hg_f31_hypergrowth_signature_relgrth_252d_base_v046_signal,
    f31hg_f31_hypergrowth_signature_relreinv_252d_base_v047_signal,
    f31hg_f31_hypergrowth_signature_relrule40_252d_base_v048_signal,
    f31hg_f31_hypergrowth_signature_convexity_252d_base_v049_signal,
    f31hg_f31_hypergrowth_signature_runway_252d_base_v050_signal,
    f31hg_f31_hypergrowth_signature_marggated_252d_base_v051_signal,
    f31hg_f31_hypergrowth_signature_compound_252d_base_v052_signal,
    f31hg_f31_hypergrowth_signature_snr_252d_base_v053_signal,
    f31hg_f31_hypergrowth_signature_rule40hit_252d_base_v054_signal,
    f31hg_f31_hypergrowth_signature_rampdefend_252d_base_v055_signal,
    f31hg_f31_hypergrowth_signature_blend_252d_base_v056_signal,
    f31hg_f31_hypergrowth_signature_gpcash_252d_base_v057_signal,
    f31hg_f31_hypergrowth_signature_profscale_252d_base_v058_signal,
    f31hg_f31_hypergrowth_signature_smoothgrow_252d_base_v059_signal,
    f31hg_f31_hypergrowth_signature_rule40fuel_252d_base_v060_signal,
    f31hg_f31_hypergrowth_signature_yoyaccel_252d_base_v061_signal,
    f31hg_f31_hypergrowth_signature_reinvcash_252d_base_v062_signal,
    f31hg_f31_hypergrowth_signature_marggrowthrank_252d_base_v063_signal,
    f31hg_f31_hypergrowth_signature_geodur_252d_base_v064_signal,
    f31hg_f31_hypergrowth_signature_cashtraj_252d_base_v065_signal,
    f31hg_f31_hypergrowth_signature_gmtrend_126d_base_v066_signal,
    f31hg_f31_hypergrowth_signature_rndprofit_252d_base_v067_signal,
    f31hg_f31_hypergrowth_signature_netsig_252d_base_v068_signal,
    f31hg_f31_hypergrowth_signature_cashmargexp_252d_base_v069_signal,
    f31hg_f31_hypergrowth_signature_tripalign_252d_base_v070_signal,
    f31hg_f31_hypergrowth_signature_r40net_252d_base_v071_signal,
    f31hg_f31_hypergrowth_signature_gmrotate_252d_base_v072_signal,
    f31hg_f31_hypergrowth_signature_qualstack_252d_base_v073_signal,
    f31hg_f31_hypergrowth_signature_reinvdur_252d_base_v074_signal,
    f31hg_f31_hypergrowth_signature_integscore_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_HYPERGROWTH_SIGNATURE_REGISTRY_001_075 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, n, base=1e9, drift=0.05, vol=0.06).rename("revenue")
    gp = (_fund(102, n, base=4e8, drift=0.045, vol=0.10)).rename("gp")
    rnd = (_fund(103, n, base=1.2e8, drift=0.035, vol=0.12)).rename("rnd")
    ncfo = _fund(104, n, base=2.5e8, drift=0.025, vol=0.16, allow_neg=True).rename("ncfo")
    grossmargin = _fund(105, n, base=0.45, drift=0.0, vol=0.05).clip(0.05, 0.95).rename("grossmargin")

    cols = {"revenue": revenue, "gp": gp, "rnd": rnd, "ncfo": ncfo,
            "grossmargin": grossmargin}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f31_hypergrowth_signature_base_001_075_claude: %d features pass" % n_features)
