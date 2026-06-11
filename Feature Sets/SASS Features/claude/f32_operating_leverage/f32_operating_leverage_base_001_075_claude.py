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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _dlog(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s over a trailing window (per-step), normalized later by caller
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (operating leverage economics) =====
# Operating leverage = how profit responds to a change in revenue. Core building
# blocks below all encode the revenue-vs-profit-growth relationship.

def _f32_incr_margin(profit, revenue, w):
    # incremental margin = change in profit per unit change in revenue
    dp = profit - profit.shift(w)
    dr = revenue - revenue.shift(w)
    return dp / dr.replace(0, np.nan)


def _f32_dol(profit, revenue, w):
    # degree of operating leverage = %Δprofit / %Δrevenue
    gp_ = _dlog(profit.clip(lower=1e-9) if False else profit, w)
    gr = _dlog(revenue, w)
    gp2 = profit / profit.shift(w).replace(0, np.nan) - 1.0
    gr2 = revenue / revenue.shift(w).replace(0, np.nan) - 1.0
    return gp2 / gr2.replace(0, np.nan)


def _f32_growth_spread(profit, revenue, w):
    # profit-growth minus revenue-growth (log)
    return _dlog(profit.abs() + 1.0, w) - _dlog(revenue, w)


def _f32_opex_ratio(opex, revenue, w):
    # opex / revenue, smoothed (scale economies: falling ratio = leverage)
    r = opex / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f32_margin(profit, revenue):
    return profit / revenue.replace(0, np.nan)


def _f32_contrib(gp, opinc):
    # contribution-margin proxy: gp captures variable-cost margin, opinc net of
    # fixed costs; their gap reflects the fixed-cost block being absorbed.
    return (gp - opinc) / gp.replace(0, np.nan)


def _f32_absorption(profit, revenue, w):
    # fixed-cost absorption: how much margin expands as revenue scales
    m = profit / revenue.replace(0, np.nan)
    return m - m.shift(w)


# ============================================================
# --- incremental margin family (Δprofit / Δrevenue) ---

# incremental operating margin over 1y (Δopinc / Δrevenue)
def f32ol_f32_operating_leverage_incmgn_252d_base_v001_signal(opinc, revenue):
    b = _f32_incr_margin(opinc, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental operating margin over 2y
def f32ol_f32_operating_leverage_incmgn_504d_base_v002_signal(opinc, revenue):
    b = _f32_incr_margin(opinc, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental EBIT margin over 1y vs trailing EBIT margin (incremental premium)
def f32ol_f32_operating_leverage_incebitmgn_252d_base_v003_signal(ebit, revenue):
    im = _f32_incr_margin(ebit, revenue, 252)
    m = _f32_margin(ebit, revenue).shift(252)
    b = np.tanh((im - m) * 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin over 1y (Δgp / Δrevenue), de-meaned vs 2y history
def f32ol_f32_operating_leverage_incgpmgn_252d_base_v004_signal(gp, revenue):
    im = _f32_incr_margin(gp, revenue, 252)
    b = im - im.rolling(504, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin z-scored vs its own 252d history (de-trended leverage shift)
def f32ol_f32_operating_leverage_incmgnz_252d_base_v005_signal(opinc, revenue):
    im = _f32_incr_margin(opinc, revenue, 126)
    b = _z(im, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin: short-horizon vs long-horizon ratio (leverage acceleration)
def f32ol_f32_operating_leverage_incmgndisp_252d_base_v006_signal(opinc, revenue):
    short = _f32_incr_margin(opinc, revenue, 63)
    long = _f32_incr_margin(opinc, revenue, 252)
    b = np.tanh(short) - np.tanh(long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# spread: incremental opinc margin minus incremental gp margin (fixed-cost drag)
def f32ol_f32_operating_leverage_incspread_252d_base_v007_signal(opinc, gp, revenue):
    a = _f32_incr_margin(opinc, revenue, 252)
    c = _f32_incr_margin(gp, revenue, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental opinc margin (1y) vs incremental gp margin, ratio of contributions
def f32ol_f32_operating_leverage_incmgnrank_126d_base_v008_signal(opinc, gp, revenue):
    io = _f32_incr_margin(opinc, revenue, 252)
    ig = _f32_incr_margin(gp, revenue, 252)
    b = np.tanh(io) / (1.0 + np.tanh(ig).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental EBIT margin vs incremental opinc margin, ratio (below-the-line leverage)
def f32ol_f32_operating_leverage_incebspread_252d_base_v009_signal(ebit, opinc, revenue):
    a = _f32_incr_margin(ebit, revenue, 126)
    c = _f32_incr_margin(opinc, revenue, 126)
    b = np.tanh(a) * np.tanh(c) * np.sign(a - c)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin scaled by current op-margin (leverage relative to base profitability)
def f32ol_f32_operating_leverage_incmgnscaled_252d_base_v010_signal(opinc, revenue):
    im = _f32_incr_margin(opinc, revenue, 252)
    m = _f32_margin(opinc, revenue).replace(0, np.nan)
    b = np.tanh(im / m.abs().clip(lower=0.01))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- degree of operating leverage (DOL = %Δprofit / %Δrevenue) ---

# DOL of opinc over 1y
def f32ol_f32_operating_leverage_dol_252d_base_v011_signal(opinc, revenue):
    b = _f32_dol(opinc, revenue, 252)
    b = np.tanh(b / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL of ebit over 1y
def f32ol_f32_operating_leverage_dolebit_252d_base_v012_signal(ebit, revenue):
    b = _f32_dol(ebit, revenue, 252)
    b = np.tanh(b / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL of gp over 1y (gross operating leverage)
def f32ol_f32_operating_leverage_dolgp_252d_base_v013_signal(gp, revenue):
    b = _f32_dol(gp, revenue, 252)
    b = np.tanh(b / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL over 2y, squashed
def f32ol_f32_operating_leverage_dol_504d_base_v014_signal(opinc, revenue):
    b = _f32_dol(opinc, revenue, 504)
    b = np.tanh(b / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL change over a quarter (leverage regime shift)
def f32ol_f32_operating_leverage_dolmom_252d_base_v015_signal(opinc, revenue):
    d = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL z-scored vs its own 1y history
def f32ol_f32_operating_leverage_dolz_252d_base_v016_signal(opinc, revenue):
    d = np.tanh(_f32_dol(opinc, revenue, 126) / 5.0)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL dispersion across opinc vs ebit (which line carries the leverage)
def f32ol_f32_operating_leverage_doldisp_252d_base_v017_signal(opinc, ebit, revenue):
    d1 = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    d2 = np.tanh(_f32_dol(ebit, revenue, 252) / 5.0)
    b = (d1 - d2).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- profit-growth minus revenue-growth (operating-leverage spread) ---

# opinc-growth minus revenue-growth, 1y
def f32ol_f32_operating_leverage_gspread_252d_base_v018_signal(opinc, revenue):
    b = _f32_growth_spread(opinc, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-growth minus revenue-growth, 1y
def f32ol_f32_operating_leverage_gspreadebit_252d_base_v019_signal(ebit, revenue):
    b = _f32_growth_spread(ebit, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth minus revenue-growth, 1y (variable-cost leverage)
def f32ol_f32_operating_leverage_gspreadgp_252d_base_v020_signal(gp, revenue):
    b = _f32_growth_spread(gp, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-growth minus revenue-growth, 2y
def f32ol_f32_operating_leverage_gspread_504d_base_v021_signal(opinc, revenue):
    b = _f32_growth_spread(opinc, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread half-year
def f32ol_f32_operating_leverage_gspread_126d_base_v022_signal(opinc, revenue):
    b = _f32_growth_spread(opinc, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread z-scored vs 2y history
def f32ol_f32_operating_leverage_gspreadz_252d_base_v023_signal(opinc, revenue):
    g = _f32_growth_spread(opinc, revenue, 252)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth spread ranked vs 2y history
def f32ol_f32_operating_leverage_gspreadrank_252d_base_v024_signal(ebit, revenue):
    g = _f32_growth_spread(ebit, revenue, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread momentum (change over a quarter)
def f32ol_f32_operating_leverage_gspreadmom_252d_base_v025_signal(opinc, revenue):
    g = _f32_growth_spread(opinc, revenue, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of spreads: opinc-spread minus gp-spread (fixed vs variable contribution)
def f32ol_f32_operating_leverage_gsprdspr_252d_base_v026_signal(opinc, gp, revenue):
    a = _f32_growth_spread(opinc, revenue, 252)
    c = _f32_growth_spread(gp, revenue, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread smoothed (durable leverage)
def f32ol_f32_operating_leverage_gspreadema_252d_base_v027_signal(opinc, revenue):
    g = _f32_growth_spread(opinc, revenue, 252)
    b = g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opex / revenue trend (scale economies) ---

# opex/revenue level, 1y smoothed (lower = more scale)
def f32ol_f32_operating_leverage_opexrev_252d_base_v028_signal(opex, revenue):
    b = _f32_opex_ratio(opex, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex/revenue trend (slope over 1y; negative = improving scale economies)
def f32ol_f32_operating_leverage_opexrevslope_252d_base_v029_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    b = -_slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex/revenue level vs its 2y minimum (proximity to best-ever scale efficiency)
def f32ol_f32_operating_leverage_opexrevchg_252d_base_v030_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    floor = r.rolling(504, min_periods=126).min()
    b = (r - floor) / floor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex/revenue z-scored vs 2y history
def f32ol_f32_operating_leverage_opexrevz_252d_base_v031_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    b = -_z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-growth minus revenue-growth (opex scaling slower than sales = leverage)
def f32ol_f32_operating_leverage_opexgspr_252d_base_v032_signal(opex, revenue):
    b = _dlog(revenue, 252) - _dlog(opex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-growth minus revenue-growth, 2y
def f32ol_f32_operating_leverage_opexgspr_504d_base_v033_signal(opex, revenue):
    b = _dlog(revenue, 504) - _dlog(opex, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental opex per incremental revenue (marginal cost ratio)
def f32ol_f32_operating_leverage_incopex_252d_base_v034_signal(opex, revenue):
    dox = opex - opex.shift(252)
    dr = revenue - revenue.shift(252)
    b = 1.0 - dox / dr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex/revenue trend momentum (acceleration of scale economies)
def f32ol_f32_operating_leverage_opexrevmom_252d_base_v035_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    chg = r.shift(126) - r
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fixed-cost absorption (margin expansion as revenue scales) ---

# op-margin expansion over 1y (fixed-cost absorption)
def f32ol_f32_operating_leverage_absorb_252d_base_v036_signal(opinc, revenue):
    b = _f32_absorption(opinc, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-margin expansion stability: absorption smoothness over 2y (durable scaling)
def f32ol_f32_operating_leverage_absorbebit_252d_base_v037_signal(ebit, revenue):
    m = _f32_margin(ebit, revenue)
    dm = m - m.shift(63)
    pos = (dm > 0).astype(float).rolling(504, min_periods=126).mean()
    b = (pos - 0.5) * np.tanh(dm.rolling(252, min_periods=126).mean() * 50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion conditioned on revenue actually growing (true absorption)
def f32ol_f32_operating_leverage_absorbcond_252d_base_v038_signal(opinc, revenue):
    dm = _f32_absorption(opinc, revenue, 252)
    grow = (revenue > revenue.shift(252)).astype(float)
    b = dm * grow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion per unit of revenue growth (absorption efficiency), ranked
def f32ol_f32_operating_leverage_absorbeff_252d_base_v039_signal(opinc, revenue):
    dm = _f32_absorption(opinc, revenue, 126)
    gr = _roc(revenue, 126)
    eff = dm / gr.replace(0, np.nan)
    b = _rank(eff, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion slope over 1y (steady absorption rate)
def f32ol_f32_operating_leverage_absorbslope_252d_base_v040_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    b = _slope(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-margin expansion relative to op-margin expansion (variable vs total absorption)
def f32ol_f32_operating_leverage_absorbgp_252d_base_v041_signal(gp, opinc, revenue):
    ag = _f32_absorption(gp, revenue, 252)
    ao = _f32_absorption(opinc, revenue, 252)
    b = np.tanh((ao - ag) * 30.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year margin absorption, ranked
def f32ol_f32_operating_leverage_absorbrank_126d_base_v042_signal(opinc, revenue):
    dm = _f32_absorption(opinc, revenue, 126)
    b = _rank(dm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- contribution-margin proxy (gp vs opinc) ---

# fixed-cost block share: (gp - opinc)/gp
def f32ol_f32_operating_leverage_contrib_base_v043_signal(gp, opinc):
    b = _f32_contrib(gp, opinc)
    b = b.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in fixed-cost share over 1y (operating-leverage shift)
def f32ol_f32_operating_leverage_contribchg_252d_base_v044_signal(gp, opinc):
    c = _f32_contrib(gp, opinc)
    b = c.shift(252) - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-to-opinc conversion volatility (instability of fixed-cost absorption)
def f32ol_f32_operating_leverage_gp2opinc_base_v045_signal(gp, opinc):
    r = opinc / gp.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).std() * np.sign(r.rolling(126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend in opinc/gp conversion (rising = fixed costs being absorbed)
def f32ol_f32_operating_leverage_gp2opincslope_252d_base_v046_signal(gp, opinc):
    r = opinc / gp.replace(0, np.nan)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# contribution leverage: opinc-growth vs gp-growth gap, conditioned on gp rising
def f32ol_f32_operating_leverage_contriblev_252d_base_v047_signal(gp, opinc):
    sp = _f32_growth_spread(opinc, gp, 126)
    cond = np.tanh(_roc(gp, 126) * 5.0)
    b = sp * cond
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost share z-scored vs 2y history
def f32ol_f32_operating_leverage_contribz_252d_base_v048_signal(gp, opinc):
    c = _f32_contrib(gp, opinc)
    b = -_z(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied fixed-cost dollar level (gp - opinc) growth vs revenue growth
def f32ol_f32_operating_leverage_fixedcostgr_252d_base_v049_signal(gp, opinc, revenue):
    fc = (gp - opinc)
    b = _dlog(revenue, 252) - _dlog(fc.abs() + 1.0, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- margins as leverage state + their interactions ---

# operating margin level (smoothed)
def f32ol_f32_operating_leverage_opmgn_base_v050_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    b = m.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin x revenue-growth (profitable growth = leverage payoff)
def f32ol_f32_operating_leverage_mgnxgrowth_252d_base_v051_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    gr = _roc(revenue, 252)
    b = m * gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-trend x revenue-growth (expanding-margin growth)
def f32ol_f32_operating_leverage_trendxgrowth_252d_base_v052_signal(opinc, revenue):
    dm = _f32_absorption(opinc, revenue, 126)
    gr = _roc(revenue, 126)
    b = np.sign(dm) * np.sqrt(np.abs(dm)) * gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-margin minus op-margin (fixed-cost wedge) trend
def f32ol_f32_operating_leverage_mgnwedge_252d_base_v053_signal(gp, opinc, revenue):
    gm = _f32_margin(gp, revenue)
    om = _f32_margin(opinc, revenue)
    wedge = gm - om
    b = wedge.shift(252) - wedge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-margin minus op-margin spread trend (non-operating drag direction)
def f32ol_f32_operating_leverage_ebitwedge_252d_base_v054_signal(ebit, opinc, revenue):
    em = _f32_margin(ebit, revenue)
    om = _f32_margin(opinc, revenue)
    wedge = em - om
    b = _slope(wedge, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin z-score (leverage-state extremity)
def f32ol_f32_operating_leverage_opmgnz_504d_base_v055_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    b = _z(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin rank vs 2y history
def f32ol_f32_operating_leverage_opmgnrank_504d_base_v056_signal(ebit, revenue):
    m = _f32_margin(ebit, revenue)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- second-order leverage descriptors ---

# leverage consistency: fraction of last year opinc grew faster than revenue
def f32ol_f32_operating_leverage_levhitrate_252d_base_v057_signal(opinc, revenue):
    go = _roc(opinc, 63)
    gr = _roc(revenue, 63)
    win = (go > gr).astype(float)
    b = win.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage stability: inverse dispersion of incremental margin
def f32ol_f32_operating_leverage_levstab_252d_base_v058_signal(opinc, revenue):
    im = _f32_incr_margin(opinc, revenue, 63)
    sd = im.rolling(252, min_periods=126).std()
    b = 1.0 / (1.0 + sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asymmetry: incremental margin when revenue up vs down (downside leverage)
def f32ol_f32_operating_leverage_levasym_252d_base_v059_signal(opinc, revenue):
    do = opinc - opinc.shift(63)
    dr = revenue - revenue.shift(63)
    up = (dr > 0).astype(float)
    contrib = do / dr.replace(0, np.nan)
    up_m = (contrib * up).rolling(252, min_periods=126).sum() / up.rolling(252, min_periods=126).sum().replace(0, np.nan)
    dn_m = (contrib * (1 - up)).rolling(252, min_periods=126).sum() / (1 - up).rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = up_m - dn_m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x op-margin-trend sign agreement (clean leverage)
def f32ol_f32_operating_leverage_levagree_252d_base_v060_signal(opinc, revenue):
    gr = _roc(revenue, 252)
    dm = _f32_absorption(opinc, revenue, 252)
    b = np.sign(gr) * np.sign(dm) * (gr.abs() + dm.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage elasticity via opex: -%Δ(opex/rev) per %Δrevenue
def f32ol_f32_operating_leverage_opexelast_252d_base_v061_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    dr_pct = _roc(revenue, 252)
    dratio = r / r.shift(252).replace(0, np.nan) - 1.0
    b = -dratio / dr_pct.replace(0, np.nan)
    b = np.tanh(b)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL via break-even identity: gp/opinc = revenue/(revenue-breakeven), x revenue-growth
def f32ol_f32_operating_leverage_breakeven_252d_base_v062_signal(gp, opinc, revenue):
    dol_identity = gp / opinc.replace(0, np.nan)
    dol_identity = np.tanh(dol_identity / 5.0)
    gr = _roc(revenue, 252)
    b = dol_identity * np.sign(gr) * (1.0 + gr.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage payoff: opinc-growth scaled by revenue-growth magnitude
def f32ol_f32_operating_leverage_levpayoff_252d_base_v063_signal(opinc, revenue):
    go = _dlog(opinc.abs() + 1.0, 252)
    gr = _dlog(revenue, 252)
    b = go * np.sign(gr) * (1.0 + gr.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon DOL agreement (short vs long leverage consistency)
def f32ol_f32_operating_leverage_dolmulti_base_v064_signal(opinc, revenue):
    d1 = np.tanh(_f32_dol(opinc, revenue, 126) / 5.0)
    d2 = np.tanh(_f32_dol(opinc, revenue, 504) / 5.0)
    b = (d1 + d2) / 2.0 - (d1 - d2).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental EBIT margin smoothed and ranked (durable bottom-line leverage)
def f32ol_f32_operating_leverage_incebitrank_252d_base_v065_signal(ebit, revenue):
    im = _f32_incr_margin(ebit, revenue, 252).ewm(span=63, min_periods=21).mean()
    b = _rank(im, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus opex-growth, z-scored (scale-economy extremity)
def f32ol_f32_operating_leverage_scalez_252d_base_v066_signal(opex, revenue):
    g = _dlog(revenue, 252) - _dlog(opex, 252)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-growth x op-margin level (variable leverage at high margin)
def f32ol_f32_operating_leverage_gpgrowxmgn_252d_base_v067_signal(gp, opinc, revenue):
    gg = _roc(gp, 252)
    om = _f32_margin(opinc, revenue)
    b = gg * om
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage acceleration: change in growth-spread acceleration
def f32ol_f32_operating_leverage_levaccel_252d_base_v068_signal(ebit, revenue):
    g = _f32_growth_spread(ebit, revenue, 126)
    b = g - 2.0 * g.shift(63) + g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized incremental margin: Δopinc/Δrevenue minus Δgp/Δrevenue, smoothed
def f32ol_f32_operating_leverage_incnetfix_252d_base_v069_signal(opinc, gp, revenue):
    a = _f32_incr_margin(opinc, revenue, 252)
    c = _f32_incr_margin(gp, revenue, 252)
    b = (a - c).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale vs fixed-cost block: log(revenue) minus log(gp-opinc)
def f32ol_f32_operating_leverage_scalefix_base_v070_signal(gp, opinc, revenue):
    fc = (gp - opinc).abs() + 1.0
    b = np.log(revenue.replace(0, np.nan)) - np.log(fc)
    b = b - b.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op-margin trend per unit revenue-growth volatility (clean leverage signal)
def f32ol_f32_operating_leverage_levclean_252d_base_v071_signal(opinc, revenue):
    dm = _f32_absorption(opinc, revenue, 126)
    grvol = _roc(revenue, 21).rolling(126, min_periods=63).std()
    ratio = dm / (grvol + 1e-6)
    b = _z(np.tanh(ratio * 0.5), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit incremental margin x opex elasticity (two leverage views, interaction)
def f32ol_f32_operating_leverage_levcombo_252d_base_v072_signal(ebit, opex, revenue):
    im = np.tanh(_f32_incr_margin(ebit, revenue, 252))
    r = opex / revenue.replace(0, np.nan)
    scale = np.tanh((r.shift(252) - r) * 20.0)
    b = im * (1.0 + scale) - scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage breadth: count of (opinc,ebit,gp) growing faster than revenue
def f32ol_f32_operating_leverage_levbreadth_252d_base_v073_signal(opinc, ebit, gp, revenue):
    gr = _roc(revenue, 252)
    s1 = np.tanh((_roc(opinc, 252) - gr) * 3.0)
    s2 = np.tanh((_roc(ebit, 252) - gr) * 3.0)
    s3 = np.tanh((_roc(gp, 252) - gr) * 3.0)
    b = (s1 + s2 + s3) / 3.0
    b = b.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost coverage: opinc relative to the fixed-cost block, trend
def f32ol_f32_operating_leverage_fixcover_252d_base_v074_signal(gp, opinc):
    fc = (gp - opinc)
    cover = opinc / fc.replace(0, np.nan)
    cover = np.tanh(cover / 3.0)
    b = cover - cover.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite leverage score: rank-blend of growth-spread, absorption, scale-economy
def f32ol_f32_operating_leverage_levscore_252d_base_v075_signal(opinc, opex, revenue):
    gs = _rank(_f32_growth_spread(opinc, revenue, 252), 504)
    ab = _rank(_f32_absorption(opinc, revenue, 252), 504)
    sc = _rank(_dlog(revenue, 252) - _dlog(opex, 252), 504)
    b = (gs + ab + sc) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32ol_f32_operating_leverage_incmgn_252d_base_v001_signal,
    f32ol_f32_operating_leverage_incmgn_504d_base_v002_signal,
    f32ol_f32_operating_leverage_incebitmgn_252d_base_v003_signal,
    f32ol_f32_operating_leverage_incgpmgn_252d_base_v004_signal,
    f32ol_f32_operating_leverage_incmgnz_252d_base_v005_signal,
    f32ol_f32_operating_leverage_incmgndisp_252d_base_v006_signal,
    f32ol_f32_operating_leverage_incspread_252d_base_v007_signal,
    f32ol_f32_operating_leverage_incmgnrank_126d_base_v008_signal,
    f32ol_f32_operating_leverage_incebspread_252d_base_v009_signal,
    f32ol_f32_operating_leverage_incmgnscaled_252d_base_v010_signal,
    f32ol_f32_operating_leverage_dol_252d_base_v011_signal,
    f32ol_f32_operating_leverage_dolebit_252d_base_v012_signal,
    f32ol_f32_operating_leverage_dolgp_252d_base_v013_signal,
    f32ol_f32_operating_leverage_dol_504d_base_v014_signal,
    f32ol_f32_operating_leverage_dolmom_252d_base_v015_signal,
    f32ol_f32_operating_leverage_dolz_252d_base_v016_signal,
    f32ol_f32_operating_leverage_doldisp_252d_base_v017_signal,
    f32ol_f32_operating_leverage_gspread_252d_base_v018_signal,
    f32ol_f32_operating_leverage_gspreadebit_252d_base_v019_signal,
    f32ol_f32_operating_leverage_gspreadgp_252d_base_v020_signal,
    f32ol_f32_operating_leverage_gspread_504d_base_v021_signal,
    f32ol_f32_operating_leverage_gspread_126d_base_v022_signal,
    f32ol_f32_operating_leverage_gspreadz_252d_base_v023_signal,
    f32ol_f32_operating_leverage_gspreadrank_252d_base_v024_signal,
    f32ol_f32_operating_leverage_gspreadmom_252d_base_v025_signal,
    f32ol_f32_operating_leverage_gsprdspr_252d_base_v026_signal,
    f32ol_f32_operating_leverage_gspreadema_252d_base_v027_signal,
    f32ol_f32_operating_leverage_opexrev_252d_base_v028_signal,
    f32ol_f32_operating_leverage_opexrevslope_252d_base_v029_signal,
    f32ol_f32_operating_leverage_opexrevchg_252d_base_v030_signal,
    f32ol_f32_operating_leverage_opexrevz_252d_base_v031_signal,
    f32ol_f32_operating_leverage_opexgspr_252d_base_v032_signal,
    f32ol_f32_operating_leverage_opexgspr_504d_base_v033_signal,
    f32ol_f32_operating_leverage_incopex_252d_base_v034_signal,
    f32ol_f32_operating_leverage_opexrevmom_252d_base_v035_signal,
    f32ol_f32_operating_leverage_absorb_252d_base_v036_signal,
    f32ol_f32_operating_leverage_absorbebit_252d_base_v037_signal,
    f32ol_f32_operating_leverage_absorbcond_252d_base_v038_signal,
    f32ol_f32_operating_leverage_absorbeff_252d_base_v039_signal,
    f32ol_f32_operating_leverage_absorbslope_252d_base_v040_signal,
    f32ol_f32_operating_leverage_absorbgp_252d_base_v041_signal,
    f32ol_f32_operating_leverage_absorbrank_126d_base_v042_signal,
    f32ol_f32_operating_leverage_contrib_base_v043_signal,
    f32ol_f32_operating_leverage_contribchg_252d_base_v044_signal,
    f32ol_f32_operating_leverage_gp2opinc_base_v045_signal,
    f32ol_f32_operating_leverage_gp2opincslope_252d_base_v046_signal,
    f32ol_f32_operating_leverage_contriblev_252d_base_v047_signal,
    f32ol_f32_operating_leverage_contribz_252d_base_v048_signal,
    f32ol_f32_operating_leverage_fixedcostgr_252d_base_v049_signal,
    f32ol_f32_operating_leverage_opmgn_base_v050_signal,
    f32ol_f32_operating_leverage_mgnxgrowth_252d_base_v051_signal,
    f32ol_f32_operating_leverage_trendxgrowth_252d_base_v052_signal,
    f32ol_f32_operating_leverage_mgnwedge_252d_base_v053_signal,
    f32ol_f32_operating_leverage_ebitwedge_252d_base_v054_signal,
    f32ol_f32_operating_leverage_opmgnz_504d_base_v055_signal,
    f32ol_f32_operating_leverage_opmgnrank_504d_base_v056_signal,
    f32ol_f32_operating_leverage_levhitrate_252d_base_v057_signal,
    f32ol_f32_operating_leverage_levstab_252d_base_v058_signal,
    f32ol_f32_operating_leverage_levasym_252d_base_v059_signal,
    f32ol_f32_operating_leverage_levagree_252d_base_v060_signal,
    f32ol_f32_operating_leverage_opexelast_252d_base_v061_signal,
    f32ol_f32_operating_leverage_breakeven_252d_base_v062_signal,
    f32ol_f32_operating_leverage_levpayoff_252d_base_v063_signal,
    f32ol_f32_operating_leverage_dolmulti_base_v064_signal,
    f32ol_f32_operating_leverage_incebitrank_252d_base_v065_signal,
    f32ol_f32_operating_leverage_scalez_252d_base_v066_signal,
    f32ol_f32_operating_leverage_gpgrowxmgn_252d_base_v067_signal,
    f32ol_f32_operating_leverage_levaccel_252d_base_v068_signal,
    f32ol_f32_operating_leverage_incnetfix_252d_base_v069_signal,
    f32ol_f32_operating_leverage_scalefix_base_v070_signal,
    f32ol_f32_operating_leverage_levclean_252d_base_v071_signal,
    f32ol_f32_operating_leverage_levcombo_252d_base_v072_signal,
    f32ol_f32_operating_leverage_levbreadth_252d_base_v073_signal,
    f32ol_f32_operating_leverage_fixcover_252d_base_v074_signal,
    f32ol_f32_operating_leverage_levscore_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_OPERATING_LEVERAGE_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    revenue = _fund(101, base=1e9, drift=0.03, vol=0.05).rename("revenue")
    opex = _fund(102, base=6e8, drift=0.025, vol=0.05).rename("opex")
    gp = _fund(103, base=4e8, drift=0.03, vol=0.06).rename("gp")
    opinc = _fund(104, base=1.5e8, drift=0.03, vol=0.09, allow_neg=True).rename("opinc")
    ebit = _fund(105, base=1.4e8, drift=0.03, vol=0.10, allow_neg=True).rename("ebit")

    cols = {"revenue": revenue, "opex": opex, "gp": gp, "opinc": opinc, "ebit": ebit}

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

    print("OK f32_operating_leverage_base_001_075_claude: %d features pass" % n_features)
