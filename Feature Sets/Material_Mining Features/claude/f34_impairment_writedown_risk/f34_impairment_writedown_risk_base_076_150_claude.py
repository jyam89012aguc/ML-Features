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


# ===== folder domain primitives (impairment / writedown risk) — see 001_075 design note =====
# Built on DEPAMOR (depreciation/amortization charge) AGING dynamics and INTANGIBLE/GOODWILL
# DRAG temporal constructs. Avoids static PP&E/assets & tangibles/assets (f30), equity/assets
# (f42/f22), intangibles/equity & intangibles/ppnenet & intangibles/tangibles (f42/f30).
# Never pairs a ratio with its own reciprocal; depamor is always kept in a non-cancelling spot.
def _aging(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan)


def _amort_rate(depamor, intangibles):
    return depamor / intangibles.replace(0, np.nan)


def _unamortized_build(intangibles, depamor, w):
    return _growth(intangibles, w) - _growth(depamor, w)




# ============================================================
# ---- AGING (depamor/PP&E): additional windows / facets ----

# aging rate z-scored vs its own half-year (faster-adapting aging extremity)
def f34iw_f34_impairment_writedown_risk_agingz_126d_base_v076_signal(depamor, ppnenet):
    b = _z(_aging(depamor, ppnenet), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate EMA (persistent charge level)
def f34iw_f34_impairment_writedown_risk_agingema_63d_base_v077_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate percentile rank vs its five-year history (long-horizon extremity)
def f34iw_f34_impairment_writedown_risk_agingrank_1260d_base_v078_signal(depamor, ppnenet):
    b = _rank(_aging(depamor, ppnenet), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate month-over-month change (short charge impulse)
def f34iw_f34_impairment_writedown_risk_agingmom_21d_base_v079_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s - s.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate dispersion over two years (long charge-regime instability)
def f34iw_f34_impairment_writedown_risk_agingdisp_504d_base_v080_signal(depamor, ppnenet):
    b = _std(_aging(depamor, ppnenet), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate vs its own 252d mean (current charge vs typical recent charge)
def f34iw_f34_impairment_writedown_risk_agingvsmean_252d_base_v081_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s / _mean(s, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of aging-rate qoq increases over the last year (frequency of charge step-ups)
def f34iw_f34_impairment_writedown_risk_agingupfreq_252d_base_v082_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    up = (s > s.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate two-year change (long-horizon charge drift)
def f34iw_f34_impairment_writedown_risk_aginggr_504d_base_v083_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = s - s.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate vs its slow EMA, ranked (charge displacement extremity)
def f34iw_f34_impairment_writedown_risk_agingdisprank_504d_base_v084_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    disp = s - s.ewm(span=126, min_periods=42).mean()
    b = _rank(disp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- AMORTIZATION RATE (depamor/intangibles): additional windows / facets ----

# amortization rate z-scored vs its own half-year
def f34iw_f34_impairment_writedown_risk_amortratez_126d_base_v085_signal(depamor, intangibles):
    b = _z(_amort_rate(depamor, intangibles), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate EMA (persistent run-off level)
def f34iw_f34_impairment_writedown_risk_amortrateema_63d_base_v086_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization rate percentile rank vs five years (long-horizon run-off extremity)
def f34iw_f34_impairment_writedown_risk_amortraterank_1260d_base_v087_signal(depamor, intangibles):
    b = _rank(_amort_rate(depamor, intangibles), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-rate two-year change, z-scored (long-horizon run-off drift extremity)
def f34iw_f34_impairment_writedown_risk_amortrategrz_504d_base_v088_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = _z(s - s.shift(504), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-rate dispersion over two years (long run-off-regime instability)
def f34iw_f34_impairment_writedown_risk_amortratedisp_504d_base_v089_signal(depamor, intangibles):
    b = _std(_amort_rate(depamor, intangibles), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years amort-rate sat in its UPPER tercile (heavy run-off regime, 2y window)
def f34iw_f34_impairment_writedown_risk_amorthi_504d_base_v090_signal(depamor, intangibles):
    r = _rank(_amort_rate(depamor, intangibles), 504) + 0.5
    b = (r >= 0.6667).astype(float).rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amortization-rate month-over-month change (short run-off impulse)
def f34iw_f34_impairment_writedown_risk_amortratemom_21d_base_v091_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = s - s.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest fraction of the last year amort-rate stayed below its 252d median (slow-run-off run)
def f34iw_f34_impairment_writedown_risk_amortcoldpersist_252d_base_v092_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    med = s.rolling(252, min_periods=126).median()
    cold = (s < med).astype(float)
    b = cold.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTANGIBLE/GOODWILL BUILD & WRITEDOWN DETECTION (temporal) ----

# half-year intangible-book build pace, tanh-bounded
def f34iw_f34_impairment_writedown_risk_intgr_126d_base_v093_signal(intangibles):
    b = np.tanh(4.0 * _growth(intangibles, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# month-over-month intangible build pace, tanh-bounded (fast goodwill moves)
def f34iw_f34_impairment_writedown_risk_intgr_21d_base_v094_signal(intangibles):
    b = np.tanh(6.0 * _growth(intangibles, 21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible book vs its own 252d high (carry below the recent peak = post-writedown)
def f34iw_f34_impairment_writedown_risk_intpeakdist_252d_base_v095_signal(intangibles):
    pk = _rmax(intangibles, 252)
    b = intangibles / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible book range position within its own 252d high-low band (0=trough,1=peak)
def f34iw_f34_impairment_writedown_risk_intbandpos_252d_base_v096_signal(intangibles):
    hi = _rmax(intangibles, 252)
    lo = _rmin(intangibles, 252)
    b = (intangibles - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of intangible new-2y-lows over the last year (repeated fresh writedown lows)
def f34iw_f34_impairment_writedown_risk_intnewlowcnt_252d_base_v097_signal(intangibles):
    lo = _rmin(intangibles, 504)
    is_low = (intangibles <= lo * 1.0001).astype(float)
    b = is_low.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single qoq intangible drop over the LAST YEAR (recent impairment-event proxy)
def f34iw_f34_impairment_writedown_risk_intmaxdrop_252d_base_v098_signal(intangibles):
    qchg = (intangibles / intangibles.shift(63).replace(0, np.nan) - 1.0).clip(-1.0, 1.0)
    b = qchg.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible build pace percentile rank over a half-year window (medium-horizon extremity)
def f34iw_f34_impairment_writedown_risk_intgrrank_252d_base_v099_signal(intangibles):
    g = (intangibles / intangibles.shift(63).replace(0, np.nan) - 1.0).clip(-0.5, 0.5)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years the intangible book made a fresh 252d high (sustained build regime)
def f34iw_f34_impairment_writedown_risk_intbuildregime_504d_base_v100_signal(intangibles):
    hi = _rmax(intangibles, 252)
    is_high = (intangibles >= hi * 0.9999).astype(float)
    b = is_high.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- UNAMORTIZED BUILD (intangible growth net of D&A growth): more windows ----

# unamortized build over a quarter
def f34iw_f34_impairment_writedown_risk_unamortbuild_63d_base_v101_signal(intangibles, depamor):
    b = np.tanh(3.0 * _unamortized_build(intangibles, depamor, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unamortized build over two years (long-horizon pile-up)
def f34iw_f34_impairment_writedown_risk_unamortbuild_504d_base_v102_signal(intangibles, depamor):
    b = np.tanh(2.0 * _unamortized_build(intangibles, depamor, 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unamortized-build percentile rank (extremity of the intangible-vs-charge wedge)
def f34iw_f34_impairment_writedown_risk_unamortbuildrank_504d_base_v103_signal(intangibles, depamor):
    b = _rank(_unamortized_build(intangibles, depamor, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of the unamortized-build wedge (instability of charge-vs-build coverage)
def f34iw_f34_impairment_writedown_risk_unamortbuilddisp_252d_base_v104_signal(intangibles, depamor):
    b = _std(_unamortized_build(intangibles, depamor, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- D&A CHARGE LEVEL (depamor) and CHARGE vs ASSETS / EQUITY: more facets ----

# D&A charge position within its own 504d high-low band (0=trough,1=peak)
def f34iw_f34_impairment_writedown_risk_chargebandpos_504d_base_v105_signal(depamor):
    hi = _rmax(depamor, 504)
    lo = _rmin(depamor, 504)
    b = (depamor - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A charge two-year log-growth (long-horizon charge build)
def f34iw_f34_impairment_writedown_risk_depgr_504d_base_v106_signal(depamor):
    b = _growth(depamor, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A charge vs its own 252d mean (charge level vs recent normal)
def f34iw_f34_impairment_writedown_risk_depvsmean_252d_base_v107_signal(depamor):
    b = depamor / _mean(depamor, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/assets month-over-month change (short whole-sheet charge impulse)
def f34iw_f34_impairment_writedown_risk_depassetsmom_63d_base_v108_signal(depamor, assets):
    s = depamor / assets.replace(0, np.nan)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/assets percentile rank vs two years (whole-sheet charge extremity)
def f34iw_f34_impairment_writedown_risk_depassetsrank_504d_base_v109_signal(depamor, assets):
    b = _rank(depamor / assets.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/assets dispersion (instability of whole-sheet charge intensity)
def f34iw_f34_impairment_writedown_risk_depassetsdisp_252d_base_v110_signal(depamor, assets):
    b = _std(depamor / assets.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/equity month-over-month change (short charge-vs-cushion impulse)
def f34iw_f34_impairment_writedown_risk_depeqmom_63d_base_v111_signal(depamor, equity):
    s = depamor / equity.replace(0, np.nan)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/equity dispersion (instability of the charge-vs-cushion ratio)
def f34iw_f34_impairment_writedown_risk_depeqdisp_252d_base_v112_signal(depamor, equity):
    b = _std(depamor / equity.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A/equity z-scored vs its own two years (longer-horizon charge-vs-cushion extremity)
def f34iw_f34_impairment_writedown_risk_depeqz_504d_base_v113_signal(depamor, equity):
    b = _z(depamor / equity.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTANGIBLE BOOK EROSION / TRAJECTORY REGIMES ----

# fraction of the last year the intangible book fell qoq (recent erosion regime)
def f34iw_f34_impairment_writedown_risk_interodestreak_252d_base_v114_signal(intangibles):
    dn = (intangibles < intangibles.shift(63)).astype(float)
    b = dn.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative downside-only intangible moves over the LAST YEAR (recent realized run-off depth)
def f34iw_f34_impairment_writedown_risk_intdowncum_252d_base_v115_signal(intangibles):
    qchg = (intangibles / intangibles.shift(63).replace(0, np.nan) - 1.0).clip(-1.0, 0.0)
    b = qchg.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# months since the intangible book last made a fresh 252d high (recent carry staleness)
def f34iw_f34_impairment_writedown_risk_intstalehigh_252d_base_v116_signal(intangibles):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = intangibles.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-book drawdown depth from its 1260d peak weighted by the amort rate (deep+fast)
def f34iw_f34_impairment_writedown_risk_intdderode_1260d_base_v117_signal(intangibles, depamor):
    pk = _rmax(intangibles, 1260)
    dd = (intangibles / pk.replace(0, np.nan) - 1.0)
    b = dd.abs() * _amort_rate(depamor, intangibles)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- AGING / AMORT CROSS-FACETS & INTERACTIONS (additional) ----

# aging-rate momentum x amort-rate momentum (hard charge and soft run-off co-accelerating, 126d)
def f34iw_f34_impairment_writedown_risk_agingxamortmom_126d_base_v118_signal(depamor, ppnenet, intangibles):
    ag = _aging(depamor, ppnenet)
    am = _amort_rate(depamor, intangibles)
    b = (ag - ag.shift(126)) * (am - am.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate z x intangible-build pace (elevated hard charge while the soft book inflates)
def f34iw_f34_impairment_writedown_risk_agingzxbuild_0d_base_v119_signal(depamor, ppnenet, intangibles):
    b = _z(_aging(depamor, ppnenet), 252) * np.tanh(4.0 * _growth(intangibles, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amort-rate z minus aging-rate z (relative de-trended run-off, soft vs hard)
def f34iw_f34_impairment_writedown_risk_softhardzspread_252d_base_v120_signal(depamor, intangibles, ppnenet):
    b = _z(_amort_rate(depamor, intangibles), 252) - _z(_aging(depamor, ppnenet), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate z x amort-rate z (joint extremity of hard and soft run-off rates)
def f34iw_f34_impairment_writedown_risk_jointrunoffz_252d_base_v121_signal(depamor, ppnenet, intangibles):
    b = _z(_aging(depamor, ppnenet), 252) * _z(_amort_rate(depamor, intangibles), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unamortized-build x aging-rate z (soft book piling up while the hard charge is elevated)
def f34iw_f34_impairment_writedown_risk_buildxagingz_0d_base_v122_signal(intangibles, depamor, ppnenet):
    b = _unamortized_build(intangibles, depamor, 252) * _z(_aging(depamor, ppnenet), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- CHARGE-COVERAGE & CROSS-BASE HORIZONS (depamor non-cancelling) ----

# D&A charge per unit of total impairment-prone book (intangibles + PP&E), z-scored
def f34iw_f34_impairment_writedown_risk_pronechargez_252d_base_v123_signal(depamor, intangibles, ppnenet):
    b = _z(depamor / (intangibles + ppnenet).replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in the prone-charge rate (run-off intensity on the prone block rising)
def f34iw_f34_impairment_writedown_risk_pronechargegr_252d_base_v124_signal(depamor, intangibles, ppnenet):
    s = depamor / (intangibles + ppnenet).replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible run-off horizon (intangibles per unit charge), tanh-compressed level
def f34iw_f34_impairment_writedown_risk_intcoverlvl_0d_base_v125_signal(intangibles, depamor):
    b = np.tanh(0.2 * (intangibles / depamor.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in the intangible run-off horizon (deferral lengthening), bounded
def f34iw_f34_impairment_writedown_risk_intcovergr_252d_base_v126_signal(intangibles, depamor):
    s = np.log1p(intangibles / depamor.replace(0, np.nan))
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPOSITE WRITEDOWN-PRESSURE / REGIME BLENDS ----

# composite: stale soft book (low amort z) + impaired soft book (deep peak drawdown)
def f34iw_f34_impairment_writedown_risk_stalexdd_0d_base_v127_signal(depamor, intangibles):
    stale = (-_z(_amort_rate(depamor, intangibles), 252)).clip(lower=0.0)
    pk = _rmax(intangibles, 504)
    dd = (intangibles / pk.replace(0, np.nan) - 1.0).abs()
    b = stale * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite writedown-pressure (2y window): low run-off + high aging both in z-space
def f34iw_f34_impairment_writedown_risk_writepress_504d_base_v128_signal(depamor, intangibles, ppnenet):
    stale = (-_z(_amort_rate(depamor, intangibles), 504)).clip(lower=0.0)
    hot = _z(_aging(depamor, ppnenet), 504).clip(lower=0.0)
    b = stale + hot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years BOTH aging was hot AND amort was cold (sustained dual-stress regime)
def f34iw_f34_impairment_writedown_risk_dualstressregime_504d_base_v129_signal(depamor, intangibles, ppnenet):
    hot = _aging(depamor, ppnenet) > _mean(_aging(depamor, ppnenet), 252)
    cold = _amort_rate(depamor, intangibles) < _mean(_amort_rate(depamor, intangibles), 252)
    both = (hot & cold).astype(float)
    b = both.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- CHARGE-ACCELERATION / JERK-STYLE BASES (single-level, distinct from deriv files) ----

# D&A charge acceleration over a half-year (charge build speeding up)
def f34iw_f34_impairment_writedown_risk_depgracc_126d_base_v130_signal(depamor):
    g = _growth(depamor, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate second difference (curvature of the charge rate, quarterly)
def f34iw_f34_impairment_writedown_risk_agingcurv_63d_base_v131_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = (s - s.shift(63)) - (s.shift(63) - s.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amort-rate second difference (curvature of the run-off rate, quarterly)
def f34iw_f34_impairment_writedown_risk_amortcurv_63d_base_v132_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = (s - s.shift(63)) - (s.shift(63) - s.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ADDITIONAL DEPAMOR-CHARGE EROSION / EXTREMITY FACETS ----

# D&A charge vs its own 1260d peak (charge running near a 5y high)
def f34iw_f34_impairment_writedown_risk_deppeak_1260d_base_v133_signal(depamor):
    pk = _rmax(depamor, 1260)
    b = depamor / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging rate signed-sqrt deviation from its 504d mean (long-horizon bounded charge surprise)
def f34iw_f34_impairment_writedown_risk_agingsignmag_504d_base_v134_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    d = s - _mean(s, 504)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amort rate signed-sqrt deviation from its 504d mean
def f34iw_f34_impairment_writedown_risk_amortsignmag_504d_base_v135_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    d = s - _mean(s, 504)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed quarterly aging change (bounded short-horizon charge acceleration)
def f34iw_f34_impairment_writedown_risk_agingtanh_63d_base_v136_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    b = np.tanh(60.0 * (s - s.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed quarterly amort-rate change (bounded short-horizon run-off acceleration)
def f34iw_f34_impairment_writedown_risk_amorttanh_63d_base_v137_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = np.tanh(30.0 * (s - s.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate range position within its own 252d band (faster band position)
def f34iw_f34_impairment_writedown_risk_agingbandpos_252d_base_v138_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    hi = _rmax(s, 252)
    lo = _rmin(s, 252)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amort-rate range position within its own 252d band
def f34iw_f34_impairment_writedown_risk_amortbandpos_252d_base_v139_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    hi = _rmax(s, 252)
    lo = _rmin(s, 252)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTANGIBLE-BUILD x CHARGE INTERACTIONS & MISC ----

# intangible build pace x (1 - amort rank): build accelerating while run-off lags, bounded
def f34iw_f34_impairment_writedown_risk_buildlagcharge_252d_base_v140_signal(intangibles, depamor):
    g = np.tanh(4.0 * _growth(intangibles, 252))
    lag = (0.5 - _rank(_amort_rate(depamor, intangibles), 504))
    b = g * lag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible book drawdown-from-peak momentum (impairment deepening/recovering over a quarter)
def f34iw_f34_impairment_writedown_risk_intddmom_63d_base_v141_signal(intangibles):
    pk = _rmax(intangibles, 504)
    dd = intangibles / pk.replace(0, np.nan) - 1.0
    b = dd - dd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate yoy change x intangible drawdown (charge rising as the soft book impairs)
def f34iw_f34_impairment_writedown_risk_aginggrxintdd_0d_base_v142_signal(depamor, ppnenet, intangibles):
    ag = _aging(depamor, ppnenet)
    pk = _rmax(intangibles, 504)
    dd = (intangibles / pk.replace(0, np.nan) - 1.0).abs()
    b = (ag - ag.shift(252)) * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E-base implied growth from the charge gap: D&A growth minus aging-rate growth, z-scored
# so neither term dominates (captures whether the base is growing or shrinking under the charge)
def f34iw_f34_impairment_writedown_risk_basegrowthimplied_252d_base_v143_signal(depamor, ppnenet):
    ag = _aging(depamor, ppnenet)
    s = _z(_growth(depamor, 252), 252) - _z(ag - ag.shift(252), 252)
    b = s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# D&A charge rise off its own 504d trough (charge climbing from a recent low), tanh-bounded
def f34iw_f34_impairment_writedown_risk_chargeofftrough_504d_base_v144_signal(depamor):
    lo = _rmin(depamor, 504)
    b = np.tanh(depamor / lo.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aging-rate EMA displacement ranked over two years (persistent charge-rate displacement)
def f34iw_f34_impairment_writedown_risk_agingemadisp_126d_base_v145_signal(depamor, ppnenet):
    s = _aging(depamor, ppnenet)
    disp = s - s.ewm(span=63, min_periods=21).mean()
    b = disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amort-rate EMA displacement (persistent run-off-rate displacement)
def f34iw_f34_impairment_writedown_risk_amortemadisp_126d_base_v146_signal(depamor, intangibles):
    s = _amort_rate(depamor, intangibles)
    b = s - s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year change in the soft-vs-hard z spread (relative run-off rotating over time)
def f34iw_f34_impairment_writedown_risk_softhardzspreadmom_126d_base_v147_signal(depamor, intangibles, ppnenet):
    sp = _z(_amort_rate(depamor, intangibles), 252) - _z(_aging(depamor, ppnenet), 252)
    b = sp - sp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible run-off horizon dispersion (instability of the soft-book carry horizon)
def f34iw_f34_impairment_writedown_risk_intcoverdisp_252d_base_v148_signal(intangibles, depamor):
    s = np.log1p(intangibles / depamor.replace(0, np.nan))
    b = _std(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# prone-charge rate dispersion (instability of run-off intensity on the prone block)
def f34iw_f34_impairment_writedown_risk_pronechargedisp_252d_base_v149_signal(depamor, intangibles, ppnenet):
    b = _std(depamor / (intangibles + ppnenet).replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite peak-stress: aging band-position x amort-rate cold-z (top-of-band charge while
# the soft book is under-amortized) — both depamor-driven, distinct from any drawdown form
def f34iw_f34_impairment_writedown_risk_jointpeakstress_0d_base_v150_signal(depamor, ppnenet, intangibles):
    ag = _aging(depamor, ppnenet)
    hi = _rmax(ag, 504)
    lo = _rmin(ag, 504)
    bandpos = (ag - lo) / (hi - lo).replace(0, np.nan)
    cold = (-_z(_amort_rate(depamor, intangibles), 252)).clip(lower=0.0)
    b = bandpos * cold
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34iw_f34_impairment_writedown_risk_agingz_126d_base_v076_signal,
    f34iw_f34_impairment_writedown_risk_agingema_63d_base_v077_signal,
    f34iw_f34_impairment_writedown_risk_agingrank_1260d_base_v078_signal,
    f34iw_f34_impairment_writedown_risk_agingmom_21d_base_v079_signal,
    f34iw_f34_impairment_writedown_risk_agingdisp_504d_base_v080_signal,
    f34iw_f34_impairment_writedown_risk_agingvsmean_252d_base_v081_signal,
    f34iw_f34_impairment_writedown_risk_agingupfreq_252d_base_v082_signal,
    f34iw_f34_impairment_writedown_risk_aginggr_504d_base_v083_signal,
    f34iw_f34_impairment_writedown_risk_agingdisprank_504d_base_v084_signal,
    f34iw_f34_impairment_writedown_risk_amortratez_126d_base_v085_signal,
    f34iw_f34_impairment_writedown_risk_amortrateema_63d_base_v086_signal,
    f34iw_f34_impairment_writedown_risk_amortraterank_1260d_base_v087_signal,
    f34iw_f34_impairment_writedown_risk_amortrategrz_504d_base_v088_signal,
    f34iw_f34_impairment_writedown_risk_amortratedisp_504d_base_v089_signal,
    f34iw_f34_impairment_writedown_risk_amorthi_504d_base_v090_signal,
    f34iw_f34_impairment_writedown_risk_amortratemom_21d_base_v091_signal,
    f34iw_f34_impairment_writedown_risk_amortcoldpersist_252d_base_v092_signal,
    f34iw_f34_impairment_writedown_risk_intgr_126d_base_v093_signal,
    f34iw_f34_impairment_writedown_risk_intgr_21d_base_v094_signal,
    f34iw_f34_impairment_writedown_risk_intpeakdist_252d_base_v095_signal,
    f34iw_f34_impairment_writedown_risk_intbandpos_252d_base_v096_signal,
    f34iw_f34_impairment_writedown_risk_intnewlowcnt_252d_base_v097_signal,
    f34iw_f34_impairment_writedown_risk_intmaxdrop_252d_base_v098_signal,
    f34iw_f34_impairment_writedown_risk_intgrrank_252d_base_v099_signal,
    f34iw_f34_impairment_writedown_risk_intbuildregime_504d_base_v100_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuild_63d_base_v101_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuild_504d_base_v102_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuildrank_504d_base_v103_signal,
    f34iw_f34_impairment_writedown_risk_unamortbuilddisp_252d_base_v104_signal,
    f34iw_f34_impairment_writedown_risk_chargebandpos_504d_base_v105_signal,
    f34iw_f34_impairment_writedown_risk_depgr_504d_base_v106_signal,
    f34iw_f34_impairment_writedown_risk_depvsmean_252d_base_v107_signal,
    f34iw_f34_impairment_writedown_risk_depassetsmom_63d_base_v108_signal,
    f34iw_f34_impairment_writedown_risk_depassetsrank_504d_base_v109_signal,
    f34iw_f34_impairment_writedown_risk_depassetsdisp_252d_base_v110_signal,
    f34iw_f34_impairment_writedown_risk_depeqmom_63d_base_v111_signal,
    f34iw_f34_impairment_writedown_risk_depeqdisp_252d_base_v112_signal,
    f34iw_f34_impairment_writedown_risk_depeqz_504d_base_v113_signal,
    f34iw_f34_impairment_writedown_risk_interodestreak_252d_base_v114_signal,
    f34iw_f34_impairment_writedown_risk_intdowncum_252d_base_v115_signal,
    f34iw_f34_impairment_writedown_risk_intstalehigh_252d_base_v116_signal,
    f34iw_f34_impairment_writedown_risk_intdderode_1260d_base_v117_signal,
    f34iw_f34_impairment_writedown_risk_agingxamortmom_126d_base_v118_signal,
    f34iw_f34_impairment_writedown_risk_agingzxbuild_0d_base_v119_signal,
    f34iw_f34_impairment_writedown_risk_softhardzspread_252d_base_v120_signal,
    f34iw_f34_impairment_writedown_risk_jointrunoffz_252d_base_v121_signal,
    f34iw_f34_impairment_writedown_risk_buildxagingz_0d_base_v122_signal,
    f34iw_f34_impairment_writedown_risk_pronechargez_252d_base_v123_signal,
    f34iw_f34_impairment_writedown_risk_pronechargegr_252d_base_v124_signal,
    f34iw_f34_impairment_writedown_risk_intcoverlvl_0d_base_v125_signal,
    f34iw_f34_impairment_writedown_risk_intcovergr_252d_base_v126_signal,
    f34iw_f34_impairment_writedown_risk_stalexdd_0d_base_v127_signal,
    f34iw_f34_impairment_writedown_risk_writepress_504d_base_v128_signal,
    f34iw_f34_impairment_writedown_risk_dualstressregime_504d_base_v129_signal,
    f34iw_f34_impairment_writedown_risk_depgracc_126d_base_v130_signal,
    f34iw_f34_impairment_writedown_risk_agingcurv_63d_base_v131_signal,
    f34iw_f34_impairment_writedown_risk_amortcurv_63d_base_v132_signal,
    f34iw_f34_impairment_writedown_risk_deppeak_1260d_base_v133_signal,
    f34iw_f34_impairment_writedown_risk_agingsignmag_504d_base_v134_signal,
    f34iw_f34_impairment_writedown_risk_amortsignmag_504d_base_v135_signal,
    f34iw_f34_impairment_writedown_risk_agingtanh_63d_base_v136_signal,
    f34iw_f34_impairment_writedown_risk_amorttanh_63d_base_v137_signal,
    f34iw_f34_impairment_writedown_risk_agingbandpos_252d_base_v138_signal,
    f34iw_f34_impairment_writedown_risk_amortbandpos_252d_base_v139_signal,
    f34iw_f34_impairment_writedown_risk_buildlagcharge_252d_base_v140_signal,
    f34iw_f34_impairment_writedown_risk_intddmom_63d_base_v141_signal,
    f34iw_f34_impairment_writedown_risk_aginggrxintdd_0d_base_v142_signal,
    f34iw_f34_impairment_writedown_risk_basegrowthimplied_252d_base_v143_signal,
    f34iw_f34_impairment_writedown_risk_chargeofftrough_504d_base_v144_signal,
    f34iw_f34_impairment_writedown_risk_agingemadisp_126d_base_v145_signal,
    f34iw_f34_impairment_writedown_risk_amortemadisp_126d_base_v146_signal,
    f34iw_f34_impairment_writedown_risk_softhardzspreadmom_126d_base_v147_signal,
    f34iw_f34_impairment_writedown_risk_intcoverdisp_252d_base_v148_signal,
    f34iw_f34_impairment_writedown_risk_pronechargedisp_252d_base_v149_signal,
    f34iw_f34_impairment_writedown_risk_jointpeakstress_0d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_IMPAIRMENT_WRITEDOWN_RISK_REGISTRY_076_150 = REGISTRY


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

    print("OK f34_impairment_writedown_risk_base_076_150_claude: %d features pass" % n_features)
