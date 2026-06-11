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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (valuation-vs-cycle) =====
def _f43_growth(s, w):
    # log growth of a fundamental over window w (cycle/growth proxy)
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f43_peg(mult, growth):
    # multiple-to-growth ratio (PEG-like); growth in pct points
    g = (growth * 100.0)
    return mult / g.replace(0, np.nan)


def _f43_rangepos(s, w):
    hi = _rmax(s, w)
    lo = _rmin(s, w)
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f43_revert_gap(s, w):
    # mean-reversion gap: level minus its own rolling mean, scaled by std
    return _z(s, w)


def _f43_implied_evebitda(ev, ebitda):
    return ev / ebitda.replace(0, np.nan)


def _f43_implied_evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


# ============================================================
# EV/EBITDA-to-growth (PEG-style): multiple per point of EBITDA growth
def f43vc_f43_valuation_vs_cycle_evebitdapeg_252d_base_v001_signal(evebitda, ebitda):
    g = _f43_growth(ebitda, 252)
    b = _f43_peg(evebitda, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA vs top-line cycle: multiple z minus revenue-growth z (rich-vs-growth)
def f43vc_f43_valuation_vs_cycle_evebitdarevg_252d_base_v002_signal(evebitda, revenue):
    g = _f43_growth(revenue, 252)
    b = _z(evebitda, 252) - _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-revenue-growth (cheapness vs growth, PEG ratio)
def f43vc_f43_valuation_vs_cycle_evsalespeg_252d_base_v003_signal(ev, revenue):
    mult = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252)
    b = _f43_peg(mult, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B-to-EBITDA-growth: asset multiple discounted by earnings cycle growth (log form)
def f43vc_f43_valuation_vs_cycle_pbpeg_252d_base_v004_signal(pb, ebitda):
    g = _f43_growth(ebitda, 252)
    b = np.log(pb.replace(0, np.nan)) - g.clip(-1.0, 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation z vs own 504d history (cheap/rich vs cycle mean) for EV/EBITDA
def f43vc_f43_valuation_vs_cycle_evebitdaz_504d_base_v005_signal(evebitda):
    b = _f43_revert_gap(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation z vs own 252d history for P/B (asset multiple cheapness vs cycle)
def f43vc_f43_valuation_vs_cycle_pbz_252d_base_v006_signal(pb):
    b = _f43_revert_gap(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales z vs own 252d history (re-rating distance from cycle mean)
def f43vc_f43_valuation_vs_cycle_evsalesz_252d_base_v007_signal(ev, revenue):
    mult = _f43_implied_evsales(ev, revenue)
    b = _f43_revert_gap(mult, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple re-rating vs fundamentals: EV growth minus EBITDA growth (de-rate gap)
def f43vc_f43_valuation_vs_cycle_evrerate_252d_base_v008_signal(ev, ebitda):
    ge = _f43_growth(ev, 252)
    gf = _f43_growth(ebitda, 252)
    b = ge - gf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap growth minus revenue growth (price re-rating vs top-line)
def f43vc_f43_valuation_vs_cycle_mcaprerate_252d_base_v009_signal(marketcap, revenue):
    gm = _f43_growth(marketcap, 252)
    gr = _f43_growth(revenue, 252)
    b = gm - gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA multiple change vs EBITDA cycle (multiple expansion contribution)
def f43vc_f43_valuation_vs_cycle_multexp_252d_base_v010_signal(evebitda, ebitda):
    gm = _f43_growth(evebitda, 252)
    gf = _f43_growth(ebitda, 252)
    b = gm - 0.5 * gf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position of EV/EBITDA within its 1260d range (cheap-at-bottom)
def f43vc_f43_valuation_vs_cycle_evebitdarng_1260d_base_v011_signal(evebitda):
    b = _f43_rangepos(evebitda, 1260) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position of P/B within its 504d range
def f43vc_f43_valuation_vs_cycle_pbrng_504d_base_v012_signal(pb):
    b = _f43_rangepos(pb, 504) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean-reversion gap: EV/EBITDA minus its 252d mean, normalized by level
def f43vc_f43_valuation_vs_cycle_evebitdamrgap_252d_base_v013_signal(evebitda):
    m = _mean(evebitda, 252)
    b = (evebitda - m) / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean-reversion gap of P/B relative to its 504d mean
def f43vc_f43_valuation_vs_cycle_pbmrgap_504d_base_v014_signal(pb):
    m = _mean(pb, 504)
    b = (pb - m) / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation vs cycle phase: EV/EBITDA z scaled by where revenue sits in its cycle
def f43vc_f43_valuation_vs_cycle_valphase_252d_base_v015_signal(evebitda, revenue):
    vz = _f43_revert_gap(evebitda, 252)
    phase = _f43_rangepos(revenue, 252) - 0.5
    b = vz * (1.0 + phase)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness gated by revenue cycle position (cheap-but-early)
def f43vc_f43_valuation_vs_cycle_cheapphase_252d_base_v016_signal(ev, revenue):
    mult = _f43_implied_evsales(ev, revenue)
    cheap = -_f43_revert_gap(mult, 504)
    phase = _f43_rangepos(revenue, 504)
    b = cheap * phase
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied EV/EBITDA from ev & ebitda vs reported evebitda (consistency drift)
def f43vc_f43_valuation_vs_cycle_implieddrift_base_v017_signal(ev, ebitda, evebitda):
    implied = _f43_implied_evebitda(ev, ebitda)
    b = (implied - evebitda) / evebitda.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth ranked vs its own 504d history (cross-cycle PEG percentile)
def f43vc_f43_valuation_vs_cycle_pegrank_504d_base_v018_signal(evebitda, ebitda):
    g = _f43_growth(ebitda, 252)
    peg = _f43_peg(evebitda, g)
    b = _rank(peg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B-to-revenue-growth ranked vs own history
def f43vc_f43_valuation_vs_cycle_pbgrank_504d_base_v019_signal(pb, revenue):
    g = _f43_growth(revenue, 252)
    peg = _f43_peg(pb, g)
    b = _rank(peg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple-vs-growth spread: EV/EBITDA z minus EBITDA-growth z (rich-vs-accelerating)
def f43vc_f43_valuation_vs_cycle_valgrowthspr_252d_base_v020_signal(evebitda, ebitda):
    vz = _z(evebitda, 252)
    gz = _z(_f43_growth(ebitda, 126), 252)
    b = vz - gz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-vs-fundamental spread: marketcap z minus revenue z (re-rating vs cycle)
def f43vc_f43_valuation_vs_cycle_mcaprevspr_252d_base_v021_signal(marketcap, revenue):
    mz = _z(marketcap, 252)
    rz = _z(revenue, 252)
    b = mz - rz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV vs EBITDA spread in z-space (enterprise value rich vs earnings cycle)
def f43vc_f43_valuation_vs_cycle_evebitspr_504d_base_v022_signal(ev, ebitda):
    ez = _z(ev, 504)
    bz = _z(ebitda, 504)
    b = ez - bz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA short-vs-long mean-reversion (63d level vs 252d mean)
def f43vc_f43_valuation_vs_cycle_evebitdarev_63v252_base_v023_signal(evebitda):
    short = _mean(evebitda, 63)
    long = _mean(evebitda, 252)
    b = (short - long) / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B short-vs-long ratio (asset multiple momentum vs cycle baseline)
def f43vc_f43_valuation_vs_cycle_pbrev_63v252_base_v024_signal(pb):
    short = _mean(pb, 63)
    long = _mean(pb, 252)
    b = (short - long) / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales short vs long (valuation drift relative to cycle)
def f43vc_f43_valuation_vs_cycle_evsalesrev_63v252_base_v025_signal(ev, revenue):
    mult = _f43_implied_evsales(ev, revenue)
    short = _mean(mult, 63)
    long = _mean(mult, 252)
    b = (short - long) / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-growth-adjusted cheapness: -(EV/EBITDA z) weighted by positive growth
def f43vc_f43_valuation_vs_cycle_growthcheap_252d_base_v026_signal(evebitda, ebitda):
    cheap = -_z(evebitda, 252)
    g = _f43_growth(ebitda, 252).clip(lower=0)
    b = cheap * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation gap from mid-cycle: EV/EBITDA minus its 1260d median
def f43vc_f43_valuation_vs_cycle_midcyclegap_1260d_base_v027_signal(evebitda):
    med = evebitda.rolling(1260, min_periods=504).median()
    b = (evebitda - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B gap from mid-cycle median (1260d)
def f43vc_f43_valuation_vs_cycle_pbmidcycle_1260d_base_v028_signal(pb):
    med = pb.rolling(1260, min_periods=504).median()
    b = (pb - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth change over a quarter (PEG improvement/deterioration)
def f43vc_f43_valuation_vs_cycle_pegchg_252d_base_v029_signal(evebitda, ebitda):
    g = _f43_growth(ebitda, 252)
    peg = _f43_peg(evebitda, g)
    b = peg - peg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far revenue cycle has moved while multiple stayed flat (cheapening via growth)
def f43vc_f43_valuation_vs_cycle_growthcatchup_252d_base_v030_signal(evebitda, revenue):
    gr = _f43_growth(revenue, 252)
    gm = _f43_growth(evebitda, 252)
    b = gr - gm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation z conditioned on down-cycle (EBITDA below its 252d mean)
def f43vc_f43_valuation_vs_cycle_downcycleval_252d_base_v031_signal(evebitda, ebitda):
    vz = _z(evebitda, 252)
    down = (ebitda < _mean(ebitda, 252)).astype(float)
    b = vz * (1.0 + down)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation z conditioned on up-cycle (revenue above its 252d mean)
def f43vc_f43_valuation_vs_cycle_upcycleval_252d_base_v032_signal(pb, revenue):
    vz = _z(pb, 252)
    up = (revenue > _mean(revenue, 252)).astype(float)
    b = vz * (1.0 + up)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA per unit of revenue-cycle position (multiple cost of being late-cycle)
def f43vc_f43_valuation_vs_cycle_multpercycle_252d_base_v033_signal(evebitda, revenue):
    phase = (_f43_rangepos(revenue, 252) + 0.1)
    b = evebitda / phase.replace(0, np.nan)
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness vs growth: average of EV/EBITDA and P/B z, minus growth z
def f43vc_f43_valuation_vs_cycle_blendedgap_252d_base_v034_signal(evebitda, pb, ebitda):
    vz = 0.5 * _z(evebitda, 252) + 0.5 * _z(pb, 252)
    gz = _z(_f43_growth(ebitda, 252), 252)
    b = vz - gz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-growth (PEG) z-scored vs own history
def f43vc_f43_valuation_vs_cycle_evsalespegz_252d_base_v035_signal(ev, revenue):
    mult = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252)
    peg = _f43_peg(mult, g)
    b = _z(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple expansion velocity: EV/EBITDA log-growth over a quarter
def f43vc_f43_valuation_vs_cycle_multvel_63d_base_v036_signal(evebitda):
    b = _f43_growth(evebitda, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B re-rating velocity over a quarter
def f43vc_f43_valuation_vs_cycle_pbvel_63d_base_v037_signal(pb):
    b = _f43_growth(pb, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation tension: EV/EBITDA rangepos minus revenue rangepos (rich-while-low-cycle)
def f43vc_f43_valuation_vs_cycle_tension_252d_base_v038_signal(evebitda, revenue):
    vp = _f43_rangepos(evebitda, 252)
    cp = _f43_rangepos(revenue, 252)
    b = vp - cp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B vs EBITDA-cycle tension (asset multiple rich while earnings depressed)
def f43vc_f43_valuation_vs_cycle_pbtension_504d_base_v039_signal(pb, ebitda):
    vp = _f43_rangepos(pb, 504)
    cp = _f43_rangepos(ebitda, 504)
    b = vp - cp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness rank gated by EBITDA-growth sign (cheap-and-growing)
def f43vc_f43_valuation_vs_cycle_cheapgrow_504d_base_v040_signal(evebitda, ebitda):
    cheap = -_rank(evebitda, 504)
    grow = np.sign(_f43_growth(ebitda, 252))
    b = cheap * grow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied EV/Sales vs EV/EBITDA scaled by margin (valuation structure vs margin cycle)
def f43vc_f43_valuation_vs_cycle_valstructure_base_v041_signal(ev, revenue, ebitda):
    evs = _f43_implied_evsales(ev, revenue)
    eve = _f43_implied_evebitda(ev, ebitda)
    margin = ebitda / revenue.replace(0, np.nan)
    b = (eve * margin - evs) / evs.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA YoY change relative to EBITDA YoY change (re-rating vs earnings)
def f43vc_f43_valuation_vs_cycle_yoyrerate_252d_base_v042_signal(evebitda, ebitda):
    vg = (evebitda - evebitda.shift(252)) / evebitda.shift(252).replace(0, np.nan)
    eg = (ebitda - ebitda.shift(252)) / ebitda.shift(252).replace(0, np.nan)
    b = vg - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap-to-revenue (price/sales proxy) z vs own cycle
def f43vc_f43_valuation_vs_cycle_psz_252d_base_v043_signal(marketcap, revenue):
    ps = marketcap / revenue.replace(0, np.nan)
    b = _z(ps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/revenue cycle position over 1260d
def f43vc_f43_valuation_vs_cycle_psrng_1260d_base_v044_signal(marketcap, revenue):
    ps = marketcap / revenue.replace(0, np.nan)
    b = _f43_rangepos(ps, 1260) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation-to-growth using marketcap/revenue: log P/S minus revenue growth (price PEG)
def f43vc_f43_valuation_vs_cycle_pspeg_252d_base_v045_signal(marketcap, revenue):
    ps = marketcap / revenue.replace(0, np.nan)
    g = _f43_growth(revenue, 252)
    b = np.log(ps.replace(0, np.nan)) - 2.0 * g.clip(-1.0, 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA dispersion vs revenue dispersion (valuation noise vs cycle noise)
def f43vc_f43_valuation_vs_cycle_dispratio_252d_base_v046_signal(evebitda, revenue):
    vd = _std(_f43_growth(evebitda, 21), 252)
    cd = _std(_f43_growth(revenue, 21), 252)
    b = vd / cd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-vs-cycle composite: low EV/EBITDA rank + high revenue-cycle rank
def f43vc_f43_valuation_vs_cycle_cheaplatecycle_504d_base_v047_signal(evebitda, revenue):
    cheap = -_rank(evebitda, 504)
    late = _f43_rangepos(revenue, 504) - 0.5
    b = cheap + late
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation overshoot persistence: time above 1-sigma rich vs 504d mean, depth-weighted
def f43vc_f43_valuation_vs_cycle_overshoot_504d_base_v048_signal(evebitda):
    z = _z(evebitda, 504)
    rich = (z > 1.0).astype(float)
    persist = rich.rolling(126, min_periods=63).mean()
    b = persist + 0.1 * z.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation undershoot of P/B: signed convex depth vs 504d mean (deep-value cycle)
def f43vc_f43_valuation_vs_cycle_undershoot_504d_base_v049_signal(pb):
    z = _z(pb, 504)
    b = -np.sign(z) * (z.abs() ** 1.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA minus P/B in z-space (which multiple is leading the re-rating)
def f43vc_f43_valuation_vs_cycle_multdiverge_252d_base_v050_signal(evebitda, pb):
    b = _z(evebitda, 252) - _z(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted EV/Sales rank (cheap per growth across cycle)
def f43vc_f43_valuation_vs_cycle_gadjevsales_504d_base_v051_signal(ev, revenue):
    mult = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252).clip(lower=0.001)
    adj = mult / (1.0 + g)
    b = _rank(adj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple momentum minus EBITDA momentum, z-scored (peak-cycle warning)
def f43vc_f43_valuation_vs_cycle_peakwarn_252d_base_v052_signal(evebitda, ebitda):
    multmom = _f43_growth(evebitda, 63)
    earnmom = _f43_growth(ebitda, 63)
    b = multmom - earnmom
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cycle-deviation curvature: change in the log ema-detrend over a quarter
def f43vc_f43_valuation_vs_cycle_logdetrend_252d_base_v053_signal(evebitda):
    le = np.log(evebitda.replace(0, np.nan))
    detr = le - le.ewm(span=252, min_periods=63).mean()
    b = detr - detr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B detrended by ema over 504d
def f43vc_f43_valuation_vs_cycle_pblogdetrend_504d_base_v054_signal(pb):
    lp = np.log(pb.replace(0, np.nan))
    b = lp - lp.ewm(span=504, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth-scaled valuation cheap gap (cheap matters more when growing)
def f43vc_f43_valuation_vs_cycle_scaledgap_252d_base_v055_signal(evebitda, revenue):
    gap = -(_z(evebitda, 252))
    g = (1.0 + _f43_growth(revenue, 252).clip(lower=-0.5))
    b = gap * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA vs EV/Sales log-spread vs its mean (margin-cycle re-rating)
def f43vc_f43_valuation_vs_cycle_marginrerate_252d_base_v056_signal(ev, ebitda, revenue):
    eve = _f43_implied_evebitda(ev, ebitda)
    evs = _f43_implied_evsales(ev, revenue)
    spread = np.log(eve.replace(0, np.nan)) - np.log(evs.replace(0, np.nan))
    b = spread - _mean(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year EV/EBITDA spent below its 252d mean (cheap-regime time)
def f43vc_f43_valuation_vs_cycle_cheaptime_252d_base_v057_signal(evebitda):
    below = (evebitda < _mean(evebitda, 252)).astype(float)
    b = below.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA crossings over mid-cycle median plus distance from median (re-rating churn)
def f43vc_f43_valuation_vs_cycle_reratechurn_504d_base_v058_signal(evebitda):
    med = evebitda.rolling(504, min_periods=252).median()
    above = (evebitda > med).astype(float)
    cross = (above != above.shift(1)).astype(float)
    churn = cross.rolling(252, min_periods=126).sum()
    gap = (evebitda - med).abs() / med.replace(0, np.nan)
    b = churn + 5.0 * gap.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth where growth measured over a quarter (short-cycle PEG)
def f43vc_f43_valuation_vs_cycle_shortpeg_63d_base_v059_signal(evebitda, ebitda):
    g = _f43_growth(ebitda, 63)
    peg = _f43_peg(evebitda, g)
    b = _z(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus EV/Sales growth, smoothed (sustained de-rating into growth)
def f43vc_f43_valuation_vs_cycle_sustainderate_252d_base_v060_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    gr = _f43_growth(revenue, 252)
    gv = _f43_growth(evs, 252)
    raw = gr - gv
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA distance from its 1260d min (how far re-rated off cycle trough)
def f43vc_f43_valuation_vs_cycle_offtrough_1260d_base_v061_signal(evebitda):
    lo = _rmin(evebitda, 1260)
    b = evebitda / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B de-rating velocity from 1260d peak: change in distance-below-peak over a quarter
def f43vc_f43_valuation_vs_cycle_offpeak_1260d_base_v062_signal(pb):
    hi = _rmax(pb, 1260)
    gap = pb / hi.replace(0, np.nan) - 1.0
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation vs cycle interaction: EV/EBITDA z times sign of EBITDA momentum
def f43vc_f43_valuation_vs_cycle_valmomsign_252d_base_v063_signal(evebitda, ebitda):
    vz = _z(evebitda, 252)
    mom = np.sign(_f43_growth(ebitda, 126))
    b = vz * mom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/EBITDA (equity multiple) z discounted by EBITDA growth (growth-adj cheapness)
def f43vc_f43_valuation_vs_cycle_mcapebitdapeg_252d_base_v064_signal(marketcap, ebitda):
    mult = marketcap / ebitda.replace(0, np.nan)
    g = _f43_growth(ebitda, 252)
    b = _z(mult, 252) - 3.0 * g.clip(-1.0, 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/EBITDA z vs cycle (equity earnings multiple cheapness)
def f43vc_f43_valuation_vs_cycle_mcapebitdaz_504d_base_v065_signal(marketcap, ebitda):
    mult = marketcap / ebitda.replace(0, np.nan)
    b = _z(mult, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended valuation rank minus blended growth rank (composite cheap-vs-growth)
def f43vc_f43_valuation_vs_cycle_blendrank_504d_base_v066_signal(evebitda, pb, revenue):
    valr = 0.5 * _rank(evebitda, 504) + 0.5 * _rank(pb, 504)
    growr = _rank(_f43_growth(revenue, 252), 504)
    b = valr - growr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA half-cycle slope (126d) minus EBITDA half-cycle slope
def f43vc_f43_valuation_vs_cycle_halfcyclespr_126d_base_v067_signal(evebitda, ebitda):
    vs = _f43_growth(evebitda, 126)
    es = _f43_growth(ebitda, 126)
    b = vs - es
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation cheap gated by EBITDA near 1260d cycle bottom (cheap & at-bottom)
def f43vc_f43_valuation_vs_cycle_bottomcheap_1260d_base_v068_signal(evebitda, ebitda):
    cheap = -_f43_rangepos(evebitda, 504)
    cyclepos = _f43_rangepos(ebitda, 1260)
    b = cheap * (1.0 - cyclepos)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales mean-reversion gap weighted by inverse revenue-cycle position
def f43vc_f43_valuation_vs_cycle_invcycleval_252d_base_v069_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    gap = (evs - _mean(evs, 252)) / _mean(evs, 252).replace(0, np.nan)
    inv = (1.0 - _f43_rangepos(revenue, 252))
    b = gap * inv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B-to-growth where growth from EBITDA half-cycle (asset PEG short)
def f43vc_f43_valuation_vs_cycle_pbpegshort_126d_base_v070_signal(pb, ebitda):
    g = _f43_growth(ebitda, 126)
    peg = _f43_peg(pb, g)
    b = _z(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA richness vs EBITDA-cycle-position implied band (residual richness)
def f43vc_f43_valuation_vs_cycle_fairresid_252d_base_v071_signal(evebitda, ebitda):
    cyclepos = _f43_rangepos(ebitda, 252)
    lo = _rmin(evebitda, 252)
    hi = _rmax(evebitda, 252)
    fair = lo + (hi - lo) * cyclepos
    b = (evebitda - fair) / fair.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth percentile minus EV/Sales percentile (cycle-vs-valuation rank gap)
def f43vc_f43_valuation_vs_cycle_rankgap_504d_base_v072_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    gr = _rank(_f43_growth(revenue, 252), 504)
    vr = _rank(evs, 504)
    b = gr - vr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA compression speed: change in distance-below-504d-peak over a quarter
def f43vc_f43_valuation_vs_cycle_compresspeak_504d_base_v073_signal(evebitda):
    hi = _rmax(evebitda, 504)
    gap = np.log(evebitda.replace(0, np.nan) / hi.replace(0, np.nan))
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple-to-growth elasticity: ratio of multiple change to growth change
def f43vc_f43_valuation_vs_cycle_elasticity_252d_base_v074_signal(evebitda, ebitda):
    dm = _f43_growth(evebitda, 63)
    dg = _f43_growth(ebitda, 63)
    b = dm / (dg.abs() + 0.05)
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cycle-cheapness: low EV/Sales rank gated by accelerating revenue momentum
def f43vc_f43_valuation_vs_cycle_cyclecheap_252d_base_v075_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    cheap = -_rank(evs, 252)
    accel = _f43_growth(revenue, 63) - _f43_growth(revenue, 126) / 2.0
    b = cheap * (1.0 + np.tanh(10.0 * accel))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43vc_f43_valuation_vs_cycle_evebitdapeg_252d_base_v001_signal,
    f43vc_f43_valuation_vs_cycle_evebitdarevg_252d_base_v002_signal,
    f43vc_f43_valuation_vs_cycle_evsalespeg_252d_base_v003_signal,
    f43vc_f43_valuation_vs_cycle_pbpeg_252d_base_v004_signal,
    f43vc_f43_valuation_vs_cycle_evebitdaz_504d_base_v005_signal,
    f43vc_f43_valuation_vs_cycle_pbz_252d_base_v006_signal,
    f43vc_f43_valuation_vs_cycle_evsalesz_252d_base_v007_signal,
    f43vc_f43_valuation_vs_cycle_evrerate_252d_base_v008_signal,
    f43vc_f43_valuation_vs_cycle_mcaprerate_252d_base_v009_signal,
    f43vc_f43_valuation_vs_cycle_multexp_252d_base_v010_signal,
    f43vc_f43_valuation_vs_cycle_evebitdarng_1260d_base_v011_signal,
    f43vc_f43_valuation_vs_cycle_pbrng_504d_base_v012_signal,
    f43vc_f43_valuation_vs_cycle_evebitdamrgap_252d_base_v013_signal,
    f43vc_f43_valuation_vs_cycle_pbmrgap_504d_base_v014_signal,
    f43vc_f43_valuation_vs_cycle_valphase_252d_base_v015_signal,
    f43vc_f43_valuation_vs_cycle_cheapphase_252d_base_v016_signal,
    f43vc_f43_valuation_vs_cycle_implieddrift_base_v017_signal,
    f43vc_f43_valuation_vs_cycle_pegrank_504d_base_v018_signal,
    f43vc_f43_valuation_vs_cycle_pbgrank_504d_base_v019_signal,
    f43vc_f43_valuation_vs_cycle_valgrowthspr_252d_base_v020_signal,
    f43vc_f43_valuation_vs_cycle_mcaprevspr_252d_base_v021_signal,
    f43vc_f43_valuation_vs_cycle_evebitspr_504d_base_v022_signal,
    f43vc_f43_valuation_vs_cycle_evebitdarev_63v252_base_v023_signal,
    f43vc_f43_valuation_vs_cycle_pbrev_63v252_base_v024_signal,
    f43vc_f43_valuation_vs_cycle_evsalesrev_63v252_base_v025_signal,
    f43vc_f43_valuation_vs_cycle_growthcheap_252d_base_v026_signal,
    f43vc_f43_valuation_vs_cycle_midcyclegap_1260d_base_v027_signal,
    f43vc_f43_valuation_vs_cycle_pbmidcycle_1260d_base_v028_signal,
    f43vc_f43_valuation_vs_cycle_pegchg_252d_base_v029_signal,
    f43vc_f43_valuation_vs_cycle_growthcatchup_252d_base_v030_signal,
    f43vc_f43_valuation_vs_cycle_downcycleval_252d_base_v031_signal,
    f43vc_f43_valuation_vs_cycle_upcycleval_252d_base_v032_signal,
    f43vc_f43_valuation_vs_cycle_multpercycle_252d_base_v033_signal,
    f43vc_f43_valuation_vs_cycle_blendedgap_252d_base_v034_signal,
    f43vc_f43_valuation_vs_cycle_evsalespegz_252d_base_v035_signal,
    f43vc_f43_valuation_vs_cycle_multvel_63d_base_v036_signal,
    f43vc_f43_valuation_vs_cycle_pbvel_63d_base_v037_signal,
    f43vc_f43_valuation_vs_cycle_tension_252d_base_v038_signal,
    f43vc_f43_valuation_vs_cycle_pbtension_504d_base_v039_signal,
    f43vc_f43_valuation_vs_cycle_cheapgrow_504d_base_v040_signal,
    f43vc_f43_valuation_vs_cycle_valstructure_base_v041_signal,
    f43vc_f43_valuation_vs_cycle_yoyrerate_252d_base_v042_signal,
    f43vc_f43_valuation_vs_cycle_psz_252d_base_v043_signal,
    f43vc_f43_valuation_vs_cycle_psrng_1260d_base_v044_signal,
    f43vc_f43_valuation_vs_cycle_pspeg_252d_base_v045_signal,
    f43vc_f43_valuation_vs_cycle_dispratio_252d_base_v046_signal,
    f43vc_f43_valuation_vs_cycle_cheaplatecycle_504d_base_v047_signal,
    f43vc_f43_valuation_vs_cycle_overshoot_504d_base_v048_signal,
    f43vc_f43_valuation_vs_cycle_undershoot_504d_base_v049_signal,
    f43vc_f43_valuation_vs_cycle_multdiverge_252d_base_v050_signal,
    f43vc_f43_valuation_vs_cycle_gadjevsales_504d_base_v051_signal,
    f43vc_f43_valuation_vs_cycle_peakwarn_252d_base_v052_signal,
    f43vc_f43_valuation_vs_cycle_logdetrend_252d_base_v053_signal,
    f43vc_f43_valuation_vs_cycle_pblogdetrend_504d_base_v054_signal,
    f43vc_f43_valuation_vs_cycle_scaledgap_252d_base_v055_signal,
    f43vc_f43_valuation_vs_cycle_marginrerate_252d_base_v056_signal,
    f43vc_f43_valuation_vs_cycle_cheaptime_252d_base_v057_signal,
    f43vc_f43_valuation_vs_cycle_reratechurn_504d_base_v058_signal,
    f43vc_f43_valuation_vs_cycle_shortpeg_63d_base_v059_signal,
    f43vc_f43_valuation_vs_cycle_sustainderate_252d_base_v060_signal,
    f43vc_f43_valuation_vs_cycle_offtrough_1260d_base_v061_signal,
    f43vc_f43_valuation_vs_cycle_offpeak_1260d_base_v062_signal,
    f43vc_f43_valuation_vs_cycle_valmomsign_252d_base_v063_signal,
    f43vc_f43_valuation_vs_cycle_mcapebitdapeg_252d_base_v064_signal,
    f43vc_f43_valuation_vs_cycle_mcapebitdaz_504d_base_v065_signal,
    f43vc_f43_valuation_vs_cycle_blendrank_504d_base_v066_signal,
    f43vc_f43_valuation_vs_cycle_halfcyclespr_126d_base_v067_signal,
    f43vc_f43_valuation_vs_cycle_bottomcheap_1260d_base_v068_signal,
    f43vc_f43_valuation_vs_cycle_invcycleval_252d_base_v069_signal,
    f43vc_f43_valuation_vs_cycle_pbpegshort_126d_base_v070_signal,
    f43vc_f43_valuation_vs_cycle_fairresid_252d_base_v071_signal,
    f43vc_f43_valuation_vs_cycle_rankgap_504d_base_v072_signal,
    f43vc_f43_valuation_vs_cycle_compresspeak_504d_base_v073_signal,
    f43vc_f43_valuation_vs_cycle_elasticity_252d_base_v074_signal,
    f43vc_f43_valuation_vs_cycle_cyclecheap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_VALUATION_VS_CYCLE_REGISTRY_001_075 = REGISTRY


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

    evebitda = _fund(1, base=8.0, drift=0.02, vol=0.05).rename("evebitda")
    pb = _fund(2, base=1.5, drift=0.015, vol=0.05).rename("pb")
    ev = _fund(3, base=5e8, drift=0.03, vol=0.07).rename("ev")
    marketcap = _fund(4, base=4e8, drift=0.03, vol=0.07).rename("marketcap")
    revenue = _fund(5, base=2e8, drift=0.025, vol=0.06).rename("revenue")
    ebitda = _fund(6, base=6e7, drift=0.025, vol=0.08).rename("ebitda")

    cols = {"evebitda": evebitda, "pb": pb, "ev": ev,
            "marketcap": marketcap, "revenue": revenue, "ebitda": ebitda}

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

    print("OK f43_valuation_vs_cycle_base_001_075_claude: %d features pass" % n_features)
