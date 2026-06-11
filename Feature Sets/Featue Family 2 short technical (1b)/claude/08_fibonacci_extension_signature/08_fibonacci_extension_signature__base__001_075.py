"""fibonacci_extension_signature base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each feature
encodes a *different concept* in the prior-swing Fibonacci-extension overshoot
theme: how far current price has overshot the canonical Fibonacci extension
targets (1.272 / 1.618 / 2.0 / 2.618 / 3.0 / 4.236) of an identified prior
swing leg, in log / pct / ATR / sigma units, at multiple swing horizons, with
indicator / dwell / streak / failure / multi-leg variants.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ---- family-specific helpers (PIT-clean) ----

def _swing_low(low: pd.Series, n: int) -> pd.Series:
    """Most-recent confirmed PIT swing-low value, carried forward. A 'swing low'
    at bar t is `low[t-n] == low.rolling(2n+1).min()[t]` evaluated only with
    data available at time t (i.e. a center pivot only confirmed n bars later).
    We carry forward the confirmed swing-low so that at any t the helper returns
    the last value of low that was confirmed as a local minimum by bar t."""
    # A bar t-n is a confirmed pivot-low at bar t iff its low is the min over [t-2n, t].
    # Place that pivot value at bar t, then carry forward.
    win = 2 * n + 1
    rolling_min = low.rolling(win, min_periods=win).min()
    # at bar t, the candidate pivot bar is t-n; its low value:
    cand = low.shift(n)
    is_pivot = (cand == rolling_min) & cand.notna() & rolling_min.notna()
    pivot_val = cand.where(is_pivot, np.nan)
    return pivot_val.ffill()


def _swing_high(high: pd.Series, n: int) -> pd.Series:
    """Mirror of _swing_low for highs."""
    win = 2 * n + 1
    rolling_max = high.rolling(win, min_periods=win).max()
    cand = high.shift(n)
    is_pivot = (cand == rolling_max) & cand.notna() & rolling_max.notna()
    pivot_val = cand.where(is_pivot, np.nan)
    return pivot_val.ffill()


def _ext_value(price: pd.Series, sl: pd.Series, sh: pd.Series) -> pd.Series:
    """Fib extension value: (price - sl) / (sh - sl). 1.0 = at swing-high.
    1.618 = at golden-ratio extension. Negative if price < sl."""
    return _safe_div(price - sl, sh - sl)


def _fib_target(sl: pd.Series, sh: pd.Series, ratio: float) -> pd.Series:
    """Absolute price target for a given Fib extension ratio of the swing."""
    return sl + ratio * (sh - sl)


def _log_dist(price: pd.Series, target: pd.Series) -> pd.Series:
    return _safe_log(price) - _safe_log(target)


# Swing-window constants (short / medium / long swings)
SW_S = 10   # ~2 weeks: short-term swing pivots
SW_M = 30   # ~6 weeks: medium-term
SW_L = 90   # ~1 quarter+: long-term


# ============================================================
# Bucket A — Log distance above multi-ratio fib extensions, multi-swing horizons (001-015)
# Each horizon (S/M/L) encodes a *different swing timescale*, not a sweep.
# Each ratio is a different overshoot regime.
# ============================================================

def f08_fibx_001_log_dist_above_1_272_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close above 1.272 fib extension of short-term swing — mild overshoot, short horizon."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    tgt = _fib_target(sl, sh, 1.272)
    return _log_dist(close, tgt)


def f08_fibx_002_log_dist_above_1_618_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.618 (golden) extension of short swing."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    return _log_dist(close, _fib_target(sl, sh, 1.618))


def f08_fibx_003_log_dist_above_2_0_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.0 (doubling) extension of short swing."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    return _log_dist(close, _fib_target(sl, sh, 2.0))


def f08_fibx_004_log_dist_above_2_618_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.618 extension of short swing — extreme short-term overshoot."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    return _log_dist(close, _fib_target(sl, sh, 2.618))


def f08_fibx_005_log_dist_above_4_236_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 4.236 extension of short swing — blowoff regime."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    return _log_dist(close, _fib_target(sl, sh, 4.236))


def f08_fibx_006_log_dist_above_1_272_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.272 ext of medium swing — different timescale than 001."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 1.272))


def f08_fibx_007_log_dist_above_1_618_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.618 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 1.618))


def f08_fibx_008_log_dist_above_2_0_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.0 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 2.0))


def f08_fibx_009_log_dist_above_2_618_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.618 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 2.618))


def f08_fibx_010_log_dist_above_4_236_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 4.236 ext of medium swing — extended medium-horizon blowoff."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 4.236))


def f08_fibx_011_log_dist_above_1_272_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.272 ext of long swing — multi-quarter horizon."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _log_dist(close, _fib_target(sl, sh, 1.272))


def f08_fibx_012_log_dist_above_1_618_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.618 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _log_dist(close, _fib_target(sl, sh, 1.618))


def f08_fibx_013_log_dist_above_2_0_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.0 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _log_dist(close, _fib_target(sl, sh, 2.0))


def f08_fibx_014_log_dist_above_2_618_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.618 ext of long swing — multi-quarter parabolic regime."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _log_dist(close, _fib_target(sl, sh, 2.618))


def f08_fibx_015_log_dist_above_4_236_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 4.236 ext of long swing — terminal blowoff."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _log_dist(close, _fib_target(sl, sh, 4.236))


# ============================================================
# Bucket B — ATR-normalized distance above fib targets (016-025)
# Different normalization than log: tells how many vol-units we're past the target.
# ============================================================

def f08_fibx_016_atr_dist_above_1_618_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance above 1.618 ext of short swing — vol-adjusted overshoot."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(close - _fib_target(sl, sh, 1.618), atr)


def f08_fibx_017_atr_dist_above_2_0_ext_of_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 2.0 ext of short swing."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    return _safe_div(close - _fib_target(sl, sh, 2.0), _atr(high, low, close, n=MDAYS))


def f08_fibx_018_atr_dist_above_1_618_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 1.618 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _safe_div(close - _fib_target(sl, sh, 1.618), _atr(high, low, close, n=MDAYS))


def f08_fibx_019_atr_dist_above_2_0_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 2.0 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _safe_div(close - _fib_target(sl, sh, 2.0), _atr(high, low, close, n=MDAYS))


def f08_fibx_020_atr_dist_above_2_618_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 2.618 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _safe_div(close - _fib_target(sl, sh, 2.618), _atr(high, low, close, n=MDAYS))


def f08_fibx_021_atr_dist_above_1_618_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 1.618 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _safe_div(close - _fib_target(sl, sh, 1.618), _atr(high, low, close, n=MDAYS))


def f08_fibx_022_atr_dist_above_2_0_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 2.0 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _safe_div(close - _fib_target(sl, sh, 2.0), _atr(high, low, close, n=MDAYS))


def f08_fibx_023_atr_dist_above_2_618_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 2.618 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _safe_div(close - _fib_target(sl, sh, 2.618), _atr(high, low, close, n=MDAYS))


def f08_fibx_024_pct_dist_above_1_618_ext_of_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raw % distance above 1.618 ext of medium swing — non-log normalization."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.618)
    return _safe_div(close - tgt, tgt)


def f08_fibx_025_pct_dist_above_2_0_ext_of_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Raw % distance above 2.0 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    tgt = _fib_target(sl, sh, 2.0)
    return _safe_div(close - tgt, tgt)


# ============================================================
# Bucket C — Current extension VALUE (signed depth into Fib stack) (026-028)
# ============================================================

def f08_fibx_026_current_extension_value_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed extension value: (close - swing_low) / (swing_high - swing_low). 1.0=at SH, 1.618=golden."""
    return _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))


