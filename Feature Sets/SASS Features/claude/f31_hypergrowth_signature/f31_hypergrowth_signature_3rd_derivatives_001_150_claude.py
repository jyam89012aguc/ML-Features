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


def _jerk(s, w):
    # 2nd math derivative: second difference over window w (acceleration of the base)
    return s - 2.0 * s.shift(w) + s.shift(2 * w)


# ===== folder domain primitives (hypergrowth signature) =====
def _f31_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f31_pct_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f31_gross_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f31_rnd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f31_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f31_margin_expansion(margin, w):
    return margin - margin.shift(w)


# ============================================================
# jerk of revenue-growth x gross-margin (5d second-diff of a 252d base)
def f31hg_f31_hypergrowth_signature_grthmargin_252d_jerk_v001_signal(revenue, gp):
    base = _f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of revenue-growth x gross-margin (504d base, 63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthmargin_504d_jerk_v002_signal(revenue, gp):
    base = _f31_growth(revenue, 504) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of revenue-growth x reported grossmargin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthgm_252d_jerk_v003_signal(revenue, grossmargin):
    base = _f31_growth(revenue, 252) * grossmargin
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-with-expanding-margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthexpand_252d_jerk_v004_signal(revenue, gp):
    m = _f31_gross_margin(gp, revenue)
    base = _f31_growth(revenue, 252) * _f31_margin_expansion(m, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-with-expanding-reported-margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthexpgm_126d_jerk_v005_signal(revenue, grossmargin):
    base = _f31_growth(revenue, 252) * _f31_margin_expansion(grossmargin, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rule40_252d_jerk_v006_signal(revenue, ncfo):
    base = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 (504d base, 63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rule40_504d_jerk_v007_signal(revenue, ncfo):
    base = _f31_pct_growth(revenue, 504) + _f31_ocf_margin(ncfo, revenue)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-funded growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvgrowth_252d_jerk_v008_signal(revenue, rnd):
    base = _f31_growth(revenue, 252) * _f31_rnd_intensity(rnd, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-funded growth (504d base, 63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvgrowth_504d_jerk_v009_signal(revenue, rnd):
    base = _f31_growth(revenue, 504) * _f31_rnd_intensity(rnd, revenue)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of R&D-growth x gross-margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rndlead_252d_jerk_v010_signal(rnd, gp, revenue):
    base = _f31_growth(rnd, 252) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of durable gp-growth x cash-margin (63d 2nd-diff, cash-level-led)
def f31hg_f31_hypergrowth_signature_durable_252d_jerk_v011_signal(gp, ncfo, revenue):
    om = _f31_ocf_margin(ncfo, revenue)
    base = _f31_growth(gp, 252) * om + 0.3 * _f31_growth(gp, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth x cash-conversion (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthquality_252d_jerk_v012_signal(revenue, ncfo, gp):
    cc = ncfo / gp.replace(0, np.nan)
    base = _f31_growth(revenue, 252) * cc
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gross-profit growth x margin-deviation (5d 2nd-diff, sequential gp-growth)
def f31hg_f31_hypergrowth_signature_gpgrowth_252d_jerk_v013_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    base = _f31_growth(gp, 63) * (m + 6.0 * mdev)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gp-growth minus revenue-growth (margin-outgrowth slope, 21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gpvsrev_252d_jerk_v014_signal(gp, revenue):
    base = _f31_growth(gp, 252) - _f31_growth(revenue, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of z-scored growth-margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthmarginz_252d_jerk_v015_signal(revenue, gp):
    base = _z(_f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue), 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triple growth x margin x cash-DEVIATION (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_triple_252d_jerk_v016_signal(revenue, gp, ncfo):
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    omdev = om - _mean(om, 252)
    base = _f31_growth(revenue, 252) * m + 4.0 * _f31_growth(revenue, 252) * m * omdev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triad sum growth+margin+reinvestment (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_triad_252d_jerk_v017_signal(revenue, gp, rnd):
    base = (_f31_pct_growth(revenue, 252) + _f31_gross_margin(gp, revenue)
            + _f31_rnd_intensity(rnd, revenue))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of stability-margin composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_stabmargin_252d_jerk_v018_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    disp = _std(g, 252).replace(0, np.nan)
    base = (g / disp) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40-stability (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rule40stab_252d_jerk_v019_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40 / _std(r40, 252).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-weighted growth momentum (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthmargmom_252d_jerk_v020_signal(revenue, gp):
    gm = _f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue)
    base = gm - gm.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment efficiency (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinveff_252d_jerk_v021_signal(revenue, rnd):
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    base = _f31_pct_growth(revenue, 252) / ri
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-funded reinvestment growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashreinv_252d_jerk_v022_signal(revenue, rnd, ncfo):
    ri = _f31_rnd_intensity(rnd, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    base = ri * np.tanh(4.0 * om)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-expansion x reinvestment (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_marginreinv_252d_jerk_v023_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = dm * ri
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dual-margin-expansion growth (63d 2nd-diff of 504d base)
def f31hg_f31_hypergrowth_signature_dualmargexp_504d_jerk_v024_signal(revenue, gp, grossmargin):
    g = _f31_growth(revenue, 504)
    dm_gp = _f31_margin_expansion(_f31_gross_margin(gp, revenue), 252)
    dm_rep = _f31_margin_expansion(grossmargin, 252)
    base = g * (dm_gp + dm_rep)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ocf-growth x margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_ocfgrowth_252d_jerk_v025_signal(ncfo, gp, revenue):
    og = _f31_growth(ncfo.abs() + 1.0, 252)
    base = og * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of weakest-link durable growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_weaklink_252d_jerk_v026_signal(revenue, gp):
    rg = _f31_growth(revenue, 252)
    gg = _f31_growth(gp, 252)
    base = pd.concat([rg, gg], axis=1).min(axis=1) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding ratio composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_selfffund_252d_jerk_v027_signal(revenue, ncfo, rnd):
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    base = np.tanh(om / ri)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 momentum (63d 2nd-diff of 504d base)
def f31hg_f31_hypergrowth_signature_rule40mom_504d_jerk_v028_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40 - r40.shift(126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of accel-margin composite (21d 2nd-diff of 126d base)
def f31hg_f31_hypergrowth_signature_accelmargin_126d_jerk_v029_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    accel = g - g.shift(63)
    base = accel * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-gated margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_growthgate_252d_jerk_v030_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    base = _f31_gross_margin(gp, revenue) * np.tanh(8.0 * g)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-gated reinvestment-growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashgate_252d_jerk_v031_signal(rnd, revenue, ncfo):
    rg = _f31_growth(rnd, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(126)
    base = rg * np.tanh(8.0 * dom)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of aligned growth-margin trajectory (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_aligned_252d_jerk_v032_signal(revenue, gp):
    rg = _f31_growth(revenue, 126)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    base = np.sign(rg) * np.sign(dm) * (rg.abs() * dm.abs()) ** 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of profit-based Rule-of-40 (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rule40gp_252d_jerk_v033_signal(gp, revenue, ncfo):
    base = _f31_pct_growth(gp, 252) + _f31_ocf_margin(ncfo, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of ramping-investment-behind-growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rampinvest_252d_jerk_v034_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(252)
    base = dri * _f31_growth(revenue, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of quality-balance composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_qualbalance_252d_jerk_v035_signal(revenue, ncfo, rnd, gp):
    g = _f31_growth(revenue, 126)
    cc = ncfo / gp.replace(0, np.nan)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = g * (cc - 3.0 * ri)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-EMA-smoothed growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthmargema_252d_jerk_v036_signal(revenue, gp):
    gm = _f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue)
    base = gm.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 EMA (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rule40ema_252d_jerk_v037_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-rnd leverage (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthrndlev_252d_jerk_v038_signal(revenue, rnd, gp):
    rdg = _f31_growth(rnd, 252).replace(0, np.nan)
    base = (_f31_growth(revenue, 252) / rdg) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of harmonic growth-margin-cash composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_harmonic_252d_jerk_v039_signal(revenue, gp, ncfo):
    g = _f31_pct_growth(revenue, 252).clip(lower=-0.9) + 1.0
    m = _f31_gross_margin(gp, revenue).clip(lower=0.01)
    om = (1.0 + _f31_ocf_margin(ncfo, revenue)).clip(lower=0.01)
    base = 3.0 / (1.0 / g + 1.0 / m + 1.0 / om)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of relative growth-z x margin-z (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_relgrth_252d_jerk_v040_signal(revenue, gp):
    gz = _z(_f31_growth(revenue, 252), 504)
    mz = _z(_f31_gross_margin(gp, revenue), 504)
    base = gz * mz
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of relative reinvestment-z interaction (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_relreinv_252d_jerk_v041_signal(revenue, rnd):
    gz = _z(_f31_growth(revenue, 252), 504)
    riz = _z(_f31_rnd_intensity(rnd, revenue), 504)
    base = gz * riz
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of standardized Rule-of-40 (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_relrule40_252d_jerk_v042_signal(revenue, ncfo):
    gz = _z(_f31_pct_growth(revenue, 252), 504)
    omz = _z(_f31_ocf_margin(ncfo, revenue), 504)
    base = gz + omz
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin convexity (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_convexity_252d_jerk_v043_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    base = g * m + 2.0 * g * dm
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-margin-funded growth runway (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_runway_252d_jerk_v044_signal(revenue, ncfo, rnd):
    om = _f31_ocf_margin(ncfo, revenue)
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    base = (om * g) / ri
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-gated growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_marggated_252d_jerk_v045_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    above = m - _mean(m, 252)
    base = g * np.tanh(15.0 * above)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of compounding signature (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_compound_252d_jerk_v046_signal(revenue, rnd, gp):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    base = g * ri * np.tanh(20.0 * dm)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin signal-to-noise (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_snr_252d_jerk_v047_signal(revenue, gp):
    gm = _f31_growth(revenue, 63) * _f31_gross_margin(gp, revenue)
    base = _mean(gm, 252) / _std(gm, 252).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-ramp-vs-margin-defense (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rampdefend_252d_jerk_v048_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    base = dri * np.tanh(20.0 * dm)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of standardized blend composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_blend_252d_jerk_v049_signal(revenue, gp, rnd, ncfo):
    g = _f31_pct_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    base = 0.4 * _z(g, 252) + 0.3 * _z(m, 252) + 0.15 * _z(ri, 252) + 0.15 * _z(om, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gp-cash composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gpcash_252d_jerk_v050_signal(gp, ncfo, revenue):
    gg = _f31_growth(gp, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    omdev = om - _mean(om, 252)
    base = gg * omdev + 0.2 * np.sign(gg) * om.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of profitable-scaling composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_profscale_252d_jerk_v051_signal(gp, revenue, ncfo):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    domt = om - om.shift(126)
    base = np.sign(dm) * np.sign(domt) * (dm.abs() * domt.abs()) ** 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of smooth-grower composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_smoothgrow_252d_jerk_v052_signal(revenue, gp):
    g = _f31_growth(revenue, 21)
    smoothpen = 1.0 / (1.0 + 5.0 * _std(g, 126))
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    base = _mean(g, 126) * smoothpen * (m + 4.0 * mdev)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40-with-fuel (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rule40fuel_252d_jerk_v053_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    base = dri * np.sign(g + om) + 0.5 * (ri - _mean(ri, 252))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of yoy growth-acceleration x margin (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_yoyaccel_252d_jerk_v054_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    accel = g - g.shift(252)
    base = accel * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-to-cash trajectory (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvcash_252d_jerk_v055_signal(rnd, ncfo, revenue):
    rc = rnd / ncfo.replace(0, np.nan)
    drc = np.tanh(rc) - np.tanh(rc).shift(126)
    g = _f31_growth(revenue, 126)
    base = drc * (1.0 + g)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin x growth-rank (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_marggrowthrank_252d_jerk_v056_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    grank = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = (grank + 0.5) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of geometric durable growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_geodur_252d_jerk_v057_signal(revenue, gp):
    rg = (1.0 + _f31_pct_growth(revenue, 252)).clip(lower=0.01)
    gg = (1.0 + _f31_pct_growth(gp, 252)).clip(lower=0.01)
    base = (rg * gg) ** 0.5 * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-trajectory composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashtraj_252d_jerk_v058_signal(ncfo, revenue):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    g = _f31_growth(revenue, 252)
    base = dom * g + om * g
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-productivity (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rndprofit_252d_jerk_v059_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    gg = _f31_growth(gp, 252)
    base = ri * gg
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net-margin-minus-reinvestment signature (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_netsig_252d_jerk_v060_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    g = _f31_growth(revenue, 126)
    ridev = ri - _mean(ri, 252)
    base = g * (m - 5.0 * ridev)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-margin-expansion composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashmargexp_252d_jerk_v061_signal(ncfo, gp, revenue):
    og = _f31_growth(ncfo.abs() + 1.0, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    base = og * dm + 0.1 * og
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triple-trajectory alignment (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_tripalign_252d_jerk_v062_signal(revenue, gp, ncfo):
    rg = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    base = (np.sign(rg) + np.sign(dm) + np.sign(dom)) * rg.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net Rule-of-40 (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40net_252d_jerk_v063_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = (om - 0.5 * ri) * (1.0 + np.tanh(4.0 * g))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin rank rotation (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gmrotate_252d_jerk_v064_signal(revenue, gp):
    gm = _f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue)
    r = gm.rolling(252, min_periods=63).rank(pct=True) - 0.5
    base = r - r.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of quality-stack composite (63d 2nd-diff, cash-conversion-led)
def f31hg_f31_hypergrowth_signature_qualstack_252d_jerk_v065_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    cc = ncfo / gp.replace(0, np.nan)
    ccdev = (cc - _mean(cc, 252)).clip(lower=-2.0, upper=2.0)
    base = g * m * ccdev * 2.0 + 0.2 * g * m
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of durable reinvestment z-signature (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvdur_252d_jerk_v066_signal(revenue, rnd):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    raw = (g * ri).ewm(span=63, min_periods=21).mean()
    base = _z(raw, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of integrated hypergrowth z-score (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_integscore_252d_jerk_v067_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    base = _z(g, 504) + _z(dm, 504) + _z(om, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of sequential-growth x margin (5d 2nd-diff of 63d base)
def f31hg_f31_hypergrowth_signature_seqgrth_63d_jerk_v068_signal(revenue, gp):
    base = _f31_growth(revenue, 63) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of sequential gp-growth x reported margin (5d 2nd-diff)
def f31hg_f31_hypergrowth_signature_seqgpgrth_63d_jerk_v069_signal(gp, grossmargin):
    base = _f31_growth(gp, 63) * grossmargin
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CAGR x margin-DEVIATION (21d 2nd-diff of 504d base)
def f31hg_f31_hypergrowth_signature_cagrmargin_504d_jerk_v070_signal(revenue, gp):
    cagr = (1.0 + _f31_pct_growth(revenue, 504)).clip(lower=0.01) ** 0.5 - 1.0
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    base = cagr * (m + 5.0 * mdev)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CAGR Rule-of-40 (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cagrrule40_504d_jerk_v071_signal(revenue, ncfo):
    cagr = (1.0 + _f31_pct_growth(revenue, 504)).clip(lower=0.01) ** 0.5 - 1.0
    base = cagr + _f31_ocf_margin(ncfo, revenue)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of re-acceleration x margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reaccel_252d_jerk_v072_signal(revenue, gp):
    gs = _f31_growth(revenue, 63)
    gl = _f31_growth(revenue, 252) * (63.0 / 252.0)
    base = (gs - gl) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-acceleration x cash (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvaccel_252d_jerk_v073_signal(rnd, revenue, ncfo):
    ri = _f31_rnd_intensity(rnd, revenue)
    accel = ri - 2.0 * ri.shift(126) + ri.shift(252)
    base = accel * (1.0 + _f31_ocf_margin(ncfo, revenue))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-slope x growth (21d 2nd-diff of 126d base)
def f31hg_f31_hypergrowth_signature_margslope_126d_jerk_v074_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    dm = m - m.shift(63)
    base = dm * _f31_growth(revenue, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of consistency-penalized growth-margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_consistgm_252d_jerk_v075_signal(revenue, gp):
    gm = _f31_growth(revenue, 63) * _f31_gross_margin(gp, revenue)
    base = _mean(gm, 252) - 1.5 * _std(gm, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 consistency (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40consist_252d_jerk_v076_signal(revenue, ncfo):
    g = _f31_growth(revenue, 63)
    om = _f31_ocf_margin(ncfo, revenue)
    r40 = g + om
    downside = r40.where(r40 < _mean(r40, 252)).rolling(252, min_periods=63).std()
    base = _mean(r40, 252) - downside
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin hit-rate (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gmhit_252d_jerk_v077_signal(revenue, gp):
    g = _f31_growth(revenue, 21)
    m = _f31_gross_margin(gp, revenue)
    dm = m - m.shift(21)
    both = ((g > 0) & (dm > 0)).astype(float)
    base = both.rolling(252, min_periods=126).mean() + 0.2 * m
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment hit-rate (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvhit_252d_jerk_v078_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(21)
    g = _f31_growth(revenue, 21)
    both = ((g > 0) & (dri > 0)).astype(float)
    base = both.rolling(252, min_periods=126).mean() + 0.3 * ri
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth asymmetry x margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthasym_252d_jerk_v079_signal(revenue, gp):
    g = _f31_growth(revenue, 21)
    up = g.where(g > 0).rolling(252, min_periods=63).std()
    dn = g.where(g < 0).rolling(252, min_periods=63).std()
    base = (up - dn) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-asymmetry composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashasym_252d_jerk_v080_signal(ncfo, revenue):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(21)
    up = dom.where(dom > 0).rolling(252, min_periods=63).std()
    dn = dom.where(dom < 0).rolling(252, min_periods=63).std()
    base = (dn - up) * (1.0 + _f31_growth(revenue, 126))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triad-rank composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_triadrank_252d_jerk_v081_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 252).rolling(504, min_periods=126).rank(pct=True) - 0.5
    m = _f31_gross_margin(gp, revenue).rolling(504, min_periods=126).rank(pct=True) - 0.5
    ri = _f31_rnd_intensity(rnd, revenue).rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = (g + m + ri) / 3.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 rank (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40rank_252d_jerk_v082_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of efficient-reinvestment composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_effreinv_252d_jerk_v083_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    rirank = ri.rolling(504, min_periods=126).rank(pct=True)
    base = dm * rirank
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of log-score composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_logscore_252d_jerk_v084_signal(revenue, gp, ncfo):
    g = (1.0 + _f31_pct_growth(revenue, 252)).clip(lower=0.05)
    m = _f31_gross_margin(gp, revenue).clip(lower=0.01)
    om = (1.0 + _f31_ocf_margin(ncfo, revenue)).clip(lower=0.05)
    base = np.log(g) + np.log(m) + np.log(om)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-quality momentum (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gqmom_252d_jerk_v085_signal(revenue, ncfo, gp):
    cc = ncfo / gp.replace(0, np.nan)
    gq = _f31_growth(revenue, 252) * cc
    base = gq - gq.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment momentum (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvmom_252d_jerk_v086_signal(revenue, rnd):
    rg = _f31_growth(revenue, 252) * _f31_rnd_intensity(rnd, revenue)
    base = rg - rg.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-defended growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_margdefend_252d_jerk_v087_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    mvol = _std(m, 252)
    base = g * m - 20.0 * g.abs() * mvol
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-defended Rule-of-40 (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40defend_252d_jerk_v088_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40 - 1.5 * _std(r40, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funded full growth (63d 2nd-diff, coverage-led)
def f31hg_f31_hypergrowth_signature_selfgrow_252d_jerk_v089_signal(revenue, gp, rnd, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    cov = (ncfo - rnd) / revenue.replace(0, np.nan)
    covdev = cov - _mean(cov, 252)
    base = g * m * covdev * 3.0 + 0.2 * g * m
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of free-cash-after-RnD margin growth (63d 2nd-diff, fcf-deviation-led)
def f31hg_f31_hypergrowth_signature_fcfreinv_252d_jerk_v090_signal(ncfo, rnd, revenue):
    fcfar = (ncfo - rnd) / revenue.replace(0, np.nan)
    fdev = fcfar - _mean(fcfar, 252)
    g = _f31_growth(revenue, 126)
    base = fdev * (1.0 + g) + 0.3 * fcfar
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of quality-funded composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_qualfunded_252d_jerk_v091_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    rg = (g * ri).rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = m * rg
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of min-of-all durable growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_minall_252d_jerk_v092_signal(revenue, gp, ncfo):
    rg = _f31_growth(revenue, 252)
    gg = _f31_growth(gp, 252)
    og = _f31_growth(ncfo.abs() + 1.0, 252)
    base = pd.concat([rg, gg, og], axis=1).min(axis=1) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin EMA crossover (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gmcross_252d_jerk_v093_signal(revenue, gp):
    gm = _f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue)
    base = gm.ewm(span=21, min_periods=10).mean() - gm.ewm(span=126, min_periods=42).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 EMA crossover (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40cross_252d_jerk_v094_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40.ewm(span=21, min_periods=10).mean() - r40.ewm(span=126, min_periods=42).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-convexity composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_margconvex_252d_jerk_v095_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    accel = m - 2.0 * m.shift(126) + m.shift(252)
    base = accel * (1.0 + 3.0 * _f31_growth(revenue, 252))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of z-reinvestment interaction (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_zreinv_252d_jerk_v096_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    g = _f31_growth(revenue, 252)
    base = _z(ri, 252) * _z(g, 252) + 0.3 * _z(ri, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of z-cash-margin x margin-expansion (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_zcashmarg_252d_jerk_v097_signal(ncfo, revenue, gp):
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    base = _z(om, 252) * _z(dm, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triple-z product (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_triplez_252d_jerk_v098_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    base = _z(g, 252) * _z(m, 252) + _z(g, 252) * _z(om, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of R&D-productivity growth x margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_rndprod_252d_jerk_v099_signal(gp, rnd, revenue):
    prod = gp / rnd.replace(0, np.nan)
    base = _f31_growth(prod, 252) * _f31_gross_margin(gp, revenue)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of sales-productivity growth x cash (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_salesprod_252d_jerk_v100_signal(revenue, rnd, ncfo):
    prod = revenue / rnd.replace(0, np.nan)
    base = _f31_growth(prod, 252) * (1.0 + _f31_ocf_margin(ncfo, revenue))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin rank EMA (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gmrankema_252d_jerk_v101_signal(revenue, gp):
    gm = _f31_growth(revenue, 252) * _f31_gross_margin(gp, revenue)
    r = gm.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = r.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of net Rule-of-40 rank (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40netrank_252d_jerk_v102_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = (g + om - 4.0 * ri).rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of co-improvement composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_comprove_252d_jerk_v103_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    dm = m - m.shift(63)
    g = _f31_growth(revenue, 252)
    dg = g - g.shift(63)
    base = np.sign(dg) * dm.abs() + np.sign(dm) * dg.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-conversion-stability composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_ccstab_252d_jerk_v104_signal(ncfo, gp, revenue):
    cc = ncfo / gp.replace(0, np.nan)
    stab = 1.0 / (1.0 + 5.0 * _std(cc, 126))
    g = _f31_growth(revenue, 252)
    ccdev = cc - _mean(cc, 252)
    base = stab * np.sign(g) + ccdev * np.tanh(3.0 * g)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of organic-vs-funded composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_organic_252d_jerk_v105_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 126)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    base = -dri + 0.5 * g * m - 3.0 * dri * np.sign(g)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-impulse composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_reinvimp_252d_jerk_v106_signal(revenue, rnd):
    g = _f31_growth(revenue, 126)
    ri = _f31_rnd_intensity(rnd, revenue)
    rg = (g * ri).ewm(span=42, min_periods=21).mean()
    base = rg - rg.shift(42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-streak x margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_growstreak_252d_jerk_v107_signal(revenue, gp):
    g = _f31_growth(revenue, 63)
    streak = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    base = streak * _f31_gross_margin(gp, revenue) + 0.1 * _mean(g, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-streak composite (63d 2nd-diff, cash-deviation-led)
def f31hg_f31_hypergrowth_signature_cashstreak_252d_jerk_v108_signal(ncfo, revenue):
    pos = (ncfo > 0).astype(float).rolling(252, min_periods=126).mean()
    g = _f31_growth(revenue, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    base = pos * np.tanh(4.0 * g) + 2.0 * (om - _mean(om, 252))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of funded-acceleration composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_fundedaccel_252d_jerk_v109_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(126)
    base = dri * (1.0 + np.tanh(5.0 * g)) + g * m * dri * 10.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gp-dollar cash composite (5d 2nd-diff, sequential gp-growth)
def f31hg_f31_hypergrowth_signature_gpdollar_252d_jerk_v110_signal(gp, ncfo, revenue):
    gg = _f31_growth(gp, 21)
    om = _f31_ocf_margin(ncfo, revenue)
    base = gg * (om - _mean(om, 126)) + 0.3 * gg
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 x margin (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40margin_252d_jerk_v111_signal(revenue, ncfo, gp):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    base = (g + om) * (0.5 + m)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-leverage composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_marglev_252d_jerk_v112_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    g = _f31_pct_growth(revenue, 252).replace(0, np.nan)
    base = np.tanh(dm / g.abs().clip(lower=0.02)) * m
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-per-reinvestment (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_growperreinv_252d_jerk_v113_signal(revenue, rnd):
    g = _f31_pct_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue).replace(0, np.nan)
    base = (g / ri).ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of twin-margin composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_twinmargin_252d_jerk_v114_signal(ncfo, revenue, gp):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    base = dom * m + dm * (0.5 + om)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin Sharpe (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gmsharpe_252d_jerk_v115_signal(revenue, gp):
    gm = _f31_growth(revenue, 63) * _f31_gross_margin(gp, revenue)
    base = _mean(gm, 252) / _std(gm, 126).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triad-min composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_triadmin_252d_jerk_v116_signal(revenue, gp, rnd):
    g = _f31_growth(revenue, 252).rolling(504, min_periods=126).rank(pct=True) - 0.5
    m = _f31_gross_margin(gp, revenue).rolling(504, min_periods=126).rank(pct=True) - 0.5
    ri = _f31_rnd_intensity(rnd, revenue).rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = pd.concat([g, m, ri], axis=1).min(axis=1)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-positive growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashposgrow_252d_jerk_v117_signal(revenue, ncfo, gp):
    g = _f31_growth(revenue, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    gate = np.tanh(10.0 * om)
    base = gate * np.tanh(5.0 * g) + 0.3 * gate * m
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of invest-into-margin composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_investmargin_252d_jerk_v118_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    base = np.sign(dri) * dm.abs() + dri * m
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of long-durable composite (63d 2nd-diff of 504d base)
def f31hg_f31_hypergrowth_signature_longdur_504d_jerk_v119_signal(revenue, gp, ncfo):
    cagr = (1.0 + _f31_pct_growth(revenue, 504)).clip(lower=0.01) ** 0.5 - 1.0
    om = _f31_ocf_margin(ncfo, revenue)
    omdev = om - _mean(om, 252)
    m = _f31_gross_margin(gp, revenue)
    base = cagr * omdev + 0.2 * cagr * np.sign(m)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth-margin YoY normalized (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gmyoy_252d_jerk_v120_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    gm = g * m
    chg = gm - gm.shift(252)
    base = chg / (1.0 + _std(gm, 252)) + 0.5 * np.sign(chg) * (m - _mean(m, 252))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of Rule-of-40 resilience (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_r40resil_252d_jerk_v121_signal(revenue, ncfo):
    r40 = _f31_pct_growth(revenue, 252) + _f31_ocf_margin(ncfo, revenue)
    base = r40 - r40.rolling(504, min_periods=126).min()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of high-margin-grower composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_hmgrow_252d_jerk_v122_signal(gp, revenue):
    m = _f31_gross_margin(gp, revenue)
    g = _f31_growth(revenue, 252)
    grank = g.rolling(504, min_periods=126).rank(pct=True)
    raw = m * grank
    base = raw.ewm(span=42, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of clean-funded growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cleanfunded_252d_jerk_v123_signal(revenue, rnd, gp):
    g = _f31_growth(revenue, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    mvol = _std(m, 252)
    base = (g * ri) / (1.0 + 25.0 * mvol)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-efficient growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashefficient_252d_jerk_v124_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    burn = (-om).clip(lower=0)
    base = -burn * (1.0 + g.abs()) - 0.3 * _std(om, 126) * np.sign(m)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gp-reinvestment-rank composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_gpreinvrank_252d_jerk_v125_signal(gp, rnd, revenue):
    gg = _f31_growth(gp, 252)
    ri = _f31_rnd_intensity(rnd, revenue)
    rirank = ri.rolling(504, min_periods=126).rank(pct=True)
    base = gg * rirank
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of triad-slope composite (21d 2nd-diff of 126d base)
def f31hg_f31_hypergrowth_signature_triadslope_126d_jerk_v126_signal(revenue, gp, rnd):
    g = _f31_pct_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    triad = g + m + ri
    base = triad - triad.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of smooth-cash composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_smoothcash_252d_jerk_v127_signal(revenue, ncfo):
    g = _f31_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    omvol = _std(om, 126)
    smoothcash = om / (1.0 + 8.0 * omvol)
    base = smoothcash * (1.0 + 2.0 * g) - 0.5 * omvol
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of twin-expansion composite (63d 2nd-diff, product form)
def f31hg_f31_hypergrowth_signature_twinexp_252d_jerk_v128_signal(gp, revenue, ncfo):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    base = dm * dom * 100.0 + 0.1 * (dm + dom)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of discipline composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_discipline_252d_jerk_v129_signal(revenue, ncfo, gp, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    disc = 1.0 / (1.0 + _std(ri, 252) * 30.0)
    base = (g + om) * m * disc
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of twin-growth composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_twingrow_252d_jerk_v130_signal(revenue, gp):
    rg = _f31_growth(revenue, 252)
    gg = _f31_growth(gp, 252)
    m = _f31_gross_margin(gp, revenue)
    base = rg * gg * np.sign(m) + 0.1 * (rg + gg) * m
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of quality-reinvestor composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_qualreinv_252d_jerk_v131_signal(rnd, revenue, gp):
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    base = _z(ri, 252) * _z(m, 252) + 0.2 * _z(ri * m, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of lean-growth composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_leangrow_252d_jerk_v132_signal(revenue, ncfo, rnd):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    r40r = (g + om).rolling(504, min_periods=126).rank(pct=True)
    rir = ri.rolling(504, min_periods=126).rank(pct=True)
    base = r40r - rir
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of clean-surprise composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cleansurp_252d_jerk_v133_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    omsurp = om - om.ewm(span=126, min_periods=63).mean()
    base = omsurp * (1.0 + 3.0 * g * m)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of multi-horizon consensus composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_consensus_252d_jerk_v134_signal(revenue, gp):
    g1 = _f31_growth(revenue, 126)
    g2 = _f31_growth(revenue, 252) * 0.5
    g3 = _f31_growth(revenue, 504) * 0.25
    consensus = (np.sign(g1) + np.sign(g2) + np.sign(g3))
    m = _f31_gross_margin(gp, revenue)
    mdev = m - _mean(m, 252)
    base = consensus * (m + 5.0 * mdev)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-funds-rnd composite (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cashfundsrnd_252d_jerk_v135_signal(ncfo, revenue, rnd):
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(126)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = dom * ri + 0.5 * np.sign(dom) * ri
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of durable-score composite (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_durscore_252d_jerk_v136_signal(revenue, gp, ncfo, rnd):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = (_z(g, 504) + 0.7 * _z(m, 504) + 0.7 * _z(dm, 504)
            + 0.5 * _z(om, 504) - 0.3 * _z(_std(ri, 126), 504))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of cash-validated hypergrowth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_ccvalid_252d_jerk_v137_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    cc = ncfo / gp.replace(0, np.nan)
    ccrank = cc.rolling(504, min_periods=126).rank(pct=True)
    base = g * m * ccrank
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of integrated-full signature (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_integfull_252d_jerk_v138_signal(revenue, ncfo, rnd, gp):
    g = _f31_pct_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 252)
    gstab = _f31_growth(revenue, 63)
    stab = 1.0 / (1.0 + 10.0 * _std(gstab, 252))
    r40r = (g + om - ri).rolling(504, min_periods=126).rank(pct=True)
    base = r40r * (1.0 + 5.0 * dm) * stab
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of revenue-growth x cash-conversion deviation (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthccdev_252d_jerk_v139_signal(revenue, ncfo, gp):
    g = _f31_growth(revenue, 252)
    cc = ncfo / gp.replace(0, np.nan)
    ccdev = cc - _mean(cc, 252)
    base = g * cc + 3.0 * g * ccdev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-expansion x reinvestment-deviation (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_margreindev_252d_jerk_v140_signal(gp, revenue, rnd):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    ri = _f31_rnd_intensity(rnd, revenue)
    ridev = ri - _mean(ri, 252)
    base = dm * ri + 8.0 * dm * ridev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of CAGR x cash Rule-of-40 (sequential, 63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_cagrseq_504d_jerk_v141_signal(revenue, gp, ncfo):
    cagr = (1.0 + _f31_pct_growth(revenue, 252)) - 1.0
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    base = cagr * m + 0.5 * om
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding spread x growth (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_selffundgr_252d_jerk_v142_signal(revenue, ncfo, rnd):
    g = _f31_growth(revenue, 252)
    om = _f31_ocf_margin(ncfo, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = g * (om - ri)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-weighted growth z (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthzmarg_252d_jerk_v143_signal(revenue, gp):
    g = _f31_growth(revenue, 252)
    gz = _z(g, 504)
    m = _f31_gross_margin(gp, revenue)
    base = gz * m
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-funded growth rank (63d 2nd-diff, longer-window rank)
def f31hg_f31_hypergrowth_signature_reinvfundrank_252d_jerk_v144_signal(revenue, rnd):
    g = _f31_growth(revenue, 126)
    ri = _f31_rnd_intensity(rnd, revenue)
    base = (g * ri).rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of profit-growth x cash-margin-improvement (63d 2nd-diff, distinct horizon)
def f31hg_f31_hypergrowth_signature_gpomdev_252d_jerk_v145_signal(gp, ncfo, revenue):
    gg = _f31_growth(gp, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    dom = om - om.shift(252)
    base = gg * dom + 0.2 * np.sign(gg) * om.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth x margin gated by cash sign (63d 2nd-diff, cash-gate-led)
def f31hg_f31_hypergrowth_signature_gmgated_252d_jerk_v146_signal(revenue, gp, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    gate = np.tanh(8.0 * om)
    base = gate * (0.5 + g * m) + 0.3 * gate
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of reinvestment-intensity-trend x growth (63d 2nd-diff, longer trend)
def f31hg_f31_hypergrowth_signature_ritrendgr_252d_jerk_v147_signal(rnd, revenue):
    ri = _f31_rnd_intensity(rnd, revenue)
    dri = ri - ri.shift(252)
    g = _f31_growth(revenue, 126)
    base = dri * (1.0 + 2.0 * g)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margin-trajectory x cash-margin (63d 2nd-diff, cash-weighted product)
def f31hg_f31_hypergrowth_signature_margtrajcash_252d_jerk_v148_signal(gp, revenue, ncfo):
    m = _f31_gross_margin(gp, revenue)
    dm = _f31_margin_expansion(m, 126)
    om = _f31_ocf_margin(ncfo, revenue)
    base = dm * om * 5.0 + 0.3 * dm * np.sign(om)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of growth x reported-grossmargin expansion (21d 2nd-diff)
def f31hg_f31_hypergrowth_signature_grthrepexp_252d_jerk_v149_signal(revenue, grossmargin):
    g = _f31_growth(revenue, 252)
    dm = _f31_margin_expansion(grossmargin, 252)
    base = g * (grossmargin + 3.0 * dm)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of full integrated z-composite (63d 2nd-diff)
def f31hg_f31_hypergrowth_signature_zfull_252d_jerk_v150_signal(revenue, gp, rnd, ncfo):
    g = _f31_growth(revenue, 252)
    m = _f31_gross_margin(gp, revenue)
    ri = _f31_rnd_intensity(rnd, revenue)
    om = _f31_ocf_margin(ncfo, revenue)
    base = _z(g, 504) * _z(m, 504) + _z(ri, 504) * _z(om, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31hg_f31_hypergrowth_signature_grthmargin_252d_jerk_v001_signal,
    f31hg_f31_hypergrowth_signature_grthmargin_504d_jerk_v002_signal,
    f31hg_f31_hypergrowth_signature_grthgm_252d_jerk_v003_signal,
    f31hg_f31_hypergrowth_signature_grthexpand_252d_jerk_v004_signal,
    f31hg_f31_hypergrowth_signature_grthexpgm_126d_jerk_v005_signal,
    f31hg_f31_hypergrowth_signature_rule40_252d_jerk_v006_signal,
    f31hg_f31_hypergrowth_signature_rule40_504d_jerk_v007_signal,
    f31hg_f31_hypergrowth_signature_reinvgrowth_252d_jerk_v008_signal,
    f31hg_f31_hypergrowth_signature_reinvgrowth_504d_jerk_v009_signal,
    f31hg_f31_hypergrowth_signature_rndlead_252d_jerk_v010_signal,
    f31hg_f31_hypergrowth_signature_durable_252d_jerk_v011_signal,
    f31hg_f31_hypergrowth_signature_grthquality_252d_jerk_v012_signal,
    f31hg_f31_hypergrowth_signature_gpgrowth_252d_jerk_v013_signal,
    f31hg_f31_hypergrowth_signature_gpvsrev_252d_jerk_v014_signal,
    f31hg_f31_hypergrowth_signature_grthmarginz_252d_jerk_v015_signal,
    f31hg_f31_hypergrowth_signature_triple_252d_jerk_v016_signal,
    f31hg_f31_hypergrowth_signature_triad_252d_jerk_v017_signal,
    f31hg_f31_hypergrowth_signature_stabmargin_252d_jerk_v018_signal,
    f31hg_f31_hypergrowth_signature_rule40stab_252d_jerk_v019_signal,
    f31hg_f31_hypergrowth_signature_grthmargmom_252d_jerk_v020_signal,
    f31hg_f31_hypergrowth_signature_reinveff_252d_jerk_v021_signal,
    f31hg_f31_hypergrowth_signature_cashreinv_252d_jerk_v022_signal,
    f31hg_f31_hypergrowth_signature_marginreinv_252d_jerk_v023_signal,
    f31hg_f31_hypergrowth_signature_dualmargexp_504d_jerk_v024_signal,
    f31hg_f31_hypergrowth_signature_ocfgrowth_252d_jerk_v025_signal,
    f31hg_f31_hypergrowth_signature_weaklink_252d_jerk_v026_signal,
    f31hg_f31_hypergrowth_signature_selfffund_252d_jerk_v027_signal,
    f31hg_f31_hypergrowth_signature_rule40mom_504d_jerk_v028_signal,
    f31hg_f31_hypergrowth_signature_accelmargin_126d_jerk_v029_signal,
    f31hg_f31_hypergrowth_signature_growthgate_252d_jerk_v030_signal,
    f31hg_f31_hypergrowth_signature_cashgate_252d_jerk_v031_signal,
    f31hg_f31_hypergrowth_signature_aligned_252d_jerk_v032_signal,
    f31hg_f31_hypergrowth_signature_rule40gp_252d_jerk_v033_signal,
    f31hg_f31_hypergrowth_signature_rampinvest_252d_jerk_v034_signal,
    f31hg_f31_hypergrowth_signature_qualbalance_252d_jerk_v035_signal,
    f31hg_f31_hypergrowth_signature_grthmargema_252d_jerk_v036_signal,
    f31hg_f31_hypergrowth_signature_rule40ema_252d_jerk_v037_signal,
    f31hg_f31_hypergrowth_signature_grthrndlev_252d_jerk_v038_signal,
    f31hg_f31_hypergrowth_signature_harmonic_252d_jerk_v039_signal,
    f31hg_f31_hypergrowth_signature_relgrth_252d_jerk_v040_signal,
    f31hg_f31_hypergrowth_signature_relreinv_252d_jerk_v041_signal,
    f31hg_f31_hypergrowth_signature_relrule40_252d_jerk_v042_signal,
    f31hg_f31_hypergrowth_signature_convexity_252d_jerk_v043_signal,
    f31hg_f31_hypergrowth_signature_runway_252d_jerk_v044_signal,
    f31hg_f31_hypergrowth_signature_marggated_252d_jerk_v045_signal,
    f31hg_f31_hypergrowth_signature_compound_252d_jerk_v046_signal,
    f31hg_f31_hypergrowth_signature_snr_252d_jerk_v047_signal,
    f31hg_f31_hypergrowth_signature_rampdefend_252d_jerk_v048_signal,
    f31hg_f31_hypergrowth_signature_blend_252d_jerk_v049_signal,
    f31hg_f31_hypergrowth_signature_gpcash_252d_jerk_v050_signal,
    f31hg_f31_hypergrowth_signature_profscale_252d_jerk_v051_signal,
    f31hg_f31_hypergrowth_signature_smoothgrow_252d_jerk_v052_signal,
    f31hg_f31_hypergrowth_signature_rule40fuel_252d_jerk_v053_signal,
    f31hg_f31_hypergrowth_signature_yoyaccel_252d_jerk_v054_signal,
    f31hg_f31_hypergrowth_signature_reinvcash_252d_jerk_v055_signal,
    f31hg_f31_hypergrowth_signature_marggrowthrank_252d_jerk_v056_signal,
    f31hg_f31_hypergrowth_signature_geodur_252d_jerk_v057_signal,
    f31hg_f31_hypergrowth_signature_cashtraj_252d_jerk_v058_signal,
    f31hg_f31_hypergrowth_signature_rndprofit_252d_jerk_v059_signal,
    f31hg_f31_hypergrowth_signature_netsig_252d_jerk_v060_signal,
    f31hg_f31_hypergrowth_signature_cashmargexp_252d_jerk_v061_signal,
    f31hg_f31_hypergrowth_signature_tripalign_252d_jerk_v062_signal,
    f31hg_f31_hypergrowth_signature_r40net_252d_jerk_v063_signal,
    f31hg_f31_hypergrowth_signature_gmrotate_252d_jerk_v064_signal,
    f31hg_f31_hypergrowth_signature_qualstack_252d_jerk_v065_signal,
    f31hg_f31_hypergrowth_signature_reinvdur_252d_jerk_v066_signal,
    f31hg_f31_hypergrowth_signature_integscore_252d_jerk_v067_signal,
    f31hg_f31_hypergrowth_signature_seqgrth_63d_jerk_v068_signal,
    f31hg_f31_hypergrowth_signature_seqgpgrth_63d_jerk_v069_signal,
    f31hg_f31_hypergrowth_signature_cagrmargin_504d_jerk_v070_signal,
    f31hg_f31_hypergrowth_signature_cagrrule40_504d_jerk_v071_signal,
    f31hg_f31_hypergrowth_signature_reaccel_252d_jerk_v072_signal,
    f31hg_f31_hypergrowth_signature_reinvaccel_252d_jerk_v073_signal,
    f31hg_f31_hypergrowth_signature_margslope_126d_jerk_v074_signal,
    f31hg_f31_hypergrowth_signature_consistgm_252d_jerk_v075_signal,
    f31hg_f31_hypergrowth_signature_r40consist_252d_jerk_v076_signal,
    f31hg_f31_hypergrowth_signature_gmhit_252d_jerk_v077_signal,
    f31hg_f31_hypergrowth_signature_reinvhit_252d_jerk_v078_signal,
    f31hg_f31_hypergrowth_signature_grthasym_252d_jerk_v079_signal,
    f31hg_f31_hypergrowth_signature_cashasym_252d_jerk_v080_signal,
    f31hg_f31_hypergrowth_signature_triadrank_252d_jerk_v081_signal,
    f31hg_f31_hypergrowth_signature_r40rank_252d_jerk_v082_signal,
    f31hg_f31_hypergrowth_signature_effreinv_252d_jerk_v083_signal,
    f31hg_f31_hypergrowth_signature_logscore_252d_jerk_v084_signal,
    f31hg_f31_hypergrowth_signature_gqmom_252d_jerk_v085_signal,
    f31hg_f31_hypergrowth_signature_reinvmom_252d_jerk_v086_signal,
    f31hg_f31_hypergrowth_signature_margdefend_252d_jerk_v087_signal,
    f31hg_f31_hypergrowth_signature_r40defend_252d_jerk_v088_signal,
    f31hg_f31_hypergrowth_signature_selfgrow_252d_jerk_v089_signal,
    f31hg_f31_hypergrowth_signature_fcfreinv_252d_jerk_v090_signal,
    f31hg_f31_hypergrowth_signature_qualfunded_252d_jerk_v091_signal,
    f31hg_f31_hypergrowth_signature_minall_252d_jerk_v092_signal,
    f31hg_f31_hypergrowth_signature_gmcross_252d_jerk_v093_signal,
    f31hg_f31_hypergrowth_signature_r40cross_252d_jerk_v094_signal,
    f31hg_f31_hypergrowth_signature_margconvex_252d_jerk_v095_signal,
    f31hg_f31_hypergrowth_signature_zreinv_252d_jerk_v096_signal,
    f31hg_f31_hypergrowth_signature_zcashmarg_252d_jerk_v097_signal,
    f31hg_f31_hypergrowth_signature_triplez_252d_jerk_v098_signal,
    f31hg_f31_hypergrowth_signature_rndprod_252d_jerk_v099_signal,
    f31hg_f31_hypergrowth_signature_salesprod_252d_jerk_v100_signal,
    f31hg_f31_hypergrowth_signature_gmrankema_252d_jerk_v101_signal,
    f31hg_f31_hypergrowth_signature_r40netrank_252d_jerk_v102_signal,
    f31hg_f31_hypergrowth_signature_comprove_252d_jerk_v103_signal,
    f31hg_f31_hypergrowth_signature_ccstab_252d_jerk_v104_signal,
    f31hg_f31_hypergrowth_signature_organic_252d_jerk_v105_signal,
    f31hg_f31_hypergrowth_signature_reinvimp_252d_jerk_v106_signal,
    f31hg_f31_hypergrowth_signature_growstreak_252d_jerk_v107_signal,
    f31hg_f31_hypergrowth_signature_cashstreak_252d_jerk_v108_signal,
    f31hg_f31_hypergrowth_signature_fundedaccel_252d_jerk_v109_signal,
    f31hg_f31_hypergrowth_signature_gpdollar_252d_jerk_v110_signal,
    f31hg_f31_hypergrowth_signature_r40margin_252d_jerk_v111_signal,
    f31hg_f31_hypergrowth_signature_marglev_252d_jerk_v112_signal,
    f31hg_f31_hypergrowth_signature_growperreinv_252d_jerk_v113_signal,
    f31hg_f31_hypergrowth_signature_twinmargin_252d_jerk_v114_signal,
    f31hg_f31_hypergrowth_signature_gmsharpe_252d_jerk_v115_signal,
    f31hg_f31_hypergrowth_signature_triadmin_252d_jerk_v116_signal,
    f31hg_f31_hypergrowth_signature_cashposgrow_252d_jerk_v117_signal,
    f31hg_f31_hypergrowth_signature_investmargin_252d_jerk_v118_signal,
    f31hg_f31_hypergrowth_signature_longdur_504d_jerk_v119_signal,
    f31hg_f31_hypergrowth_signature_gmyoy_252d_jerk_v120_signal,
    f31hg_f31_hypergrowth_signature_r40resil_252d_jerk_v121_signal,
    f31hg_f31_hypergrowth_signature_hmgrow_252d_jerk_v122_signal,
    f31hg_f31_hypergrowth_signature_cleanfunded_252d_jerk_v123_signal,
    f31hg_f31_hypergrowth_signature_cashefficient_252d_jerk_v124_signal,
    f31hg_f31_hypergrowth_signature_gpreinvrank_252d_jerk_v125_signal,
    f31hg_f31_hypergrowth_signature_triadslope_126d_jerk_v126_signal,
    f31hg_f31_hypergrowth_signature_smoothcash_252d_jerk_v127_signal,
    f31hg_f31_hypergrowth_signature_twinexp_252d_jerk_v128_signal,
    f31hg_f31_hypergrowth_signature_discipline_252d_jerk_v129_signal,
    f31hg_f31_hypergrowth_signature_twingrow_252d_jerk_v130_signal,
    f31hg_f31_hypergrowth_signature_qualreinv_252d_jerk_v131_signal,
    f31hg_f31_hypergrowth_signature_leangrow_252d_jerk_v132_signal,
    f31hg_f31_hypergrowth_signature_cleansurp_252d_jerk_v133_signal,
    f31hg_f31_hypergrowth_signature_consensus_252d_jerk_v134_signal,
    f31hg_f31_hypergrowth_signature_cashfundsrnd_252d_jerk_v135_signal,
    f31hg_f31_hypergrowth_signature_durscore_252d_jerk_v136_signal,
    f31hg_f31_hypergrowth_signature_ccvalid_252d_jerk_v137_signal,
    f31hg_f31_hypergrowth_signature_integfull_252d_jerk_v138_signal,
    f31hg_f31_hypergrowth_signature_grthccdev_252d_jerk_v139_signal,
    f31hg_f31_hypergrowth_signature_margreindev_252d_jerk_v140_signal,
    f31hg_f31_hypergrowth_signature_cagrseq_504d_jerk_v141_signal,
    f31hg_f31_hypergrowth_signature_selffundgr_252d_jerk_v142_signal,
    f31hg_f31_hypergrowth_signature_grthzmarg_252d_jerk_v143_signal,
    f31hg_f31_hypergrowth_signature_reinvfundrank_252d_jerk_v144_signal,
    f31hg_f31_hypergrowth_signature_gpomdev_252d_jerk_v145_signal,
    f31hg_f31_hypergrowth_signature_gmgated_252d_jerk_v146_signal,
    f31hg_f31_hypergrowth_signature_ritrendgr_252d_jerk_v147_signal,
    f31hg_f31_hypergrowth_signature_margtrajcash_252d_jerk_v148_signal,
    f31hg_f31_hypergrowth_signature_grthrepexp_252d_jerk_v149_signal,
    f31hg_f31_hypergrowth_signature_zfull_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_HYPERGROWTH_SIGNATURE_REGISTRY_JERK_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f31_hypergrowth_signature_3rd_derivatives_001_150_claude: %d features pass" % n_features)
