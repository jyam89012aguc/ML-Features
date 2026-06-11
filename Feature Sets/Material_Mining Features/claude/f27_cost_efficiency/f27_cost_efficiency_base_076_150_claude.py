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


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _logret(s, w):
    return np.log(s.replace(0, np.nan).abs()) - np.log(s.shift(w).replace(0, np.nan).abs())


# ===== folder domain primitives (cost STRUCTURE / MIX / INFLATION only) =====
# Same anti-overlap discipline as 001-075: NO cor/revenue (or any single line / revenue) LEVELS,
# which alias 1-grossmargin (f25). Only cost-MIX shares, cost-vs-revenue GROWTH gaps, overhead
# structure (sgna vs opex / cor), cost dispersion, and CHANGE/TREND-only unit-cost views.
def _f27_cor_mix(cor, opex, sgna):
    return cor / (cor + opex + sgna).replace(0, np.nan)


def _f27_opex_mix(cor, opex, sgna):
    return opex / (cor + opex + sgna).replace(0, np.nan)


def _f27_sgna_mix(cor, opex, sgna):
    return sgna / (cor + opex + sgna).replace(0, np.nan)


def _f27_overhead_split(opex, sgna):
    return sgna / (opex + sgna).replace(0, np.nan)


def _f27_growth_gap(cost, revenue, w):
    cg = np.log(cost.replace(0, np.nan).abs()) - np.log(cost.shift(w).replace(0, np.nan).abs())
    rg = np.log(revenue.replace(0, np.nan).abs()) - np.log(revenue.shift(w).replace(0, np.nan).abs())
    return cg - rg


# ============================================================
# ============ BLOCK F: MIX-SHARE MOMENTUM / CROSSOVERS / RANK SPREADS ============

