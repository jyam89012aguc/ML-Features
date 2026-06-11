import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _median(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).median()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (valuation-vs-growth / GARP) =====
def _growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _log_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _peg(mult, growth_pct):
    return mult / (growth_pct * 100.0).replace(0, np.nan)


def _fcf_yield(fcf, marketcap):
    return fcf / marketcap.replace(0, np.nan)


def _rule40_mult(mult, growth_pct, margin):
    r40 = growth_pct + margin
    return mult / (1.0 + r40)


# ============================================================
# v076 EV/Sales-to-126d-growth PEG, percentile-ranked (medium-horizon cheap GARP)
def f44vg_f44_valuation_vs_growth_evspeg126_126d_base_v076_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    result = _rank(_peg(evs, g), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v077 P/S-to-126d-growth PEG, z-scored (de-trended medium-horizon GARP)
def f44vg_f44_valuation_vs_growth_pspeg126_126d_base_v077_signal(ps, revenue):
    g = _growth(revenue, 126)
    result = _z(_peg(ps, g), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v078 EV/EBITDA-to-126d-EBITDA-growth PEG, level
def f44vg_f44_valuation_vs_growth_evebpeg126_126d_base_v078_signal(evebitda, ebitda):
    g = _growth(ebitda, 126)
    result = _peg(evebitda, g)
    return result.replace([np.inf, -np.inf], np.nan)


# v079 EV/Sales-to-504d-growth PEG (long-horizon GARP level)
def f44vg_f44_valuation_vs_growth_evspeg504_504d_base_v079_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 504)
    result = _peg(evs, g)
    return result.replace([np.inf, -np.inf], np.nan)


# v080 marketcap/revenue PEG (P/S-style on marketcap), percentile-ranked vs 2yr
def f44vg_f44_valuation_vs_growth_mcrevpeg_252d_base_v080_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    result = _rank(_peg(mc_rev, g), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v081 FCF-yield plus 126d revenue growth (shorter-horizon GARP total-return)
def f44vg_f44_valuation_vs_growth_fcfgro126_126d_base_v081_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 126)
    result = yld + g
    return result.replace([np.inf, -np.inf], np.nan)


# v082 EV/EBITDA-to-growth minus EV/Sales-to-growth (profit-vs-sales GARP spread)
def f44vg_f44_valuation_vs_growth_pegprofspr_252d_base_v082_signal(ev, evebitda, revenue, ebitda):
    p_sales = _peg(_evsales(ev, revenue), _growth(revenue, 252))
    p_prof = _peg(evebitda, _growth(ebitda, 252))
    result = p_prof - p_sales
    return result.replace([np.inf, -np.inf], np.nan)


# v083 growth-adjusted cheapness using 126d growth and EV/Sales z (medium GARP)
def f44vg_f44_valuation_vs_growth_garpmed_126d_base_v083_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    result = g - _z(evs, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v084 EV/Sales PEG momentum over a month (faster re-rating)
def f44vg_f44_valuation_vs_growth_evspegmom21_252d_base_v084_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    result = peg - peg.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# v085 P/S PEG vs its 504d minimum (distance above cheapest GARP level)
def f44vg_f44_valuation_vs_growth_pegabovemin_252d_base_v085_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    lo = peg.rolling(504, min_periods=126).min()
    result = (peg - lo) / lo.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v086 EV/EBITDA PEG vs its 504d max (distance below most-expensive level)
def f44vg_f44_valuation_vs_growth_pegbelowmax_252d_base_v086_signal(evebitda, ebitda):
    peg = _peg(evebitda, _growth(ebitda, 252))
    hi = peg.rolling(504, min_periods=126).max()
    result = (hi - peg) / hi.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v087 inverse PEG (growth-per-EV/Sales-turn) on 126d growth, z-scored
def f44vg_f44_valuation_vs_growth_invevs126_126d_base_v087_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    inv = (g * 100.0) / evs.replace(0, np.nan)
    result = _z(inv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v088 inverse PEG on P/S, 126d growth, momentum
def f44vg_f44_valuation_vs_growth_invps126_126d_base_v088_signal(ps, revenue):
    g = _growth(revenue, 126)
    inv = (g * 100.0) / ps.replace(0, np.nan)
    result = inv - inv.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v089 EV/Sales vs marketcap/revenue PEG spread momentum (debt-load GARP shift)
def f44vg_f44_valuation_vs_growth_evmcpegspr_252d_base_v089_signal(ev, marketcap, revenue):
    g = _growth(revenue, 252)
    p_ev = _peg(_evsales(ev, revenue), g)
    p_mc = _peg(_safe_div(marketcap, revenue), g)
    spread = p_ev - p_mc
    result = spread - spread.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v090 GARP composite z over 126d: growth z minus avg(P/S z, EV/EBITDA z)
def f44vg_f44_valuation_vs_growth_garpcompz126_126d_base_v090_signal(ps, evebitda, revenue):
    gz = _z(_growth(revenue, 126), 126)
    vz = (_z(ps, 126) + _z(evebitda, 126)) / 2.0
    result = gz - vz
    return result.replace([np.inf, -np.inf], np.nan)


# v091 rule-of-40 (revenue growth + ebitda margin) score, level
def f44vg_f44_valuation_vs_growth_r40eb_252d_base_v091_signal(revenue, ebitda):
    g = _growth(revenue, 252)
    margin = _safe_div(ebitda, revenue)
    result = g + margin
    return result.replace([np.inf, -np.inf], np.nan)


# v092 rule-of-40 (ebitda-margin variant) per EV/Sales turn, ranked
def f44vg_f44_valuation_vs_growth_r40ebperevs_252d_base_v092_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(ebitda, revenue)
    r = (g + margin) / evs.replace(0, np.nan)
    result = _rank(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v093 FCF growth coupled to FCF yield (self-funding GARP: growing cash + cheap)
def f44vg_f44_valuation_vs_growth_fcfgrowyld_252d_base_v093_signal(fcf, marketcap):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(fcf, 252)
    result = yld + np.tanh(g)
    return result.replace([np.inf, -np.inf], np.nan)


# v094 EV/Sales cheapness vs EBITDA growth (cross-line GARP: cheap on sales, growing profit)
def f44vg_f44_valuation_vs_growth_evscrosseb_252d_base_v094_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _growth(ebitda, 252)
    result = g - _z(evs, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v095 P/S cheapness vs EBITDA growth, ranked
def f44vg_f44_valuation_vs_growth_pscrosseb_252d_base_v095_signal(ps, ebitda):
    g = _growth(ebitda, 252)
    raw = g - _z(ps, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v096 EV/EBITDA cheapness vs revenue growth (cross-line GARP)
def f44vg_f44_valuation_vs_growth_evebcrossrev_252d_base_v096_signal(evebitda, revenue):
    g = _growth(revenue, 252)
    result = g - _z(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v097 growth acceleration minus EV/Sales re-rating (is accel paid for?)
def f44vg_f44_valuation_vs_growth_accelvsmult_252d_base_v097_signal(ev, revenue):
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    evs = _evsales(ev, revenue)
    rerate = _log_growth(evs, 126)
    result = accel - rerate
    return result.replace([np.inf, -np.inf], np.nan)


# v098 EV/Sales-to-growth, growth measured as 63d annualized (fast GARP)
def f44vg_f44_valuation_vs_growth_fastpeg_63d_base_v098_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 63) * 4.0
    result = _peg(evs, g)
    return result.replace([np.inf, -np.inf], np.nan)


# v099 fcf-yield-plus-growth dispersion across revenue & ebitda growth (GARP read spread)
def f44vg_f44_valuation_vs_growth_garpdisp_252d_base_v099_signal(fcf, marketcap, revenue, ebitda):
    yld = _fcf_yield(fcf, marketcap)
    a = yld + _growth(revenue, 252)
    b = yld + _growth(ebitda, 252)
    result = (a - b).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# v100 EV/Sales PEG vs P/S PEG ratio (capital-structure GARP tilt)
def f44vg_f44_valuation_vs_growth_pegratio_252d_base_v100_signal(ev, ps, revenue):
    g = _growth(revenue, 252)
    p1 = _peg(_evsales(ev, revenue), g)
    p2 = _peg(ps, g)
    result = p1 / p2.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v101 growth-adjusted EV/Sales fast vs slow EMA crossover (responsive GARP shift)
def f44vg_f44_valuation_vs_growth_garpfast_252d_base_v101_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    raw = g - _z(evs, 252)
    result = raw.ewm(span=21, min_periods=10).mean() - raw.ewm(span=84, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v102 EV/Sales residual vs 504d-implied multiple (long-horizon residual)
def f44vg_f44_valuation_vs_growth_evsresid504_504d_base_v102_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 504)
    implied = (1.0 + g).clip(lower=0.0) * _mean(evs, 504)
    result = (evs - implied) / implied.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v103 EBITDA-margin trajectory coupled to EV/EBITDA cheapness (improving + cheap)
def f44vg_f44_valuation_vs_growth_margtrajeveb_252d_base_v103_signal(evebitda, ebitda, revenue):
    margin = _safe_div(ebitda, revenue)
    dmargin = margin - margin.shift(252)
    cheap = -_z(evebitda, 252)
    result = cheap + dmargin * 8.0
    return result.replace([np.inf, -np.inf], np.nan)


# v104 fcf-yield growth-coupled, regime: fraction of year fcf-yield>0 and revenue growing
def f44vg_f44_valuation_vs_growth_fcfgroregime_252d_base_v104_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    good = ((yld > 0) & (g > 0)).astype(float)
    result = good.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# v105 EV/Sales-to-growth curvature (second difference of PEG)
def f44vg_f44_valuation_vs_growth_pegcurv2_252d_base_v105_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    result = peg - 2.0 * peg.shift(63) + peg.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# v106 growth-per-EV/EBITDA-turn momentum (re-rating of profit-GARP)
def f44vg_f44_valuation_vs_growth_invevebmom_252d_base_v106_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    inv = (g * 100.0) / evebitda.replace(0, np.nan)
    result = inv - inv.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v107 EV/Sales discount weighted by EBITDA growth (cheap on sales, growing profit)
def f44vg_f44_valuation_vs_growth_evsebgweight_252d_base_v107_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    disc = _mean(evs, 252) / evs.replace(0, np.nan) - 1.0
    g = _growth(ebitda, 252)
    result = disc * (1.0 + g.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)


# v108 blended PEG (EV/Sales + EV/EBITDA) level, average
def f44vg_f44_valuation_vs_growth_blendpeg_252d_base_v108_signal(ev, evebitda, revenue, ebitda):
    p1 = _peg(_evsales(ev, revenue), _growth(revenue, 252))
    p2 = _peg(evebitda, _growth(ebitda, 252))
    result = (p1 + p2) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# v109 blended PEG (EV/Sales + P/S) z-scored vs own 1yr history (de-trended composite)
def f44vg_f44_valuation_vs_growth_blendpegrank_252d_base_v109_signal(ev, ps, revenue):
    g = _growth(revenue, 252)
    p1 = _peg(_evsales(ev, revenue), g)
    p2 = _peg(ps, g)
    blended = (p1 + p2) / 2.0
    result = _z(blended, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v110 FCF-yield-plus-growth minus EV/EBITDA z (total profit-GARP)
def f44vg_f44_valuation_vs_growth_totalprofgarp_252d_base_v110_signal(fcf, marketcap, ebitda, evebitda):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(ebitda, 252)
    result = (yld + g) - _z(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v111 growth-funded valuation on EBITDA: ebitda log-growth minus EV log-change
def f44vg_f44_valuation_vs_growth_ebgrovsev_252d_base_v111_signal(ev, ebitda):
    g = _log_growth(ebitda, 252)
    de = _log_growth(ev, 252)
    result = g - de
    return result.replace([np.inf, -np.inf], np.nan)


# v112 P/S cheapness x revenue-growth-acceleration interaction
def f44vg_f44_valuation_vs_growth_psaccelinter_252d_base_v112_signal(ps, revenue):
    cheap = -_z(ps, 252)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    result = cheap * accel
    return result.replace([np.inf, -np.inf], np.nan)


# v113 EV/Sales-to-growth above-median fraction over last quarter (regime persistence)
def f44vg_f44_valuation_vs_growth_pegregmed_252d_base_v113_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    above = (peg > _median(peg, 252)).astype(float)
    result = above.rolling(63, min_periods=21).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# v114 growth-per-marketcap-turn (sales-growth GARP yield) z-scored
def f44vg_f44_valuation_vs_growth_mcgroyld_252d_base_v114_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / mc_rev.replace(0, np.nan)
    result = _z(inv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v115 rule-of-40-adjusted marketcap/revenue (growth + fcf margin penalize multiple)
def f44vg_f44_valuation_vs_growth_r40mcrev_252d_base_v115_signal(marketcap, revenue, fcf):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    result = _rule40_mult(mc_rev, g, margin)
    return result.replace([np.inf, -np.inf], np.nan)


# v116 EV/Sales-to-growth, tanh-bounded level (squashed GARP)
def f44vg_f44_valuation_vs_growth_evspegtanh_252d_base_v116_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    result = np.tanh((peg - 1.0) / 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# v117 growth-vol-penalized EV/EBITDA cheapness, change over a quarter (durable-GARP shift)
def f44vg_f44_valuation_vs_growth_durablecheap_252d_base_v117_signal(evebitda, ebitda):
    g63 = _growth(ebitda, 63)
    durability = 1.0 / (1.0 + _std(g63, 252) * 5.0)
    cheap = -_z(evebitda, 252)
    raw = cheap * durability
    result = raw - raw.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118 EV/EBITDA-to-growth dispersion across ebitda growth windows
def f44vg_f44_valuation_vs_growth_evebpegdisp_252d_base_v118_signal(evebitda, ebitda):
    p1 = _peg(evebitda, _growth(ebitda, 63))
    p2 = _peg(evebitda, _growth(ebitda, 126))
    p3 = _peg(evebitda, _growth(ebitda, 252))
    result = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# v119 FCF-yield rank coupled to revenue growth rank (double-percentile GARP)
def f44vg_f44_valuation_vs_growth_dualrankgarp_252d_base_v119_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    result = (_rank(yld, 504) + _rank(g, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# v120 EV/Sales mispricing: required growth (from multiple) vs 504d delivered, ranked
def f44vg_f44_valuation_vs_growth_misprrank_252d_base_v120_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    required = evs / _mean(evs, 504).replace(0, np.nan) - 1.0
    delivered = _growth(revenue, 252)
    gap = delivered - required
    result = _rank(gap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v121 growth-adjusted cheapness change over a year (annual GARP shift)
def f44vg_f44_valuation_vs_growth_garpyoy_252d_base_v121_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    score = g - _z(evs, 252)
    result = score - score.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# v122 P/S-to-growth PEG below-median fraction (cheap-GARP regime persistence)
def f44vg_f44_valuation_vs_growth_pegbelowmedfrac_252d_base_v122_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    below = (peg < _median(peg, 504)).astype(float)
    result = below.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# v123 EV/EBITDA-margin-growth GARP, ranked composite (margin growth + cheapness rank)
def f44vg_f44_valuation_vs_growth_margrowgarp_252d_base_v123_signal(evebitda, ebitda, revenue):
    margin = _safe_div(ebitda, revenue)
    gmarg = margin - margin.shift(252)
    result = _rank(gmarg, 504) - _rank(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v124 sales-growth-per-EV/Sales minus profit-growth-per-EV/EBITDA (GARP line divergence)
def f44vg_f44_valuation_vs_growth_garplinedivg_252d_base_v124_signal(ev, evebitda, revenue, ebitda):
    a = (_growth(revenue, 252) * 100.0) / _evsales(ev, revenue).replace(0, np.nan)
    b = (_growth(ebitda, 252) * 100.0) / evebitda.replace(0, np.nan)
    result = a - b
    return result.replace([np.inf, -np.inf], np.nan)


# v125 FCF-yield-plus-revenue-growth, 504d percentile rank (long-horizon GARP percentile)
def f44vg_f44_valuation_vs_growth_fcfgroz504_252d_base_v125_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    result = _rank(yld + g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v126 EV/Sales PEG vs P/S PEG correlation-breaker: log-ratio momentum
def f44vg_f44_valuation_vs_growth_pegratiomom_252d_base_v126_signal(ev, ps, revenue):
    g = _growth(revenue, 252)
    ratio = np.log(_peg(_evsales(ev, revenue), g).abs().replace(0, np.nan)
                   / _peg(ps, g).abs().replace(0, np.nan))
    result = ratio - ratio.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127 cheap-and-growing intensity: (-EV/Sales z clipped) x revenue growth
def f44vg_f44_valuation_vs_growth_cheapgrow_252d_base_v127_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    cheap = (-_z(evs, 252)).clip(lower=0)
    g = _growth(revenue, 252)
    result = cheap * g
    return result.replace([np.inf, -np.inf], np.nan)


# v128 EV/EBITDA cheap-and-growing intensity (profit line)
def f44vg_f44_valuation_vs_growth_cheapgroweb_252d_base_v128_signal(evebitda, ebitda):
    cheap = (-_z(evebitda, 252)).clip(lower=0)
    g = _growth(ebitda, 252)
    result = cheap * g
    return result.replace([np.inf, -np.inf], np.nan)


# v129 forward EV/EBITDA gap (one year of EBITDA growth)
def f44vg_f44_valuation_vs_growth_fwdeveb_252d_base_v129_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    fwd = evebitda / (1.0 + g).replace(0, np.nan)
    result = (evebitda - fwd) / evebitda.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v130 GARP quality composite: rule-of-40 (rev growth + fcf margin) minus EV/EBITDA z, smoothed
def f44vg_f44_valuation_vs_growth_r40minusval_252d_base_v130_signal(revenue, fcf, evebitda):
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    raw = (g + margin) - _z(evebitda, 252)
    result = raw.ewm(span=42, min_periods=21).mean() - raw
    return result.replace([np.inf, -np.inf], np.nan)


# v131 EV/Sales-to-growth, ranked over 252d (medium-window cheap-GARP percentile)
def f44vg_f44_valuation_vs_growth_evspegrk252_252d_base_v131_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    result = _rank(peg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v132 fcf-growth coupled to marketcap/revenue cheapness (growing cash, cheap price/sales)
def f44vg_f44_valuation_vs_growth_fcfgrocheap_252d_base_v132_signal(fcf, marketcap, revenue):
    gfcf = np.tanh(_growth(fcf, 252))
    cheap = -_z(_safe_div(marketcap, revenue), 252)
    result = gfcf + cheap
    return result.replace([np.inf, -np.inf], np.nan)


# v133 EV/Sales-to-growth half-life: PEG minus its 252d EMA, tanh-bounded displacement
def f44vg_f44_valuation_vs_growth_pegdisplace_252d_base_v133_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    disp = peg - peg.ewm(span=126, min_periods=42).mean()
    result = np.tanh(disp / _std(peg, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# v134 P/S-to-growth PEG vs its 126d rolling min (distance above cheapest, ranked)
def f44vg_f44_valuation_vs_growth_pspegdisplace_252d_base_v134_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    lo = peg.rolling(126, min_periods=42).min()
    gap = (peg - lo) / lo.abs().replace(0, np.nan)
    result = _rank(gap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v135 growth-scaled EV: revenue growth minus EV growth, ranked
def f44vg_f44_valuation_vs_growth_grovsevrank_252d_base_v135_signal(ev, revenue):
    g = _log_growth(revenue, 252)
    de = _log_growth(ev, 252)
    result = _rank(g - de, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v136 EV/Sales cheapness streak depth (avg distance below 252d mean, sign-aware)
def f44vg_f44_valuation_vs_growth_cheapdepth_252d_base_v136_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    depth = (_mean(evs, 252) - evs).where(g > 0, np.nan)
    result = depth.rolling(126, min_periods=42).mean() / _mean(evs, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v137 EBITDA-growth premium to EV/EBITDA over 126d (medium-window mispricing)
def f44vg_f44_valuation_vs_growth_ebgromispr126_126d_base_v137_signal(evebitda, ebitda):
    gz = _z(_growth(ebitda, 126), 126)
    vz = _z(evebitda, 126)
    result = gz - vz
    return result.replace([np.inf, -np.inf], np.nan)


# v138 dual-line GARP: avg of (rev-growth - EV/Sales z) and (ebitda-growth - EV/EBITDA z)
def f44vg_f44_valuation_vs_growth_dualline_252d_base_v138_signal(ev, revenue, evebitda, ebitda):
    a = _growth(revenue, 252) - _z(_evsales(ev, revenue), 252)
    b = _growth(ebitda, 252) - _z(evebitda, 252)
    result = (a + b) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# v139 PEG percentile flip on P/S (2yr rank minus 63d rank)
def f44vg_f44_valuation_vs_growth_pspegflip_252d_base_v139_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    result = _rank(peg, 504) - _rank(peg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v140 growth-adjusted FCF yield change (re-rating of cash-GARP over a quarter)
def f44vg_f44_valuation_vs_growth_fcfgarprerate_252d_base_v140_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    garp = yld * (1.0 + g.clip(lower=0))
    result = garp - garp.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v141 EV/Sales-to-growth, 504d rank (long-horizon cheap percentile)
def f44vg_f44_valuation_vs_growth_evspegrk504_504d_base_v141_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 504))
    result = _rank(peg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v142 P/S-to-126d-growth PEG curvature (medium-window re-rating acceleration)
def f44vg_f44_valuation_vs_growth_pspeg126curv_126d_base_v142_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 126))
    result = peg - 2.0 * peg.shift(42) + peg.shift(84)
    return result.replace([np.inf, -np.inf], np.nan)


# v143 growth-quality minus valuation: low-rev-growth-vol minus EV/Sales z
def f44vg_f44_valuation_vs_growth_qualminusval_252d_base_v143_signal(ev, revenue):
    g = _growth(revenue, 63)
    stability = -_std(g, 252)
    evs = _evsales(ev, revenue)
    result = _z(stability, 252) - _z(evs, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v144 EV/EBITDA-to-growth tanh, change over a quarter (bounded re-rating)
def f44vg_f44_valuation_vs_growth_evebtanhmom_252d_base_v144_signal(evebitda, ebitda):
    peg = _peg(evebitda, _growth(ebitda, 252))
    b = np.tanh(peg / 2.0)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145 composite mispricing rank: blended growth z minus blended valuation z, ranked
def f44vg_f44_valuation_vs_growth_misprblendrk_252d_base_v145_signal(ps, evebitda, revenue, ebitda):
    gz = (_z(_growth(revenue, 252), 252) + _z(_growth(ebitda, 252), 252)) / 2.0
    vz = (_z(ps, 252) + _z(evebitda, 252)) / 2.0
    result = _rank(gz - vz, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v146 EV/Sales-to-growth, growth = max(rev, ebitda) growth (best-line PEG)
def f44vg_f44_valuation_vs_growth_bestlinepeg_252d_base_v146_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = pd.concat([_growth(revenue, 252), _growth(ebitda, 252)], axis=1).max(axis=1)
    result = _peg(evs, g)
    return result.replace([np.inf, -np.inf], np.nan)


# v147 FCF-yield-plus-growth minus P/S z (cash-GARP vs price/sales valuation)
def f44vg_f44_valuation_vs_growth_cashgarp_252d_base_v147_signal(fcf, marketcap, revenue, ps):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    result = (yld + g) - _z(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v148 EV/Sales-to-growth minus EV/EBITDA-to-growth, smoothed (line-spread persistence)
def f44vg_f44_valuation_vs_growth_linespreadsm_252d_base_v148_signal(ev, evebitda, revenue, ebitda):
    p1 = _peg(_evsales(ev, revenue), _growth(revenue, 252))
    p2 = _peg(evebitda, _growth(ebitda, 252))
    spread = p1 - p2
    result = spread.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v149 growth-per-EV/Sales-turn vs growth-per-P/S-turn dispersion (GARP read disagreement)
def f44vg_f44_valuation_vs_growth_invpegdisp_252d_base_v149_signal(ev, ps, revenue):
    g = _growth(revenue, 252) * 100.0
    a = g / _evsales(ev, revenue).replace(0, np.nan)
    b = g / ps.replace(0, np.nan)
    result = _z((a - b).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v150 total GARP grand composite: blended inverse-PEG plus fcf yield, ranked
def f44vg_f44_valuation_vs_growth_grandgarp_252d_base_v150_signal(ev, ps, evebitda, revenue, ebitda, fcf, marketcap):
    g_rev = _growth(revenue, 252) * 100.0
    g_eb = _growth(ebitda, 252) * 100.0
    a = g_rev / _evsales(ev, revenue).replace(0, np.nan)
    b = g_rev / ps.replace(0, np.nan)
    c = g_eb / evebitda.replace(0, np.nan)
    yld = _fcf_yield(fcf, marketcap)
    composite = (a + b + c) / 3.0 + yld * 100.0
    result = _rank(composite, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44vg_f44_valuation_vs_growth_evspeg126_126d_base_v076_signal,
    f44vg_f44_valuation_vs_growth_pspeg126_126d_base_v077_signal,
    f44vg_f44_valuation_vs_growth_evebpeg126_126d_base_v078_signal,
    f44vg_f44_valuation_vs_growth_evspeg504_504d_base_v079_signal,
    f44vg_f44_valuation_vs_growth_mcrevpeg_252d_base_v080_signal,
    f44vg_f44_valuation_vs_growth_fcfgro126_126d_base_v081_signal,
    f44vg_f44_valuation_vs_growth_pegprofspr_252d_base_v082_signal,
    f44vg_f44_valuation_vs_growth_garpmed_126d_base_v083_signal,
    f44vg_f44_valuation_vs_growth_evspegmom21_252d_base_v084_signal,
    f44vg_f44_valuation_vs_growth_pegabovemin_252d_base_v085_signal,
    f44vg_f44_valuation_vs_growth_pegbelowmax_252d_base_v086_signal,
    f44vg_f44_valuation_vs_growth_invevs126_126d_base_v087_signal,
    f44vg_f44_valuation_vs_growth_invps126_126d_base_v088_signal,
    f44vg_f44_valuation_vs_growth_evmcpegspr_252d_base_v089_signal,
    f44vg_f44_valuation_vs_growth_garpcompz126_126d_base_v090_signal,
    f44vg_f44_valuation_vs_growth_r40eb_252d_base_v091_signal,
    f44vg_f44_valuation_vs_growth_r40ebperevs_252d_base_v092_signal,
    f44vg_f44_valuation_vs_growth_fcfgrowyld_252d_base_v093_signal,
    f44vg_f44_valuation_vs_growth_evscrosseb_252d_base_v094_signal,
    f44vg_f44_valuation_vs_growth_pscrosseb_252d_base_v095_signal,
    f44vg_f44_valuation_vs_growth_evebcrossrev_252d_base_v096_signal,
    f44vg_f44_valuation_vs_growth_accelvsmult_252d_base_v097_signal,
    f44vg_f44_valuation_vs_growth_fastpeg_63d_base_v098_signal,
    f44vg_f44_valuation_vs_growth_garpdisp_252d_base_v099_signal,
    f44vg_f44_valuation_vs_growth_pegratio_252d_base_v100_signal,
    f44vg_f44_valuation_vs_growth_garpfast_252d_base_v101_signal,
    f44vg_f44_valuation_vs_growth_evsresid504_504d_base_v102_signal,
    f44vg_f44_valuation_vs_growth_margtrajeveb_252d_base_v103_signal,
    f44vg_f44_valuation_vs_growth_fcfgroregime_252d_base_v104_signal,
    f44vg_f44_valuation_vs_growth_pegcurv2_252d_base_v105_signal,
    f44vg_f44_valuation_vs_growth_invevebmom_252d_base_v106_signal,
    f44vg_f44_valuation_vs_growth_evsebgweight_252d_base_v107_signal,
    f44vg_f44_valuation_vs_growth_blendpeg_252d_base_v108_signal,
    f44vg_f44_valuation_vs_growth_blendpegrank_252d_base_v109_signal,
    f44vg_f44_valuation_vs_growth_totalprofgarp_252d_base_v110_signal,
    f44vg_f44_valuation_vs_growth_ebgrovsev_252d_base_v111_signal,
    f44vg_f44_valuation_vs_growth_psaccelinter_252d_base_v112_signal,
    f44vg_f44_valuation_vs_growth_pegregmed_252d_base_v113_signal,
    f44vg_f44_valuation_vs_growth_mcgroyld_252d_base_v114_signal,
    f44vg_f44_valuation_vs_growth_r40mcrev_252d_base_v115_signal,
    f44vg_f44_valuation_vs_growth_evspegtanh_252d_base_v116_signal,
    f44vg_f44_valuation_vs_growth_durablecheap_252d_base_v117_signal,
    f44vg_f44_valuation_vs_growth_evebpegdisp_252d_base_v118_signal,
    f44vg_f44_valuation_vs_growth_dualrankgarp_252d_base_v119_signal,
    f44vg_f44_valuation_vs_growth_misprrank_252d_base_v120_signal,
    f44vg_f44_valuation_vs_growth_garpyoy_252d_base_v121_signal,
    f44vg_f44_valuation_vs_growth_pegbelowmedfrac_252d_base_v122_signal,
    f44vg_f44_valuation_vs_growth_margrowgarp_252d_base_v123_signal,
    f44vg_f44_valuation_vs_growth_garplinedivg_252d_base_v124_signal,
    f44vg_f44_valuation_vs_growth_fcfgroz504_252d_base_v125_signal,
    f44vg_f44_valuation_vs_growth_pegratiomom_252d_base_v126_signal,
    f44vg_f44_valuation_vs_growth_cheapgrow_252d_base_v127_signal,
    f44vg_f44_valuation_vs_growth_cheapgroweb_252d_base_v128_signal,
    f44vg_f44_valuation_vs_growth_fwdeveb_252d_base_v129_signal,
    f44vg_f44_valuation_vs_growth_r40minusval_252d_base_v130_signal,
    f44vg_f44_valuation_vs_growth_evspegrk252_252d_base_v131_signal,
    f44vg_f44_valuation_vs_growth_fcfgrocheap_252d_base_v132_signal,
    f44vg_f44_valuation_vs_growth_pegdisplace_252d_base_v133_signal,
    f44vg_f44_valuation_vs_growth_pspegdisplace_252d_base_v134_signal,
    f44vg_f44_valuation_vs_growth_grovsevrank_252d_base_v135_signal,
    f44vg_f44_valuation_vs_growth_cheapdepth_252d_base_v136_signal,
    f44vg_f44_valuation_vs_growth_ebgromispr126_126d_base_v137_signal,
    f44vg_f44_valuation_vs_growth_dualline_252d_base_v138_signal,
    f44vg_f44_valuation_vs_growth_pspegflip_252d_base_v139_signal,
    f44vg_f44_valuation_vs_growth_fcfgarprerate_252d_base_v140_signal,
    f44vg_f44_valuation_vs_growth_evspegrk504_504d_base_v141_signal,
    f44vg_f44_valuation_vs_growth_pspeg126curv_126d_base_v142_signal,
    f44vg_f44_valuation_vs_growth_qualminusval_252d_base_v143_signal,
    f44vg_f44_valuation_vs_growth_evebtanhmom_252d_base_v144_signal,
    f44vg_f44_valuation_vs_growth_misprblendrk_252d_base_v145_signal,
    f44vg_f44_valuation_vs_growth_bestlinepeg_252d_base_v146_signal,
    f44vg_f44_valuation_vs_growth_cashgarp_252d_base_v147_signal,
    f44vg_f44_valuation_vs_growth_linespreadsm_252d_base_v148_signal,
    f44vg_f44_valuation_vs_growth_invpegdisp_252d_base_v149_signal,
    f44vg_f44_valuation_vs_growth_grandgarp_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_VALUATION_VS_GROWTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    ps = _fund(1, base=6.0, drift=0.01, vol=0.05).rename("ps")
    evebitda = _fund(2, base=18.0, drift=0.01, vol=0.05).rename("evebitda")
    ev = _fund(3, base=2.0e9, drift=0.035, vol=0.08).rename("ev")
    marketcap = _fund(4, base=1.8e9, drift=0.035, vol=0.08).rename("marketcap")
    revenue = _fund(5, base=5.0e8, drift=0.04, vol=0.06).rename("revenue")
    ebitda = _fund(6, base=8.0e7, drift=0.03, vol=0.10).rename("ebitda")
    fcf = _fund(7, base=4.0e7, drift=0.03, vol=0.12, allow_neg=True).rename("fcf")

    cols = {
        "ps": ps, "evebitda": evebitda, "ev": ev, "marketcap": marketcap,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f44_valuation_vs_growth_base_076_150_claude: %d features pass" % n_features)
