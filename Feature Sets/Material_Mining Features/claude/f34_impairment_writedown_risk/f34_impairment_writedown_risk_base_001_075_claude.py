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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ===== folder domain primitives (impairment / writedown risk) =====
# DESIGN NOTE: this family is TIGHTENED to IMPAIRMENT / WRITEDOWN RISK only and is
# deliberately built on DEPRECIATION/AMORTIZATION (depamor) AGING dynamics and
# INTANGIBLE/GOODWILL DRAG temporal constructs. It intentionally AVOIDS the static
# balance-sheet level ratios owned by siblings: PP&E/assets & tangibles/assets (f30),
# equity/assets (f42 & f22), intangibles/equity & intangibles/ppnenet (f42/f30).
# None of those siblings use `depamor`, so the aging axis is structurally distinct.
# To keep the family internally non-redundant on smooth data we never pair a ratio with
# its own reciprocal; the aging charge (depamor/ppnenet) is the single retained life axis.
def _aging(depamor, ppnenet):
    # depreciation/amortization charge against the hard PP&E base (aging proxy:
    # a high & rising charge means an old, heavily-used base prone to writedown).
    return depamor / ppnenet.replace(0, np.nan)


def _amort_rate(depamor, intangibles):
    # amortization run-off rate of the SOFT (intangible/goodwill) book: a low rate on a
    # large book -> stale, un-charged goodwill carrying latent writedown risk.
    return depamor / intangibles.replace(0, np.nan)


def _gw_load(intangibles, tangibles):
    # goodwill-heavy mix vs the HARD tangible base (soft-to-hard book composition).
    # uses tangibles (not assets) so it does not reduce to f30/f42 tangible-share-of-assets.
    return intangibles / tangibles.replace(0, np.nan)


def _unamortized_build(intangibles, depamor, w):
    # intangible-book growth in excess of what amortization is running off:
    # goodwill/intangibles piling up faster than they are charged down -> writedown fuel.
    return _growth(intangibles, w) - _growth(depamor, w)


def _reinvest_gap(ppnenet, depamor, w):
    # CHARGE-led decay gap: D&A-charge growth versus the aging level, with BOTH terms z-scored
    # over the same window so neither dominates. A positive gap = the charge is accelerating
    # faster than the (already heavy) aging rate -> depreciation pulled forward, decaying base.
    # Built on depamor (sibling-free) and the aging rate, NOT raw PP&E growth, so it neither
    # reduces to f30's PP&E-growth feature nor to the raw D&A-charge-growth feature.
    return _z(_growth(depamor, w), w) - _z(_aging(depamor, ppnenet), w)




# ============================================================
# ---- DEPAMOR AGING core (depamor/ppnenet): level + de-trended transforms ----

# aging charge-rate level (depamor / PP&E) — the canonical aging proxy
def f34iw_f34_impairment_writedown_risk_aging_0d_base_v001_signal(depamor, ppnenet):
    b = _aging(depamor, ppnenet)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate z-scored vs its own year (de-trended aging extremity)
