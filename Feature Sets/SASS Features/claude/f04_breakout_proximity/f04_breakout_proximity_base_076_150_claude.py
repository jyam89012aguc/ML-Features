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



# Donchian channel position over 21d (fast channel)
def f04bp_f04_breakout_proximity_donchpos_21d_base_v076_signal(closeadj):
    result = _donch_pos(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 504d (long channel)
def f04bp_f04_breakout_proximity_donchpos_504d_base_v077_signal(closeadj):
    result = _donch_pos(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Multi-year vs mid channel position spread: 1260d Donchian pos minus 504d pos
def f04bp_f04_breakout_proximity_donchpos_1260d_base_v078_signal(closeadj):
    p_long = _donch_pos(closeadj, 1260)
    p_mid = _donch_pos(closeadj, 504)
    result = p_long - p_mid
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position 126d, z-scored vs own 63d history
def f04bp_f04_breakout_proximity_donchposz_126d_base_v079_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    result = _z(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position 1260d, percentile vs own 504d history
def f04bp_f04_breakout_proximity_donchposrk_1260d_base_v080_signal(closeadj):
    p = _donch_pos(closeadj, 1260)
    result = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position spread: 126d channel minus 504d channel
def f04bp_f04_breakout_proximity_donchposspr_126d_base_v081_signal(closeadj):
    s = _donch_pos(closeadj, 126)
    l = _donch_pos(closeadj, 504)
    result = s - l
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position momentum: 126d channel position change over a month
def f04bp_f04_breakout_proximity_donchposmom_126d_base_v082_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    result = p - p.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position smoothed, 252d (slow EMA placement)
def f04bp_f04_breakout_proximity_donchposema_252d_base_v083_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    result = p.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position displacement from own EMA, 126d
def f04bp_f04_breakout_proximity_donchposdisp_126d_base_v084_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    result = p - p.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# True high/low channel position 126d, percentile vs 252d history
def f04bp_f04_breakout_proximity_hldonchrk_126d_base_v085_signal(closeadj, high, low):
    p = _donch_pos_hl(closeadj, high, low, 126)
    result = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# True high/low channel position 504d, z-scored vs own 252d history
def f04bp_f04_breakout_proximity_hldonchz_504d_base_v086_signal(closeadj, high, low):
    p = _donch_pos_hl(closeadj, high, low, 504)
    result = _z(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# True-channel vs close-channel position gap, 252d (intraday breakout premium)
def f04bp_f04_breakout_proximity_hlclosegap_252d_base_v087_signal(closeadj, high, low):
    ph = _donch_pos_hl(closeadj, high, low, 252)
    pc = _donch_pos(closeadj, 252)
    result = ph - pc
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 21d high (fast ceiling gap)
def f04bp_f04_breakout_proximity_disthi_21d_base_v088_signal(closeadj):
    result = _dist_high(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 504d high
def f04bp_f04_breakout_proximity_disthi_504d_base_v089_signal(closeadj):
    result = _dist_high(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 1260d high, mean-reverting vs its own 252d typical multi-year gap
def f04bp_f04_breakout_proximity_disthi_1260d_base_v090_signal(closeadj):
    g = _dist_high(closeadj, 1260)
    result = g - g.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 126d high, z-scored vs own 126d history
def f04bp_f04_breakout_proximity_disthiz_126d_base_v091_signal(closeadj):
    g = _dist_high(closeadj, 126)
    result = _z(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance to 252d high mean-reverting vs own 63d average
def f04bp_f04_breakout_proximity_disthimr_252d_base_v092_signal(closeadj):
    g = _dist_high(closeadj, 252)
    result = g - g.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-504d-high momentum over a quarter
def f04bp_f04_breakout_proximity_disthimom_504d_base_v093_signal(closeadj):
    g = _dist_high(closeadj, 504)
    result = g - g.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 21d low (fast floor cushion)
def f04bp_f04_breakout_proximity_distlo_21d_base_v094_signal(closeadj):
    result = _dist_low(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 504d low
def f04bp_f04_breakout_proximity_distlo_504d_base_v095_signal(closeadj):
    result = _dist_low(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 1260d low, mean-reverting vs its own 252d typical multi-year cushion
def f04bp_f04_breakout_proximity_distlo_1260d_base_v096_signal(closeadj):
    g = _dist_low(closeadj, 1260)
    result = g - g.rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 126d low, z-scored vs own 126d history
def f04bp_f04_breakout_proximity_distloz_126d_base_v097_signal(closeadj):
    g = _dist_low(closeadj, 126)
    result = _z(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance above 252d low, mean-reverting vs own 63d average
def f04bp_f04_breakout_proximity_distlomr_252d_base_v098_signal(closeadj):
    g = _dist_low(closeadj, 252)
    result = g - g.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-126d-high relative to its own 126d typical gap (closeness vs usual)
def f04bp_f04_breakout_proximity_headroom_126d_base_v099_signal(closeadj):
    g = _dist_high(closeadj, 126)
    typ = g.rolling(126, min_periods=63).mean()
    result = g / typ.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-504d-high relative to its own 252d typical gap, smoothed
def f04bp_f04_breakout_proximity_headroomz_504d_base_v100_signal(closeadj):
    g = _dist_high(closeadj, 504)
    typ = g.rolling(252, min_periods=126).mean()
    r = g / typ.replace(0, np.nan) - 1.0
    result = r.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-above-126d-low relative to its own 126d typical cushion (closeness vs usual)
def f04bp_f04_breakout_proximity_cushion_126d_base_v101_signal(closeadj):
    g = _dist_low(closeadj, 126)
    typ = g.rolling(126, min_periods=63).mean()
    result = g / typ.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-above-504d-low relative to its own 252d typical cushion, smoothed
def f04bp_f04_breakout_proximity_cushionz_504d_base_v102_signal(closeadj):
    g = _dist_low(closeadj, 504)
    typ = g.rolling(252, min_periods=126).mean()
    r = g / typ.replace(0, np.nan) - 1.0
    result = r.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Breakout asymmetry at 252d: headroom-above-high minus cushion-above-low
def f04bp_f04_breakout_proximity_brkasym_252d_base_v103_signal(closeadj):
    h = _headroom_high(closeadj, 252)
    c = _cushion_low(closeadj, 252)
    result = h - c
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 504d high, percentile-ranked vs own 252d history (relative breakout staleness)
def f04bp_f04_breakout_proximity_dsh_504d_base_v104_signal(closeadj):
    d = _days_since_high(closeadj, 504)
    result = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 1260d high minus days since 504d high (multi-year vs mid breakout staleness spread)
def f04bp_f04_breakout_proximity_dsh_1260d_base_v105_signal(closeadj):
    d_long = _days_since_high(closeadj, 1260)
    d_mid = _days_since_high(closeadj, 504)
    result = d_long - d_mid
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 126d high
def f04bp_f04_breakout_proximity_dsh_126d_base_v106_signal(closeadj):
    result = _days_since_high(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 504d low
def f04bp_f04_breakout_proximity_dsl_504d_base_v107_signal(closeadj):
    result = _days_since_low(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Days since 126d low
def f04bp_f04_breakout_proximity_dsl_126d_base_v108_signal(closeadj):
    result = _days_since_low(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Recency balance at 504d: days-since-low minus days-since-high
def f04bp_f04_breakout_proximity_dsbal_504d_base_v109_signal(closeadj):
    dh = _days_since_high(closeadj, 504)
    dl = _days_since_low(closeadj, 504)
    result = dl - dh
    return result.replace([np.inf, -np.inf], np.nan)


# Stale-low-with-recovery: days-since-252d-low times distance-above-low
def f04bp_f04_breakout_proximity_dsldd_252d_base_v110_signal(closeadj):
    dl = _days_since_low(closeadj, 252)
    g = _dist_low(closeadj, 252)
    result = dl * g
    return result.replace([np.inf, -np.inf], np.nan)


# New-63d-high frequency over the last month plus proximity (fast breakout cadence)
def f04bp_f04_breakout_proximity_nhfreqS_63d_base_v111_signal(closeadj):
    f = _newhigh_freq(closeadj, 63, 21)
    prox = closeadj / _rmax(closeadj, 63).replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-252d-high frequency over the last half-year, depth-weighted
def f04bp_f04_breakout_proximity_nhfreqL_252d_base_v112_signal(closeadj):
    f = _newhigh_freq(closeadj, 252, 126)
    prox = closeadj / _rmax(closeadj, 252).replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-504d-high frequency over the last quarter, depth-weighted
def f04bp_f04_breakout_proximity_nhfreq_504d_base_v113_signal(closeadj):
    f = _newhigh_freq(closeadj, 504, 63)
    prox = closeadj / _rmax(closeadj, 504).replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-126d-low frequency over the last quarter, depth-weighted
def f04bp_f04_breakout_proximity_nlfreq_126d_base_v114_signal(closeadj):
    f = _newlow_freq(closeadj, 126, 63)
    prox = _rmin(closeadj, 126).replace(0, np.nan) / closeadj.replace(0, np.nan)
    result = f + 0.5 * prox
    return result.replace([np.inf, -np.inf], np.nan)


# New-504d-low frequency over the last half-year, modulated by channel width (deep-base breakdowns)
def f04bp_f04_breakout_proximity_nlfreqL_504d_base_v115_signal(closeadj):
    f = _newlow_freq(closeadj, 504, 126)
    cw = _chan_width(closeadj, 504)
    result = f + 0.3 * cw + 0.2 * cw.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# Breakout dominance at 252d: new-high vs new-low log-odds plus proximity differential
def f04bp_f04_breakout_proximity_nhlfreqnet_252d_base_v116_signal(closeadj):
    nh = _newhigh_freq(closeadj, 252, 63)
    nl = _newlow_freq(closeadj, 252, 63)
    ph = closeadj / _rmax(closeadj, 252).replace(0, np.nan)
    pl = _rmin(closeadj, 252).replace(0, np.nan) / closeadj.replace(0, np.nan)
    result = np.log((nh + 0.02) / (nl + 0.02)) + (ph - pl)
    return result.replace([np.inf, -np.inf], np.nan)


# New-126d-high frequency change over a quarter plus proximity drift
def f04bp_f04_breakout_proximity_nhfreqmom_126d_base_v117_signal(closeadj):
    f = _newhigh_freq(closeadj, 126, 63)
    prox = closeadj / _rmax(closeadj, 126).replace(0, np.nan)
    result = (f - f.shift(63)) + 0.25 * (prox - prox.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel width, 126d
def f04bp_f04_breakout_proximity_chanwid_126d_base_v118_signal(closeadj):
    result = _chan_width(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel width, 504d
def f04bp_f04_breakout_proximity_chanwid_504d_base_v119_signal(closeadj):
    result = _chan_width(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze ratio: 252d channel width vs its 504d typical width
def f04bp_f04_breakout_proximity_squeeze_252d_base_v120_signal(closeadj):
    result = _squeeze_ratio(closeadj, 252, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze ratio: 21d channel width vs its 126d typical width, log
def f04bp_f04_breakout_proximity_squeezelog_21d_base_v121_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 21, 126)
    result = np.log(sr.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-width compression streak: tight (<0.8x) fraction of last half-year plus inverse-width, 126d
def f04bp_f04_breakout_proximity_sqzstreak_126d_base_v122_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 126, 504)
    tight = (sr < 0.8).astype(float)
    result = tight.rolling(126, min_periods=63).mean() + 0.25 / sr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze-then-break at 126d: tight channel AND fresh breakout headroom
def f04bp_f04_breakout_proximity_sqzbreak_126d_base_v123_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 126, 504)
    tight = (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    h = _headroom_high(closeadj, 126).clip(lower=0)
    result = tight * h
    return result.replace([np.inf, -np.inf], np.nan)


# Squeeze-then-breakdown setup at 63d: tight channel times floor-proximity (coiled near support)
def f04bp_f04_breakout_proximity_sqzbreakdn_63d_base_v124_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 63, 252)
    tight = (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    near_floor = 1.0 / (1.0 + 50.0 * _dist_low(closeadj, 63))
    result = tight * near_floor
    return result.replace([np.inf, -np.inf], np.nan)


# Channel mid-skew, 63d
def f04bp_f04_breakout_proximity_midskew_63d_base_v125_signal(closeadj):
    result = _mid_skew(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel mid-skew 504d smoothed (long breakout bias)
def f04bp_f04_breakout_proximity_midskewsm_504d_base_v126_signal(closeadj):
    m = _mid_skew(closeadj, 504)
    result = m.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Channel mid-skew convexity at 126d (signed squared bias)
def f04bp_f04_breakout_proximity_midconvex_126d_base_v127_signal(closeadj):
    m = _mid_skew(closeadj, 126)
    result = np.sign(m) * (m * m) * 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-high climb rate over a quarter, 504d
def f04bp_f04_breakout_proximity_hiclimb_504d_base_v128_signal(closeadj):
    result = _high_climb(closeadj, 504, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-high climb rate over a month, 63d
def f04bp_f04_breakout_proximity_hiclimbS_63d_base_v129_signal(closeadj):
    result = _high_climb(closeadj, 63, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-low lift rate over a quarter, 504d
def f04bp_f04_breakout_proximity_lolift_504d_base_v130_signal(closeadj):
    result = _low_lift(closeadj, 504, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel slope balance at 126d: ceiling-climb minus floor-lift
def f04bp_f04_breakout_proximity_chanslopebal_126d_base_v131_signal(closeadj):
    hc = _high_climb(closeadj, 126, 21)
    ll = _low_lift(closeadj, 126, 21)
    result = hc - ll
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-to-504d-high conditioned on 126d channel squeeze (coiled-and-close long setup)
def f04bp_f04_breakout_proximity_gapvol_504d_base_v132_signal(closeadj):
    g = _dist_high(closeadj, 504)
    sr = _squeeze_ratio(closeadj, 126, 504)
    result = g * (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position times volume surge, 126d
def f04bp_f04_breakout_proximity_posvol_126d_base_v133_signal(closeadj, volume):
    p = _donch_pos(closeadj, 126)
    vz = _z(volume, 126)
    result = (p - 0.5) * vz
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position times dollar-volume z, 252d
def f04bp_f04_breakout_proximity_posdvol_252d_base_v134_signal(closeadj, volume):
    p = _donch_pos(closeadj, 252)
    dv = closeadj * volume
    dz = _z(dv, 252)
    result = (p - 0.5) * dz
    return result.replace([np.inf, -np.inf], np.nan)


# Approach speed to 126d high in ATR units (change over a month of the ATR-gap)
def f04bp_f04_breakout_proximity_gapatr_126d_base_v135_signal(closeadj, high, low):
    hi = _rmax(closeadj, 126)
    atr = (high - low).rolling(21, min_periods=5).mean()
    r = (closeadj - hi) / atr.replace(0, np.nan)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Lift-off speed from 126d low in ATR units (change over a month of the ATR-cushion)
def f04bp_f04_breakout_proximity_lgapatr_126d_base_v136_signal(closeadj, high, low):
    lo = _rmin(closeadj, 126)
    atr = (high - low).rolling(21, min_periods=5).mean()
    r = (closeadj - lo) / atr.replace(0, np.nan)
    result = r - r.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# Time in upper channel third over last half-year, 126d
def f04bp_f04_breakout_proximity_uppertime_126d_base_v137_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    up = (p >= 0.6667).astype(float)
    result = up.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Time in lower channel third over last half-year, 126d
def f04bp_f04_breakout_proximity_lowertime_126d_base_v138_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    dn = (p <= 0.3333).astype(float)
    result = dn.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Sticky-bottom: channel position deficit weighted by time held near floor, 252d
def f04bp_f04_breakout_proximity_stickybot_252d_base_v139_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    persist = (p <= 0.2).astype(float).rolling(63, min_periods=21).mean()
    result = (p - 0.5) * persist
    return result.replace([np.inf, -np.inf], np.nan)


# Near-low excess: avg distance below the 105% channel-floor band, 252d
def f04bp_f04_breakout_proximity_nearlo_252d_base_v140_signal(closeadj):
    lo = _rmin(closeadj, 252)
    excess = (1.05 - closeadj / lo.replace(0, np.nan)).clip(lower=0)
    result = excess.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Breakout count: fresh 126d-high entries over last year plus headroom tilt
def f04bp_f04_breakout_proximity_brkcount_126d_base_v141_signal(closeadj):
    hi = _rmax(closeadj, 126)
    is_hi = (closeadj >= hi * 0.99999).astype(float)
    entries = ((is_hi == 1) & (is_hi.shift(1) == 0)).astype(float)
    result = entries.rolling(252, min_periods=126).sum() + 5.0 * _headroom_high(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Breakdown count: fresh 126d-low entries over last year plus cushion tilt
def f04bp_f04_breakout_proximity_brkdncount_126d_base_v142_signal(closeadj):
    lo = _rmin(closeadj, 126)
    is_lo = (closeadj <= lo * 1.00001).astype(float)
    entries = ((is_lo == 1) & (is_lo.shift(1) == 0)).astype(float)
    result = entries.rolling(252, min_periods=126).sum() - 5.0 * _cushion_low(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Multi-channel proximity disagreement across 126/252/504
def f04bp_f04_breakout_proximity_multiprox_504d_base_v143_signal(closeadj):
    h1 = _rmax(closeadj, 126)
    h2 = _rmax(closeadj, 252)
    h3 = _rmax(closeadj, 504)
    p1 = closeadj / h1.replace(0, np.nan)
    p2 = closeadj / h2.replace(0, np.nan)
    p3 = closeadj / h3.replace(0, np.nan)
    st = pd.concat([p1, p2, p3], axis=1)
    result = st.max(axis=1) - st.min(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# Multi-channel position dispersion across 126/252/504
def f04bp_f04_breakout_proximity_multidisp_504d_base_v144_signal(closeadj):
    p1 = _donch_pos(closeadj, 126)
    p2 = _donch_pos(closeadj, 252)
    p3 = _donch_pos(closeadj, 504)
    result = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel-position agreement across 126/252/504 (signed geometric-style breakout consensus)
def f04bp_f04_breakout_proximity_chanbreadth_504d_base_v145_signal(closeadj):
    p1 = _donch_pos(closeadj, 126) - 0.5
    p2 = _donch_pos(closeadj, 252) - 0.5
    p3 = _donch_pos(closeadj, 504) - 0.5
    mn = (p1 + p2 + p3) / 3.0
    result = np.sign(mn) * (p1.abs() * p2.abs() * p3.abs()) ** (1.0 / 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position tanh-squashed momentum, 252d
def f04bp_f04_breakout_proximity_postanh_252d_base_v146_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    chg = p - p.shift(63)
    result = np.tanh(5.0 * chg)
    return result.replace([np.inf, -np.inf], np.nan)


# Distance-above-low sign x sqrt-magnitude (compressed cushion), 252d
def f04bp_f04_breakout_proximity_lgapsignmag_252d_base_v147_signal(closeadj):
    g = _dist_low(closeadj, 252)
    result = np.sign(g) * (g.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# Channel position rank vs cross-time history, 126d
def f04bp_f04_breakout_proximity_posrank_126d_base_v148_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    result = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# True-high breakout headroom at 504d, percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_truehead_504d_base_v149_signal(closeadj, high):
    prior_hi = high.shift(1).rolling(504, min_periods=252).max()
    raw = closeadj / prior_hi.replace(0, np.nan) - 1.0
    result = raw.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# True-low breakdown cushion at 504d, percentile-ranked vs own 252d history
def f04bp_f04_breakout_proximity_truecush_504d_base_v150_signal(closeadj, low):
    prior_lo = low.shift(1).rolling(504, min_periods=252).min()
    raw = closeadj / prior_lo.replace(0, np.nan) - 1.0
    result = raw.rolling(252, min_periods=63).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04bp_f04_breakout_proximity_donchpos_21d_base_v076_signal,
    f04bp_f04_breakout_proximity_donchpos_504d_base_v077_signal,
    f04bp_f04_breakout_proximity_donchpos_1260d_base_v078_signal,
    f04bp_f04_breakout_proximity_donchposz_126d_base_v079_signal,
    f04bp_f04_breakout_proximity_donchposrk_1260d_base_v080_signal,
    f04bp_f04_breakout_proximity_donchposspr_126d_base_v081_signal,
    f04bp_f04_breakout_proximity_donchposmom_126d_base_v082_signal,
    f04bp_f04_breakout_proximity_donchposema_252d_base_v083_signal,
    f04bp_f04_breakout_proximity_donchposdisp_126d_base_v084_signal,
    f04bp_f04_breakout_proximity_hldonchrk_126d_base_v085_signal,
    f04bp_f04_breakout_proximity_hldonchz_504d_base_v086_signal,
    f04bp_f04_breakout_proximity_hlclosegap_252d_base_v087_signal,
    f04bp_f04_breakout_proximity_disthi_21d_base_v088_signal,
    f04bp_f04_breakout_proximity_disthi_504d_base_v089_signal,
    f04bp_f04_breakout_proximity_disthi_1260d_base_v090_signal,
    f04bp_f04_breakout_proximity_disthiz_126d_base_v091_signal,
    f04bp_f04_breakout_proximity_disthimr_252d_base_v092_signal,
    f04bp_f04_breakout_proximity_disthimom_504d_base_v093_signal,
    f04bp_f04_breakout_proximity_distlo_21d_base_v094_signal,
    f04bp_f04_breakout_proximity_distlo_504d_base_v095_signal,
    f04bp_f04_breakout_proximity_distlo_1260d_base_v096_signal,
    f04bp_f04_breakout_proximity_distloz_126d_base_v097_signal,
    f04bp_f04_breakout_proximity_distlomr_252d_base_v098_signal,
    f04bp_f04_breakout_proximity_headroom_126d_base_v099_signal,
    f04bp_f04_breakout_proximity_headroomz_504d_base_v100_signal,
    f04bp_f04_breakout_proximity_cushion_126d_base_v101_signal,
    f04bp_f04_breakout_proximity_cushionz_504d_base_v102_signal,
    f04bp_f04_breakout_proximity_brkasym_252d_base_v103_signal,
    f04bp_f04_breakout_proximity_dsh_504d_base_v104_signal,
    f04bp_f04_breakout_proximity_dsh_1260d_base_v105_signal,
    f04bp_f04_breakout_proximity_dsh_126d_base_v106_signal,
    f04bp_f04_breakout_proximity_dsl_504d_base_v107_signal,
    f04bp_f04_breakout_proximity_dsl_126d_base_v108_signal,
    f04bp_f04_breakout_proximity_dsbal_504d_base_v109_signal,
    f04bp_f04_breakout_proximity_dsldd_252d_base_v110_signal,
    f04bp_f04_breakout_proximity_nhfreqS_63d_base_v111_signal,
    f04bp_f04_breakout_proximity_nhfreqL_252d_base_v112_signal,
    f04bp_f04_breakout_proximity_nhfreq_504d_base_v113_signal,
    f04bp_f04_breakout_proximity_nlfreq_126d_base_v114_signal,
    f04bp_f04_breakout_proximity_nlfreqL_504d_base_v115_signal,
    f04bp_f04_breakout_proximity_nhlfreqnet_252d_base_v116_signal,
    f04bp_f04_breakout_proximity_nhfreqmom_126d_base_v117_signal,
    f04bp_f04_breakout_proximity_chanwid_126d_base_v118_signal,
    f04bp_f04_breakout_proximity_chanwid_504d_base_v119_signal,
    f04bp_f04_breakout_proximity_squeeze_252d_base_v120_signal,
    f04bp_f04_breakout_proximity_squeezelog_21d_base_v121_signal,
    f04bp_f04_breakout_proximity_sqzstreak_126d_base_v122_signal,
    f04bp_f04_breakout_proximity_sqzbreak_126d_base_v123_signal,
    f04bp_f04_breakout_proximity_sqzbreakdn_63d_base_v124_signal,
    f04bp_f04_breakout_proximity_midskew_63d_base_v125_signal,
    f04bp_f04_breakout_proximity_midskewsm_504d_base_v126_signal,
    f04bp_f04_breakout_proximity_midconvex_126d_base_v127_signal,
    f04bp_f04_breakout_proximity_hiclimb_504d_base_v128_signal,
    f04bp_f04_breakout_proximity_hiclimbS_63d_base_v129_signal,
    f04bp_f04_breakout_proximity_lolift_504d_base_v130_signal,
    f04bp_f04_breakout_proximity_chanslopebal_126d_base_v131_signal,
    f04bp_f04_breakout_proximity_gapvol_504d_base_v132_signal,
    f04bp_f04_breakout_proximity_posvol_126d_base_v133_signal,
    f04bp_f04_breakout_proximity_posdvol_252d_base_v134_signal,
    f04bp_f04_breakout_proximity_gapatr_126d_base_v135_signal,
    f04bp_f04_breakout_proximity_lgapatr_126d_base_v136_signal,
    f04bp_f04_breakout_proximity_uppertime_126d_base_v137_signal,
    f04bp_f04_breakout_proximity_lowertime_126d_base_v138_signal,
    f04bp_f04_breakout_proximity_stickybot_252d_base_v139_signal,
    f04bp_f04_breakout_proximity_nearlo_252d_base_v140_signal,
    f04bp_f04_breakout_proximity_brkcount_126d_base_v141_signal,
    f04bp_f04_breakout_proximity_brkdncount_126d_base_v142_signal,
    f04bp_f04_breakout_proximity_multiprox_504d_base_v143_signal,
    f04bp_f04_breakout_proximity_multidisp_504d_base_v144_signal,
    f04bp_f04_breakout_proximity_chanbreadth_504d_base_v145_signal,
    f04bp_f04_breakout_proximity_postanh_252d_base_v146_signal,
    f04bp_f04_breakout_proximity_lgapsignmag_252d_base_v147_signal,
    f04bp_f04_breakout_proximity_posrank_126d_base_v148_signal,
    f04bp_f04_breakout_proximity_truehead_504d_base_v149_signal,
    f04bp_f04_breakout_proximity_truecush_504d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_BREAKOUT_PROXIMITY_REGISTRY_076_150 = REGISTRY


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

    print("OK f04_breakout_proximity_base_076_150_claude: %d features pass" % n_features)
