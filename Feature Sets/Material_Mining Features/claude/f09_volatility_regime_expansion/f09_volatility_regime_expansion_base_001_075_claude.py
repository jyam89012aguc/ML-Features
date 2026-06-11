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
    # log returns — the building block for realized-vol regime work
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f09_rvol(closeadj, w):
    # realized vol = rolling std of log returns
    r = _f09_ret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_bbwidth(closeadj, w):
    # Bollinger bandwidth = (upper-lower)/mid = 4*sigma/mean (price units)
    m = closeadj.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = closeadj.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f09_tr(high, low, closeadj):
    # true range using intraday hi/lo and prior close
    pc = closeadj.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f09_atr(high, low, closeadj, w):
    return _f09_tr(high, low, closeadj).rolling(w, min_periods=max(2, w // 2)).mean()


def _f09_volratio(closeadj, ws, wl):
    # compression->expansion: short vol vs long vol (>1 = expanding)
    return _f09_rvol(closeadj, ws) / _f09_rvol(closeadj, wl).replace(0, np.nan)


def _f09_squeeze_pctl(closeadj, w, lookback):
    # percentile of current bandwidth within its own history (low = squeeze)
    bw = _f09_bbwidth(closeadj, w)
    return bw.rolling(lookback, min_periods=max(5, lookback // 3)).rank(pct=True)


def _f09_contraction_streak(closeadj, w):
    # consecutive-day streak where short bandwidth keeps shrinking
    bw = _f09_bbwidth(closeadj, w)
    shrinking = (bw < bw.shift(1)).astype(float)
    grp = (shrinking == 0).cumsum()
    return shrinking.groupby(grp).cumsum()


# ============================================================
# 21d realized-vol regime z vs its own 252d history (news-driven blowup z)
def f09vr_f09_volatility_regime_expansion_rvolz_21d_base_v001_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = _z(rv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d realized-vol regime z vs its own 504d history
def f09vr_f09_volatility_regime_expansion_rvolz_63d_base_v002_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    b = _z(rv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d realized-vol regime z vs its own 504d history (slow regime)
def f09vr_f09_volatility_regime_expansion_rvolz_126d_base_v003_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    b = _z(rv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression->expansion: 5d vs 63d realized-vol ratio (fast expansion)
def f09vr_f09_volatility_regime_expansion_volratio_5v63_base_v004_signal(closeadj):
    b = _f09_volratio(closeadj, 5, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression->expansion: 21d vs 126d realized-vol ratio
def f09vr_f09_volatility_regime_expansion_volratio_21v126_base_v005_signal(closeadj):
    b = _f09_volratio(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression->expansion: 63d vs 252d realized-vol ratio, rank vs 504d history
def f09vr_f09_volatility_regime_expansion_volratio_63v252_base_v006_signal(closeadj):
    vr = _f09_volratio(closeadj, 63, 252)
    b = vr.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log vol-expansion ratio 5v21 z-scored vs 252d (de-trended expansion impulse)
def f09vr_f09_volatility_regime_expansion_volratioz_5v21_base_v007_signal(closeadj):
    lr = np.log(_f09_volratio(closeadj, 5, 21).replace(0, np.nan))
    b = _z(lr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger bandwidth level 21d (compression/expansion gauge)
def f09vr_f09_volatility_regime_expansion_bbwidth_21d_base_v008_signal(closeadj):
    b = _f09_bbwidth(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger bandwidth level 63d
def f09vr_f09_volatility_regime_expansion_bbwidth_63d_base_v009_signal(closeadj):
    b = _f09_bbwidth(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger bandwidth 126d, z-scored vs its own 504d history
def f09vr_f09_volatility_regime_expansion_bbwidthz_126d_base_v010_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 126)
    b = _z(bw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger squeeze: percentile of 21d bandwidth within 252d (low = squeeze)
def f09vr_f09_volatility_regime_expansion_squeeze_21d_base_v011_signal(closeadj):
    b = _f09_squeeze_pctl(closeadj, 21, 252) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger squeeze: percentile of 63d bandwidth within 504d
def f09vr_f09_volatility_regime_expansion_squeeze_63d_base_v012_signal(closeadj):
    b = _f09_squeeze_pctl(closeadj, 63, 504) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze depth change: how the 252d-median-relative tightness is evolving (delta)
def f09vr_f09_volatility_regime_expansion_squeezedepth_21d_base_v013_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    med = bw.rolling(252, min_periods=63).median()
    depth = (med - bw) / med.replace(0, np.nan)
    b = depth - depth.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 63d std of the 21d realized-vol series (regime instability)
def f09vr_f09_volatility_regime_expansion_volofvol_21in63_base_v014_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol normalized: std(rvol)/mean(rvol) — coefficient of variation of vol
def f09vr_f09_volatility_regime_expansion_volofvolcv_21in126_base_v015_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    sd = rv.rolling(126, min_periods=42).std()
    mn = rv.rolling(126, min_periods=42).mean()
    b = sd / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of the slower 63d rvol over 252d (slow regime turbulence)
def f09vr_f09_volatility_regime_expansion_volofvol_63in252_base_v016_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    b = rv.rolling(252, min_periods=84).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak (21d bandwidth) scaled by current squeeze depth
def f09vr_f09_volatility_regime_expansion_contractstreak_21d_base_v017_signal(closeadj):
    streak = _f09_contraction_streak(closeadj, 21)
    bw = _f09_bbwidth(closeadj, 21)
    med = bw.rolling(252, min_periods=63).median()
    depth = (med - bw) / med.replace(0, np.nan)
    b = streak * (1.0 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak on the 5d bandwidth (fast coil), magnitude-weighted
def f09vr_f09_volatility_regime_expansion_contractstreak_5d_base_v018_signal(closeadj):
    streak = _f09_contraction_streak(closeadj, 5)
    bw = _f09_bbwidth(closeadj, 5)
    shrink_amt = ((bw.shift(1) - bw) / bw.shift(1).replace(0, np.nan)).clip(lower=0)
    cum_shrink = shrink_amt.rolling(10, min_periods=1).sum()
    b = streak + 5.0 * cum_shrink
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze: vol expansion impulse gated by prior squeeze tightness
def f09vr_f09_volatility_regime_expansion_breakfromsqz_21d_base_v019_signal(closeadj):
    sqz_prior = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0).shift(5)
    expand = (_f09_volratio(closeadj, 5, 63) - 1.0).clip(lower=0)
    b = sqz_prior * expand
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze: 63d squeeze release amplitude
def f09vr_f09_volatility_regime_expansion_breakfromsqz_63d_base_v020_signal(closeadj):
    sqz_prior = (0.5 - _f09_squeeze_pctl(closeadj, 63, 504)).clip(lower=0).shift(10)
    expand = (_f09_volratio(closeadj, 21, 126) - 1.0).clip(lower=0)
    b = sqz_prior * expand
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price regime z (intraday range expansion) — short ATR vs 252d history
def f09vr_f09_volatility_regime_expansion_atrpz_21d_base_v021_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    b = _z(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR expansion ratio: 5d ATR vs 63d ATR (intraday compression->expansion)
def f09vr_f09_volatility_regime_expansion_atrratio_5v63_base_v022_signal(closeadj, high, low):
    a_s = _f09_atr(high, low, closeadj, 5)
    a_l = _f09_atr(high, low, closeadj, 63)
    b = a_s / a_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range vs close, regime z over 252d (raw intraday range regime)
def f09vr_f09_volatility_regime_expansion_hlrngz_21d_base_v023_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    smoothed = rng.rolling(21, min_periods=7).mean()
    b = _z(smoothed, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol acceleration: 21d rvol now minus 21d rvol a month ago
def f09vr_f09_volatility_regime_expansion_rvolchg_21d_base_v024_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = rv - rv.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime asymmetry: upside vs downside realized vol (semi-vol spread)
def f09vr_f09_volatility_regime_expansion_semivolspr_63d_base_v025_signal(closeadj):
    r = _f09_ret(closeadj)
    up = r.where(r > 0, 0.0).rolling(63, min_periods=21).std()
    dn = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    b = (dn - up) / (dn + up).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth expansion velocity: 21d bandwidth change over a week
def f09vr_f09_volatility_regime_expansion_bbwvel_21d_base_v026_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    b = (bw - bw.shift(5)) / bw.shift(5).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze persistence: fraction of last quarter spent in bottom-quartile bandwidth
def f09vr_f09_volatility_regime_expansion_sqzpersist_21d_base_v027_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    tight = (pctl <= 0.25).astype(float)
    b = tight.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion persistence: fraction of last quarter in top-quartile bandwidth
def f09vr_f09_volatility_regime_expansion_exppersist_21d_base_v028_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    wide = (pctl >= 0.75).astype(float)
    b = wide.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime transition count: squeeze->expansion crossings over last year
def f09vr_f09_volatility_regime_expansion_transcount_21d_base_v029_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    expand = (_f09_volratio(closeadj, 5, 63) - 1.0).clip(lower=0)
    crossed = ((pctl > 0.75) & (pctl.shift(1) <= 0.75)).astype(float) * (1.0 + expand)
    b = crossed.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol ratio: short vol-of-vol vs long vol-of-vol (turbulence regime)
def f09vr_f09_volatility_regime_expansion_vovratio_base_v030_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov_s = rv.rolling(42, min_periods=14).std()
    vov_l = rv.rolling(252, min_periods=84).std()
    b = vov_s / vov_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol level percentile within 504d (vol-cone-style regime position)
def f09vr_f09_volatility_regime_expansion_rvolpctl_63d_base_v031_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    b = rv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute-return surprise: |today ret| in units of 63d realized vol (shock z)
def f09vr_f09_volatility_regime_expansion_retshock_63d_base_v032_signal(closeadj):
    r = _f09_ret(closeadj)
    rv = _f09_rvol(closeadj, 63)
    shock = r.abs() / rv.replace(0, np.nan)
    b = shock.rolling(21, min_periods=7).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of vol-shock days (|ret|>2.5sigma) over last quarter (news blowups)
def f09vr_f09_volatility_regime_expansion_shockcount_63d_base_v033_signal(closeadj):
    r = _f09_ret(closeadj)
    rv = _f09_rvol(closeadj, 63)
    excess = (r.abs() / rv.replace(0, np.nan) - 2.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth compression ratio: current 21d bandwidth vs its own 126d max (coil)
def f09vr_f09_volatility_regime_expansion_coilratio_21d_base_v034_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    mx = bw.rolling(126, min_periods=42).max()
    b = bw / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth expansion ratio: current 21d bandwidth vs its own 126d min (release)
def f09vr_f09_volatility_regime_expansion_releaseratio_21d_base_v035_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    mn = bw.rolling(126, min_periods=42).min()
    b = bw / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure inversion: which end of 21/63/126 leads (argmax position)
def f09vr_f09_volatility_regime_expansion_voltermlead_base_v036_signal(closeadj):
    v21 = _f09_rvol(closeadj, 21)
    v63 = _f09_rvol(closeadj, 63)
    v126 = _f09_rvol(closeadj, 126)
    stacked = pd.concat([v21, v63, v126], axis=1)
    # signed dominance: short-end excess over the cross-window mean, normalized
    mn = stacked.mean(axis=1)
    rng = stacked.max(axis=1) - stacked.min(axis=1)
    b = (v21 - mn) / rng.replace(0, np.nan) - (v126 - mn) / rng.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol smoothed EMA displacement (vol vs its slow EMA — regime shift)
def f09vr_f09_volatility_regime_expansion_rvoldisp_21d_base_v037_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    b = (rv - rv.ewm(span=63, min_periods=21).mean()) / rv.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-fire signal: low bandwidth percentile times positive return drift
def f09vr_f09_volatility_regime_expansion_sqzfire_21d_base_v038_signal(closeadj):
    sqz = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0)
    drift = _f09_ret(closeadj).rolling(5, min_periods=3).sum().abs()
    b = sqz * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak (ATR-based) on intraday true range
def f09vr_f09_volatility_regime_expansion_atrcontract_21d_base_v039_signal(closeadj, high, low):
    atr = _f09_atr(high, low, closeadj, 21)
    shrinking = (atr < atr.shift(1)).astype(float)
    grp = (shrinking == 0).cumsum()
    streak = shrinking.groupby(grp).cumsum()
    atrp = atr / closeadj.replace(0, np.nan)
    floor126 = atrp.rolling(126, min_periods=42).min()
    depth = (atrp - floor126) / floor126.replace(0, np.nan)
    b = streak * (1.0 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z using ATR/price over a half-year (intraday regime extremity)
def f09vr_f09_volatility_regime_expansion_atrpz_63d_base_v040_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    b = _z(atrp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth dispersion across 21/63/126 windows (multi-scale vol disagreement)
def f09vr_f09_volatility_regime_expansion_bbwdisp_multi_base_v041_signal(closeadj):
    b1 = _f09_bbwidth(closeadj, 21)
    b2 = _f09_bbwidth(closeadj, 63)
    b3 = _f09_bbwidth(closeadj, 126)
    b = pd.concat([b1, b2, b3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion impulse rank: vol ratio 10v126 percentile vs 252d (rank of expansion)
def f09vr_f09_volatility_regime_expansion_exprank_10v126_base_v042_signal(closeadj):
    vr = _f09_volratio(closeadj, 10, 126)
    b = vr.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime momentum: change in 63d rvol z over a quarter
def f09vr_f09_volatility_regime_expansion_rvolzmom_63d_base_v043_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 63), 504)
    b = rvz - rvz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed acceleration of the 21v252 vol ratio (bounded expansion onset)
def f09vr_f09_volatility_regime_expansion_exptanh_21d_base_v044_signal(closeadj):
    lr = np.log(_f09_volratio(closeadj, 21, 252).replace(0, np.nan))
    chg = lr - lr.shift(10)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-vol regime z (semi-deviation of negative returns vs history)
def f09vr_f09_volatility_regime_expansion_downvolz_21d_base_v045_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    b = _z(dn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-style hi/lo vol regime z (range-based vol blowup, 21d)
def f09vr_f09_volatility_regime_expansion_parkz_21d_base_v046_signal(closeadj, high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    park = (hl ** 2).rolling(21, min_periods=7).mean() ** 0.5
    b = _z(park, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-to-squeeze recency: days since last squeeze (bottom-decile bandwidth)
def f09vr_f09_volatility_regime_expansion_dayssincesqz_21d_base_v047_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    tight = (pctl <= 0.10).astype(float)

    def _dsl(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = tight.rolling(252, min_periods=63).apply(_dsl, raw=True) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime breadth: how wide the 21d-vol distribution sits inside its 252d range
def f09vr_f09_volatility_regime_expansion_rvolrangepos_21d_base_v048_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    hi = rv.rolling(252, min_periods=63).max()
    lo = rv.rolling(252, min_periods=63).min()
    b = (rv - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration normalized by vol-of-vol (standardized regime jump)
def f09vr_f09_volatility_regime_expansion_volaccelstd_21d_base_v049_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    chg = rv - rv.shift(10)
    vov = rv.rolling(126, min_periods=42).std()
    b = chg / vov.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze tightness times time-in-squeeze (matured coil ready to fire)
def f09vr_f09_volatility_regime_expansion_maturecoil_21d_base_v050_signal(closeadj):
    sqz = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0)
    streak = _f09_contraction_streak(closeadj, 21)
    b = sqz * streak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol 5d vs 21d ratio, smoothed (very-fast expansion onset)
def f09vr_f09_volatility_regime_expansion_volratio_5v21_base_v051_signal(closeadj):
    vr = _f09_volratio(closeadj, 5, 21)
    b = vr.rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth z minus its lag (acceleration of compression/expansion regime)
def f09vr_f09_volatility_regime_expansion_bbwzaccel_63d_base_v052_signal(closeadj):
    bwz = _z(_f09_bbwidth(closeadj, 63), 504)
    b = bwz - bwz.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter with expanding vol (rvol5 > rvol63) — expansion regime
def f09vr_f09_volatility_regime_expansion_expandfrac_base_v053_signal(closeadj):
    expanding = (_f09_rvol(closeadj, 5) > _f09_rvol(closeadj, 63)).astype(float)
    b = expanding.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vs-close vol divergence z: hi/lo range vol minus close-to-close vol (21d)
def f09vr_f09_volatility_regime_expansion_rangeclosediv_21d_base_v054_signal(closeadj, high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    park = (hl / (4.0 * np.log(2.0))).rolling(21, min_periods=7).mean() ** 0.5
    cc = _f09_rvol(closeadj, 21)
    div = park - cc
    b = _z(div, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z spread: short-window regime z minus long-window regime z
def f09vr_f09_volatility_regime_expansion_regimezspr_base_v055_signal(closeadj):
    z21 = _z(_f09_rvol(closeadj, 21), 252)
    z126 = _z(_f09_rvol(closeadj, 126), 504)
    b = z21 - z126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth squeeze recovery: bandwidth now vs its trailing 63d min (release size)
def f09vr_f09_volatility_regime_expansion_sqzrelease_63d_base_v056_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 63)
    floor63 = bw.rolling(126, min_periods=42).min()
    b = np.log(bw.replace(0, np.nan) / floor63.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol z (turbulence regime z over 252d)
def f09vr_f09_volatility_regime_expansion_vovz_base_v057_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov = rv.rolling(63, min_periods=21).std()
    b = _z(vov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion breakout confirmation: vol ratio expansion times absolute price move
def f09vr_f09_volatility_regime_expansion_breakconfirm_21d_base_v058_signal(closeadj):
    expand = (_f09_volratio(closeadj, 5, 63) - 1.0).clip(lower=0)
    move = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan)).abs()
    b = expand * move
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inside-day contraction: fraction of last month with narrowing daily hi/lo range
def f09vr_f09_volatility_regime_expansion_rngcontractdepth_base_v059_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    inside = (rng < rng.shift(1)).astype(float)
    frac = inside.rolling(21, min_periods=7).mean()
    # weight by how compressed the current daily range is vs its own 63d max
    mx = rng.rolling(63, min_periods=21).max()
    compress = 1.0 - (rng / mx.replace(0, np.nan))
    b = frac * compress
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime cycle position: 126d bandwidth within 1260d high-low band (multi-year)
def f09vr_f09_volatility_regime_expansion_rvolcyclepos_126d_base_v060_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 126)
    hi = bw.rolling(1260, min_periods=252).max()
    lo = bw.rolling(1260, min_periods=252).min()
    pos = (bw - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-vol-high frequency: how often 21d rvol prints a 252d high (blowup recurrence)
def f09vr_f09_volatility_regime_expansion_volhifreq_21d_base_v061_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    hi = rv.rolling(252, min_periods=63).max()
    nearness = (rv / hi.replace(0, np.nan)).clip(upper=1.0)
    is_high = (nearness >= 0.95).astype(float) * nearness
    b = is_high.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-fire asymmetry: expansion impulse signed by subsequent return direction
def f09vr_f09_volatility_regime_expansion_firedirection_21d_base_v062_signal(closeadj):
    expand = (_f09_volratio(closeadj, 5, 63) - 1.0).clip(lower=0)
    direction = np.sign(_f09_ret(closeadj).rolling(5, min_periods=3).sum())
    b = expand * direction
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth half-life proxy: 21d bandwidth vs 63d bandwidth ratio (term structure)
def f09vr_f09_volatility_regime_expansion_bbwterm_21v63_base_v063_signal(closeadj):
    b = _f09_bbwidth(closeadj, 21) / _f09_bbwidth(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-shock recency weighted by magnitude (most recent blowup dominates)
def f09vr_f09_volatility_regime_expansion_shockrecency_63d_base_v064_signal(closeadj):
    r = _f09_ret(closeadj)
    rv = _f09_rvol(closeadj, 63)
    shock = (r.abs() / rv.replace(0, np.nan)).clip(upper=10)
    w = pd.Series(np.linspace(0.2, 1.0, 21), index=range(21))
    b = shock.rolling(21, min_periods=7).apply(
        lambda a: np.average(a, weights=np.linspace(0.2, 1.0, len(a))), raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol curvature: rvol21 - 2*rvol63 + rvol126 (regime convexity)
def f09vr_f09_volatility_regime_expansion_volcurv_base_v065_signal(closeadj):
    b = _f09_rvol(closeadj, 21) - 2.0 * _f09_rvol(closeadj, 63) + _f09_rvol(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression streak normalized by typical streak length (relative coil maturity)
def f09vr_f09_volatility_regime_expansion_streaknorm_21d_base_v066_signal(closeadj):
    streak = _f09_contraction_streak(closeadj, 21)
    typ = streak.rolling(252, min_periods=63).mean()
    b = streak / typ.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime distance from neutral via downside-vol z, signed-sqrt compressed
def f09vr_f09_volatility_regime_expansion_regimedist_63d_base_v067_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    up = r.where(r > 0, 0.0).rolling(63, min_periods=21).std()
    spread = dn - up
    sz = _z(spread, 504)
    b = np.sign(sz) * (sz.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-vs-close vol gap: ATR-based vol minus close-based rvol (overnight gap vol)
def f09vr_f09_volatility_regime_expansion_intravsclose_21d_base_v068_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    rv = _f09_rvol(closeadj, 21)
    b = atrp - rv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-count over a year (number of distinct compression episodes)
def f09vr_f09_volatility_regime_expansion_sqzepisodes_base_v069_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    intight = (pctl <= 0.15).astype(float)
    depth = (0.15 - pctl).clip(lower=0)
    entries = ((intight == 1) & (intight.shift(1) == 0)).astype(float) * (1.0 + 5.0 * depth)
    b = entries.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth expansion velocity z (standardized rate of band widening)
def f09vr_f09_volatility_regime_expansion_bbwvelz_21d_base_v070_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    vel = bw - bw.shift(5)
    b = _z(vel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol mean-reversion gap: rvol vs its 252d mean (over/under-vol regime)
def f09vr_f09_volatility_regime_expansion_rvolmrgap_63d_base_v071_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    mn = rv.rolling(252, min_periods=63).mean()
    b = (rv - mn) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-confirmed-by-range: vol ratio up AND ATR ratio up (joint regime break)
def f09vr_f09_volatility_regime_expansion_jointexpand_base_v072_signal(closeadj, high, low):
    vexp = (_f09_volratio(closeadj, 5, 63) - 1.0)
    aexp = (_f09_atr(high, low, closeadj, 5) / _f09_atr(high, low, closeadj, 63).replace(0, np.nan) - 1.0)
    b = vexp.clip(lower=0) * aexp.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-regime entropy proxy: dispersion of daily |ret| within 21d (clustered shocks)
def f09vr_f09_volatility_regime_expansion_shockcluster_21d_base_v073_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    sd = ar.rolling(21, min_periods=7).std()
    mn = ar.rolling(21, min_periods=7).mean()
    b = sd / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-horizon vol regime drift: 126d rvol log-change over a year
def f09vr_f09_volatility_regime_expansion_volyoy_126d_base_v074_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    b = np.log(rv.replace(0, np.nan) / rv.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression->expansion balance: signed log(rvol5/rvol126) smoothed (regime tilt)
def f09vr_f09_volatility_regime_expansion_cebalance_base_v075_signal(closeadj):
    tilt = np.log(_f09_volratio(closeadj, 5, 126).replace(0, np.nan))
    b = tilt.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vr_f09_volatility_regime_expansion_rvolz_21d_base_v001_signal,
    f09vr_f09_volatility_regime_expansion_rvolz_63d_base_v002_signal,
    f09vr_f09_volatility_regime_expansion_rvolz_126d_base_v003_signal,
    f09vr_f09_volatility_regime_expansion_volratio_5v63_base_v004_signal,
    f09vr_f09_volatility_regime_expansion_volratio_21v126_base_v005_signal,
    f09vr_f09_volatility_regime_expansion_volratio_63v252_base_v006_signal,
    f09vr_f09_volatility_regime_expansion_volratioz_5v21_base_v007_signal,
    f09vr_f09_volatility_regime_expansion_bbwidth_21d_base_v008_signal,
    f09vr_f09_volatility_regime_expansion_bbwidth_63d_base_v009_signal,
    f09vr_f09_volatility_regime_expansion_bbwidthz_126d_base_v010_signal,
    f09vr_f09_volatility_regime_expansion_squeeze_21d_base_v011_signal,
    f09vr_f09_volatility_regime_expansion_squeeze_63d_base_v012_signal,
    f09vr_f09_volatility_regime_expansion_squeezedepth_21d_base_v013_signal,
    f09vr_f09_volatility_regime_expansion_volofvol_21in63_base_v014_signal,
    f09vr_f09_volatility_regime_expansion_volofvolcv_21in126_base_v015_signal,
    f09vr_f09_volatility_regime_expansion_volofvol_63in252_base_v016_signal,
    f09vr_f09_volatility_regime_expansion_contractstreak_21d_base_v017_signal,
    f09vr_f09_volatility_regime_expansion_contractstreak_5d_base_v018_signal,
    f09vr_f09_volatility_regime_expansion_breakfromsqz_21d_base_v019_signal,
    f09vr_f09_volatility_regime_expansion_breakfromsqz_63d_base_v020_signal,
    f09vr_f09_volatility_regime_expansion_atrpz_21d_base_v021_signal,
    f09vr_f09_volatility_regime_expansion_atrratio_5v63_base_v022_signal,
    f09vr_f09_volatility_regime_expansion_hlrngz_21d_base_v023_signal,
    f09vr_f09_volatility_regime_expansion_rvolchg_21d_base_v024_signal,
    f09vr_f09_volatility_regime_expansion_semivolspr_63d_base_v025_signal,
    f09vr_f09_volatility_regime_expansion_bbwvel_21d_base_v026_signal,
    f09vr_f09_volatility_regime_expansion_sqzpersist_21d_base_v027_signal,
    f09vr_f09_volatility_regime_expansion_exppersist_21d_base_v028_signal,
    f09vr_f09_volatility_regime_expansion_transcount_21d_base_v029_signal,
    f09vr_f09_volatility_regime_expansion_vovratio_base_v030_signal,
    f09vr_f09_volatility_regime_expansion_rvolpctl_63d_base_v031_signal,
    f09vr_f09_volatility_regime_expansion_retshock_63d_base_v032_signal,
    f09vr_f09_volatility_regime_expansion_shockcount_63d_base_v033_signal,
    f09vr_f09_volatility_regime_expansion_coilratio_21d_base_v034_signal,
    f09vr_f09_volatility_regime_expansion_releaseratio_21d_base_v035_signal,
    f09vr_f09_volatility_regime_expansion_voltermlead_base_v036_signal,
    f09vr_f09_volatility_regime_expansion_rvoldisp_21d_base_v037_signal,
    f09vr_f09_volatility_regime_expansion_sqzfire_21d_base_v038_signal,
    f09vr_f09_volatility_regime_expansion_atrcontract_21d_base_v039_signal,
    f09vr_f09_volatility_regime_expansion_atrpz_63d_base_v040_signal,
    f09vr_f09_volatility_regime_expansion_bbwdisp_multi_base_v041_signal,
    f09vr_f09_volatility_regime_expansion_exprank_10v126_base_v042_signal,
    f09vr_f09_volatility_regime_expansion_rvolzmom_63d_base_v043_signal,
    f09vr_f09_volatility_regime_expansion_exptanh_21d_base_v044_signal,
    f09vr_f09_volatility_regime_expansion_downvolz_21d_base_v045_signal,
    f09vr_f09_volatility_regime_expansion_parkz_21d_base_v046_signal,
    f09vr_f09_volatility_regime_expansion_dayssincesqz_21d_base_v047_signal,
    f09vr_f09_volatility_regime_expansion_rvolrangepos_21d_base_v048_signal,
    f09vr_f09_volatility_regime_expansion_volaccelstd_21d_base_v049_signal,
    f09vr_f09_volatility_regime_expansion_maturecoil_21d_base_v050_signal,
    f09vr_f09_volatility_regime_expansion_volratio_5v21_base_v051_signal,
    f09vr_f09_volatility_regime_expansion_bbwzaccel_63d_base_v052_signal,
    f09vr_f09_volatility_regime_expansion_expandfrac_base_v053_signal,
    f09vr_f09_volatility_regime_expansion_rangeclosediv_21d_base_v054_signal,
    f09vr_f09_volatility_regime_expansion_regimezspr_base_v055_signal,
    f09vr_f09_volatility_regime_expansion_sqzrelease_63d_base_v056_signal,
    f09vr_f09_volatility_regime_expansion_vovz_base_v057_signal,
    f09vr_f09_volatility_regime_expansion_breakconfirm_21d_base_v058_signal,
    f09vr_f09_volatility_regime_expansion_rngcontractdepth_base_v059_signal,
    f09vr_f09_volatility_regime_expansion_rvolcyclepos_126d_base_v060_signal,
    f09vr_f09_volatility_regime_expansion_volhifreq_21d_base_v061_signal,
    f09vr_f09_volatility_regime_expansion_firedirection_21d_base_v062_signal,
    f09vr_f09_volatility_regime_expansion_bbwterm_21v63_base_v063_signal,
    f09vr_f09_volatility_regime_expansion_shockrecency_63d_base_v064_signal,
    f09vr_f09_volatility_regime_expansion_volcurv_base_v065_signal,
    f09vr_f09_volatility_regime_expansion_streaknorm_21d_base_v066_signal,
    f09vr_f09_volatility_regime_expansion_regimedist_63d_base_v067_signal,
    f09vr_f09_volatility_regime_expansion_intravsclose_21d_base_v068_signal,
    f09vr_f09_volatility_regime_expansion_sqzepisodes_base_v069_signal,
    f09vr_f09_volatility_regime_expansion_bbwvelz_21d_base_v070_signal,
    f09vr_f09_volatility_regime_expansion_rvolmrgap_63d_base_v071_signal,
    f09vr_f09_volatility_regime_expansion_jointexpand_base_v072_signal,
    f09vr_f09_volatility_regime_expansion_shockcluster_21d_base_v073_signal,
    f09vr_f09_volatility_regime_expansion_volyoy_126d_base_v074_signal,
    f09vr_f09_volatility_regime_expansion_cebalance_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_REGIME_EXPANSION_REGISTRY_001_075 = REGISTRY


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

    print("OK f09_volatility_regime_expansion_base_001_075_claude: %d features pass" % n_features)
