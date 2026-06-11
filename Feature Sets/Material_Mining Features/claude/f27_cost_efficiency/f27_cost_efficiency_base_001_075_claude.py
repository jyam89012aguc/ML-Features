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
    # ordinary least squares slope of s over a trailing window
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
# NOTE (anti-overlap with f25 margins): cor/revenue == 1 - grossmargin, an exact affine of
# gross margin. We therefore NEVER use cor/revenue (or any single cost line / revenue) as a
# LEVEL signal. The tightened domain is cost MIX shares (fractions of TOTAL COST, which are
# NOT affine in margin), cost-vs-revenue GROWTH differentials, SG&A/overhead structure, cost
# dispersion, and CHANGE/TREND-only views of unit cost.
def _f27_totcost(cor, opex, sgna):
    return cor + opex + sgna


def _f27_cor_mix(cor, opex, sgna):
    # direct production cost as a fraction of the TOTAL cost base (mix, not margin)
    return cor / (cor + opex + sgna).replace(0, np.nan)


def _f27_opex_mix(cor, opex, sgna):
    return opex / (cor + opex + sgna).replace(0, np.nan)


def _f27_sgna_mix(cor, opex, sgna):
    return sgna / (cor + opex + sgna).replace(0, np.nan)


def _f27_overhead_split(opex, sgna):
    # SG&A weight inside total overhead (opex+sgna): overhead composition tilt
    return sgna / (opex + sgna).replace(0, np.nan)


def _f27_sgna_per_opex(sgna, opex):
    # SG&A relative to operating overhead (structure, not /revenue)
    return sgna / opex.replace(0, np.nan)


def _f27_growth_gap(cost, revenue, w):
    # cost inflation pass-through: log cost growth minus log revenue growth over w
    cg = np.log(cost.replace(0, np.nan).abs()) - np.log(cost.shift(w).replace(0, np.nan).abs())
    rg = np.log(revenue.replace(0, np.nan).abs()) - np.log(revenue.shift(w).replace(0, np.nan).abs())
    return cg - rg


# ============================================================
# ============ BLOCK A: COST-LINE MIX SHARES (of total cost) ============
# These are fractions of (cor+opex+sgna). A mix share is invariant to revenue scale and is
# NOT an affine function of gross margin, so it is structurally orthogonal to f25.