def f08_fibx_027_current_extension_value_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed extension value for medium swing."""
    return _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))


def f08_fibx_028_current_extension_value_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed extension value for long swing."""
    return _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))


# ============================================================
# Bucket D — Fib-zone categorical and nearest-fib distance (029-039)
# ============================================================

def f08_fibx_029_fib_zone_id_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Categorical fib zone (encoded as ordinal) of current ext on short swing.
    0=<1.0, 1=[1.0,1.272), 2=[1.272,1.618), 3=[1.618,2.0), 4=[2.0,2.618), 5=[2.618,4.236), 6=>=4.236."""
    e = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    z = pd.Series(np.nan, index=close.index)
    mask = e.notna()
    arr = e.to_numpy()
    out = np.full(len(e), np.nan)
    out = np.where(mask & (arr < 1.0), 0, out)
    out = np.where(mask & (arr >= 1.0) & (arr < 1.272), 1, out)
    out = np.where(mask & (arr >= 1.272) & (arr < 1.618), 2, out)
    out = np.where(mask & (arr >= 1.618) & (arr < 2.0), 3, out)
    out = np.where(mask & (arr >= 2.0) & (arr < 2.618), 4, out)
    out = np.where(mask & (arr >= 2.618) & (arr < 4.236), 5, out)
    out = np.where(mask & (arr >= 4.236), 6, out)
    return pd.Series(out, index=close.index)


def f08_fibx_030_fib_zone_id_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same fib zone ordinal on medium swing."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    arr = e.to_numpy()
    out = np.full(len(e), np.nan)
    m = ~np.isnan(arr)
    out = np.where(m & (arr < 1.0), 0, out)
    out = np.where(m & (arr >= 1.0) & (arr < 1.272), 1, out)
    out = np.where(m & (arr >= 1.272) & (arr < 1.618), 2, out)
    out = np.where(m & (arr >= 1.618) & (arr < 2.0), 3, out)
    out = np.where(m & (arr >= 2.0) & (arr < 2.618), 4, out)
    out = np.where(m & (arr >= 2.618) & (arr < 4.236), 5, out)
    out = np.where(m & (arr >= 4.236), 6, out)
    return pd.Series(out, index=close.index)


def f08_fibx_031_fib_zone_id_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fib zone ordinal on long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    arr = e.to_numpy()
    out = np.full(len(e), np.nan)
    m = ~np.isnan(arr)
    out = np.where(m & (arr < 1.0), 0, out)
    out = np.where(m & (arr >= 1.0) & (arr < 1.272), 1, out)
    out = np.where(m & (arr >= 1.272) & (arr < 1.618), 2, out)
    out = np.where(m & (arr >= 1.618) & (arr < 2.0), 3, out)
    out = np.where(m & (arr >= 2.0) & (arr < 2.618), 4, out)
    out = np.where(m & (arr >= 2.618) & (arr < 4.236), 5, out)
    out = np.where(m & (arr >= 4.236), 6, out)
    return pd.Series(out, index=close.index)


def f08_fibx_032_atr_dist_to_nearest_fib_level_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum ATR-normalized distance to nearest of {1.272,1.618,2.0,2.618,4.236} on short swing."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    atr = _atr(high, low, close, n=MDAYS)
    parts = [(_fib_target(sl, sh, r) - close).abs().rename(f"r{i}") for i, r in enumerate([1.272, 1.618, 2.0, 2.618, 4.236])]
    nearest = pd.concat(parts, axis=1).min(axis=1)
    return _safe_div(nearest, atr)


def f08_fibx_033_atr_dist_to_nearest_fib_level_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum ATR-normalized distance to nearest fib on medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    parts = [(_fib_target(sl, sh, r) - close).abs().rename(f"r{i}") for i, r in enumerate([1.272, 1.618, 2.0, 2.618, 4.236])]
    return _safe_div(pd.concat(parts, axis=1).min(axis=1), atr)


def f08_fibx_034_atr_dist_to_nearest_fib_level_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Minimum ATR-normalized distance to nearest fib on long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    atr = _atr(high, low, close, n=MDAYS)
    parts = [(_fib_target(sl, sh, r) - close).abs().rename(f"r{i}") for i, r in enumerate([1.272, 1.618, 2.0, 2.618, 4.236])]
    return _safe_div(pd.concat(parts, axis=1).min(axis=1), atr)


def f08_fibx_035_signed_dist_to_nearest_lower_fib_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed log-distance from close down to nearest fib level *below* current price (support fib)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    parts = []
    for i, r in enumerate(ratios):
        t = _fib_target(sl, sh, r)
        below = t.where(t < close, np.nan)
        parts.append(_safe_log(close).sub(_safe_log(below)).rename(f"r{i}"))
    return pd.concat(parts, axis=1).min(axis=1)


def f08_fibx_036_signed_dist_to_nearest_upper_fib_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed log-distance from close up to nearest fib *above* current price (resistance fib)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    parts = []
    for i, r in enumerate(ratios):
        t = _fib_target(sl, sh, r)
        above = t.where(t > close, np.nan)
        parts.append(_safe_log(above).sub(_safe_log(close)).rename(f"r{i}"))
    return pd.concat(parts, axis=1).min(axis=1)


def f08_fibx_037_count_fib_levels_exceeded_short_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many of {1.272,1.618,2.0,2.618,4.236} fib targets close is currently above — short swing."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    cnt = pd.Series(0.0, index=close.index)
    valid = sl.notna() & sh.notna() & close.notna()
    for r in [1.272, 1.618, 2.0, 2.618, 4.236]:
        cnt = cnt + (close > _fib_target(sl, sh, r)).astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_038_count_fib_levels_exceeded_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same count on medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    cnt = pd.Series(0.0, index=close.index)
    valid = sl.notna() & sh.notna() & close.notna()
    for r in [1.272, 1.618, 2.0, 2.618, 4.236]:
        cnt = cnt + (close > _fib_target(sl, sh, r)).astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_039_count_fib_levels_exceeded_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same count on long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    cnt = pd.Series(0.0, index=close.index)
    valid = sl.notna() & sh.notna() & close.notna()
    for r in [1.272, 1.618, 2.0, 2.618, 4.236]:
        cnt = cnt + (close > _fib_target(sl, sh, r)).astype(float)
    return cnt.where(valid, np.nan)


# ============================================================
# Bucket E — Indicator: crossed above fib level within last K bars (040-044)
# ============================================================

def f08_fibx_040_crossed_1_618_ext_short_swing_within_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close crossed above 1.618 ext of short swing at any time in last 5 bars."""
    sl = _swing_low(low, SW_S); sh = _swing_high(high, SW_S)
    cross_up = (close > _fib_target(sl, sh, 1.618)) & (close.shift(1) <= _fib_target(sl, sh, 1.618).shift(1))
    return cross_up.rolling(WDAYS, min_periods=1).max().astype(float)


