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


# ===== folder domain primitives (volatility regime / compression-expansion) =====
def _f11_ret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f11_vol(closeadj, w):
    r = _f11_ret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f11_bbwidth(closeadj, w):
    m = closeadj.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = closeadj.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f11_compress_ratio(closeadj, ws, wl):
    vs = _f11_vol(closeadj, ws)
    vl = _f11_vol(closeadj, wl)
    return vs / vl.replace(0, np.nan)


def _f11_volofvol(closeadj, wv, ws):
    v = _f11_vol(closeadj, wv)
    return v.rolling(ws, min_periods=max(2, ws // 2)).std() / v.rolling(ws, min_periods=max(2, ws // 2)).mean().replace(0, np.nan)


def _f11_truerange(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11_atr(high, low, closeadj, w):
    tr = _f11_truerange(high, low, closeadj)
    return tr.rolling(w, min_periods=max(2, w // 2)).mean()


def _f11_squeeze_pct(closeadj, w, lookback):
    bw = _f11_bbwidth(closeadj, w)
    return bw.rolling(lookback, min_periods=max(2, lookback // 4)).rank(pct=True)


def _f11_parkinson(high, low, w):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    return (hl.rolling(w, min_periods=max(2, w // 2)).mean() / (4.0 * np.log(2.0))) ** 0.5


# ============================================================
# expansion ratio 10d vs 126d (compression/expansion regime)
def f11vr_f11_volatility_regime_shift_compr_v076_signal(closeadj):
    b = _f11_compress_ratio(closeadj, 10, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio 5d vs 252d (very short vs very long regime gap)
def f11vr_f11_volatility_regime_shift_compr_v077_signal(closeadj):
    b = _f11_compress_ratio(closeadj, 5, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio of band-widths: 21d band width vs 126d band width
def f11vr_f11_volatility_regime_shift_bbwcompr_v078_signal(closeadj):
    bs = _f11_bbwidth(closeadj, 21)
    bl = _f11_bbwidth(closeadj, 126)
    b = bs / bl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width compression z-scored (band-tightening regime extremity)
def f11vr_f11_volatility_regime_shift_bbwcomprz_v079_signal(closeadj):
    bs = _f11_bbwidth(closeadj, 10)
    bl = _f11_bbwidth(closeadj, 63)
    ratio = bs / bl.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of band width: instability of the compression state itself
def f11vr_f11_volatility_regime_shift_bbwvov_v080_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    b = bw.rolling(63, min_periods=21).std() / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze percentile of parkinson range vol (hi-lo based squeeze)
def f11vr_f11_volatility_regime_shift_pksqueeze_v081_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = pk.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parkinson vol regime acceleration (range-vol momentum over a month)
def f11vr_f11_volatility_regime_shift_pkaccel_v082_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = pk / pk.shift(21).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z using parkinson on a quarter window
def f11vr_f11_volatility_regime_shift_pkregz_v083_signal(high, low):
    pk = _f11_parkinson(high, low, 63)
    b = _z(pk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-to-range vol gap: realized vol vs parkinson vol (gap-vs-intraday regime)
def f11vr_f11_volatility_regime_shift_volgaptype_v084_signal(high, low, closeadj):
    rv = _f11_vol(closeadj, 21)
    pk = _f11_parkinson(high, low, 21)
    b = rv / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime persistence: AR(1)-like slope of 21d vol on its own lag (clustering)
def f11vr_f11_volatility_regime_shift_volcluster_v085_signal(closeadj):
    v = _f11_vol(closeadj, 5)
    vl = v.shift(5)
    cov = (v * vl).rolling(63, min_periods=21).mean() - v.rolling(63, min_periods=21).mean() * vl.rolling(63, min_periods=21).mean()
    var = vl.rolling(63, min_periods=21).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band width relative to its 252d max (how far from peak expansion)
def f11vr_f11_volatility_regime_shift_bbwfrommax_v086_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    mx = bw.rolling(252, min_periods=63).max()
    b = bw / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion thrust: band width now vs its value 5 days ago (fast widening)
def f11vr_f11_volatility_regime_shift_bbwthrust_v087_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    b = bw / bw.shift(5).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime tilt: 63d vol percentile minus 252d vol percentile (medium vs long regime)
def f11vr_f11_volatility_regime_shift_voltilt_v088_signal(closeadj):
    v63 = _f11_vol(closeadj, 63)
    p_med = v63.rolling(252, min_periods=63).rank(pct=True)
    p_long = v63.rolling(504, min_periods=126).rank(pct=True)
    b = p_med - p_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range contraction streak depth in ATR terms (consecutive narrowing TR days)
def f11vr_f11_volatility_regime_shift_trcontr_v089_signal(high, low, closeadj):
    tr = _f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)
    sm = tr.rolling(5, min_periods=3).mean()
    narrowing = (sm.diff() < 0).astype(float)
    grp = (narrowing == 0).cumsum()
    streak = narrowing.groupby(grp).cumsum()
    depth = 1.0 - sm / sm.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = streak * (1.0 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze: TR expansion intensity following a parkinson squeeze
def f11vr_f11_volatility_regime_shift_pkbreakout_v090_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 21)
    sq = pk.rolling(252, min_periods=63).rank(pct=True)
    was_sq = (sq.shift(1) <= 0.20).astype(float)
    tr = _f11_truerange(high, low, closeadj)
    impulse = tr / _f11_atr(high, low, closeadj, 63).replace(0, np.nan)
    b = (was_sq * impulse).ewm(span=10, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration sign x magnitude (signed sqrt of monthly vol change)
def f11vr_f11_volatility_regime_shift_volaccsm_v091_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    chg = v / v.shift(21).replace(0, np.nan) - 1.0
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime range: 252d high-low of vol normalized by mean (regime amplitude)
def f11vr_f11_volatility_regime_shift_volamp_v092_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    amp = (v.rolling(252, min_periods=63).max() - v.rolling(252, min_periods=63).min())
    b = amp / v.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %b dispersion: rolling std of where price sits in its bands (regime of band travel)
def f11vr_f11_volatility_regime_shift_pctbdisp_v093_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    b = pctb.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol on a long window scaled by current vol level (instability x level)
def f11vr_f11_volatility_regime_shift_vovlevel_v094_signal(closeadj):
    vov = _f11_volofvol(closeadj, 21, 126)
    vlvl = _rank(_f11_vol(closeadj, 21), 252) + 0.5
    b = vov * vlvl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio EWM minus its slow EWM (regime-shift oscillator)
def f11vr_f11_volatility_regime_shift_comprosc_v095_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 10, 63)
    b = cr.ewm(span=10, min_periods=5).mean() - cr.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime hysteresis: difference between fast and slow vol percentile
def f11vr_f11_volatility_regime_shift_volhyst_v096_signal(closeadj):
    pf = _rank(_f11_vol(closeadj, 10), 252)
    ps = _rank(_f11_vol(closeadj, 63), 252)
    b = pf - ps
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion breadth: fraction of last month with above-median true range, signed by level
def f11vr_f11_volatility_regime_shift_expbreadth_v097_signal(high, low, closeadj):
    tr = _f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)
    med = tr.rolling(126, min_periods=42).median()
    excess = (tr - med) / med.replace(0, np.nan)
    b = excess.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze intensity weighted by duration (how deep AND how long band width stays tight)
def f11vr_f11_volatility_regime_shift_sqintensity_v098_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    tight = (0.30 - sq).clip(lower=0)
    b = tight.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime skew: skewness of the 21d vol series over a half year (asymmetric regime)
def f11vr_f11_volatility_regime_shift_volskew_v099_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    b = v.rolling(126, min_periods=42).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio kurtosis-like tail of vol changes (regime jumpiness)
def f11vr_f11_volatility_regime_shift_volkurt_v100_signal(closeadj):
    dv = _f11_vol(closeadj, 21).diff()
    b = dv.rolling(126, min_periods=42).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width to ATR-width ratio change (regime divergence momentum)
def f11vr_f11_volatility_regime_shift_bbwatrmom_v101_signal(high, low, closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    atrp = _f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    ratio = bw / atrp.replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime reversion speed: how fast vol returns toward 252d mean (negative feedback)
def f11vr_f11_volatility_regime_shift_volrevspeed_v102_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    mn = v.rolling(252, min_periods=63).mean()
    gap = (v - mn)
    b = -(gap.shift(-0) - gap.shift(5)) / gap.shift(5).replace(0, np.nan)
    b = (gap.shift(5) - gap) / gap.shift(5).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol of overlapping 5d returns vs 1d returns (term-structure-free regime curvature)
def f11vr_f11_volatility_regime_shift_volscaling_v103_signal(closeadj):
    r1 = _f11_ret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v1 = r1.rolling(63, min_periods=21).std() * np.sqrt(5.0)
    v5 = r5.rolling(63, min_periods=21).std()
    b = v5 / v1.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion regime flag decayed: above-90th-pct band width event, EWM-decayed
def f11vr_f11_volatility_regime_shift_expflag_v104_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    event = (sq >= 0.90).astype(float)
    b = event.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze regime flag decayed: below-10th-pct band width event, EWM-decayed
def f11vr_f11_volatility_regime_shift_sqflag_v105_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    event = (sq <= 0.10).astype(float)
    b = event.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime net drift: cumulative signed band-width change over a quarter, normalized
def f11vr_f11_volatility_regime_shift_bbwdrift_v106_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    chg = bw.diff()
    b = chg.rolling(63, min_periods=21).sum() / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime transition probability proxy: |Δ vol percentile| averaged (regime mobility)
def f11vr_f11_volatility_regime_shift_regmobility_v107_signal(closeadj):
    vp = _rank(_f11_vol(closeadj, 21), 252)
    b = vp.diff().abs().rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-then-trend: tight band width times subsequent absolute drift
def f11vr_f11_volatility_regime_shift_coiltrend_v108_signal(closeadj):
    bw_pct = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    drift = _f11_ret(closeadj).rolling(10, min_periods=5).sum().abs()
    b = (1.0 - bw_pct) * drift / _f11_vol(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z asymmetry: upside-vol z minus downside-vol z (which tail drives regime)
def f11vr_f11_volatility_regime_shift_volzasym_v109_signal(closeadj):
    r = _f11_ret(closeadj)
    uv = r.where(r > 0).rolling(63, min_periods=21).std()
    dv = r.where(r < 0).rolling(63, min_periods=21).std()
    b = _z(uv, 252) - _z(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band slope: rate the upper band is widening away from the mean
def f11vr_f11_volatility_regime_shift_bandslope_v110_signal(closeadj):
    sd = _std(closeadj, 21)
    upper_dist = 2.0 * sd / _mean(closeadj, 21).replace(0, np.nan)
    b = (upper_dist - upper_dist.shift(10)) / upper_dist.shift(10).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol regime z (instability extremity on a long lookback)
def f11vr_f11_volatility_regime_shift_vovz_v111_signal(closeadj):
    vov = _f11_volofvol(closeadj, 10, 42)
    b = _z(vov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio vs its own lagged self (regime-shift detector over a quarter)
def f11vr_f11_volatility_regime_shift_comprlag_v112_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 21, 126)
    b = cr - cr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized true range expansion vs its 504d median (long-horizon regime level)
def f11vr_f11_volatility_regime_shift_trlong_v113_signal(high, low, closeadj):
    trp = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    med = trp.rolling(504, min_periods=126).median()
    b = trp / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-release directional persistence: signed sum of returns while not squeezed
def f11vr_f11_volatility_regime_shift_releasedir_v114_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    not_sq = (sq > 0.5).astype(float)
    signed = not_sq * _f11_ret(closeadj)
    b = signed.rolling(21, min_periods=10).sum() / _f11_vol(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime double-z: 21d vol z relative to its own 63d-z history (regime of regimes)
def f11vr_f11_volatility_regime_shift_doublez_v115_signal(closeadj):
    z1 = _z(_f11_vol(closeadj, 21), 252)
    b = _z(z1, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width spread across windows: 21d vs 63d band width difference, normalized
def f11vr_f11_volatility_regime_shift_bbwspread_v116_signal(closeadj):
    b21 = _f11_bbwidth(closeadj, 21)
    b63 = _f11_bbwidth(closeadj, 63)
    b = (b21 - b63) / b63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol convexity in percentile space: short+long minus 2*mid percentile (curve shape)
def f11vr_f11_volatility_regime_shift_volconvex_v117_signal(closeadj):
    p5 = _rank(_f11_vol(closeadj, 5), 252)
    p21 = _rank(_f11_vol(closeadj, 21), 252)
    p63 = _rank(_f11_vol(closeadj, 63), 252)
    b = p5 + p63 - 2.0 * p21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized range efficiency: net move over the period vs sum of daily true ranges
def f11vr_f11_volatility_regime_shift_rangeeff_v118_signal(high, low, closeadj):
    net = (closeadj - closeadj.shift(21)).abs()
    path = _f11_truerange(high, low, closeadj).rolling(21, min_periods=10).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol clustering decay: ratio of 5d vol autocovariance to variance over a quarter
def f11vr_f11_volatility_regime_shift_volacf_v119_signal(closeadj):
    v = _f11_vol(closeadj, 10)
    dv = v - v.rolling(63, min_periods=21).mean()
    acf = (dv * dv.shift(10)).rolling(63, min_periods=21).mean()
    var = (dv * dv).rolling(63, min_periods=21).mean()
    b = acf / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression deviation in MAD units (robust band-width squeeze score)
def f11vr_f11_volatility_regime_shift_bbwmad_v120_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    med = bw.rolling(126, min_periods=42).median()
    mad = (bw - med).abs().rolling(126, min_periods=42).median()
    b = (bw - med) / mad.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime breakaway: current vol vs trailing minimum vol (energy released from trough)
def f11vr_f11_volatility_regime_shift_volbreakaway_v121_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    mn = v.rolling(126, min_periods=42).min()
    b = np.log(v.replace(0, np.nan) / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime ceiling proximity: current vol vs trailing max vol (near-exhaustion)
def f11vr_f11_volatility_regime_shift_volceiling_v122_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    mx = v.rolling(126, min_periods=42).max()
    b = v / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parkinson-vs-realized regime divergence z (true range vs close vol regime gap)
def f11vr_f11_volatility_regime_shift_pkrvdivz_v123_signal(high, low, closeadj):
    rv = _f11_vol(closeadj, 21)
    pk = _f11_parkinson(high, low, 21)
    gap = (pk - rv)
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width regime momentum percentile: how fast width-percentile is rising
def f11vr_f11_volatility_regime_shift_bbwpctmom_v124_signal(closeadj):
    bp = _f11_squeeze_pct(closeadj, 21, 252)
    b = bp - bp.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coiling score: low band width AND low realized range together (rank product)
def f11vr_f11_volatility_regime_shift_coilscore_v125_signal(high, low, closeadj):
    bw_pct = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    tr_pct = (_f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)).rolling(21, min_periods=10).mean().rolling(252, min_periods=63).rank(pct=True)
    b = (1.0 - bw_pct) + (1.0 - tr_pct) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime shift indicator: sign change of (vol - its EMA) frequency, magnitude-weighted
def f11vr_f11_volatility_regime_shift_volshiftmag_v126_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    dev = v - v.ewm(span=63, min_periods=21).mean()
    b = np.tanh(dev / v.rolling(252, min_periods=63).std().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion acceleration: 2nd difference of band width over weekly steps
def f11vr_f11_volatility_regime_shift_bbwaccel_v127_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    b = (bw - 2.0 * bw.shift(5) + bw.shift(10)) / bw.shift(5).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime energy: low vol now combined with high past vol (stored mean-reversion energy)
def f11vr_f11_volatility_regime_shift_regenergy_v128_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    now_low = 1.0 - v.rolling(252, min_periods=63).rank(pct=True)
    past_high = v.shift(21).rolling(252, min_periods=63).rank(pct=True)
    b = now_low * past_high
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile crossing 0.5 (regime midline) recency, decayed
def f11vr_f11_volatility_regime_shift_midcross_v129_signal(closeadj):
    vp = _rank(_f11_vol(closeadj, 21), 252)
    cross = ((np.sign(vp) != np.sign(vp.shift(1)))).astype(float)
    b = cross.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol regime stability: 1 minus coefficient of variation of parkinson vol
def f11vr_f11_volatility_regime_shift_pkstab_v130_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    cv = pk.rolling(63, min_periods=21).std() / pk.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = -cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio interaction with trend strength (quiet-trend vs quiet-chop)
def f11vr_f11_volatility_regime_shift_quiettrend_v131_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 10, 63)
    net = (closeadj - closeadj.shift(21)).abs()
    path = _f11_ret(closeadj).abs().rolling(21, min_periods=10).sum() * closeadj
    eff = net / path.replace(0, np.nan)
    b = (1.0 - cr.clip(upper=2.0) / 2.0) * eff
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime half-life proxy: lag-1 vol autocorrelation over a half year
def f11vr_f11_volatility_regime_shift_volhalflife_v132_signal(closeadj):
    v = _f11_vol(closeadj, 10)
    vn = v - v.rolling(126, min_periods=42).mean()
    num = (vn * vn.shift(1)).rolling(126, min_periods=42).mean()
    den = (vn * vn).rolling(126, min_periods=42).mean()
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze tightness vs ATR floor: band width relative to minimum ATR-implied width
def f11vr_f11_volatility_regime_shift_atrfloor_v133_signal(high, low, closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    atrp = (_f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)) * 4.0
    floor = atrp.rolling(126, min_periods=42).min()
    b = bw / floor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime expansion breadth across windows: count of vol windows above their median
def f11vr_f11_volatility_regime_shift_expconsensus_v134_signal(closeadj):
    def above(w):
        v = _f11_vol(closeadj, w)
        return (v > v.rolling(252, min_periods=63).median()).astype(float)
    s = above(5) + above(21) + above(63)
    drift = _f11_vol(closeadj, 21) / _f11_vol(closeadj, 252).replace(0, np.nan)
    b = s - 1.5 + 0.5 * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol momentum (change in instability over a month)
def f11vr_f11_volatility_regime_shift_vovmom_v135_signal(closeadj):
    vov = _f11_volofvol(closeadj, 21, 63)
    b = vov - vov.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression depth percentile vs expansion: net regime position (-1 squeeze .. +1 expand)
def f11vr_f11_volatility_regime_shift_netregime_v136_signal(closeadj):
    bw_pct = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = 2.0 * bw_pct - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol slope via linear regression over a quarter (regime trend)
def f11vr_f11_volatility_regime_shift_volregslope_v137_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    w = 63
    x = pd.Series(np.arange(len(v)), index=v.index, dtype=float)
    mx = x.rolling(w, min_periods=21).mean()
    my = v.rolling(w, min_periods=21).mean()
    cov = (x * v).rolling(w, min_periods=21).mean() - mx * my
    varx = (x * x).rolling(w, min_periods=21).mean() - mx * mx
    b = (cov / varx.replace(0, np.nan)) / my.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger width vs Donchian width ratio (band tightness vs raw range regime)
def f11vr_f11_volatility_regime_shift_bbwdonch_v138_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    donch = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / _mean(closeadj, 21).replace(0, np.nan)
    b = bw / donch.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol regime ratio: short downside semivol vs long downside semivol
def f11vr_f11_volatility_regime_shift_downratio_v139_signal(closeadj):
    r = _f11_ret(closeadj)
    dn = r.where(r < 0)
    ds = dn.rolling(21, min_periods=8).std()
    dl = dn.rolling(126, min_periods=42).std()
    b = ds / dl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime shift jump: largest single-day jump in band width over a month (sudden expansion)
def f11vr_f11_volatility_regime_shift_bbwjump_v140_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    jump = (bw.diff() / bw.shift(1).replace(0, np.nan))
    b = jump.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction then close-position bias (coiling near range edge)
def f11vr_f11_volatility_regime_shift_coiledge_v141_signal(high, low, closeadj):
    hi = _rmax(high, 21)
    lo = _rmin(low, 21)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    bw_pct = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = (1.0 - bw_pct) * (pos - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime convexity over time: band-width 2nd derivative percentile-mapped
def f11vr_f11_volatility_regime_shift_bbwconvpct_v142_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    curv = bw - 2.0 * bw.shift(10) + bw.shift(20)
    b = curv.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-day clustering: avg gap between expansion events (regime burstiness)
def f11vr_f11_volatility_regime_shift_burstiness_v143_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    exp_day = (sq >= 0.8).astype(float)
    rate = exp_day.rolling(63, min_periods=21).mean()
    inten = (sq - 0.8).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 10.0 * inten - 0.2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z difference: parkinson z minus realized z (which measure flags the regime)
def f11vr_f11_volatility_regime_shift_zmeasurediff_v144_signal(high, low, closeadj):
    pz = _z(_f11_parkinson(high, low, 21), 252)
    rz = _z(_f11_vol(closeadj, 21), 252)
    b = pz - rz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio tail: how often compression ratio dipped below 0.7 over a quarter
def f11vr_f11_volatility_regime_shift_deepcompr_v145_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 10, 63)
    deep = (0.7 - cr).clip(lower=0)
    b = deep.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-acceleration regime sign persistence (trend in vol acceleration)
def f11vr_f11_volatility_regime_shift_accelpersist_v146_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    acc = v.diff(5)
    sgn = np.sign(acc)
    b = sgn.rolling(21, min_periods=10).mean() * (acc.abs() / v.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width energy ratio: variance of band width over short vs long window
def f11vr_f11_volatility_regime_shift_bbwenergy_v147_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    vs = bw.rolling(21, min_periods=10).var()
    vl = bw.rolling(126, min_periods=42).var()
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol vs Yang-Zhang-ish drift-free range vol regime ratio
def f11vr_f11_volatility_regime_shift_rsregime_v148_signal(high, low, closeadj):
    # Rogers-Satchell drift-free estimator, smoothed, vs realized vol
    hc = np.log(high.replace(0, np.nan) / closeadj.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / closeadj.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / closeadj.shift(1).replace(0, np.nan))
    rs = (hc * ho + lc * lo).rolling(21, min_periods=10).mean().clip(lower=0) ** 0.5
    b = _z(rs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-release expectation: tightness percentile times time spent tight (loaded spring)
def f11vr_f11_volatility_regime_shift_loadedspring_v149_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    tight = (sq <= 0.25).astype(float)
    dur = tight.rolling(42, min_periods=21).sum()
    b = dur * (1.0 - sq)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window vol regime dispersion z (regime disagreement extremity)
def f11vr_f11_volatility_regime_shift_regdispz_v150_signal(closeadj):
    p5 = _rank(_f11_vol(closeadj, 5), 252)
    p21 = _rank(_f11_vol(closeadj, 21), 252)
    p63 = _rank(_f11_vol(closeadj, 63), 252)
    p126 = _rank(_f11_vol(closeadj, 126), 252)
    disp = pd.concat([p5, p21, p63, p126], axis=1).std(axis=1)
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11vr_f11_volatility_regime_shift_compr_v076_signal,
    f11vr_f11_volatility_regime_shift_compr_v077_signal,
    f11vr_f11_volatility_regime_shift_bbwcompr_v078_signal,
    f11vr_f11_volatility_regime_shift_bbwcomprz_v079_signal,
    f11vr_f11_volatility_regime_shift_bbwvov_v080_signal,
    f11vr_f11_volatility_regime_shift_pksqueeze_v081_signal,
    f11vr_f11_volatility_regime_shift_pkaccel_v082_signal,
    f11vr_f11_volatility_regime_shift_pkregz_v083_signal,
    f11vr_f11_volatility_regime_shift_volgaptype_v084_signal,
    f11vr_f11_volatility_regime_shift_volcluster_v085_signal,
    f11vr_f11_volatility_regime_shift_bbwfrommax_v086_signal,
    f11vr_f11_volatility_regime_shift_bbwthrust_v087_signal,
    f11vr_f11_volatility_regime_shift_voltilt_v088_signal,
    f11vr_f11_volatility_regime_shift_trcontr_v089_signal,
    f11vr_f11_volatility_regime_shift_pkbreakout_v090_signal,
    f11vr_f11_volatility_regime_shift_volaccsm_v091_signal,
    f11vr_f11_volatility_regime_shift_volamp_v092_signal,
    f11vr_f11_volatility_regime_shift_pctbdisp_v093_signal,
    f11vr_f11_volatility_regime_shift_vovlevel_v094_signal,
    f11vr_f11_volatility_regime_shift_comprosc_v095_signal,
    f11vr_f11_volatility_regime_shift_volhyst_v096_signal,
    f11vr_f11_volatility_regime_shift_expbreadth_v097_signal,
    f11vr_f11_volatility_regime_shift_sqintensity_v098_signal,
    f11vr_f11_volatility_regime_shift_volskew_v099_signal,
    f11vr_f11_volatility_regime_shift_volkurt_v100_signal,
    f11vr_f11_volatility_regime_shift_bbwatrmom_v101_signal,
    f11vr_f11_volatility_regime_shift_volrevspeed_v102_signal,
    f11vr_f11_volatility_regime_shift_volscaling_v103_signal,
    f11vr_f11_volatility_regime_shift_expflag_v104_signal,
    f11vr_f11_volatility_regime_shift_sqflag_v105_signal,
    f11vr_f11_volatility_regime_shift_bbwdrift_v106_signal,
    f11vr_f11_volatility_regime_shift_regmobility_v107_signal,
    f11vr_f11_volatility_regime_shift_coiltrend_v108_signal,
    f11vr_f11_volatility_regime_shift_volzasym_v109_signal,
    f11vr_f11_volatility_regime_shift_bandslope_v110_signal,
    f11vr_f11_volatility_regime_shift_vovz_v111_signal,
    f11vr_f11_volatility_regime_shift_comprlag_v112_signal,
    f11vr_f11_volatility_regime_shift_trlong_v113_signal,
    f11vr_f11_volatility_regime_shift_releasedir_v114_signal,
    f11vr_f11_volatility_regime_shift_doublez_v115_signal,
    f11vr_f11_volatility_regime_shift_bbwspread_v116_signal,
    f11vr_f11_volatility_regime_shift_volconvex_v117_signal,
    f11vr_f11_volatility_regime_shift_rangeeff_v118_signal,
    f11vr_f11_volatility_regime_shift_volacf_v119_signal,
    f11vr_f11_volatility_regime_shift_bbwmad_v120_signal,
    f11vr_f11_volatility_regime_shift_volbreakaway_v121_signal,
    f11vr_f11_volatility_regime_shift_volceiling_v122_signal,
    f11vr_f11_volatility_regime_shift_pkrvdivz_v123_signal,
    f11vr_f11_volatility_regime_shift_bbwpctmom_v124_signal,
    f11vr_f11_volatility_regime_shift_coilscore_v125_signal,
    f11vr_f11_volatility_regime_shift_volshiftmag_v126_signal,
    f11vr_f11_volatility_regime_shift_bbwaccel_v127_signal,
    f11vr_f11_volatility_regime_shift_regenergy_v128_signal,
    f11vr_f11_volatility_regime_shift_midcross_v129_signal,
    f11vr_f11_volatility_regime_shift_pkstab_v130_signal,
    f11vr_f11_volatility_regime_shift_quiettrend_v131_signal,
    f11vr_f11_volatility_regime_shift_volhalflife_v132_signal,
    f11vr_f11_volatility_regime_shift_atrfloor_v133_signal,
    f11vr_f11_volatility_regime_shift_expconsensus_v134_signal,
    f11vr_f11_volatility_regime_shift_vovmom_v135_signal,
    f11vr_f11_volatility_regime_shift_netregime_v136_signal,
    f11vr_f11_volatility_regime_shift_volregslope_v137_signal,
    f11vr_f11_volatility_regime_shift_bbwdonch_v138_signal,
    f11vr_f11_volatility_regime_shift_downratio_v139_signal,
    f11vr_f11_volatility_regime_shift_bbwjump_v140_signal,
    f11vr_f11_volatility_regime_shift_coiledge_v141_signal,
    f11vr_f11_volatility_regime_shift_bbwconvpct_v142_signal,
    f11vr_f11_volatility_regime_shift_burstiness_v143_signal,
    f11vr_f11_volatility_regime_shift_zmeasurediff_v144_signal,
    f11vr_f11_volatility_regime_shift_deepcompr_v145_signal,
    f11vr_f11_volatility_regime_shift_accelpersist_v146_signal,
    f11vr_f11_volatility_regime_shift_bbwenergy_v147_signal,
    f11vr_f11_volatility_regime_shift_rsregime_v148_signal,
    f11vr_f11_volatility_regime_shift_loadedspring_v149_signal,
    f11vr_f11_volatility_regime_shift_regdispz_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_VOLATILITY_REGIME_SHIFT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f11_volatility_regime_shift_base_076_150_claude: %d features pass" % n_features)
