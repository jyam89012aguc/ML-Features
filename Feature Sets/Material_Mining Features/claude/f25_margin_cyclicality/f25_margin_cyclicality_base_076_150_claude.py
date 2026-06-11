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


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (margin cyclicality) =====
# Real-data note: gross/op/gp-margin are ~0.99 collinear; net/ebitda-margin are ~0.99
# collinear. File 2 uses windows/facets DISTINCT from file 1 so the pooled real-data
# within-family check stays clean: longer horizons, persistence/autocorr, entropy,
# regime durations, spread dynamics, asymmetry ratios, revenue-scaled margin.
def _f25_amplitude(s, w):
    return _rmax(s, w) - _rmin(s, w)


def _f25_range_pos(s, w):
    hi = _rmax(s, w)
    lo = _rmin(s, w)
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f25_op_margin(opinc, revenue):
    return opinc / revenue.replace(0, np.nan)


def _f25_gp_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f25_autocorr(s, w, lag):
    return s.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda a: pd.Series(a).autocorr(lag) if np.std(a) > 0 else np.nan, raw=True)


# ============================================================
# ==== BLOCK 1: LONG-HORIZON LEVEL / CHEAPNESS (distinct windows vs file 1) ====

# gross-margin level z-scored vs a long 504d cycle (mid-cycle normalized gross margin)
def f25mc_f25_margin_cyclicality_gmlevelz_504d_base_v076_signal(grossmargin):
    b = _z(grossmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin level z-scored vs a 252d cycle (de-trended bottom-line level)
def f25mc_f25_margin_cyclicality_nmlevelz_252d_base_v077_signal(netmargin):
    b = _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level smoothed over a long 252d window (slow structural margin)
def f25mc_f25_margin_cyclicality_gmlevel_252d_base_v078_signal(grossmargin):
    b = grossmargin.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin percentile rank within a long 504d cycle (long cheap/rich bottom line)
def f25mc_f25_margin_cyclicality_nmrank_504d_base_v079_signal(netmargin):
    b = _rank(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin level z-scored vs its own 126d history (de-trended cash-margin level)
def f25mc_f25_margin_cyclicality_emlevel_126d_base_v080_signal(ebitdamargin):
    b = _z(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin deviation from its 252d baseline scaled by 126d vol (tighter-window z)
def f25mc_f25_margin_cyclicality_gmmidz_252d_base_v081_signal(grossmargin):
    base = grossmargin.rolling(252, min_periods=84).mean()
    sd = _std(grossmargin, 126)
    b = (grossmargin - base) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin compression fraction: distance below its 252d peak as a fraction of that peak
def f25mc_f25_margin_cyclicality_omlevel_63d_base_v082_signal(opinc, revenue):
    om = _f25_op_margin(opinc, revenue)
    pk = _rmax(om, 252)
    b = (pk - om) / pk.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin level as a fraction of its own 252d peak (distance from best recent cash margin)
def f25mc_f25_margin_cyclicality_nmvspeak_504d_base_v083_signal(ebitdamargin):
    pk = _rmax(ebitdamargin, 252)
    b = ebitdamargin / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin floor proximity ratio: how far current sits above the 252d trough as a multiple
def f25mc_f25_margin_cyclicality_gmfloor_504d_base_v084_signal(grossmargin):
    lo = _rmin(grossmargin, 252)
    b = grossmargin / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin vol-fill ratio: realized 252d std relative to its 252d peak-to-trough range
def f25mc_f25_margin_cyclicality_emperscale_base_v085_signal(ebitdamargin):
    sd = _std(ebitdamargin, 252)
    amp = _f25_amplitude(ebitdamargin, 252)
    b = sd / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 2: LONG-HORIZON VOLATILITY / STABILITY ====

# gross-margin vol term structure: short 126d vol vs long 504d vol (vol-curve slope)
def f25mc_f25_margin_cyclicality_gmvol_504d_base_v086_signal(grossmargin):
    vs = _std(grossmargin, 126)
    vl = _std(grossmargin, 504)
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin volatility over a long 504d cycle (structural bottom-line instability)
def f25mc_f25_margin_cyclicality_nmvol_504d_base_v087_signal(netmargin):
    b = _std(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin short-quarter volatility (tactical margin instability)
def f25mc_f25_margin_cyclicality_gmvol_63d_base_v088_signal(grossmargin):
    b = _std(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin coefficient of variation over a year (level-normalized instability)
def f25mc_f25_margin_cyclicality_nmcov_252d_base_v089_signal(netmargin):
    sd = _std(netmargin, 252)
    mu = _mean(netmargin, 252)
    b = sd / mu.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin vol acceleration: 63d vol now minus 63d vol a quarter ago (vol regime shift)
def f25mc_f25_margin_cyclicality_gmvolchg_base_v090_signal(grossmargin):
    v = _std(grossmargin, 63)
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin semi-deviation ratio: downside vol vs upside vol (loss-skew of swings)
def f25mc_f25_margin_cyclicality_nmsemiratio_252d_base_v091_signal(netmargin):
    mu = _mean(netmargin, 252)
    dn = (netmargin - mu).clip(upper=0.0)
    up = (netmargin - mu).clip(lower=0.0)
    dvol = (dn * dn).rolling(252, min_periods=84).mean() ** 0.5
    uvol = (up * up).rolling(252, min_periods=84).mean() ** 0.5
    b = dvol / uvol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin vol-of-vol over a long window (instability of margin instability, 504d)
def f25mc_f25_margin_cyclicality_gmvov_504d_base_v092_signal(grossmargin):
    v = _std(grossmargin, 126)
    b = _std(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin stability quality: mean over std across a long 504d cycle
def f25mc_f25_margin_cyclicality_emstab_504d_base_v093_signal(ebitdamargin):
    mu = _mean(ebitdamargin, 504)
    sd = _std(ebitdamargin, 504)
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin vol term structure: short 63d vol vs long 504d vol (vol curve)
def f25mc_f25_margin_cyclicality_nmvolterm_base_v094_signal(netmargin):
    vs = _std(netmargin, 63)
    vl = _std(netmargin, 504)
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin instability percentile rank within its long cycle (vol regime rank)
def f25mc_f25_margin_cyclicality_gmvolrank_504d_base_v095_signal(grossmargin):
    v = _std(grossmargin, 126)
    b = _rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 3: AMPLITUDE (long horizons & new facets) ====

# gross-margin amplitude over the long 504d cycle (structural swing span)
def f25mc_f25_margin_cyclicality_gmamp_504d_base_v096_signal(grossmargin):
    b = _f25_amplitude(grossmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin amplitude expansion vs a year ago (long-horizon bottom-line cycle widening)
def f25mc_f25_margin_cyclicality_nmamp_252d_base_v097_signal(netmargin):
    amp = _f25_amplitude(netmargin, 252)
    b = amp - amp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin amplitude expansion vs a year ago (is the cycle widening)
def f25mc_f25_margin_cyclicality_gmampexp_504d_base_v098_signal(grossmargin):
    amp = _f25_amplitude(grossmargin, 252)
    b = amp - amp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin amplitude in vol-units over a long window (swing efficiency, 504d)
def f25mc_f25_margin_cyclicality_nmamprel_504d_base_v099_signal(netmargin):
    amp = _f25_amplitude(netmargin, 504)
    sd = _std(netmargin, 126)
    b = amp / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin amplitude rank within a 504d cycle (extreme-swing regime)
def f25mc_f25_margin_cyclicality_gmamprank_504d_base_v100_signal(grossmargin):
    amp = _f25_amplitude(grossmargin, 252)
    b = _rank(amp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trend persistence: fraction of the quarter the EBIT margin improved (regime)
def f25mc_f25_margin_cyclicality_omenergy_252d_base_v101_signal(opinc, revenue):
    om = _f25_op_margin(opinc, revenue)
    up = (om.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin amplitude asymmetry: peak-side span minus trough-side span vs median
def f25mc_f25_margin_cyclicality_nmampskew_252d_base_v102_signal(netmargin):
    hi = _rmax(netmargin, 252)
    lo = _rmin(netmargin, 252)
    med = netmargin.rolling(252, min_periods=84).median()
    b = (hi - med) - (med - lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin range crush: how much the 63d range sits inside the 252d range (compression)
def f25mc_f25_margin_cyclicality_gmrangecrush_base_v103_signal(grossmargin):
    short = _f25_amplitude(grossmargin, 63)
    long = _f25_amplitude(grossmargin, 252)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin persistence: lag-21 autocorrelation of its daily changes over a long window
def f25mc_f25_margin_cyclicality_nmpathlen_504d_base_v104_signal(netmargin):
    d = netmargin.diff()
    b = d.rolling(504, min_periods=168).apply(
        lambda a: pd.Series(a).autocorr(21) if np.std(a) > 0 else np.nan, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin swing efficiency: net 252d displacement over total path (directionality)
def f25mc_f25_margin_cyclicality_gmswingeff_252d_base_v105_signal(grossmargin):
    net = (grossmargin - grossmargin.shift(252)).abs()
    path = grossmargin.diff().abs().rolling(252, min_periods=84).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 4: SPREAD DYNAMICS (cross-cluster, new facets vs file 1) ====

# gross-vs-net spread directional efficiency: net 252d change over total path (cost-wedge trendiness)
def f25mc_f25_margin_cyclicality_gnspreadamp_504d_base_v106_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    net = (sp - sp.shift(252)).abs()
    path = sp.diff().abs().rolling(252, min_periods=84).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread range position (where the cost wedge sits in its own cycle)
def f25mc_f25_margin_cyclicality_gnspreadpos_252d_base_v107_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    b = _f25_range_pos(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-ebitda spread z-score level (D&A+opex burden vs its own 252d cycle)
def f25mc_f25_margin_cyclicality_gespreadtrend_126d_base_v108_signal(grossmargin, ebitdamargin):
    sp = grossmargin - ebitdamargin
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-minus-net spread range position (where the interest+tax wedge sits in its own cycle)
def f25mc_f25_margin_cyclicality_enspreadvol_252d_base_v109_signal(ebitdamargin, netmargin):
    sp = ebitdamargin - netmargin
    b = _f25_range_pos(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net pass-through: change in net per unit change in gross over a quarter (flow-through)
def f25mc_f25_margin_cyclicality_passthru_base_v110_signal(grossmargin, netmargin):
    dn = netmargin - netmargin.shift(63)
    dg = grossmargin - grossmargin.shift(63)
    b = (dn / dg.replace(0, np.nan)).clip(-5.0, 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread compression ratio: gross-net spread now vs its 252d mean (cost-wedge tightening)
def f25mc_f25_margin_cyclicality_gnspreadcompress_base_v111_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = sp.rolling(252, min_periods=84).mean()
    b = sp / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin expansion-regime count: quarters in the year EBIT margin rose vs prior quarter
def f25mc_f25_margin_cyclicality_gospreadvol_252d_base_v112_signal(opinc, revenue):
    om = _f25_op_margin(opinc, revenue)
    q = om.rolling(63, min_periods=21).mean()
    up = (q.diff(63) > 0).astype(float)
    b = up.rolling(252, min_periods=84).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-minus-net spread rank within its long cycle (interest+tax wedge rank)
def f25mc_f25_margin_cyclicality_onspreadrank_504d_base_v113_signal(opinc, revenue, netmargin):
    om = _f25_op_margin(opinc, revenue)
    sp = om - netmargin
    b = _rank(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# swing retention: how much of gross-margin amplitude survives down to net (cost leverage)
def f25mc_f25_margin_cyclicality_swingretention_base_v114_signal(grossmargin, netmargin):
    ga = _f25_amplitude(grossmargin, 252)
    na = _f25_amplitude(netmargin, 252)
    b = na / ga.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread MA-crossover (fast 63d minus slow 252d mean) — cost-wedge direction
def f25mc_f25_margin_cyclicality_gnspreadyoy_base_v115_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    fast = sp.rolling(63, min_periods=21).mean()
    slow = sp.rolling(252, min_periods=84).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 5: TREND / PERSISTENCE (long horizons & new facets) ====

# gross-margin trend over a long 252d horizon (structural margin direction)
def f25mc_f25_margin_cyclicality_gmtrend_252d_base_v116_signal(grossmargin):
    b = _slope(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend strength over a half-year: 126d slope per 126d vol (reliable bottom-line direction)
def f25mc_f25_margin_cyclicality_nmtrend_126d_base_v117_signal(netmargin):
    sl = _slope(netmargin, 126)
    vol = _std(netmargin, 126)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin autocorrelation at lag 21 of daily changes (margin momentum/reversal)
def f25mc_f25_margin_cyclicality_gmac21_252d_base_v118_signal(grossmargin):
    b = _f25_autocorr(grossmargin.diff(), 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin autocorrelation at lag 5 of daily changes (short bottom-line persistence)
def f25mc_f25_margin_cyclicality_nmac5_252d_base_v119_signal(netmargin):
    b = _f25_autocorr(netmargin.diff(), 252, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin efficiency ratio over 126d: net change over summed absolute change (trendiness)
def f25mc_f25_margin_cyclicality_gmeff_126d_base_v120_signal(grossmargin):
    net = (grossmargin - grossmargin.shift(126)).abs()
    path = grossmargin.diff().abs().rolling(126, min_periods=42).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend strength over a long horizon: slope per 252d vol (reliable direction)
def f25mc_f25_margin_cyclicality_nmtrendstr_252d_base_v121_signal(netmargin):
    sl = _slope(netmargin, 252)
    vol = _std(netmargin, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin MA-crossover over long windows (126d vs 504d structural crossover)
def f25mc_f25_margin_cyclicality_gmmacrosslong_base_v122_signal(grossmargin):
    fast = grossmargin.rolling(126, min_periods=42).mean()
    slow = grossmargin.rolling(504, min_periods=168).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trend acceleration: 63d slope now minus a quarter ago (cash-margin curvature)
def f25mc_f25_margin_cyclicality_emtrendaccel_base_v123_signal(ebitdamargin):
    sl = _slope(ebitdamargin, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin EWMA displacement vs a slow EMA (bottom-line trend displacement)
def f25mc_f25_margin_cyclicality_nmemadisp_base_v124_signal(netmargin):
    b = netmargin - netmargin.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin tanh-squashed half-year change (bounded medium-horizon margin swing)
def f25mc_f25_margin_cyclicality_gmhytanh_base_v125_signal(grossmargin):
    chg = grossmargin - grossmargin.shift(126)
    b = np.tanh(10.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 6: TROUGH / PEAK / CYCLE-PHASE (long horizons & new facets) ====

# days since gross-margin 504d cyclical peak (staleness of the structural margin high)
def f25mc_f25_margin_cyclicality_gmtrough_504d_base_v126_signal(grossmargin):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = grossmargin.rolling(504, min_periods=168).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since net-margin 504d cyclical trough (staleness of the structural bottom-line low)
def f25mc_f25_margin_cyclicality_nmpeak_504d_base_v127_signal(netmargin):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = netmargin.rolling(504, min_periods=168).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin range position over a short 126d cycle (short-cycle phase)
def f25mc_f25_margin_cyclicality_gmrangepos_504d_base_v128_signal(grossmargin):
    b = _f25_range_pos(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin range position over a very short 63d cycle (tactical-cycle phase)
def f25mc_f25_margin_cyclicality_nmrangepos_126d_base_v129_signal(netmargin):
    b = _f25_range_pos(netmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since gross-margin long 504d trough (staleness of the structural margin low)
def f25mc_f25_margin_cyclicality_gmdsl_504d_base_v130_signal(grossmargin):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = grossmargin.rolling(504, min_periods=168).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since net-margin long 504d peak (staleness of the structural bottom-line high)
def f25mc_f25_margin_cyclicality_nmdsh_504d_base_v131_signal(netmargin):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = netmargin.rolling(504, min_periods=168).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin peak compression in vol-units (distance below 252d peak per 63d vol)
def f25mc_f25_margin_cyclicality_gmpeakrel_252d_base_v132_signal(grossmargin):
    pk = _rmax(grossmargin, 252) - grossmargin
    sd = _std(grossmargin, 63)
    b = pk / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trough-touch fraction over a long window (time spent near the 252d low)
def f25mc_f25_margin_cyclicality_nmtroughtouch_504d_base_v133_signal(netmargin):
    lo = _rmin(netmargin, 252)
    hi = _rmax(netmargin, 252)
    nearness = (hi - netmargin) / (hi - lo).replace(0, np.nan)
    b = nearness.rolling(504, min_periods=168).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin good-time fraction over a long window (share in upper third over 504d)
def f25mc_f25_margin_cyclicality_gmuppertime_504d_base_v134_signal(grossmargin):
    pos = _f25_range_pos(grossmargin, 252)
    upper = (pos >= 0.6667).astype(float)
    b = upper.rolling(504, min_periods=168).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin V-shape balance: recovery off 252d trough vs compression below 252d peak
def f25mc_f25_margin_cyclicality_nmvshape_252d_base_v135_signal(netmargin):
    rec = netmargin - _rmin(netmargin, 252)
    comp = _rmax(netmargin, 252) - netmargin
    b = (rec - comp) / (rec + comp).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 7: REGIME / ASYMMETRY / ENTROPY (count-friendly) ====

# gross-margin expansion-regime fraction: share of the year the smoothed margin rose
def f25mc_f25_margin_cyclicality_gmexpandfreq_252d_base_v136_signal(grossmargin):
    sm = grossmargin.rolling(21, min_periods=7).mean()
    up = (sm.diff() > 0).astype(float)
    b = up.rolling(252, min_periods=84).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin below-median weakness streak (consecutive sub-par bottom-line days)
def f25mc_f25_margin_cyclicality_nmweakstreak_base_v137_signal(netmargin):
    med = netmargin.rolling(252, min_periods=84).median()
    weak = (netmargin < med).astype(float)
    grp = (weak == 0).cumsum()
    b = weak.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin regime balance: magnitude-weighted time above vs below its 252d mean
def f25mc_f25_margin_cyclicality_gmregimebal_252d_base_v138_signal(grossmargin):
    mu = grossmargin.rolling(252, min_periods=84).mean()
    dev = grossmargin - mu
    up = dev.clip(lower=0.0).rolling(252, min_periods=84).sum()
    dn = (-dev).clip(lower=0.0).rolling(252, min_periods=84).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin distributional skew over a long 504d cycle (long bottom-line asymmetry)
def f25mc_f25_margin_cyclicality_nmskew_504d_base_v139_signal(netmargin):
    b = netmargin.rolling(504, min_periods=168).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin tail kurtosis over a long 504d cycle (fat-tailed structural margin shocks)
def f25mc_f25_margin_cyclicality_gmkurt_504d_base_v140_signal(grossmargin):
    b = grossmargin.rolling(504, min_periods=168).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin strength regime: fraction of year cash margin above its 504d median (strong-margin time)
def f25mc_f25_margin_cyclicality_emposfreq_252d_base_v141_signal(ebitdamargin):
    med = ebitdamargin.rolling(504, min_periods=126).median()
    strong = (ebitdamargin > med).astype(float)
    b = strong.rolling(252, min_periods=84).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin distribution entropy: spread of the margin histogram over a year (regime breadth)
def f25mc_f25_margin_cyclicality_gmentropy_252d_base_v142_signal(grossmargin):
    def _ent(a):
        a = a[np.isfinite(a)]
        if len(a) < 10 or np.ptp(a) == 0:
            return np.nan
        h, _ = np.histogram(a, bins=8)
        p = h / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    b = grossmargin.rolling(252, min_periods=84).apply(_ent, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin time-near-trough-band: fraction of year within 20% of amplitude of the low
def f25mc_f25_margin_cyclicality_nmlowband_252d_base_v143_signal(netmargin):
    lo = _rmin(netmargin, 252)
    amp = _f25_amplitude(netmargin, 252)
    near = ((netmargin - lo) / amp.replace(0, np.nan) <= 0.20).astype(float)
    b = near.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin recovery momentum: run-up off trough now vs a quarter ago (rebound accel)
def f25mc_f25_margin_cyclicality_gmrebound_base_v144_signal(grossmargin):
    ru = grossmargin - _rmin(grossmargin, 252)
    b = ru - ru.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin worst relative dip: deepest below-median gross-margin dip as a fraction of median (top-line stress)
def f25mc_f25_margin_cyclicality_nmworstdip_252d_base_v145_signal(grossmargin):
    med = grossmargin.rolling(126, min_periods=42).median()
    dip = (med - grossmargin).clip(lower=0.0) / med.abs().replace(0, np.nan)
    b = dip.rolling(252, min_periods=84).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ==== BLOCK 8: CROSS-MARGIN COMPOSITES (new facets vs file 1) ====

# rolling corr of gross & ebitda margins over a year (top-line vs cash margin co-movement)
def f25mc_f25_margin_cyclicality_gecorr_252d_base_v146_signal(grossmargin, ebitdamargin):
    b = grossmargin.rolling(252, min_periods=84).corr(ebitdamargin)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling beta of net margin to ebitda margin (below-EBITDA leverage)
def f25mc_f25_margin_cyclicality_nebeta_252d_base_v147_signal(ebitdamargin, netmargin):
    cov = ebitdamargin.rolling(252, min_periods=84).cov(netmargin)
    var = ebitdamargin.rolling(252, min_periods=84).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# four-margin dispersion: spread across gross/net/ebitda/operating margins (disagreement)
def f25mc_f25_margin_cyclicality_margindisp4_base_v148_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = _f25_op_margin(opinc, revenue)
    stacked = pd.concat([grossmargin, netmargin, ebitdamargin, om], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-phase lag: gross-margin range-pos momentum minus net-margin range-pos momentum
def f25mc_f25_margin_cyclicality_phaselag_base_v149_signal(grossmargin, netmargin):
    gp = _f25_range_pos(grossmargin, 252)
    np_ = _f25_range_pos(netmargin, 252)
    b = (gp - gp.shift(63)) - (np_ - np_.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-quality composite: gp-margin rank times tanh of its trend strength (durable rising margin)
def f25mc_f25_margin_cyclicality_qualcomposite_base_v150_signal(gp, revenue):
    gm = _f25_gp_margin(gp, revenue)
    lvl = _rank(gm, 252)
    sl = _slope(gm, 126)
    vol = _std(gm, 126)
    str_ = sl / vol.replace(0, np.nan)
    b = lvl * np.tanh(str_)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25mc_f25_margin_cyclicality_gmlevelz_504d_base_v076_signal,
    f25mc_f25_margin_cyclicality_nmlevelz_252d_base_v077_signal,
    f25mc_f25_margin_cyclicality_gmlevel_252d_base_v078_signal,
    f25mc_f25_margin_cyclicality_nmrank_504d_base_v079_signal,
    f25mc_f25_margin_cyclicality_emlevel_126d_base_v080_signal,
    f25mc_f25_margin_cyclicality_gmmidz_252d_base_v081_signal,
    f25mc_f25_margin_cyclicality_omlevel_63d_base_v082_signal,
    f25mc_f25_margin_cyclicality_nmvspeak_504d_base_v083_signal,
    f25mc_f25_margin_cyclicality_gmfloor_504d_base_v084_signal,
    f25mc_f25_margin_cyclicality_emperscale_base_v085_signal,
    f25mc_f25_margin_cyclicality_gmvol_504d_base_v086_signal,
    f25mc_f25_margin_cyclicality_nmvol_504d_base_v087_signal,
    f25mc_f25_margin_cyclicality_gmvol_63d_base_v088_signal,
    f25mc_f25_margin_cyclicality_nmcov_252d_base_v089_signal,
    f25mc_f25_margin_cyclicality_gmvolchg_base_v090_signal,
    f25mc_f25_margin_cyclicality_nmsemiratio_252d_base_v091_signal,
    f25mc_f25_margin_cyclicality_gmvov_504d_base_v092_signal,
    f25mc_f25_margin_cyclicality_emstab_504d_base_v093_signal,
    f25mc_f25_margin_cyclicality_nmvolterm_base_v094_signal,
    f25mc_f25_margin_cyclicality_gmvolrank_504d_base_v095_signal,
    f25mc_f25_margin_cyclicality_gmamp_504d_base_v096_signal,
    f25mc_f25_margin_cyclicality_nmamp_252d_base_v097_signal,
    f25mc_f25_margin_cyclicality_gmampexp_504d_base_v098_signal,
    f25mc_f25_margin_cyclicality_nmamprel_504d_base_v099_signal,
    f25mc_f25_margin_cyclicality_gmamprank_504d_base_v100_signal,
    f25mc_f25_margin_cyclicality_omenergy_252d_base_v101_signal,
    f25mc_f25_margin_cyclicality_nmampskew_252d_base_v102_signal,
    f25mc_f25_margin_cyclicality_gmrangecrush_base_v103_signal,
    f25mc_f25_margin_cyclicality_nmpathlen_504d_base_v104_signal,
    f25mc_f25_margin_cyclicality_gmswingeff_252d_base_v105_signal,
    f25mc_f25_margin_cyclicality_gnspreadamp_504d_base_v106_signal,
    f25mc_f25_margin_cyclicality_gnspreadpos_252d_base_v107_signal,
    f25mc_f25_margin_cyclicality_gespreadtrend_126d_base_v108_signal,
    f25mc_f25_margin_cyclicality_enspreadvol_252d_base_v109_signal,
    f25mc_f25_margin_cyclicality_passthru_base_v110_signal,
    f25mc_f25_margin_cyclicality_gnspreadcompress_base_v111_signal,
    f25mc_f25_margin_cyclicality_gospreadvol_252d_base_v112_signal,
    f25mc_f25_margin_cyclicality_onspreadrank_504d_base_v113_signal,
    f25mc_f25_margin_cyclicality_swingretention_base_v114_signal,
    f25mc_f25_margin_cyclicality_gnspreadyoy_base_v115_signal,
    f25mc_f25_margin_cyclicality_gmtrend_252d_base_v116_signal,
    f25mc_f25_margin_cyclicality_nmtrend_126d_base_v117_signal,
    f25mc_f25_margin_cyclicality_gmac21_252d_base_v118_signal,
    f25mc_f25_margin_cyclicality_nmac5_252d_base_v119_signal,
    f25mc_f25_margin_cyclicality_gmeff_126d_base_v120_signal,
    f25mc_f25_margin_cyclicality_nmtrendstr_252d_base_v121_signal,
    f25mc_f25_margin_cyclicality_gmmacrosslong_base_v122_signal,
    f25mc_f25_margin_cyclicality_emtrendaccel_base_v123_signal,
    f25mc_f25_margin_cyclicality_nmemadisp_base_v124_signal,
    f25mc_f25_margin_cyclicality_gmhytanh_base_v125_signal,
    f25mc_f25_margin_cyclicality_gmtrough_504d_base_v126_signal,
    f25mc_f25_margin_cyclicality_nmpeak_504d_base_v127_signal,
    f25mc_f25_margin_cyclicality_gmrangepos_504d_base_v128_signal,
    f25mc_f25_margin_cyclicality_nmrangepos_126d_base_v129_signal,
    f25mc_f25_margin_cyclicality_gmdsl_504d_base_v130_signal,
    f25mc_f25_margin_cyclicality_nmdsh_504d_base_v131_signal,
    f25mc_f25_margin_cyclicality_gmpeakrel_252d_base_v132_signal,
    f25mc_f25_margin_cyclicality_nmtroughtouch_504d_base_v133_signal,
    f25mc_f25_margin_cyclicality_gmuppertime_504d_base_v134_signal,
    f25mc_f25_margin_cyclicality_nmvshape_252d_base_v135_signal,
    f25mc_f25_margin_cyclicality_gmexpandfreq_252d_base_v136_signal,
    f25mc_f25_margin_cyclicality_nmweakstreak_base_v137_signal,
    f25mc_f25_margin_cyclicality_gmregimebal_252d_base_v138_signal,
    f25mc_f25_margin_cyclicality_nmskew_504d_base_v139_signal,
    f25mc_f25_margin_cyclicality_gmkurt_504d_base_v140_signal,
    f25mc_f25_margin_cyclicality_emposfreq_252d_base_v141_signal,
    f25mc_f25_margin_cyclicality_gmentropy_252d_base_v142_signal,
    f25mc_f25_margin_cyclicality_nmlowband_252d_base_v143_signal,
    f25mc_f25_margin_cyclicality_gmrebound_base_v144_signal,
    f25mc_f25_margin_cyclicality_nmworstdip_252d_base_v145_signal,
    f25mc_f25_margin_cyclicality_gecorr_252d_base_v146_signal,
    f25mc_f25_margin_cyclicality_nebeta_252d_base_v147_signal,
    f25mc_f25_margin_cyclicality_margindisp4_base_v148_signal,
    f25mc_f25_margin_cyclicality_phaselag_base_v149_signal,
    f25mc_f25_margin_cyclicality_qualcomposite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_MARGIN_CYCLICALITY_REGISTRY_076_150 = REGISTRY


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

    grossmargin = _fund(2501, base=0.32, drift=0.0, vol=0.16).rename("grossmargin")
    netmargin = _fund(2502, base=0.12, drift=0.0, vol=0.30, allow_neg=False).rename("netmargin")
    ebitdamargin = _fund(2503, base=0.22, drift=0.0, vol=0.22).rename("ebitdamargin")
    opinc = _fund(2504, base=8e7, drift=0.0, vol=0.26, allow_neg=True).rename("opinc")
    revenue = _fund(2505, base=6e8, drift=0.01, vol=0.12).rename("revenue")
    gp = _fund(2506, base=2e8, drift=0.0, vol=0.16).rename("gp")

    cols = {"grossmargin": grossmargin, "netmargin": netmargin,
            "ebitdamargin": ebitdamargin, "opinc": opinc,
            "revenue": revenue, "gp": gp}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("grossmargin", "netmargin", "ebitdamargin",
                         "opinc", "revenue", "gp")
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

    print("OK f25_margin_cyclicality_base_076_150_claude: %d features pass" % n_features)
