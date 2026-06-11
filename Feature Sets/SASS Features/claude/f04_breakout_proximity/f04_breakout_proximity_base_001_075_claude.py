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


# ===== folder domain primitives (BREAKOUT PROXIMITY) =====
# Donchian channel position: where price sits inside the rolling [low_w, high_w] channel.
def _donch_pos(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


# Donchian position using true intraday extremes (high/low channel).
def _donch_pos_hl(close, high, low, w):
    hi = high.rolling(w, min_periods=max(1, w // 2)).max()
    lo = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


# Distance to the N-day high as a log gap (<=0; 0 == at the high).
def _dist_high(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


# Distance above the N-day low as a log gap (>=0; 0 == at the low).
def _dist_low(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(close.replace(0, np.nan) / lo.replace(0, np.nan))


# Headroom to prior breakout level (channel uses data strictly before today).
def _headroom_high(close, w):
    prior_hi = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return close / prior_hi.replace(0, np.nan) - 1.0


# Cushion above prior breakdown level.
def _cushion_low(close, w):
    prior_lo = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return close / prior_lo.replace(0, np.nan) - 1.0


# Days since the N-day high, normalized to [0,1] (staleness of breakout).
def _days_since_high(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


# Days since the N-day low, normalized to [0,1].
def _days_since_low(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


# New-high frequency: fraction of the lookback dw spent making fresh w-day highs.
def _newhigh_freq(close, w, dw):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    is_hi = (close >= hi * 0.99999).astype(float)
    return is_hi.rolling(dw, min_periods=max(1, dw // 2)).mean()


# New-low frequency over the lookback dw.
def _newlow_freq(close, w, dw):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    is_lo = (close <= lo * 1.00001).astype(float)
    return is_lo.rolling(dw, min_periods=max(1, dw // 2)).mean()


# Channel width (Donchian band amplitude) normalized by price -- the "squeeze" gauge.
def _chan_width(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / close.replace(0, np.nan)


# Squeeze ratio: current channel width vs its own typical width (compression < 1).
def _squeeze_ratio(close, w, lw):
    cw = _chan_width(close, w)
    return cw / cw.rolling(lw, min_periods=max(1, lw // 2)).mean().replace(0, np.nan)


# Channel midline skew: signed gap of price above/below the channel midpoint,
# normalized by PRICE (not by range) so it is a distinct nonlinear function of the
# channel rather than an affine shift of the range-position.
def _mid_skew(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    mid = (hi + lo) / 2.0
    return (close - mid) / close.replace(0, np.nan)


# Channel-high climb rate: how fast the rolling-max ceiling is being lifted.
def _high_climb(close, w, k):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(hi.replace(0, np.nan) / hi.shift(k).replace(0, np.nan))


# Channel-low lift rate: how fast the rolling-min floor is rising.
def _low_lift(close, w, k):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(lo.replace(0, np.nan) / lo.shift(k).replace(0, np.nan))



# Donchian channel position over 63d
def f04bp_f04_breakout_proximity_donchpos_63d_base_v001_signal(closeadj):
    result = _donch_pos(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 126d
def f04bp_f04_breakout_proximity_donchpos_126d_base_v002_signal(closeadj):
    result = _donch_pos(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 252d
def f04bp_f04_breakout_proximity_donchpos_252d_base_v003_signal(closeadj):
    result = _donch_pos(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position 252d, z-scored vs own 126d history
def f04bp_f04_breakout_proximity_donchposz_252d_base_v004_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    result = _z(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position 504d, percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_donchposrk_504d_base_v005_signal(closeadj):
    p = _donch_pos(closeadj, 504)
    result = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position spread: short 63d channel minus long 252d channel
def f04bp_f04_breakout_proximity_donchposspr_63d_base_v006_signal(closeadj):
    s = _donch_pos(closeadj, 63)
    l = _donch_pos(closeadj, 252)
    result = s - l
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position momentum: 252d channel position change over a quarter
def f04bp_f04_breakout_proximity_donchposmom_252d_base_v007_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    result = p - p.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position smoothed (persistent channel placement), 126d
def f04bp_f04_breakout_proximity_donchposema_126d_base_v008_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    result = p.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position displacement from its own slow EMA, 252d
def f04bp_f04_breakout_proximity_donchposdisp_252d_base_v009_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    result = p - p.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position in the true high/low channel, 63d, z vs 126d
def f04bp_f04_breakout_proximity_hldonchz_63d_base_v010_signal(closeadj, high, low):
    p = _donch_pos_hl(closeadj, high, low, 63)
    result = _z(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# True high/low channel position 252d, percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_hldonchrk_252d_base_v011_signal(closeadj, high, low):
    p = _donch_pos_hl(closeadj, high, low, 252)
    result = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# True-channel vs close-channel position gap (intraday breakout premium), 126d
def f04bp_f04_breakout_proximity_hlclosegap_126d_base_v012_signal(closeadj, high, low):
    ph = _donch_pos_hl(closeadj, high, low, 126)
    pc = _donch_pos(closeadj, 126)
    result = ph - pc
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 63d high (log gap to ceiling)
def f04bp_f04_breakout_proximity_disthi_63d_base_v013_signal(closeadj):
    result = _dist_high(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 126d high
def f04bp_f04_breakout_proximity_disthi_126d_base_v014_signal(closeadj):
    result = _dist_high(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 252d high
def f04bp_f04_breakout_proximity_disthi_252d_base_v015_signal(closeadj):
    result = _dist_high(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 252d high, z-scored vs own 252d history
def f04bp_f04_breakout_proximity_disthiz_252d_base_v016_signal(closeadj):
    g = _dist_high(closeadj, 252)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 504d high, mean-reverting vs own 126d average
def f04bp_f04_breakout_proximity_disthimr_504d_base_v017_signal(closeadj):
    g = _dist_high(closeadj, 504)
    result = g - g.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-252d-high momentum (approach speed over a month)
def f04bp_f04_breakout_proximity_disthimom_252d_base_v018_signal(closeadj):
    g = _dist_high(closeadj, 252)
    result = g - g.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 63d low (log cushion off floor)
def f04bp_f04_breakout_proximity_distlo_63d_base_v019_signal(closeadj):
    result = _dist_low(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 126d low
def f04bp_f04_breakout_proximity_distlo_126d_base_v020_signal(closeadj):
    result = _dist_low(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 252d low
def f04bp_f04_breakout_proximity_distlo_252d_base_v021_signal(closeadj):
    result = _dist_low(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 252d low, z-scored vs own 252d history
def f04bp_f04_breakout_proximity_distloz_252d_base_v022_signal(closeadj):
    g = _dist_low(closeadj, 252)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 504d low, percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_distlork_504d_base_v023_signal(closeadj):
    g = _dist_low(closeadj, 504)
    result = g.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-63d-high relative to its own 63d typical gap (closeness vs usual)
def f04bp_f04_breakout_proximity_headroom_63d_base_v024_signal(closeadj):
    g = _dist_high(closeadj, 63)
    typ = g.rolling(63, min_periods=21).mean()
    result = g / typ.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-252d-high relative to its own 126d typical gap, smoothed
def f04bp_f04_breakout_proximity_headroomz_252d_base_v025_signal(closeadj):
    g = _dist_high(closeadj, 252)
    typ = g.rolling(126, min_periods=63).mean()
    r = g / typ.replace(0, np.nan) - 1.0
    result = r.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-above-63d-low relative to its own 63d typical cushion (closeness vs usual)
def f04bp_f04_breakout_proximity_cushion_63d_base_v026_signal(closeadj):
    g = _dist_low(closeadj, 63)
    typ = g.rolling(63, min_periods=21).mean()
    result = g / typ.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-above-252d-low relative to its own 126d typical cushion, smoothed
def f04bp_f04_breakout_proximity_cushionz_252d_base_v027_signal(closeadj):
    g = _dist_low(closeadj, 252)
    typ = g.rolling(126, min_periods=63).mean()
    r = g / typ.replace(0, np.nan) - 1.0
    result = r.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Breakout asymmetry: headroom-above-high minus cushion-above-low at 126d
def f04bp_f04_breakout_proximity_brkasym_126d_base_v028_signal(closeadj):
    h = _headroom_high(closeadj, 126)
    c = _cushion_low(closeadj, 126)
    result = h - c
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 63d high (breakout staleness)
def f04bp_f04_breakout_proximity_dsh_63d_base_v029_signal(closeadj):
    result = _days_since_high(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 126d high
def f04bp_f04_breakout_proximity_dsh_126d_base_v030_signal(closeadj):
    result = _days_since_high(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 252d high
def f04bp_f04_breakout_proximity_dsh_252d_base_v031_signal(closeadj):
    result = _days_since_high(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 63d low
def f04bp_f04_breakout_proximity_dsl_63d_base_v032_signal(closeadj):
    result = _days_since_low(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 252d low
def f04bp_f04_breakout_proximity_dsl_252d_base_v033_signal(closeadj):
    result = _days_since_low(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Recency balance: days-since-low minus days-since-high at 252d
def f04bp_f04_breakout_proximity_dsbal_252d_base_v034_signal(closeadj):
    dh = _days_since_high(closeadj, 252)
    dl = _days_since_low(closeadj, 252)
    result = dl - dh
    return result.replace([np.inf, -np.inf], np.nan)


# Stale-high-with-drawdown: days-since-252d-high times distance-to-high
def f04bp_f04_breakout_proximity_dshdd_252d_base_v035_signal(closeadj):
    dh = _days_since_high(closeadj, 252)
    g = _dist_high(closeadj, 252)
    result = dh * g
    return result.replace([np.inf, -np.inf], np.nan)


# New-63d-high frequency over the last quarter, depth-weighted by proximity
def f04bp_f04_breakout_proximity_nhfreq_63d_base_v036_signal(closeadj):
    f = _newhigh_freq(closeadj, 63, 63)
    prox = closeadj / _rmax(closeadj, 63).replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-126d-high frequency over the last half-year, depth-weighted
def f04bp_f04_breakout_proximity_nhfreq_126d_base_v037_signal(closeadj):
    f = _newhigh_freq(closeadj, 126, 126)
    prox = closeadj / _rmax(closeadj, 126).replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-252d-high frequency over the last quarter, depth-weighted
def f04bp_f04_breakout_proximity_nhfreq_252d_base_v038_signal(closeadj):
    f = _newhigh_freq(closeadj, 252, 63)
    prox = closeadj / _rmax(closeadj, 252).replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-63d-low frequency over the last quarter, depth-weighted by floor proximity
def f04bp_f04_breakout_proximity_nlfreq_63d_base_v039_signal(closeadj):
    f = _newlow_freq(closeadj, 63, 63)
    prox = _rmin(closeadj, 63).replace(0, np.nan) / closeadj.replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-252d-low frequency over the last quarter, tempered by staleness of the low
def f04bp_f04_breakout_proximity_nlfreq_252d_base_v040_signal(closeadj):
    f = _newlow_freq(closeadj, 252, 63)
    stale = _days_since_low(closeadj, 252)
    result = f * (1.0 - stale) + 0.1 * stale
    return result.replace([np.inf, -np.inf], np.nan)


# Breakout dominance ratio: new-high vs new-low activity (log odds), 63d
def f04bp_f04_breakout_proximity_nhlfreqnet_63d_base_v041_signal(closeadj):
    nh = _newhigh_freq(closeadj, 63, 63)
    nl = _newlow_freq(closeadj, 63, 63)
    result = np.log((nh + 0.02) / (nl + 0.02))
    return result.replace([np.inf, -np.inf], np.nan)


# New-252d-high frequency change over a quarter plus proximity drift (breakout acceleration)
def f04bp_f04_breakout_proximity_nhfreqmom_252d_base_v042_signal(closeadj):
    f = _newhigh_freq(closeadj, 252, 63)
    prox = closeadj / _rmax(closeadj, 252).replace(0, np.nan)
    result = (f - f.shift(63)) + 0.25 * (prox - prox.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel width (band amplitude / price), 63d
def f04bp_f04_breakout_proximity_chanwid_63d_base_v043_signal(closeadj):
    result = _chan_width(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel width, 252d
def f04bp_f04_breakout_proximity_chanwid_252d_base_v044_signal(closeadj):
    result = _chan_width(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze ratio: 63d channel width vs its 252d typical width
def f04bp_f04_breakout_proximity_squeeze_63d_base_v045_signal(closeadj):
    result = _squeeze_ratio(closeadj, 63, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze ratio: 126d channel width vs its 252d typical width, log
def f04bp_f04_breakout_proximity_squeezelog_126d_base_v046_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 126, 252)
    result = np.log(sr.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-width compression streak: tight (<0.8x) fraction of last quarter plus inverse-width, 63d
def f04bp_f04_breakout_proximity_sqzstreak_63d_base_v047_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 63, 252)
    tight = (sr < 0.8).astype(float)
    result = tight.rolling(63, min_periods=21).mean() + 0.25 / sr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze-then-break: tight 63d channel AND fresh breakout headroom
def f04bp_f04_breakout_proximity_sqzbreak_63d_base_v048_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 63, 252)
    tight = (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    h = _headroom_high(closeadj, 63).clip(lower=0)
    result = tight * h
    return result.replace([np.inf, -np.inf], np.nan)


# Channel mid-skew (signed position vs channel midpoint), 126d
def f04bp_f04_breakout_proximity_midskew_126d_base_v049_signal(closeadj):
    result = _mid_skew(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel mid-skew 252d, change over a month (skew momentum)
def f04bp_f04_breakout_proximity_midskewmom_252d_base_v050_signal(closeadj):
    m = _mid_skew(closeadj, 252)
    result = m - m.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel mid-skew convexity: signed squared upper-channel bias, 252d
def f04bp_f04_breakout_proximity_midconvex_252d_base_v051_signal(closeadj):
    m = _mid_skew(closeadj, 252)
    result = np.sign(m) * (m * m) * 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-high climb rate over a quarter (ceiling lift), 252d
def f04bp_f04_breakout_proximity_hiclimb_252d_base_v052_signal(closeadj):
    result = _high_climb(closeadj, 252, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-high climb rate over a month, 126d
def f04bp_f04_breakout_proximity_hiclimbS_126d_base_v053_signal(closeadj):
    result = _high_climb(closeadj, 126, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-low lift rate over a quarter (floor rising), 252d
def f04bp_f04_breakout_proximity_lolift_252d_base_v054_signal(closeadj):
    result = _low_lift(closeadj, 252, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel slope balance: ceiling-climb minus floor-lift (expansion/translation), 252d
def f04bp_f04_breakout_proximity_chanslopebal_252d_base_v055_signal(closeadj):
    hc = _high_climb(closeadj, 252, 63)
    ll = _low_lift(closeadj, 252, 63)
    result = hc - ll
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-252d-high conditioned on channel squeeze (coiled-and-close breakout setup)
def f04bp_f04_breakout_proximity_gapvol_252d_base_v056_signal(closeadj):
    g = _dist_high(closeadj, 252)
    sr = _squeeze_ratio(closeadj, 63, 252)
    result = g * (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position times volume surge (breakout participation), 63d
def f04bp_f04_breakout_proximity_posvol_63d_base_v057_signal(closeadj, volume):
    p = _donch_pos(closeadj, 63)
    vz = _z(volume, 63)
    result = (p - 0.5) * vz
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position times dollar-volume z (conviction at the edge), 126d
def f04bp_f04_breakout_proximity_posdvol_126d_base_v058_signal(closeadj, volume):
    p = _donch_pos(closeadj, 126)
    dv = closeadj * volume
    dz = _z(dv, 126)
    result = (p - 0.5) * dz
    return result.replace([np.inf, -np.inf], np.nan)


# Approach speed to 252d high in ATR units (change over a month of the ATR-gap)
def f04bp_f04_breakout_proximity_gapatr_252d_base_v059_signal(closeadj, high, low):
    hi = _rmax(closeadj, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    r = (closeadj - hi) / atr.replace(0, np.nan)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Lift-off speed from 252d low in ATR units (change over a month of the ATR-cushion)
def f04bp_f04_breakout_proximity_lgapatr_252d_base_v060_signal(closeadj, high, low):
    lo = _rmin(closeadj, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    r = (closeadj - lo) / atr.replace(0, np.nan)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Time in upper channel third over last year (breakout persistence), 252d
def f04bp_f04_breakout_proximity_uppertime_252d_base_v061_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    up = (p >= 0.6667).astype(float)
    result = up.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Capitulation rate: entries into the lower channel third over last year, depth-weighted, 252d
def f04bp_f04_breakout_proximity_lowertime_252d_base_v062_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    dn = (p <= 0.3333).astype(float)
    entries = ((dn == 1) & (dn.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = (0.3333 - p).clip(lower=0).rolling(63, min_periods=21).mean()
    result = rate + 20.0 * depth
    return result.replace([np.inf, -np.inf], np.nan)


# Sticky-top: channel position weighted by how long it has held near the ceiling, 252d
def f04bp_f04_breakout_proximity_stickytop_252d_base_v063_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    persist = (p >= 0.8).astype(float).rolling(63, min_periods=21).mean()
    result = p * persist
    return result.replace([np.inf, -np.inf], np.nan)


# Near-high excess: avg distance above the 95% channel band when near ceiling, 252d
def f04bp_f04_breakout_proximity_nearhi_252d_base_v064_signal(closeadj):
    hi = _rmax(closeadj, 252)
    excess = (closeadj / hi.replace(0, np.nan) - 0.95).clip(lower=0)
    result = excess.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Breakout count: fresh 63d-high entries over last year plus headroom (continuous tilt)
def f04bp_f04_breakout_proximity_brkcount_63d_base_v065_signal(closeadj):
    hi = _rmax(closeadj, 63)
    is_hi = (closeadj >= hi * 0.99999).astype(float)
    entries = ((is_hi == 1) & (is_hi.shift(1) == 0)).astype(float)
    result = entries.rolling(252, min_periods=126).sum() + 5.0 * _headroom_high(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Breakdown count: fresh 63d-low entries over last year plus cushion (continuous tilt)
def f04bp_f04_breakout_proximity_brkdncount_63d_base_v066_signal(closeadj):
    lo = _rmin(closeadj, 63)
    is_lo = (closeadj <= lo * 1.00001).astype(float)
    entries = ((is_lo == 1) & (is_lo.shift(1) == 0)).astype(float)
    result = entries.rolling(252, min_periods=126).sum() - 5.0 * _cushion_low(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Multi-channel proximity disagreement: spread of close-vs-high across 63/126/252
def f04bp_f04_breakout_proximity_multiprox_252d_base_v067_signal(closeadj):
    h1 = _rmax(closeadj, 63)
    h2 = _rmax(closeadj, 126)
    h3 = _rmax(closeadj, 252)
    p1 = closeadj / h1.replace(0, np.nan)
    p2 = closeadj / h2.replace(0, np.nan)
    p3 = closeadj / h3.replace(0, np.nan)
    st = pd.concat([p1, p2, p3], axis=1)
    result = st.max(axis=1) - st.min(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# Multi-channel position dispersion (std of Donchian pos across 63/126/252)
def f04bp_f04_breakout_proximity_multidisp_252d_base_v068_signal(closeadj):
    p1 = _donch_pos(closeadj, 63)
    p2 = _donch_pos(closeadj, 126)
    p3 = _donch_pos(closeadj, 252)
    result = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-position agreement across 63/126/252 (signed geometric-style breakout consensus)
def f04bp_f04_breakout_proximity_chanbreadth_252d_base_v069_signal(closeadj):
    p1 = _donch_pos(closeadj, 63) - 0.5
    p2 = _donch_pos(closeadj, 126) - 0.5
    p3 = _donch_pos(closeadj, 252) - 0.5
    mn = (p1 + p2 + p3) / 3.0
    result = np.sign(mn) * (p1.abs() * p2.abs() * p3.abs()) ** (1.0 / 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position tanh-squashed momentum (bounded breakout thrust), 126d
def f04bp_f04_breakout_proximity_postanh_126d_base_v070_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    chg = p - p.shift(21)
    result = np.tanh(5.0 * chg)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-width change over a quarter (expansion/contraction velocity), 126d
def f04bp_f04_breakout_proximity_widchg_126d_base_v071_signal(closeadj):
    cw = _chan_width(closeadj, 126)
    result = cw - cw.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# Year-over-year distance-to-high change (anchor of breakout regime), 252d
def f04bp_f04_breakout_proximity_gapyoy_252d_base_v072_signal(closeadj):
    g = _dist_high(closeadj, 252)
    result = g - g.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position rank vs cross-time history (where-in-channel percentile), 252d
def f04bp_f04_breakout_proximity_posrank_252d_base_v073_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    result = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# True-high breakout headroom (close vs prior 252d intraday high), percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_truehead_252d_base_v074_signal(closeadj, high):
    prior_hi = high.shift(1).rolling(252, min_periods=126).max()
    raw = closeadj / prior_hi.replace(0, np.nan) - 1.0
    result = raw.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# True-low breakdown cushion (close vs prior 252d intraday low), percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_truecush_252d_base_v075_signal(closeadj, low):
    prior_lo = low.shift(1).rolling(252, min_periods=126).min()
    raw = closeadj / prior_lo.replace(0, np.nan) - 1.0
    result = raw.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04bp_f04_breakout_proximity_donchpos_63d_base_v001_signal,
    f04bp_f04_breakout_proximity_donchpos_126d_base_v002_signal,
    f04bp_f04_breakout_proximity_donchpos_252d_base_v003_signal,
    f04bp_f04_breakout_proximity_donchposz_252d_base_v004_signal,
    f04bp_f04_breakout_proximity_donchposrk_504d_base_v005_signal,
    f04bp_f04_breakout_proximity_donchposspr_63d_base_v006_signal,
    f04bp_f04_breakout_proximity_donchposmom_252d_base_v007_signal,
    f04bp_f04_breakout_proximity_donchposema_126d_base_v008_signal,
    f04bp_f04_breakout_proximity_donchposdisp_252d_base_v009_signal,
    f04bp_f04_breakout_proximity_hldonchz_63d_base_v010_signal,
    f04bp_f04_breakout_proximity_hldonchrk_252d_base_v011_signal,
    f04bp_f04_breakout_proximity_hlclosegap_126d_base_v012_signal,
    f04bp_f04_breakout_proximity_disthi_63d_base_v013_signal,
    f04bp_f04_breakout_proximity_disthi_126d_base_v014_signal,
    f04bp_f04_breakout_proximity_disthi_252d_base_v015_signal,
    f04bp_f04_breakout_proximity_disthiz_252d_base_v016_signal,
    f04bp_f04_breakout_proximity_disthimr_504d_base_v017_signal,
    f04bp_f04_breakout_proximity_disthimom_252d_base_v018_signal,
    f04bp_f04_breakout_proximity_distlo_63d_base_v019_signal,
    f04bp_f04_breakout_proximity_distlo_126d_base_v020_signal,
    f04bp_f04_breakout_proximity_distlo_252d_base_v021_signal,
    f04bp_f04_breakout_proximity_distloz_252d_base_v022_signal,
    f04bp_f04_breakout_proximity_distlork_504d_base_v023_signal,
    f04bp_f04_breakout_proximity_headroom_63d_base_v024_signal,
    f04bp_f04_breakout_proximity_headroomz_252d_base_v025_signal,
    f04bp_f04_breakout_proximity_cushion_63d_base_v026_signal,
    f04bp_f04_breakout_proximity_cushionz_252d_base_v027_signal,
    f04bp_f04_breakout_proximity_brkasym_126d_base_v028_signal,
    f04bp_f04_breakout_proximity_dsh_63d_base_v029_signal,
    f04bp_f04_breakout_proximity_dsh_126d_base_v030_signal,
    f04bp_f04_breakout_proximity_dsh_252d_base_v031_signal,
    f04bp_f04_breakout_proximity_dsl_63d_base_v032_signal,
    f04bp_f04_breakout_proximity_dsl_252d_base_v033_signal,
    f04bp_f04_breakout_proximity_dsbal_252d_base_v034_signal,
    f04bp_f04_breakout_proximity_dshdd_252d_base_v035_signal,
    f04bp_f04_breakout_proximity_nhfreq_63d_base_v036_signal,
    f04bp_f04_breakout_proximity_nhfreq_126d_base_v037_signal,
    f04bp_f04_breakout_proximity_nhfreq_252d_base_v038_signal,
    f04bp_f04_breakout_proximity_nlfreq_63d_base_v039_signal,
    f04bp_f04_breakout_proximity_nlfreq_252d_base_v040_signal,
    f04bp_f04_breakout_proximity_nhlfreqnet_63d_base_v041_signal,
    f04bp_f04_breakout_proximity_nhfreqmom_252d_base_v042_signal,
    f04bp_f04_breakout_proximity_chanwid_63d_base_v043_signal,
    f04bp_f04_breakout_proximity_chanwid_252d_base_v044_signal,
    f04bp_f04_breakout_proximity_squeeze_63d_base_v045_signal,
    f04bp_f04_breakout_proximity_squeezelog_126d_base_v046_signal,
    f04bp_f04_breakout_proximity_sqzstreak_63d_base_v047_signal,
    f04bp_f04_breakout_proximity_sqzbreak_63d_base_v048_signal,
    f04bp_f04_breakout_proximity_midskew_126d_base_v049_signal,
    f04bp_f04_breakout_proximity_midskewmom_252d_base_v050_signal,
    f04bp_f04_breakout_proximity_midconvex_252d_base_v051_signal,
    f04bp_f04_breakout_proximity_hiclimb_252d_base_v052_signal,
    f04bp_f04_breakout_proximity_hiclimbS_126d_base_v053_signal,
    f04bp_f04_breakout_proximity_lolift_252d_base_v054_signal,
    f04bp_f04_breakout_proximity_chanslopebal_252d_base_v055_signal,
    f04bp_f04_breakout_proximity_gapvol_252d_base_v056_signal,
    f04bp_f04_breakout_proximity_posvol_63d_base_v057_signal,
    f04bp_f04_breakout_proximity_posdvol_126d_base_v058_signal,
    f04bp_f04_breakout_proximity_gapatr_252d_base_v059_signal,
    f04bp_f04_breakout_proximity_lgapatr_252d_base_v060_signal,
    f04bp_f04_breakout_proximity_uppertime_252d_base_v061_signal,
    f04bp_f04_breakout_proximity_lowertime_252d_base_v062_signal,
    f04bp_f04_breakout_proximity_stickytop_252d_base_v063_signal,
    f04bp_f04_breakout_proximity_nearhi_252d_base_v064_signal,
    f04bp_f04_breakout_proximity_brkcount_63d_base_v065_signal,
    f04bp_f04_breakout_proximity_brkdncount_63d_base_v066_signal,
    f04bp_f04_breakout_proximity_multiprox_252d_base_v067_signal,
    f04bp_f04_breakout_proximity_multidisp_252d_base_v068_signal,
    f04bp_f04_breakout_proximity_chanbreadth_252d_base_v069_signal,
    f04bp_f04_breakout_proximity_postanh_126d_base_v070_signal,
    f04bp_f04_breakout_proximity_widchg_126d_base_v071_signal,
    f04bp_f04_breakout_proximity_gapyoy_252d_base_v072_signal,
    f04bp_f04_breakout_proximity_posrank_252d_base_v073_signal,
    f04bp_f04_breakout_proximity_truehead_252d_base_v074_signal,
    f04bp_f04_breakout_proximity_truecush_252d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_BREAKOUT_PROXIMITY_REGISTRY_001_075 = REGISTRY


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

    print("OK f04_breakout_proximity_base_001_075_claude: %d features pass" % n_features)