def f08_fibx_041_crossed_1_618_ext_medium_swing_within_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close crossed above 1.618 ext of medium swing within last 21 bars."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    cross_up = (close > _fib_target(sl, sh, 1.618)) & (close.shift(1) <= _fib_target(sl, sh, 1.618).shift(1))
    return cross_up.rolling(MDAYS, min_periods=1).max().astype(float)


def f08_fibx_042_crossed_1_618_ext_long_swing_within_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close crossed above 1.618 ext of long swing within last 63 bars."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    cross_up = (close > _fib_target(sl, sh, 1.618)) & (close.shift(1) <= _fib_target(sl, sh, 1.618).shift(1))
    return cross_up.rolling(QDAYS, min_periods=1).max().astype(float)


def f08_fibx_043_crossed_2_618_ext_medium_swing_within_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close crossed above 2.618 ext of medium swing within last 21 bars — extreme reach."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    cross_up = (close > _fib_target(sl, sh, 2.618)) & (close.shift(1) <= _fib_target(sl, sh, 2.618).shift(1))
    return cross_up.rolling(MDAYS, min_periods=1).max().astype(float)


def f08_fibx_044_crossed_4_236_ext_long_swing_within_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close crossed above 4.236 ext of long swing within last 252 bars — terminal blowoff event."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    cross_up = (close > _fib_target(sl, sh, 4.236)) & (close.shift(1) <= _fib_target(sl, sh, 4.236).shift(1))
    return cross_up.rolling(YDAYS, min_periods=1).max().astype(float)


