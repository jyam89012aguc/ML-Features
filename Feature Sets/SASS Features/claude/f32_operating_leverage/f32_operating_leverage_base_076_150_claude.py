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
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (operating leverage economics) =====
def _f32_incr_margin(profit, revenue, w):
    dp = profit - profit.shift(w)
    dr = revenue - revenue.shift(w)
    return dp / dr.replace(0, np.nan)


def _f32_dol(profit, revenue, w):
    gp2 = profit / profit.shift(w).replace(0, np.nan) - 1.0
    gr2 = revenue / revenue.shift(w).replace(0, np.nan) - 1.0
    return gp2 / gr2.replace(0, np.nan)


def _f32_growth_spread(profit, revenue, w):
    return _dlog(profit.abs() + 1.0, w) - _dlog(revenue, w)


def _f32_opex_ratio(opex, revenue, w):
    r = opex / revenue.replace(0, np.nan)
    return r.rolling(w, min_periods=max(1, w // 2)).mean()


def _f32_margin(profit, revenue):
    return profit / revenue.replace(0, np.nan)


def _f32_contrib(gp, opinc):
    return (gp - opinc) / gp.replace(0, np.nan)


def _f32_absorption(profit, revenue, w):
    m = profit / revenue.replace(0, np.nan)
    return m - m.shift(w)


# ============================================================
# --- elasticity & sensitivity (profit response to revenue) ---

# point elasticity of opinc to revenue (log-log local slope over 1y)
def f32ol_f32_operating_leverage_elast_252d_base_v076_signal(opinc, revenue):
    do = _dlog(opinc.abs() + 1.0, 252)
    dr = _dlog(revenue, 252)
    b = np.tanh(do / dr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity of gp to revenue (variable-cost elasticity)
def f32ol_f32_operating_leverage_elastgp_252d_base_v077_signal(gp, revenue):
    dg = _dlog(gp, 252)
    dr = _dlog(revenue, 252)
    b = np.tanh(dg / dr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity gap: opinc-elasticity minus gp-elasticity (fixed-cost leverage)
def f32ol_f32_operating_leverage_elastgap_252d_base_v078_signal(opinc, gp, revenue):
    eo = np.tanh(_dlog(opinc.abs() + 1.0, 252) / _dlog(revenue, 252).replace(0, np.nan))
    eg = np.tanh(_dlog(gp, 252) / _dlog(revenue, 252).replace(0, np.nan))
    b = eo - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity smoothed half-year then change over a quarter (elasticity momentum)
def f32ol_f32_operating_leverage_elastmom_252d_base_v079_signal(ebit, revenue):
    e = np.tanh(_dlog(ebit.abs() + 1.0, 126) / _dlog(revenue, 126).replace(0, np.nan))
    e = e.ewm(span=42, min_periods=21).mean()
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# elasticity dispersion across opinc/ebit/gp (which line is most levered)
def f32ol_f32_operating_leverage_elastdisp_252d_base_v080_signal(opinc, ebit, gp, revenue):
    dr = _dlog(revenue, 252).replace(0, np.nan)
    e1 = np.tanh(_dlog(opinc.abs() + 1.0, 252) / dr)
    e2 = np.tanh(_dlog(ebit.abs() + 1.0, 252) / dr)
    e3 = np.tanh(_dlog(gp, 252) / dr)
    b = pd.concat([e1, e2, e3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- revenue-per-opex efficiency (sales generated per cost dollar) ---

# revenue / opex level (sales efficiency)
def f32ol_f32_operating_leverage_salesperopex_base_v081_signal(revenue, opex):
    r = revenue / opex.replace(0, np.nan)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/opex trend (rising = scaling efficiency)
def f32ol_f32_operating_leverage_salesperopexslope_252d_base_v082_signal(revenue, opex):
    r = revenue / opex.replace(0, np.nan)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/opex z-scored vs 2y history (efficiency extremity)
def f32ol_f32_operating_leverage_salesperopexz_504d_base_v083_signal(revenue, opex):
    r = revenue / opex.replace(0, np.nan)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/opex change over 1y (operating-efficiency improvement)
def f32ol_f32_operating_leverage_salesperopexchg_252d_base_v084_signal(revenue, opex):
    r = revenue / opex.replace(0, np.nan)
    b = r / r.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opinc per revenue dynamics (margin path, leverage flavored) ---

# operating margin acceleration (2nd difference of margin level)
def f32ol_f32_operating_leverage_mgnaccel_252d_base_v085_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    b = m - 2.0 * m.shift(126) + m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin breakout vs trailing range (margin new-high proximity)
def f32ol_f32_operating_leverage_mgnbreakout_504d_base_v086_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    hi = m.rolling(504, min_periods=126).max()
    lo = m.rolling(504, min_periods=126).min()
    b = (m - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-margin breakout vs trailing range
def f32ol_f32_operating_leverage_ebitmgnbreakout_504d_base_v087_signal(ebit, revenue):
    m = _f32_margin(ebit, revenue)
    hi = m.rolling(504, min_periods=126).max()
    lo = m.rolling(504, min_periods=126).min()
    b = (m - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin drawdown from its 2y peak (operating deleverage stress)
def f32ol_f32_operating_leverage_mgndd_504d_base_v088_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    peak = m.rolling(504, min_periods=126).max()
    b = m - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin recovery off its 2y trough, scaled by time since the trough (releverage rate)
def f32ol_f32_operating_leverage_mgnrecov_504d_base_v089_signal(ebit, revenue):
    m = _f32_margin(ebit, revenue)
    trough = m.rolling(504, min_periods=126).min()
    rec = m - trough

    def _dst(a):
        if np.any(np.isnan(a)):
            return np.nan
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dst = m.rolling(504, min_periods=126).apply(_dst, raw=True).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-spread variations (profit vs revenue trajectory) ---

# profit-growth/revenue-growth ratio over 2y, squashed (durable DOL)
def f32ol_f32_operating_leverage_dolratio_504d_base_v090_signal(opinc, revenue):
    b = np.tanh(_f32_dol(opinc, revenue, 504) / 4.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread asymmetry: spread in up-revenue years minus down-revenue years
def f32ol_f32_operating_leverage_gspreadasym_504d_base_v091_signal(opinc, revenue):
    gs = _f32_growth_spread(opinc, revenue, 63)
    up = (_roc(revenue, 63) > 0).astype(float)
    up_m = (gs * up).rolling(504, min_periods=126).sum() / up.rolling(504, min_periods=126).sum().replace(0, np.nan)
    dn_m = (gs * (1 - up)).rolling(504, min_periods=126).sum() / (1 - up).rolling(504, min_periods=126).sum().replace(0, np.nan)
    b = up_m - dn_m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread consistency: fraction of quarters profit outgrew revenue
def f32ol_f32_operating_leverage_gspreadcons_252d_base_v092_signal(ebit, revenue):
    win = (_f32_growth_spread(ebit, revenue, 63) > 0).astype(float)
    b = win.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative leverage gap: sum of quarterly growth spreads over a year
def f32ol_f32_operating_leverage_gspreadcum_252d_base_v093_signal(opinc, revenue):
    gs = _f32_growth_spread(opinc, revenue, 63)
    b = gs.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage gap volatility (instability of profit-vs-revenue tracking)
def f32ol_f32_operating_leverage_gspreadvol_252d_base_v094_signal(opinc, revenue):
    gs = _f32_growth_spread(opinc, revenue, 63)
    b = gs.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside leverage: growth-spread only when revenue contracts (cost stickiness)
def f32ol_f32_operating_leverage_downlev_252d_base_v095_signal(opinc, revenue):
    gs = _f32_growth_spread(opinc, revenue, 252)
    contract = (_roc(revenue, 252) < 0).astype(float)
    b = gs * contract + gs.rolling(126, min_periods=42).mean() * (1 - contract)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- opex composition / scale economics ---

# opex/revenue convexity: 2nd diff of opex-ratio (accelerating scale economies)
def f32ol_f32_operating_leverage_opexconvex_252d_base_v096_signal(opex, revenue):
    r = opex / revenue.replace(0, np.nan)
    b = -(r - 2.0 * r.shift(126) + r.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied variable opex: incremental opex per incremental revenue, ranked
def f32ol_f32_operating_leverage_varopexrank_252d_base_v097_signal(opex, revenue):
    dox = opex - opex.shift(252)
    dr = revenue - revenue.shift(252)
    vc = dox / dr.replace(0, np.nan)
    b = -_rank(vc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied fixed opex level: opex minus variable*revenue, normalized by revenue
def f32ol_f32_operating_leverage_fixopex_252d_base_v098_signal(opex, revenue):
    dox = opex - opex.shift(252)
    dr = (revenue - revenue.shift(252)).replace(0, np.nan)
    vc = (dox / dr).clip(-2, 2)
    fixed = opex - vc * revenue
    b = (fixed / revenue.replace(0, np.nan))
    b = b - b.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex elasticity to revenue (cost flexibility; <1 = scale economies)
def f32ol_f32_operating_leverage_opexelast2_252d_base_v099_signal(opex, revenue):
    b = np.tanh(_dlog(opex, 252) / _dlog(revenue, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-elasticity stability over 2y (predictable cost behavior)
def f32ol_f32_operating_leverage_opexelaststab_504d_base_v100_signal(opex, revenue):
    e = np.tanh(_dlog(opex, 126) / _dlog(revenue, 126).replace(0, np.nan))
    b = -e.rolling(504, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- contribution margin & gp-vs-opinc structure ---

# contribution margin proxy (gp/revenue) trend (variable margin scaling)
def f32ol_f32_operating_leverage_cmtrend_252d_base_v101_signal(gp, revenue):
    cm = _f32_margin(gp, revenue)
    b = _slope(cm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage factor: contribution margin / operating margin
def f32ol_f32_operating_leverage_olfactor_base_v102_signal(gp, opinc):
    cm = gp
    om = opinc
    b = np.tanh((cm / om.replace(0, np.nan)) / 5.0)
    b = b.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage factor change over 1y (leverage regime shift)
def f32ol_f32_operating_leverage_olfactorchg_252d_base_v103_signal(gp, opinc):
    f = np.tanh((gp / opinc.replace(0, np.nan)) / 5.0)
    b = f.shift(252) - f
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost share trend (gp-opinc)/revenue slope (de-fixed-cost over time)
def f32ol_f32_operating_leverage_fixshare_252d_base_v104_signal(gp, opinc, revenue):
    fc = (gp - opinc) / revenue.replace(0, np.nan)
    b = -_slope(fc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost coverage by gross profit, z-scored (cushion above fixed costs)
def f32ol_f32_operating_leverage_fixcoverz_504d_base_v105_signal(gp, opinc):
    fc = (gp - opinc)
    cover = gp / fc.replace(0, np.nan)
    b = _z(np.tanh(cover / 5.0), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# contribution-margin-weighted growth: cm-level x revenue-growth (levered growth)
def f32ol_f32_operating_leverage_cmgrowth_252d_base_v106_signal(gp, revenue):
    cm = _f32_margin(gp, revenue)
    gr = _roc(revenue, 252)
    b = cm * gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- incremental & marginal profitability ---

# marginal opinc: Δopinc over Δgp (how much extra gp drops to opinc)
def f32ol_f32_operating_leverage_margopinc_252d_base_v107_signal(opinc, gp):
    do = opinc - opinc.shift(252)
    dg = (gp - gp.shift(252)).replace(0, np.nan)
    b = np.tanh(do / dg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marginal ebit: Δebit over Δopinc (below-operating-line conversion)
def f32ol_f32_operating_leverage_margebit_252d_base_v108_signal(ebit, opinc):
    de = ebit - ebit.shift(252)
    do = (opinc - opinc.shift(252)).replace(0, np.nan)
    b = np.tanh(de / do)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental contribution chain: Δopinc/Δrevenue x Δgp/Δrevenue interaction
def f32ol_f32_operating_leverage_incchain_252d_base_v109_signal(opinc, gp, revenue):
    a = np.tanh(_f32_incr_margin(opinc, revenue, 252))
    c = np.tanh(_f32_incr_margin(gp, revenue, 252))
    b = a * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin trend (slope of Δopinc/Δrevenue over time)
def f32ol_f32_operating_leverage_incmgntrend_252d_base_v110_signal(opinc, revenue):
    im = _f32_incr_margin(opinc, revenue, 126)
    b = _slope(np.tanh(im), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental ebit margin smoothed minus its long-run level (leverage surprise)
def f32ol_f32_operating_leverage_incebitsurp_252d_base_v111_signal(ebit, revenue):
    im = np.tanh(_f32_incr_margin(ebit, revenue, 126))
    b = im.ewm(span=42, min_periods=21).mean() - im.rolling(504, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- regime / state classification of leverage ---

# leverage regime: sign of growth-spread persistence (positive-leverage streak length)
def f32ol_f32_operating_leverage_levstreak_252d_base_v112_signal(opinc, revenue):
    gs = _f32_growth_spread(opinc, revenue, 63)
    sign = np.sign(gs)
    b = (sign * (sign == sign.shift(1)).astype(float)).rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-quality: growth-spread divided by its own volatility (info ratio of leverage)
def f32ol_f32_operating_leverage_levir_252d_base_v113_signal(opinc, revenue):
    gs = _f32_growth_spread(opinc, revenue, 63)
    m = gs.rolling(252, min_periods=126).mean()
    sd = gs.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage skew: skewness of quarterly growth-spread over 2y
def f32ol_f32_operating_leverage_levskew_504d_base_v114_signal(ebit, revenue):
    gs = _f32_growth_spread(ebit, revenue, 63)
    b = gs.rolling(504, min_periods=252).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-trend vs revenue-trend sign agreement (clean operating leverage flag)
def f32ol_f32_operating_leverage_cleanflag_252d_base_v115_signal(opinc, revenue):
    sm = np.sign(_slope(_f32_margin(opinc, revenue), 252))
    sr = np.sign(_slope(revenue, 252))
    b = (sm * sr).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-line interactions ---

# gp-margin x op-margin product change (compounding leverage stack)
def f32ol_f32_operating_leverage_mgnstack_252d_base_v116_signal(gp, opinc, revenue):
    stack = _f32_margin(gp, revenue) * _f32_margin(opinc, revenue)
    b = stack - stack.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-to-gp conversion trend (bottom-line absorption of gross profit)
def f32ol_f32_operating_leverage_ebit2gp_252d_base_v117_signal(ebit, gp):
    r = ebit / gp.replace(0, np.nan)
    b = _slope(np.tanh(r), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opinc-to-opex ratio (profit generated per cost dollar), trend
def f32ol_f32_operating_leverage_opinc2opex_252d_base_v118_signal(opinc, opex):
    r = opinc / opex.replace(0, np.nan)
    b = _slope(np.tanh(r), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-to-opex ratio z-scored (cost-efficiency extremity)
def f32ol_f32_operating_leverage_ebit2opexz_504d_base_v119_signal(ebit, opex):
    r = ebit / opex.replace(0, np.nan)
    b = _z(np.tanh(r), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-to-fixedcost ratio (scale over fixed base), log change
def f32ol_f32_operating_leverage_rev2fix_252d_base_v120_signal(gp, opinc, revenue):
    fc = (gp - opinc).abs() + 1.0
    r = revenue / fc
    b = np.log(r.replace(0, np.nan) / r.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-horizon and acceleration ---

# DOL short minus DOL long (leverage term structure)
def f32ol_f32_operating_leverage_doltermstruct_base_v121_signal(opinc, revenue):
    ds = np.tanh(_f32_dol(opinc, revenue, 126) / 5.0)
    dl = np.tanh(_f32_dol(opinc, revenue, 504) / 5.0)
    b = ds - dl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin short vs long (leverage acceleration)
def f32ol_f32_operating_leverage_incterm_base_v122_signal(ebit, revenue):
    s = np.tanh(_f32_incr_margin(ebit, revenue, 126))
    l = np.tanh(_f32_incr_margin(ebit, revenue, 504))
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absorption acceleration: 2nd difference of op-margin (leverage jerk-as-level)
def f32ol_f32_operating_leverage_absorbaccel_252d_base_v123_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    d1 = m - m.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-spread term structure: 1y spread minus 2y spread (recent leverage shift)
def f32ol_f32_operating_leverage_gspreadterm_base_v124_signal(opinc, revenue):
    s1 = _f32_growth_spread(opinc, revenue, 252)
    s2 = _f32_growth_spread(opinc, revenue, 504)
    b = s1 - s2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scale-economy term structure: opex elasticity 1y vs 2y
def f32ol_f32_operating_leverage_scaleterm_base_v125_signal(opex, revenue):
    e1 = np.tanh(_dlog(opex, 252) / _dlog(revenue, 252).replace(0, np.nan))
    e2 = np.tanh(_dlog(opex, 504) / _dlog(revenue, 504).replace(0, np.nan))
    b = e2 - e1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite & rank-blended leverage scores ---

# levered-growth score: revenue-growth x margin-expansion sign, ranked
def f32ol_f32_operating_leverage_levgrowscore_252d_base_v126_signal(opinc, revenue):
    gr = _roc(revenue, 252)
    dm = _f32_absorption(opinc, revenue, 252)
    raw = np.sign(gr) * dm
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage composite: blend of DOL, incremental margin, scale economy
def f32ol_f32_operating_leverage_olcomposite_252d_base_v127_signal(opinc, opex, revenue):
    a = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    c = np.tanh(_f32_incr_margin(opinc, revenue, 252))
    d = np.tanh((_dlog(revenue, 252) - _dlog(opex, 252)) * 5.0)
    b = (_rank(a, 504) + _rank(c, 504) + _rank(d, 504)) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-leverage: high incremental margin AND low volatility, interaction
def f32ol_f32_operating_leverage_qualitylev_252d_base_v128_signal(ebit, revenue):
    im = np.tanh(_f32_incr_margin(ebit, revenue, 252))
    vol = _f32_growth_spread(ebit, revenue, 63).rolling(252, min_periods=126).std()
    b = im / (1.0 + vol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage breadth: average sign of (opinc,ebit,gp) margin expansion
def f32ol_f32_operating_leverage_marginbreadth_252d_base_v129_signal(opinc, ebit, gp, revenue):
    a = np.tanh(_f32_absorption(opinc, revenue, 252) * 50.0)
    c = np.tanh(_f32_absorption(ebit, revenue, 252) * 50.0)
    d = np.tanh(_f32_absorption(gp, revenue, 252) * 50.0)
    b = (a + c + d) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scale-economy composite: revenue/opex efficiency change x contribution-margin trend
def f32ol_f32_operating_leverage_scalecomposite_252d_base_v130_signal(gp, opex, revenue):
    eff = (revenue / opex.replace(0, np.nan))
    eff_chg = np.tanh((eff / eff.shift(252).replace(0, np.nan) - 1.0) * 5.0)
    cm_trend = np.tanh(_slope(_f32_margin(gp, revenue), 252) * 1e3)
    b = (eff_chg + cm_trend) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional distinct leverage descriptors ---

# cost inflation pressure: opex-growth vs revenue-growth, conditioned on rev rising
def f32ol_f32_operating_leverage_costpressure_252d_base_v131_signal(opex, revenue):
    gr = _roc(revenue, 252)
    gc = _roc(opex, 252)
    pressure = np.tanh((gc - gr) * 3.0)
    rising = np.tanh(gr * 5.0).clip(lower=0)
    b = pressure * rising
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin Sharpe: mean margin over its volatility (stable profitability base)
def f32ol_f32_operating_leverage_mgnsharpe_504d_base_v132_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    b = m.rolling(504, min_periods=126).mean() / m.rolling(504, min_periods=126).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-margin minus ebit-margin gap vs revenue scale (fixed+nonop block per sales-growth)
def f32ol_f32_operating_leverage_totwedge_252d_base_v133_signal(gp, ebit, revenue):
    wedge = _f32_margin(gp, revenue) - _f32_margin(ebit, revenue)
    dwedge = wedge.shift(252) - wedge
    gr = _roc(revenue, 252)
    b = np.tanh(dwedge * 30.0) * np.sign(gr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration x margin level (accelerating-sales leverage payoff)
def f32ol_f32_operating_leverage_revaccelxmgn_252d_base_v134_signal(opinc, revenue):
    gr = _roc(revenue, 126)
    accel = gr - gr.shift(126)
    m = _f32_margin(opinc, revenue)
    b = accel * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental margin captured vs lost (positive vs negative contribution share)
def f32ol_f32_operating_leverage_incsharepos_252d_base_v135_signal(opinc, revenue):
    im = _f32_incr_margin(opinc, revenue, 63)
    pos = (im > 0).astype(float)
    b = pos.rolling(504, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage relative to gross leverage (fixed-cost dominance ratio)
def f32ol_f32_operating_leverage_oprelgross_252d_base_v136_signal(opinc, gp, revenue):
    do = np.tanh(_f32_dol(opinc, revenue, 252) / 5.0)
    dg = np.tanh(_f32_dol(gp, revenue, 252) / 5.0)
    b = do - dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-margin trend conditioned on opex/revenue falling (true scale leverage)
def f32ol_f32_operating_leverage_truescale_252d_base_v137_signal(ebit, opex, revenue):
    dm = _f32_absorption(ebit, revenue, 252)
    opex_r = opex / revenue.replace(0, np.nan)
    falling = (opex_r < opex_r.shift(252)).astype(float)
    b = dm * (2.0 * falling - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin level minus contribution-margin-implied ceiling (headroom)
def f32ol_f32_operating_leverage_mgnheadroom_252d_base_v138_signal(gp, opinc, revenue):
    om = _f32_margin(opinc, revenue)
    cm = _f32_margin(gp, revenue)
    b = (cm - om) / cm.replace(0, np.nan)
    b = b - b.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage payoff realized: opinc-growth in excess of revenue-growth, cumulative log
def f32ol_f32_operating_leverage_payoffcum_504d_base_v139_signal(opinc, revenue):
    excess = _dlog(opinc.abs() + 1.0, 63) - _dlog(revenue, 63)
    b = excess.rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit incremental margin minus opex marginal cost (net marginal profitability)
def f32ol_f32_operating_leverage_netmarginal_252d_base_v140_signal(ebit, opex, revenue):
    im = np.tanh(_f32_incr_margin(ebit, revenue, 252))
    mc = np.tanh((opex - opex.shift(252)) / (revenue - revenue.shift(252)).replace(0, np.nan))
    b = im - mc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# contribution margin scaled growth: cm-trend x revenue-growth, z-scored
def f32ol_f32_operating_leverage_cmscaledz_252d_base_v141_signal(gp, revenue):
    cm = _f32_margin(gp, revenue)
    raw = (cm - cm.shift(252)) * _roc(revenue, 252)
    b = _z(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-leverage durability: positive incremental-margin streak fraction (2y)
def f32ol_f32_operating_leverage_durable_504d_base_v142_signal(opinc, revenue):
    im = _f32_incr_margin(opinc, revenue, 63)
    pos = (im > 0).astype(float)
    streak = pos * (pos.shift(63) > 0).astype(float)
    b = streak.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-mix leverage: gp/opex ratio change (gross profit per operating cost)
def f32ol_f32_operating_leverage_gpperopex_252d_base_v143_signal(gp, opex):
    r = gp / opex.replace(0, np.nan)
    b = r / r.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage tilt: ebit-margin z minus revenue-growth z (profitability-vs-growth balance)
def f32ol_f32_operating_leverage_levtilt_252d_base_v144_signal(ebit, revenue):
    mz = _z(_f32_margin(ebit, revenue), 504)
    gz = _z(_roc(revenue, 63), 504)
    b = mz - gz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion velocity normalized by margin level (relative leverage rate)
def f32ol_f32_operating_leverage_relabsorb_252d_base_v145_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    dm = m - m.shift(252)
    b = dm / m.abs().clip(lower=0.01)
    b = np.tanh(b)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage stress: margin drawdown interacted with revenue contraction only
def f32ol_f32_operating_leverage_stress_252d_base_v146_signal(opinc, revenue):
    m = _f32_margin(opinc, revenue)
    mdd = (m - m.rolling(504, min_periods=126).max())
    rc = -_roc(revenue, 252)
    b = np.sign(mdd) * np.sqrt(mdd.abs()) * (1.0 + np.tanh(rc * 4.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scale-adjusted profit growth: opinc-growth deflated by opex-growth
def f32ol_f32_operating_leverage_scaleadjgrow_252d_base_v147_signal(opinc, opex):
    b = _dlog(opinc.abs() + 1.0, 252) - _dlog(opex, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating leverage breadth-weighted score: spread x consistency
def f32ol_f32_operating_leverage_spreadxcons_252d_base_v148_signal(ebit, revenue):
    gs = _f32_growth_spread(ebit, revenue, 252)
    cons = (_f32_growth_spread(ebit, revenue, 63) > 0).astype(float).rolling(252, min_periods=126).mean()
    b = gs * cons
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-cost intensity trend: (gp-opinc)/gp slope, sign-flipped (de-leveraging fixed base)
def f32ol_f32_operating_leverage_fixintens_252d_base_v149_signal(gp, opinc):
    fc = _f32_contrib(gp, opinc)
    b = -_slope(fc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# grand operating-leverage index: rank blend of elasticity, absorption, scale, contribution
def f32ol_f32_operating_leverage_grandindex_252d_base_v150_signal(opinc, gp, opex, revenue):
    el = _rank(np.tanh(_dlog(opinc.abs() + 1.0, 252) / _dlog(revenue, 252).replace(0, np.nan)), 504)
    ab = _rank(_f32_absorption(opinc, revenue, 252), 504)
    sc = _rank(_dlog(revenue, 252) - _dlog(opex, 252), 504)
    co = _rank(-_f32_contrib(gp, opinc), 504)
    b = (el + ab + sc + co) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32ol_f32_operating_leverage_elast_252d_base_v076_signal,
    f32ol_f32_operating_leverage_elastgp_252d_base_v077_signal,
    f32ol_f32_operating_leverage_elastgap_252d_base_v078_signal,
    f32ol_f32_operating_leverage_elastmom_252d_base_v079_signal,
    f32ol_f32_operating_leverage_elastdisp_252d_base_v080_signal,
    f32ol_f32_operating_leverage_salesperopex_base_v081_signal,
    f32ol_f32_operating_leverage_salesperopexslope_252d_base_v082_signal,
    f32ol_f32_operating_leverage_salesperopexz_504d_base_v083_signal,
    f32ol_f32_operating_leverage_salesperopexchg_252d_base_v084_signal,
    f32ol_f32_operating_leverage_mgnaccel_252d_base_v085_signal,
    f32ol_f32_operating_leverage_mgnbreakout_504d_base_v086_signal,
    f32ol_f32_operating_leverage_ebitmgnbreakout_504d_base_v087_signal,
    f32ol_f32_operating_leverage_mgndd_504d_base_v088_signal,
    f32ol_f32_operating_leverage_mgnrecov_504d_base_v089_signal,
    f32ol_f32_operating_leverage_dolratio_504d_base_v090_signal,
    f32ol_f32_operating_leverage_gspreadasym_504d_base_v091_signal,
    f32ol_f32_operating_leverage_gspreadcons_252d_base_v092_signal,
    f32ol_f32_operating_leverage_gspreadcum_252d_base_v093_signal,
    f32ol_f32_operating_leverage_gspreadvol_252d_base_v094_signal,
    f32ol_f32_operating_leverage_downlev_252d_base_v095_signal,
    f32ol_f32_operating_leverage_opexconvex_252d_base_v096_signal,
    f32ol_f32_operating_leverage_varopexrank_252d_base_v097_signal,
    f32ol_f32_operating_leverage_fixopex_252d_base_v098_signal,
    f32ol_f32_operating_leverage_opexelast2_252d_base_v099_signal,
    f32ol_f32_operating_leverage_opexelaststab_504d_base_v100_signal,
    f32ol_f32_operating_leverage_cmtrend_252d_base_v101_signal,
    f32ol_f32_operating_leverage_olfactor_base_v102_signal,
    f32ol_f32_operating_leverage_olfactorchg_252d_base_v103_signal,
    f32ol_f32_operating_leverage_fixshare_252d_base_v104_signal,
    f32ol_f32_operating_leverage_fixcoverz_504d_base_v105_signal,
    f32ol_f32_operating_leverage_cmgrowth_252d_base_v106_signal,
    f32ol_f32_operating_leverage_margopinc_252d_base_v107_signal,
    f32ol_f32_operating_leverage_margebit_252d_base_v108_signal,
    f32ol_f32_operating_leverage_incchain_252d_base_v109_signal,
    f32ol_f32_operating_leverage_incmgntrend_252d_base_v110_signal,
    f32ol_f32_operating_leverage_incebitsurp_252d_base_v111_signal,
    f32ol_f32_operating_leverage_levstreak_252d_base_v112_signal,
    f32ol_f32_operating_leverage_levir_252d_base_v113_signal,
    f32ol_f32_operating_leverage_levskew_504d_base_v114_signal,
    f32ol_f32_operating_leverage_cleanflag_252d_base_v115_signal,
    f32ol_f32_operating_leverage_mgnstack_252d_base_v116_signal,
    f32ol_f32_operating_leverage_ebit2gp_252d_base_v117_signal,
    f32ol_f32_operating_leverage_opinc2opex_252d_base_v118_signal,
    f32ol_f32_operating_leverage_ebit2opexz_504d_base_v119_signal,
    f32ol_f32_operating_leverage_rev2fix_252d_base_v120_signal,
    f32ol_f32_operating_leverage_doltermstruct_base_v121_signal,
    f32ol_f32_operating_leverage_incterm_base_v122_signal,
    f32ol_f32_operating_leverage_absorbaccel_252d_base_v123_signal,
    f32ol_f32_operating_leverage_gspreadterm_base_v124_signal,
    f32ol_f32_operating_leverage_scaleterm_base_v125_signal,
    f32ol_f32_operating_leverage_levgrowscore_252d_base_v126_signal,
    f32ol_f32_operating_leverage_olcomposite_252d_base_v127_signal,
    f32ol_f32_operating_leverage_qualitylev_252d_base_v128_signal,
    f32ol_f32_operating_leverage_marginbreadth_252d_base_v129_signal,
    f32ol_f32_operating_leverage_scalecomposite_252d_base_v130_signal,
    f32ol_f32_operating_leverage_costpressure_252d_base_v131_signal,
    f32ol_f32_operating_leverage_mgnsharpe_504d_base_v132_signal,
    f32ol_f32_operating_leverage_totwedge_252d_base_v133_signal,
    f32ol_f32_operating_leverage_revaccelxmgn_252d_base_v134_signal,
    f32ol_f32_operating_leverage_incsharepos_252d_base_v135_signal,
    f32ol_f32_operating_leverage_oprelgross_252d_base_v136_signal,
    f32ol_f32_operating_leverage_truescale_252d_base_v137_signal,
    f32ol_f32_operating_leverage_mgnheadroom_252d_base_v138_signal,
    f32ol_f32_operating_leverage_payoffcum_504d_base_v139_signal,
    f32ol_f32_operating_leverage_netmarginal_252d_base_v140_signal,
    f32ol_f32_operating_leverage_cmscaledz_252d_base_v141_signal,
    f32ol_f32_operating_leverage_durable_504d_base_v142_signal,
    f32ol_f32_operating_leverage_gpperopex_252d_base_v143_signal,
    f32ol_f32_operating_leverage_levtilt_252d_base_v144_signal,
    f32ol_f32_operating_leverage_relabsorb_252d_base_v145_signal,
    f32ol_f32_operating_leverage_stress_252d_base_v146_signal,
    f32ol_f32_operating_leverage_scaleadjgrow_252d_base_v147_signal,
    f32ol_f32_operating_leverage_spreadxcons_252d_base_v148_signal,
    f32ol_f32_operating_leverage_fixintens_252d_base_v149_signal,
    f32ol_f32_operating_leverage_grandindex_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_OPERATING_LEVERAGE_REGISTRY_076_150 = REGISTRY


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

    print("OK f32_operating_leverage_base_076_150_claude: %d features pass" % n_features)
