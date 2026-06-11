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


# ===== folder domain primitives (cash-flow cyclicality) =====
def _f32_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f32_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f32_fcf_after_capex(ncfo, capex):
    return ncfo - capex


def _f32_capex_cover(ncfo, capex):
    return ncfo / capex.replace(0, np.nan)


def _f32_fcf_conversion(fcf, ncfo):
    return fcf / ncfo.replace(0, np.nan)


def _f32_sign_sqrt(s):
    return np.sign(s) * (s.abs() ** 0.5)


# ============================================================
# --- MULTI-YEAR CYCLE AMPLITUDE / POSITION ---
# FCF-margin amplitude over 504d normalized by its mean level (relative cyclical span)
def f32cf_f32_cash_flow_cyclicality_relamp_504d_base_v076_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    span = _rmax(m, 504) - _rmin(m, 504)
    lvl = _mean(m.abs(), 504)
    b = span / lvl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF cyclical position within 504d range (long-cycle phase of cash generation)
def f32cf_f32_cash_flow_cyclicality_ocfcyclepos_504d_base_v077_signal(ncfo):
    s = _f32_sign_sqrt(ncfo)
    hi = _rmax(s, 504)
    lo = _rmin(s, 504)
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin distance above its 1260d trough (full-cycle recovery height)
def f32cf_f32_cash_flow_cyclicality_fcftrough_1260d_base_v078_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m - _rmin(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin position within 1260d band, smoothed (multi-year cash phase)
def f32cf_f32_cash_flow_cyclicality_ocfphase_1260d_base_v079_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 1260)
    lo = _rmin(m, 1260)
    pos = (m - lo) / (hi - lo).replace(0, np.nan)
    b = pos.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CASH-MARGIN VOLATILITY VARIANTS ---
# FCF-margin volatility over half a year (shorter-cycle cash instability)
def f32cf_f32_cash_flow_cyclicality_fcfvol_126d_base_v080_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin vol-of-vol: dispersion of rolling 63d vol over a year (instability of instability)
def f32cf_f32_cash_flow_cyclicality_ocfvolofvol_252d_base_v081_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    v = m.rolling(63, min_periods=21).std()
    b = v.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage volatility over a year (erratic self-funding ability)