# ============================================================
# Bucket F — Bars-since first crossing fib level (045-047)
# ============================================================

def f08_fibx_045_bars_since_first_crossing_1_618_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most recent up-cross of 1.618 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.618)
    cross_up = (close > tgt) & (close.shift(1) <= tgt.shift(1))
    idx_at_cross = np.where(cross_up.to_numpy(), np.arange(len(close)), np.nan)
    last_cross_idx = pd.Series(idx_at_cross, index=close.index).ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_cross_idx


def f08_fibx_046_bars_since_first_crossing_2_0_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent up-cross of 2.0 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 2.0)
    cross_up = (close > tgt) & (close.shift(1) <= tgt.shift(1))
    idx_at_cross = np.where(cross_up.to_numpy(), np.arange(len(close)), np.nan)
    last_cross_idx = pd.Series(idx_at_cross, index=close.index).ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_cross_idx


def f08_fibx_047_bars_since_first_crossing_2_618_ext_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent up-cross of 2.618 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    tgt = _fib_target(sl, sh, 2.618)
    cross_up = (close > tgt) & (close.shift(1) <= tgt.shift(1))
    idx_at_cross = np.where(cross_up.to_numpy(), np.arange(len(close)), np.nan)
    last_cross_idx = pd.Series(idx_at_cross, index=close.index).ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_cross_idx


# ============================================================
# Bucket G — Extension velocity & speed-of-achievement (048-051)
# ============================================================

def f08_fibx_048_extension_velocity_medium_swing_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day change in ext value of medium swing — how fast we're moving through fib levels."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e - e.shift(WDAYS)


