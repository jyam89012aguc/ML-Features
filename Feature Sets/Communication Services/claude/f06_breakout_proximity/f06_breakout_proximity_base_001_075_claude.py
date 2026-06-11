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


# ===== folder domain primitives (breakout proximity / Donchian) =====
def _f06_donch_pos(price, w):
    # position within the Donchian channel: 0 at lower band, 1 at upper band
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return (price - lo) / (hi - lo).replace(0, np.nan)


def _f06_dist_high(price, w):
    # distance to the N-day high (<=0, breakout when ~0)
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    return price / hi.replace(0, np.nan) - 1.0


def _f06_dist_low(price, w):
    # distance above the N-day low (>=0)
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return price / lo.replace(0, np.nan) - 1.0


def _f06_prior_high(price, w):
    # prior N-day high (excludes today) -> breakout reference
    return price.shift(1).rolling(w, min_periods=max(1, w // 2)).max()


def _f06_prior_low(price, w):
    return price.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _f06_days_since_high(price, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return price.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_days_since_low(price, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return price.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_atr(high, low, w):
    return (high - low).rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_band_width(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / price.replace(0, np.nan)


# ============================================================
# Donchian channel position over 21d (where price sits in the recent band)
def f06bp_f06_breakout_proximity_donchpos_21d_base_v001_signal(close):
    b = _f06_donch_pos(close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 63d (windows >21d use closeadj)
def f06bp_f06_breakout_proximity_donchpos_63d_base_v002_signal(closeadj):
    b = _f06_donch_pos(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 126d, z-scored vs its own 63d history
def f06bp_f06_breakout_proximity_donchpos_126d_base_v003_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    b = _z(p, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 252d
def f06bp_f06_breakout_proximity_donchpos_252d_base_v004_signal(closeadj):
    b = _f06_donch_pos(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to the 21d high (how close to a near-term breakout)
def f06bp_f06_breakout_proximity_disthi_21d_base_v005_signal(close):
    b = _f06_dist_high(close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to the 63d high
def f06bp_f06_breakout_proximity_disthi_63d_base_v006_signal(closeadj):
    b = _f06_dist_high(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to the 126d high, percentile-ranked vs its own 63d history
def f06bp_f06_breakout_proximity_disthi_126d_base_v007_signal(closeadj):
    d = _f06_dist_high(closeadj, 126)
    b = d.rolling(63, min_periods=21).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to the 252d high, z-scored vs its own 126d history (de-trended proximity)
def f06bp_f06_breakout_proximity_disthi_252d_base_v008_signal(closeadj):
    d = _f06_dist_high(closeadj, 252)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above the 21d low (proximity to downside breakdown)
def f06bp_f06_breakout_proximity_distlo_21d_base_v009_signal(close):
    b = _f06_dist_low(close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above the 63d low
def f06bp_f06_breakout_proximity_distlo_63d_base_v010_signal(closeadj):
    b = _f06_dist_low(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above the 126d low, z-scored vs its own 63d history
def f06bp_f06_breakout_proximity_distlo_126d_base_v011_signal(closeadj):
    d = _f06_dist_low(closeadj, 126)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above the 252d low
def f06bp_f06_breakout_proximity_distlo_252d_base_v012_signal(closeadj):
    b = _f06_dist_low(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 21d high (recency of the upper anchor)
def f06bp_f06_breakout_proximity_dsh_21d_base_v013_signal(close):
    b = _f06_days_since_high(close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 63d high
def f06bp_f06_breakout_proximity_dsh_63d_base_v014_signal(closeadj):
    b = _f06_days_since_high(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 126d high
def f06bp_f06_breakout_proximity_dsh_126d_base_v015_signal(closeadj):
    b = _f06_days_since_high(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 21d low
def f06bp_f06_breakout_proximity_dsl_21d_base_v016_signal(close):
    b = _f06_days_since_low(close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 63d low
def f06bp_f06_breakout_proximity_dsl_63d_base_v017_signal(closeadj):
    b = _f06_days_since_low(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 126d low
def f06bp_f06_breakout_proximity_dsl_126d_base_v018_signal(closeadj):
    b = _f06_days_since_low(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d upside breakout magnitude: positive-only headroom above prior 21d high (clipped)
def f06bp_f06_breakout_proximity_brkup_21d_base_v019_signal(close):
    ph = _f06_prior_high(close, 21)
    b = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d upside breakout magnitude: positive-only headroom above prior 63d high
def f06bp_f06_breakout_proximity_brkup_63d_base_v020_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    b = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d upside breakout magnitude: positive-only headroom above prior 126d high
def f06bp_f06_breakout_proximity_brkup_126d_base_v021_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    b = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d downside breakdown depth: negative-only depth below the prior 21d low
def f06bp_f06_breakout_proximity_brkdn_21d_base_v022_signal(close):
    pl = _f06_prior_low(close, 21)
    b = (close / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d downside breakdown depth (negative-only)
def f06bp_f06_breakout_proximity_brkdn_63d_base_v023_signal(closeadj):
    pl = _f06_prior_low(closeadj, 63)
    b = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d downside breakdown depth (negative-only)
def f06bp_f06_breakout_proximity_brkdn_126d_base_v024_signal(closeadj):
    pl = _f06_prior_low(closeadj, 126)
    b = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout + volume confirmation (21d): breakout headroom weighted by volume surge
def f06bp_f06_breakout_proximity_brkvol_21d_base_v025_signal(close, volume):
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    b = head * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout + volume confirmation (63d) using closeadj for the level test
def f06bp_f06_breakout_proximity_brkvol_63d_base_v026_signal(closeadj, volume):
    ph = _f06_prior_high(closeadj, 63)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 63).replace(0, np.nan)
    b = head * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakdown + volume confirmation (21d): downside break depth weighted by volume
def f06bp_f06_breakout_proximity_brkdnvol_21d_base_v027_signal(close, volume):
    pl = _f06_prior_low(close, 21)
    depth = (close / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    b = depth * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside breakout volume divergence: are new highs supported by volume? (63d)
def f06bp_f06_breakout_proximity_brkdiverg_63d_base_v028_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    vz = _z(volume, 63)
    b = pos * np.sign(vz) * vz.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-break: prior 21d band tightness (rank) gating a 63d channel breakout
def f06bp_f06_breakout_proximity_squeezebrk_base_v029_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    tight_rank = 1.0 - bw.rolling(126, min_periods=63).rank(pct=True)
    prior_tight = tight_rank.shift(10)
    pos63 = _f06_donch_pos(closeadj, 63)
    b = prior_tight * (pos63 - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-style squeeze: 21d band width relative to its own 126d median (compression)
def f06bp_f06_breakout_proximity_squeeze_21d_base_v030_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    b = bw / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday close-location in daily true range, averaged over 21d (accumulation posture)
def f06bp_f06_breakout_proximity_hldonch_21d_base_v031_signal(close, high, low):
    clv = (2.0 * close - high - low) / (high - low).replace(0, np.nan)
    b = clv.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday breakout premium: 63d intraday high above the 63d close-based high
def f06bp_f06_breakout_proximity_truedisthi_63d_base_v032_signal(closeadj, high):
    hi_true = _rmax(high, 63)
    hi_close = _rmax(closeadj, 63)
    b = hi_true / hi_close.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday breakdown discount: 63d close-based low above the 63d intraday low
def f06bp_f06_breakout_proximity_truedistlo_63d_base_v033_signal(closeadj, low):
    lo_true = _rmin(low, 63)
    lo_close = _rmin(closeadj, 63)
    b = lo_close / lo_true.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# approach speed to 63d high in ATR units: change in ATR-distance over a month
def f06bp_f06_breakout_proximity_disthiatr_63d_base_v034_signal(closeadj, high, low):
    hi = _rmax(closeadj, 63)
    atr = _f06_atr(high, low, 21)
    ratio = (closeadj - hi) / atr.replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 63d low measured in ATR units
def f06bp_f06_breakout_proximity_distloatr_63d_base_v035_signal(closeadj, high, low):
    lo = _rmin(closeadj, 63)
    atr = _f06_atr(high, low, 21)
    b = (closeadj - lo) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-21d-high frequency over the last quarter (breakout cadence)
def f06bp_f06_breakout_proximity_newhifreq_21d_base_v036_signal(close):
    ph = _f06_prior_high(close, 21)
    is_break = (close > ph).astype(float)
    b = is_break.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-21d-low frequency over the last quarter, weighted by break depth (breakdown cadence)
def f06bp_f06_breakout_proximity_newlofreq_21d_base_v037_signal(close):
    pl = _f06_prior_low(close, 21)
    is_break = (close < pl).astype(float)
    freq = is_break.rolling(63, min_periods=21).mean()
    depth = (pl / close.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).mean()
    b = freq + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net breakout pressure: new-high days minus new-low days over a quarter (63d)
def f06bp_f06_breakout_proximity_netbreak_63d_base_v038_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    pl = _f06_prior_low(closeadj, 21)
    up = (closeadj > ph).astype(float)
    dn = (closeadj < pl).astype(float)
    b = (up - dn).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position momentum (change over a month)
def f06bp_f06_breakout_proximity_donchmom_63d_base_v039_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    b = p - p.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position acceleration of approach to upper band (126d)
def f06bp_f06_breakout_proximity_donchapproach_126d_base_v040_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    b = p - p.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: 21d Donchian position minus 252d Donchian position (short vs long band)
def f06bp_f06_breakout_proximity_donchspr_21v252_base_v041_signal(close, closeadj):
    s = _f06_donch_pos(close, 21)
    l = _f06_donch_pos(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout headroom per unit of volatility, percentile-ranked vs its 252d history
def f06bp_f06_breakout_proximity_brkvoladj_63d_base_v042_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    ratio = head / vol.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band hug: time spent in the top decile of the 63d Donchian channel
def f06bp_f06_breakout_proximity_upperhug_63d_base_v043_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    hug = (p >= 0.9).astype(float)
    b = hug.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-band hug: time spent in the bottom decile of the 63d Donchian channel
def f06bp_f06_breakout_proximity_lowerhug_63d_base_v044_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    hug = (p <= 0.1).astype(float)
    b = hug.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout extension z-scored: how far above the prior 252d high vs its own history
def f06bp_f06_breakout_proximity_brkupz_252d_base_v045_signal(closeadj):
    ph = _f06_prior_high(closeadj, 252)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    b = _z(head, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian width trend: is the channel expanding or contracting? (63d width chg)
def f06bp_f06_breakout_proximity_widthtrend_63d_base_v046_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    b = bw / bw.shift(21).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze streak: count of consecutive days the 21d band sits below its 126d median
def f06bp_f06_breakout_proximity_squeezestreak_base_v047_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    tight = (bw < med).astype(float)
    grp = (tight == 0).cumsum()
    b = tight.groupby(grp).cumsum() / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze release: prior compression x current 21d channel position (break direction)
def f06bp_f06_breakout_proximity_squeezerelease_base_v048_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    compr = (med / bw.replace(0, np.nan)).shift(5)
    pos = _f06_donch_pos(closeadj, 21) - 0.5
    b = compr * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range position smoothed over 21d (persistent breakout posture)
def f06bp_f06_breakout_proximity_donchposema_63d_base_v049_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    b = p.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position displacement: position minus its slow EMA (breakout impulse)
def f06bp_f06_breakout_proximity_donchdisp_63d_base_v050_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    b = p - p.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-since-high relative to days-since-low (who is the more recent anchor) 63d
def f06bp_f06_breakout_proximity_dshvsdsl_63d_base_v051_signal(closeadj):
    dsh = _f06_days_since_high(closeadj, 63)
    dsl = _f06_days_since_low(closeadj, 63)
    b = dsl - dsh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fresh-high recency: 1 - days-since-high, weighted by channel position (126d)
def f06bp_f06_breakout_proximity_freshhi_126d_base_v052_signal(closeadj):
    dsh = _f06_days_since_high(closeadj, 126)
    pos = _f06_donch_pos(closeadj, 126)
    b = (1.0 - dsh) * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout magnitude when it occurs: tanh of 63d headroom (bounded breakout strength)
def f06bp_f06_breakout_proximity_brktanh_63d_base_v053_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    b = np.tanh(15.0 * head)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# channel-position term-structure curvature: 63d position vs mean of 21d & 126d
def f06bp_f06_breakout_proximity_convex_63d_base_v054_signal(close, closeadj):
    p_s = _f06_donch_pos(close, 21)
    p_m = _f06_donch_pos(closeadj, 63)
    p_l = _f06_donch_pos(closeadj, 126)
    b = p_m - 0.5 * (p_s + p_l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window breakout agreement: average top-band proximity across 21/63/126/252
def f06bp_f06_breakout_proximity_multiagree_base_v055_signal(close, closeadj):
    p1 = _f06_donch_pos(close, 21)
    p2 = _f06_donch_pos(closeadj, 63)
    p3 = _f06_donch_pos(closeadj, 126)
    p4 = _f06_donch_pos(closeadj, 252)
    b = pd.concat([p1, p2, p3, p4], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window channel-position dispersion (anchor disagreement across windows)
def f06bp_f06_breakout_proximity_multidisp_base_v056_signal(close, closeadj):
    p1 = _f06_donch_pos(close, 21)
    p2 = _f06_donch_pos(closeadj, 63)
    p3 = _f06_donch_pos(closeadj, 126)
    p4 = _f06_donch_pos(closeadj, 252)
    b = pd.concat([p1, p2, p3, p4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-then-hold quality: fraction of last month still above the prior 63d high
def f06bp_f06_breakout_proximity_brkhold_63d_base_v057_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63).shift(21)
    hold = (closeadj >= ph).astype(float)
    b = hold.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# false-breakout / failure: max 63d Donchian position last month minus current
def f06bp_f06_breakout_proximity_brkfail_63d_base_v058_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    recent_top = p.rolling(21, min_periods=10).max()
    b = recent_top - p
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-high momentum: is the gap to the 126d high closing? (chg over a month)
def f06bp_f06_breakout_proximity_disthimom_126d_base_v059_signal(closeadj):
    d = _f06_dist_high(closeadj, 126)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-low momentum: is price pulling away from the 126d low? (chg over month)
def f06bp_f06_breakout_proximity_distlomom_126d_base_v060_signal(closeadj):
    d = _f06_dist_low(closeadj, 126)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout/volume divergence: 63d channel-position rank minus volume-trend rank
def f06bp_f06_breakout_proximity_volconfpos_63d_base_v061_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    vtrend = _mean(volume, 21) / _mean(volume, 63).replace(0, np.nan)
    pos_r = pos.rolling(63, min_periods=21).rank(pct=True)
    vol_r = vtrend.rolling(63, min_periods=21).rank(pct=True)
    b = pos_r - vol_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume breakout thrust: 21d breakout headroom x dollar-volume z-score
def f06bp_f06_breakout_proximity_dvbrk_21d_base_v062_signal(close, closeadj, volume):
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    dv = closeadj * volume
    dvz = _z(dv, 63)
    b = head * dvz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian midline distance in ATR units (63d midpoint distance scaled by daily range)
def f06bp_f06_breakout_proximity_middist_63d_base_v063_signal(closeadj, high, low):
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    mid = (hi + lo) / 2.0
    atr = _f06_atr(high, low, 21)
    b = (closeadj - mid) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# channel-width-normalized headroom: how many channel-widths to the 126d high
def f06bp_f06_breakout_proximity_headwidth_126d_base_v064_signal(closeadj):
    hi = _rmax(closeadj, 126)
    lo = _rmin(closeadj, 126)
    b = (hi - closeadj) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band push streak: consecutive days in the top quartile of the 63d channel
def f06bp_f06_breakout_proximity_pushstreak_63d_base_v065_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    up = (p >= 0.75).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum() / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-proximity term structure: 63d distance-to-high minus 252d distance-to-high
def f06bp_f06_breakout_proximity_disthirank_63d_base_v066_signal(closeadj):
    d63 = _f06_dist_high(closeadj, 63)
    d252 = _f06_dist_high(closeadj, 252)
    b = d63 - d252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze depth: how far below its 252d max the 63d band width has compressed
def f06bp_f06_breakout_proximity_squeezedepth_base_v067_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    bwmax = bw.rolling(252, min_periods=126).max()
    b = bw / bwmax.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout volume ratio: up-day volume vs down-day volume near the 21d high
def f06bp_f06_breakout_proximity_brkupvol_21d_base_v068_signal(close, volume):
    pos = _f06_donch_pos(close, 21)
    up = close > close.shift(1)
    upvol = volume.where(up, 0.0).rolling(21, min_periods=10).sum()
    dnvol = volume.where(~up, 0.0).rolling(21, min_periods=10).sum()
    ratio = upvol / (upvol + dnvol).replace(0, np.nan)
    b = pos * (ratio - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout thrust: 21d return achieved while making a new 63d high (clean leadership)
def f06bp_f06_breakout_proximity_thrust_63d_base_v069_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    at_high = (closeadj >= ph).astype(float)
    ret21 = closeadj / closeadj.shift(21).replace(0, np.nan) - 1.0
    b = at_high.rolling(21, min_periods=10).mean() * ret21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range compression then position: inverse 21d width x signed channel position
def f06bp_f06_breakout_proximity_comprpos_base_v070_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    b = pos / bw.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year breakout proximity change: 252d distance-to-high vs one year ago
def f06bp_f06_breakout_proximity_disthiyoy_252d_base_v071_signal(closeadj):
    d = _f06_dist_high(closeadj, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout count weighted by magnitude: sum of positive 21d breakout headroom (63d)
def f06bp_f06_breakout_proximity_brkmagsum_63d_base_v072_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    b = head.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout/breakdown magnitude asymmetry over 63d (up-thrust vs down-thrust balance)
def f06bp_f06_breakout_proximity_brkdnmagsum_63d_base_v073_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    pl = _f06_prior_low(closeadj, 21)
    up = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (1.0 - closeadj / pl.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# channel-position skew over a quarter: average asymmetry of where price sits (63d)
def f06bp_f06_breakout_proximity_posskew_63d_base_v074_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    b = (p - 0.5).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high in true-range units (intraday hi/lo) over 126d
def f06bp_f06_breakout_proximity_truedisthiatr_126d_base_v075_signal(closeadj, high, low):
    hi = _rmax(high, 126)
    atr = _f06_atr(high, low, 21)
    b = (closeadj - hi) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06bp_f06_breakout_proximity_donchpos_21d_base_v001_signal,
    f06bp_f06_breakout_proximity_donchpos_63d_base_v002_signal,
    f06bp_f06_breakout_proximity_donchpos_126d_base_v003_signal,
    f06bp_f06_breakout_proximity_donchpos_252d_base_v004_signal,
    f06bp_f06_breakout_proximity_disthi_21d_base_v005_signal,
    f06bp_f06_breakout_proximity_disthi_63d_base_v006_signal,
    f06bp_f06_breakout_proximity_disthi_126d_base_v007_signal,
    f06bp_f06_breakout_proximity_disthi_252d_base_v008_signal,
    f06bp_f06_breakout_proximity_distlo_21d_base_v009_signal,
    f06bp_f06_breakout_proximity_distlo_63d_base_v010_signal,
    f06bp_f06_breakout_proximity_distlo_126d_base_v011_signal,
    f06bp_f06_breakout_proximity_distlo_252d_base_v012_signal,
    f06bp_f06_breakout_proximity_dsh_21d_base_v013_signal,
    f06bp_f06_breakout_proximity_dsh_63d_base_v014_signal,
    f06bp_f06_breakout_proximity_dsh_126d_base_v015_signal,
    f06bp_f06_breakout_proximity_dsl_21d_base_v016_signal,
    f06bp_f06_breakout_proximity_dsl_63d_base_v017_signal,
    f06bp_f06_breakout_proximity_dsl_126d_base_v018_signal,
    f06bp_f06_breakout_proximity_brkup_21d_base_v019_signal,
    f06bp_f06_breakout_proximity_brkup_63d_base_v020_signal,
    f06bp_f06_breakout_proximity_brkup_126d_base_v021_signal,
    f06bp_f06_breakout_proximity_brkdn_21d_base_v022_signal,
    f06bp_f06_breakout_proximity_brkdn_63d_base_v023_signal,
    f06bp_f06_breakout_proximity_brkdn_126d_base_v024_signal,
    f06bp_f06_breakout_proximity_brkvol_21d_base_v025_signal,
    f06bp_f06_breakout_proximity_brkvol_63d_base_v026_signal,
    f06bp_f06_breakout_proximity_brkdnvol_21d_base_v027_signal,
    f06bp_f06_breakout_proximity_brkdiverg_63d_base_v028_signal,
    f06bp_f06_breakout_proximity_squeezebrk_base_v029_signal,
    f06bp_f06_breakout_proximity_squeeze_21d_base_v030_signal,
    f06bp_f06_breakout_proximity_hldonch_21d_base_v031_signal,
    f06bp_f06_breakout_proximity_truedisthi_63d_base_v032_signal,
    f06bp_f06_breakout_proximity_truedistlo_63d_base_v033_signal,
    f06bp_f06_breakout_proximity_disthiatr_63d_base_v034_signal,
    f06bp_f06_breakout_proximity_distloatr_63d_base_v035_signal,
    f06bp_f06_breakout_proximity_newhifreq_21d_base_v036_signal,
    f06bp_f06_breakout_proximity_newlofreq_21d_base_v037_signal,
    f06bp_f06_breakout_proximity_netbreak_63d_base_v038_signal,
    f06bp_f06_breakout_proximity_donchmom_63d_base_v039_signal,
    f06bp_f06_breakout_proximity_donchapproach_126d_base_v040_signal,
    f06bp_f06_breakout_proximity_donchspr_21v252_base_v041_signal,
    f06bp_f06_breakout_proximity_brkvoladj_63d_base_v042_signal,
    f06bp_f06_breakout_proximity_upperhug_63d_base_v043_signal,
    f06bp_f06_breakout_proximity_lowerhug_63d_base_v044_signal,
    f06bp_f06_breakout_proximity_brkupz_252d_base_v045_signal,
    f06bp_f06_breakout_proximity_widthtrend_63d_base_v046_signal,
    f06bp_f06_breakout_proximity_squeezestreak_base_v047_signal,
    f06bp_f06_breakout_proximity_squeezerelease_base_v048_signal,
    f06bp_f06_breakout_proximity_donchposema_63d_base_v049_signal,
    f06bp_f06_breakout_proximity_donchdisp_63d_base_v050_signal,
    f06bp_f06_breakout_proximity_dshvsdsl_63d_base_v051_signal,
    f06bp_f06_breakout_proximity_freshhi_126d_base_v052_signal,
    f06bp_f06_breakout_proximity_brktanh_63d_base_v053_signal,
    f06bp_f06_breakout_proximity_convex_63d_base_v054_signal,
    f06bp_f06_breakout_proximity_multiagree_base_v055_signal,
    f06bp_f06_breakout_proximity_multidisp_base_v056_signal,
    f06bp_f06_breakout_proximity_brkhold_63d_base_v057_signal,
    f06bp_f06_breakout_proximity_brkfail_63d_base_v058_signal,
    f06bp_f06_breakout_proximity_disthimom_126d_base_v059_signal,
    f06bp_f06_breakout_proximity_distlomom_126d_base_v060_signal,
    f06bp_f06_breakout_proximity_volconfpos_63d_base_v061_signal,
    f06bp_f06_breakout_proximity_dvbrk_21d_base_v062_signal,
    f06bp_f06_breakout_proximity_middist_63d_base_v063_signal,
    f06bp_f06_breakout_proximity_headwidth_126d_base_v064_signal,
    f06bp_f06_breakout_proximity_pushstreak_63d_base_v065_signal,
    f06bp_f06_breakout_proximity_disthirank_63d_base_v066_signal,
    f06bp_f06_breakout_proximity_squeezedepth_base_v067_signal,
    f06bp_f06_breakout_proximity_brkupvol_21d_base_v068_signal,
    f06bp_f06_breakout_proximity_thrust_63d_base_v069_signal,
    f06bp_f06_breakout_proximity_comprpos_base_v070_signal,
    f06bp_f06_breakout_proximity_disthiyoy_252d_base_v071_signal,
    f06bp_f06_breakout_proximity_brkmagsum_63d_base_v072_signal,
    f06bp_f06_breakout_proximity_brkdnmagsum_63d_base_v073_signal,
    f06bp_f06_breakout_proximity_posskew_63d_base_v074_signal,
    f06bp_f06_breakout_proximity_truedisthiatr_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_BREAKOUT_PROXIMITY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f06_breakout_proximity_base_001_075_claude: %d features pass" % n_features)
