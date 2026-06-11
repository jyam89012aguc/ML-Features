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


# ===== folder domain primitives (volatility regime expansion) =====
def _f09_ret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f09_rvol(closeadj, w):
    r = _f09_ret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_bbwidth(closeadj, w):
    m = closeadj.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = closeadj.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f09_tr(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f09_atr(high, low, closeadj, w):
    return _f09_tr(high, low, closeadj).rolling(w, min_periods=max(2, w // 2)).mean()


def _f09_volratio(closeadj, ws, wl):
    return _f09_rvol(closeadj, ws) / _f09_rvol(closeadj, wl).replace(0, np.nan)


def _f09_squeeze_pctl(closeadj, w, lookback):
    bw = _f09_bbwidth(closeadj, w)
    return bw.rolling(lookback, min_periods=max(5, lookback // 3)).rank(pct=True)


def _f09_parkinson(high, low, w):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    return (hl / (4.0 * np.log(2.0))).rolling(w, min_periods=max(2, w // 2)).mean() ** 0.5


def _f09_ewmvol(closeadj, span):
    r = _f09_ret(closeadj)
    return r.ewm(span=span, min_periods=max(2, span // 2)).std()


# ============================================================
# EWMA realized vol regime z (RiskMetrics-style 21d-equivalent span)
def f09vr_f09_volatility_regime_expansion_ewmvolz_21d_base_v076_signal(closeadj):
    ev = _f09_ewmvol(closeadj, 21)
    b = _z(ev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vol vs simple vol divergence (recency-weighted expansion vs flat)
def f09vr_f09_volatility_regime_expansion_ewmsimplediv_21d_base_v077_signal(closeadj):
    ev = _f09_ewmvol(closeadj, 21)
    sv = _f09_rvol(closeadj, 21)
    b = (ev - sv) / sv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast/slow EWMA vol ratio (compression->expansion with exponential memory)
def f09vr_f09_volatility_regime_expansion_ewmvolratio_base_v078_signal(closeadj):
    fast = _f09_ewmvol(closeadj, 10)
    slow = _f09_ewmvol(closeadj, 63)
    b = fast / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze using Keltner-vs-Bollinger relationship (TTM-squeeze proxy)
def f09vr_f09_volatility_regime_expansion_ttmsqueeze_20d_base_v079_signal(closeadj, high, low):
    m = closeadj.rolling(20, min_periods=10).mean()
    bb = 2.0 * closeadj.rolling(20, min_periods=10).std()
    kc = 1.5 * _f09_atr(high, low, closeadj, 20)
    # negative => Bollinger inside Keltner => squeeze on
    b = (bb - kc) / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# TTM-squeeze persistence: fraction of last quarter with squeeze on
def f09vr_f09_volatility_regime_expansion_ttmpersist_20d_base_v080_signal(closeadj, high, low):
    bb = 2.0 * closeadj.rolling(20, min_periods=10).std()
    kc = 1.5 * _f09_atr(high, low, closeadj, 20)
    on = (bb < kc).astype(float)
    frac = on.rolling(63, min_periods=21).mean()
    depth = ((kc - bb) / kc.replace(0, np.nan)).clip(lower=0)
    b = frac + depth.rolling(21, min_periods=7).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol skewness over 63d (asymmetry of the vol distribution)
def f09vr_f09_volatility_regime_expansion_volskew_63d_base_v081_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol kurtosis over 126d (fat-tailed vol-of-vol regime)
def f09vr_f09_volatility_regime_expansion_volkurt_126d_base_v082_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(126, min_periods=42).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return kurtosis 63d (tail-shock regime — discovery gaps fatten tails)
def f09vr_f09_volatility_regime_expansion_retkurt_63d_base_v083_signal(closeadj):
    r = _f09_ret(closeadj)
    b = r.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return skewness 63d (directional shock asymmetry)
def f09vr_f09_volatility_regime_expansion_retskew_63d_base_v084_signal(closeadj):
    r = _f09_ret(closeadj)
    b = r.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth slope normalized (rate of band-width change per day over 21d window)
def f09vr_f09_volatility_regime_expansion_bbwslope_21d_base_v085_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    x = np.arange(21)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _slp(a):
        return float(((np.arange(len(a)) - (len(a) - 1) / 2.0) * (a - a.mean())).sum()
                     / (((np.arange(len(a)) - (len(a) - 1) / 2.0) ** 2).sum()))
    b = bw.rolling(21, min_periods=10).apply(_slp, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol autocorrelation (vol clustering / persistence over 63d)
def f09vr_f09_volatility_regime_expansion_volcluster_63d_base_v086_signal(closeadj):
    ar = _f09_ret(closeadj).abs()

    def _ac1(a):
        a0 = a[:-1]
        a1 = a[1:]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return float(np.corrcoef(a0, a1)[0, 1])
    b = ar.rolling(63, min_periods=30).apply(_ac1, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion thrust: today's true range vs 21d-avg true range
def f09vr_f09_volatility_regime_expansion_trthrust_21d_base_v087_signal(closeadj, high, low):
    tr = _f09_tr(high, low, closeadj)
    atr = tr.rolling(21, min_periods=7).mean()
    thrust = tr / atr.replace(0, np.nan)
    b = thrust.rolling(5, min_periods=3).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized true-range z (intraday shock z vs 252d history)
def f09vr_f09_volatility_regime_expansion_trz_base_v088_signal(closeadj, high, low):
    trp = _f09_tr(high, low, closeadj) / closeadj.replace(0, np.nan)
    b = _z(trp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion start detector: bandwidth crossing above its own 63d median, weighted
def f09vr_f09_volatility_regime_expansion_expstart_21d_base_v089_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    med = bw.rolling(63, min_periods=21).median()
    cross = ((bw > med) & (bw.shift(1) <= med.shift(1))).astype(float)
    amt = ((bw - med) / med.replace(0, np.nan)).clip(lower=0)
    b = (cross * (1.0 + amt)).rolling(21, min_periods=7).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson range vol ratio short/long (intraday compression->expansion)
def f09vr_f09_volatility_regime_expansion_parkratio_5v63_base_v090_signal(closeadj, high, low):
    ps = _f09_parkinson(high, low, 5)
    pl = _f09_parkinson(high, low, 63)
    b = ps / pl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol regime z over 504d (long-horizon range-vol regime)
def f09vr_f09_volatility_regime_expansion_parkz_63d_base_v091_signal(closeadj, high, low):
    pk = _f09_parkinson(high, low, 63)
    b = _z(pk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol slope: change in vol-of-vol over a month (turbulence acceleration)
def f09vr_f09_volatility_regime_expansion_vovslope_base_v092_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov = rv.rolling(63, min_periods=21).std()
    b = vov - vov.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze->expansion lag signal: time since bandwidth was in bottom decile, decayed
def f09vr_f09_volatility_regime_expansion_sqzlagdecay_21d_base_v093_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    tight = (pctl <= 0.10).astype(float)

    def _dsl(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        gap = len(a) - 1 - idx[-1]
        return float(np.exp(-gap / 21.0))
    b = tight.rolling(126, min_periods=42).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z difference vs intraday-range regime z (close vs intraday divergence)
def f09vr_f09_volatility_regime_expansion_closeintradiv_base_v094_signal(closeadj, high, low):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    pkz = _z(_f09_parkinson(high, low, 21), 252)
    b = rvz - pkz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol Sharpe-of-expansion: vol change divided by its noise (clean signal)
def f09vr_f09_volatility_regime_expansion_expsharpe_21d_base_v095_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    chg = rv - rv.shift(21)
    noise = chg.rolling(63, min_periods=21).std()
    b = chg / noise.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth percentile spread: 21d squeeze pctl minus 63d squeeze pctl (scale gap)
def f09vr_f09_volatility_regime_expansion_sqzscalegap_base_v096_signal(closeadj):
    p21 = _f09_squeeze_pctl(closeadj, 21, 252)
    p63 = _f09_squeeze_pctl(closeadj, 63, 252)
    b = p21 - p63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion momentum: 63d rvol log-change over a month (medium-horizon thrust)
def f09vr_f09_volatility_regime_expansion_volmom_63d_base_v097_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    b = np.log(rv.replace(0, np.nan) / rv.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year above the 80th-percentile vol (high-vol regime occupancy)
def f09vr_f09_volatility_regime_expansion_highvolocc_base_v098_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    pctl = rv.rolling(252, min_periods=63).rank(pct=True)
    hi = (pctl >= 0.8).astype(float)
    b = hi.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year below the 20th-percentile vol (low-vol regime occupancy)
def f09vr_f09_volatility_regime_expansion_lowvolocc_base_v099_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    pctl = rv.rolling(252, min_periods=63).rank(pct=True)
    lo = (pctl <= 0.2).astype(float)
    occ = lo.rolling(252, min_periods=63).mean()
    depth = (0.2 - pctl).clip(lower=0).rolling(63, min_periods=21).mean()
    b = occ + 2.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime change-point: abs difference of 21d-vol mean across a split window
def f09vr_f09_volatility_regime_expansion_changepoint_42d_base_v100_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    recent = rv.rolling(21, min_periods=10).mean()
    prior = rv.shift(21).rolling(21, min_periods=10).mean()
    b = (recent - prior) / prior.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-fire breakout strength: post-squeeze price move scaled by ATR
def f09vr_f09_volatility_regime_expansion_firestrength_21d_base_v101_signal(closeadj, high, low):
    sqz_prior = (0.25 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0).shift(3)
    move = (closeadj - closeadj.shift(5)).abs()
    atr = _f09_atr(high, low, closeadj, 21)
    b = sqz_prior * (move / atr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol expansion breadth across scales: count of windows with expanding vol
def f09vr_f09_volatility_regime_expansion_expbreadth_base_v102_signal(closeadj):
    e1 = (_f09_volratio(closeadj, 5, 63) > 1.0).astype(float)
    e2 = (_f09_volratio(closeadj, 10, 126) > 1.0).astype(float)
    e3 = (_f09_volratio(closeadj, 21, 252) > 1.0).astype(float)
    cnt = e1 + e2 + e3
    # weight by average expansion magnitude for continuity
    mag = ((_f09_volratio(closeadj, 5, 63) - 1.0).clip(lower=0)
           + (_f09_volratio(closeadj, 21, 252) - 1.0).clip(lower=0))
    b = cnt + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-vol expansion ratio (5d down-vol vs 63d down-vol)
def f09vr_f09_volatility_regime_expansion_downexpratio_base_v103_signal(closeadj):
    r = _f09_ret(closeadj)
    dn_s = r.where(r < 0, 0.0).rolling(5, min_periods=3).std()
    dn_l = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    b = dn_s / dn_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-vol expansion ratio (discovery rallies — upside vol blowup)
def f09vr_f09_volatility_regime_expansion_upexpratio_base_v104_signal(closeadj):
    r = _f09_ret(closeadj)
    up_s = r.where(r > 0, 0.0).rolling(5, min_periods=3).std()
    up_l = r.where(r > 0, 0.0).rolling(63, min_periods=21).std()
    b = up_s / up_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z curvature: second difference of 21d-vol z (regime acceleration)
def f09vr_f09_volatility_regime_expansion_rvolzcurv_base_v105_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    b = rvz - 2.0 * rvz.shift(10) + rvz.shift(20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth coil-spring: inverse bandwidth times prior contraction streak length
def f09vr_f09_volatility_regime_expansion_coilspring_21d_base_v106_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    shrinking = (bw < bw.shift(1)).astype(float)
    grp = (shrinking == 0).cumsum()
    streak = shrinking.groupby(grp).cumsum()
    inv = 1.0 / bw.replace(0, np.nan)
    invn = inv / inv.rolling(252, min_periods=63).mean().replace(0, np.nan)
    b = invn * (1.0 + streak / 10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol percentile within 1260d (multi-year vol-cone position)
def f09vr_f09_volatility_regime_expansion_volconepos_252d_base_v107_signal(closeadj):
    rv = _f09_rvol(closeadj, 252)
    b = rv.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z over 252d using 5d vol (very-fast shock z)
def f09vr_f09_volatility_regime_expansion_rvolz_5d_base_v108_signal(closeadj):
    rv = _f09_rvol(closeadj, 5)
    b = _z(rv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion onset asymmetry: up-vol-ratio minus down-vol-ratio (rally vs crash vol)
def f09vr_f09_volatility_regime_expansion_updownexpasym_base_v109_signal(closeadj):
    r = _f09_ret(closeadj)
    up_r = (r.where(r > 0, 0.0).rolling(5, min_periods=3).std()
            / r.where(r > 0, 0.0).rolling(63, min_periods=21).std().replace(0, np.nan))
    dn_r = (r.where(r < 0, 0.0).rolling(5, min_periods=3).std()
            / r.where(r < 0, 0.0).rolling(63, min_periods=21).std().replace(0, np.nan))
    b = up_r - dn_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth trend efficiency: net bandwidth change over total path traveled
def f09vr_f09_volatility_regime_expansion_bbweff_63d_base_v110_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    net = (bw - bw.shift(63)).abs()
    path = bw.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol min-over-max within 126d (compression depth indicator)
def f09vr_f09_volatility_regime_expansion_volminmax_126d_base_v111_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    mn = rv.rolling(126, min_periods=42).min()
    mx = rv.rolling(126, min_periods=42).max()
    b = mn / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current vol vs trailing 126d min (how far off the vol floor — release magnitude)
def f09vr_f09_volatility_regime_expansion_volofffloor_base_v112_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    floor126 = rv.rolling(126, min_periods=42).min()
    b = np.log(rv.replace(0, np.nan) / floor126.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current vol vs trailing 126d max (how far below the vol ceiling — room to expand)
def f09vr_f09_volatility_regime_expansion_volunderceil_base_v113_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    ceil126 = rv.rolling(126, min_periods=42).max()
    b = np.log(ceil126.replace(0, np.nan) / rv.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration sign-persistence: streak of rising 21d-vol (sustained expansion)
def f09vr_f09_volatility_regime_expansion_risingvolstreak_base_v114_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    rising = (rv > rv.shift(1)).astype(float)
    grp = (rising == 0).cumsum()
    streak = rising.groupby(grp).cumsum()
    mag = ((rv - rv.shift(1)) / rv.shift(1).replace(0, np.nan)).clip(lower=0)
    b = streak + 10.0 * mag.rolling(5, min_periods=1).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-vol expansion z using high-low range over a quarter window
def f09vr_f09_volatility_regime_expansion_hlexpz_63d_base_v115_signal(closeadj, high, low):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _z(rng, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime breakout confirmation with directional return over 10d
def f09vr_f09_volatility_regime_expansion_dirbreakout_base_v116_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    expand = rvz.clip(lower=0)
    ret10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    b = expand * np.sign(ret10) * ret10.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth quantile range: 75th minus 25th pctile of 21d-bw over 252d (vol dispersion)
def f09vr_f09_volatility_regime_expansion_bbwiqr_base_v117_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    q75 = bw.rolling(252, min_periods=63).quantile(0.75)
    q25 = bw.rolling(252, min_periods=63).quantile(0.25)
    med = bw.rolling(252, min_periods=63).median()
    b = (q75 - q25) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol relative to vol level (normalized turbulence — regime instability)
def f09vr_f09_volatility_regime_expansion_normturbulence_base_v118_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov = rv.rolling(63, min_periods=21).std()
    lvl = rv.rolling(63, min_periods=21).mean()
    b = vov / lvl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol downside contribution ratio (share of vol from down days)
def f09vr_f09_volatility_regime_expansion_downshare_63d_base_v119_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = (r.where(r < 0, 0.0) ** 2).rolling(63, min_periods=21).sum()
    tot = (r ** 2).rolling(63, min_periods=21).sum()
    b = dn / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze maturity: contraction streak times inverse-bandwidth percentile
def f09vr_f09_volatility_regime_expansion_sqzmaturity_base_v120_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    shrinking = (bw < bw.shift(1)).astype(float)
    grp = (shrinking == 0).cumsum()
    streak = shrinking.groupby(grp).cumsum()
    tight = 1.0 - _f09_squeeze_pctl(closeadj, 21, 252)
    b = streak * tight
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime spread: 5d vol z minus 63d vol z (impulse vs base regime)
def f09vr_f09_volatility_regime_expansion_volzspread_5v63_base_v121_signal(closeadj):
    z5 = _z(_f09_rvol(closeadj, 5), 252)
    z63 = _z(_f09_rvol(closeadj, 63), 504)
    b = z5 - z63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion impulse half-life: bandwidth now vs ewm-smoothed bandwidth (overshoot)
def f09vr_f09_volatility_regime_expansion_bbwovershoot_base_v122_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    sm = bw.ewm(span=42, min_periods=14).mean()
    b = (bw - sm) / sm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price ratio momentum: change in ATR% over a quarter (intraday regime drift)
def f09vr_f09_volatility_regime_expansion_atrpmom_63d_base_v123_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    b = atrp - atrp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol vs Parkinson efficiency (gap-vol vs continuous-vol ratio)
def f09vr_f09_volatility_regime_expansion_gapvolratio_base_v124_signal(closeadj, high, low):
    cc = _f09_rvol(closeadj, 21)
    pk = _f09_parkinson(high, low, 21)
    b = cc / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime turning point: sign change in vol-z momentum (peak/trough flag, weighted)
def f09vr_f09_volatility_regime_expansion_volturn_base_v125_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    mom = rvz - rvz.shift(10)
    turn = (np.sign(mom) != np.sign(mom.shift(5))).astype(float)
    b = (turn * rvz.abs()).rolling(21, min_periods=7).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized bandwidth velocity over 63d window (smooth expansion rate)
def f09vr_f09_volatility_regime_expansion_bbwvel_63d_base_v126_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 63)
    b = (bw - bw.shift(21)) / bw.shift(21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze with volume-free price thrust (close-only confirmation)
def f09vr_f09_volatility_regime_expansion_pricethrustsqz_base_v127_signal(closeadj):
    sqz_prior = (0.5 - _f09_squeeze_pctl(closeadj, 63, 504)).clip(lower=0).shift(5)
    thrust = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan)).abs()
    b = sqz_prior * thrust
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol range over total: (max-min)/mean of 21d-vol within 252d (vol amplitude)
def f09vr_f09_volatility_regime_expansion_volamplitude_base_v128_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    mx = rv.rolling(252, min_periods=63).max()
    mn = rv.rolling(252, min_periods=63).min()
    me = rv.rolling(252, min_periods=63).mean()
    b = (mx - mn) / me.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semivol asymmetry change over a quarter (rotation of vol asymmetry regime)
def f09vr_f09_volatility_regime_expansion_semivolchg_base_v129_signal(closeadj):
    r = _f09_ret(closeadj)
    up = r.where(r > 0, 0.0).rolling(63, min_periods=21).std()
    dn = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    asym = (dn - up) / (dn + up).replace(0, np.nan)
    b = asym - asym.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling-window max single-day |ret| in 21d vs 63d-vol (extreme-day prominence)
def f09vr_f09_volatility_regime_expansion_maxdayshock_base_v130_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    mx = ar.rolling(21, min_periods=7).max()
    rv = _f09_rvol(closeadj, 63)
    b = mx / rv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression index: 1 - (21d vol / 252d vol), clipped (pure compression gauge)
def f09vr_f09_volatility_regime_expansion_compressidx_base_v131_signal(closeadj):
    ratio = _f09_volratio(closeadj, 21, 252)
    b = (1.0 - ratio)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime entropy: dispersion of 21d-vol percentiles over 63d (regime churn)
def f09vr_f09_volatility_regime_expansion_regimechurn_base_v132_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    pctl = rv.rolling(252, min_periods=63).rank(pct=True)
    b = pctl.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-confirmed vol expansion ranked vs history (rank of joint break)
def f09vr_f09_volatility_regime_expansion_jointbreakrank_base_v133_signal(closeadj, high, low):
    vexp = (_f09_volratio(closeadj, 5, 63) - 1.0).clip(lower=0)
    aexp = (_f09_atr(high, low, closeadj, 5)
            / _f09_atr(high, low, closeadj, 63).replace(0, np.nan) - 1.0).clip(lower=0)
    joint = vexp * aexp
    b = joint.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d realized vol log-change over half a year (slow-regime drift)
def f09vr_f09_volatility_regime_expansion_slowvoldrift_base_v134_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    b = np.log(rv.replace(0, np.nan) / rv.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze->expansion conversion rate: expansions following squeezes over a year
def f09vr_f09_volatility_regime_expansion_conversionrate_base_v135_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    was_tight = (pctl.shift(10) <= 0.2).astype(float)
    now_wide = (pctl >= 0.6).astype(float)
    conv = (was_tight * now_wide)
    amt = ((pctl - 0.6).clip(lower=0))
    b = (conv * (1.0 + amt)).rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol-of-vol (range-based turbulence over 63d)
def f09vr_f09_volatility_regime_expansion_parkvov_base_v136_signal(closeadj, high, low):
    pk = _f09_parkinson(high, low, 21)
    b = pk.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional vol asymmetry z: (down-vol - up-vol) standardized over 252d
def f09vr_f09_volatility_regime_expansion_asymvolz_base_v137_signal(closeadj):
    r = _f09_ret(closeadj)
    up = r.where(r > 0, 0.0).rolling(21, min_periods=7).std()
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    b = _z(dn - up, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth blowup ranked across multi-year history (rare band-expansion percentile)
def f09vr_f09_volatility_regime_expansion_blowuppctl_base_v138_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    floor = bw.rolling(126, min_periods=42).min()
    release = bw / floor.replace(0, np.nan)
    b = release.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth re-expansion after squeeze: bw delta gated by prior squeeze depth, ranked
def f09vr_f09_volatility_regime_expansion_reexpandrank_base_v139_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    prior_tight = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0).shift(5)
    delta = ((bw - bw.shift(5)) / bw.shift(5).replace(0, np.nan)).clip(lower=0)
    sig = prior_tight * delta
    b = sig.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-vs-vol efficiency regime: directional move per unit of expanding vol
def f09vr_f09_volatility_regime_expansion_trendvolz_base_v140_signal(closeadj):
    trend = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    path = _f09_ret(closeadj).abs().rolling(63, min_periods=21).sum()
    efficiency = trend / path.replace(0, np.nan)
    volexp = (_f09_volratio(closeadj, 21, 126) - 1.0)
    b = efficiency * volexp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-memory vol term-structure curvature: log rvol at 21/126/504 (convexity)
def f09vr_f09_volatility_regime_expansion_voltermcurv_long_base_v141_signal(closeadj):
    l21 = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    l126 = np.log(_f09_rvol(closeadj, 126).replace(0, np.nan))
    l504 = np.log(_f09_rvol(closeadj, 504).replace(0, np.nan))
    b = l21 - 2.0 * l126 + l504
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth acceleration: second difference of 21d bandwidth (coil-to-fire curvature)
def f09vr_f09_volatility_regime_expansion_bbwaccel_base_v142_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    b = bw - 2.0 * bw.shift(5) + bw.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol vs its own 63d EWMA (regime displacement, recency-aware)
def f09vr_f09_volatility_regime_expansion_volewmdisp_63d_base_v143_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    ew = rv.ewm(span=126, min_periods=42).mean()
    b = (rv - ew) / ew.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count-weighted expansion days in last quarter (rvol5 above rvol63 by margin)
def f09vr_f09_volatility_regime_expansion_expdaysmargin_base_v144_signal(closeadj):
    margin = (_f09_volratio(closeadj, 5, 63) - 1.2).clip(lower=0)
    b = margin.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime cycle phase: 63d-vol position in its 1260d range minus 0.5 (multi-year)
def f09vr_f09_volatility_regime_expansion_volcyclephase_base_v145_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    hi = rv.rolling(1260, min_periods=252).max()
    lo = rv.rolling(1260, min_periods=252).min()
    b = (rv - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth minus ATR-band-width divergence (close-band vs range-band squeeze gap)
def f09vr_f09_volatility_regime_expansion_banddiverge_base_v146_signal(closeadj, high, low):
    bb = (4.0 * closeadj.rolling(21, min_periods=10).std()) / closeadj.replace(0, np.nan)
    kb = (2.0 * _f09_atr(high, low, closeadj, 21)) / closeadj.replace(0, np.nan)
    b = (bb - kb)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol shock recency-weighted average over 63d (recent blowups weighted more)
def f09vr_f09_volatility_regime_expansion_shockrecency_base_v147_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    rv = _f09_rvol(closeadj, 126)
    shock = (ar / rv.replace(0, np.nan)).clip(upper=12)
    b = shock.rolling(63, min_periods=21).apply(
        lambda a: np.average(a, weights=np.linspace(0.1, 1.0, len(a))), raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-state dwell time: consecutive days with rvol21 above its 252d median
def f09vr_f09_volatility_regime_expansion_expdwell_base_v148_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    med = rv.rolling(252, min_periods=63).median()
    above = (rv > med).astype(float)
    grp = (above == 0).cumsum()
    streak = above.groupby(grp).cumsum()
    excess = ((rv - med) / med.replace(0, np.nan)).clip(lower=0)
    b = streak * (1.0 + excess)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime mean-reversion pressure: -z weighted by distance (snap-back tendency)
def f09vr_f09_volatility_regime_expansion_volmrpressure_base_v149_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    b = -np.sign(rvz) * (rvz ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite coil-and-fire: prior squeeze depth times current expansion z (regime flip)
def f09vr_f09_volatility_regime_expansion_coilfire_base_v150_signal(closeadj):
    prior_sqz = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0).shift(10)
    exp_z = _z(_f09_rvol(closeadj, 5), 252).clip(lower=0)
    b = prior_sqz * exp_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vr_f09_volatility_regime_expansion_ewmvolz_21d_base_v076_signal,
    f09vr_f09_volatility_regime_expansion_ewmsimplediv_21d_base_v077_signal,
    f09vr_f09_volatility_regime_expansion_ewmvolratio_base_v078_signal,
    f09vr_f09_volatility_regime_expansion_ttmsqueeze_20d_base_v079_signal,
    f09vr_f09_volatility_regime_expansion_ttmpersist_20d_base_v080_signal,
    f09vr_f09_volatility_regime_expansion_volskew_63d_base_v081_signal,
    f09vr_f09_volatility_regime_expansion_volkurt_126d_base_v082_signal,
    f09vr_f09_volatility_regime_expansion_retkurt_63d_base_v083_signal,
    f09vr_f09_volatility_regime_expansion_retskew_63d_base_v084_signal,
    f09vr_f09_volatility_regime_expansion_bbwslope_21d_base_v085_signal,
    f09vr_f09_volatility_regime_expansion_volcluster_63d_base_v086_signal,
    f09vr_f09_volatility_regime_expansion_trthrust_21d_base_v087_signal,
    f09vr_f09_volatility_regime_expansion_trz_base_v088_signal,
    f09vr_f09_volatility_regime_expansion_expstart_21d_base_v089_signal,
    f09vr_f09_volatility_regime_expansion_parkratio_5v63_base_v090_signal,
    f09vr_f09_volatility_regime_expansion_parkz_63d_base_v091_signal,
    f09vr_f09_volatility_regime_expansion_vovslope_base_v092_signal,
    f09vr_f09_volatility_regime_expansion_sqzlagdecay_21d_base_v093_signal,
    f09vr_f09_volatility_regime_expansion_closeintradiv_base_v094_signal,
    f09vr_f09_volatility_regime_expansion_expsharpe_21d_base_v095_signal,
    f09vr_f09_volatility_regime_expansion_sqzscalegap_base_v096_signal,
    f09vr_f09_volatility_regime_expansion_volmom_63d_base_v097_signal,
    f09vr_f09_volatility_regime_expansion_highvolocc_base_v098_signal,
    f09vr_f09_volatility_regime_expansion_lowvolocc_base_v099_signal,
    f09vr_f09_volatility_regime_expansion_changepoint_42d_base_v100_signal,
    f09vr_f09_volatility_regime_expansion_firestrength_21d_base_v101_signal,
    f09vr_f09_volatility_regime_expansion_expbreadth_base_v102_signal,
    f09vr_f09_volatility_regime_expansion_downexpratio_base_v103_signal,
    f09vr_f09_volatility_regime_expansion_upexpratio_base_v104_signal,
    f09vr_f09_volatility_regime_expansion_rvolzcurv_base_v105_signal,
    f09vr_f09_volatility_regime_expansion_coilspring_21d_base_v106_signal,
    f09vr_f09_volatility_regime_expansion_volconepos_252d_base_v107_signal,
    f09vr_f09_volatility_regime_expansion_rvolz_5d_base_v108_signal,
    f09vr_f09_volatility_regime_expansion_updownexpasym_base_v109_signal,
    f09vr_f09_volatility_regime_expansion_bbweff_63d_base_v110_signal,
    f09vr_f09_volatility_regime_expansion_volminmax_126d_base_v111_signal,
    f09vr_f09_volatility_regime_expansion_volofffloor_base_v112_signal,
    f09vr_f09_volatility_regime_expansion_volunderceil_base_v113_signal,
    f09vr_f09_volatility_regime_expansion_risingvolstreak_base_v114_signal,
    f09vr_f09_volatility_regime_expansion_hlexpz_63d_base_v115_signal,
    f09vr_f09_volatility_regime_expansion_dirbreakout_base_v116_signal,
    f09vr_f09_volatility_regime_expansion_bbwiqr_base_v117_signal,
    f09vr_f09_volatility_regime_expansion_normturbulence_base_v118_signal,
    f09vr_f09_volatility_regime_expansion_downshare_63d_base_v119_signal,
    f09vr_f09_volatility_regime_expansion_sqzmaturity_base_v120_signal,
    f09vr_f09_volatility_regime_expansion_volzspread_5v63_base_v121_signal,
    f09vr_f09_volatility_regime_expansion_bbwovershoot_base_v122_signal,
    f09vr_f09_volatility_regime_expansion_atrpmom_63d_base_v123_signal,
    f09vr_f09_volatility_regime_expansion_gapvolratio_base_v124_signal,
    f09vr_f09_volatility_regime_expansion_volturn_base_v125_signal,
    f09vr_f09_volatility_regime_expansion_bbwvel_63d_base_v126_signal,
    f09vr_f09_volatility_regime_expansion_pricethrustsqz_base_v127_signal,
    f09vr_f09_volatility_regime_expansion_volamplitude_base_v128_signal,
    f09vr_f09_volatility_regime_expansion_semivolchg_base_v129_signal,
    f09vr_f09_volatility_regime_expansion_maxdayshock_base_v130_signal,
    f09vr_f09_volatility_regime_expansion_compressidx_base_v131_signal,
    f09vr_f09_volatility_regime_expansion_regimechurn_base_v132_signal,
    f09vr_f09_volatility_regime_expansion_jointbreakrank_base_v133_signal,
    f09vr_f09_volatility_regime_expansion_slowvoldrift_base_v134_signal,
    f09vr_f09_volatility_regime_expansion_conversionrate_base_v135_signal,
    f09vr_f09_volatility_regime_expansion_parkvov_base_v136_signal,
    f09vr_f09_volatility_regime_expansion_asymvolz_base_v137_signal,
    f09vr_f09_volatility_regime_expansion_blowuppctl_base_v138_signal,
    f09vr_f09_volatility_regime_expansion_reexpandrank_base_v139_signal,
    f09vr_f09_volatility_regime_expansion_trendvolz_base_v140_signal,
    f09vr_f09_volatility_regime_expansion_voltermcurv_long_base_v141_signal,
    f09vr_f09_volatility_regime_expansion_bbwaccel_base_v142_signal,
    f09vr_f09_volatility_regime_expansion_volewmdisp_63d_base_v143_signal,
    f09vr_f09_volatility_regime_expansion_expdaysmargin_base_v144_signal,
    f09vr_f09_volatility_regime_expansion_volcyclephase_base_v145_signal,
    f09vr_f09_volatility_regime_expansion_banddiverge_base_v146_signal,
    f09vr_f09_volatility_regime_expansion_shockrecency_base_v147_signal,
    f09vr_f09_volatility_regime_expansion_expdwell_base_v148_signal,
    f09vr_f09_volatility_regime_expansion_volmrpressure_base_v149_signal,
    f09vr_f09_volatility_regime_expansion_coilfire_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_REGIME_EXPANSION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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

    print("OK f09_volatility_regime_expansion_base_076_150_claude: %d features pass" % n_features)