# direct-cost (cor) share of total cost, smoothed (production-vs-overhead mix level)
def f27ce_f27_cost_efficiency_cormix_lvl_63d_base_v001_signal(cor, opex, sgna):
    b = _mean(_f27_cor_mix(cor, opex, sgna), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost mix z-scored vs own 252d history (de-trended production-cost tilt)
def f27ce_f27_cost_efficiency_cormix_z_252d_base_v002_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost mix percentile rank vs own 504d history (mix-regime position)
def f27ce_f27_cost_efficiency_cormix_rank_504d_base_v003_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = m.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost mix change over a quarter (shift toward/away from production cost)
def f27ce_f27_cost_efficiency_cormix_chg_63d_base_v004_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex share of total cost, smoothed (operating-overhead weight in the cost base)
def f27ce_f27_cost_efficiency_opexmix_lvl_63d_base_v005_signal(cor, opex, sgna):
    b = _mean(_f27_opex_mix(cor, opex, sgna), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex share of total cost z-scored vs own 252d history
def f27ce_f27_cost_efficiency_opexmix_z_252d_base_v006_signal(cor, opex, sgna):
    m = _f27_opex_mix(cor, opex, sgna)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex share of total cost change over a quarter (overhead encroaching on the mix)
def f27ce_f27_cost_efficiency_opexmix_chg_63d_base_v007_signal(cor, opex, sgna):
    m = _f27_opex_mix(cor, opex, sgna)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A share of total cost, smoothed (admin weight in the cost base)
def f27ce_f27_cost_efficiency_sgnamix_lvl_63d_base_v008_signal(cor, opex, sgna):
    b = _mean(_f27_sgna_mix(cor, opex, sgna), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A share of total cost z-scored vs own 252d history
def f27ce_f27_cost_efficiency_sgnamix_z_252d_base_v009_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A share of total cost percentile rank vs own 504d history
def f27ce_f27_cost_efficiency_sgnamix_rank_504d_base_v010_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    b = m.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A share of total cost change over a quarter (admin creep into the mix)
def f27ce_f27_cost_efficiency_sgnamix_chg_63d_base_v011_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-balance dispersion: |opex share - sgna share| within total cost (overhead lopsidedness)
def f27ce_f27_cost_efficiency_mixdisp_63d_base_v012_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    gap = (opex - sgna).abs() / tot
    b = _mean(gap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-mix concentration (Herfindahl of the three shares) z-scored vs 252d history
def f27ce_f27_cost_efficiency_mixhhi_z_252d_base_v013_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    hhi = (cor / tot) ** 2 + (opex / tot) ** 2 + (sgna / tot) ** 2
    b = _z(hhi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix-shift magnitude: total absolute quarterly drift across the three cost shares
def f27ce_f27_cost_efficiency_mixshift_63d_base_v014_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    s1 = cor / tot
    s2 = opex / tot
    s3 = sgna / tot
    drift = (s1 - s1.shift(63)).abs() + (s2 - s2.shift(63)).abs() + (s3 - s3.shift(63)).abs()
    b = drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost-mix trend (slope over a year): structural shift toward production cost
def f27ce_f27_cost_efficiency_cormix_trend_252d_base_v015_signal(cor, opex, sgna):
    m = _mean(_f27_cor_mix(cor, opex, sgna), 21)
    b = _slope(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-mix trend (slope over a year): structural admin-share trajectory
def f27ce_f27_cost_efficiency_sgnamix_trend_252d_base_v016_signal(cor, opex, sgna):
    m = _mean(_f27_sgna_mix(cor, opex, sgna), 21)
    b = _slope(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-vs-overhead mix spread CHANGE over a half-year (production-vs-overhead rotation momentum)
def f27ce_f27_cost_efficiency_prodvsovh_mix_63d_base_v017_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    spr = (cor - opex - sgna) / tot
    b = spr - spr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-mix volatility: how unstable the direct-cost share is through the cycle
def f27ce_f27_cost_efficiency_cormix_vol_126d_base_v018_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = _std(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost mix distance above its own 252d minimum (production-cost-share creep)
def f27ce_f27_cost_efficiency_cormix_offmin_252d_base_v019_signal(cor, opex, sgna):
    m = _f27_cor_mix(cor, opex, sgna)
    b = m - _rmin(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A mix year-over-year shift (cyclical admin-share rotation)
def f27ce_f27_cost_efficiency_sgnamix_yoy_252d_base_v020_signal(cor, opex, sgna):
    m = _mean(_f27_sgna_mix(cor, opex, sgna), 21)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK B: OVERHEAD STRUCTURE (sgna vs opex; NOT /revenue) ============

# SG&A weight inside total overhead (sgna/(opex+sgna)), smoothed (overhead composition)
def f27ce_f27_cost_efficiency_ovhsplit_lvl_63d_base_v021_signal(opex, sgna):
    b = _mean(_f27_overhead_split(opex, sgna), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead split z-scored vs own 252d history (de-trended admin-vs-opex tilt)
def f27ce_f27_cost_efficiency_ovhsplit_z_252d_base_v022_signal(opex, sgna):
    sp = _f27_overhead_split(opex, sgna)
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead split change over a quarter (admin gaining/losing weight in overhead)
def f27ce_f27_cost_efficiency_ovhsplit_chg_63d_base_v023_signal(opex, sgna):
    sp = _f27_overhead_split(opex, sgna)
    b = sp - sp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A relative to operating cost (sgna/opex) displacement vs its own slow EMA (overhead drift)
def f27ce_f27_cost_efficiency_sgnaperopex_lvl_63d_base_v024_signal(sgna, opex):
    r = _f27_sgna_per_opex(sgna, opex)
    b = r - r.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-per-opex percentile rank vs own 504d history (overhead-intensity regime)
def f27ce_f27_cost_efficiency_sgnaperopex_rank_504d_base_v025_signal(sgna, opex):
    r = _f27_sgna_per_opex(sgna, opex)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A relative to direct cost (sgna/cor), percentile rank vs own 504d history (admin-vs-prod regime)
def f27ce_f27_cost_efficiency_sgnapercor_lvl_63d_base_v026_signal(sgna, cor):
    r = sgna / cor.replace(0, np.nan)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-per-direct-cost z-scored vs own 252d history
def f27ce_f27_cost_efficiency_sgnapercor_z_252d_base_v027_signal(sgna, cor):
    r = sgna / cor.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex relative to direct cost (opex/cor) volatility (overhead-vs-production instability through cycle)
def f27ce_f27_cost_efficiency_opexpercor_lvl_63d_base_v028_signal(opex, cor):
    r = opex / cor.replace(0, np.nan)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-vs-direct-cost growth gap over a quarter (short-horizon overhead-vs-production inflation)
def f27ce_f27_cost_efficiency_opexpercor_chg_63d_base_v029_signal(opex, cor):
    b = _logret(opex, 63) - _logret(cor, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-to-opex ratio year-over-year shift (overhead composition rotation, independent of cor)
def f27ce_f27_cost_efficiency_sgnaopex_yoy_252d_base_v030_signal(opex, sgna):
    r = _mean(sgna / opex.replace(0, np.nan), 21)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead split trend (slope of sgna/(opex+sgna) over a year)
def f27ce_f27_cost_efficiency_ovhsplit_trend_252d_base_v031_signal(opex, sgna):
    sp = _mean(_f27_overhead_split(opex, sgna), 21)
    b = _slope(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-per-opex volatility (instability of overhead composition through cycle)
def f27ce_f27_cost_efficiency_sgnaperopex_vol_126d_base_v032_signal(sgna, opex):
    r = _f27_sgna_per_opex(sgna, opex)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-vs-opex growth gap z-scored vs own 252d history (overhead-line inflation divergence regime)
def f27ce_f27_cost_efficiency_ovhpercor_disp_base_v033_signal(sgna, opex):
    g = _logret(sgna, 126) - _logret(opex, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-per-direct-cost year-over-year shift (admin-vs-production rotation)
def f27ce_f27_cost_efficiency_sgnapercor_yoy_252d_base_v034_signal(sgna, cor):
    r = _mean(sgna / cor.replace(0, np.nan), 21)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-split distance above its 252d minimum (admin-weight creep within overhead)
def f27ce_f27_cost_efficiency_ovhsplit_offmin_252d_base_v035_signal(opex, sgna):
    sp = _f27_overhead_split(opex, sgna)
    b = sp - _rmin(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK C: COST-vs-REVENUE GROWTH (inflation pass-through / elasticity) ============
# Δlog(cost) - Δlog(revenue): cost inflation passed through vs sales. Distinct from f26's
# Δprofit/Δrevenue (incremental margin) because it compares COST growth to revenue growth.

# direct-cost inflation pass-through over a year (cor growth minus revenue growth)
def f27ce_f27_cost_efficiency_corpass_252d_base_v036_signal(cor, revenue):
    b = _f27_growth_gap(cor, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost inflation pass-through over a half-year
def f27ce_f27_cost_efficiency_corpass_126d_base_v037_signal(cor, revenue):
    b = _f27_growth_gap(cor, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex pass-through over a year (opex growth minus revenue growth: overhead elasticity)
def f27ce_f27_cost_efficiency_opexpass_252d_base_v038_signal(opex, revenue):
    b = _f27_growth_gap(opex, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A pass-through over a year (sgna growth minus revenue growth: admin elasticity)
def f27ce_f27_cost_efficiency_sgnapass_252d_base_v039_signal(sgna, revenue):
    b = _f27_growth_gap(sgna, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost pass-through over a year ((cor+opex+sgna) growth minus revenue growth)
def f27ce_f27_cost_efficiency_totpass_252d_base_v040_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    b = _f27_growth_gap(tot, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-elasticity of revenue: cor growth divided by revenue growth (pass-through ratio, bounded)
def f27ce_f27_cost_efficiency_corelast_252d_base_v041_signal(cor, revenue):
    cg = np.log(cor.replace(0, np.nan).abs()) - np.log(cor.shift(252).replace(0, np.nan).abs())
    rg = np.log(revenue.replace(0, np.nan).abs()) - np.log(revenue.shift(252).replace(0, np.nan).abs())
    b = np.tanh(cg / rg.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-elasticity: (opex+sgna) growth minus revenue growth (overhead pass-through)
def f27ce_f27_cost_efficiency_ovhpass_252d_base_v042_signal(opex, sgna, revenue):
    ovh = opex + sgna
    b = _f27_growth_gap(ovh, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pass-through dispersion: spread between cor, opex and sgna pass-through gaps (cost-line divergence)
def f27ce_f27_cost_efficiency_passdisp_252d_base_v043_signal(cor, opex, sgna, revenue):
    g1 = _f27_growth_gap(cor, revenue, 252)
    g2 = _f27_growth_gap(opex, revenue, 252)
    g3 = _f27_growth_gap(sgna, revenue, 252)
    stk = pd.concat([g1, g2, g3], axis=1)
    b = stk.max(axis=1) - stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-vs-revenue growth gap acceleration (pass-through now minus a quarter ago)
def f27ce_f27_cost_efficiency_corpass_accel_base_v044_signal(cor, revenue):
    g = _f27_growth_gap(cor, revenue, 126)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost pass-through z-scored vs own 504d history (cost-inflation regime)
def f27ce_f27_cost_efficiency_totpass_z_504d_base_v045_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    g = _f27_growth_gap(tot, revenue, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-inflation persistence: fraction of last year cor outgrew revenue (cost outpacing sales)
def f27ce_f27_cost_efficiency_inflpersist_252d_base_v046_signal(cor, revenue):
    g = _f27_growth_gap(cor, revenue, 63)
    outpace = (g > 0).astype(float)
    b = outpace.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-vs-direct-cost growth gap (admin growing faster than production cost)
def f27ce_f27_cost_efficiency_sgnavscor_grw_252d_base_v047_signal(sgna, cor):
    b = _logret(sgna, 252) - _logret(cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-vs-direct-cost growth gap over a half-year (overhead growing faster than production)
def f27ce_f27_cost_efficiency_opexvscor_grw_126d_base_v048_signal(opex, cor):
    b = _logret(opex, 126) - _logret(cor, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-base growth itself (total cost log-growth over a year) — cost-inflation magnitude
def f27ce_f27_cost_efficiency_totcost_grw_252d_base_v049_signal(cor, opex, sgna):
    tot = cor + opex + sgna
    b = _logret(tot, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost growth acceleration (cor growth now minus a year ago) — cost-inflation inflection
def f27ce_f27_cost_efficiency_corgrw_accel_252d_base_v050_signal(cor):
    g = _logret(cor, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK D: OVERHEAD-INTENSITY & SG&A UNIT-COST DYNAMICS (change/trend only) ============
# To avoid aliasing gross margin on real data (where cor dominates so (cor+anything)/revenue ~ 1-gm),
# we expose unit-cost dynamics ONLY for the OVERHEAD lines (opex, sgna), whose /revenue ratios are
# small and NOT close to gross margin, plus genuinely structural mix/growth features.

# overhead intensity ((opex+sgna)/revenue) TREND (slope over a year) — overhead unit-cost direction
def f27ce_f27_cost_efficiency_aisc_trend_252d_base_v051_signal(opex, sgna, revenue):
    a = _mean((opex + sgna) / revenue.replace(0, np.nan), 21)
    b = _slope(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A pass-through minus direct-cost pass-through (overhead-vs-production inflation gap, no margin)
def f27ce_f27_cost_efficiency_aisc_chg_63d_base_v052_signal(sgna, cor, revenue):
    gs = _f27_growth_gap(sgna, revenue, 63)
    gc = _f27_growth_gap(cor, revenue, 63)
    b = gs - gc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-share-of-total-cost acceleration (admin-mix curvature; structural, no revenue)
def f27ce_f27_cost_efficiency_aisc_accel_base_v053_signal(cor, opex, sgna):
    m = _f27_sgna_mix(cor, opex, sgna)
    chg = m - m.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-share-of-total-cost year-over-year shift, ranked (admin-mix rotation regime)
def f27ce_f27_cost_efficiency_aisc_yoy_252d_base_v054_signal(cor, opex, sgna):
    m = _mean(_f27_sgna_mix(cor, opex, sgna), 21)
    chg = m - m.shift(252)
    b = chg.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost growth minus its own slow EMA over a half-year horizon (cost-inflation deviation)
def f27ce_f27_cost_efficiency_aisc_disp_base_v055_signal(cor, opex, sgna):
    g = _logret(cor + opex + sgna, 126)
    b = g - g.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead intensity ((opex+sgna)/revenue) trend strength: slope divided by its own volatility
def f27ce_f27_cost_efficiency_aisc_trendstr_252d_base_v056_signal(opex, sgna, revenue):
    a = _mean((opex + sgna) / revenue.replace(0, np.nan), 21)
    sl = _slope(a, 252)
    vol = _std(a, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-vs-direct growth gap change over a quarter (overhead-encroachment momentum, structural)
def f27ce_f27_cost_efficiency_totunit_chg_63d_base_v057_signal(cor, opex, sgna):
    ovh = opex + sgna
    g = _logret(ovh, 63) - _logret(cor, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost-mix trend strength: cor-share slope divided by its own volatility (mix-trend t-stat)
def f27ce_f27_cost_efficiency_totunit_trend_252d_base_v058_signal(cor, opex, sgna):
    m = _mean(_f27_cor_mix(cor, opex, sgna), 21)
    sl = _slope(m, 252)
    vol = _std(m, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A intensity (sgna/revenue) acceleration smoothed (bounded tanh of admin unit-cost curvature)
def f27ce_f27_cost_efficiency_aisc_accel_tanh_base_v059_signal(sgna, revenue):
    a = sgna / revenue.replace(0, np.nan)
    chg = a - a.shift(63)
    accel = chg - chg.shift(63)
    b = np.tanh(accel * 200.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-share-of-total-cost acceleration (operating-overhead-mix curvature; structural, no revenue)
def f27ce_f27_cost_efficiency_sgnaunit_chg_63d_base_v060_signal(cor, opex, sgna):
    m = _f27_opex_mix(cor, opex, sgna)
    chg = m - m.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============ BLOCK E: COST-DISCIPLINE REGIMES & DISPERSION ============

# cost-discipline regime: fraction of last year total cost FELL while revenue held/rose
def f27ce_f27_cost_efficiency_discipline_252d_base_v061_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    cost_falls = (tot < tot.shift(63)).astype(float)
    rev_holds = (revenue >= revenue.shift(63) * 0.98).astype(float)
    disc = cost_falls * rev_holds
    b = disc.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-cut depth in disciplined regimes: avg quarterly cost decline when revenue held
def f27ce_f27_cost_efficiency_cutdepth_252d_base_v062_signal(cor, opex, sgna, revenue):
    tot = cor + opex + sgna
    cg = _logret(tot, 63)
    rev_holds = (revenue >= revenue.shift(63) * 0.98)
    cut = cg.where(rev_holds & (cg < 0), 0.0)
    b = cut.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-base dispersion: rolling coefficient of variation of total cost (cost-base instability)
def f27ce_f27_cost_efficiency_costcv_126d_base_v063_signal(cor, opex, sgna):
    tot = cor + opex + sgna
    cv = _std(tot, 126) / _mean(tot, 126).replace(0, np.nan)
    b = cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direct-cost growth volatility (std of quarterly cor log-growth) — input-cost shock instability
def f27ce_f27_cost_efficiency_corgrwvol_252d_base_v064_signal(cor):
    g = _logret(cor, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-growth volatility (std of quarterly (opex+sgna) log-growth)
def f27ce_f27_cost_efficiency_ovhgrwvol_252d_base_v065_signal(opex, sgna):
    ovh = opex + sgna
    g = _logret(ovh, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-base growth skew: direct-cost growth minus mean overhead-line growth (production-led vs overhead-led)
def f27ce_f27_cost_efficiency_linegrwdisp_252d_base_v066_signal(cor, opex, sgna):
    g1 = _logret(cor, 252)
    g2 = _logret(opex, 252)
    g3 = _logret(sgna, 252)
    b = g1 - (g2 + g3) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-inflation regime: total cost growth z-scored vs its own 504d history (hot/cold cost cycle)
def f27ce_f27_cost_efficiency_costinfl_z_504d_base_v067_signal(cor, opex, sgna):
    tot = cor + opex + sgna
    g = _logret(tot, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-cut breadth: count of cost lines falling YoY (cor, opex, sgna) plus a continuous nudge
def f27ce_f27_cost_efficiency_cutbreadth_252d_base_v068_signal(cor, opex, sgna):
    f1 = (cor < cor.shift(252)).astype(float)
    f2 = (opex < opex.shift(252)).astype(float)
    f3 = (sgna < sgna.shift(252)).astype(float)
    g = _logret(cor + opex + sgna, 126)
    b = (f1 + f2 + f3) + np.tanh(g * 5.0) * 0.1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead-encroachment regime: fraction of last year overhead grew faster than direct cost
def f27ce_f27_cost_efficiency_ovhencroach_252d_base_v069_signal(opex, sgna, cor):
    ovh = opex + sgna
    gap = _logret(ovh, 63) - _logret(cor, 63)
    enc = (gap > 0).astype(float)
    b = enc.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# input-cost shock: largest single-quarter direct-cost jump over the last year (max cost spike)
def f27ce_f27_cost_efficiency_corshock_252d_base_v070_signal(cor):
    g = _logret(cor, 63)
    b = _rmax(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-mix entropy CHANGE over a half-year (how the cost-base balance is rotating)
def f27ce_f27_cost_efficiency_mixentropy_63d_base_v071_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    s1 = (cor / tot).clip(lower=1e-9)
    s2 = (opex / tot).clip(lower=1e-9)
    s3 = (sgna / tot).clip(lower=1e-9)
    ent = -(s1 * np.log(s1) + s2 * np.log(s2) + s3 * np.log(s3))
    b = ent - ent.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-cost growth minus its own slow EMA (cost-inflation acceleration vs baseline)
def f27ce_f27_cost_efficiency_costgrw_disp_base_v072_signal(cor, opex, sgna):
    g = _logret(cor + opex + sgna, 63)
    b = g - g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# disciplined-quarter streak: longest run within last year of cost falling vs prior quarter
def f27ce_f27_cost_efficiency_disciplinestreak_252d_base_v073_signal(cor, opex, sgna):
    tot = _mean(cor + opex + sgna, 21)
    falling = (tot < tot.shift(21)).astype(float)
    b = falling.rolling(252, min_periods=126).sum() / 252.0 + _z(tot, 126) * 0.05
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# SG&A-share-of-overhead extremity: tanh of (short-window minus long-window split z) regime
def f27ce_f27_cost_efficiency_ovhsplit_zgap_tanh_base_v074_signal(opex, sgna):
    sp = _f27_overhead_split(opex, sgna)
    gap = _z(sp, 63) - _z(sp, 252)
    b = np.tanh(gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cost-mix concentration distance above its own 504d minimum (how concentrated vs least-concentrated)
def f27ce_f27_cost_efficiency_mixhhi_velocity_base_v075_signal(cor, opex, sgna):
    tot = (cor + opex + sgna).replace(0, np.nan)
    hhi = (cor / tot) ** 2 + (opex / tot) ** 2 + (sgna / tot) ** 2
    b = hhi - _rmin(hhi, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27ce_f27_cost_efficiency_cormix_lvl_63d_base_v001_signal,
    f27ce_f27_cost_efficiency_cormix_z_252d_base_v002_signal,
    f27ce_f27_cost_efficiency_cormix_rank_504d_base_v003_signal,
    f27ce_f27_cost_efficiency_cormix_chg_63d_base_v004_signal,
    f27ce_f27_cost_efficiency_opexmix_lvl_63d_base_v005_signal,
    f27ce_f27_cost_efficiency_opexmix_z_252d_base_v006_signal,
    f27ce_f27_cost_efficiency_opexmix_chg_63d_base_v007_signal,
    f27ce_f27_cost_efficiency_sgnamix_lvl_63d_base_v008_signal,
    f27ce_f27_cost_efficiency_sgnamix_z_252d_base_v009_signal,
    f27ce_f27_cost_efficiency_sgnamix_rank_504d_base_v010_signal,
    f27ce_f27_cost_efficiency_sgnamix_chg_63d_base_v011_signal,
    f27ce_f27_cost_efficiency_mixdisp_63d_base_v012_signal,
    f27ce_f27_cost_efficiency_mixhhi_z_252d_base_v013_signal,
    f27ce_f27_cost_efficiency_mixshift_63d_base_v014_signal,
    f27ce_f27_cost_efficiency_cormix_trend_252d_base_v015_signal,
    f27ce_f27_cost_efficiency_sgnamix_trend_252d_base_v016_signal,
    f27ce_f27_cost_efficiency_prodvsovh_mix_63d_base_v017_signal,
    f27ce_f27_cost_efficiency_cormix_vol_126d_base_v018_signal,
    f27ce_f27_cost_efficiency_cormix_offmin_252d_base_v019_signal,
    f27ce_f27_cost_efficiency_sgnamix_yoy_252d_base_v020_signal,
    f27ce_f27_cost_efficiency_ovhsplit_lvl_63d_base_v021_signal,
    f27ce_f27_cost_efficiency_ovhsplit_z_252d_base_v022_signal,
    f27ce_f27_cost_efficiency_ovhsplit_chg_63d_base_v023_signal,
    f27ce_f27_cost_efficiency_sgnaperopex_lvl_63d_base_v024_signal,
    f27ce_f27_cost_efficiency_sgnaperopex_rank_504d_base_v025_signal,
    f27ce_f27_cost_efficiency_sgnapercor_lvl_63d_base_v026_signal,
    f27ce_f27_cost_efficiency_sgnapercor_z_252d_base_v027_signal,
    f27ce_f27_cost_efficiency_opexpercor_lvl_63d_base_v028_signal,
    f27ce_f27_cost_efficiency_opexpercor_chg_63d_base_v029_signal,
    f27ce_f27_cost_efficiency_sgnaopex_yoy_252d_base_v030_signal,
    f27ce_f27_cost_efficiency_ovhsplit_trend_252d_base_v031_signal,
    f27ce_f27_cost_efficiency_sgnaperopex_vol_126d_base_v032_signal,
    f27ce_f27_cost_efficiency_ovhpercor_disp_base_v033_signal,
    f27ce_f27_cost_efficiency_sgnapercor_yoy_252d_base_v034_signal,
    f27ce_f27_cost_efficiency_ovhsplit_offmin_252d_base_v035_signal,
    f27ce_f27_cost_efficiency_corpass_252d_base_v036_signal,
    f27ce_f27_cost_efficiency_corpass_126d_base_v037_signal,
    f27ce_f27_cost_efficiency_opexpass_252d_base_v038_signal,
    f27ce_f27_cost_efficiency_sgnapass_252d_base_v039_signal,
    f27ce_f27_cost_efficiency_totpass_252d_base_v040_signal,
    f27ce_f27_cost_efficiency_corelast_252d_base_v041_signal,
    f27ce_f27_cost_efficiency_ovhpass_252d_base_v042_signal,
    f27ce_f27_cost_efficiency_passdisp_252d_base_v043_signal,
    f27ce_f27_cost_efficiency_corpass_accel_base_v044_signal,
    f27ce_f27_cost_efficiency_totpass_z_504d_base_v045_signal,
    f27ce_f27_cost_efficiency_inflpersist_252d_base_v046_signal,
    f27ce_f27_cost_efficiency_sgnavscor_grw_252d_base_v047_signal,
    f27ce_f27_cost_efficiency_opexvscor_grw_126d_base_v048_signal,
    f27ce_f27_cost_efficiency_totcost_grw_252d_base_v049_signal,
    f27ce_f27_cost_efficiency_corgrw_accel_252d_base_v050_signal,
    f27ce_f27_cost_efficiency_aisc_trend_252d_base_v051_signal,
    f27ce_f27_cost_efficiency_aisc_chg_63d_base_v052_signal,
    f27ce_f27_cost_efficiency_aisc_accel_base_v053_signal,
    f27ce_f27_cost_efficiency_aisc_yoy_252d_base_v054_signal,
    f27ce_f27_cost_efficiency_aisc_disp_base_v055_signal,
    f27ce_f27_cost_efficiency_aisc_trendstr_252d_base_v056_signal,
    f27ce_f27_cost_efficiency_totunit_chg_63d_base_v057_signal,
    f27ce_f27_cost_efficiency_totunit_trend_252d_base_v058_signal,
    f27ce_f27_cost_efficiency_aisc_accel_tanh_base_v059_signal,
    f27ce_f27_cost_efficiency_sgnaunit_chg_63d_base_v060_signal,
    f27ce_f27_cost_efficiency_discipline_252d_base_v061_signal,
    f27ce_f27_cost_efficiency_cutdepth_252d_base_v062_signal,
    f27ce_f27_cost_efficiency_costcv_126d_base_v063_signal,
    f27ce_f27_cost_efficiency_corgrwvol_252d_base_v064_signal,
    f27ce_f27_cost_efficiency_ovhgrwvol_252d_base_v065_signal,
    f27ce_f27_cost_efficiency_linegrwdisp_252d_base_v066_signal,
    f27ce_f27_cost_efficiency_costinfl_z_504d_base_v067_signal,
    f27ce_f27_cost_efficiency_cutbreadth_252d_base_v068_signal,
    f27ce_f27_cost_efficiency_ovhencroach_252d_base_v069_signal,
    f27ce_f27_cost_efficiency_corshock_252d_base_v070_signal,
    f27ce_f27_cost_efficiency_mixentropy_63d_base_v071_signal,
    f27ce_f27_cost_efficiency_costgrw_disp_base_v072_signal,
    f27ce_f27_cost_efficiency_disciplinestreak_252d_base_v073_signal,
    f27ce_f27_cost_efficiency_ovhsplit_zgap_tanh_base_v074_signal,
    f27ce_f27_cost_efficiency_mixhhi_velocity_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_COST_EFFICIENCY_REGISTRY_001_075 = REGISTRY


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

    print("OK f27_cost_efficiency_base_001_075_claude: %d features pass" % n_features)
