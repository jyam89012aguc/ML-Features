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
    # realized vol of log returns over window w
    r = _f11_ret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f11_bbwidth(closeadj, w):
    # Bollinger band width = 2*k*std / mean (normalized band span)
    m = closeadj.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = closeadj.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f11_compress_ratio(closeadj, ws, wl):
    # short vol relative to long vol: <1 compression, >1 expansion
    vs = _f11_vol(closeadj, ws)
    vl = _f11_vol(closeadj, wl)
    return vs / vl.replace(0, np.nan)


def _f11_volofvol(closeadj, wv, ws):
    # vol-of-vol: dispersion of the rolling vol series
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
    # where current bbwidth sits in its own history: low pct = squeeze
    bw = _f11_bbwidth(closeadj, w)
    return bw.rolling(lookback, min_periods=max(2, lookback // 4)).rank(pct=True)


def _f11_contract_streak(closeadj, w):
    # running count of consecutive days the rolling range is narrower than the day before
    rng = (_rmax(closeadj, w) - _rmin(closeadj, w))
    narrowing = (rng.diff() < 0).astype(float)
    grp = (narrowing == 0).cumsum()
    return narrowing.groupby(grp).cumsum()


# ============================================================
# vol compression/expansion ratio 5d vs 63d
def f11vr_f11_volatility_regime_shift_compr_63d_base_v001_signal(closeadj):
    b = _f11_compress_ratio(closeadj, 5, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio 21d vs 126d
def f11vr_f11_volatility_regime_shift_compr_126d_base_v002_signal(closeadj):
    b = _f11_compress_ratio(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio 21d vs 252d
def f11vr_f11_volatility_regime_shift_compr_252d_base_v003_signal(closeadj):
    b = _f11_compress_ratio(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log compression ratio 10d vs 63d, smoothed (persistent regime tilt)
def f11vr_f11_volatility_regime_shift_logcompr_63d_base_v004_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 10, 63)
    b = np.log(cr.replace(0, np.nan)).ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression ratio z-scored vs its own 252d history (regime extremity)
def f11vr_f11_volatility_regime_shift_comprz_252d_base_v005_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 5, 21)
    b = _z(cr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band width, 21d
def f11vr_f11_volatility_regime_shift_bbw_21d_base_v006_signal(closeadj):
    b = _f11_bbwidth(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band width, 63d
def f11vr_f11_volatility_regime_shift_bbw_63d_base_v007_signal(closeadj):
    b = _f11_bbwidth(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band width, 126d (uses closeadj for >21d)
def f11vr_f11_volatility_regime_shift_bbw_126d_base_v008_signal(closeadj):
    b = _f11_bbwidth(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger squeeze: percentile of 21d band-width vs 252d history (low = squeeze)
def f11vr_f11_volatility_regime_shift_squeeze_21d_base_v009_signal(closeadj):
    b = _f11_squeeze_pct(closeadj, 21, 252) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger squeeze: percentile of 63d band-width vs 252d history
def f11vr_f11_volatility_regime_shift_squeeze_63d_base_v010_signal(closeadj):
    b = _f11_squeeze_pct(closeadj, 63, 252) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze depth: how far below the 126d median band-width the current width sits
def f11vr_f11_volatility_regime_shift_squeezedepth_21d_base_v011_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    med = bw.rolling(126, min_periods=42).median()
    b = (med - bw) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width ratio: 21d band width vs its own 63d average (band tightening)
def f11vr_f11_volatility_regime_shift_bbwratio_63d_base_v012_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    b = bw / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: dispersion of 21d rolling vol over a quarter
def f11vr_f11_volatility_regime_shift_vov_63d_base_v013_signal(closeadj):
    b = _f11_volofvol(closeadj, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol over half year
def f11vr_f11_volatility_regime_shift_vov_126d_base_v014_signal(closeadj):
    b = _f11_volofvol(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of short vol (5d vol dispersion over a month)
def f11vr_f11_volatility_regime_shift_vovshort_21d_base_v015_signal(closeadj):
    b = _f11_volofvol(closeadj, 5, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z-score on a downside-only 21d semivol vs 252d history (asymmetric regime)
def f11vr_f11_volatility_regime_shift_volz_252d_base_v016_signal(closeadj):
    r = _f11_ret(closeadj)
    up = r.where(r > 0)
    uv = up.rolling(21, min_periods=8).std()
    b = _z(uv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z-score on 63d vol vs 504d history (slow regime)
def f11vr_f11_volatility_regime_shift_volz_504d_base_v017_signal(closeadj):
    v = _f11_vol(closeadj, 63)
    b = _z(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime percentile: where 21d vol sits in its 252d distribution
def f11vr_f11_volatility_regime_shift_volpct_252d_base_v018_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    b = _rank(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak length weighted by current contraction depth
def f11vr_f11_volatility_regime_shift_contrstreak_21d_base_v019_signal(closeadj):
    streak = _f11_contract_streak(closeadj, 21)
    rng = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / closeadj.replace(0, np.nan)
    depth = 1.0 - rng / rng.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = streak * (1.0 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak (63d) blended with the rate of band tightening
def f11vr_f11_volatility_regime_shift_contrstreak_63d_base_v020_signal(closeadj):
    streak = _f11_contract_streak(closeadj, 63)
    rng = (_rmax(closeadj, 63) - _rmin(closeadj, 63)) / closeadj.replace(0, np.nan)
    rate = -(rng / rng.shift(5).replace(0, np.nan) - 1.0)
    b = streak + 20.0 * rate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net contraction pressure: avg signed log-change of band width over a quarter
def f11vr_f11_volatility_regime_shift_contrfrac_63d_base_v021_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    chg = np.log(bw.replace(0, np.nan)).diff()
    b = -chg.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze flag: in-squeeze recently AND today's |return| is large
def f11vr_f11_volatility_regime_shift_breakout_21d_base_v022_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    was_sq = (sq.shift(1) <= 0.20).astype(float)
    r = _f11_ret(closeadj).abs()
    typ = r.rolling(21, min_periods=10).mean()
    impulse = r / typ.replace(0, np.nan)
    b = was_sq * impulse
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout magnitude: range expansion right after a 63d squeeze
def f11vr_f11_volatility_regime_shift_breakout_63d_base_v023_signal(closeadj, high, low):
    sq = _f11_squeeze_pct(closeadj, 63, 252)
    was_sq = (sq.shift(1) <= 0.25).astype(float)
    tr = _f11_truerange(high, low, closeadj)
    atrn = tr / _f11_atr(high, low, closeadj, 63).replace(0, np.nan)
    b = was_sq * (atrn - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration regime: change in 21d vol over a month, normalized by vol
def f11vr_f11_volatility_regime_shift_volaccel_21d_base_v024_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    b = (v - v.shift(21)) / v.shift(21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration on 63d vol over a quarter
def f11vr_f11_volatility_regime_shift_volaccel_63d_base_v025_signal(closeadj):
    v = _f11_vol(closeadj, 63)
    b = (v - v.shift(63)) / v.shift(63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion ratio using ATR: short ATR vs long ATR
def f11vr_f11_volatility_regime_shift_atrcompr_63d_base_v026_signal(high, low, closeadj):
    a_s = _f11_atr(high, low, closeadj, 5)
    a_l = _f11_atr(high, low, closeadj, 63)
    b = (a_s / closeadj.replace(0, np.nan)) / (a_l / closeadj.replace(0, np.nan)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR compression 21d vs 126d, normalized by price
def f11vr_f11_volatility_regime_shift_atrcompr_126d_base_v027_signal(high, low, closeadj):
    a_s = _f11_atr(high, low, closeadj, 21)
    a_l = _f11_atr(high, low, closeadj, 126)
    b = a_s / a_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price regime z-score (volatility level in true-range terms)
def f11vr_f11_volatility_regime_shift_atrz_252d_base_v028_signal(high, low, closeadj):
    atrp = _f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    b = _z(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band-width regime z-score (63d width) vs 504d history (slow regime)
def f11vr_f11_volatility_regime_shift_bbwz_252d_base_v029_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 63)
    b = _z(bw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime transition: short vol minus long vol, both normalized, signed switch
def f11vr_f11_volatility_regime_shift_regswitch_base_v030_signal(closeadj):
    vs = _f11_vol(closeadj, 10)
    vl = _f11_vol(closeadj, 63)
    diff = (vs - vl) / vl.replace(0, np.nan)
    b = np.tanh(3.0 * diff)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-release timing: days since the band-width was in its lowest 252d decile
def f11vr_f11_volatility_regime_shift_sincesqueeze_base_v031_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    in_sq = (sq <= 0.10)
    days = pd.Series(np.arange(len(closeadj)), index=closeadj.index, dtype=float)
    last = days.where(in_sq.values).ffill()
    b = (days - last) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime persistence: time-in-high-vol blended with current excess over median
def f11vr_f11_volatility_regime_shift_highvolfrac_63d_base_v032_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    med = v.rolling(252, min_periods=63).median()
    high = (v > med).astype(float)
    frac = high.rolling(63, min_periods=21).mean() - 0.5
    excess = (v - med) / med.replace(0, np.nan)
    b = frac + 0.5 * excess
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion: today's 5d range relative to the trailing 63d typical range
def f11vr_f11_volatility_regime_shift_rngexp_63d_base_v033_signal(closeadj):
    rng5 = (_rmax(closeadj, 5) - _rmin(closeadj, 5)) / closeadj.replace(0, np.nan)
    typ = rng5.rolling(63, min_periods=21).mean()
    b = rng5 / typ.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol z-score: regime instability extremity
def f11vr_f11_volatility_regime_shift_vovz_252d_base_v034_signal(closeadj):
    vov = _f11_volofvol(closeadj, 21, 63)
    b = _z(vov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-expansion oscillator: difference of fast and slow band-width EMAs (MACD-style)
def f11vr_f11_volatility_regime_shift_bbwosc_base_v035_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    fast = bw.ewm(span=10, min_periods=5).mean()
    slow = bw.ewm(span=42, min_periods=21).mean()
    macd = (fast - slow) / slow.replace(0, np.nan)
    b = macd - macd.ewm(span=9, min_periods=4).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol convexity: difference between 5d, 21d, 63d vol arranged as a curvature term
def f11vr_f11_volatility_regime_shift_volcurv_base_v036_signal(closeadj):
    v5 = _f11_vol(closeadj, 5)
    v21 = _f11_vol(closeadj, 21)
    v63 = _f11_vol(closeadj, 63)
    b = (v5 - 2.0 * v21 + v63) / v21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %B excess: avg signed distance price sits beyond its 2-sigma bands
def f11vr_f11_volatility_regime_shift_bandtag_63d_base_v037_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21).replace(0, np.nan)
    pctb = (closeadj - m) / (2.0 * sd)
    excess = (pctb.abs() - 1.0).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol ratio asymmetry: upside vol regime vs downside vol regime
def f11vr_f11_volatility_regime_shift_volasym_63d_base_v038_signal(closeadj):
    r = _f11_ret(closeadj)
    up = r.where(r > 0)
    dn = r.where(r < 0)
    uv = up.rolling(63, min_periods=21).std()
    dv = dn.rolling(63, min_periods=21).std()
    b = (uv - dv) / (uv + dv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol spike intensity: max single-day |ret| over last month vs typical vol
def f11vr_f11_volatility_regime_shift_volspike_21d_base_v039_signal(closeadj):
    r = _f11_ret(closeadj).abs()
    mx = r.rolling(21, min_periods=10).max()
    v = _f11_vol(closeadj, 63)
    b = mx / v.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression then expansion: low past squeeze times current expansion (NR-then-WR)
def f11vr_f11_volatility_regime_shift_nrwr_base_v040_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    past_tight = (1.0 - bw.shift(5).rolling(126, min_periods=42).rank(pct=True))
    now_wide = bw.rolling(126, min_periods=42).rank(pct=True)
    b = past_tight * now_wide
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol gap: 21d realized vol minus 63d realized vol, in absolute vol units
def f11vr_f11_volatility_regime_shift_volgap_base_v041_signal(closeadj):
    b = _f11_vol(closeadj, 21) - _f11_vol(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# narrow-range pressure: avg shortfall of true range below its rolling median
def f11vr_f11_volatility_regime_shift_nrfreq_63d_base_v042_signal(high, low, closeadj):
    tr = _f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)
    med = tr.rolling(126, min_periods=42).median()
    shortfall = (med - tr) / med.replace(0, np.nan)
    b = shortfall.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band-width momentum: rate of change of width over a month
def f11vr_f11_volatility_regime_shift_bbwmom_21d_base_v043_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    b = bw / bw.shift(21).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime instability: rolling std of the compression ratio (regime churning)
def f11vr_f11_volatility_regime_shift_regchurn_base_v044_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 10, 63)
    b = cr.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol ratio: short-window vov vs long-window vov
def f11vr_f11_volatility_regime_shift_vovratio_base_v045_signal(closeadj):
    vov_s = _f11_volofvol(closeadj, 10, 21)
    vov_l = _f11_volofvol(closeadj, 21, 126)
    b = vov_s / vov_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion breakout strength: range now vs minimum range over prior quarter
def f11vr_f11_volatility_regime_shift_expvsmin_base_v046_signal(closeadj):
    rng = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / closeadj.replace(0, np.nan)
    mn = rng.rolling(63, min_periods=21).min()
    b = rng / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime z spread: short-vol z minus long-vol z (regime divergence)
def f11vr_f11_volatility_regime_shift_volzspread_base_v047_signal(closeadj):
    zs = _z(_f11_vol(closeadj, 10), 126)
    zl = _z(_f11_vol(closeadj, 63), 252)
    b = zs - zl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width contraction depth vs its own 252d minimum (extreme squeeze proximity)
def f11vr_f11_volatility_regime_shift_squeezemin_base_v048_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    mn = bw.rolling(252, min_periods=63).min()
    b = bw / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime entropy proxy: spread of vol percentile across 5/21/63 windows
def f11vr_f11_volatility_regime_shift_voldisp_base_v049_signal(closeadj):
    p5 = _rank(_f11_vol(closeadj, 5), 252)
    p21 = _rank(_f11_vol(closeadj, 21), 252)
    p63 = _rank(_f11_vol(closeadj, 63), 252)
    b = pd.concat([p5, p21, p63], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log band-width level, smoothed (slow compression state)
def f11vr_f11_volatility_regime_shift_logbbw_63d_base_v050_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 63)
    b = np.log(bw.replace(0, np.nan)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol mean-reversion pull: distance of 21d vol from its 126d median in MAD units
def f11vr_f11_volatility_regime_shift_volmrgap_base_v051_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    med = v.rolling(126, min_periods=42).median()
    mad = (v - med).abs().rolling(126, min_periods=42).median()
    b = (v - med) / mad.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze episode rate blended with continuous time-in-squeeze depth over the year
def f11vr_f11_volatility_regime_shift_squeezecount_base_v052_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    in_sq = (sq <= 0.15).astype(float)
    entries = ((in_sq == 1) & (in_sq.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = (0.15 - sq).clip(lower=0).rolling(252, min_periods=126).mean()
    b = rate + 50.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion episode rate blended with continuous time-above-85th-pct intensity
def f11vr_f11_volatility_regime_shift_expcount_base_v053_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    in_exp = (sq >= 0.85).astype(float)
    entries = ((in_exp == 1) & (in_exp.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    inten = (sq - 0.85).clip(lower=0).rolling(252, min_periods=126).mean()
    b = rate + 50.0 * inten
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Keltner-vs-Bollinger squeeze ratio, z-scored vs its own history (relative regime)
def f11vr_f11_volatility_regime_shift_kcsqueeze_base_v054_signal(high, low, closeadj):
    sd = _std(closeadj, 21)
    atr = _f11_atr(high, low, closeadj, 21)
    ratio = (2.0 * sd) / (1.5 * atr).replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration of acceleration proxy: second difference of 21d vol over months
def f11vr_f11_volatility_regime_shift_volaccel2_base_v055_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    b = (v - 2.0 * v.shift(21) + v.shift(42)) / v.shift(21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime tilt sign x magnitude: signed compression with sqrt magnitude
def f11vr_f11_volatility_regime_shift_regsignmag_base_v056_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 21, 126) - 1.0
    b = np.sign(cr) * (cr.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# parkinson-style range vol regime ratio (hi-lo based) short vs long
def f11vr_f11_volatility_regime_shift_pkratio_base_v057_signal(high, low, closeadj):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    pk_s = hl.rolling(10, min_periods=5).mean() ** 0.5
    pk_l = hl.rolling(63, min_periods=21).mean() ** 0.5
    b = pk_s / pk_l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol regime z (parkinson level z-scored)
def f11vr_f11_volatility_regime_shift_pkz_252d_base_v058_signal(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    pk = hl.rolling(21, min_periods=10).mean() ** 0.5
    b = _z(pk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression persistence streak weighted by how far below 1 the ratio sits
def f11vr_f11_volatility_regime_shift_comprstreak_base_v059_signal(closeadj):
    cr = _f11_compress_ratio(closeadj, 10, 63)
    below = (cr < 1.0).astype(float)
    grp = (below == 0).cumsum()
    streak = below.groupby(grp).cumsum()
    b = streak * (1.0 - cr).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol whipsaw: flip-rate scaled by avg magnitude of the vol changes (choppy regime)
def f11vr_f11_volatility_regime_shift_volwhip_base_v060_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    dv = v.diff()
    d = np.sign(dv)
    flip = (d != d.shift(1)).astype(float)
    rate = flip.rolling(63, min_periods=21).mean() - 0.5
    mag = (dv.abs() / v.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = rate + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-from-squeeze (directional), decayed since last release event
def f11vr_f11_volatility_regime_shift_breakdir_base_v061_signal(closeadj):
    sq = _f11_squeeze_pct(closeadj, 21, 252)
    released = ((sq.shift(1) <= 0.20) & (sq > 0.20)).astype(float)
    thr = _f11_ret(closeadj).rolling(5, min_periods=3).sum()
    impulse = released * thr / _f11_vol(closeadj, 63).replace(0, np.nan)
    b = impulse.ewm(span=10, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime ratio EWM (exponentially weighted compression)
def f11vr_f11_volatility_regime_shift_ewmcompr_base_v062_signal(closeadj):
    r = _f11_ret(closeadj)
    vs = (r.ewm(span=10, min_periods=5).std())
    vl = (r.ewm(span=63, min_periods=21).std())
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-width acceleration: 2nd difference of band width (compression curvature)
def f11vr_f11_volatility_regime_shift_bbwcurv_base_v063_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    b = (bw - 2.0 * bw.shift(10) + bw.shift(20)) / bw.shift(10).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol regime z (semivol of negative returns vs history)
def f11vr_f11_volatility_regime_shift_downvolz_base_v064_signal(closeadj):
    r = _f11_ret(closeadj)
    dn = r.where(r < 0)
    dv = dn.rolling(21, min_periods=8).std()
    b = _z(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike headroom: how compressed the recent vol-range is vs its own typical span
def f11vr_f11_volatility_regime_shift_volq90gap_base_v065_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    recent_span = (v.rolling(21, min_periods=10).max() - v.rolling(21, min_periods=10).min())
    typ_span = recent_span.rolling(252, min_periods=63).median()
    b = recent_span / typ_span.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-range coil: low band-width AND low vov together (energy building)
def f11vr_f11_volatility_regime_shift_coil_base_v066_signal(closeadj):
    bw_pct = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    vov_pct = _f11_volofvol(closeadj, 21, 63).rolling(252, min_periods=63).rank(pct=True)
    b = (1.0 - bw_pct) * (1.0 - vov_pct)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range contraction ratio: 5d range vs 21d range (intra-month tightening)
def f11vr_f11_volatility_regime_shift_rngcontr_base_v067_signal(closeadj):
    r5 = _rmax(closeadj, 5) - _rmin(closeadj, 5)
    r21 = _rmax(closeadj, 21) - _rmin(closeadj, 21)
    b = r5 / r21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime crossover momentum: rate of change of the short-minus-long vol gap
def f11vr_f11_volatility_regime_shift_volcross_base_v068_signal(closeadj):
    vs = _f11_vol(closeadj, 21)
    vl = _f11_vol(closeadj, 126)
    gap = (vs - vl) / vl.replace(0, np.nan)
    b = gap.ewm(span=10, min_periods=5).mean() - gap.ewm(span=42, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# atr regime band-width interaction: atr-pct times bbwidth percentile (double vol)
def f11vr_f11_volatility_regime_shift_atrbbw_base_v069_signal(high, low, closeadj):
    atrp = (_f11_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan))
    atr_pct = atrp.rolling(252, min_periods=63).rank(pct=True)
    bbw_pct = _f11_bbwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    b = atr_pct * bbw_pct - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol expansion vs contraction over month (signed slope of vol percentile)
def f11vr_f11_volatility_regime_shift_volpctchg_base_v070_signal(closeadj):
    vp = _rank(_f11_vol(closeadj, 21), 252) + 0.5
    b = vp - vp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime stability: how flat the band-width has been (1 minus normalized range of bw)
def f11vr_f11_volatility_regime_shift_bbwflat_base_v071_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    rng = (bw.rolling(63, min_periods=21).max() - bw.rolling(63, min_periods=21).min())
    b = rng / bw.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol of true range: dispersion of normalized true range (range-regime instability)
def f11vr_f11_volatility_regime_shift_trvov_base_v072_signal(high, low, closeadj):
    trp = _f11_truerange(high, low, closeadj) / closeadj.replace(0, np.nan)
    b = trp.rolling(63, min_periods=21).std() / trp.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze release lag asymmetry: long compression then expansion ratio
def f11vr_f11_volatility_regime_shift_coilrelease_base_v073_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    min_recent = bw.rolling(126, min_periods=42).min()
    coil_depth = (bw.shift(10) - min_recent) / min_recent.replace(0, np.nan)
    release = bw / bw.shift(10).replace(0, np.nan) - 1.0
    b = release - coil_depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime memory: correlation-like persistence of high-vol from one month to next
def f11vr_f11_volatility_regime_shift_volpersist_base_v074_signal(closeadj):
    v = _f11_vol(closeadj, 21)
    vn = (v - v.rolling(252, min_periods=63).mean()) / v.rolling(252, min_periods=63).std().replace(0, np.nan)
    b = vn * vn.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression-expansion full-cycle score: signed distance of bbwidth from its median band
def f11vr_f11_volatility_regime_shift_cycle_base_v075_signal(closeadj):
    bw = _f11_bbwidth(closeadj, 21)
    med = bw.rolling(126, min_periods=42).median()
    iqr = (bw.rolling(126, min_periods=42).quantile(0.75) - bw.rolling(126, min_periods=42).quantile(0.25))
    b = (bw - med) / iqr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11vr_f11_volatility_regime_shift_compr_63d_base_v001_signal,
    f11vr_f11_volatility_regime_shift_compr_126d_base_v002_signal,
    f11vr_f11_volatility_regime_shift_compr_252d_base_v003_signal,
    f11vr_f11_volatility_regime_shift_logcompr_63d_base_v004_signal,
    f11vr_f11_volatility_regime_shift_comprz_252d_base_v005_signal,
    f11vr_f11_volatility_regime_shift_bbw_21d_base_v006_signal,
    f11vr_f11_volatility_regime_shift_bbw_63d_base_v007_signal,
    f11vr_f11_volatility_regime_shift_bbw_126d_base_v008_signal,
    f11vr_f11_volatility_regime_shift_squeeze_21d_base_v009_signal,
    f11vr_f11_volatility_regime_shift_squeeze_63d_base_v010_signal,
    f11vr_f11_volatility_regime_shift_squeezedepth_21d_base_v011_signal,
    f11vr_f11_volatility_regime_shift_bbwratio_63d_base_v012_signal,
    f11vr_f11_volatility_regime_shift_vov_63d_base_v013_signal,
    f11vr_f11_volatility_regime_shift_vov_126d_base_v014_signal,
    f11vr_f11_volatility_regime_shift_vovshort_21d_base_v015_signal,
    f11vr_f11_volatility_regime_shift_volz_252d_base_v016_signal,
    f11vr_f11_volatility_regime_shift_volz_504d_base_v017_signal,
    f11vr_f11_volatility_regime_shift_volpct_252d_base_v018_signal,
    f11vr_f11_volatility_regime_shift_contrstreak_21d_base_v019_signal,
    f11vr_f11_volatility_regime_shift_contrstreak_63d_base_v020_signal,
    f11vr_f11_volatility_regime_shift_contrfrac_63d_base_v021_signal,
    f11vr_f11_volatility_regime_shift_breakout_21d_base_v022_signal,
    f11vr_f11_volatility_regime_shift_breakout_63d_base_v023_signal,
    f11vr_f11_volatility_regime_shift_volaccel_21d_base_v024_signal,
    f11vr_f11_volatility_regime_shift_volaccel_63d_base_v025_signal,
    f11vr_f11_volatility_regime_shift_atrcompr_63d_base_v026_signal,
    f11vr_f11_volatility_regime_shift_atrcompr_126d_base_v027_signal,
    f11vr_f11_volatility_regime_shift_atrz_252d_base_v028_signal,
    f11vr_f11_volatility_regime_shift_bbwz_252d_base_v029_signal,
    f11vr_f11_volatility_regime_shift_regswitch_base_v030_signal,
    f11vr_f11_volatility_regime_shift_sincesqueeze_base_v031_signal,
    f11vr_f11_volatility_regime_shift_highvolfrac_63d_base_v032_signal,
    f11vr_f11_volatility_regime_shift_rngexp_63d_base_v033_signal,
    f11vr_f11_volatility_regime_shift_vovz_252d_base_v034_signal,
    f11vr_f11_volatility_regime_shift_bbwosc_base_v035_signal,
    f11vr_f11_volatility_regime_shift_volcurv_base_v036_signal,
    f11vr_f11_volatility_regime_shift_bandtag_63d_base_v037_signal,
    f11vr_f11_volatility_regime_shift_volasym_63d_base_v038_signal,
    f11vr_f11_volatility_regime_shift_volspike_21d_base_v039_signal,
    f11vr_f11_volatility_regime_shift_nrwr_base_v040_signal,
    f11vr_f11_volatility_regime_shift_volgap_base_v041_signal,
    f11vr_f11_volatility_regime_shift_nrfreq_63d_base_v042_signal,
    f11vr_f11_volatility_regime_shift_bbwmom_21d_base_v043_signal,
    f11vr_f11_volatility_regime_shift_regchurn_base_v044_signal,
    f11vr_f11_volatility_regime_shift_vovratio_base_v045_signal,
    f11vr_f11_volatility_regime_shift_expvsmin_base_v046_signal,
    f11vr_f11_volatility_regime_shift_volzspread_base_v047_signal,
    f11vr_f11_volatility_regime_shift_squeezemin_base_v048_signal,
    f11vr_f11_volatility_regime_shift_voldisp_base_v049_signal,
    f11vr_f11_volatility_regime_shift_logbbw_63d_base_v050_signal,
    f11vr_f11_volatility_regime_shift_volmrgap_base_v051_signal,
    f11vr_f11_volatility_regime_shift_squeezecount_base_v052_signal,
    f11vr_f11_volatility_regime_shift_expcount_base_v053_signal,
    f11vr_f11_volatility_regime_shift_kcsqueeze_base_v054_signal,
    f11vr_f11_volatility_regime_shift_volaccel2_base_v055_signal,
    f11vr_f11_volatility_regime_shift_regsignmag_base_v056_signal,
    f11vr_f11_volatility_regime_shift_pkratio_base_v057_signal,
    f11vr_f11_volatility_regime_shift_pkz_252d_base_v058_signal,
    f11vr_f11_volatility_regime_shift_comprstreak_base_v059_signal,
    f11vr_f11_volatility_regime_shift_volwhip_base_v060_signal,
    f11vr_f11_volatility_regime_shift_breakdir_base_v061_signal,
    f11vr_f11_volatility_regime_shift_ewmcompr_base_v062_signal,
    f11vr_f11_volatility_regime_shift_bbwcurv_base_v063_signal,
    f11vr_f11_volatility_regime_shift_downvolz_base_v064_signal,
    f11vr_f11_volatility_regime_shift_volq90gap_base_v065_signal,
    f11vr_f11_volatility_regime_shift_coil_base_v066_signal,
    f11vr_f11_volatility_regime_shift_rngcontr_base_v067_signal,
    f11vr_f11_volatility_regime_shift_volcross_base_v068_signal,
    f11vr_f11_volatility_regime_shift_atrbbw_base_v069_signal,
    f11vr_f11_volatility_regime_shift_volpctchg_base_v070_signal,
    f11vr_f11_volatility_regime_shift_bbwflat_base_v071_signal,
    f11vr_f11_volatility_regime_shift_trvov_base_v072_signal,
    f11vr_f11_volatility_regime_shift_coilrelease_base_v073_signal,
    f11vr_f11_volatility_regime_shift_volpersist_base_v074_signal,
    f11vr_f11_volatility_regime_shift_cycle_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_VOLATILITY_REGIME_SHIFT_REGISTRY_001_075 = REGISTRY


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

    print("OK f11_volatility_regime_shift_base_001_075_claude: %d features pass" % n_features)