def f08_fibx_049_extension_velocity_long_swing_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day change in ext value of long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return e - e.shift(MDAYS)


def f08_fibx_050_log_extension_velocity_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-ratio of current ext to 21d-ago ext on medium swing — compound progress rate."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return _safe_log(e) - _safe_log(e.shift(MDAYS))


def f08_fibx_051_log_extension_velocity_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-ratio of current to 63d-ago ext on long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _safe_log(e) - _safe_log(e.shift(QDAYS))


# ============================================================
# Bucket H — Dwell time above fib levels (052-056)
# ============================================================

def f08_fibx_052_dwell_above_1_0_ext_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 bars where close > swing_high (1.0 ext) on medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above = (close > sh).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_053_dwell_above_1_272_ext_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 bars where close > 1.272 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above = (close > _fib_target(sl, sh, 1.272)).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_054_dwell_above_1_618_ext_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 bars where close > 1.618 ext."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above = (close > _fib_target(sl, sh, 1.618)).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_055_dwell_above_1_0_ext_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 252 bars where close > swing_high on long swing."""
    sh = _swing_high(high, SW_L)
    return (close > sh).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f08_fibx_056_dwell_above_1_618_ext_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 252 bars where close > 1.618 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    above = (close > _fib_target(sl, sh, 1.618)).astype(float)
    return above.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket I — Failure-to-extend & rejection events (057-061)
# ============================================================

def f08_fibx_057_failure_to_extend_above_1_618_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: high pierced 1.618 ext but close < 1.618 ext — intraday rejection at the level."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.618)
    valid = sl.notna() & sh.notna()
    return ((high > tgt) & (close < tgt)).astype(float).where(valid, np.nan)