def f32cf_f32_cash_flow_cyclicality_covervol_252d_base_v082_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = c.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation of FCF margin (volatility only of below-mean cash months)
def f32cf_f32_cash_flow_cyclicality_fcfdownsemi_252d_base_v083_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    mu = _mean(m, 252)
    downside = (m - mu).clip(upper=0.0)
    b = (downside ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INFLECTION / SIGN-CHANGE FORMS ---
# FCF-margin distance from zero scaled by recent vol (signed standardized break-even)
def f32cf_f32_cash_flow_cyclicality_fcfzero_63d_base_v084_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    vol = m.rolling(126, min_periods=63).std()
    b = (m / vol.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of FCF positive->negative crossings over a year (downward inflection tally)
def f32cf_f32_cash_flow_cyclicality_fcfdowninflect_252d_base_v085_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    neg = (f < 0).astype(float)
    cross_dn = ((neg == 1) & (neg.shift(1) == 0)).astype(float)
    b = cross_dn.rolling(252, min_periods=126).sum() + 0.25 * neg.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest FCF-negative run in last year (deepest cash-loss spell), log-scaled
def f32cf_f32_cash_flow_cyclicality_fcfnegrun_252d_base_v086_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    neg = (f < 0).astype(float)
    grp = (neg != neg.shift(1)).cumsum()
    run = neg.groupby(grp).cumsum() * neg
    b = np.log1p(run.rolling(252, min_periods=126).max())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling skewness of FCF margin over a year (asymmetric cash-cycle shape)
def f32cf_f32_cash_flow_cyclicality_fcfskew_252d_base_v087_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- OCF TREND / MOMENTUM VARIANTS ---
# OCF momentum: 63d change minus 252d change (acceleration of cash generation, base)
def f32cf_f32_cash_flow_cyclicality_ocfmomdiff_base_v088_signal(ncfo):
    s = _f32_sign_sqrt(ncfo)
    short = s - s.shift(63)
    long = (s - s.shift(252)) / 4.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF half-year vs full-year mean tilt (medium-term cash-generation drift)
def f32cf_f32_cash_flow_cyclicality_ocftilt_base_v089_signal(ncfo):
    s = _f32_sign_sqrt(ncfo)
    half = s.rolling(126, min_periods=63).mean()
    full = s.rolling(252, min_periods=126).mean()
    b = (half - full) / s.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin recovery off its 252d trough scaled by time since trough (matured rebound)
def f32cf_f32_cash_flow_cyclicality_ocfrebound_252d_base_v090_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    lo = _rmin(m, 252)
    rec = m - lo

    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dst = m.rolling(252, min_periods=126).apply(_dsl, raw=True)
    b = rec * dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CAPEX / INVESTMENT CYCLE FORMS ---
# capex/OCF ratio (investment intensity vs cash generation), smoothed
def f32cf_f32_cash_flow_cyclicality_capexvsocf_63d_base_v091_signal(capex, ncfo):
    r = (capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth (log-change over a quarter) — investment-cycle momentum
def f32cf_f32_cash_flow_cyclicality_capexgrow_63d_base_v092_signal(capex):
    lc = np.log(capex.replace(0, np.nan))
    b = lc - lc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity cyclical position within 252d range (investment-phase indicator)
def f32cf_f32_cash_flow_cyclicality_capexintenspos_252d_base_v093_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity volatility over a year (lumpy vs steady investment)
def f32cf_f32_cash_flow_cyclicality_capexintvol_252d_base_v094_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex drawdown from its 252d peak (investment pullback depth)
def f32cf_f32_cash_flow_cyclicality_capexdd_252d_base_v095_signal(capex):
    peak = _rmax(capex, 252)
    b = capex / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF CONVERSION / QUALITY VARIANTS ---
# FCF conversion percentile-rank vs 504d (where conversion sits in its cycle)
def f32cf_f32_cash_flow_cyclicality_convrank_504d_base_v096_signal(fcf, ncfo):
    c = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conversion trend over half a year (rising/falling cash-retention through capex)
def f32cf_f32_cash_flow_cyclicality_convtrend_126d_base_v097_signal(fcf, ncfo):
    c = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year fcf and ncfo agreed in sign (cash-flow coherence)
def f32cf_f32_cash_flow_cyclicality_signcoher_252d_base_v098_signal(fcf, ncfo):
    agree = (np.sign(fcf) == np.sign(ncfo)).astype(float)
    b = agree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISPERSION / RANGE-OF-RATIOS ---
# multi-window dispersion of OCF margins (short/med/long disagreement)
def f32cf_f32_cash_flow_cyclicality_ocfdisp_multi_base_v099_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    a = m.rolling(63, min_periods=21).mean()
    b2 = m.rolling(126, min_periods=63).mean()
    c = m.rolling(252, min_periods=126).mean()
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range of capex-coverage across windows (self-funding disagreement)
def f32cf_f32_cash_flow_cyclicality_coverdisp_multi_base_v100_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    a = c.rolling(63, min_periods=21).mean()
    b2 = c.rolling(126, min_periods=63).mean()
    d = c.rolling(252, min_periods=126).mean()
    stk = pd.concat([a, b2, d], axis=1)
    b = stk.max(axis=1) - stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INTERACTIONS / COMPOSITES ---
# cash-stress divergence: capex intensity rising while OCF margin falling (jaws)
def f32cf_f32_cash_flow_cyclicality_cashstress_252d_base_v101_signal(ncfo, capex, revenue):
    intens = (capex / revenue.replace(0, np.nan))
    capex_chg = intens - intens.shift(126)
    om = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    om_chg = om - om.shift(126)
    b = capex_chg - om_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cyclical-quality: FCF-margin level x its consistency (steady & strong cash)
def f32cf_f32_cash_flow_cyclicality_cycqual_252d_base_v102_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    lvl = m.rolling(63, min_periods=21).mean()
    steady = -m.rolling(252, min_periods=126).std()
    b = np.tanh(lvl) + 0.5 * steady
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-revenue sync x amplitude (procyclical cash with big swings = high-beta cash)
def f32cf_f32_cash_flow_cyclicality_procyc_252d_base_v103_signal(ncfo, revenue):
    docf = np.sign(ncfo - ncfo.shift(63))
    drev = np.sign(revenue - revenue.shift(63))
    sync = (docf * drev).rolling(126, min_periods=63).mean()
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    amp = _rmax(m, 252) - _rmin(m, 252)
    b = sync * amp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TERM STRUCTURE / RATIO VARIANTS ---
# short/long capex-intensity ratio (investment ramp vs structural)
def f32cf_f32_cash_flow_cyclicality_capexterm_base_v104_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short/long FCF-margin vol ratio (cash-vol term structure, half vs full year)
def f32cf_f32_cash_flow_cyclicality_fcfvolterm2_base_v105_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    short = m.rolling(126, min_periods=63).std()
    long = m.rolling(252, min_periods=126).std()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share short/long mean tilt (recent per-share cash vs structural)
def f32cf_f32_cash_flow_cyclicality_fcfpsterm_base_v106_signal(fcfps):
    s = _f32_sign_sqrt(fcfps)
    short = s.rolling(63, min_periods=21).mean()
    long = s.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCFPS-CENTRIC FORMS ---
# FCF-per-share drawdown from 252d peak (per-share cash strength loss)
def f32cf_f32_cash_flow_cyclicality_fcfpsdd_252d_base_v107_signal(fcfps):
    s = _f32_sign_sqrt(fcfps)
    peak = _rmax(s, 252)
    b = s - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share swing amplitude over a year (per-share cyclical span)
def f32cf_f32_cash_flow_cyclicality_fcfpsswing_252d_base_v108_signal(fcfps):
    b = _rmax(fcfps, 252) - _rmin(fcfps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share momentum over a quarter (per-share cash acceleration)
def f32cf_f32_cash_flow_cyclicality_fcfpsmom_63d_base_v109_signal(fcfps):
    s = _f32_sign_sqrt(fcfps)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share coefficient of variation over a year (per-share instability)
def f32cf_f32_cash_flow_cyclicality_fcfpscv_252d_base_v110_signal(fcfps):
    sd = _std(fcfps, 252)
    m = _mean(fcfps.abs(), 252)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME / COUNT FORMS ---
# fraction of last year capex-coverage above 1 (operations self-funding development)
def f32cf_f32_cash_flow_cyclicality_selffundtime_252d_base_v111_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex)
    self_fund = (c >= 1.0).astype(float)
    frac = self_fund.rolling(252, min_periods=126).mean()
    margin = (c - 1.0).clip(lower=-2.0, upper=2.0).rolling(63, min_periods=21).mean()
    b = frac + 0.2 * margin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year OCF margin in top third of its range (cash-peak prevalence)
def f32cf_f32_cash_flow_cyclicality_ocfpeaktime_252d_base_v112_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    pos = (m - lo) / (hi - lo).replace(0, np.nan)
    top = (pos >= 0.6667).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-burst prevalence: fraction of year capex sat above its 252d mean + 1 std (bursts)
def f32cf_f32_cash_flow_cyclicality_capexspike_252d_base_v113_signal(capex):
    mu = _mean(capex, 252)
    sd = _std(capex, 252)
    thr = mu + sd
    spike = (capex > thr).astype(float)
    frac = spike.rolling(252, min_periods=126).mean()
    excess = ((capex - thr) / sd.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 0.3 * excess
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN x MAGNITUDE / BOUNDED FORMS ---
# tanh-squashed OCF-margin momentum (bounded cash-margin change over a quarter)
def f32cf_f32_cash_flow_cyclicality_ocftanh_63d_base_v114_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    chg = m - m.shift(63)
    b = np.tanh(3.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-root of FCF-after-capex scaled by revenue (compressed free-cash yield)
def f32cf_f32_cash_flow_cyclicality_fcfyieldsr_63d_base_v115_signal(ncfo, capex, revenue):
    y = (_f32_fcf_after_capex(ncfo, capex) / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    b = _f32_sign_sqrt(y).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed capex-coverage momentum (bounded change in self-funding over a quarter)
def f32cf_f32_cash_flow_cyclicality_covertanh_63d_base_v116_signal(ncfo, capex):
    c = (_f32_capex_cover(ncfo, capex)).clip(lower=-10.0, upper=10.0)
    chg = c - c.shift(63)
    b = np.tanh(0.5 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CURVATURE-LIKE (base second differences) ---
# capex-intensity curvature: minus average of lead/lag (investment concavity, base)
def f32cf_f32_cash_flow_cyclicality_capexcurv_63d_base_v117_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    b = r - 0.5 * (r.shift(63) + r.shift(-63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share second difference (per-share cash acceleration, base)
def f32cf_f32_cash_flow_cyclicality_fcfpsaccel_63d_base_v118_signal(fcfps):
    s = _f32_sign_sqrt(fcfps)
    d1 = s - s.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin acceleration over a month (base second difference, faster window)
def f32cf_f32_cash_flow_cyclicality_ocfaccel_21d_base_v119_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    d1 = m - m.shift(21)
    b = d1 - d1.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- YEAR-OVER-YEAR / LONG-HORIZON ---
# FCF-margin year-over-year change (cyclical cash-margin shift)
def f32cf_f32_cash_flow_cyclicality_fcfmarginyoy_252d_base_v120_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage year-over-year change (self-funding shift across the cycle)
def f32cf_f32_cash_flow_cyclicality_coveryoy_252d_base_v121_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin two-year change (long-cycle cash-profitability shift)
def f32cf_f32_cash_flow_cyclicality_ocfmargin2yr_504d_base_v122_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = m - m.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RANK / Z VARIANTS (distinct underlying) ---
# capex/OCF ratio z-scored vs 252d (investment-vs-cash regime)
def f32cf_f32_cash_flow_cyclicality_capexocfz_252d_base_v123_signal(capex, ncfo):
    r = (capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-after-capex percentile-rank vs 252d (free-cash percentile, direct)
def f32cf_f32_cash_flow_cyclicality_fcfacrank_252d_base_v124_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    b = _rank(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin z-scored vs 126d history (shorter-cycle de-trended cash margin)
def f32cf_f32_cash_flow_cyclicality_fcfmarginz_126d_base_v125_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _z(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE CYCLE SCORES ---
# cash-cycle bottom score: deep-below-median FCF margin + rising slope (turn from trough)
def f32cf_f32_cash_flow_cyclicality_bottomscore_252d_base_v126_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    med = m.rolling(252, min_periods=126).median()
    depth = (med - m).clip(lower=0)
    rising = (m - m.shift(63)).clip(lower=0)
    b = np.tanh(depth) * np.tanh(rising)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-cycle top score: high-above-median OCF margin + falling slope (rollover from peak)
def f32cf_f32_cash_flow_cyclicality_topscore_252d_base_v127_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    med = m.rolling(252, min_periods=126).median()
    height = (m - med).clip(lower=0)
    falling = (m.shift(63) - m).clip(lower=0)
    b = np.tanh(height) * np.tanh(falling)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash durability: positivity time x conversion quality (durable producer cash)
def f32cf_f32_cash_flow_cyclicality_durability_252d_base_v128_signal(fcf, ncfo):
    postime = (fcf > 0).astype(float).rolling(252, min_periods=126).mean()
    conv = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0).rolling(63, min_periods=21).mean()
    b = postime * np.tanh(conv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ADDITIONAL DISTINCT RATIOS ---
# current self-funded streak: consecutive days OCF covers capex, log-scaled
def f32cf_f32_cash_flow_cyclicality_selffundstreak_base_v129_signal(ncfo, capex):
    covered = (ncfo >= capex).astype(float)
    grp = (covered != covered.shift(1)).cumsum()
    streak = covered.groupby(grp).cumsum() * covered
    b = np.log1p(streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-to-FCF lead/lag sync over 126d (does cash follow revenue swings)
def f32cf_f32_cash_flow_cyclicality_revfcflag_126d_base_v130_signal(fcf, revenue):
    drev = np.sign(revenue.shift(63) - revenue.shift(126))
    dfcf = np.sign(fcf - fcf.shift(63))
    b = (drev * dfcf).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin percentile-rank vs its own 1260d history (multi-year cash-margin anomaly)
def f32cf_f32_cash_flow_cyclicality_fcfanomrank_1260d_base_v131_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _rank(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin minus FCF margin spread, ranked vs 252d (capex-drag percentile)
def f32cf_f32_cash_flow_cyclicality_dragrank_252d_base_v132_signal(ncfo, fcf, revenue):
    drag = (_f32_ocf_margin(ncfo, revenue) - _f32_fcf_margin(fcf, revenue)).clip(lower=-3.0, upper=3.0)
    b = _rank(drag, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MORE VOLATILITY / SWING DISTINCT ---
# OCF swing amplitude over 252d normalized by revenue (cash-flow cyclical span)
def f32cf_f32_cash_flow_cyclicality_ocfswingrev_252d_base_v133_signal(ncfo, revenue):
    swing = _rmax(ncfo, 252) - _rmin(ncfo, 252)
    b = (swing / _mean(revenue, 252).replace(0, np.nan)).clip(upper=5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-after-capex coefficient of variation over half a year (shorter-cycle instability)
def f32cf_f32_cash_flow_cyclicality_fcfcv_126d_base_v134_signal(ncfo, capex):
    f = _f32_fcf_after_capex(ncfo, capex)
    sd = _std(f, 126)
    m = _mean(f.abs(), 126)
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semideviation of OCF margin (volatility of above-mean cash months)
def f32cf_f32_cash_flow_cyclicality_ocfupsemi_252d_base_v135_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    mu = _mean(m, 252)
    up = (m - mu).clip(lower=0.0)
    b = (up ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DISTINCT INFLECTION / TREND COMBOS ---
# FCF-margin slope sign persistence (fraction of last half-year slope was positive)
def f32cf_f32_cash_flow_cyclicality_slopepersist_126d_base_v136_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    up = (m > m.shift(21)).astype(float)
    b = up.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of OCF margin from its own EMA trend (cash-margin displacement)
def f32cf_f32_cash_flow_cyclicality_ocfdisp_ema_63d_base_v137_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = m - m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage minimum over half a year (worst recent self-funding point)
def f32cf_f32_cash_flow_cyclicality_covermin_126d_base_v138_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = _rmin(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FINAL DISTINCT FORMS ---
# FCF margin EMA fast minus slow (cash-margin MACD-style cycle oscillator)
def f32cf_f32_cash_flow_cyclicality_fcfosc_base_v139_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    fast = m.ewm(span=42, min_periods=21).mean()
    slow = m.ewm(span=126, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin EMA fast minus slow (OCF cycle oscillator)
def f32cf_f32_cash_flow_cyclicality_ocfosc_base_v140_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    fast = m.ewm(span=42, min_periods=21).mean()
    slow = m.ewm(span=126, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash conversion volatility over a year (instability of capex retention)
def f32cf_f32_cash_flow_cyclicality_convvol_252d_base_v141_signal(fcf, ncfo):
    c = _f32_fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = c.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share cyclical position within 504d range (long per-share phase)
def f32cf_f32_cash_flow_cyclicality_fcfpspos_504d_base_v142_signal(fcfps):
    hi = _rmax(fcfps, 504)
    lo = _rmin(fcfps, 504)
    b = (fcfps - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity smoothed over half a year (structural investment level)
def f32cf_f32_cash_flow_cyclicality_capexintens_126d_base_v143_signal(capex, revenue):
    r = capex / revenue.replace(0, np.nan)
    b = r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF-margin quarterly-momentum rank vs 504d (where cash-margin change sits multi-year)
def f32cf_f32_cash_flow_cyclicality_ocfmommrank_504d_base_v144_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    mom = m - m.shift(63)
    b = _rank(mom, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin worst quarter vs best quarter ratio over a year (asymmetry of cash cycle)
def f32cf_f32_cash_flow_cyclicality_fcfasym_252d_base_v145_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    mid = _mean(m, 252)
    b = (hi - mid) - (mid - lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year FCF margin within a tight band of zero (near-break-even chop)
def f32cf_f32_cash_flow_cyclicality_chopzero_252d_base_v146_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    band = m.rolling(252, min_periods=126).std() * 0.5
    near = (m.abs() <= band).astype(float)
    b = near.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding instability: half-year vs full-year capex-coverage vol ratio (term structure)
def f32cf_f32_cash_flow_cyclicality_coververatio_base_v147_signal(ncfo, capex):
    c = (_f32_capex_cover(ncfo, capex)).clip(lower=-10.0, upper=10.0)
    short = c.rolling(126, min_periods=63).std()
    long = c.rolling(252, min_periods=126).std()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex-coverage cyclical position within 252d range (self-funding phase)
def f32cf_f32_cash_flow_cyclicality_coverpos_252d_base_v148_signal(ncfo, capex):
    c = _f32_capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    hi = _rmax(c, 252)
    lo = _rmin(c, 252)
    b = (c - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash yield (FCF/revenue) EMA-trend over a quarter (cash-yield momentum)
def f32cf_f32_cash_flow_cyclicality_fcfyieldmom_63d_base_v149_signal(fcf, revenue):
    y = (fcf / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    ema = y.ewm(span=42, min_periods=21).mean()
    b = ema - ema.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# whole-cycle cash quality: free-cash momentum relative to its own jaggedness
# (smooth improvement scores high; choppy or deteriorating cash scores low)
def f32cf_f32_cash_flow_cyclicality_cyclecomposite_252d_base_v150_signal(ncfo, capex, revenue):
    f = _f32_fcf_after_capex(ncfo, capex)
    y = (f / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    mom = y.rolling(63, min_periods=21).mean() - y.rolling(252, min_periods=126).mean()
    jag = (y - y.shift(21)).abs().rolling(252, min_periods=126).mean()
    b = mom / (jag + jag.rolling(252, min_periods=126).mean()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32cf_f32_cash_flow_cyclicality_relamp_504d_base_v076_signal,
    f32cf_f32_cash_flow_cyclicality_ocfcyclepos_504d_base_v077_signal,
    f32cf_f32_cash_flow_cyclicality_fcftrough_1260d_base_v078_signal,
    f32cf_f32_cash_flow_cyclicality_ocfphase_1260d_base_v079_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvol_126d_base_v080_signal,
    f32cf_f32_cash_flow_cyclicality_ocfvolofvol_252d_base_v081_signal,
    f32cf_f32_cash_flow_cyclicality_covervol_252d_base_v082_signal,
    f32cf_f32_cash_flow_cyclicality_fcfdownsemi_252d_base_v083_signal,
    f32cf_f32_cash_flow_cyclicality_fcfzero_63d_base_v084_signal,
    f32cf_f32_cash_flow_cyclicality_fcfdowninflect_252d_base_v085_signal,
    f32cf_f32_cash_flow_cyclicality_fcfnegrun_252d_base_v086_signal,
    f32cf_f32_cash_flow_cyclicality_fcfskew_252d_base_v087_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmomdiff_base_v088_signal,
    f32cf_f32_cash_flow_cyclicality_ocftilt_base_v089_signal,
    f32cf_f32_cash_flow_cyclicality_ocfrebound_252d_base_v090_signal,
    f32cf_f32_cash_flow_cyclicality_capexvsocf_63d_base_v091_signal,
    f32cf_f32_cash_flow_cyclicality_capexgrow_63d_base_v092_signal,
    f32cf_f32_cash_flow_cyclicality_capexintenspos_252d_base_v093_signal,
    f32cf_f32_cash_flow_cyclicality_capexintvol_252d_base_v094_signal,
    f32cf_f32_cash_flow_cyclicality_capexdd_252d_base_v095_signal,
    f32cf_f32_cash_flow_cyclicality_convrank_504d_base_v096_signal,
    f32cf_f32_cash_flow_cyclicality_convtrend_126d_base_v097_signal,
    f32cf_f32_cash_flow_cyclicality_signcoher_252d_base_v098_signal,
    f32cf_f32_cash_flow_cyclicality_ocfdisp_multi_base_v099_signal,
    f32cf_f32_cash_flow_cyclicality_coverdisp_multi_base_v100_signal,
    f32cf_f32_cash_flow_cyclicality_cashstress_252d_base_v101_signal,
    f32cf_f32_cash_flow_cyclicality_cycqual_252d_base_v102_signal,
    f32cf_f32_cash_flow_cyclicality_procyc_252d_base_v103_signal,
    f32cf_f32_cash_flow_cyclicality_capexterm_base_v104_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvolterm2_base_v105_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsterm_base_v106_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsdd_252d_base_v107_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsswing_252d_base_v108_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsmom_63d_base_v109_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpscv_252d_base_v110_signal,
    f32cf_f32_cash_flow_cyclicality_selffundtime_252d_base_v111_signal,
    f32cf_f32_cash_flow_cyclicality_ocfpeaktime_252d_base_v112_signal,
    f32cf_f32_cash_flow_cyclicality_capexspike_252d_base_v113_signal,
    f32cf_f32_cash_flow_cyclicality_ocftanh_63d_base_v114_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyieldsr_63d_base_v115_signal,
    f32cf_f32_cash_flow_cyclicality_covertanh_63d_base_v116_signal,
    f32cf_f32_cash_flow_cyclicality_capexcurv_63d_base_v117_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsaccel_63d_base_v118_signal,
    f32cf_f32_cash_flow_cyclicality_ocfaccel_21d_base_v119_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginyoy_252d_base_v120_signal,
    f32cf_f32_cash_flow_cyclicality_coveryoy_252d_base_v121_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargin2yr_504d_base_v122_signal,
    f32cf_f32_cash_flow_cyclicality_capexocfz_252d_base_v123_signal,
    f32cf_f32_cash_flow_cyclicality_fcfacrank_252d_base_v124_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginz_126d_base_v125_signal,
    f32cf_f32_cash_flow_cyclicality_bottomscore_252d_base_v126_signal,
    f32cf_f32_cash_flow_cyclicality_topscore_252d_base_v127_signal,
    f32cf_f32_cash_flow_cyclicality_durability_252d_base_v128_signal,
    f32cf_f32_cash_flow_cyclicality_selffundstreak_base_v129_signal,
    f32cf_f32_cash_flow_cyclicality_revfcflag_126d_base_v130_signal,
    f32cf_f32_cash_flow_cyclicality_fcfanomrank_1260d_base_v131_signal,
    f32cf_f32_cash_flow_cyclicality_dragrank_252d_base_v132_signal,
    f32cf_f32_cash_flow_cyclicality_ocfswingrev_252d_base_v133_signal,
    f32cf_f32_cash_flow_cyclicality_fcfcv_126d_base_v134_signal,
    f32cf_f32_cash_flow_cyclicality_ocfupsemi_252d_base_v135_signal,
    f32cf_f32_cash_flow_cyclicality_slopepersist_126d_base_v136_signal,
    f32cf_f32_cash_flow_cyclicality_ocfdisp_ema_63d_base_v137_signal,
    f32cf_f32_cash_flow_cyclicality_covermin_126d_base_v138_signal,
    f32cf_f32_cash_flow_cyclicality_fcfosc_base_v139_signal,
    f32cf_f32_cash_flow_cyclicality_ocfosc_base_v140_signal,
    f32cf_f32_cash_flow_cyclicality_convvol_252d_base_v141_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpspos_504d_base_v142_signal,
    f32cf_f32_cash_flow_cyclicality_capexintens_126d_base_v143_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmommrank_504d_base_v144_signal,
    f32cf_f32_cash_flow_cyclicality_fcfasym_252d_base_v145_signal,
    f32cf_f32_cash_flow_cyclicality_chopzero_252d_base_v146_signal,
    f32cf_f32_cash_flow_cyclicality_coververatio_base_v147_signal,
    f32cf_f32_cash_flow_cyclicality_coverpos_252d_base_v148_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyieldmom_63d_base_v149_signal,
    f32cf_f32_cash_flow_cyclicality_cyclecomposite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_CASH_FLOW_CYCLICALITY_REGISTRY_076_150 = REGISTRY


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

    fcf = _fund(3201, base=1.0e8, drift=-0.01, vol=0.24, allow_neg=True).rename("fcf")
    ncfo = _fund(3202, base=1.2e8, drift=0.0, vol=0.20, allow_neg=True).rename("ncfo")
    fcfps = _fund(3203, base=4.0, drift=-0.005, vol=0.26, allow_neg=True).rename("fcfps")
    revenue = _fund(3204, base=3.0e8, drift=0.015, vol=0.07).rename("revenue")
    capex = _fund(3205, base=7.0e7, drift=0.01, vol=0.16).rename("capex")

    cols = {"fcf": fcf, "ncfo": ncfo, "fcfps": fcfps,
            "revenue": revenue, "capex": capex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("fcf", "ncfo", "fcfps", "revenue", "capex")
                   for c in meta["inputs"]), name
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

    print("OK f32_cash_flow_cyclicality_base_076_150_claude: %d features pass" % n_features)
