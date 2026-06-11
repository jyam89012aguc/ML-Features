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
    # trailing fractional growth of a fundamental series over w days
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _log_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _peg(mult, growth_pct):
    # PEG-style: multiple divided by growth expressed in percent points
    return mult / (growth_pct * 100.0).replace(0, np.nan)


def _fcf_yield(fcf, marketcap):
    return fcf / marketcap.replace(0, np.nan)


def _rule40_mult(mult, growth_pct, margin):
    # cheapness penalized/rewarded by rule-of-40 score
    r40 = growth_pct + margin
    return mult / (1.0 + r40)


# ============================================================
# v001 EV/Sales-to-growth PEG (level)
def f44vg_f44_valuation_vs_growth_evspeg_252d_base_v001_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    result = _peg(evs, g)
    return result.replace([np.inf, -np.inf], np.nan)


# v002 EV/Sales PEG over 126d growth, z-scored (de-trended PEG)
def f44vg_f44_valuation_vs_growth_evspeg_126d_base_v002_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    result = _z(_peg(evs, g), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v003 P/S-to-growth PEG, percentile-ranked vs own 2yr (cheap-GARP percentile)
def f44vg_f44_valuation_vs_growth_pspeg_252d_base_v003_signal(ps, revenue):
    g = _growth(revenue, 252)
    result = _rank(_peg(ps, g), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v004 P/S PEG on 63d sequential growth, change over a month (PEG momentum)
def f44vg_f44_valuation_vs_growth_pspeg_63d_base_v004_signal(ps, revenue):
    g = _growth(revenue, 63)
    peg = _peg(ps, g)
    result = peg - peg.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# v005 EV/EBITDA-to-growth PEG on EBITDA growth (level)
def f44vg_f44_valuation_vs_growth_evebpeg_252d_base_v005_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    result = _peg(evebitda, g)
    return result.replace([np.inf, -np.inf], np.nan)


# v006 EV/EBITDA vs revenue-growth PEG, z-scored vs own 1yr history (de-trended)
def f44vg_f44_valuation_vs_growth_evebrevpeg_252d_base_v006_signal(evebitda, revenue):
    g = _growth(revenue, 252)
    result = _z(_peg(evebitda, g), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v007 FCF-yield plus revenue growth (GARP total-return, level)
def f44vg_f44_valuation_vs_growth_fcfyldgro_252d_base_v007_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    result = yld + g
    return result.replace([np.inf, -np.inf], np.nan)


# v008 FCF-yield plus EBITDA growth, z-scored (relative mature-GARP)
def f44vg_f44_valuation_vs_growth_fcfyldebg_252d_base_v008_signal(fcf, marketcap, ebitda):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(ebitda, 252)
    result = _z(yld + g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v009 Rule-of-40-adjusted EV/Sales (growth% + fcf-margin penalize the multiple)
def f44vg_f44_valuation_vs_growth_r40evs_252d_base_v009_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    result = _rule40_mult(evs, g, margin)
    return result.replace([np.inf, -np.inf], np.nan)


# v010 Rule-of-40-adjusted P/S, change over a quarter (re-rating speed)
def f44vg_f44_valuation_vs_growth_r40ps_252d_base_v010_signal(ps, revenue, fcf):
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    r = _rule40_mult(ps, g, margin)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v011 growth-adjusted cheapness: revenue growth minus z of EV/Sales
def f44vg_f44_valuation_vs_growth_garp_evs_252d_base_v011_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    result = g - _z(evs, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v012 growth-adjusted cheapness on P/S z-score, sign of the read only x magnitude
def f44vg_f44_valuation_vs_growth_garp_ps_252d_base_v012_signal(ps, revenue):
    g = _z(_growth(revenue, 252), 252)
    v = -_z(ps, 252)
    result = np.sign(g + v) * (g.abs() + v.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# v013 growth-adjusted cheapness on EV/EBITDA z (ebitda growth z minus multiple z)
def f44vg_f44_valuation_vs_growth_garp_eveb_252d_base_v013_signal(evebitda, ebitda):
    g = _z(_growth(ebitda, 252), 252)
    result = g - _z(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v014 EV/Sales PEG dispersion across growth windows (stability of the GARP read)
def f44vg_f44_valuation_vs_growth_evspegrank_252d_base_v014_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    p1 = _peg(evs, _growth(revenue, 63))
    p2 = _peg(evs, _growth(revenue, 126))
    p3 = _peg(evs, _growth(revenue, 252))
    result = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# v015 P/S PEG below-1 streak (fraction of last year PEG sat under 1.0 = cheap)
def f44vg_f44_valuation_vs_growth_pspegrank_252d_base_v015_signal(ps, revenue):
    g = _growth(revenue, 252)
    peg = _peg(ps, g)
    sub1 = ((peg > 0) & (peg < 1.0)).astype(float)
    result = sub1.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v016 EV/Sales PEG momentum (change over a quarter)
def f44vg_f44_valuation_vs_growth_evspegmom_252d_base_v016_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    peg = _peg(evs, g)
    result = peg - peg.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v017 P/S PEG curvature (second difference; re-rating acceleration)
def f44vg_f44_valuation_vs_growth_pspegmom_252d_base_v017_signal(ps, revenue):
    g = _growth(revenue, 252)
    peg = _peg(ps, g)
    result = peg - 2.0 * peg.shift(42) + peg.shift(84)
    return result.replace([np.inf, -np.inf], np.nan)


# v018 multiple-growth divergence: log EV/Sales change minus log revenue growth change
def f44vg_f44_valuation_vs_growth_multgrodiv_252d_base_v018_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    dmult = _log_growth(evs, 63)
    dgro = _log_growth(revenue, 63)
    result = dmult - dgro
    return result.replace([np.inf, -np.inf], np.nan)


# v019 EV/Sales residual vs growth-implied fair multiple
def f44vg_f44_valuation_vs_growth_evsresid_252d_base_v019_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    implied = (1.0 + g).clip(lower=0.0) * _mean(evs, 252)
    result = (evs - implied) / implied.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v020 blended GARP cheapness: growth z minus avg of EV/Sales & P/S z (composite)
def f44vg_f44_valuation_vs_growth_garpblend_252d_base_v020_signal(ev, ps, revenue):
    evs = _evsales(ev, revenue)
    gz = _z(_growth(revenue, 252), 252)
    result = gz - (_z(evs, 252) + _z(ps, 252)) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# v021 growth-per-turn-of-EV/Sales (inverted PEG), de-trended vs own mean
def f44vg_f44_valuation_vs_growth_gropermult_252d_base_v021_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / evs.replace(0, np.nan)
    result = inv - _mean(inv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v022 growth-per-turn-of-P/S, percentile-ranked (GARP attractiveness percentile)
def f44vg_f44_valuation_vs_growth_groperps_252d_base_v022_signal(ps, revenue):
    g = _growth(revenue, 252)
    inv = (g * 100.0) / ps.replace(0, np.nan)
    result = _rank(inv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v023 growth-per-turn-of-EV/EBITDA, percentile-ranked vs own 2yr history
def f44vg_f44_valuation_vs_growth_gropereveb_252d_base_v023_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    inv = (g * 100.0) / evebitda.replace(0, np.nan)
    result = _rank(inv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v024 FCF-yield-plus-growth momentum (change over a quarter)
def f44vg_f44_valuation_vs_growth_fcfgroz_252d_base_v024_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    cg = yld + g
    result = cg - cg.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025 rule-of-40 distance above the 0.40 hurdle, smoothed (continuous GARP-quality)
def f44vg_f44_valuation_vs_growth_r40score_252d_base_v025_signal(revenue, fcf):
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    r40 = g + margin
    excess = r40 - 0.40
    result = excess.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v026 r40 score per turn of EV/Sales, percentile-ranked (efficiency of GARP)
def f44vg_f44_valuation_vs_growth_r40perevs_252d_base_v026_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    r = (g + margin) / evs.replace(0, np.nan)
    result = _rank(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v027 acceleration-adjusted PEG: EV/Sales over revenue-growth acceleration
def f44vg_f44_valuation_vs_growth_evsaccpeg_252d_base_v027_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = (g_now - g_prev)
    result = evs / (accel * 100.0).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v028 cheapness conditioned on positive growth regime (EV/Sales counts only when growing)
def f44vg_f44_valuation_vs_growth_condcheap_252d_base_v028_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    sign = (g > 0).astype(float)
    result = -_z(evs, 126) * sign
    return result.replace([np.inf, -np.inf], np.nan)


# v029 EV/EBITDA PEG with revenue-growth fallback, momentum form
def f44vg_f44_valuation_vs_growth_evebpegrk_252d_base_v029_signal(evebitda, ebitda, revenue):
    geb = _growth(ebitda, 252)
    g = geb.where(geb.abs() > 0.01, _growth(revenue, 252))
    peg = _peg(evebitda, g)
    result = peg - peg.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v030 growth surprise vs valuation: revenue-growth z minus EV/Sales z
def f44vg_f44_valuation_vs_growth_grosurp_252d_base_v030_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    gz = _z(_growth(revenue, 126), 252)
    vz = _z(evs, 252)
    result = gz - vz
    return result.replace([np.inf, -np.inf], np.nan)


# v031 FCF-yield-to-growth (yield-PEG), sign-aware
def f44vg_f44_valuation_vs_growth_fcfyldpeg_252d_base_v031_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    result = yld / (g.abs() + 0.05) * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


# v032 EV/Sales cheap-and-growing fraction (regime streak over last quarter)
def f44vg_f44_valuation_vs_growth_cheapstreak_252d_base_v032_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    cheap = ((evs < _median(evs, 252)) & (g > 0)).astype(float)
    result = cheap.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v033 growth-weighted EV/Sales discount to history
def f44vg_f44_valuation_vs_growth_groweighted_252d_base_v033_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    disc = _mean(evs, 252) / evs.replace(0, np.nan) - 1.0
    result = disc * (1.0 + g.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)


# v034 P/S vs EV/Sales spread normalized by growth (capital-structure GARP nuance)
def f44vg_f44_valuation_vs_growth_psevsspr_252d_base_v034_signal(ps, ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    result = (evs - ps) / (g.abs() * 100.0 + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# v035 EBITDA-growth-adjusted EV/EBITDA discount momentum (change over a quarter)
def f44vg_f44_valuation_vs_growth_evebdisc_252d_base_v035_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    disc = _mean(evebitda, 504) / evebitda.replace(0, np.nan) - 1.0
    score = disc + g
    result = score - score.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v036 forward EV/Sales relief percentile (how cheap the growth-adjusted multiple ranks)
def f44vg_f44_valuation_vs_growth_fwdevs_252d_base_v036_signal(ev, revenue):
    g = _growth(revenue, 252)
    fwd_rev = revenue * (1.0 + g)
    evs_fwd = ev / fwd_rev.replace(0, np.nan)
    result = _rank(evs_fwd, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v037 forward P/S compression, z-scored vs its own 1yr history (de-trended relief)
def f44vg_f44_valuation_vs_growth_fwdpscomp_252d_base_v037_signal(ps, revenue):
    g = _growth(revenue, 252)
    fwd_ps = ps / (1.0 + g).replace(0, np.nan)
    comp = (ps - fwd_ps) / ps.replace(0, np.nan)
    result = _z(comp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v038 GARP composite z: growth z minus avg valuation z (EV/Sales & EV/EBITDA)
def f44vg_f44_valuation_vs_growth_garpcompz_252d_base_v038_signal(ev, revenue, evebitda, ebitda):
    evs = _evsales(ev, revenue)
    gz = (_z(_growth(revenue, 252), 252) + _z(_growth(ebitda, 252), 252)) / 2.0
    vz = (_z(evs, 252) + _z(evebitda, 252)) / 2.0
    result = gz - vz
    return result.replace([np.inf, -np.inf], np.nan)


# v039 EV/Sales PEG dispersion across growth windows, ranked (read-stability percentile)
def f44vg_f44_valuation_vs_growth_pegdisp_252d_base_v039_signal(ev, ps, revenue):
    evs = _evsales(ev, revenue)
    p1 = _peg(evs, _growth(revenue, 63))
    p2 = _peg(evs, _growth(revenue, 126))
    p3 = _peg(ps, _growth(revenue, 252))
    disp = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = _rank(disp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v040 mature-GARP positive regime: fraction of last year (fcf-yld + ebitda-growth) > 0
def f44vg_f44_valuation_vs_growth_fcfebgrank_252d_base_v040_signal(fcf, marketcap, ebitda):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(ebitda, 252)
    pos = (yld + g > 0).astype(float)
    result = pos.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# v041 EV/Sales PEG using 2yr CAGR growth (smoother denom), level
def f44vg_f44_valuation_vs_growth_evscagrpeg_504d_base_v041_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    cagr = (revenue / revenue.shift(504).replace(0, np.nan)) ** (252.0 / 504.0) - 1.0
    result = _peg(evs, cagr)
    return result.replace([np.inf, -np.inf], np.nan)


# v042 P/S PEG (2yr CAGR) momentum (change over a quarter)
def f44vg_f44_valuation_vs_growth_pscagrpeg_504d_base_v042_signal(ps, revenue):
    cagr = (revenue / revenue.shift(504).replace(0, np.nan)) ** (252.0 / 504.0) - 1.0
    peg = _peg(ps, cagr)
    result = peg - peg.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043 growth durability discount: EV/Sales penalized by growth volatility
def f44vg_f44_valuation_vs_growth_durabledisc_252d_base_v043_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 63)
    gvol = _std(g, 252)
    result = -evs / (1.0 + gvol * 5.0)
    return result.replace([np.inf, -np.inf], np.nan)


# v044 market-implied vs delivered growth gap (EV/Sales required vs revenue delivered)
def f44vg_f44_valuation_vs_growth_impliedgap_252d_base_v044_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    required = evs / _mean(evs, 504).replace(0, np.nan) - 1.0
    delivered = _growth(revenue, 252)
    result = delivered - required
    return result.replace([np.inf, -np.inf], np.nan)


# v045 EV/EBITDA-to-growth PEG curvature (second difference)
def f44vg_f44_valuation_vs_growth_evebpegmom_252d_base_v045_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    peg = _peg(evebitda, g)
    result = peg - 2.0 * peg.shift(42) + peg.shift(84)
    return result.replace([np.inf, -np.inf], np.nan)


# v046 total GARP: (yield + growth) minus EV/Sales z, percentile-ranked
def f44vg_f44_valuation_vs_growth_totalgarp_252d_base_v046_signal(fcf, marketcap, revenue, ev):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    evs = _evsales(ev, revenue)
    raw = (yld + g) - _z(evs, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v047 EV/Sales PEG regime distance from its 2yr median (in std units)
def f44vg_f44_valuation_vs_growth_pegregdist_252d_base_v047_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    med = _median(peg, 504)
    sd = _std(peg, 504)
    result = (peg - med) / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v048 growth per turn of marketcap-to-revenue, momentum (change over a quarter)
def f44vg_f44_valuation_vs_growth_mcaprevgro_252d_base_v048_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / mc_rev.replace(0, np.nan)
    result = inv - inv.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049 EBITDA-margin-expansion-adjusted EV/EBITDA (growth in profitability cheapness)
def f44vg_f44_valuation_vs_growth_margexpadj_252d_base_v049_signal(evebitda, ebitda, revenue):
    margin = _safe_div(ebitda, revenue)
    dmargin = margin - margin.shift(252)
    result = -evebitda / (1.0 + (dmargin * 10.0).clip(lower=-0.9))
    return result.replace([np.inf, -np.inf], np.nan)


# v050 revenue-growth-to-EV/EBITDA cross multiple regime distance from its 2yr median
def f44vg_f44_valuation_vs_growth_revgroeveb_252d_base_v050_signal(evebitda, revenue):
    g = _growth(revenue, 252)
    cross = (g * 100.0) / evebitda.replace(0, np.nan)
    result = (cross - _median(cross, 504)) / _std(cross, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v051 EV/Sales PEG cheapness depth: avg distance below 1.0 when PEG is positive-and-cheap
def f44vg_f44_valuation_vs_growth_pegsub1_252d_base_v051_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    depth = (1.0 - peg).where(peg > 0, np.nan).clip(lower=0)
    result = depth.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v052 growth-funded valuation: revenue log-growth minus log-change in EV
def f44vg_f44_valuation_vs_growth_grovsev_252d_base_v052_signal(ev, revenue):
    g = _log_growth(revenue, 252)
    de = _log_growth(ev, 252)
    result = g - de
    return result.replace([np.inf, -np.inf], np.nan)


# v053 P/S cheapness x revenue-growth interaction (sign x sqrt-magnitude)
def f44vg_f44_valuation_vs_growth_psgrointer_252d_base_v053_signal(ps, revenue):
    cheap = -_z(ps, 252)
    g = _z(_growth(revenue, 252), 252)
    result = np.sign(cheap) * np.sign(g) * (cheap.abs() * g.abs()) ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# v054 FCF-yield growth-tilt (yield scaled by revenue-growth acceleration)
def f44vg_f44_valuation_vs_growth_fcfyldtilt_252d_base_v054_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    result = yld * (1.0 + accel.clip(lower=-0.5))
    return result.replace([np.inf, -np.inf], np.nan)


# v055 EV/Sales PEG vol-of-PEG (instability of the GARP read over a year)
def f44vg_f44_valuation_vs_growth_pegcurv_252d_base_v055_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    result = _std(peg.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v056 blended valuation z minus blended growth z (composite mispricing, P/S & EV/EBITDA)
def f44vg_f44_valuation_vs_growth_blendmispr_252d_base_v056_signal(ps, evebitda, revenue, ebitda):
    vz = (_z(ps, 126) + _z(evebitda, 126)) / 2.0
    gz = (_z(_growth(revenue, 126), 126) + _z(_growth(ebitda, 126), 126)) / 2.0
    result = gz - vz
    return result.replace([np.inf, -np.inf], np.nan)


# v057 P/S PEG asymmetry: fraction of last year PEG sat above its 2yr median
def f44vg_f44_valuation_vs_growth_pegspread_252d_base_v057_signal(ps, revenue):
    g = _growth(revenue, 252)
    peg = _peg(ps, g)
    above = (peg > _median(peg, 504)).astype(float)
    result = above.rolling(252, min_periods=63).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# v058 EV/EBITDA residual vs growth-implied fair multiple
def f44vg_f44_valuation_vs_growth_evebresid_252d_base_v058_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    implied = (1.0 + g).clip(lower=0.0) * _mean(evebitda, 252)
    result = (evebitda - implied) / implied.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# v059 growth-adjusted EV/Sales smoothed (persistent GARP cheapness)
def f44vg_f44_valuation_vs_growth_garpsmooth_252d_base_v059_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    raw = g - _z(evs, 252)
    result = raw.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v060 rule-of-40-adjusted EV/EBITDA, momentum (change over a quarter)
def f44vg_f44_valuation_vs_growth_r40eveb_252d_base_v060_signal(evebitda, ebitda, revenue):
    g = _growth(ebitda, 252)
    margin = _safe_div(ebitda, revenue)
    r = _rule40_mult(evebitda, g, margin)
    result = r - r.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061 small-cap GARP: growth per marketcap-turn plus fcf yield, z-scored
def f44vg_f44_valuation_vs_growth_smallgarp_252d_base_v061_signal(marketcap, revenue, fcf):
    g = _growth(revenue, 252)
    mc_rev = _safe_div(marketcap, revenue)
    yld = _fcf_yield(fcf, marketcap)
    raw = (g / mc_rev.replace(0, np.nan)) + yld
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v062 PEG percentile flip: 2yr rank minus 63d rank of EV/Sales PEG (regime shift)
def f44vg_f44_valuation_vs_growth_pegflip_252d_base_v062_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    result = _rank(peg, 504) - _rank(peg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v063 cheap-and-accelerating intensity: low EV/Sales z AND positive growth accel
def f44vg_f44_valuation_vs_growth_cheapaccel_252d_base_v063_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    vz = _z(evs, 252)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    result = (-vz).clip(lower=0) * accel
    return result.replace([np.inf, -np.inf], np.nan)


# v064 growth-adjusted P/FCF multiple (GARP P/FCF-G), ranked
def f44vg_f44_valuation_vs_growth_pfcfg_252d_base_v064_signal(marketcap, fcf, revenue):
    pfcf = _safe_div(marketcap, fcf)
    g = _growth(revenue, 252)
    peg = pfcf / (g * 100.0).replace(0, np.nan)
    result = _rank(peg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v065 cheap EV/Sales x improving EBITDA margin (cheap + improving profitability)
def f44vg_f44_valuation_vs_growth_cheapmargin_252d_base_v065_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    disc = -_z(evs, 252)
    margin = _safe_div(ebitda, revenue)
    dmargin = margin - margin.shift(126)
    result = disc * np.sign(dmargin) * (dmargin.abs() * 10.0)
    return result.replace([np.inf, -np.inf], np.nan)


# v066 revenue-growth-yield (Δrevenue / EV) z-scored vs its own 2yr history
def f44vg_f44_valuation_vs_growth_grevperev_252d_base_v066_signal(ev, revenue):
    rev_grow = revenue - revenue.shift(252)
    yld = _safe_div(rev_grow, ev)
    result = _z(yld, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v067 cross-multiple PEG disagreement, z-scored (coefficient-of-variation of PEGs)
def f44vg_f44_valuation_vs_growth_multpegdisp_252d_base_v067_signal(ev, ps, evebitda, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    p1 = _peg(evs, g)
    p2 = _peg(ps, g)
    p3 = _peg(evebitda, g)
    stk = pd.concat([p1, p2, p3], axis=1)
    cv = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    result = _z(cv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# v068 growth-quality GARP: low growth-vol x cheap EV/Sales, smoothed momentum
def f44vg_f44_valuation_vs_growth_qualgarp_252d_base_v068_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 63)
    stability = 1.0 / (1.0 + _std(g, 252) * 5.0)
    raw = stability * (-_z(evs, 252))
    result = raw - raw.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# v069 EV/EBITDA-to-growth PEG tanh-squashed (bounded PEG)
def f44vg_f44_valuation_vs_growth_evebpegtanh_252d_base_v069_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    peg = _peg(evebitda, g)
    result = np.tanh(peg / 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# v070 fcf-yield-plus-growth minus its own 2yr mean (de-trended cheap-growth)
def f44vg_f44_valuation_vs_growth_fcfgrodetr_252d_base_v070_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    cg = yld + g
    result = cg - _mean(cg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# v071 growth-paid ratio (marketcap-to-revenue PEG) tanh-squashed level (bounded GARP)
def f44vg_f44_valuation_vs_growth_mcrevpegrk_252d_base_v071_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    peg = mc_rev / (g * 100.0).replace(0, np.nan)
    result = np.tanh((peg - 1.0) / 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# v072 inverse EV/Sales PEG (growth per multiple) year-over-year change
def f44vg_f44_valuation_vs_growth_invpegrank_252d_base_v072_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / evs.replace(0, np.nan)
    result = inv - inv.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# v073 EBITDA-growth premium to EV/EBITDA z (mispricing on the profit line)
def f44vg_f44_valuation_vs_growth_ebgromispr_252d_base_v073_signal(evebitda, ebitda):
    gz = _z(_growth(ebitda, 126), 252)
    vz = _z(evebitda, 252)
    result = gz - vz
    return result.replace([np.inf, -np.inf], np.nan)


# v074 growth-adjusted cheapness change over a quarter (GARP score delta)
def f44vg_f44_valuation_vs_growth_garpdelta_252d_base_v074_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    score = g - _z(evs, 252)
    result = score - score.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# v075 total-GARP composite: blended inverse-PEG across all three multiples
def f44vg_f44_valuation_vs_growth_garpall_252d_base_v075_signal(ev, ps, evebitda, revenue, ebitda):
    g_rev = _growth(revenue, 252) * 100.0
    g_eb = _growth(ebitda, 252) * 100.0
    evs = _evsales(ev, revenue)
    a = g_rev / evs.replace(0, np.nan)
    b = g_rev / ps.replace(0, np.nan)
    c = g_eb / evebitda.replace(0, np.nan)
    blended = (a + b + c) / 3.0
    result = _rank(blended, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44vg_f44_valuation_vs_growth_evspeg_252d_base_v001_signal,
    f44vg_f44_valuation_vs_growth_evspeg_126d_base_v002_signal,
    f44vg_f44_valuation_vs_growth_pspeg_252d_base_v003_signal,
    f44vg_f44_valuation_vs_growth_pspeg_63d_base_v004_signal,
    f44vg_f44_valuation_vs_growth_evebpeg_252d_base_v005_signal,
    f44vg_f44_valuation_vs_growth_evebrevpeg_252d_base_v006_signal,
    f44vg_f44_valuation_vs_growth_fcfyldgro_252d_base_v007_signal,
    f44vg_f44_valuation_vs_growth_fcfyldebg_252d_base_v008_signal,
    f44vg_f44_valuation_vs_growth_r40evs_252d_base_v009_signal,
    f44vg_f44_valuation_vs_growth_r40ps_252d_base_v010_signal,
    f44vg_f44_valuation_vs_growth_garp_evs_252d_base_v011_signal,
    f44vg_f44_valuation_vs_growth_garp_ps_252d_base_v012_signal,
    f44vg_f44_valuation_vs_growth_garp_eveb_252d_base_v013_signal,
    f44vg_f44_valuation_vs_growth_evspegrank_252d_base_v014_signal,
    f44vg_f44_valuation_vs_growth_pspegrank_252d_base_v015_signal,
    f44vg_f44_valuation_vs_growth_evspegmom_252d_base_v016_signal,
    f44vg_f44_valuation_vs_growth_pspegmom_252d_base_v017_signal,
    f44vg_f44_valuation_vs_growth_multgrodiv_252d_base_v018_signal,
    f44vg_f44_valuation_vs_growth_evsresid_252d_base_v019_signal,
    f44vg_f44_valuation_vs_growth_garpblend_252d_base_v020_signal,
    f44vg_f44_valuation_vs_growth_gropermult_252d_base_v021_signal,
    f44vg_f44_valuation_vs_growth_groperps_252d_base_v022_signal,
    f44vg_f44_valuation_vs_growth_gropereveb_252d_base_v023_signal,
    f44vg_f44_valuation_vs_growth_fcfgroz_252d_base_v024_signal,
    f44vg_f44_valuation_vs_growth_r40score_252d_base_v025_signal,
    f44vg_f44_valuation_vs_growth_r40perevs_252d_base_v026_signal,
    f44vg_f44_valuation_vs_growth_evsaccpeg_252d_base_v027_signal,
    f44vg_f44_valuation_vs_growth_condcheap_252d_base_v028_signal,
    f44vg_f44_valuation_vs_growth_evebpegrk_252d_base_v029_signal,
    f44vg_f44_valuation_vs_growth_grosurp_252d_base_v030_signal,
    f44vg_f44_valuation_vs_growth_fcfyldpeg_252d_base_v031_signal,
    f44vg_f44_valuation_vs_growth_cheapstreak_252d_base_v032_signal,
    f44vg_f44_valuation_vs_growth_groweighted_252d_base_v033_signal,
    f44vg_f44_valuation_vs_growth_psevsspr_252d_base_v034_signal,
    f44vg_f44_valuation_vs_growth_evebdisc_252d_base_v035_signal,
    f44vg_f44_valuation_vs_growth_fwdevs_252d_base_v036_signal,
    f44vg_f44_valuation_vs_growth_fwdpscomp_252d_base_v037_signal,
    f44vg_f44_valuation_vs_growth_garpcompz_252d_base_v038_signal,
    f44vg_f44_valuation_vs_growth_pegdisp_252d_base_v039_signal,
    f44vg_f44_valuation_vs_growth_fcfebgrank_252d_base_v040_signal,
    f44vg_f44_valuation_vs_growth_evscagrpeg_504d_base_v041_signal,
    f44vg_f44_valuation_vs_growth_pscagrpeg_504d_base_v042_signal,
    f44vg_f44_valuation_vs_growth_durabledisc_252d_base_v043_signal,
    f44vg_f44_valuation_vs_growth_impliedgap_252d_base_v044_signal,
    f44vg_f44_valuation_vs_growth_evebpegmom_252d_base_v045_signal,
    f44vg_f44_valuation_vs_growth_totalgarp_252d_base_v046_signal,
    f44vg_f44_valuation_vs_growth_pegregdist_252d_base_v047_signal,
    f44vg_f44_valuation_vs_growth_mcaprevgro_252d_base_v048_signal,
    f44vg_f44_valuation_vs_growth_margexpadj_252d_base_v049_signal,
    f44vg_f44_valuation_vs_growth_revgroeveb_252d_base_v050_signal,
    f44vg_f44_valuation_vs_growth_pegsub1_252d_base_v051_signal,
    f44vg_f44_valuation_vs_growth_grovsev_252d_base_v052_signal,
    f44vg_f44_valuation_vs_growth_psgrointer_252d_base_v053_signal,
    f44vg_f44_valuation_vs_growth_fcfyldtilt_252d_base_v054_signal,
    f44vg_f44_valuation_vs_growth_pegcurv_252d_base_v055_signal,
    f44vg_f44_valuation_vs_growth_blendmispr_252d_base_v056_signal,
    f44vg_f44_valuation_vs_growth_pegspread_252d_base_v057_signal,
    f44vg_f44_valuation_vs_growth_evebresid_252d_base_v058_signal,
    f44vg_f44_valuation_vs_growth_garpsmooth_252d_base_v059_signal,
    f44vg_f44_valuation_vs_growth_r40eveb_252d_base_v060_signal,
    f44vg_f44_valuation_vs_growth_smallgarp_252d_base_v061_signal,
    f44vg_f44_valuation_vs_growth_pegflip_252d_base_v062_signal,
    f44vg_f44_valuation_vs_growth_cheapaccel_252d_base_v063_signal,
    f44vg_f44_valuation_vs_growth_pfcfg_252d_base_v064_signal,
    f44vg_f44_valuation_vs_growth_cheapmargin_252d_base_v065_signal,
    f44vg_f44_valuation_vs_growth_grevperev_252d_base_v066_signal,
    f44vg_f44_valuation_vs_growth_multpegdisp_252d_base_v067_signal,
    f44vg_f44_valuation_vs_growth_qualgarp_252d_base_v068_signal,
    f44vg_f44_valuation_vs_growth_evebpegtanh_252d_base_v069_signal,
    f44vg_f44_valuation_vs_growth_fcfgrodetr_252d_base_v070_signal,
    f44vg_f44_valuation_vs_growth_mcrevpegrk_252d_base_v071_signal,
    f44vg_f44_valuation_vs_growth_invpegrank_252d_base_v072_signal,
    f44vg_f44_valuation_vs_growth_ebgromispr_252d_base_v073_signal,
    f44vg_f44_valuation_vs_growth_garpdelta_252d_base_v074_signal,
    f44vg_f44_valuation_vs_growth_garpall_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_VALUATION_VS_GROWTH_REGISTRY_001_075 = REGISTRY


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

    print("OK f44_valuation_vs_growth_base_001_075_claude: %d features pass" % n_features)
