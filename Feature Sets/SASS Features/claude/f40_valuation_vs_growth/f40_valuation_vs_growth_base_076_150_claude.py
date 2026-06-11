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
    def _f(a):
        mlen = len(a)
        idx = np.arange(mlen, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (GARP: valuation x growth) =====
def _grw(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _grw_ann(s, w):
    g = s / s.shift(w).replace(0, np.nan)
    return g ** (252.0 / w) - 1.0


def _grw_pct(s, w):
    return s.pct_change().rolling(w, min_periods=max(2, w // 2)).mean()


def _peg(mult, growth_pct):
    g = (growth_pct * 100.0).replace(0, np.nan)
    return mult / g


def _earnyield(netinc, marketcap):
    return _safe_div(netinc, marketcap)


def _fcfyield(fcf, marketcap):
    return _safe_div(fcf, marketcap)


def _evsales(ev, revenue):
    return _safe_div(ev, revenue)


def _ebitda_yield(ebitda, ev):
    return _safe_div(ebitda, ev)


def _margin(num, den):
    return _safe_div(num, den)


# ============================================================
# --- growth-quality interactions with valuation ---

# revenue-growth x earnings-yield, both ranked, summed (cheap-and-growing)
def f40vg_f40_valuation_vs_growth_grwey_rev_252d_base_v076_signal(revenue, netinc, marketcap):
    g = _rank(_grw(revenue, 252), 504)
    ey = _rank(_earnyield(netinc, marketcap), 504)
    b = g + ey
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-margin level x EBITDA-growth divided by EV/EBITDA (quality GARP)
def f40vg_f40_valuation_vs_growth_marginvg_ebitda_252d_base_v077_signal(ebitda, revenue, evebitda):
    margin = _margin(ebitda, revenue)
    g = _grw(ebitda, 252)
    b = _safe_div(margin * (1.0 + g), evebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin trajectory minus EV/Sales z (improving-cash-cheap)
def f40vg_f40_valuation_vs_growth_fcfmargvg_252d_base_v078_signal(fcf, revenue, ev):
    fm = _margin(fcf, revenue)
    fmtrend = fm - fm.shift(252)
    evs = _evsales(ev, revenue)
    b = _z(fmtrend, 126) - _z(evs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG penalized by inverse margin (cheap growth that is also profitable)
def f40vg_f40_valuation_vs_growth_pegmargin_252d_base_v079_signal(pe, revenue, netinc):
    peg = _peg(pe, _grw(revenue, 252))
    nm = _margin(netinc, revenue)
    b = peg * (1.0 - np.tanh(nm))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted EV/EBITDA combined with EBITDA margin level, z-summed
def f40vg_f40_valuation_vs_growth_evebmargin_252d_base_v080_signal(evebitda, ebitda, revenue):
    g = _grw(ebitda, 252)
    margin = _margin(ebitda, revenue)
    b = -_z(_peg(evebitda, g), 252) + _z(margin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation-vs-growth divergence / re-rating ---

# divergence: re-rating of EV/Sales vs revenue-growth trajectory
def f40vg_f40_valuation_vs_growth_rerate_evs_252d_base_v081_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    evtrend = evs / evs.shift(63) - 1.0
    gtrend = _grw(revenue, 63)
    b = evtrend - gtrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PE re-rating relative to earnings-growth re-rating (overshoot signal)
def f40vg_f40_valuation_vs_growth_rerate_pe_252d_base_v082_signal(pe, netinc):
    petrend = pe / pe.shift(63) - 1.0
    gtrend = _grw(netinc, 63)
    b = petrend - gtrend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA multiple change minus EBITDA-growth change (multiple vs fundamentals)
def f40vg_f40_valuation_vs_growth_rerate_eveb_252d_base_v083_signal(evebitda, ebitda):
    mtrend = evebitda - evebitda.shift(126)
    g = _grw(ebitda, 126)
    gchg = g - g.shift(63)
    b = _z(mtrend, 126) - _z(gchg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheapness-growth gap mean reversion: PEG minus its 252d median proxy
def f40vg_f40_valuation_vs_growth_pegmr_rev_252d_base_v084_signal(pe, revenue):
    peg = _peg(pe, _grw(revenue, 252))
    b = peg - peg.rolling(252, min_periods=63).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-EBITDA-growth mean reversion gap, z-scored
def f40vg_f40_valuation_vs_growth_evsgmr_rev_252d_base_v085_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _grw(ebitda, 252))
    b = _z(peg - peg.rolling(252, min_periods=63).median(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-multiple GARP composites ---

# blended cheapness z minus blended growth z (value-tilt residual)
def f40vg_f40_valuation_vs_growth_blendgap_252d_base_v086_signal(pe, evebitda, ps, revenue, ebitda):
    cheap = (_z(pe, 252) + _z(evebitda, 252) + _z(ps, 252)) / 3.0
    grow = (_z(_grw(revenue, 252), 252) + _z(_grw(ebitda, 252), 252)) / 2.0
    b = -cheap + grow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of inverse-PE-PEG times rank of EBITDA-yield (double cheap grower)
def f40vg_f40_valuation_vs_growth_dblrank_252d_base_v087_signal(pe, revenue, ebitda, ev):
    invpeg = _safe_div(_grw(revenue, 252) * 100.0, pe.replace(0, np.nan))
    eby = _ebitda_yield(ebitda, ev)
    b = _rank(invpeg, 252) + _rank(eby, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP harmonic blend: 2/(1/invpeg_rev + 1/invpeg_ebitda)
def f40vg_f40_valuation_vs_growth_harmgarp_252d_base_v088_signal(pe, evebitda, revenue, ebitda):
    a = _safe_div(_grw(revenue, 252) * 100.0, pe.replace(0, np.nan))
    c = _safe_div(_grw(ebitda, 252) * 100.0, evebitda.replace(0, np.nan))
    b = 2.0 / (1.0 / a.replace(0, np.nan) + 1.0 / c.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between cheapest and most-expensive growth-adjusted multiple
def f40vg_f40_valuation_vs_growth_multispread_252d_base_v089_signal(pe, evebitda, ps, ev, revenue, ebitda):
    p1 = _z(_peg(pe, _grw(revenue, 252)), 252)
    p2 = _z(_peg(evebitda, _grw(ebitda, 252)), 252)
    p3 = _z(_peg(ps, _grw(revenue, 252)), 252)
    p4 = _z(_peg(_evsales(ev, revenue), _grw(revenue, 252)), 252)
    stacked = pd.concat([p1, p2, p3, p4], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean of growth-adjusted yields minus PEG-cheapness (net GARP attractiveness level)
def f40vg_f40_valuation_vs_growth_multidisp_252d_base_v090_signal(netinc, fcf, marketcap, revenue, pe):
    ey = _earnyield(netinc, marketcap)
    fy = _fcfyield(fcf, marketcap)
    g = _grw(revenue, 252)
    yieldleg = _z((ey + fy) * (1.0 + g), 252)
    pegleg = _z(_peg(pe, g), 252)
    b = yieldleg - pegleg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-acceleration adjusted valuation ---

# invPEG scaled by growth acceleration sign (accelerating cheap grower)
def f40vg_f40_valuation_vs_growth_accelgarp_rev_252d_base_v091_signal(pe, revenue):
    g = _grw(revenue, 126)
    accel = g - g.shift(63)
    invpeg = _safe_div(g * 100.0, pe.replace(0, np.nan))
    b = invpeg * np.tanh(5.0 * accel)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-growth-acceleration over EV/EBITDA (cheap accelerating cashflow)
def f40vg_f40_valuation_vs_growth_accel_eveb_252d_base_v092_signal(evebitda, ebitda):
    g = _grw(ebitda, 126)
    accel = g - g.shift(63)
    b = _safe_div(accel, evebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# second difference of revenue-growth divided by PE (growth convexity vs price)
def f40vg_f40_valuation_vs_growth_grwconvex_252d_base_v093_signal(pe, revenue):
    g = _grw(revenue, 63)
    convex = g - 2.0 * g.shift(21) + g.shift(42)
    b = _safe_div(convex, pe)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield-plus-growth (Rule-of-40 family extensions) ---

# EBITDA-yield + EBITDA-growth (EV-based Rule-of-40)
def f40vg_f40_valuation_vs_growth_evr40_ebitda_252d_base_v094_signal(ebitda, ev):
    eby = _ebitda_yield(ebitda, ev)
    g = _grw(ebitda, 252)
    b = _z(eby, 126) + _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-yield + revenue-growth, smoothed (cheap-revenue compounder)
def f40vg_f40_valuation_vs_growth_salesr40_252d_base_v095_signal(revenue, marketcap):
    sy = _safe_div(revenue, marketcap)
    g = _grw(revenue, 252)
    raw = _z(sy, 126) + _z(g, 126)
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-yield + net-income-growth, ranked (cheap earnings grower)
def f40vg_f40_valuation_vs_growth_earnr40_252d_base_v096_signal(netinc, marketcap):
    ey = _earnyield(netinc, marketcap)
    g = _grw(netinc, 252)
    b = _rank(ey, 252) + _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 with margin-improvement instead of pure growth
def f40vg_f40_valuation_vs_growth_marginr40_252d_base_v097_signal(fcf, marketcap, ebitda, revenue):
    fy = _fcfyield(fcf, marketcap)
    margin = _margin(ebitda, revenue)
    mimp = margin - margin.shift(126)
    b = _z(fy, 126) + _z(mimp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-yield ratios ---

# revenue-growth divided by sales-yield-inverse (growth per dollar of price-to-sales)
def f40vg_f40_valuation_vs_growth_grwperps_252d_base_v098_signal(ps, revenue):
    g = _grw(revenue, 252)
    b = _safe_div(g, ps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-growth divided by PE (earnings-growth yield per multiple turn)
def f40vg_f40_valuation_vs_growth_grwperpe_252d_base_v099_signal(pe, netinc):
    g = _grw(netinc, 252)
    b = _safe_div(g, pe)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-growth divided by EV/Sales (cash-growth per sales-turn)
def f40vg_f40_valuation_vs_growth_grwperevs_252d_base_v100_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    g = _grw(fcf, 252)
    b = _safe_div(g, evs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PEG on different windows / annualization ---

# PEG with 126d annualized revenue growth, ranked
def f40vg_f40_valuation_vs_growth_pegann_rev_126d_base_v101_signal(pe, revenue):
    g = _grw_ann(revenue, 126)
    b = _rank(_peg(pe, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-annualized-EBITDA-growth (126d), z-scored
def f40vg_f40_valuation_vs_growth_pegann_eveb_126d_base_v102_signal(evebitda, ebitda):
    g = _grw_ann(ebitda, 126)
    b = _z(_peg(evebitda, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG using growth measured over 504d but multiple averaged over 63d (smoothed multiple)
def f40vg_f40_valuation_vs_growth_pegsm_rev_504d_base_v103_signal(pe, revenue):
    pe_sm = _mean(pe, 63)
    g = _grw(revenue, 504)
    b = _peg(pe_sm, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-stability adjusted valuation ---

# EV/EBITDA invPEG times EBITDA-growth-consistency, z-scored (stable cheap cashflow)
def f40vg_f40_valuation_vs_growth_pegconsist_rev_252d_base_v104_signal(evebitda, ebitda):
    g = _grw(ebitda, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    invpeg = _safe_div(_grw(ebitda, 252) * 100.0, evebitda.replace(0, np.nan))
    b = _z(invpeg * consist, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-revenue-growth divided by growth dispersion, z-scored (stable cheap grower)
def f40vg_f40_valuation_vs_growth_pegstabeb_252d_base_v105_signal(evebitda, revenue):
    g = _grw(revenue, 252)
    disp = _grw(revenue, 63).rolling(252, min_periods=63).std()
    invpeg = _safe_div(g * 100.0, evebitda.replace(0, np.nan))
    b = _z(invpeg / (1.0 + 10.0 * disp), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient-of-variation of revenue growth penalizing PEG-rank
def f40vg_f40_valuation_vs_growth_grwcv_rev_252d_base_v106_signal(pe, revenue):
    g = _grw(revenue, 63)
    cv = g.rolling(252, min_periods=63).std() / g.rolling(252, min_periods=63).mean().abs().replace(0, np.nan)
    pegr = _rank(_peg(pe, _grw(revenue, 252)), 252)
    b = -pegr - _z(cv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-fundamental growth-vs-valuation ---

# revenue-growth vs earnings-growth spread divided by PE (growth-quality cheapness)
def f40vg_f40_valuation_vs_growth_grwspread_252d_base_v107_signal(pe, revenue, netinc):
    gr = _grw(revenue, 252)
    gn = _grw(netinc, 252)
    b = _safe_div(gn - gr, pe)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-growth minus revenue-growth (operating leverage) over EV/EBITDA
def f40vg_f40_valuation_vs_growth_oplevvg_252d_base_v108_signal(evebitda, ebitda, revenue):
    gE = _grw(ebitda, 252)
    gR = _grw(revenue, 252)
    b = _safe_div(gE - gR, evebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-growth minus net-income-growth (cash-quality growth) over PE
def f40vg_f40_valuation_vs_growth_cashqualvg_252d_base_v109_signal(pe, fcf, netinc):
    gF = _grw(fcf, 252)
    gN = _grw(netinc, 252)
    b = _safe_div(gF - gN, pe)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation level vs growth rank interactions ---

# z(earnings yield) gated by high growth (only counts when growth above median)
def f40vg_f40_valuation_vs_growth_gatedey_252d_base_v110_signal(netinc, marketcap, revenue):
    ey = _z(_earnyield(netinc, marketcap), 252)
    g = _grw(revenue, 252)
    gate = (_rank(g, 504) + 0.5)
    b = ey * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z(FCF yield) gated by high EBITDA growth
def f40vg_f40_valuation_vs_growth_gatedfcf_252d_base_v111_signal(fcf, marketcap, ebitda):
    fy = _z(_fcfyield(fcf, marketcap), 252)
    g = _grw(ebitda, 252)
    gate = (_rank(g, 504) + 0.5)
    b = fy * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# -z(EV/Sales) gated by revenue-growth above its own trend
def f40vg_f40_valuation_vs_growth_gatedevs_252d_base_v112_signal(ev, revenue):
    evs = _z(_evsales(ev, revenue), 252)
    g = _grw(revenue, 126)
    above = (g > g.rolling(252, min_periods=63).mean()).astype(float)
    b = -evs * above
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-adjusted yields ranked / smoothed ---

# growth-adjusted earnings yield smoothed (EMA) and de-meaned
def f40vg_f40_valuation_vs_growth_gaeysm_252d_base_v113_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    g = _grw(revenue, 252)
    raw = ey * (1.0 + g)
    sm = raw.ewm(span=63, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted FCF yield ranked vs 504d history
def f40vg_f40_valuation_vs_growth_gafcfrank_252d_base_v114_signal(fcf, marketcap, ebitda):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(ebitda, 252)
    raw = fy * (1.0 + g)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted EBITDA yield z-score
def f40vg_f40_valuation_vs_growth_gaebyz_252d_base_v115_signal(ebitda, ev):
    eby = _ebitda_yield(ebitda, ev)
    g = _grw(ebitda, 252)
    b = _z(eby * (1.0 + g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PEG momentum / trajectory family ---

# invPEG momentum over a half-year (improving GARP attractiveness)
def f40vg_f40_valuation_vs_growth_invpegmom_rev_252d_base_v116_signal(pe, revenue):
    invpeg = _safe_div(_grw(revenue, 252) * 100.0, pe.replace(0, np.nan))
    b = invpeg - invpeg.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth momentum (quarterly), z-scored
def f40vg_f40_valuation_vs_growth_evebgmomz_252d_base_v117_signal(evebitda, ebitda):
    peg = _peg(evebitda, _grw(ebitda, 252))
    mom = peg - peg.shift(63)
    b = _z(mom, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 acceleration (change in fcf-yield+growth over two quarters)
def f40vg_f40_valuation_vs_growth_r40accel_252d_base_v118_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(revenue, 252)
    r40 = fy + g
    b = (r40 - r40.shift(63)) - (r40.shift(63) - r40.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted earnings-yield momentum ranked
def f40vg_f40_valuation_vs_growth_gaeymomrank_252d_base_v119_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    g = _grw(revenue, 252)
    raw = ey * (1.0 + g)
    mom = raw - raw.shift(63)
    b = _rank(mom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fair-multiple gaps ---

# fair-PE gap: PE minus net-income-growth-points, ranked (Lynch fair line on earnings)
def f40vg_f40_valuation_vs_growth_fairpe_rev_252d_base_v120_signal(pe, netinc):
    g = _grw(netinc, 252) * 100.0
    b = _rank(pe - g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fair-EV/Sales gap: EV/Sales minus growth-implied band, ranked (FCF-growth band)
def f40vg_f40_valuation_vs_growth_fairevs_252d_base_v121_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    g = _grw(fcf, 252)
    band = 1.0 + 2.0 * g
    b = _rank(evs - band, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fair-EV/EBITDA gap: EV/EBITDA minus FCF-growth-points, smoothed and de-meaned
def f40vg_f40_valuation_vs_growth_faireveb_252d_base_v122_signal(evebitda, fcf):
    g = _grw(fcf, 252) * 100.0
    gap = evebitda - 0.5 * g
    sm = gap.ewm(span=63, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- size / scale adjusted GARP ---

# invPEG times log-marketcap rank (large-cap-tilted GARP)
def f40vg_f40_valuation_vs_growth_sizegarp_252d_base_v123_signal(pe, revenue, marketcap):
    invpeg = _safe_div(_grw(revenue, 252) * 100.0, pe.replace(0, np.nan))
    sz = _rank(np.log(marketcap.replace(0, np.nan)), 504)
    b = invpeg * (0.5 - sz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth per unit EV (scale-aware growth value)
def f40vg_f40_valuation_vs_growth_grwperev_252d_base_v124_signal(ev, revenue):
    g = _grw(revenue, 252)
    sales_to_ev = _safe_div(revenue, ev)
    b = g * sales_to_ev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-growth per unit marketcap, ranked (small earnings-grower premium)
def f40vg_f40_valuation_vs_growth_grwpermc_252d_base_v125_signal(marketcap, netinc):
    g = _grw(netinc, 252)
    ni_to_mc = _safe_div(netinc, marketcap)
    b = _rank(g * ni_to_mc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite GARP scores ---

# full multi-leg GARP z-score (cheap on 4 multiples, growing on 3 fundamentals)
def f40vg_f40_valuation_vs_growth_megacomp_252d_base_v126_signal(pe, evebitda, ps, ev, revenue, ebitda, netinc):
    evs = _evsales(ev, revenue)
    cheap = -(_z(pe, 252) + _z(evebitda, 252) + _z(ps, 252) + _z(evs, 252))
    grow = (_z(_grw(revenue, 252), 252) + _z(_grw(ebitda, 252), 252) + _z(_grw(netinc, 252), 252))
    b = cheap + grow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP rank-sum: rank(growth legs) minus rank(valuation legs)
def f40vg_f40_valuation_vs_growth_ranksum_252d_base_v127_signal(pe, evebitda, revenue, ebitda):
    grow = _rank(_grw(revenue, 252), 504) + _rank(_grw(ebitda, 252), 504)
    cheap = _rank(pe, 504) + _rank(evebitda, 504)
    b = grow - cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded GARP: squashed (growth-z minus valuation-z) on FCF & PE
def f40vg_f40_valuation_vs_growth_tanhgarp_fcf_252d_base_v128_signal(pe, fcf, marketcap):
    fy = _fcfyield(fcf, marketcap)
    gF = _grw(fcf, 252)
    score = _z(fy, 252) + _z(gF, 252) - _z(pe, 252)
    b = np.tanh(0.4 * score)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- inflection / turnaround GARP ---

# growth inflection (growth crossing above zero) weighted by cheapness
def f40vg_f40_valuation_vs_growth_inflection_rev_252d_base_v129_signal(pe, revenue):
    g = _grw(revenue, 126)
    infl = ((g > 0) & (g.shift(63) <= 0)).astype(float)
    rate = infl.rolling(252, min_periods=126).mean()
    cheap = -_z(pe, 252)
    b = rate + 0.3 * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-to-positive-EBITDA-growth at low EV/EBITDA (cheap turnaround)
def f40vg_f40_valuation_vs_growth_turngarp_eveb_252d_base_v130_signal(evebitda, ebitda):
    g = _grw(ebitda, 126)
    positive = (g > 0).astype(float)
    streak = positive.rolling(63, min_periods=21).mean()
    cheap = -_z(evebitda, 252)
    b = streak * 0.5 + 0.5 * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- valuation-vs-growth z-divergence over time ---

# z(PEG) minus z(invPEG-rank) is degenerate; use PE-yield vs growth divergence trend
def f40vg_f40_valuation_vs_growth_ydiv_252d_base_v131_signal(netinc, marketcap, revenue):
    ey = _z(_earnyield(netinc, marketcap), 252)
    g = _z(_grw(revenue, 252), 252)
    div = ey - g
    b = div - div.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales z minus EBITDA-growth z, smoothed (expensive-on-slowing signal)
def f40vg_f40_valuation_vs_growth_evgdiv_252d_base_v132_signal(ev, revenue, ebitda):
    evs = _z(_evsales(ev, revenue), 252)
    g = _z(_grw(ebitda, 252), 252)
    b = (evs - g).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional PEG variants on FCF / netinc ---

# FCF-PEG ranked (cash PEG percentile)
def f40vg_f40_valuation_vs_growth_fcfpegrank_252d_base_v133_signal(pe, fcf):
    g = _grw(fcf, 252)
    b = _rank(_peg(pe, g), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-PEG z-scored (earnings PEG de-trended)
def f40vg_f40_valuation_vs_growth_nipegz_252d_base_v134_signal(pe, netinc):
    g = _grw(netinc, 252)
    b = _z(_peg(pe, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-FCF-growth (cross: cashflow growth vs EV multiple)
def f40vg_f40_valuation_vs_growth_evebfcfg_252d_base_v135_signal(evebitda, fcf):
    g = _grw(fcf, 252)
    b = _peg(evebitda, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S-to-EBITDA-growth ranked (sales multiple vs cashflow growth)
def f40vg_f40_valuation_vs_growth_psebg_252d_base_v136_signal(ps, ebitda):
    g = _grw(ebitda, 252)
    b = _rank(_peg(ps, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-yield products / GARP intensity ---

# sales-yield x EBITDA-margin x revenue-growth (compounder intensity)
def f40vg_f40_valuation_vs_growth_compintensity_252d_base_v137_signal(marketcap, revenue, ebitda):
    sy = _safe_div(revenue, marketcap)
    margin = _margin(ebitda, revenue)
    g = _grw(revenue, 252)
    b = _z(sy * margin * (1.0 + g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-yield x net-margin x earnings-growth (quality GARP intensity)
def f40vg_f40_valuation_vs_growth_qualintensity_252d_base_v138_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    nm = _margin(netinc, revenue)
    g = _grw(netinc, 252)
    b = _z(ey * (1.0 + nm) * (1.0 + g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-yield x FCF-margin x FCF-growth (cash compounder intensity)
def f40vg_f40_valuation_vs_growth_cashintensity_252d_base_v139_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    fm = _margin(fcf, revenue)
    g = _grw(fcf, 252)
    b = _z(fy * (1.0 + fm) * (1.0 + g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GARP relative to own history (re-rating vs growth) ---

# PE z minus revenue-growth z (cheap relative to own growth)
def f40vg_f40_valuation_vs_growth_relpe_rev_252d_base_v140_signal(pe, revenue):
    b = -_z(pe, 252) + _z(_grw(revenue, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA z minus EBITDA-growth z, ranked
def f40vg_f40_valuation_vs_growth_releveb_252d_base_v141_signal(evebitda, ebitda):
    raw = -_z(evebitda, 252) + _z(_grw(ebitda, 252), 252)
    b = _rank(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S z minus revenue-growth z, smoothed
def f40vg_f40_valuation_vs_growth_relps_rev_252d_base_v142_signal(ps, revenue):
    raw = -_z(ps, 252) + _z(_grw(revenue, 504), 252)
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- long-horizon GARP ---

# PEG using 504d growth and 252d-smoothed PE, z-scored (durable GARP)
def f40vg_f40_valuation_vs_growth_durablepeg_504d_base_v143_signal(pe, revenue):
    pe_sm = _mean(pe, 252)
    g = _grw(revenue, 504)
    b = _z(_peg(pe_sm, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-504d-EBITDA-growth ranked (durable cashflow GARP)
def f40vg_f40_valuation_vs_growth_durableeveb_504d_base_v144_signal(evebitda, ebitda):
    g = _grw(ebitda, 504)
    b = _rank(_peg(evebitda, g), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-year invPEG minus one-year invPEG (GARP horizon spread)
def f40vg_f40_valuation_vs_growth_horizonspread_252d_base_v145_signal(pe, revenue):
    ip2 = _safe_div(_grw(revenue, 504) * 100.0, pe.replace(0, np.nan))
    ip1 = _safe_div(_grw(revenue, 252) * 100.0, pe.replace(0, np.nan))
    b = ip2 - ip1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- final blended GARP scores ---

# GARP momentum composite: change in mega-cheapness-vs-growth over a quarter
def f40vg_f40_valuation_vs_growth_garpmomcomp_252d_base_v146_signal(pe, evebitda, revenue, ebitda):
    cheap = -(_z(pe, 252) + _z(evebitda, 252))
    grow = (_z(_grw(revenue, 252), 252) + _z(_grw(ebitda, 252), 252))
    score = cheap + grow
    b = score - score.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP dispersion across yields (earnings vs fcf vs ebitda yield) growth-weighted
def f40vg_f40_valuation_vs_growth_yielddisp_252d_base_v147_signal(netinc, fcf, ebitda, marketcap, ev, revenue):
    ey = _earnyield(netinc, marketcap)
    fy = _fcfyield(fcf, marketcap)
    eby = _ebitda_yield(ebitda, ev)
    g = (1.0 + _grw(revenue, 252))
    stacked = pd.concat([_z(ey, 252) * g, _z(fy, 252) * g, _z(eby, 252) * g], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP convexity: sign(EBITDA-growth) x sqrt(|invPEG on EV/EBITDA|), ranked
def f40vg_f40_valuation_vs_growth_garpconvex_252d_base_v148_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    invpeg = _safe_div(g * 100.0, evebitda.replace(0, np.nan))
    b = _rank(np.sign(g) * np.sqrt(invpeg.abs()), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-fundamental growth-momentum over blended cheapness (GARP thrust)
def f40vg_f40_valuation_vs_growth_garpthrust_252d_base_v149_signal(pe, evebitda, revenue, ebitda):
    gmom = (_grw(revenue, 63) - _grw(revenue, 252)) + (_grw(ebitda, 63) - _grw(ebitda, 252))
    cheap = -(_z(pe, 126) + _z(evebitda, 126)) / 2.0
    b = _z(gmom, 126) + cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capstone GARP: harmonic of growth-rank and cheapness-rank across all inputs
def f40vg_f40_valuation_vs_growth_capstone_252d_base_v150_signal(pe, evebitda, ps, ev, revenue, ebitda, fcf, netinc, marketcap):
    grow = (_rank(_grw(revenue, 252), 504) + _rank(_grw(ebitda, 252), 504)
            + _rank(_grw(netinc, 252), 504) + _rank(_grw(fcf, 252), 504)) / 4.0 + 0.5
    evs = _evsales(ev, revenue)
    cheap = (_rank(-pe, 504) + _rank(-evebitda, 504) + _rank(-ps, 504) + _rank(-evs, 504)) / 4.0 + 0.5
    b = 2.0 / (1.0 / grow.replace(0, np.nan) + 1.0 / cheap.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40vg_f40_valuation_vs_growth_grwey_rev_252d_base_v076_signal,
    f40vg_f40_valuation_vs_growth_marginvg_ebitda_252d_base_v077_signal,
    f40vg_f40_valuation_vs_growth_fcfmargvg_252d_base_v078_signal,
    f40vg_f40_valuation_vs_growth_pegmargin_252d_base_v079_signal,
    f40vg_f40_valuation_vs_growth_evebmargin_252d_base_v080_signal,
    f40vg_f40_valuation_vs_growth_rerate_evs_252d_base_v081_signal,
    f40vg_f40_valuation_vs_growth_rerate_pe_252d_base_v082_signal,
    f40vg_f40_valuation_vs_growth_rerate_eveb_252d_base_v083_signal,
    f40vg_f40_valuation_vs_growth_pegmr_rev_252d_base_v084_signal,
    f40vg_f40_valuation_vs_growth_evsgmr_rev_252d_base_v085_signal,
    f40vg_f40_valuation_vs_growth_blendgap_252d_base_v086_signal,
    f40vg_f40_valuation_vs_growth_dblrank_252d_base_v087_signal,
    f40vg_f40_valuation_vs_growth_harmgarp_252d_base_v088_signal,
    f40vg_f40_valuation_vs_growth_multispread_252d_base_v089_signal,
    f40vg_f40_valuation_vs_growth_multidisp_252d_base_v090_signal,
    f40vg_f40_valuation_vs_growth_accelgarp_rev_252d_base_v091_signal,
    f40vg_f40_valuation_vs_growth_accel_eveb_252d_base_v092_signal,
    f40vg_f40_valuation_vs_growth_grwconvex_252d_base_v093_signal,
    f40vg_f40_valuation_vs_growth_evr40_ebitda_252d_base_v094_signal,
    f40vg_f40_valuation_vs_growth_salesr40_252d_base_v095_signal,
    f40vg_f40_valuation_vs_growth_earnr40_252d_base_v096_signal,
    f40vg_f40_valuation_vs_growth_marginr40_252d_base_v097_signal,
    f40vg_f40_valuation_vs_growth_grwperps_252d_base_v098_signal,
    f40vg_f40_valuation_vs_growth_grwperpe_252d_base_v099_signal,
    f40vg_f40_valuation_vs_growth_grwperevs_252d_base_v100_signal,
    f40vg_f40_valuation_vs_growth_pegann_rev_126d_base_v101_signal,
    f40vg_f40_valuation_vs_growth_pegann_eveb_126d_base_v102_signal,
    f40vg_f40_valuation_vs_growth_pegsm_rev_504d_base_v103_signal,
    f40vg_f40_valuation_vs_growth_pegconsist_rev_252d_base_v104_signal,
    f40vg_f40_valuation_vs_growth_pegstabeb_252d_base_v105_signal,
    f40vg_f40_valuation_vs_growth_grwcv_rev_252d_base_v106_signal,
    f40vg_f40_valuation_vs_growth_grwspread_252d_base_v107_signal,
    f40vg_f40_valuation_vs_growth_oplevvg_252d_base_v108_signal,
    f40vg_f40_valuation_vs_growth_cashqualvg_252d_base_v109_signal,
    f40vg_f40_valuation_vs_growth_gatedey_252d_base_v110_signal,
    f40vg_f40_valuation_vs_growth_gatedfcf_252d_base_v111_signal,
    f40vg_f40_valuation_vs_growth_gatedevs_252d_base_v112_signal,
    f40vg_f40_valuation_vs_growth_gaeysm_252d_base_v113_signal,
    f40vg_f40_valuation_vs_growth_gafcfrank_252d_base_v114_signal,
    f40vg_f40_valuation_vs_growth_gaebyz_252d_base_v115_signal,
    f40vg_f40_valuation_vs_growth_invpegmom_rev_252d_base_v116_signal,
    f40vg_f40_valuation_vs_growth_evebgmomz_252d_base_v117_signal,
    f40vg_f40_valuation_vs_growth_r40accel_252d_base_v118_signal,
    f40vg_f40_valuation_vs_growth_gaeymomrank_252d_base_v119_signal,
    f40vg_f40_valuation_vs_growth_fairpe_rev_252d_base_v120_signal,
    f40vg_f40_valuation_vs_growth_fairevs_252d_base_v121_signal,
    f40vg_f40_valuation_vs_growth_faireveb_252d_base_v122_signal,
    f40vg_f40_valuation_vs_growth_sizegarp_252d_base_v123_signal,
    f40vg_f40_valuation_vs_growth_grwperev_252d_base_v124_signal,
    f40vg_f40_valuation_vs_growth_grwpermc_252d_base_v125_signal,
    f40vg_f40_valuation_vs_growth_megacomp_252d_base_v126_signal,
    f40vg_f40_valuation_vs_growth_ranksum_252d_base_v127_signal,
    f40vg_f40_valuation_vs_growth_tanhgarp_fcf_252d_base_v128_signal,
    f40vg_f40_valuation_vs_growth_inflection_rev_252d_base_v129_signal,
    f40vg_f40_valuation_vs_growth_turngarp_eveb_252d_base_v130_signal,
    f40vg_f40_valuation_vs_growth_ydiv_252d_base_v131_signal,
    f40vg_f40_valuation_vs_growth_evgdiv_252d_base_v132_signal,
    f40vg_f40_valuation_vs_growth_fcfpegrank_252d_base_v133_signal,
    f40vg_f40_valuation_vs_growth_nipegz_252d_base_v134_signal,
    f40vg_f40_valuation_vs_growth_evebfcfg_252d_base_v135_signal,
    f40vg_f40_valuation_vs_growth_psebg_252d_base_v136_signal,
    f40vg_f40_valuation_vs_growth_compintensity_252d_base_v137_signal,
    f40vg_f40_valuation_vs_growth_qualintensity_252d_base_v138_signal,
    f40vg_f40_valuation_vs_growth_cashintensity_252d_base_v139_signal,
    f40vg_f40_valuation_vs_growth_relpe_rev_252d_base_v140_signal,
    f40vg_f40_valuation_vs_growth_releveb_252d_base_v141_signal,
    f40vg_f40_valuation_vs_growth_relps_rev_252d_base_v142_signal,
    f40vg_f40_valuation_vs_growth_durablepeg_504d_base_v143_signal,
    f40vg_f40_valuation_vs_growth_durableeveb_504d_base_v144_signal,
    f40vg_f40_valuation_vs_growth_horizonspread_252d_base_v145_signal,
    f40vg_f40_valuation_vs_growth_garpmomcomp_252d_base_v146_signal,
    f40vg_f40_valuation_vs_growth_yielddisp_252d_base_v147_signal,
    f40vg_f40_valuation_vs_growth_garpconvex_252d_base_v148_signal,
    f40vg_f40_valuation_vs_growth_garpthrust_252d_base_v149_signal,
    f40vg_f40_valuation_vs_growth_capstone_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_VALUATION_VS_GROWTH_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    pe = _fund(1, base=20.0, drift=0.01, vol=0.06).rename("pe")
    evebitda = _fund(2, base=12.0, drift=0.01, vol=0.06).rename("evebitda")
    ps = _fund(3, base=4.0, drift=0.01, vol=0.06).rename("ps")
    marketcap = _fund(4, base=5e9, drift=0.02, vol=0.05).rename("marketcap")
    ev = _fund(5, base=6e9, drift=0.02, vol=0.05).rename("ev")
    revenue = _fund(6, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    ebitda = _fund(7, base=2e8, drift=0.03, vol=0.05).rename("ebitda")
    netinc = _fund(8, base=1.2e8, drift=0.025, vol=0.06, allow_neg=True).rename("netinc")
    fcf = _fund(9, base=1e8, drift=0.025, vol=0.06, allow_neg=True).rename("fcf")

    cols = {"pe": pe, "evebitda": evebitda, "ps": ps, "marketcap": marketcap,
            "ev": ev, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
            "fcf": fcf}

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

    print("OK f40_valuation_vs_growth_base_076_150_claude: %d features pass" % n_features)