def f08_fibx_058_failure_to_extend_above_2_0_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High pierced 2.0 ext but close < 2.0 ext."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 2.0)
    return ((high > tgt) & (close < tgt)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_059_failure_to_extend_above_1_618_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High pierced 1.618 ext but close < 1.618 ext on long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    tgt = _fib_target(sl, sh, 1.618)
    return ((high > tgt) & (close < tgt)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_060_close_back_below_1_272_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today close < 1.272 ext but yesterday close >= 1.272 ext (down-cross)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.272)
    return ((close < tgt) & (close.shift(1) >= tgt.shift(1))).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_061_failed_extension_count_medium_swing_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of failure-to-extend(1.618, medium swing) events in last 252 bars."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.618)
    failure = ((high > tgt) & (close < tgt)).astype(float)
    return failure.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket J — Intraday wick beyond fib (062-064)
# ============================================================

def f08_fibx_062_high_to_close_distance_above_1_618_medium_swing_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized intraday wick distance above 1.618: (high - max(close,1.618_tgt)) / ATR — pure wick above the fib."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.618)
    base = np.maximum(close.to_numpy(), tgt.to_numpy())
    wick = pd.Series(high.to_numpy() - base, index=close.index)
    wick = wick.clip(lower=0)
    return _safe_div(wick, _atr(high, low, close, n=MDAYS))


def f08_fibx_063_wick_above_1_618_medium_swing_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: high > 1.618 ext but close <= 1.618 ext (wick-only breach, intraday rejection)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt = _fib_target(sl, sh, 1.618)
    return ((high > tgt) & (close <= tgt)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_064_low_breakdown_below_swing_low_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today low < long-swing swing-low (pattern broken at the bottom — invalidates the up-swing)."""
    sl = _swing_low(low, SW_L)
    return (low < sl).astype(float).where(sl.notna(), np.nan)


# ============================================================
# Bucket K — Cross-horizon disagreement / agreement (065-068)
# ============================================================

def f08_fibx_065_extension_ratio_medium_over_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of medium-swing ext value to long-swing ext value — relative reach across timescales."""
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _safe_div(em, el)


def f08_fibx_066_extension_sign_disagreement_medium_vs_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: medium ext > 1 but long ext < 1 (or vice versa) — timescale disagreement."""
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    disagree = ((em > 1.0) & (el < 1.0)) | ((em < 1.0) & (el > 1.0))
    return disagree.astype(float).where(em.notna() & el.notna(), np.nan)


def f08_fibx_067_extension_acceleration_medium_swing_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d acceleration of ext value: (ext_now - ext_-21) - (ext_-21 - ext_-42)."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    v_now = e - e.shift(MDAYS)
    v_lag = e.shift(MDAYS) - e.shift(2 * MDAYS)
    return v_now - v_lag


def f08_fibx_068_log_progress_speed_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-progress speed: average log change in ext per bar over last 21 bars."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    log_e = _safe_log(e)
    return (log_e - log_e.shift(MDAYS)) / float(MDAYS)


# ============================================================
# Bucket L — Multi-leg / measured-move (069-072)
# ============================================================

def _abcd_legs(high: pd.Series, low: pd.Series, n: int):
    """Return (leg1_len, leg2_len) where leg1 = swing_high - swing_low (most recent confirmed),
    leg2 = current high - swing_high. Both in absolute price units."""
    sl = _swing_low(low, n)
    sh = _swing_high(high, n)
    leg1 = sh - sl
    leg2 = high - sh
    return leg1, leg2


def f08_fibx_069_multi_leg_extension_ratio_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ABCD measured-move ratio: leg2 / leg1 on medium swing. 1.0 = exact measured move."""
    leg1, leg2 = _abcd_legs(high, low, SW_M)
    return _safe_div(leg2, leg1)


def f08_fibx_070_abcd_extension_pattern_match_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: leg2/leg1 within ±10% of 1.0 — clean ABCD pattern completed."""
    leg1, leg2 = _abcd_legs(high, low, SW_M)
    r = _safe_div(leg2, leg1)
    return ((r >= 0.9) & (r <= 1.1)).astype(float).where(r.notna(), np.nan)


def f08_fibx_071_abcd_overshoot_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: leg2 > 1.618 × leg1 — abcd overshoot regime, classic blowoff."""
    leg1, leg2 = _abcd_legs(high, low, SW_M)
    r = _safe_div(leg2, leg1)
    return (r > 1.618).astype(float).where(r.notna(), np.nan)


def f08_fibx_072_measured_move_excess_medium_swing_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized excess of leg2 over leg1 — (leg2 - leg1)/atr."""
    leg1, leg2 = _abcd_legs(high, low, SW_M)
    return _safe_div(leg2 - leg1, _atr(high, low, close, n=MDAYS))


# ============================================================
# Bucket M — Less common fib ratios (073-075)
# ============================================================

def f08_fibx_073_log_dist_above_1_5_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.5 ext (midpoint between 1.272 and 1.618) — alternative measured move."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 1.5))


def f08_fibx_074_log_dist_above_1_786_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.786 ext (between golden and doubling) — secondary fib resistance."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _log_dist(close, _fib_target(sl, sh, 1.786))


def f08_fibx_075_cumulative_extension_score_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of weighted-fib-exceedances on medium swing: weight i for crossing i-th fib in {1.272,1.618,2.0,2.618,4.236}."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    score = pd.Series(0.0, index=close.index)
    weights = [1, 2, 3, 4, 5]
    for r, w in zip([1.272, 1.618, 2.0, 2.618, 4.236], weights):
        score = score + w * (close > _fib_target(sl, sh, r)).astype(float)
    return score.where(sl.notna() & sh.notna(), np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

FIBONACCI_EXTENSION_SIGNATURE_BASE_REGISTRY_001_075 = {
    "f08_fibx_001_log_dist_above_1_272_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_001_log_dist_above_1_272_ext_of_short_swing},
    "f08_fibx_002_log_dist_above_1_618_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_002_log_dist_above_1_618_ext_of_short_swing},
    "f08_fibx_003_log_dist_above_2_0_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_003_log_dist_above_2_0_ext_of_short_swing},
    "f08_fibx_004_log_dist_above_2_618_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_004_log_dist_above_2_618_ext_of_short_swing},
    "f08_fibx_005_log_dist_above_4_236_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_005_log_dist_above_4_236_ext_of_short_swing},
    "f08_fibx_006_log_dist_above_1_272_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_006_log_dist_above_1_272_ext_of_medium_swing},
    "f08_fibx_007_log_dist_above_1_618_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_007_log_dist_above_1_618_ext_of_medium_swing},
    "f08_fibx_008_log_dist_above_2_0_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_008_log_dist_above_2_0_ext_of_medium_swing},
    "f08_fibx_009_log_dist_above_2_618_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_009_log_dist_above_2_618_ext_of_medium_swing},
    "f08_fibx_010_log_dist_above_4_236_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_010_log_dist_above_4_236_ext_of_medium_swing},
    "f08_fibx_011_log_dist_above_1_272_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_011_log_dist_above_1_272_ext_of_long_swing},
    "f08_fibx_012_log_dist_above_1_618_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_012_log_dist_above_1_618_ext_of_long_swing},
    "f08_fibx_013_log_dist_above_2_0_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_013_log_dist_above_2_0_ext_of_long_swing},
    "f08_fibx_014_log_dist_above_2_618_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_014_log_dist_above_2_618_ext_of_long_swing},
    "f08_fibx_015_log_dist_above_4_236_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_015_log_dist_above_4_236_ext_of_long_swing},
    "f08_fibx_016_atr_dist_above_1_618_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_016_atr_dist_above_1_618_ext_of_short_swing},
    "f08_fibx_017_atr_dist_above_2_0_ext_of_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_017_atr_dist_above_2_0_ext_of_short_swing},
    "f08_fibx_018_atr_dist_above_1_618_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_018_atr_dist_above_1_618_ext_of_medium_swing},
    "f08_fibx_019_atr_dist_above_2_0_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_019_atr_dist_above_2_0_ext_of_medium_swing},
    "f08_fibx_020_atr_dist_above_2_618_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_020_atr_dist_above_2_618_ext_of_medium_swing},
    "f08_fibx_021_atr_dist_above_1_618_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_021_atr_dist_above_1_618_ext_of_long_swing},
    "f08_fibx_022_atr_dist_above_2_0_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_022_atr_dist_above_2_0_ext_of_long_swing},
    "f08_fibx_023_atr_dist_above_2_618_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_023_atr_dist_above_2_618_ext_of_long_swing},
    "f08_fibx_024_pct_dist_above_1_618_ext_of_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_024_pct_dist_above_1_618_ext_of_medium_swing},
    "f08_fibx_025_pct_dist_above_2_0_ext_of_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_025_pct_dist_above_2_0_ext_of_long_swing},
    "f08_fibx_026_current_extension_value_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_026_current_extension_value_short_swing},
    "f08_fibx_027_current_extension_value_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_027_current_extension_value_medium_swing},
    "f08_fibx_028_current_extension_value_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_028_current_extension_value_long_swing},
    "f08_fibx_029_fib_zone_id_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_029_fib_zone_id_short_swing},
    "f08_fibx_030_fib_zone_id_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_030_fib_zone_id_medium_swing},
    "f08_fibx_031_fib_zone_id_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_031_fib_zone_id_long_swing},
    "f08_fibx_032_atr_dist_to_nearest_fib_level_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_032_atr_dist_to_nearest_fib_level_short_swing},
    "f08_fibx_033_atr_dist_to_nearest_fib_level_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_033_atr_dist_to_nearest_fib_level_medium_swing},
    "f08_fibx_034_atr_dist_to_nearest_fib_level_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_034_atr_dist_to_nearest_fib_level_long_swing},
    "f08_fibx_035_signed_dist_to_nearest_lower_fib_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_035_signed_dist_to_nearest_lower_fib_medium_swing},
    "f08_fibx_036_signed_dist_to_nearest_upper_fib_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_036_signed_dist_to_nearest_upper_fib_medium_swing},
    "f08_fibx_037_count_fib_levels_exceeded_short_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_037_count_fib_levels_exceeded_short_swing},
    "f08_fibx_038_count_fib_levels_exceeded_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_038_count_fib_levels_exceeded_medium_swing},
    "f08_fibx_039_count_fib_levels_exceeded_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_039_count_fib_levels_exceeded_long_swing},
    "f08_fibx_040_crossed_1_618_ext_short_swing_within_5d": {"inputs": ["high", "low", "close"], "func": f08_fibx_040_crossed_1_618_ext_short_swing_within_5d},
    "f08_fibx_041_crossed_1_618_ext_medium_swing_within_21d": {"inputs": ["high", "low", "close"], "func": f08_fibx_041_crossed_1_618_ext_medium_swing_within_21d},
    "f08_fibx_042_crossed_1_618_ext_long_swing_within_63d": {"inputs": ["high", "low", "close"], "func": f08_fibx_042_crossed_1_618_ext_long_swing_within_63d},
    "f08_fibx_043_crossed_2_618_ext_medium_swing_within_21d": {"inputs": ["high", "low", "close"], "func": f08_fibx_043_crossed_2_618_ext_medium_swing_within_21d},
    "f08_fibx_044_crossed_4_236_ext_long_swing_within_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_044_crossed_4_236_ext_long_swing_within_252d},
    "f08_fibx_045_bars_since_first_crossing_1_618_ext_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_045_bars_since_first_crossing_1_618_ext_medium_swing},
    "f08_fibx_046_bars_since_first_crossing_2_0_ext_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_046_bars_since_first_crossing_2_0_ext_medium_swing},
    "f08_fibx_047_bars_since_first_crossing_2_618_ext_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_047_bars_since_first_crossing_2_618_ext_long_swing},
    "f08_fibx_048_extension_velocity_medium_swing_5d": {"inputs": ["high", "low", "close"], "func": f08_fibx_048_extension_velocity_medium_swing_5d},
    "f08_fibx_049_extension_velocity_long_swing_21d": {"inputs": ["high", "low", "close"], "func": f08_fibx_049_extension_velocity_long_swing_21d},
    "f08_fibx_050_log_extension_velocity_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_050_log_extension_velocity_medium_swing},
    "f08_fibx_051_log_extension_velocity_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_051_log_extension_velocity_long_swing},
    "f08_fibx_052_dwell_above_1_0_ext_medium_swing_63d": {"inputs": ["high", "low", "close"], "func": f08_fibx_052_dwell_above_1_0_ext_medium_swing_63d},
    "f08_fibx_053_dwell_above_1_272_ext_medium_swing_63d": {"inputs": ["high", "low", "close"], "func": f08_fibx_053_dwell_above_1_272_ext_medium_swing_63d},
    "f08_fibx_054_dwell_above_1_618_ext_medium_swing_63d": {"inputs": ["high", "low", "close"], "func": f08_fibx_054_dwell_above_1_618_ext_medium_swing_63d},
    "f08_fibx_055_dwell_above_1_0_ext_long_swing_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_055_dwell_above_1_0_ext_long_swing_252d},
    "f08_fibx_056_dwell_above_1_618_ext_long_swing_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_056_dwell_above_1_618_ext_long_swing_252d},
    "f08_fibx_057_failure_to_extend_above_1_618_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_057_failure_to_extend_above_1_618_medium_swing},
    "f08_fibx_058_failure_to_extend_above_2_0_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_058_failure_to_extend_above_2_0_medium_swing},
    "f08_fibx_059_failure_to_extend_above_1_618_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_059_failure_to_extend_above_1_618_long_swing},
    "f08_fibx_060_close_back_below_1_272_ext_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_060_close_back_below_1_272_ext_medium_swing},
    "f08_fibx_061_failed_extension_count_medium_swing_in_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_061_failed_extension_count_medium_swing_in_252d},
    "f08_fibx_062_high_to_close_distance_above_1_618_medium_swing_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_062_high_to_close_distance_above_1_618_medium_swing_atr},
    "f08_fibx_063_wick_above_1_618_medium_swing_indicator": {"inputs": ["high", "low", "close"], "func": f08_fibx_063_wick_above_1_618_medium_swing_indicator},
    "f08_fibx_064_low_breakdown_below_swing_low_long": {"inputs": ["high", "low", "close"], "func": f08_fibx_064_low_breakdown_below_swing_low_long},
    "f08_fibx_065_extension_ratio_medium_over_long": {"inputs": ["high", "low", "close"], "func": f08_fibx_065_extension_ratio_medium_over_long},
    "f08_fibx_066_extension_sign_disagreement_medium_vs_long": {"inputs": ["high", "low", "close"], "func": f08_fibx_066_extension_sign_disagreement_medium_vs_long},
    "f08_fibx_067_extension_acceleration_medium_swing_21d": {"inputs": ["high", "low", "close"], "func": f08_fibx_067_extension_acceleration_medium_swing_21d},
    "f08_fibx_068_log_progress_speed_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_068_log_progress_speed_medium_swing},
    "f08_fibx_069_multi_leg_extension_ratio_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_069_multi_leg_extension_ratio_medium_swing},
    "f08_fibx_070_abcd_extension_pattern_match_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_070_abcd_extension_pattern_match_medium_swing},
    "f08_fibx_071_abcd_overshoot_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_071_abcd_overshoot_medium_swing},
    "f08_fibx_072_measured_move_excess_medium_swing_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_072_measured_move_excess_medium_swing_atr},
    "f08_fibx_073_log_dist_above_1_5_ext_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_073_log_dist_above_1_5_ext_medium_swing},
    "f08_fibx_074_log_dist_above_1_786_ext_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_074_log_dist_above_1_786_ext_medium_swing},
    "f08_fibx_075_cumulative_extension_score_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_075_cumulative_extension_score_medium_swing},
}
