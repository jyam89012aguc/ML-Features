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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _prox_high(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / hi.replace(0, np.nan)


def _prox_low(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / lo.replace(0, np.nan)


def _range_pos(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


def _drawdown(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / hi.replace(0, np.nan) - 1.0


def _recovery(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / lo.replace(0, np.nan) - 1.0


def _anchor_gap(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _midskew(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    mid = (hi + lo) / 2.0
    return (close - mid) / (hi - lo).replace(0, np.nan)


def _amplitude(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / close.replace(0, np.nan)


def _days_since_high(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _days_since_low(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _hiclimb(close, w, k):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(hi.replace(0, np.nan) / hi.shift(k).replace(0, np.nan))


def _loclimb(close, w, k):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(lo.replace(0, np.nan) / lo.shift(k).replace(0, np.nan))


def _gapdisp(close, w, dw):
    g = _anchor_gap(close, w)
    return g.rolling(dw, min_periods=max(1, dw // 2)).std()


def _rngdisp(close, w, dw):
    rp = _range_pos(close, w)
    return rp.rolling(dw, min_periods=max(1, dw // 2)).std()


def _abovemid(close, w, dw):
    rp = _range_pos(close, w)
    above = (rp >= 0.5).astype(float)
    return above.rolling(dw, min_periods=max(1, dw // 2)).mean()


def _ddfreq(close, w, dw, thr):
    dd = _drawdown(close, w)
    ind = (dd <= thr).astype(float)
    return ind.rolling(dw, min_periods=max(1, dw // 2)).mean()


def _proxrank(close, w, rw):
    p = _prox_high(close, w)
    return p.rolling(rw, min_periods=max(1, rw // 4)).rank(pct=True) - 0.5


def _rngrank(close, w, rw):
    rp = _range_pos(close, w)
    return rp.rolling(rw, min_periods=max(1, rw // 4)).rank(pct=True) - 0.5


def _recovrank(close, w, rw):
    rec = _recovery(close, w)
    return rec.rolling(rw, min_periods=max(1, rw // 4)).rank(pct=True) - 0.5

def f05fw_f05_fiftytwo_week_anchor_rngpos_126d_jerk_v001_signal(closeadj):
    base = _range_pos(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngpos_126d_jerk_v002_signal(closeadj):
    base = _range_pos(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngpos_252d_jerk_v003_signal(closeadj):
    base = _range_pos(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngpos_252d_jerk_v004_signal(closeadj):
    base = _range_pos(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngpos_504d_jerk_v005_signal(closeadj):
    base = _range_pos(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngpos_504d_jerk_v006_signal(closeadj):
    base = _range_pos(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhiz_126d_jerk_v007_signal(closeadj):
    base = _z(_prox_high(closeadj, 126), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhiz_126d_jerk_v008_signal(closeadj):
    base = _z(_prox_high(closeadj, 126), 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhiz_252d_jerk_v009_signal(closeadj):
    base = _z(_prox_high(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhiz_504d_jerk_v010_signal(closeadj):
    base = _z(_prox_high(closeadj, 504), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhiz_504d_jerk_v011_signal(closeadj):
    base = _z(_prox_high(closeadj, 504), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_126d_jerk_v012_signal(closeadj):
    base = _z(_prox_low(closeadj, 126), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_126d_jerk_v013_signal(closeadj):
    base = _z(_prox_low(closeadj, 126), 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_252d_jerk_v014_signal(closeadj):
    base = _z(_prox_low(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_252d_jerk_v015_signal(closeadj):
    base = _z(_prox_low(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_504d_jerk_v016_signal(closeadj):
    base = _z(_prox_low(closeadj, 504), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_504d_jerk_v017_signal(closeadj):
    base = _z(_prox_low(closeadj, 504), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_1260d_jerk_v018_signal(closeadj):
    base = _z(_prox_low(closeadj, 1260), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxloz_1260d_jerk_v019_signal(closeadj):
    base = _z(_prox_low(closeadj, 1260), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_126d_jerk_v020_signal(closeadj):
    base = _amplitude(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_126d_jerk_v021_signal(closeadj):
    base = _amplitude(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_252d_jerk_v022_signal(closeadj):
    base = _amplitude(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_252d_jerk_v023_signal(closeadj):
    base = _amplitude(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_504d_jerk_v024_signal(closeadj):
    base = _amplitude(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_504d_jerk_v025_signal(closeadj):
    base = _amplitude(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_amplitude_1260d_jerk_v026_signal(closeadj):
    base = _amplitude(closeadj, 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_126d_jerk_v027_signal(closeadj):
    base = _z(_amplitude(closeadj, 126), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_126d_jerk_v028_signal(closeadj):
    base = _z(_amplitude(closeadj, 126), 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_252d_jerk_v029_signal(closeadj):
    base = _z(_amplitude(closeadj, 252), 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_252d_jerk_v030_signal(closeadj):
    base = _z(_amplitude(closeadj, 252), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_504d_jerk_v031_signal(closeadj):
    base = _z(_amplitude(closeadj, 504), 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_504d_jerk_v032_signal(closeadj):
    base = _z(_amplitude(closeadj, 504), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ampz_1260d_jerk_v033_signal(closeadj):
    base = _z(_amplitude(closeadj, 1260), 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsh_126d_jerk_v034_signal(closeadj):
    base = _days_since_high(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsh_126d_jerk_v035_signal(closeadj):
    base = _days_since_high(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsh_252d_jerk_v036_signal(closeadj):
    base = _days_since_high(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsh_252d_jerk_v037_signal(closeadj):
    base = _days_since_high(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsh_504d_jerk_v038_signal(closeadj):
    base = _days_since_high(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsh_504d_jerk_v039_signal(closeadj):
    base = _days_since_high(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_126d_jerk_v040_signal(closeadj):
    base = _days_since_low(closeadj, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_126d_jerk_v041_signal(closeadj):
    base = _days_since_low(closeadj, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_252d_jerk_v042_signal(closeadj):
    base = _days_since_low(closeadj, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_252d_jerk_v043_signal(closeadj):
    base = _days_since_low(closeadj, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_504d_jerk_v044_signal(closeadj):
    base = _days_since_low(closeadj, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_504d_jerk_v045_signal(closeadj):
    base = _days_since_low(closeadj, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_1260d_jerk_v046_signal(closeadj):
    base = _days_since_low(closeadj, 1260)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_dsl_1260d_jerk_v047_signal(closeadj):
    base = _days_since_low(closeadj, 1260)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimb_126d_jerk_v048_signal(closeadj):
    base = _hiclimb(closeadj, 126, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimb_126d_jerk_v049_signal(closeadj):
    base = _hiclimb(closeadj, 126, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimb_252d_jerk_v050_signal(closeadj):
    base = _hiclimb(closeadj, 252, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimb_252d_jerk_v051_signal(closeadj):
    base = _hiclimb(closeadj, 252, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimb_504d_jerk_v052_signal(closeadj):
    base = _hiclimb(closeadj, 504, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimb_504d_jerk_v053_signal(closeadj):
    base = _hiclimb(closeadj, 504, 63)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimb_126d_jerk_v054_signal(closeadj):
    base = _loclimb(closeadj, 126, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimb_126d_jerk_v055_signal(closeadj):
    base = _loclimb(closeadj, 126, 63)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimb_252d_jerk_v056_signal(closeadj):
    base = _loclimb(closeadj, 252, 63)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimb_252d_jerk_v057_signal(closeadj):
    base = _loclimb(closeadj, 252, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimb_504d_jerk_v058_signal(closeadj):
    base = _loclimb(closeadj, 504, 63)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimb_504d_jerk_v059_signal(closeadj):
    base = _loclimb(closeadj, 504, 63)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimbL_126d_jerk_v060_signal(closeadj):
    base = _hiclimb(closeadj, 126, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimbL_126d_jerk_v061_signal(closeadj):
    base = _hiclimb(closeadj, 126, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimbL_252d_jerk_v062_signal(closeadj):
    base = _hiclimb(closeadj, 252, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimbL_252d_jerk_v063_signal(closeadj):
    base = _hiclimb(closeadj, 252, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimbL_504d_jerk_v064_signal(closeadj):
    base = _hiclimb(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_hiclimbL_504d_jerk_v065_signal(closeadj):
    base = _hiclimb(closeadj, 504, 126)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimbL_126d_jerk_v066_signal(closeadj):
    base = _loclimb(closeadj, 126, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimbL_126d_jerk_v067_signal(closeadj):
    base = _loclimb(closeadj, 126, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimbL_252d_jerk_v068_signal(closeadj):
    base = _loclimb(closeadj, 252, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimbL_252d_jerk_v069_signal(closeadj):
    base = _loclimb(closeadj, 252, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimbL_504d_jerk_v070_signal(closeadj):
    base = _loclimb(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_loclimbL_504d_jerk_v071_signal(closeadj):
    base = _loclimb(closeadj, 504, 126)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdisp_126d_jerk_v072_signal(closeadj):
    base = _gapdisp(closeadj, 126, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdisp_126d_jerk_v073_signal(closeadj):
    base = _gapdisp(closeadj, 126, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdisp_252d_jerk_v074_signal(closeadj):
    base = _gapdisp(closeadj, 252, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdisp_252d_jerk_v075_signal(closeadj):
    base = _gapdisp(closeadj, 252, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdisp_504d_jerk_v076_signal(closeadj):
    base = _gapdisp(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdisp_504d_jerk_v077_signal(closeadj):
    base = _gapdisp(closeadj, 504, 126)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdisp_126d_jerk_v078_signal(closeadj):
    base = _rngdisp(closeadj, 126, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdisp_126d_jerk_v079_signal(closeadj):
    base = _rngdisp(closeadj, 126, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdisp_252d_jerk_v080_signal(closeadj):
    base = _rngdisp(closeadj, 252, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdisp_252d_jerk_v081_signal(closeadj):
    base = _rngdisp(closeadj, 252, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdisp_504d_jerk_v082_signal(closeadj):
    base = _rngdisp(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdisp_504d_jerk_v083_signal(closeadj):
    base = _rngdisp(closeadj, 504, 126)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdispL_126d_jerk_v084_signal(closeadj):
    base = _gapdisp(closeadj, 126, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdispL_126d_jerk_v085_signal(closeadj):
    base = _gapdisp(closeadj, 126, 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdispL_252d_jerk_v086_signal(closeadj):
    base = _gapdisp(closeadj, 252, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdispL_252d_jerk_v087_signal(closeadj):
    base = _gapdisp(closeadj, 252, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdispL_504d_jerk_v088_signal(closeadj):
    base = _gapdisp(closeadj, 504, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_gapdispL_504d_jerk_v089_signal(closeadj):
    base = _gapdisp(closeadj, 504, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdispL_126d_jerk_v090_signal(closeadj):
    base = _rngdisp(closeadj, 126, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdispL_126d_jerk_v091_signal(closeadj):
    base = _rngdisp(closeadj, 126, 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdispL_252d_jerk_v092_signal(closeadj):
    base = _rngdisp(closeadj, 252, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdispL_252d_jerk_v093_signal(closeadj):
    base = _rngdisp(closeadj, 252, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdispL_504d_jerk_v094_signal(closeadj):
    base = _rngdisp(closeadj, 504, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngdispL_504d_jerk_v095_signal(closeadj):
    base = _rngdisp(closeadj, 504, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_126d_jerk_v096_signal(closeadj):
    base = _abovemid(closeadj, 126, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_126d_jerk_v097_signal(closeadj):
    base = _abovemid(closeadj, 126, 126)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_252d_jerk_v098_signal(closeadj):
    base = _abovemid(closeadj, 252, 126)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_252d_jerk_v099_signal(closeadj):
    base = _abovemid(closeadj, 252, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_504d_jerk_v100_signal(closeadj):
    base = _abovemid(closeadj, 504, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_504d_jerk_v101_signal(closeadj):
    base = _abovemid(closeadj, 504, 126)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_1260d_jerk_v102_signal(closeadj):
    base = _abovemid(closeadj, 1260, 126)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemid_1260d_jerk_v103_signal(closeadj):
    base = _abovemid(closeadj, 1260, 126)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_126d_jerk_v104_signal(closeadj):
    base = _abovemid(closeadj, 126, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_126d_jerk_v105_signal(closeadj):
    base = _abovemid(closeadj, 126, 252)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_252d_jerk_v106_signal(closeadj):
    base = _abovemid(closeadj, 252, 252)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_252d_jerk_v107_signal(closeadj):
    base = _abovemid(closeadj, 252, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_504d_jerk_v108_signal(closeadj):
    base = _abovemid(closeadj, 504, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_504d_jerk_v109_signal(closeadj):
    base = _abovemid(closeadj, 504, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_1260d_jerk_v110_signal(closeadj):
    base = _abovemid(closeadj, 1260, 252)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_abovemidL_1260d_jerk_v111_signal(closeadj):
    base = _abovemid(closeadj, 1260, 252)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_126d_jerk_v112_signal(closeadj):
    base = _ddfreq(closeadj, 126, 252, -0.10)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_126d_jerk_v113_signal(closeadj):
    base = _ddfreq(closeadj, 126, 252, -0.10)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_252d_jerk_v114_signal(closeadj):
    base = _ddfreq(closeadj, 252, 252, -0.10)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_252d_jerk_v115_signal(closeadj):
    base = _ddfreq(closeadj, 252, 252, -0.10)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_504d_jerk_v116_signal(closeadj):
    base = _ddfreq(closeadj, 504, 252, -0.10)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_504d_jerk_v117_signal(closeadj):
    base = _ddfreq(closeadj, 504, 252, -0.10)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_1260d_jerk_v118_signal(closeadj):
    base = _ddfreq(closeadj, 1260, 252, -0.10)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq10_1260d_jerk_v119_signal(closeadj):
    base = _ddfreq(closeadj, 1260, 252, -0.10)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_126d_jerk_v120_signal(closeadj):
    base = _ddfreq(closeadj, 126, 252, -0.15)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_126d_jerk_v121_signal(closeadj):
    base = _ddfreq(closeadj, 126, 252, -0.15)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_252d_jerk_v122_signal(closeadj):
    base = _ddfreq(closeadj, 252, 252, -0.15)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_252d_jerk_v123_signal(closeadj):
    base = _ddfreq(closeadj, 252, 252, -0.15)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_504d_jerk_v124_signal(closeadj):
    base = _ddfreq(closeadj, 504, 252, -0.15)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_504d_jerk_v125_signal(closeadj):
    base = _ddfreq(closeadj, 504, 252, -0.15)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_ddfreq15_1260d_jerk_v126_signal(closeadj):
    base = _ddfreq(closeadj, 1260, 252, -0.15)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxrank_126d_jerk_v127_signal(closeadj):
    base = _proxrank(closeadj, 126, 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxrank_126d_jerk_v128_signal(closeadj):
    base = _proxrank(closeadj, 126, 504)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxrank_504d_jerk_v129_signal(closeadj):
    base = _proxrank(closeadj, 504, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngrank_252d_jerk_v130_signal(closeadj):
    base = _rngrank(closeadj, 252, 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngrank_252d_jerk_v131_signal(closeadj):
    base = _rngrank(closeadj, 252, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngrank_504d_jerk_v132_signal(closeadj):
    base = _rngrank(closeadj, 504, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_126d_jerk_v133_signal(closeadj):
    base = _recovrank(closeadj, 126, 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_126d_jerk_v134_signal(closeadj):
    base = _recovrank(closeadj, 126, 504)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_252d_jerk_v135_signal(closeadj):
    base = _recovrank(closeadj, 252, 504)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_252d_jerk_v136_signal(closeadj):
    base = _recovrank(closeadj, 252, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_504d_jerk_v137_signal(closeadj):
    base = _recovrank(closeadj, 504, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_504d_jerk_v138_signal(closeadj):
    base = _recovrank(closeadj, 504, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_1260d_jerk_v139_signal(closeadj):
    base = _recovrank(closeadj, 1260, 504)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_recovrank_1260d_jerk_v140_signal(closeadj):
    base = _recovrank(closeadj, 1260, 504)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngcube_126d_jerk_v141_signal(closeadj):
    base = ((_range_pos(closeadj, 126) - 0.5) ** 3)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngcube_126d_jerk_v142_signal(closeadj):
    base = ((_range_pos(closeadj, 126) - 0.5) ** 3)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngcube_252d_jerk_v143_signal(closeadj):
    base = ((_range_pos(closeadj, 252) - 0.5) ** 3)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngcube_252d_jerk_v144_signal(closeadj):
    base = ((_range_pos(closeadj, 252) - 0.5) ** 3)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngcube_504d_jerk_v145_signal(closeadj):
    base = ((_range_pos(closeadj, 504) - 0.5) ** 3)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_rngcube_504d_jerk_v146_signal(closeadj):
    base = ((_range_pos(closeadj, 504) - 0.5) ** 3)
    sl = base.diff(126) / float(126)
    j = sl.diff(126) / float(126)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhipow_252d_jerk_v147_signal(closeadj):
    base = (_prox_high(closeadj, 252) ** 8)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxhipow_252d_jerk_v148_signal(closeadj):
    base = (_prox_high(closeadj, 252) ** 8)
    sl = base.diff(63) / float(63)
    j = sl.diff(63) / float(63)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxlopow_126d_jerk_v149_signal(closeadj):
    base = (_prox_low(closeadj, 126) ** 8)
    sl = base.diff(21) / float(21)
    j = sl.diff(21) / float(21)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)

def f05fw_f05_fiftytwo_week_anchor_proxlopow_126d_jerk_v150_signal(closeadj):
    base = (_prox_low(closeadj, 126) ** 8)
    sl = base.diff(42) / float(42)
    j = sl.diff(42) / float(42)
    result = j
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05fw_f05_fiftytwo_week_anchor_rngpos_126d_jerk_v001_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_126d_jerk_v002_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_252d_jerk_v003_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_252d_jerk_v004_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_504d_jerk_v005_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_504d_jerk_v006_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhiz_126d_jerk_v007_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhiz_126d_jerk_v008_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhiz_252d_jerk_v009_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhiz_504d_jerk_v010_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhiz_504d_jerk_v011_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_126d_jerk_v012_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_126d_jerk_v013_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_252d_jerk_v014_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_252d_jerk_v015_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_504d_jerk_v016_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_504d_jerk_v017_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_1260d_jerk_v018_signal,
    f05fw_f05_fiftytwo_week_anchor_proxloz_1260d_jerk_v019_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_126d_jerk_v020_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_126d_jerk_v021_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_252d_jerk_v022_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_252d_jerk_v023_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_504d_jerk_v024_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_504d_jerk_v025_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_1260d_jerk_v026_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_126d_jerk_v027_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_126d_jerk_v028_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_252d_jerk_v029_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_252d_jerk_v030_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_504d_jerk_v031_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_504d_jerk_v032_signal,
    f05fw_f05_fiftytwo_week_anchor_ampz_1260d_jerk_v033_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_126d_jerk_v034_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_126d_jerk_v035_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_252d_jerk_v036_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_252d_jerk_v037_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_504d_jerk_v038_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_504d_jerk_v039_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_126d_jerk_v040_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_126d_jerk_v041_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_252d_jerk_v042_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_252d_jerk_v043_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_504d_jerk_v044_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_504d_jerk_v045_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_1260d_jerk_v046_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_1260d_jerk_v047_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_126d_jerk_v048_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_126d_jerk_v049_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_252d_jerk_v050_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_252d_jerk_v051_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_504d_jerk_v052_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_504d_jerk_v053_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_126d_jerk_v054_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_126d_jerk_v055_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_252d_jerk_v056_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_252d_jerk_v057_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_504d_jerk_v058_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_504d_jerk_v059_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimbL_126d_jerk_v060_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimbL_126d_jerk_v061_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimbL_252d_jerk_v062_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimbL_252d_jerk_v063_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimbL_504d_jerk_v064_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimbL_504d_jerk_v065_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimbL_126d_jerk_v066_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimbL_126d_jerk_v067_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimbL_252d_jerk_v068_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimbL_252d_jerk_v069_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimbL_504d_jerk_v070_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimbL_504d_jerk_v071_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_126d_jerk_v072_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_126d_jerk_v073_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_252d_jerk_v074_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_252d_jerk_v075_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_504d_jerk_v076_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_504d_jerk_v077_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdisp_126d_jerk_v078_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdisp_126d_jerk_v079_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdisp_252d_jerk_v080_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdisp_252d_jerk_v081_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdisp_504d_jerk_v082_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdisp_504d_jerk_v083_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdispL_126d_jerk_v084_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdispL_126d_jerk_v085_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdispL_252d_jerk_v086_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdispL_252d_jerk_v087_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdispL_504d_jerk_v088_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdispL_504d_jerk_v089_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdispL_126d_jerk_v090_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdispL_126d_jerk_v091_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdispL_252d_jerk_v092_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdispL_252d_jerk_v093_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdispL_504d_jerk_v094_signal,
    f05fw_f05_fiftytwo_week_anchor_rngdispL_504d_jerk_v095_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_126d_jerk_v096_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_126d_jerk_v097_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_252d_jerk_v098_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_252d_jerk_v099_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_504d_jerk_v100_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_504d_jerk_v101_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_1260d_jerk_v102_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_1260d_jerk_v103_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_126d_jerk_v104_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_126d_jerk_v105_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_252d_jerk_v106_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_252d_jerk_v107_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_504d_jerk_v108_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_504d_jerk_v109_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_1260d_jerk_v110_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemidL_1260d_jerk_v111_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_126d_jerk_v112_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_126d_jerk_v113_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_252d_jerk_v114_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_252d_jerk_v115_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_504d_jerk_v116_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_504d_jerk_v117_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_1260d_jerk_v118_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq10_1260d_jerk_v119_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_126d_jerk_v120_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_126d_jerk_v121_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_252d_jerk_v122_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_252d_jerk_v123_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_504d_jerk_v124_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_504d_jerk_v125_signal,
    f05fw_f05_fiftytwo_week_anchor_ddfreq15_1260d_jerk_v126_signal,
    f05fw_f05_fiftytwo_week_anchor_proxrank_126d_jerk_v127_signal,
    f05fw_f05_fiftytwo_week_anchor_proxrank_126d_jerk_v128_signal,
    f05fw_f05_fiftytwo_week_anchor_proxrank_504d_jerk_v129_signal,
    f05fw_f05_fiftytwo_week_anchor_rngrank_252d_jerk_v130_signal,
    f05fw_f05_fiftytwo_week_anchor_rngrank_252d_jerk_v131_signal,
    f05fw_f05_fiftytwo_week_anchor_rngrank_504d_jerk_v132_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_126d_jerk_v133_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_126d_jerk_v134_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_252d_jerk_v135_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_252d_jerk_v136_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_504d_jerk_v137_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_504d_jerk_v138_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_1260d_jerk_v139_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_1260d_jerk_v140_signal,
    f05fw_f05_fiftytwo_week_anchor_rngcube_126d_jerk_v141_signal,
    f05fw_f05_fiftytwo_week_anchor_rngcube_126d_jerk_v142_signal,
    f05fw_f05_fiftytwo_week_anchor_rngcube_252d_jerk_v143_signal,
    f05fw_f05_fiftytwo_week_anchor_rngcube_252d_jerk_v144_signal,
    f05fw_f05_fiftytwo_week_anchor_rngcube_504d_jerk_v145_signal,
    f05fw_f05_fiftytwo_week_anchor_rngcube_504d_jerk_v146_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhipow_252d_jerk_v147_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhipow_252d_jerk_v148_signal,
    f05fw_f05_fiftytwo_week_anchor_proxlopow_126d_jerk_v149_signal,
    f05fw_f05_fiftytwo_week_anchor_proxlopow_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_FIFTYTWO_WEEK_ANCHOR_REGISTRY_001_150 = REGISTRY


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

    print("OK f05_fiftytwo_week_anchor_3rd_derivatives_001_150_claude: %d features pass" % n_features)