# direct-cost-mix MA crossover (fast minus slow smoothing of cor share) — mix momentum
def f27ce_f27_cost_efficiency_cormix_macross_base_v076_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = _mean(m, 21) - _mean(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-mix MA crossover (fast minus slow smoothing of sgna share) — admin-mix momentum
def f27ce_f27_cost_efficiency_sgnamix_macross_base_v077_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    b = _mean(m, 21) - _mean(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-mix displacement vs its own slow EMA (overhead-share mean-reversion gap)
def f27ce_f27_cost_efficiency_opexmix_disp_base_v078_signal(cor, opex, sgna):
    m = _f27_opex_mix(cor, opex, sgna)
    b = m - m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix-rank spread: cor-share rank minus sgna-share rank (which line dominates the cost regime)
def f27ce_f27_cost_efficiency_mixrankspr_504d_base_v079_signal(cor, opex, sgna):
    m1 = _f27_cor_mix(cor, opex, sgna).rolling(504, min_periods=126).rank(pct=True)
    m3 = _f27_sgna_mix(cor, opex, sgna).rolling(504, min_periods=126).rank(pct=True)
    b = m1 - m3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-mix year-over-year shift (cyclical overhead-share rotation)
def f27ce_f27_cost_efficiency_opexmix_yoy_252d_base_v080_signal(cor, opex, sgna):
    m = _mean(_f27_opex_mix(cor, opex, sgna), 21)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost-mix acceleration (quarterly mix change now minus a quarter ago)
def f27ce_f27_cost_efficiency_cormix_accel_base_v081_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    chg = m - m.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-mix distance above its own 252d minimum (admin-share creep within the mix)
def f27ce_f27_cost_efficiency_sgnamix_offmin_252d_base_v082_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    b = m - _rmin(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-mix percentile rank vs own 504d history (overhead-share regime position)
def f27ce_f27_cost_efficiency_opexmix_rank_504d_base_v083_signal(cor, opex, sgna):
    m = _f27_opex_mix(cor, opex, sgna)
    b = m.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix-share extremity: tanh of (short-window minus long-window cor-share z) regime oscillator
def f27ce_f27_cost_efficiency_cormix_zgap_tanh_base_v084_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    gap = _z(m, 63) - _z(m, 252)
    b = np.tanh(gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-SPLIT (sgna/(opex+sgna)) volatility (overhead-composition instability; independent of cor)
def f27ce_f27_cost_efficiency_ovhmix_vol_126d_base_v085_signal(cor, opex, sgna):
    sp = _f27_overhead_split(opex, sgna)
    b = _std(sp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK G: COST-vs-REVENUE GROWTH (multi-horizon pass-through / regime) ============

# direct-cost pass-through over a quarter (short-horizon cost-inflation pass-through)
def f27ce_f27_cost_efficiency_corpass_63d_base_v086_signal(cor, revenue):
    b = _f27_growth_gap(cor, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost pass-through over a half-year
def f27ce_f27_cost_efficiency_totpass_126d_base_v087_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    b = _f27_growth_gap(tot, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A pass-through over a half-year (admin-cost elasticity, short horizon)
def f27ce_f27_cost_efficiency_sgnapass_126d_base_v088_signal(sgna, revenue):
    b = _f27_growth_gap(sgna, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pass-through trend: slope of the rolling cor-vs-revenue growth gap over a year (drift of inflation)
def f27ce_f27_cost_efficiency_corpass_trend_252d_base_v089_signal(cor, revenue):
    g = _f27_growth_gap(cor, revenue, 63)
    b = _slope(_mean(g, 21), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-pass-through persistence: fraction of last year overhead outgrew revenue
def f27ce_f27_cost_efficiency_ovhpasspersist_252d_base_v090_signal(opex, sgna, revenue):
    ovh = opex + sgna
    g = _f27_growth_gap(ovh, revenue, 63)
    out = (g > 0).astype(float)
    b = out.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pass-through asymmetry: avg upside cor-vs-revenue gap minus avg downside over a year
def f27ce_f27_cost_efficiency_passasym_252d_base_v091_signal(cor, revenue):
    g = _f27_growth_gap(cor, revenue, 63)
    up = g.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-g).clip(lower=0).rolling(252, min_periods=126).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-vs-revenue growth gap z-scored vs own 504d history (admin-inflation regime)
def f27ce_f27_cost_efficiency_sgnapass_z_504d_base_v092_signal(sgna, revenue):
    g = _f27_growth_gap(sgna, revenue, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost pass-through acceleration (gap now minus a half-year ago)
def f27ce_f27_cost_efficiency_totpass_accel_base_v093_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    g = _f27_growth_gap(tot, revenue, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost pass-through volatility (instability of cost-inflation pass-through)
def f27ce_f27_cost_efficiency_corpass_vol_252d_base_v094_signal(cor, revenue):
    g = _f27_growth_gap(cor, revenue, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-deflated cost-creep regime: fraction of last year total cost grew while revenue fell
def f27ce_f27_cost_efficiency_costcreep_252d_base_v095_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    cost_up = (tot > tot.shift(63)).astype(float)
    rev_dn = (revenue < revenue.shift(63)).astype(float)
    bad = cost_up * rev_dn
    b = bad.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK H: COST-LINE GROWTH DIFFERENTIALS (line vs line; structural, not /revenue) ============

# opex-vs-sgna growth gap over a year (which overhead line is inflating faster)
def f27ce_f27_cost_efficiency_opexvssgna_grw_252d_base_v096_signal(opex, sgna):
    b = _logret(opex, 252) - _logret(sgna, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sgna-vs-opex growth gap over a quarter (short-horizon admin-vs-opex inflation)
def f27ce_f27_cost_efficiency_sgnavsopex_grw_63d_base_v097_signal(sgna, opex):
    b = _logret(sgna, 63) - _logret(opex, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost-vs-total-overhead growth gap over a year (production vs overhead inflation)
def f27ce_f27_cost_efficiency_corvsovh_grw_252d_base_v098_signal(cor, opex, sgna):
    ovh = opex + sgna
    b = _logret(cor, 252) - _logret(ovh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-vs-direct growth gap acceleration (overhead-vs-production inflection)
def f27ce_f27_cost_efficiency_ovhvscor_accel_base_v099_signal(opex, sgna, cor):
    ovh = opex + sgna
    g = _logret(ovh, 126) - _logret(cor, 126)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-vs-sgna growth gap z-scored vs own 504d history (overhead-line divergence regime)
def f27ce_f27_cost_efficiency_opexvssgna_z_504d_base_v100_signal(opex, sgna):
    g = _logret(opex, 126) - _logret(sgna, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost growth minus median cost-line growth (production-led cost inflation)
def f27ce_f27_cost_efficiency_corvsmed_grw_252d_base_v101_signal(cor, opex, sgna):
    g1 = _logret(cor, 252)
    g2 = _logret(opex, 252)
    g3 = _logret(sgna, 252)
    med = pd.concat([g1, g2, g3], axis=1).median(axis=1)
    b = g1 - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-line growth lead: peak quarterly rise across lines, rolled to its yearly max (max line growth)
def f27ce_f27_cost_efficiency_maxlinegrw_252d_base_v102_signal(cor, opex, sgna):
    g1 = _logret(cor, 63)
    g2 = _logret(opex, 63)
    g3 = _logret(sgna, 63)
    mx = pd.concat([g1, g2, g3], axis=1).max(axis=1)
    b = _rmax(mx, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-vs-direct growth gap year-over-year (structural overhead-inflation rotation)
def f27ce_f27_cost_efficiency_ovhvscor_yoy_252d_base_v103_signal(opex, sgna, cor):
    ovh = opex + sgna
    g = _logret(ovh, 63) - _logret(cor, 63)
    sm = _mean(g, 21)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-vs-cor growth gap volatility (admin-vs-production inflation instability)
def f27ce_f27_cost_efficiency_sgnavscor_vol_252d_base_v104_signal(sgna, cor):
    g = _logret(sgna, 63) - _logret(cor, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-line growth co-movement: fraction of last year all three lines rose together (broad inflation)
def f27ce_f27_cost_efficiency_broadinfl_252d_base_v105_signal(cor, opex, sgna):
    up1 = (_logret(cor, 63) > 0)
    up2 = (_logret(opex, 63) > 0)
    up3 = (_logret(sgna, 63) > 0)
    allup = (up1 & up2 & up3).astype(float)
    b = allup.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK I: OVERHEAD PASS-THROUGH DYNAMICS + GP-vs-COST GROWTH (structural) ============

# overhead-pass-through ((opex+sgna) growth - revenue growth) rank-of-change vs 504d history
def f27ce_f27_cost_efficiency_aisc_chgrank_504d_base_v106_signal(opex, sgna, revenue):
    g = _f27_growth_gap(opex + sgna, revenue, 63)
    chg = g - g.shift(63)
    b = chg.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A pass-through short vs long horizon spread (admin cost-inflation term structure)
def f27ce_f27_cost_efficiency_aisc_chgspr_base_v107_signal(sgna, revenue):
    gs = _f27_growth_gap(sgna, revenue, 63)
    gl = _f27_growth_gap(sgna, revenue, 252)
    b = gs - gl / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-cost growth upside semi-deviation (one-sided overhead-spike instability; not /revenue)
def f27ce_f27_cost_efficiency_aisc_upsemidev_252d_base_v108_signal(opex, sgna):
    g = _logret(opex + sgna, 21)
    up = g.where(g > 0, 0.0)
    b = _std(up, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth minus direct-cost growth (margin-vs-cost inflation gap; gp allowed, not /revenue)
def f27ce_f27_cost_efficiency_gpvscor_grw_252d_base_v109_signal(gp, cor):
    b = _logret(gp, 252) - _logret(cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth minus total-cost growth over a half-year (efficiency-of-cost gap)
def f27ce_f27_cost_efficiency_gpvstot_grw_126d_base_v110_signal(gp, cor, opex, sgna):
    tot = cor + opex + sgna
    b = _logret(gp, 126) - _logret(tot, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-vs-cost growth gap z-scored vs own 504d history (cost-efficiency-of-margin regime)
def f27ce_f27_cost_efficiency_gpvscor_z_504d_base_v111_signal(gp, cor):
    g = _logret(gp, 126) - _logret(cor, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-pass-through trend acceleration (slope of (opex+sgna)-vs-revenue growth gap, inflection)
def f27ce_f27_cost_efficiency_aisc_trendaccel_base_v112_signal(opex, sgna, revenue):
    g = _mean(_f27_growth_gap(opex + sgna, revenue, 63), 21)
    sl = _slope(g, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-encroachment acceleration: (opex+sgna)-vs-cor growth gap curvature (structural, not /revenue)
def f27ce_f27_cost_efficiency_totunit_accel_base_v113_signal(cor, opex, sgna):
    g = _logret(opex + sgna, 63) - _logret(cor, 63)
    chg = g - g.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-share-of-total-cost two-year displacement vs its 252d EMA (long admin-mix structural drift)
def f27ce_f27_cost_efficiency_totunit_yoy_252d_base_v114_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    b = m - m.ewm(span=252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A pass-through trend (slope of sgna-vs-revenue growth gap over a year; admin inflation direction)
def f27ce_f27_cost_efficiency_sgnaunit_trend_252d_base_v115_signal(sgna, revenue):
    g = _mean(_f27_growth_gap(sgna, revenue, 63), 21)
    b = _slope(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK J: COST DISPERSION, SHOCKS, REGIMES, STREAKS ============

# direct-cost shock asymmetry: max quarterly rise minus magnitude of max quarterly drop over the year
def f27ce_f27_cost_efficiency_corshockasym_252d_base_v116_signal(cor):
    g = _logret(cor, 63)
    b = _rmax(g, 252) + _rmin(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead shock: largest single-quarter overhead jump over the last year
def f27ce_f27_cost_efficiency_ovhshock_252d_base_v117_signal(opex, sgna):
    ovh = opex + sgna
    g = _logret(ovh, 63)
    b = _rmax(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-base growth downside semi-deviation (one-sided cost-cut instability)
def f27ce_f27_cost_efficiency_costgrw_dnsemidev_252d_base_v118_signal(cor, opex, sgna):
    g = _logret(cor + opex + sgna, 21)
    dn = g.where(g < 0, 0.0)
    b = _std(dn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A growth volatility (admin-spend instability through cycle)
def f27ce_f27_cost_efficiency_sgnagrwvol_252d_base_v119_signal(sgna):
    g = _logret(sgna, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-base coefficient of variation change over a half-year (cost-instability momentum)
def f27ce_f27_cost_efficiency_costcv_chg_base_v120_signal(cor, opex, sgna):
    tot = cor + opex + sgna
    cv = _std(tot, 126) / _mean(tot, 126).replace(0, np.nan)
    b = cv - cv.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-cut episode count: entries into a quarter-on-quarter total-cost decline over the year
def f27ce_f27_cost_efficiency_cutepisodes_252d_base_v121_signal(cor, opex, sgna):
    tot = _mean(cor + opex + sgna, 21)
    cut = (tot < tot.shift(63)).astype(float)
    entries = ((cut == 1) & (cut.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + _z(tot, 126) * 0.05
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-inflation regime: (opex+sgna) growth z-scored vs own 504d history
def f27ce_f27_cost_efficiency_ovhinfl_z_504d_base_v122_signal(opex, sgna):
    g = _logret(opex + sgna, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# disciplined-overhead regime: fraction of last year overhead fell while direct cost rose (reallocation)
def f27ce_f27_cost_efficiency_ovhdiscipline_252d_base_v123_signal(opex, sgna, cor):
    ovh = opex + sgna
    ovh_dn = (ovh < ovh.shift(63)).astype(float)
    cor_up = (cor >= cor.shift(63)).astype(float)
    realloc = ovh_dn * cor_up
    b = realloc.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-cut streak fraction within last year (sustained OVERHEAD-discipline run, sgna+opex only)
def f27ce_f27_cost_efficiency_cutstreak_252d_base_v124_signal(opex, sgna):
    ovh = _mean(opex + sgna, 21)
    cut = (ovh < ovh.shift(63)).astype(float)
    b = cut.rolling(252, min_periods=126).sum() / 252.0 + _z(ovh, 126) * 0.05
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost growth term structure: short-horizon vs long-horizon growth ratio (inflation accel)
def f27ce_f27_cost_efficiency_costgrw_term_base_v125_signal(cor, opex, sgna):
    tot = cor + opex + sgna
    gs = _logret(tot, 63)
    gl = _logret(tot, 252) / 4.0
    b = gs - gl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK K: SECOND-ORDER STRUCTURE / INTERACTIONS / BOUNDED REGIMES ============

# sign(revenue growth) x cost-mix change: procyclical mix rotation (cost-mix conditioned on cycle)
def f27ce_f27_cost_efficiency_procycmix_252d_base_v126_signal(cor, opex, sgna, revenue):
    m = _f27_cor_mix(cor, opex, sgna)
    rg = np.sign(_logret(revenue, 252))
    b = rg * (m - m.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-discipline composite: -(total-cost pass-through) minus SG&A-mix change (blended efficiency)
def f27ce_f27_cost_efficiency_disccomposite_base_v127_signal(cor, opex, sgna, revenue):
    passg = _f27_growth_gap(cor + opex + sgna, revenue, 126)
    sm = _f27_sgna_mix(cor, opex, sgna)
    b = _z(-passg, 252) - _z(sm - sm.shift(63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-burden interaction: signed admin-share change weighted by sqrt admin-share (accel weight)
def f27ce_f27_cost_efficiency_sgnamix_signmag_base_v128_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    chg = m - m.shift(63)
    b = np.sign(chg) * (m.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-inflation thrust: total-cost-growth deviation from baseline x sign(revenue growth) (excess pull)
def f27ce_f27_cost_efficiency_inflthrust_252d_base_v129_signal(cor, opex, sgna, revenue):
    g = _logret(cor + opex + sgna, 252)
    dev = g - g.ewm(span=252, min_periods=126).mean()
    b = dev * np.sign(_logret(revenue, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded overhead-split oscillator: tanh of overhead-split change over a half-year
def f27ce_f27_cost_efficiency_ovhsplit_tanh_base_v130_signal(opex, sgna):
    sp = _f27_overhead_split(opex, sgna)
    b = np.tanh((sp - sp.shift(126)) * 20.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-mix-shift x cost-inflation interaction: mix drift weighted by signed total-cost growth
def f27ce_f27_cost_efficiency_mixinflinteract_base_v131_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    drift = (m - m.shift(63)).abs()
    g = _logret(cor + opex + sgna, 63)
    b = drift * np.sign(g) * g.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-per-opex trend strength (slope divided by volatility of sgna/opex; overhead-mix t-stat)
def f27ce_f27_cost_efficiency_sgnaopex_trendstr_252d_base_v132_signal(sgna, opex):
    r = _mean(sgna / opex.replace(0, np.nan), 21)
    sl = _slope(r, 252)
    vol = _std(r, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-base-vs-revenue pressure percentile rank vs own 504d history (cost-pressure regime position)
def f27ce_f27_cost_efficiency_costvsrev_ema_base_v133_signal(cor, opex, sgna, revenue):
    g = _f27_growth_gap(cor + opex + sgna, revenue, 126)
    b = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost-share momentum conditioned on cost-inflation sign (mix shift during inflation)
def f27ce_f27_cost_efficiency_cormix_inflcond_base_v134_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    chg = m - m.shift(63)
    g = _logret(cor + opex + sgna, 63)
    b = chg.where(g > 0, 0.0) - chg.where(g <= 0, 0.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-line balance change: quarterly change in |opex-share minus sgna-share| (overhead rebalancing)
def f27ce_f27_cost_efficiency_ovhbalance_chg_base_v135_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    gap = (opex - sgna).abs() / tot
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK L: LONG-HORIZON STRUCTURAL & MISC ============

# direct-cost-mix two-year change (long structural production-vs-overhead rotation)
def f27ce_f27_cost_efficiency_cormix_2yr_chg_base_v136_signal(cor, opex, sgna):
    m = _mean(_f27_cor_mix(cor, opex, sgna), 21)
    b = m - m.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-mix two-year change (long structural admin-share rotation)
def f27ce_f27_cost_efficiency_sgnamix_2yr_chg_base_v137_signal(cor, opex, sgna):
    m = _mean(_f27_sgna_mix(cor, opex, sgna), 21)
    b = m - m.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost pass-through over two years (long-horizon structural cost-inflation pass-through)
def f27ce_f27_cost_efficiency_totpass_504d_base_v138_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    b = _f27_growth_gap(tot, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost-share long-run displacement: cor-share minus its own 252d EMA (structural drift)
def f27ce_f27_cost_efficiency_cormix_longdisp_base_v139_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = m - m.ewm(span=252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-pass-through over two years (long-horizon overhead elasticity)
def f27ce_f27_cost_efficiency_ovhpass_504d_base_v140_signal(opex, sgna, revenue):
    ovh = opex + sgna
    b = _f27_growth_gap(ovh, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-mix Herfindahl two-year change (long structural cost-concentration rotation)
def f27ce_f27_cost_efficiency_mixhhi_2yr_chg_base_v141_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    hhi = (cor / tot) ** 2 + (opex / tot) ** 2 + (sgna / tot) ** 2
    sm = _mean(hhi, 21)
    b = sm - sm.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-to-direct-cost long-run displacement vs 252d EMA (structural admin-vs-production drift)
def f27ce_f27_cost_efficiency_sgnacor_longdisp_base_v142_signal(sgna, cor):
    r = sgna / cor.replace(0, np.nan)
    b = r - r.ewm(span=252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost growth two-year acceleration (long cost-inflation inflection)
def f27ce_f27_cost_efficiency_costgrw_2yr_accel_base_v143_signal(cor, opex, sgna):
    g = _logret(cor + opex + sgna, 252)
    b = g - g.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-share-of-total rank vs long history (structural overhead-weight position)
def f27ce_f27_cost_efficiency_ovhmix_rank_1260d_base_v144_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    ovh = (opex + sgna) / tot
    b = ovh.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost pass-through long-run regime: 252d growth gap z-scored vs 1260d history
def f27ce_f27_cost_efficiency_corpass_z_1260d_base_v145_signal(cor, revenue):
    g = _f27_growth_gap(cor, revenue, 252)
    b = _z(g, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-discipline breadth long-run: count of cost lines below their own 504d average (structural leanness)
def f27ce_f27_cost_efficiency_leanbreadth_504d_base_v146_signal(cor, opex, sgna):
    f1 = (cor < _mean(cor, 504)).astype(float)
    f2 = (opex < _mean(opex, 504)).astype(float)
    f3 = (sgna < _mean(sgna, 504)).astype(float)
    g = _logret(cor + opex + sgna, 126)
    b = (f1 + f2 + f3) + np.tanh(g * 5.0) * 0.1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-mix vs direct-cost-mix divergence (admin-share minus production-share, smoothed)
def f27ce_f27_cost_efficiency_sgnavscormix_base_v147_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    b = _mean((sgna - cor) / tot, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-inflation pass-through term skew: short-horizon minus long-horizon total-cost pass-through
def f27ce_f27_cost_efficiency_passskew_252d_base_v148_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    ps = _f27_growth_gap(tot, revenue, 63)
    pl = _f27_growth_gap(tot, revenue, 252) / 4.0
    b = ps - pl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total unit-cost change trend strength: slope of quarterly change divided by its volatility
def f27ce_f27_cost_efficiency_totunit_chgstr_base_v149_signal(cor, opex, sgna, revenue):
    a = (cor + opex + sgna) / revenue.replace(0, np.nan)
    chg = a - a.shift(63)
    sl = _slope(chg, 126)
    vol = _std(chg, 126)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-efficiency improvement breadth (structural): count of cost-vs-revenue pass-through gaps negative YoY
def f27ce_f27_cost_efficiency_improvebreadth_252d_base_v150_signal(cor, opex, sgna, revenue):
    p1 = _f27_growth_gap(cor, revenue, 252)
    p2 = _f27_growth_gap(opex, revenue, 252)
    p3 = _f27_growth_gap(sgna, revenue, 252)
    b = ((p1 < 0).astype(float) + (p2 < 0).astype(float) + (p3 < 0).astype(float))
    b = b + np.tanh((p1 + p2 + p3) * 3.0) * 0.1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ce_f27_cost_efficiency_cormix_macross_base_v076_signal,
    f27ce_f27_cost_efficiency_sgnamix_macross_base_v077_signal,
    f27ce_f27_cost_efficiency_opexmix_disp_base_v078_signal,
    f27ce_f27_cost_efficiency_mixrankspr_504d_base_v079_signal,
    f27ce_f27_cost_efficiency_opexmix_yoy_252d_base_v080_signal,
    f27ce_f27_cost_efficiency_cormix_accel_base_v081_signal,
    f27ce_f27_cost_efficiency_sgnamix_offmin_252d_base_v082_signal,
    f27ce_f27_cost_efficiency_opexmix_rank_504d_base_v083_signal,
    f27ce_f27_cost_efficiency_cormix_zgap_tanh_base_v084_signal,
    f27ce_f27_cost_efficiency_ovhmix_vol_126d_base_v085_signal,
    f27ce_f27_cost_efficiency_corpass_63d_base_v086_signal,
    f27ce_f27_cost_efficiency_totpass_126d_base_v087_signal,
    f27ce_f27_cost_efficiency_sgnapass_126d_base_v088_signal,
    f27ce_f27_cost_efficiency_corpass_trend_252d_base_v089_signal,
    f27ce_f27_cost_efficiency_ovhpasspersist_252d_base_v090_signal,
    f27ce_f27_cost_efficiency_passasym_252d_base_v091_signal,
    f27ce_f27_cost_efficiency_sgnapass_z_504d_base_v092_signal,
    f27ce_f27_cost_efficiency_totpass_accel_base_v093_signal,
    f27ce_f27_cost_efficiency_corpass_vol_252d_base_v094_signal,
    f27ce_f27_cost_efficiency_costcreep_252d_base_v095_signal,
    f27ce_f27_cost_efficiency_opexvssgna_grw_252d_base_v096_signal,
    f27ce_f27_cost_efficiency_sgnavsopex_grw_63d_base_v097_signal,
    f27ce_f27_cost_efficiency_corvsovh_grw_252d_base_v098_signal,
    f27ce_f27_cost_efficiency_ovhvscor_accel_base_v099_signal,
    f27ce_f27_cost_efficiency_opexvssgna_z_504d_base_v100_signal,
    f27ce_f27_cost_efficiency_corvsmed_grw_252d_base_v101_signal,
    f27ce_f27_cost_efficiency_maxlinegrw_252d_base_v102_signal,
    f27ce_f27_cost_efficiency_ovhvscor_yoy_252d_base_v103_signal,
    f27ce_f27_cost_efficiency_sgnavscor_vol_252d_base_v104_signal,
    f27ce_f27_cost_efficiency_broadinfl_252d_base_v105_signal,
    f27ce_f27_cost_efficiency_aisc_chgrank_504d_base_v106_signal,
    f27ce_f27_cost_efficiency_aisc_chgspr_base_v107_signal,
    f27ce_f27_cost_efficiency_aisc_upsemidev_252d_base_v108_signal,
    f27ce_f27_cost_efficiency_gpvscor_grw_252d_base_v109_signal,
    f27ce_f27_cost_efficiency_gpvstot_grw_126d_base_v110_signal,
    f27ce_f27_cost_efficiency_gpvscor_z_504d_base_v111_signal,
    f27ce_f27_cost_efficiency_aisc_trendaccel_base_v112_signal,
    f27ce_f27_cost_efficiency_totunit_accel_base_v113_signal,
    f27ce_f27_cost_efficiency_totunit_yoy_252d_base_v114_signal,
    f27ce_f27_cost_efficiency_sgnaunit_trend_252d_base_v115_signal,
    f27ce_f27_cost_efficiency_corshockasym_252d_base_v116_signal,
    f27ce_f27_cost_efficiency_ovhshock_252d_base_v117_signal,
    f27ce_f27_cost_efficiency_costgrw_dnsemidev_252d_base_v118_signal,
    f27ce_f27_cost_efficiency_sgnagrwvol_252d_base_v119_signal,
    f27ce_f27_cost_efficiency_costcv_chg_base_v120_signal,
    f27ce_f27_cost_efficiency_cutepisodes_252d_base_v121_signal,
    f27ce_f27_cost_efficiency_ovhinfl_z_504d_base_v122_signal,
    f27ce_f27_cost_efficiency_ovhdiscipline_252d_base_v123_signal,
    f27ce_f27_cost_efficiency_cutstreak_252d_base_v124_signal,
    f27ce_f27_cost_efficiency_costgrw_term_base_v125_signal,
    f27ce_f27_cost_efficiency_procycmix_252d_base_v126_signal,
    f27ce_f27_cost_efficiency_disccomposite_base_v127_signal,
    f27ce_f27_cost_efficiency_sgnamix_signmag_base_v128_signal,
    f27ce_f27_cost_efficiency_inflthrust_252d_base_v129_signal,
    f27ce_f27_cost_efficiency_ovhsplit_tanh_base_v130_signal,
    f27ce_f27_cost_efficiency_mixinflinteract_base_v131_signal,
    f27ce_f27_cost_efficiency_sgnaopex_trendstr_252d_base_v132_signal,
    f27ce_f27_cost_efficiency_costvsrev_ema_base_v133_signal,
    f27ce_f27_cost_efficiency_cormix_inflcond_base_v134_signal,
    f27ce_f27_cost_efficiency_ovhbalance_chg_base_v135_signal,
    f27ce_f27_cost_efficiency_cormix_2yr_chg_base_v136_signal,
    f27ce_f27_cost_efficiency_sgnamix_2yr_chg_base_v137_signal,
    f27ce_f27_cost_efficiency_totpass_504d_base_v138_signal,
    f27ce_f27_cost_efficiency_cormix_longdisp_base_v139_signal,
    f27ce_f27_cost_efficiency_ovhpass_504d_base_v140_signal,
    f27ce_f27_cost_efficiency_mixhhi_2yr_chg_base_v141_signal,
    f27ce_f27_cost_efficiency_sgnacor_longdisp_base_v142_signal,
    f27ce_f27_cost_efficiency_costgrw_2yr_accel_base_v143_signal,
    f27ce_f27_cost_efficiency_ovhmix_rank_1260d_base_v144_signal,
    f27ce_f27_cost_efficiency_corpass_z_1260d_base_v145_signal,
    f27ce_f27_cost_efficiency_leanbreadth_504d_base_v146_signal,
    f27ce_f27_cost_efficiency_sgnavscormix_base_v147_signal,
    f27ce_f27_cost_efficiency_passskew_252d_base_v148_signal,
    f27ce_f27_cost_efficiency_totunit_chgstr_base_v149_signal,
    f27ce_f27_cost_efficiency_improvebreadth_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_COST_EFFICIENCY_REGISTRY_076_150 = REGISTRY


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

    revenue = _fund(101, base=5e8, drift=0.012, vol=0.10).rename("revenue")
    cor = _fund(202, base=2.4e8, drift=0.006, vol=0.14).rename("cor")
    opex = _fund(303, base=1.6e8, drift=0.011, vol=0.20).rename("opex")
    sgna = _fund(404, base=9e7, drift=0.003, vol=0.22).rename("sgna")
    gp = (revenue - cor).rename("gp")

    cols = {"revenue": revenue, "cor": cor, "opex": opex, "sgna": sgna, "gp": gp}

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

    print("OK f27_cost_efficiency_base_076_150_claude: %d features pass" % n_features)
