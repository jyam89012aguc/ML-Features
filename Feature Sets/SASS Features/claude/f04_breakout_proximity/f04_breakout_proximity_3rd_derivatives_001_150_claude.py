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



# jerk (2nd deriv, 5d ROC) of donchpos 21d breakout-proximity base
def f04bp_f04_breakout_proximity_donchpos_21d_jerk_v001_signal(closeadj):
    base = _donch_pos(closeadj, 21)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchpos 63d breakout-proximity base
def f04bp_f04_breakout_proximity_donchpos_63d_jerk_v002_signal(closeadj):
    base = _donch_pos(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchpos 126d breakout-proximity base
def f04bp_f04_breakout_proximity_donchpos_126d_jerk_v003_signal(closeadj):
    base = _donch_pos(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchpos 252d breakout-proximity base
def f04bp_f04_breakout_proximity_donchpos_252d_jerk_v004_signal(closeadj):
    base = _donch_pos(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposspr 63d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposspr_63d_jerk_v005_signal(closeadj):
    base = _donch_pos(closeadj, 63) - _donch_pos(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposspr 126d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposspr_126d_jerk_v006_signal(closeadj):
    base = _donch_pos(closeadj, 126) - _donch_pos(closeadj, 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposspr 252d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposspr_252d_jerk_v007_signal(closeadj):
    base = _donch_pos(closeadj, 252) - _donch_pos(closeadj, 1260)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposz 63d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposz_63d_jerk_v008_signal(closeadj):
    base = _z(_donch_pos(closeadj, 63), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposz 126d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposz_126d_jerk_v009_signal(closeadj):
    base = _z(_donch_pos(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposz_252d_jerk_v010_signal(closeadj):
    base = _z(_donch_pos(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposdisp 126d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposdisp_126d_jerk_v011_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    base = p - p.ewm(span=42, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposdisp 252d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposdisp_252d_jerk_v012_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    base = p - p.ewm(span=63, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hlclosegap 63d breakout-proximity base
def f04bp_f04_breakout_proximity_hlclosegap_63d_jerk_v013_signal(closeadj, high, low):
    base = _donch_pos_hl(closeadj, high, low, 63) - _donch_pos(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hlclosegap 126d breakout-proximity base
def f04bp_f04_breakout_proximity_hlclosegap_126d_jerk_v014_signal(closeadj, high, low):
    base = _donch_pos_hl(closeadj, high, low, 126) - _donch_pos(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hlclosegap 252d breakout-proximity base
def f04bp_f04_breakout_proximity_hlclosegap_252d_jerk_v015_signal(closeadj, high, low):
    base = _donch_pos_hl(closeadj, high, low, 252) - _donch_pos(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 5d ROC) of disthi 21d breakout-proximity base
def f04bp_f04_breakout_proximity_disthi_21d_jerk_v016_signal(closeadj):
    base = _dist_high(closeadj, 21)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthi 63d breakout-proximity base
def f04bp_f04_breakout_proximity_disthi_63d_jerk_v017_signal(closeadj):
    base = _dist_high(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthi 126d breakout-proximity base
def f04bp_f04_breakout_proximity_disthi_126d_jerk_v018_signal(closeadj):
    base = _dist_high(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthi 252d breakout-proximity base
def f04bp_f04_breakout_proximity_disthi_252d_jerk_v019_signal(closeadj):
    base = _dist_high(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of disthimr504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_disthimr504_504d_jerk_v020_signal(closeadj):
    g = _dist_high(closeadj, 504)
    base = g - g.rolling(126, min_periods=63).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of disthimr1260 1260d breakout-proximity base
def f04bp_f04_breakout_proximity_disthimr1260_1260d_jerk_v021_signal(closeadj):
    g = _dist_high(closeadj, 1260)
    base = g - g.rolling(252, min_periods=126).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthiz 126d breakout-proximity base
def f04bp_f04_breakout_proximity_disthiz_126d_jerk_v022_signal(closeadj):
    base = _z(_dist_high(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthiz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_disthiz_252d_jerk_v023_signal(closeadj):
    base = _z(_dist_high(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 5d ROC) of distlo 21d breakout-proximity base
def f04bp_f04_breakout_proximity_distlo_21d_jerk_v024_signal(closeadj):
    base = _dist_low(closeadj, 21)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlo 63d breakout-proximity base
def f04bp_f04_breakout_proximity_distlo_63d_jerk_v025_signal(closeadj):
    base = _dist_low(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlo 126d breakout-proximity base
def f04bp_f04_breakout_proximity_distlo_126d_jerk_v026_signal(closeadj):
    base = _dist_low(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlo 252d breakout-proximity base
def f04bp_f04_breakout_proximity_distlo_252d_jerk_v027_signal(closeadj):
    base = _dist_low(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of distlomr504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_distlomr504_504d_jerk_v028_signal(closeadj):
    g = _dist_low(closeadj, 504)
    base = g - g.rolling(126, min_periods=63).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distloz 126d breakout-proximity base
def f04bp_f04_breakout_proximity_distloz_126d_jerk_v029_signal(closeadj):
    base = _z(_dist_low(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distloz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_distloz_252d_jerk_v030_signal(closeadj):
    base = _z(_dist_low(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of headroom 63d breakout-proximity base
def f04bp_f04_breakout_proximity_headroom_63d_jerk_v031_signal(closeadj):
    g = _dist_high(closeadj, 63)
    typ = g.rolling(63, min_periods=21).mean()
    base = g / typ.replace(0, np.nan) - 1.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of headroom 126d breakout-proximity base
def f04bp_f04_breakout_proximity_headroom_126d_jerk_v032_signal(closeadj):
    g = _dist_high(closeadj, 126)
    typ = g.rolling(126, min_periods=63).mean()
    base = g / typ.replace(0, np.nan) - 1.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of headroom 252d breakout-proximity base
def f04bp_f04_breakout_proximity_headroom_252d_jerk_v033_signal(closeadj):
    g = _dist_high(closeadj, 252)
    typ = g.rolling(252, min_periods=126).mean()
    base = g / typ.replace(0, np.nan) - 1.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of cushion 63d breakout-proximity base
def f04bp_f04_breakout_proximity_cushion_63d_jerk_v034_signal(closeadj):
    g = _dist_low(closeadj, 63)
    typ = g.rolling(63, min_periods=21).mean()
    base = g / typ.replace(0, np.nan) - 1.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of cushion 126d breakout-proximity base
def f04bp_f04_breakout_proximity_cushion_126d_jerk_v035_signal(closeadj):
    g = _dist_low(closeadj, 126)
    typ = g.rolling(126, min_periods=63).mean()
    base = g / typ.replace(0, np.nan) - 1.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of cushion 252d breakout-proximity base
def f04bp_f04_breakout_proximity_cushion_252d_jerk_v036_signal(closeadj):
    g = _dist_low(closeadj, 252)
    typ = g.rolling(126, min_periods=63).mean()
    base = g / typ.replace(0, np.nan) - 1.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of brkasym 126d breakout-proximity base
def f04bp_f04_breakout_proximity_brkasym_126d_jerk_v037_signal(closeadj):
    base = _headroom_high(closeadj, 126) - _cushion_low(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of brkasym 252d breakout-proximity base
def f04bp_f04_breakout_proximity_brkasym_252d_jerk_v038_signal(closeadj):
    base = _headroom_high(closeadj, 252) - _cushion_low(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsh 63d breakout-proximity base
def f04bp_f04_breakout_proximity_dsh_63d_jerk_v039_signal(closeadj):
    base = _days_since_high(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsh 126d breakout-proximity base
def f04bp_f04_breakout_proximity_dsh_126d_jerk_v040_signal(closeadj):
    base = _days_since_high(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsh 252d breakout-proximity base
def f04bp_f04_breakout_proximity_dsh_252d_jerk_v041_signal(closeadj):
    base = _days_since_high(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsl 63d breakout-proximity base
def f04bp_f04_breakout_proximity_dsl_63d_jerk_v042_signal(closeadj):
    base = _days_since_low(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsl 126d breakout-proximity base
def f04bp_f04_breakout_proximity_dsl_126d_jerk_v043_signal(closeadj):
    base = _days_since_low(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsl 252d breakout-proximity base
def f04bp_f04_breakout_proximity_dsl_252d_jerk_v044_signal(closeadj):
    base = _days_since_low(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsbal 252d breakout-proximity base
def f04bp_f04_breakout_proximity_dsbal_252d_jerk_v045_signal(closeadj):
    base = _days_since_low(closeadj, 252) - _days_since_high(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of dsbal 504d breakout-proximity base
def f04bp_f04_breakout_proximity_dsbal_504d_jerk_v046_signal(closeadj):
    base = _days_since_low(closeadj, 504) - _days_since_high(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dshdd 252d breakout-proximity base
def f04bp_f04_breakout_proximity_dshdd_252d_jerk_v047_signal(closeadj):
    base = _days_since_high(closeadj, 252) * _dist_high(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of dsldd 252d breakout-proximity base
def f04bp_f04_breakout_proximity_dsldd_252d_jerk_v048_signal(closeadj):
    base = _days_since_low(closeadj, 252) * _dist_low(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanwid 63d breakout-proximity base
def f04bp_f04_breakout_proximity_chanwid_63d_jerk_v049_signal(closeadj):
    base = _chan_width(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanwid 252d breakout-proximity base
def f04bp_f04_breakout_proximity_chanwid_252d_jerk_v050_signal(closeadj):
    base = _chan_width(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of squeeze 63d breakout-proximity base
def f04bp_f04_breakout_proximity_squeeze_63d_jerk_v051_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 63, 252)
    base = _z(sr, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of squeeze 126d breakout-proximity base
def f04bp_f04_breakout_proximity_squeeze_126d_jerk_v052_signal(closeadj):
    base = _squeeze_ratio(closeadj, 126, 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 5d ROC) of squeezelog 21d breakout-proximity base
def f04bp_f04_breakout_proximity_squeezelog_21d_jerk_v053_signal(closeadj):
    base = np.log(_squeeze_ratio(closeadj, 21, 126).replace(0, np.nan))
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of widchg 126d breakout-proximity base
def f04bp_f04_breakout_proximity_widchg_126d_jerk_v054_signal(closeadj):
    cw = _chan_width(closeadj, 126)
    base = cw - cw.shift(63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of widchg 252d breakout-proximity base
def f04bp_f04_breakout_proximity_widchg_252d_jerk_v055_signal(closeadj):
    cw = _chan_width(closeadj, 252)
    base = cw - cw.shift(63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of sqzbreak 63d breakout-proximity base
def f04bp_f04_breakout_proximity_sqzbreak_63d_jerk_v056_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 63, 252)
    tight = (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    base = tight * _headroom_high(closeadj, 63).clip(lower=0)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of sqzbreak 126d breakout-proximity base
def f04bp_f04_breakout_proximity_sqzbreak_126d_jerk_v057_signal(closeadj):
    sr = _squeeze_ratio(closeadj, 126, 504)
    tight = (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    base = tight * _headroom_high(closeadj, 126).clip(lower=0)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of gapsqz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_gapsqz_252d_jerk_v058_signal(closeadj):
    g = _dist_high(closeadj, 252)
    sr = _squeeze_ratio(closeadj, 63, 252)
    base = g * (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of gapsqz 504d breakout-proximity base
def f04bp_f04_breakout_proximity_gapsqz_504d_jerk_v059_signal(closeadj):
    g = _dist_high(closeadj, 504)
    sr = _squeeze_ratio(closeadj, 126, 504)
    base = g * (1.0 / sr.replace(0, np.nan)).clip(upper=5.0)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midskew 63d breakout-proximity base
def f04bp_f04_breakout_proximity_midskew_63d_jerk_v060_signal(closeadj):
    base = _mid_skew(closeadj, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midskew 126d breakout-proximity base
def f04bp_f04_breakout_proximity_midskew_126d_jerk_v061_signal(closeadj):
    base = _mid_skew(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midskew 252d breakout-proximity base
def f04bp_f04_breakout_proximity_midskew_252d_jerk_v062_signal(closeadj):
    base = _mid_skew(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of midskew 504d breakout-proximity base
def f04bp_f04_breakout_proximity_midskew_504d_jerk_v063_signal(closeadj):
    base = _mid_skew(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midconvex 126d breakout-proximity base
def f04bp_f04_breakout_proximity_midconvex_126d_jerk_v064_signal(closeadj):
    m = _mid_skew(closeadj, 126)
    base = np.sign(m) * (m * m) * 4.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midconvex 252d breakout-proximity base
def f04bp_f04_breakout_proximity_midconvex_252d_jerk_v065_signal(closeadj):
    m = _mid_skew(closeadj, 252)
    base = np.sign(m) * (m * m) * 4.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hiclimb 126d breakout-proximity base
def f04bp_f04_breakout_proximity_hiclimb_126d_jerk_v066_signal(closeadj):
    base = _high_climb(closeadj, 126, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hiclimb 252d breakout-proximity base
def f04bp_f04_breakout_proximity_hiclimb_252d_jerk_v067_signal(closeadj):
    base = _high_climb(closeadj, 252, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of hiclimb 504d breakout-proximity base
def f04bp_f04_breakout_proximity_hiclimb_504d_jerk_v068_signal(closeadj):
    base = _high_climb(closeadj, 504, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of lolift 126d breakout-proximity base
def f04bp_f04_breakout_proximity_lolift_126d_jerk_v069_signal(closeadj):
    base = _low_lift(closeadj, 126, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of lolift 252d breakout-proximity base
def f04bp_f04_breakout_proximity_lolift_252d_jerk_v070_signal(closeadj):
    base = _low_lift(closeadj, 252, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of lolift 504d breakout-proximity base
def f04bp_f04_breakout_proximity_lolift_504d_jerk_v071_signal(closeadj):
    base = _low_lift(closeadj, 504, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanslopebal 126d breakout-proximity base
def f04bp_f04_breakout_proximity_chanslopebal_126d_jerk_v072_signal(closeadj):
    base = _high_climb(closeadj, 126, 21) - _low_lift(closeadj, 126, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanslopebal 252d breakout-proximity base
def f04bp_f04_breakout_proximity_chanslopebal_252d_jerk_v073_signal(closeadj):
    base = _high_climb(closeadj, 252, 63) - _low_lift(closeadj, 252, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of gapatr 126d breakout-proximity base
def f04bp_f04_breakout_proximity_gapatr_126d_jerk_v074_signal(closeadj, high, low):
    hi = _rmax(closeadj, 126)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - hi) / atr.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of gapatr 252d breakout-proximity base
def f04bp_f04_breakout_proximity_gapatr_252d_jerk_v075_signal(closeadj, high, low):
    hi = _rmax(closeadj, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - hi) / atr.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of lgapatr 126d breakout-proximity base
def f04bp_f04_breakout_proximity_lgapatr_126d_jerk_v076_signal(closeadj, high, low):
    lo = _rmin(closeadj, 126)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - lo) / atr.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of lgapatr 252d breakout-proximity base
def f04bp_f04_breakout_proximity_lgapatr_252d_jerk_v077_signal(closeadj, high, low):
    lo = _rmin(closeadj, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - lo) / atr.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of edgeconvex 126d breakout-proximity base
def f04bp_f04_breakout_proximity_edgeconvex_126d_jerk_v078_signal(closeadj):
    e = (_donch_pos(closeadj, 126) - 0.5).abs() * 2.0
    base = e * e
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of edgeconvex 252d breakout-proximity base
def f04bp_f04_breakout_proximity_edgeconvex_252d_jerk_v079_signal(closeadj):
    e = (_donch_pos(closeadj, 252) - 0.5).abs() * 2.0
    base = e * e
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of edgeconvex 504d breakout-proximity base
def f04bp_f04_breakout_proximity_edgeconvex_504d_jerk_v080_signal(closeadj):
    e = (_donch_pos(closeadj, 504) - 0.5).abs() * 2.0
    base = e * e
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of stickytop 252d breakout-proximity base
def f04bp_f04_breakout_proximity_stickytop_252d_jerk_v081_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    persist = (p >= 0.8).astype(float).rolling(63, min_periods=21).mean()
    base = p * persist
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of stickybot 252d breakout-proximity base
def f04bp_f04_breakout_proximity_stickybot_252d_jerk_v082_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    persist = (p <= 0.2).astype(float).rolling(63, min_periods=21).mean()
    base = (p - 0.5) * persist
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of nearhi 252d breakout-proximity base
def f04bp_f04_breakout_proximity_nearhi_252d_jerk_v083_signal(closeadj):
    hi = _rmax(closeadj, 252)
    excess = (closeadj / hi.replace(0, np.nan) - 0.95).clip(lower=0)
    base = excess.rolling(126, min_periods=63).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of nearlo 252d breakout-proximity base
def f04bp_f04_breakout_proximity_nearlo_252d_jerk_v084_signal(closeadj):
    lo = _rmin(closeadj, 252)
    excess = (1.05 - closeadj / lo.replace(0, np.nan)).clip(lower=0)
    base = excess.rolling(126, min_periods=63).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of multidisp 252d breakout-proximity base
def f04bp_f04_breakout_proximity_multidisp_252d_jerk_v085_signal(closeadj):
    p1 = _donch_pos(closeadj, 63)
    p2 = _donch_pos(closeadj, 126)
    p3 = _donch_pos(closeadj, 252)
    base = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of multidisp 504d breakout-proximity base
def f04bp_f04_breakout_proximity_multidisp_504d_jerk_v086_signal(closeadj):
    p1 = _donch_pos(closeadj, 126)
    p2 = _donch_pos(closeadj, 252)
    p3 = _donch_pos(closeadj, 504)
    base = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of multiprox 252d breakout-proximity base
def f04bp_f04_breakout_proximity_multiprox_252d_jerk_v087_signal(closeadj):
    h1 = _rmax(closeadj, 63)
    h2 = _rmax(closeadj, 126)
    h3 = _rmax(closeadj, 252)
    p1 = closeadj / h1.replace(0, np.nan)
    p2 = closeadj / h2.replace(0, np.nan)
    p3 = closeadj / h3.replace(0, np.nan)
    st = pd.concat([p1, p2, p3], axis=1)
    base = st.max(axis=1) - st.min(axis=1)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanbreadth 252d breakout-proximity base
def f04bp_f04_breakout_proximity_chanbreadth_252d_jerk_v088_signal(closeadj):
    p1 = _donch_pos(closeadj, 63) - 0.5
    p2 = _donch_pos(closeadj, 126) - 0.5
    p3 = _donch_pos(closeadj, 252) - 0.5
    mn = (p1 + p2 + p3) / 3.0
    base = np.sign(mn) * (p1.abs() * p2.abs() * p3.abs()) ** (1.0 / 3.0)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposmom 63d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposmom_63d_jerk_v089_signal(closeadj):
    p = _donch_pos(closeadj, 63)
    base = p - p.shift(21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposmom 126d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposmom_126d_jerk_v090_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    base = p - p.shift(21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposmom 252d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposmom_252d_jerk_v091_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    base = p - p.shift(63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthimom 252d breakout-proximity base
def f04bp_f04_breakout_proximity_disthimom_252d_jerk_v092_signal(closeadj):
    g = _dist_high(closeadj, 252)
    base = g - g.shift(21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of disthimom 504d breakout-proximity base
def f04bp_f04_breakout_proximity_disthimom_504d_jerk_v093_signal(closeadj):
    g = _dist_high(closeadj, 504)
    base = g - g.shift(63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of postanh 126d breakout-proximity base
def f04bp_f04_breakout_proximity_postanh_126d_jerk_v094_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    base = np.tanh(5.0 * (p - p.shift(21)))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of postanh 252d breakout-proximity base
def f04bp_f04_breakout_proximity_postanh_252d_jerk_v095_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    base = np.tanh(5.0 * (p - p.shift(63)))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of gapsignmag 252d breakout-proximity base
def f04bp_f04_breakout_proximity_gapsignmag_252d_jerk_v096_signal(closeadj):
    g = _dist_high(closeadj, 252)
    base = np.sign(g) * (g.abs() ** 0.5)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of lgapsignmag 252d breakout-proximity base
def f04bp_f04_breakout_proximity_lgapsignmag_252d_jerk_v097_signal(closeadj):
    g = _dist_low(closeadj, 252)
    base = np.sign(g) * (g.abs() ** 0.5)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of gapvol 252d breakout-proximity base
def f04bp_f04_breakout_proximity_gapvol_252d_jerk_v098_signal(closeadj):
    g = _dist_high(closeadj, 252)
    vs = closeadj.pct_change().rolling(21, min_periods=10).std()
    vl = closeadj.pct_change().rolling(126, min_periods=63).std()
    base = g * (vs / vl.replace(0, np.nan))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posvol 63d breakout-proximity base
def f04bp_f04_breakout_proximity_posvol_63d_jerk_v099_signal(closeadj, volume):
    p = _donch_pos(closeadj, 63)
    base = (p - 0.5) * _z(volume, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posvol 126d breakout-proximity base
def f04bp_f04_breakout_proximity_posvol_126d_jerk_v100_signal(closeadj, volume):
    p = _donch_pos(closeadj, 126)
    base = (p - 0.5) * _z(volume, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posdvol 126d breakout-proximity base
def f04bp_f04_breakout_proximity_posdvol_126d_jerk_v101_signal(closeadj, volume):
    p = _donch_pos(closeadj, 126)
    dv = closeadj * volume
    base = (p - 0.5) * _z(dv, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posdvol 252d breakout-proximity base
def f04bp_f04_breakout_proximity_posdvol_252d_jerk_v102_signal(closeadj, volume):
    p = _donch_pos(closeadj, 252)
    dv = closeadj * volume
    base = (p - 0.5) * _z(dv, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposema 126d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposema_126d_jerk_v103_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    base = p.ewm(span=42, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of donchposema 252d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposema_252d_jerk_v104_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    base = p.ewm(span=63, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posrank 126d breakout-proximity base
def f04bp_f04_breakout_proximity_posrank_126d_jerk_v105_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    base = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posrank 252d breakout-proximity base
def f04bp_f04_breakout_proximity_posrank_252d_jerk_v106_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    base = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthirk 252d breakout-proximity base
def f04bp_f04_breakout_proximity_disthirk_252d_jerk_v107_signal(closeadj):
    g = _dist_high(closeadj, 252)
    base = g.rolling(252, min_periods=63).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlork 252d breakout-proximity base
def f04bp_f04_breakout_proximity_distlork_252d_jerk_v108_signal(closeadj):
    g = _dist_low(closeadj, 252)
    base = g.rolling(252, min_periods=63).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of midskewsm 504d breakout-proximity base
def f04bp_f04_breakout_proximity_midskewsm_504d_jerk_v109_signal(closeadj):
    m = _mid_skew(closeadj, 504)
    base = m.ewm(span=21, min_periods=10).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of widrk126 126d breakout-proximity base
def f04bp_f04_breakout_proximity_widrk126_126d_jerk_v110_signal(closeadj):
    cw = _chan_width(closeadj, 126)
    base = cw.rolling(252, min_periods=63).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlork126 126d breakout-proximity base
def f04bp_f04_breakout_proximity_distlork126_126d_jerk_v111_signal(closeadj):
    g = _dist_low(closeadj, 126)
    base = g.rolling(252, min_periods=63).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hldonchz 63d breakout-proximity base
def f04bp_f04_breakout_proximity_hldonchz_63d_jerk_v112_signal(closeadj, high, low):
    g = _donch_pos_hl(closeadj, high, low, 63) - _donch_pos(closeadj, 63)
    base = _z(g, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hldonchz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_hldonchz_252d_jerk_v113_signal(closeadj, high, low):
    g = _donch_pos_hl(closeadj, high, low, 252) - _donch_pos(closeadj, 252)
    base = _z(g, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hldonchrk 126d breakout-proximity base
def f04bp_f04_breakout_proximity_hldonchrk_126d_jerk_v114_signal(closeadj, high, low):
    p = _donch_pos_hl(closeadj, high, low, 126)
    base = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of truehead 252d breakout-proximity base
def f04bp_f04_breakout_proximity_truehead_252d_jerk_v115_signal(closeadj, high):
    prior_hi = high.shift(1).rolling(252, min_periods=126).max()
    raw = closeadj / prior_hi.replace(0, np.nan) - 1.0
    base = _z(raw, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of truecush 252d breakout-proximity base
def f04bp_f04_breakout_proximity_truecush_252d_jerk_v116_signal(closeadj, low):
    prior_lo = low.shift(1).rolling(252, min_periods=126).min()
    raw = closeadj / prior_lo.replace(0, np.nan) - 1.0
    base = _z(raw, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of truehead 504d breakout-proximity base
def f04bp_f04_breakout_proximity_truehead_504d_jerk_v117_signal(closeadj, high):
    prior_hi = high.shift(1).rolling(504, min_periods=252).max()
    raw = closeadj / prior_hi.replace(0, np.nan) - 1.0
    base = _z(raw, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hiextend 252d breakout-proximity base
def f04bp_f04_breakout_proximity_hiextend_252d_jerk_v118_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (hi - mn) / mn.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of loextend 252d breakout-proximity base
def f04bp_f04_breakout_proximity_loextend_252d_jerk_v119_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (mn - lo) / mn.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of hiextend 504d breakout-proximity base
def f04bp_f04_breakout_proximity_hiextend_504d_jerk_v120_signal(closeadj):
    hi = _rmax(closeadj, 504)
    mn = _mean(closeadj, 504)
    base = (hi - mn) / mn.replace(0, np.nan)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of loextend 504d breakout-proximity base
def f04bp_f04_breakout_proximity_loextend_504d_jerk_v121_signal(closeadj):
    lo = _rmin(closeadj, 504)
    mn = _mean(closeadj, 504)
    base = (mn - lo) / mn.replace(0, np.nan)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posaccl 126d breakout-proximity base
def f04bp_f04_breakout_proximity_posaccl_126d_jerk_v122_signal(closeadj):
    p = _donch_pos(closeadj, 126)
    base = (p - p.shift(21)) - (p.shift(21) - p.shift(42))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of posaccl 252d breakout-proximity base
def f04bp_f04_breakout_proximity_posaccl_252d_jerk_v123_signal(closeadj):
    p = _donch_pos(closeadj, 252)
    base = (p - p.shift(21)) - (p.shift(21) - p.shift(63))
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of donchpos504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_donchpos504_504d_jerk_v124_signal(closeadj):
    p = _donch_pos(closeadj, 504)
    base = p - p.ewm(span=126, min_periods=63).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of donchpos1260 1260d breakout-proximity base
def f04bp_f04_breakout_proximity_donchpos1260_1260d_jerk_v125_signal(closeadj):
    base = _donch_pos(closeadj, 1260) - _donch_pos(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthihalf 63d breakout-proximity base
def f04bp_f04_breakout_proximity_disthihalf_63d_jerk_v126_signal(closeadj):
    g = _dist_high(closeadj, 63)
    base = g - g.rolling(21, min_periods=10).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of disthihalf 126d breakout-proximity base
def f04bp_f04_breakout_proximity_disthihalf_126d_jerk_v127_signal(closeadj):
    g = _dist_high(closeadj, 126)
    base = g - g.rolling(42, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlohalf 63d breakout-proximity base
def f04bp_f04_breakout_proximity_distlohalf_63d_jerk_v128_signal(closeadj):
    g = _dist_low(closeadj, 63)
    base = g - g.rolling(21, min_periods=10).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of distlohalf 126d breakout-proximity base
def f04bp_f04_breakout_proximity_distlohalf_126d_jerk_v129_signal(closeadj):
    g = _dist_low(closeadj, 126)
    base = g - g.rolling(42, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midskewz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_midskewz_252d_jerk_v130_signal(closeadj):
    base = _z(_mid_skew(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midskewz 126d breakout-proximity base
def f04bp_f04_breakout_proximity_midskewz_126d_jerk_v131_signal(closeadj):
    base = _z(_mid_skew(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanwidz 252d breakout-proximity base
def f04bp_f04_breakout_proximity_chanwidz_252d_jerk_v132_signal(closeadj):
    base = _z(_chan_width(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of chanwidz 126d breakout-proximity base
def f04bp_f04_breakout_proximity_chanwidz_126d_jerk_v133_signal(closeadj):
    base = _z(_chan_width(closeadj, 126), 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of hiclimbL 252d breakout-proximity base
def f04bp_f04_breakout_proximity_hiclimbL_252d_jerk_v134_signal(closeadj):
    base = _high_climb(closeadj, 252, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of hiclimbL 504d breakout-proximity base
def f04bp_f04_breakout_proximity_hiclimbL_504d_jerk_v135_signal(closeadj):
    base = _high_climb(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of loliftL 252d breakout-proximity base
def f04bp_f04_breakout_proximity_loliftL_252d_jerk_v136_signal(closeadj):
    base = _low_lift(closeadj, 252, 21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of loliftL 504d breakout-proximity base
def f04bp_f04_breakout_proximity_loliftL_504d_jerk_v137_signal(closeadj):
    base = _low_lift(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of gapatr504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_gapatr504_504d_jerk_v138_signal(closeadj, high, low):
    hi = _rmax(closeadj, 504)
    atr = (high - low).rolling(63, min_periods=21).mean()
    r = (closeadj - hi) / atr.replace(0, np.nan)
    base = r.rolling(63, min_periods=21).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of lgapatr504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_lgapatr504_504d_jerk_v139_signal(closeadj, high, low):
    lo = _rmin(closeadj, 504)
    atr = (high - low).rolling(63, min_periods=21).mean()
    r = (closeadj - lo) / atr.replace(0, np.nan)
    base = r.rolling(63, min_periods=21).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of nearhi504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_nearhi504_504d_jerk_v140_signal(closeadj):
    hi = _rmax(closeadj, 504)
    prox = closeadj / hi.replace(0, np.nan)
    base = prox.rolling(126, min_periods=63).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of nearlo504 504d breakout-proximity base
def f04bp_f04_breakout_proximity_nearlo504_504d_jerk_v141_signal(closeadj):
    lo = _rmin(closeadj, 504)
    prox = lo.replace(0, np.nan) / closeadj.replace(0, np.nan)
    base = prox.rolling(126, min_periods=63).mean()
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of amplitude 252d breakout-proximity base
def f04bp_f04_breakout_proximity_amplitude_252d_jerk_v142_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (hi - lo) / mn.replace(0, np.nan)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d ROC) of amplitude 504d breakout-proximity base
def f04bp_f04_breakout_proximity_amplitude_504d_jerk_v143_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mn = _mean(closeadj, 504)
    base = (hi - lo) / mn.replace(0, np.nan)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of tophug 252d breakout-proximity base
def f04bp_f04_breakout_proximity_tophug_252d_jerk_v144_signal(closeadj):
    rp = _donch_pos(closeadj, 252)
    base = np.sign(rp - 0.5) * (rp - 0.5) ** 2 * 4.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of tophug 126d breakout-proximity base
def f04bp_f04_breakout_proximity_tophug_126d_jerk_v145_signal(closeadj):
    rp = _donch_pos(closeadj, 126)
    base = np.sign(rp - 0.5) * (rp - 0.5) ** 2 * 4.0
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of gapyoy 252d breakout-proximity base
def f04bp_f04_breakout_proximity_gapyoy_252d_jerk_v146_signal(closeadj):
    g = _dist_high(closeadj, 252)
    base = g - g.shift(252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of lgapyoy 252d breakout-proximity base
def f04bp_f04_breakout_proximity_lgapyoy_252d_jerk_v147_signal(closeadj):
    g = _dist_low(closeadj, 252)
    base = g - g.shift(252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 5d ROC) of donchposspr2 21d breakout-proximity base
def f04bp_f04_breakout_proximity_donchposspr2_21d_jerk_v148_signal(closeadj):
    base = _donch_pos(closeadj, 21) - _donch_pos(closeadj, 126)
    sl = base.diff(5) / float(5)
    j = sl.diff(5) / float(5)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of midskewmom 252d breakout-proximity base
def f04bp_f04_breakout_proximity_midskewmom_252d_jerk_v149_signal(closeadj):
    m = _mid_skew(closeadj, 252)
    base = m - m.shift(21)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d ROC) of nhfreqprox 252d breakout-proximity base
def f04bp_f04_breakout_proximity_nhfreqprox_252d_jerk_v150_signal(closeadj):
    prox = closeadj / _rmax(closeadj, 252).replace(0, np.nan)
    base = prox.rolling(63, min_periods=21).mean()
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04bp_f04_breakout_proximity_donchpos_21d_jerk_v001_signal,
    f04bp_f04_breakout_proximity_donchpos_63d_jerk_v002_signal,
    f04bp_f04_breakout_proximity_donchpos_126d_jerk_v003_signal,
    f04bp_f04_breakout_proximity_donchpos_252d_jerk_v004_signal,
    f04bp_f04_breakout_proximity_donchposspr_63d_jerk_v005_signal,
    f04bp_f04_breakout_proximity_donchposspr_126d_jerk_v006_signal,
    f04bp_f04_breakout_proximity_donchposspr_252d_jerk_v007_signal,
    f04bp_f04_breakout_proximity_donchposz_63d_jerk_v008_signal,
    f04bp_f04_breakout_proximity_donchposz_126d_jerk_v009_signal,
    f04bp_f04_breakout_proximity_donchposz_252d_jerk_v010_signal,
    f04bp_f04_breakout_proximity_donchposdisp_126d_jerk_v011_signal,
    f04bp_f04_breakout_proximity_donchposdisp_252d_jerk_v012_signal,
    f04bp_f04_breakout_proximity_hlclosegap_63d_jerk_v013_signal,
    f04bp_f04_breakout_proximity_hlclosegap_126d_jerk_v014_signal,
    f04bp_f04_breakout_proximity_hlclosegap_252d_jerk_v015_signal,
    f04bp_f04_breakout_proximity_disthi_21d_jerk_v016_signal,
    f04bp_f04_breakout_proximity_disthi_63d_jerk_v017_signal,
    f04bp_f04_breakout_proximity_disthi_126d_jerk_v018_signal,
    f04bp_f04_breakout_proximity_disthi_252d_jerk_v019_signal,
    f04bp_f04_breakout_proximity_disthimr504_504d_jerk_v020_signal,
    f04bp_f04_breakout_proximity_disthimr1260_1260d_jerk_v021_signal,
    f04bp_f04_breakout_proximity_disthiz_126d_jerk_v022_signal,
    f04bp_f04_breakout_proximity_disthiz_252d_jerk_v023_signal,
    f04bp_f04_breakout_proximity_distlo_21d_jerk_v024_signal,
    f04bp_f04_breakout_proximity_distlo_63d_jerk_v025_signal,
    f04bp_f04_breakout_proximity_distlo_126d_jerk_v026_signal,
    f04bp_f04_breakout_proximity_distlo_252d_jerk_v027_signal,
    f04bp_f04_breakout_proximity_distlomr504_504d_jerk_v028_signal,
    f04bp_f04_breakout_proximity_distloz_126d_jerk_v029_signal,
    f04bp_f04_breakout_proximity_distloz_252d_jerk_v030_signal,
    f04bp_f04_breakout_proximity_headroom_63d_jerk_v031_signal,
    f04bp_f04_breakout_proximity_headroom_126d_jerk_v032_signal,
    f04bp_f04_breakout_proximity_headroom_252d_jerk_v033_signal,
    f04bp_f04_breakout_proximity_cushion_63d_jerk_v034_signal,
    f04bp_f04_breakout_proximity_cushion_126d_jerk_v035_signal,
    f04bp_f04_breakout_proximity_cushion_252d_jerk_v036_signal,
    f04bp_f04_breakout_proximity_brkasym_126d_jerk_v037_signal,
    f04bp_f04_breakout_proximity_brkasym_252d_jerk_v038_signal,
    f04bp_f04_breakout_proximity_dsh_63d_jerk_v039_signal,
    f04bp_f04_breakout_proximity_dsh_126d_jerk_v040_signal,
    f04bp_f04_breakout_proximity_dsh_252d_jerk_v041_signal,
    f04bp_f04_breakout_proximity_dsl_63d_jerk_v042_signal,
    f04bp_f04_breakout_proximity_dsl_126d_jerk_v043_signal,
    f04bp_f04_breakout_proximity_dsl_252d_jerk_v044_signal,
    f04bp_f04_breakout_proximity_dsbal_252d_jerk_v045_signal,
    f04bp_f04_breakout_proximity_dsbal_504d_jerk_v046_signal,
    f04bp_f04_breakout_proximity_dshdd_252d_jerk_v047_signal,
    f04bp_f04_breakout_proximity_dsldd_252d_jerk_v048_signal,
    f04bp_f04_breakout_proximity_chanwid_63d_jerk_v049_signal,
    f04bp_f04_breakout_proximity_chanwid_252d_jerk_v050_signal,
    f04bp_f04_breakout_proximity_squeeze_63d_jerk_v051_signal,
    f04bp_f04_breakout_proximity_squeeze_126d_jerk_v052_signal,
    f04bp_f04_breakout_proximity_squeezelog_21d_jerk_v053_signal,
    f04bp_f04_breakout_proximity_widchg_126d_jerk_v054_signal,
    f04bp_f04_breakout_proximity_widchg_252d_jerk_v055_signal,
    f04bp_f04_breakout_proximity_sqzbreak_63d_jerk_v056_signal,
    f04bp_f04_breakout_proximity_sqzbreak_126d_jerk_v057_signal,
    f04bp_f04_breakout_proximity_gapsqz_252d_jerk_v058_signal,
    f04bp_f04_breakout_proximity_gapsqz_504d_jerk_v059_signal,
    f04bp_f04_breakout_proximity_midskew_63d_jerk_v060_signal,
    f04bp_f04_breakout_proximity_midskew_126d_jerk_v061_signal,
    f04bp_f04_breakout_proximity_midskew_252d_jerk_v062_signal,
    f04bp_f04_breakout_proximity_midskew_504d_jerk_v063_signal,
    f04bp_f04_breakout_proximity_midconvex_126d_jerk_v064_signal,
    f04bp_f04_breakout_proximity_midconvex_252d_jerk_v065_signal,
    f04bp_f04_breakout_proximity_hiclimb_126d_jerk_v066_signal,
    f04bp_f04_breakout_proximity_hiclimb_252d_jerk_v067_signal,
    f04bp_f04_breakout_proximity_hiclimb_504d_jerk_v068_signal,
    f04bp_f04_breakout_proximity_lolift_126d_jerk_v069_signal,
    f04bp_f04_breakout_proximity_lolift_252d_jerk_v070_signal,
    f04bp_f04_breakout_proximity_lolift_504d_jerk_v071_signal,
    f04bp_f04_breakout_proximity_chanslopebal_126d_jerk_v072_signal,
    f04bp_f04_breakout_proximity_chanslopebal_252d_jerk_v073_signal,
    f04bp_f04_breakout_proximity_gapatr_126d_jerk_v074_signal,
    f04bp_f04_breakout_proximity_gapatr_252d_jerk_v075_signal,
    f04bp_f04_breakout_proximity_lgapatr_126d_jerk_v076_signal,
    f04bp_f04_breakout_proximity_lgapatr_252d_jerk_v077_signal,
    f04bp_f04_breakout_proximity_edgeconvex_126d_jerk_v078_signal,
    f04bp_f04_breakout_proximity_edgeconvex_252d_jerk_v079_signal,
    f04bp_f04_breakout_proximity_edgeconvex_504d_jerk_v080_signal,
    f04bp_f04_breakout_proximity_stickytop_252d_jerk_v081_signal,
    f04bp_f04_breakout_proximity_stickybot_252d_jerk_v082_signal,
    f04bp_f04_breakout_proximity_nearhi_252d_jerk_v083_signal,
    f04bp_f04_breakout_proximity_nearlo_252d_jerk_v084_signal,
    f04bp_f04_breakout_proximity_multidisp_252d_jerk_v085_signal,
    f04bp_f04_breakout_proximity_multidisp_504d_jerk_v086_signal,
    f04bp_f04_breakout_proximity_multiprox_252d_jerk_v087_signal,
    f04bp_f04_breakout_proximity_chanbreadth_252d_jerk_v088_signal,
    f04bp_f04_breakout_proximity_donchposmom_63d_jerk_v089_signal,
    f04bp_f04_breakout_proximity_donchposmom_126d_jerk_v090_signal,
    f04bp_f04_breakout_proximity_donchposmom_252d_jerk_v091_signal,
    f04bp_f04_breakout_proximity_disthimom_252d_jerk_v092_signal,
    f04bp_f04_breakout_proximity_disthimom_504d_jerk_v093_signal,
    f04bp_f04_breakout_proximity_postanh_126d_jerk_v094_signal,
    f04bp_f04_breakout_proximity_postanh_252d_jerk_v095_signal,
    f04bp_f04_breakout_proximity_gapsignmag_252d_jerk_v096_signal,
    f04bp_f04_breakout_proximity_lgapsignmag_252d_jerk_v097_signal,
    f04bp_f04_breakout_proximity_gapvol_252d_jerk_v098_signal,
    f04bp_f04_breakout_proximity_posvol_63d_jerk_v099_signal,
    f04bp_f04_breakout_proximity_posvol_126d_jerk_v100_signal,
    f04bp_f04_breakout_proximity_posdvol_126d_jerk_v101_signal,
    f04bp_f04_breakout_proximity_posdvol_252d_jerk_v102_signal,
    f04bp_f04_breakout_proximity_donchposema_126d_jerk_v103_signal,
    f04bp_f04_breakout_proximity_donchposema_252d_jerk_v104_signal,
    f04bp_f04_breakout_proximity_posrank_126d_jerk_v105_signal,
    f04bp_f04_breakout_proximity_posrank_252d_jerk_v106_signal,
    f04bp_f04_breakout_proximity_disthirk_252d_jerk_v107_signal,
    f04bp_f04_breakout_proximity_distlork_252d_jerk_v108_signal,
    f04bp_f04_breakout_proximity_midskewsm_504d_jerk_v109_signal,
    f04bp_f04_breakout_proximity_widrk126_126d_jerk_v110_signal,
    f04bp_f04_breakout_proximity_distlork126_126d_jerk_v111_signal,
    f04bp_f04_breakout_proximity_hldonchz_63d_jerk_v112_signal,
    f04bp_f04_breakout_proximity_hldonchz_252d_jerk_v113_signal,
    f04bp_f04_breakout_proximity_hldonchrk_126d_jerk_v114_signal,
    f04bp_f04_breakout_proximity_truehead_252d_jerk_v115_signal,
    f04bp_f04_breakout_proximity_truecush_252d_jerk_v116_signal,
    f04bp_f04_breakout_proximity_truehead_504d_jerk_v117_signal,
    f04bp_f04_breakout_proximity_hiextend_252d_jerk_v118_signal,
    f04bp_f04_breakout_proximity_loextend_252d_jerk_v119_signal,
    f04bp_f04_breakout_proximity_hiextend_504d_jerk_v120_signal,
    f04bp_f04_breakout_proximity_loextend_504d_jerk_v121_signal,
    f04bp_f04_breakout_proximity_posaccl_126d_jerk_v122_signal,
    f04bp_f04_breakout_proximity_posaccl_252d_jerk_v123_signal,
    f04bp_f04_breakout_proximity_donchpos504_504d_jerk_v124_signal,
    f04bp_f04_breakout_proximity_donchpos1260_1260d_jerk_v125_signal,
    f04bp_f04_breakout_proximity_disthihalf_63d_jerk_v126_signal,
    f04bp_f04_breakout_proximity_disthihalf_126d_jerk_v127_signal,
    f04bp_f04_breakout_proximity_distlohalf_63d_jerk_v128_signal,
    f04bp_f04_breakout_proximity_distlohalf_126d_jerk_v129_signal,
    f04bp_f04_breakout_proximity_midskewz_252d_jerk_v130_signal,
    f04bp_f04_breakout_proximity_midskewz_126d_jerk_v131_signal,
    f04bp_f04_breakout_proximity_chanwidz_252d_jerk_v132_signal,
    f04bp_f04_breakout_proximity_chanwidz_126d_jerk_v133_signal,
    f04bp_f04_breakout_proximity_hiclimbL_252d_jerk_v134_signal,
    f04bp_f04_breakout_proximity_hiclimbL_504d_jerk_v135_signal,
    f04bp_f04_breakout_proximity_loliftL_252d_jerk_v136_signal,
    f04bp_f04_breakout_proximity_loliftL_504d_jerk_v137_signal,
    f04bp_f04_breakout_proximity_gapatr504_504d_jerk_v138_signal,
    f04bp_f04_breakout_proximity_lgapatr504_504d_jerk_v139_signal,
    f04bp_f04_breakout_proximity_nearhi504_504d_jerk_v140_signal,
    f04bp_f04_breakout_proximity_nearlo504_504d_jerk_v141_signal,
    f04bp_f04_breakout_proximity_amplitude_252d_jerk_v142_signal,
    f04bp_f04_breakout_proximity_amplitude_504d_jerk_v143_signal,
    f04bp_f04_breakout_proximity_tophug_252d_jerk_v144_signal,
    f04bp_f04_breakout_proximity_tophug_126d_jerk_v145_signal,
    f04bp_f04_breakout_proximity_gapyoy_252d_jerk_v146_signal,
    f04bp_f04_breakout_proximity_lgapyoy_252d_jerk_v147_signal,
    f04bp_f04_breakout_proximity_donchposspr2_21d_jerk_v148_signal,
    f04bp_f04_breakout_proximity_midskewmom_252d_jerk_v149_signal,
    f04bp_f04_breakout_proximity_nhfreqprox_252d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_BREAKOUT_PROXIMITY_REGISTRY_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f04_breakout_proximity_3rd_derivatives_001_150_claude: %d features pass" % n_features)