def f34iw_f34_impairment_writedown_risk_agingz_252d_base_v002_signal(depamor, ppnenet):
    b = _z(_aging(depamor, ppnenet), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate percentile rank vs its two-year history
def f34iw_f34_impairment_writedown_risk_agingrank_504d_base_v003_signal(depamor, ppnenet):
    b = _rank(_aging(depamor, ppnenet), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarterly momentum of the aging rate (accelerating depreciation drag)
def f34iw_f34_impairment_writedown_risk_agingmom_63d_base_v004_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year momentum of the aging rate
def f34iw_f34_impairment_writedown_risk_agingmom_126d_base_v005_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in the aging rate
def f34iw_f34_impairment_writedown_risk_aginggr_252d_base_v006_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate term structure (short mean minus long mean)
def f34iw_f34_impairment_writedown_risk_agingterm_63v504_base_v007_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = _mean(s, 63) - _mean(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion (rolling std) of the aging rate — instability of the charge regime
def f34iw_f34_impairment_writedown_risk_agingdisp_252d_base_v008_signal(depamor, ppnenet):
    b = _std(_aging(depamor, ppnenet), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate minus its slow EMA (charge-rate displacement)
def f34iw_f34_impairment_writedown_risk_agingdispema_126d_base_v009_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s - s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt of aging deviation from its year mean (bounded charge surprise)
def f34iw_f34_impairment_writedown_risk_agingsignmag_252d_base_v010_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    d = s - _mean(s, 252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest run (as a fraction of a year) the aging rate stayed above its 252d median
def f34iw_f34_impairment_writedown_risk_aginghotpersist_252d_base_v011_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    med = s.rolling(252, min_periods=126).median()
    hot = (s > med).astype(float)
    b = hot.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate range position within its own 504d high-low band (0=floor, 1=ceiling)
def f34iw_f34_impairment_writedown_risk_agingbandpos_504d_base_v012_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    hi = _rmax(s, 504)
    lo = _rmin(s, 504)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed YEAR-over-year aging change (bounded long-horizon acceleration)
def f34iw_f34_impairment_writedown_risk_agingtanh_252d_base_v013_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    chg = s - s.shift(252)
    b = np.tanh(40.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the aging rate is above its 252d minimum (rise off the charge floor),
# tanh-bounded so a near-zero floor cannot produce outliers
def f34iw_f34_impairment_writedown_risk_agingofffloor_252d_base_v014_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    lo = _rmin(s, 252)
    b = np.tanh(s / lo.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTANGIBLE/GOODWILL AMORTIZATION RATE (depamor / intangibles) ----

# amortization rate of the soft book (D&A per unit of intangibles)
def f34iw_f34_impairment_writedown_risk_amortrate_0d_base_v015_signal(depamor, intangibles):
    b = _amort_rate(depamor, intangibles)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate z-scored vs its own year (run-off speed extremity)
def f34iw_f34_impairment_writedown_risk_amortratez_252d_base_v016_signal(depamor, intangibles):
    b = _z(_amort_rate(depamor, intangibles), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate percentile rank vs two years
def f34iw_f34_impairment_writedown_risk_amortraterank_504d_base_v017_signal(depamor, intangibles):
    b = _rank(_amort_rate(depamor, intangibles), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate vs its own 504d max (run-off speed relative to its historic peak)
def f34iw_f34_impairment_writedown_risk_amortratepeak_504d_base_v018_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    pk = _rmax(s, 504)
    b = s / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarterly momentum of amortization rate
def f34iw_f34_impairment_writedown_risk_amortratemom_63d_base_v019_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of amortization rate (volatile run-off assumptions)
def f34iw_f34_impairment_writedown_risk_amortratedisp_252d_base_v020_signal(depamor, intangibles):
    b = _std(_amort_rate(depamor, intangibles), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stale-goodwill regime: fraction of two years amort-rate sat in its LOWER tercile
def f34iw_f34_impairment_writedown_risk_stalegw_504d_base_v021_signal(depamor, intangibles):
    r = _rank(_amort_rate(depamor, intangibles), 504) + 0.5
    b = (r <= 0.3333).astype(float).rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-rate vs its slow EMA (run-off displacement)
def f34iw_f34_impairment_writedown_risk_amortratedispema_126d_base_v022_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = s - s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTANGIBLE/GOODWILL BUILD & WRITEDOWN DETECTION (temporal, not static share) ----

# intangible-book drop from its trailing 504d peak (writedown shows as a peak gap)
def f34iw_f34_impairment_writedown_risk_intpeakdist_504d_base_v023_signal(intangibles):
    pk = _rmax(intangibles, 504)
    b = intangibles / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far the 1260d intangible peak sits above the current 252d low (multi-year span)
def f34iw_f34_impairment_writedown_risk_intpeakspan_1260d_base_v024_signal(intangibles):
    pk = _rmax(intangibles, 1260)
    lo = _rmin(intangibles, 252)
    b = np.log(pk.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarterly intangible-book build pace, tanh-bounded (goodwill build, outlier-robust)
def f34iw_f34_impairment_writedown_risk_intgr_63d_base_v025_signal(intangibles):
    b = np.tanh(4.0 * _growth(intangibles, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year log growth of the intangible book
def f34iw_f34_impairment_writedown_risk_intgr_252d_base_v026_signal(intangibles):
    b = _growth(intangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of intangible-book build pace (qoq build speeding up), tanh-bounded
def f34iw_f34_impairment_writedown_risk_intgracc_63d_base_v027_signal(intangibles):
    g = _growth(intangibles, 63)
    b = np.tanh(4.0 * (g - g.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of yoy intangible growth (extreme goodwill build)
def f34iw_f34_impairment_writedown_risk_intgrrank_504d_base_v028_signal(intangibles):
    b = _rank(_growth(intangibles, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single qoq intangible drop over the last two years (impairment-event proxy)
def f34iw_f34_impairment_writedown_risk_intmaxdrop_504d_base_v029_signal(intangibles):
    qchg = intangibles / intangibles.shift(63).replace(0, np.nan) - 1.0
    b = qchg.rolling(504, min_periods=252).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative downside-only intangible moves over two years (total realized run-off depth)
def f34iw_f34_impairment_writedown_risk_intdowncum_504d_base_v030_signal(intangibles):
    qchg = intangibles / intangibles.shift(63).replace(0, np.nan) - 1.0
    down = qchg.clip(upper=0.0)
    b = down.rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# UNAMORTIZED BUILD: intangible growth in excess of amortization run-off (yoy)
def f34iw_f34_impairment_writedown_risk_unamortbuild_252d_base_v031_signal(intangibles, depamor):
    b = _unamortized_build(intangibles, depamor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unamortized build over a half-year
def f34iw_f34_impairment_writedown_risk_unamortbuild_126d_base_v032_signal(intangibles, depamor):
    b = _unamortized_build(intangibles, depamor, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unamortized build z-scored vs its own year (extreme pile-up)
def f34iw_f34_impairment_writedown_risk_unamortbuildz_252d_base_v033_signal(intangibles, depamor):
    b = _z(_unamortized_build(intangibles, depamor, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years intangibles grew faster than D&A (sustained pile-up regime)
def f34iw_f34_impairment_writedown_risk_buildregime_504d_base_v034_signal(intangibles, depamor):
    d = _unamortized_build(intangibles, depamor, 63)
    up = (d > 0).astype(float)
    b = up.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-book build inflection: qoq build now vs a year ago, tanh-bounded
def f34iw_f34_impairment_writedown_risk_intgrinflect_252d_base_v035_signal(intangibles):
    g = _growth(intangibles, 63)
    b = np.tanh(4.0 * (g - g.shift(252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- D&A CHARGE INTENSITY vs DENOMINATORS OTHER THAN PP&E (cross-base aging) ----

# D&A / assets charge intensity (total non-cash drag against the whole sheet)
def f34iw_f34_impairment_writedown_risk_depassets_0d_base_v036_signal(depamor, assets):
    b = depamor / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A / assets z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_depassetsz_252d_base_v037_signal(depamor, assets):
    b = _z(depamor / assets.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A / equity (non-cash charge relative to the book cushion that absorbs writedowns)
def f34iw_f34_impairment_writedown_risk_depeq_0d_base_v038_signal(depamor, equity):
    b = depamor / equity.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A / equity z-scored vs its own year
def f34iw_f34_impairment_writedown_risk_depeqz_252d_base_v039_signal(depamor, equity):
    b = _z(depamor / equity.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log growth of the D&A charge (accelerating non-cash drag)
def f34iw_f34_impairment_writedown_risk_depgr_252d_base_v040_signal(depamor):
    b = _growth(depamor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the D&A charge (jerk of the charge level)
def f34iw_f34_impairment_writedown_risk_depgracc_63d_base_v041_signal(depamor):
    g = _growth(depamor, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A charge vs its own 504d peak (charge running at a historic top)
def f34iw_f34_impairment_writedown_risk_deppeak_504d_base_v042_signal(depamor):
    pk = _rmax(depamor, 504)
    b = depamor / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/assets term structure (short minus long mean) — charge-intensity drift
def f34iw_f34_impairment_writedown_risk_depassetsterm_63v504_base_v043_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    b = _mean(s, 63) - _mean(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- D&A CHARGE vs TANGIBLE BASE (charge intensity on the hard book; depamor-driven) ----
# NOTE: these use the depamor CHARGE FLOW (which no sibling uses) against tangibles, so
# they do not reduce to the static intangibles/tangibles soft-mix owned by f42 (softhardmix).

# charge coverage of fresh intangible build: one year of D&A vs the yoy increase in
# intangibles (how well newly-added goodwill is being amortized; low -> un-charged build),
# tanh-bounded for robustness
def f34iw_f34_impairment_writedown_risk_buildchargecover_252d_base_v044_signal(depamor, intangibles):
    add = (intangibles - intangibles.shift(252)).clip(lower=0.0)
    b = np.tanh(depamor / (add + depamor).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate term structure (short minus long mean) — run-off-rate drift on the soft book
def f34iw_f34_impairment_writedown_risk_amortterm_63v504_base_v045_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = _mean(s, 63) - _mean(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate vs its own 504d MIN (run-off rate rising off its historic floor)
def f34iw_f34_impairment_writedown_risk_amortofffloor_504d_base_v046_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    lo = _rmin(s, 504)
    b = s / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/equity percentile rank vs two years (charge-vs-book-cushion extremity)
def f34iw_f34_impairment_writedown_risk_depeqrank_504d_base_v047_signal(depamor, equity):
    b = _rank(depamor / equity.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt of amortization-rate deviation from its year mean (bounded run-off surprise)
def f34iw_f34_impairment_writedown_risk_amortsignmag_252d_base_v048_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    d = s - _mean(s, 252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed yoy change in amortization rate (bounded run-off acceleration)
def f34iw_f34_impairment_writedown_risk_amorttanh_252d_base_v049_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    chg = s - s.shift(252)
    b = np.tanh(20.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year the amortization rate sat in its upper tercile (heavy-run-off regime)
def f34iw_f34_impairment_writedown_risk_amorthi_252d_base_v050_signal(depamor, intangibles):
    r = _rank(_amort_rate(depamor, intangibles), 504) + 0.5
    b = (r >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- PP&E REINVESTMENT GAP (growth vs charge) — capacity vs decay ----

# reinvestment gap (yoy): PP&E growth minus its aging charge
def f34iw_f34_impairment_writedown_risk_reinvgap_252d_base_v051_signal(ppnenet, depamor):
    b = _reinvest_gap(ppnenet, depamor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment gap (half-year)
def f34iw_f34_impairment_writedown_risk_reinvgap_126d_base_v052_signal(ppnenet, depamor):
    b = _reinvest_gap(ppnenet, depamor, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment gap z-scored vs its own year (extreme under/over-investment)
def f34iw_f34_impairment_writedown_risk_reinvgapz_252d_base_v053_signal(ppnenet, depamor):
    b = _z(_reinvest_gap(ppnenet, depamor, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years PP&E shrank net of depreciation (decaying-base regime)
def f34iw_f34_impairment_writedown_risk_decaybase_504d_base_v054_signal(ppnenet, depamor):
    d = _reinvest_gap(ppnenet, depamor, 63)
    dn = (d < 0).astype(float)
    b = dn.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year momentum of the charge-led decay gap (decay regime accelerating)
def f34iw_f34_impairment_writedown_risk_reinvgapmom_126d_base_v055_signal(ppnenet, depamor):
    d = _reinvest_gap(ppnenet, depamor, 252)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- AGING x INTANGIBLE / COMPOUND WRITEDOWN-RISK INTERACTIONS ----

# aging charge x amortization rate (old hard base AND fast-running soft book)
def f34iw_f34_impairment_writedown_risk_agingxamort_0d_base_v056_signal(depamor, ppnenet, intangibles):
    b = _aging(depamor, ppnenet) * _amort_rate(depamor, intangibles)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging charge x intangible run-off horizon weakness (old hard base + slow soft run-off)
def f34iw_f34_impairment_writedown_risk_agingxstale_0d_base_v057_signal(depamor, ppnenet, intangibles):
    ag = _aging(depamor, ppnenet)
    slow = (-_z(_amort_rate(depamor, intangibles), 252)).clip(lower=0.0)
    b = ag * slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unamortized build x aging-rate momentum (soft book piling up while the charge accelerates)
def f34iw_f34_impairment_writedown_risk_buildxagingmom_0d_base_v058_signal(intangibles, depamor, ppnenet):
    ag = _aging(depamor, ppnenet)
    b = _unamortized_build(intangibles, depamor, 126) * (ag - ag.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# whether the intangible book is currently below its own 252d average (carry already cut)
def f34iw_f34_impairment_writedown_risk_intbelowavg_252d_base_v059_signal(intangibles):
    avg = _mean(intangibles, 252)
    b = intangibles / avg.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest fraction of the last year the intangible book held below its 252d high (stuck-down)
def f34iw_f34_impairment_writedown_risk_intstuckdown_252d_base_v060_signal(intangibles):
    hi = _rmax(intangibles, 252)
    down = (intangibles < hi * 0.98).astype(float)
    b = down.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate momentum x goodwill-build pace (both charge AND soft book accelerating)
def f34iw_f34_impairment_writedown_risk_agingmomxbuild_0d_base_v061_signal(depamor, ppnenet, intangibles):
    ag = _aging(depamor, ppnenet)
    b = (ag - ag.shift(126)) * _growth(intangibles, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DEPAMOR vs INTANGIBLE-BUILD DIVERGENCE (charge not keeping up with the soft book) ----

# divergence sign-regime: fraction of last year intangibles grew while D&A shrank
def f34iw_f34_impairment_writedown_risk_chargelagregime_252d_base_v062_signal(intangibles, depamor):
    ig = intangibles > intangibles.shift(63)
    dd = depamor < depamor.shift(63)
    div = (ig & dd).astype(float)
    b = div.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# correlation-free build-vs-charge wedge: 252d intangible growth scaled by (1 - amort rank)
def f34iw_f34_impairment_writedown_risk_buildstalewedge_504d_base_v063_signal(intangibles, depamor):
    g = _growth(intangibles, 252)
    stale = (0.5 - _rank(_amort_rate(depamor, intangibles), 504))
    b = g * stale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- D&A-SCALED TRAJECTORY REGIMES / SURPRISES ----

# fraction of last year the amortization rate fell qoq (run-off slowing regime)
def f34iw_f34_impairment_writedown_risk_amortslowstreak_252d_base_v064_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    dn = (s < s.shift(63)).astype(float)
    b = dn.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/assets vs its own 504d peak (whole-sheet charge intensity at a historic high)
def f34iw_f34_impairment_writedown_risk_depassetspeak_504d_base_v065_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    pk = _rmax(s, 504)
    b = s / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/assets vs its 504d min (charge rising off its floor)
def f34iw_f34_impairment_writedown_risk_depassetsofffloor_504d_base_v066_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    lo = _rmin(s, 504)
    b = s / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt of D&A/equity deviation from its year mean (bounded charge surprise)
def f34iw_f34_impairment_writedown_risk_depeqsignmag_252d_base_v067_signal(depamor, equity):
    s = depamor / equity.replace(0, np.nan)
    d = s - _mean(s, 252)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTANGIBLE-BOOK SHAPE / EROSION TRAJECTORY ----

# fraction of two years the intangible book fell qoq (sustained erosion regime)
def f34iw_f34_impairment_writedown_risk_interodestreak_504d_base_v068_signal(intangibles):
    dn = (intangibles < intangibles.shift(63)).astype(float)
    b = dn.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# months since the intangible book last made a fresh 504d high (staleness of the carry)
def f34iw_f34_impairment_writedown_risk_intstalehigh_504d_base_v069_signal(intangibles):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = intangibles.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-growth dispersion (volatile goodwill build/erosion path)
def f34iw_f34_impairment_writedown_risk_intgrdisp_252d_base_v070_signal(intangibles):
    g = (intangibles / intangibles.shift(63).replace(0, np.nan) - 1.0).clip(-0.5, 0.5)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- AGING vs CROSS-BASE CHARGE SPREADS ----

# aging-charge acceleration relative to the raw D&A-charge growth (PP&E base shrinking
# faster than the charge itself = the denominator, not the charge, is driving aging up)
def f34iw_f34_impairment_writedown_risk_agingaccelsrc_252d_base_v071_signal(depamor, ppnenet):
    ag = _aging(depamor, ppnenet)
    b = (ag - ag.shift(126)) - _growth(depamor, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging charge minus amortization rate, z-scored (hard vs soft run-off tilt, de-trended)
def f34iw_f34_impairment_writedown_risk_hardsofttiltz_252d_base_v072_signal(depamor, ppnenet, intangibles):
    s = _aging(depamor, ppnenet) - _amort_rate(depamor, intangibles)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in D&A/equity (charge eating into the book cushion over time)
def f34iw_f34_impairment_writedown_risk_depeqgr_252d_base_v073_signal(depamor, equity):
    s = depamor / equity.replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amort-rate momentum x aging momentum (soft run-off and hard charge co-accelerating)
def f34iw_f34_impairment_writedown_risk_amortxagingmom_63d_base_v074_signal(depamor, intangibles, ppnenet):
    am = _amort_rate(depamor, intangibles)
    ag = _aging(depamor, ppnenet)
    b = (am - am.shift(63)) * (ag - ag.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite writedown-pressure: stale soft book + decaying hard base (regime blend)
def f34iw_f34_impairment_writedown_risk_writepress_252d_base_v075_signal(depamor, intangibles, ppnenet):
    stale = (-_z(_amort_rate(depamor, intangibles), 252)).clip(lower=0.0)
    decay = _z(_aging(depamor, ppnenet), 252).clip(lower=0.0)
    b = stale + decay
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34iw_f34_impairment_writedown_risk_aging_0d_base_v001_signal,
    f34iw_f34_impairment_writedown_risk_agingz_252d_base_v002_signal,
    f34iw_f34_impairment_writedown_risk_agingrank_504d_base_v003_signal,
    f34iw_f34_impairment_writedown_risk_agingmom_63d_base_v004_signal,
    f34iw_f34_impairment_writedown_risk_agingmom_126d_base_v005_signal,
    f34iw_f34_impairment_writedown_risk_aginggr_252d_base_v006_signal,
    f34iw_f34_impairment_writedown_risk_agingterm_63v504_base_v007_signal,
    f34iw_f34_impairment_writedown_risk_agingdisp_252d_base_v008_signal,
    f34iw_f34_impairment_writedown_risk_agingdispema_126d_base_v009_signal,
    f34iw_f34_impairment_writedown_risk_agingsignmag_252d_base_v010_signal,
    f34iw_f34_impairment_writedown_risk_aginghotpersist_252d_base_v011_signal,
    f34iw_f34_impairment_writedown_risk_agingbandpos_504d_base_v012_signal,
    f34iw_f34_impairment_writedown_risk_agingtanh_252d_base_v013_signal,
    f34iw_f34_impairment_writedown_risk_agingofffloor_252d_base_v014_signal,
    f34iw_f34_impairment_writedown_risk_amortrate_0d_base_v015_signal,
    f34iw_f34_impairment_writedown_risk_amortratez_252d_base_v016_signal,
    f34iw_f34_impairment_writedown_risk_amortraterank_504d_base_v017_signal,
    f34iw_f34_impairment_writedown_risk_amortratepeak_504d_base_v018_signal,
    f34iw_f34_impairment_writedown_risk_amortratemom_63d_base_v019_signal,
    f34iw_f34_impairment_writedown_risk_amortratedisp_252d_base_v020_signal,
    f34iw_f34_impairment_writedown_risk_stalegw_504d_base_v021_signal,
    f34iw_f34_impairment_writedown_risk_amortratedispema_126d_base_v022_signal,
    f34iw_f34_impairment_writedown_risk_intpeakdist_504d_base_v023_signal,
    f34iw_f34_impairment_writedown_risk_intpeakspan_1260d_base_v024_signal,
    f34iw_f34_impairment_writedown_risk_intgr_63d_base_v025_signal,
    f34iw_f34_impairment_writedown_risk_intgr_252d_base_v026_signal,
    f34iw_f34_impairment_writedown_risk_intgracc_63d_base_v027_signal,
    f34iw_f34_impairment_writedown_risk_intgrrank_504d_base_v028_signal,
    f34iw_f34_impairment_writedown_risk_intmaxdrop_504d_base_v029_signal,
    f34iw_f34_impairment_writedown_risk_intdowncum_504d_base_v030_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuild_252d_base_v031_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuild_126d_base_v032_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuildz_252d_base_v033_signal,
    f34iw_f34_impairment_writedown_risk_buildregime_504d_base_v034_signal,
    f34iw_f34_impairment_writedown_risk_intgrinflect_252d_base_v035_signal,
    f34iw_f34_impairment_writedown_risk_depassets_0d_base_v036_signal,
    f34iw_f34_impairment_writedown_risk_depassetsz_252d_base_v037_signal,
    f34iw_f34_impairment_writedown_risk_depeq_0d_base_v038_signal,
    f34iw_f34_impairment_writedown_risk_depeqz_252d_base_v039_signal,
    f34iw_f34_impairment_writedown_risk_depgr_252d_base_v040_signal,
    f34iw_f34_impairment_writedown_risk_depgracc_63d_base_v041_signal,
    f34iw_f34_impairment_writedown_risk_deppeak_504d_base_v042_signal,
    f34iw_f34_impairment_writedown_risk_depassetsterm_63v504_base_v043_signal,
    f34iw_f34_impairment_writedown_risk_buildchargecover_252d_base_v044_signal,
    f34iw_f34_impairment_writedown_risk_amortterm_63v504_base_v045_signal,
    f34iw_f34_impairment_writedown_risk_amortofffloor_504d_base_v046_signal,
    f34iw_f34_impairment_writedown_risk_depeqrank_504d_base_v047_signal,
    f34iw_f34_impairment_writedown_risk_amortsignmag_252d_base_v048_signal,
    f34iw_f34_impairment_writedown_risk_amorttanh_252d_base_v049_signal,
    f34iw_f34_impairment_writedown_risk_amorthi_252d_base_v050_signal,
    f34iw_f34_impairment_writedown_risk_reinvgap_252d_base_v051_signal,
    f34iw_f34_impairment_writedown_risk_reinvgap_126d_base_v052_signal,
    f34iw_f34_impairment_writedown_risk_reinvgapz_252d_base_v053_signal,
    f34iw_f34_impairment_writedown_risk_decaybase_504d_base_v054_signal,
    f34iw_f34_impairment_writedown_risk_reinvgapmom_126d_base_v055_signal,
    f34iw_f34_impairment_writedown_risk_agingxamort_0d_base_v056_signal,
    f34iw_f34_impairment_writedown_risk_agingxstale_0d_base_v057_signal,
    f34iw_f34_impairment_writedown_risk_buildxagingmom_0d_base_v058_signal,
    f34iw_f34_impairment_writedown_risk_intbelowavg_252d_base_v059_signal,
    f34iw_f34_impairment_writedown_risk_intstuckdown_252d_base_v060_signal,
    f34iw_f34_impairment_writedown_risk_agingmomxbuild_0d_base_v061_signal,
    f34iw_f34_impairment_writedown_risk_chargelagregime_252d_base_v062_signal,
    f34iw_f34_impairment_writedown_risk_buildstalewedge_504d_base_v063_signal,
    f34iw_f34_impairment_writedown_risk_amortslowstreak_252d_base_v064_signal,
    f34iw_f34_impairment_writedown_risk_depassetspeak_504d_base_v065_signal,
    f34iw_f34_impairment_writedown_risk_depassetsofffloor_504d_base_v066_signal,
    f34iw_f34_impairment_writedown_risk_depeqsignmag_252d_base_v067_signal,
    f34iw_f34_impairment_writedown_risk_interodestreak_504d_base_v068_signal,
    f34iw_f34_impairment_writedown_risk_intstalehigh_504d_base_v069_signal,
    f34iw_f34_impairment_writedown_risk_intgrdisp_252d_base_v070_signal,
    f34iw_f34_impairment_writedown_risk_agingaccelsrc_252d_base_v071_signal,
    f34iw_f34_impairment_writedown_risk_hardsofttiltz_252d_base_v072_signal,
    f34iw_f34_impairment_writedown_risk_depeqgr_252d_base_v073_signal,
    f34iw_f34_impairment_writedown_risk_amortxagingmom_63d_base_v074_signal,
    f34iw_f34_impairment_writedown_risk_writepress_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_IMPAIRMENT_WRITEDOWN_RISK_REGISTRY_001_075 = REGISTRY


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

    # impairment / writedown-risk fundamentals.
    # assets is the largest aggregate; tangibles + intangibles are subsets of assets;
    # ppnenet is a subset of tangibles; equity allows negative (post-writedown distress);
    # depamor is the depreciation/amortization charge (drives the aging axis).
    assets = _fund(3401, base=1.4e9, drift=0.010, vol=0.06).rename("assets")
    _tang_raw = _fund(3402, base=8.0e8, drift=0.006, vol=0.08)
    tangibles = pd.Series(np.minimum(_tang_raw.values, 0.95 * assets.values),
                          name="tangibles")
    _ppe_raw = _fund(3403, base=5.0e8, drift=0.012, vol=0.11)
    ppnenet = pd.Series(np.minimum(_ppe_raw.values, 0.97 * tangibles.values),
                        name="ppnenet")
    _intang_raw = _fund(3404, base=3.0e8, drift=0.020, vol=0.14)
    intangibles = pd.Series(np.minimum(_intang_raw.values, 0.9 * (assets.values - tangibles.values + 1.0)),
                            name="intangibles")
    equity = _fund(3405, base=6.0e8, drift=0.004, vol=0.12, allow_neg=True).rename("equity")
    depamor = _fund(3406, base=6.0e7, drift=0.010, vol=0.16).rename("depamor")

    cols = {"intangibles": intangibles, "ppnenet": ppnenet, "assets": assets,
            "equity": equity, "tangibles": tangibles, "depamor": depamor}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("intangibles", "ppnenet", "assets", "equity", "tangibles", "depamor") for c in meta["inputs"]), name
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

    print("OK f34_impairment_writedown_risk_base_001_075_claude: %d features pass" % n_features)
