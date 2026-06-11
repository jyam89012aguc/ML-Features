"""
49_reversal_patterns — Extended Features 001-075
Domain: intraday/multi-bar named reversal candlestick pattern recognition at/near lows
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

NEW canonical patterns: stick sandwich, ladder bottom, matching low, bullish counterattack /
meeting line, bullish separating lines, unique three river bottom, concealing baby swallow,
homing pigeon, descending hawk, two-bar reversal / pivot-low, bullish breakaway, tower bottom,
fry-pan bottom (rounded bottom).
Also: deep volume-confirmed / near-52wk-low / gap-context / strength-graded variants;
pattern-confluence scores; pattern-after-deep-drawdown context;
rate-of-change & acceleration of extended pattern frequency.
Self-contained (numpy/pandas only). No cross-file imports.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _body_abs(o: pd.Series, c: pd.Series) -> pd.Series:
    """Absolute candle body size."""
    return (c - o).abs()


def _range(h: pd.Series, l: pd.Series) -> pd.Series:
    """High-low range; zero replaced with NaN."""
    return (h - l).replace(0, np.nan)


def _upper_wick(o: pd.Series, c: pd.Series, h: pd.Series) -> pd.Series:
    """Upper shadow = high minus the higher of open/close."""
    return h - pd.concat([o, c], axis=1).max(axis=1)


def _lower_wick(o: pd.Series, c: pd.Series, l: pd.Series) -> pd.Series:
    """Lower shadow = the lower of open/close minus low."""
    return pd.concat([o, c], axis=1).min(axis=1) - l


def _atr(c: pd.Series, h: pd.Series, l: pd.Series, w: int = 14) -> pd.Series:
    """Average true range over w periods."""
    tr = pd.concat([
        h - l,
        (h - c.shift(1)).abs(),
        (l - c.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _near_low(c: pd.Series, l: pd.Series, lookback: int = 21) -> pd.Series:
    """Flag: today's close is within bottom 10% of lookback-day range."""
    lo = _rolling_min(l, lookback)
    hi = _rolling_max(c, lookback)
    rng = (hi - lo).replace(0, np.nan)
    return (c - lo) / rng <= 0.10


def _days_since(flag: pd.Series) -> pd.Series:
    """Days elapsed since most recent True bar (backward-looking only)."""
    idx = np.arange(len(flag))
    result = pd.Series(np.nan, index=flag.index, dtype=float)
    last = np.nan
    for i, f in zip(idx, flag):
        if f:
            last = i
        result.iloc[i] = i - last if not np.isnan(last) else np.nan
    return result


def _near_52wk_low(c: pd.Series) -> pd.Series:
    """Flag: close within 10% of 252-day closing low."""
    low52 = _rolling_min(c, _TD_YEAR)
    return c <= low52 * 1.10


def _deep_drawdown(c: pd.Series, lookback: int = 63, threshold: float = 0.20) -> pd.Series:
    """Flag: close is at least threshold % below its lookback-period high (deep drawdown)."""
    peak = _rolling_max(c, lookback)
    return c <= peak * (1.0 - threshold)


# ── New-pattern base helpers (self-contained, no cross-file imports) ───────────

def _stick_sandwich_flag(o, c, h, l):
    """
    Stick sandwich: bar1 bear close X, bar2 bull closing above X, bar3 bear closing AT X.
    Last bar (bar3) closes at same level as bar1 (within ATR tolerance).
    Confirmed on bar3.
    """
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(2) < o.shift(2)
    bar2_bull = c.shift(1) > o.shift(1)
    bar2_above_bar1_close = c.shift(1) > c.shift(2)
    bar3_bear = c < o
    bar3_matches_bar1 = (c - c.shift(2)).abs() <= tol
    return (bar1_bear & bar2_bull & bar2_above_bar1_close & bar3_bear & bar3_matches_bar1)


def _ladder_bottom_flag(o, c, h, l):
    """
    Ladder bottom: three consecutive bear bars with lower closes, then small bear bar with upper
    wick, then bullish gap-up bar. Confirmed on bar5.
    """
    b1_bear = c.shift(4) < o.shift(4)
    b2_bear = c.shift(3) < o.shift(3)
    b3_bear = c.shift(2) < o.shift(2)
    b2_lower = c.shift(3) < c.shift(4)
    b3_lower = c.shift(2) < c.shift(3)
    atr14 = _atr(c, h, l, 14)
    # bar4: small bear body with meaningful upper wick
    b4_bear = c.shift(1) < o.shift(1)
    b4_upper_wick = _upper_wick(o.shift(1), c.shift(1), h.shift(1)) >= atr14 * 0.3
    # bar5: bullish, opens above bar4 open
    b5_bull = c > o
    b5_gap_or_higher = o > o.shift(1)
    return (b1_bear & b2_bear & b3_bear & b2_lower & b3_lower
            & b4_bear & b4_upper_wick & b5_bull & b5_gap_or_higher)


def _matching_low_flag(o, c, h, l):
    """
    Matching low: two consecutive bear bars with equal (or near-equal) closes.
    Both bars must close lower than prior bar; closes match within tight tolerance.
    """
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(1) < o.shift(1)
    bar2_bear = c < o
    lows_match = (c - c.shift(1)).abs() <= tol
    both_declining = c.shift(1) < c.shift(2)
    return (bar1_bear & bar2_bear & lows_match & both_declining)


def _bullish_counterattack_flag(o, c, h, l):
    """
    Bullish counterattack / meeting line: bar1 is a large bear, bar2 is bull that
    closes at the same level as bar1 close (within tolerance). Opening gap down.
    """
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(1) < o.shift(1)
    bar1_large = _body_abs(o.shift(1), c.shift(1)) >= atr14 * 0.5
    bar2_bull = c > o
    bar2_opens_lower = o < c.shift(1)
    bar2_closes_at_bar1 = (c - c.shift(1)).abs() <= tol
    return (bar1_bear & bar1_large & bar2_bull & bar2_opens_lower & bar2_closes_at_bar1)


def _separating_lines_bull_flag(o, c, h, l):
    """
    Bullish separating lines: bar1 bearish, bar2 opens at the same level as bar1 open
    (within tolerance) but is strongly bullish (long body, closes well above bar1 open).
    """
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(1) < o.shift(1)
    bar2_bull = c > o
    opens_match = (o - o.shift(1)).abs() <= tol
    bar2_strong = _body_abs(o, c) >= atr14 * 0.6
    return (bar1_bear & bar2_bull & opens_match & bar2_strong)


def _unique_three_river_bottom_flag(o, c, h, l):
    """
    Unique three river bottom: bar1 large bear, bar2 hammer-like with lower low,
    bar3 small bull body closing inside bar2 body.
    """
    atr14 = _atr(c, h, l, 14)
    bar1_bear = c.shift(2) < o.shift(2)
    bar1_large = _body_abs(o.shift(2), c.shift(2)) >= atr14 * 0.5
    # bar2: lower low than bar1, long lower wick
    bar2_lower_low = l.shift(1) < l.shift(2)
    lw2 = _lower_wick(o.shift(1), c.shift(1), l.shift(1))
    body2 = _body_abs(o.shift(1), c.shift(1))
    bar2_has_lw = lw2 >= body2 * 1.5
    # bar3: small bull body, closes within bar2's body range
    bar3_bull = c > o
    bar3_small = _body_abs(o, c) <= atr14 * 0.4
    bar3_inside_bar2 = (c <= pd.concat([o.shift(1), c.shift(1)], axis=1).max(axis=1))
    return (bar1_bear & bar1_large & bar2_lower_low & bar2_has_lw
            & bar3_bull & bar3_small & bar3_inside_bar2)


def _concealing_baby_swallow_flag(o, c, h, l):
    """
    Concealing baby swallow: two marubozu (no-wick) bear bars, then small bear bar with
    upper wick that is engulfed inside the prior bar, then fourth bull bar closing up.
    Confirmed on bar4.
    """
    atr14 = _atr(c, h, l, 14)
    tiny = atr14 * 0.05
    # bar1, bar2: strong bear marubozu (tiny wicks)
    b1_bear = c.shift(3) < o.shift(3)
    b1_tiny_lw = _lower_wick(o.shift(3), c.shift(3), l.shift(3)) <= tiny
    b1_tiny_uw = _upper_wick(o.shift(3), c.shift(3), h.shift(3)) <= tiny
    b2_bear = c.shift(2) < o.shift(2)
    b2_tiny_lw = _lower_wick(o.shift(2), c.shift(2), l.shift(2)) <= tiny
    b2_tiny_uw = _upper_wick(o.shift(2), c.shift(2), h.shift(2)) <= tiny
    # bar3: small bear with upper wick that protrudes above bar2 body
    b3_bear = c.shift(1) < o.shift(1)
    b3_uw = _upper_wick(o.shift(1), c.shift(1), h.shift(1))
    b3_has_uw = b3_uw >= tiny * 2
    # bar4: bull, closes above bar3 open
    b4_bull = c > o
    b4_higher = c > o.shift(1)
    return (b1_bear & b1_tiny_lw & b1_tiny_uw
            & b2_bear & b2_tiny_lw & b2_tiny_uw
            & b3_bear & b3_has_uw
            & b4_bull & b4_higher)


def _homing_pigeon_flag(o, c, h, l):
    """
    Homing pigeon: bar1 large bear, bar2 smaller bear with body fully inside bar1's body.
    Both bars bearish; bar2 body contained within bar1 body (bearish harami-like but both bear).
    """
    bar1_bear = c.shift(1) < o.shift(1)
    bar2_bear = c < o
    body1_top = o.shift(1)
    body1_bot = c.shift(1)
    # bar2 body must be inside bar1 body
    b2_inside = (o < body1_top) & (o > body1_bot) & (c > body1_bot) & (c < body1_top)
    bar2_smaller = _body_abs(o, c) < _body_abs(o.shift(1), c.shift(1))
    return (bar1_bear & bar2_bear & b2_inside & bar2_smaller)


def _descending_hawk_flag(o, c, h, l):
    """
    Descending hawk (bearish, but signals exhaustion at bottom — bullish reversal context):
    bar1 large bull, bar2 smaller bull inside bar1's range (or opening within) — signals
    waning momentum. Used as a capitulation-reversal precursor: flag when this fires
    AND the next bar (bar3=today) is bullish and closes above bar2.
    Confirmed on bar3.
    """
    bar1_bull = c.shift(2) > o.shift(2)
    bar1_large = _body_abs(o.shift(2), c.shift(2)) >= _atr(c, h, l, 14) * 0.5
    bar2_bull = c.shift(1) > o.shift(1)
    bar2_smaller = _body_abs(o.shift(1), c.shift(1)) < _body_abs(o.shift(2), c.shift(2))
    bar2_inside = (o.shift(1) > o.shift(2)) & (c.shift(1) < c.shift(2))
    # Confirming bar: bullish, reclaims above bar2
    bar3_bull = c > o
    bar3_above = c > c.shift(1)
    return (bar1_bull & bar1_large & bar2_bull & bar2_smaller & bar2_inside
            & bar3_bull & bar3_above)


def _two_bar_reversal_flag(o, c, h, l):
    """
    Two-bar reversal / pivot-low: large bear bar followed immediately by a large bull bar
    of comparable size, forming a V-shaped reversal. Both bars have substantial bodies.
    """
    atr14 = _atr(c, h, l, 14)
    bar1_bear = c.shift(1) < o.shift(1)
    bar1_large = _body_abs(o.shift(1), c.shift(1)) >= atr14 * 0.7
    bar2_bull = c > o
    bar2_large = _body_abs(o, c) >= atr14 * 0.7
    # Bar2 should engulf or largely recover bar1
    bar2_recovers = c >= (o.shift(1) + c.shift(1)) / 2.0
    return (bar1_bear & bar1_large & bar2_bull & bar2_large & bar2_recovers)


def _bullish_breakaway_flag(o, c, h, l):
    """
    Bullish breakaway: 5-bar pattern. Bar1 large bear, bars 2-4 small bears drifting lower
    (gapping or stepping down), bar5 large bull closing well back into bar1's range.
    Confirmed on bar5.
    """
    atr14 = _atr(c, h, l, 14)
    b1_bear = c.shift(4) < o.shift(4)
    b1_large = _body_abs(o.shift(4), c.shift(4)) >= atr14 * 0.6
    # bars 2-4 all bear or flat, each closing lower than or near prior
    b2_bear = c.shift(3) < o.shift(3)
    b3_bear = c.shift(2) < o.shift(2)
    b4_bear = c.shift(1) < o.shift(1)
    declining = (c.shift(3) < c.shift(4)) & (c.shift(2) < c.shift(3))
    # bar5: large bull, closes well above bar4 close
    b5_bull = c > o
    b5_large = _body_abs(o, c) >= atr14 * 0.6
    b5_recovers = c > c.shift(2)
    return (b1_bear & b1_large & b2_bear & b3_bear & b4_bear & declining
            & b5_bull & b5_large & b5_recovers)


def _tower_bottom_flag(o, c, h, l):
    """
    Tower bottom: prolonged downtrend (several large bear bars) followed by small bars
    (congestion at the bottom), then several large bull bars surging up.
    Simplified detection: 2 large bears in bars 3-4 ago, then today is a large bull.
    """
    atr14 = _atr(c, h, l, 14)
    threshold = atr14 * 0.6
    # Two large bear bars in the recent past (shifts 3 and 4)
    b_minus4_large_bear = (_body_abs(o.shift(4), c.shift(4)) >= threshold) & (c.shift(4) < o.shift(4))
    b_minus3_large_bear = (_body_abs(o.shift(3), c.shift(3)) >= threshold) & (c.shift(3) < o.shift(3))
    # Small bars in congestion zone (bars 2-1 ago)
    b_minus2_small = _body_abs(o.shift(2), c.shift(2)) <= threshold * 0.5
    b_minus1_small = _body_abs(o.shift(1), c.shift(1)) <= threshold * 0.5
    # Today: large bull
    today_large_bull = (c > o) & (_body_abs(o, c) >= threshold)
    return (b_minus4_large_bear & b_minus3_large_bear
            & b_minus2_small & b_minus1_small
            & today_large_bull)


def _frypan_bottom_flag(o, c, h, l):
    """
    Fry-pan / rounded bottom: gradual curving low over a multi-bar window, then gap-up.
    Detection: 10-bar rolling low of close is declining for 5 bars then rising, plus today
    gaps up above prior close. Approximated from trailing data only.
    """
    # Proxy: close has been declining for first half, rising for second half of window
    win = 10
    close_5_ago = c.shift(5)
    close_10_ago = c.shift(10)
    # First half declining
    first_half_down = close_5_ago < close_10_ago
    # Second half rising
    second_half_up = c > close_5_ago
    # Rounded shape: min of window is near the midpoint (5 bars ago)
    min_10 = _rolling_min(c, win)
    midpoint_is_min = (c.shift(5) - min_10).abs() <= (c - min_10) * 0.5
    # Gap up today
    gap_up = o > c.shift(1)
    return (first_half_down & second_half_up & midpoint_is_min & gap_up)


def _all_extended_flag(o, c, h, l):
    """Union of all 13 extended canonical patterns."""
    total = (
        _stick_sandwich_flag(o, c, h, l).astype(float)
        + _ladder_bottom_flag(o, c, h, l).astype(float)
        + _matching_low_flag(o, c, h, l).astype(float)
        + _bullish_counterattack_flag(o, c, h, l).astype(float)
        + _separating_lines_bull_flag(o, c, h, l).astype(float)
        + _unique_three_river_bottom_flag(o, c, h, l).astype(float)
        + _concealing_baby_swallow_flag(o, c, h, l).astype(float)
        + _homing_pigeon_flag(o, c, h, l).astype(float)
        + _descending_hawk_flag(o, c, h, l).astype(float)
        + _two_bar_reversal_flag(o, c, h, l).astype(float)
        + _bullish_breakaway_flag(o, c, h, l).astype(float)
        + _tower_bottom_flag(o, c, h, l).astype(float)
        + _frypan_bottom_flag(o, c, h, l).astype(float)
    )
    return (total > 0).astype(float)


# ── Feature functions rev_ext_001 – rev_ext_075 ───────────────────────────────

# --- Group A (001-010): Stick Sandwich ---

def rev_ext_001_stick_sandwich_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: stick sandwich — two bear bars at same close price sandwiching a bull bar."""
    return _stick_sandwich_flag(open, close, high, low).astype(float)


def rev_ext_002_stick_sandwich_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Stick sandwich completing at/near the 21-day closing low."""
    pat = _stick_sandwich_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_003_stick_sandwich_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Stick sandwich within 10% of the 252-day closing low."""
    pat = _stick_sandwich_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_004_stick_sandwich_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Stick sandwich where bar3 (today) volume exceeds 21-day average."""
    pat = _stick_sandwich_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


def rev_ext_005_stick_sandwich_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of stick sandwich patterns completing in trailing 63 days."""
    return _rolling_sum(rev_ext_001_stick_sandwich_flag(open, close, high, low), _TD_QTR)


def rev_ext_006_stick_sandwich_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent stick sandwich pattern."""
    flag = rev_ext_001_stick_sandwich_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group B (007-012): Ladder Bottom ---

def rev_ext_007_ladder_bottom_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: ladder bottom — 3 declining bear bars, small bear with upper wick, then bull gap-up."""
    return _ladder_bottom_flag(open, close, high, low).astype(float)


def rev_ext_008_ladder_bottom_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Ladder bottom completing at/near the 21-day closing low."""
    pat = _ladder_bottom_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_009_ladder_bottom_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Ladder bottom within 10% of 252-day closing low."""
    pat = _ladder_bottom_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_010_ladder_bottom_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Ladder bottom where bar5 (today) volume exceeds 21-day average."""
    pat = _ladder_bottom_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


def rev_ext_011_ladder_bottom_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of ladder bottom patterns completing in trailing 252 days."""
    return _rolling_sum(rev_ext_007_ladder_bottom_flag(open, close, high, low), _TD_YEAR)


def rev_ext_012_ladder_bottom_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent ladder bottom pattern."""
    flag = rev_ext_007_ladder_bottom_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group C (013-018): Matching Low ---

def rev_ext_013_matching_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: matching low — two consecutive bear bars closing at the same level (support test)."""
    return _matching_low_flag(open, close, high, low).astype(float)


def rev_ext_014_matching_low_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Matching low at/near the 21-day closing low."""
    pat = _matching_low_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_015_matching_low_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Matching low within 10% of 252-day closing low."""
    pat = _matching_low_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_016_matching_low_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of matching low patterns in trailing 63 days."""
    return _rolling_sum(rev_ext_013_matching_low_flag(open, close, high, low), _TD_QTR)


def rev_ext_017_matching_low_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Matching low where today's volume exceeds yesterday's (fresh selling absorbed)."""
    pat = _matching_low_flag(open, close, high, low)
    vol_up = volume >= volume.shift(1)
    return (pat & vol_up).astype(float)


def rev_ext_018_matching_low_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent matching low pattern."""
    flag = rev_ext_013_matching_low_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group D (019-025): Bullish Counterattack / Meeting Line ---

def rev_ext_019_bullish_counterattack_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish counterattack — bear bar, then bull bar closing at same level (price support)."""
    return _bullish_counterattack_flag(open, close, high, low).astype(float)


def rev_ext_020_bullish_counterattack_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish counterattack at/near the 21-day closing low."""
    pat = _bullish_counterattack_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_021_bullish_counterattack_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish counterattack within 10% of 252-day closing low."""
    pat = _bullish_counterattack_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_022_bullish_counterattack_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish counterattack with above-average volume on the bull bar."""
    pat = _bullish_counterattack_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


def rev_ext_023_bullish_counterattack_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish counterattack patterns in trailing 63 days."""
    return _rolling_sum(rev_ext_019_bullish_counterattack_flag(open, close, high, low), _TD_QTR)


def rev_ext_024_bullish_counterattack_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent bullish counterattack pattern."""
    flag = rev_ext_019_bullish_counterattack_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_ext_025_bullish_counterattack_body_strength(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """On counterattack days: bull-bar body ATR-normalized (strength of the counter); else 0."""
    flag = _bullish_counterattack_flag(open, close, high, low)
    atr14 = _atr(close, high, low, 14)
    strength = _safe_div(_body_abs(open, close), atr14)
    return strength.where(flag, 0.0)


# --- Group E (026-031): Bullish Separating Lines ---

def rev_ext_026_separating_lines_bull_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish separating lines — bar1 bear, bar2 opens at same level as bar1 open, surges up."""
    return _separating_lines_bull_flag(open, close, high, low).astype(float)


def rev_ext_027_separating_lines_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish separating lines at/near the 21-day closing low."""
    pat = _separating_lines_bull_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_028_separating_lines_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish separating lines within 10% of 252-day closing low."""
    pat = _separating_lines_bull_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_029_separating_lines_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish separating lines with today's volume above 21-day average."""
    pat = _separating_lines_bull_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


def rev_ext_030_separating_lines_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bullish separating line patterns in trailing 63 days."""
    return _rolling_sum(rev_ext_026_separating_lines_bull_flag(open, close, high, low), _TD_QTR)


def rev_ext_031_separating_lines_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent bullish separating lines pattern."""
    flag = rev_ext_026_separating_lines_bull_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group F (032-037): Unique Three River Bottom ---

def rev_ext_032_unique_three_river_bottom_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: unique three river bottom — large bear, hammer-like, small bull inside bar2."""
    return _unique_three_river_bottom_flag(open, close, high, low).astype(float)


def rev_ext_033_unique_three_river_bottom_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Unique three river bottom at/near the 21-day closing low."""
    pat = _unique_three_river_bottom_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_034_unique_three_river_bottom_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Unique three river bottom within 10% of 252-day closing low."""
    pat = _unique_three_river_bottom_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_035_unique_three_river_bottom_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of unique three river bottom patterns in trailing 252 days."""
    return _rolling_sum(rev_ext_032_unique_three_river_bottom_flag(open, close, high, low), _TD_YEAR)


def rev_ext_036_unique_three_river_bottom_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent unique three river bottom pattern."""
    flag = rev_ext_032_unique_three_river_bottom_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


def rev_ext_037_unique_three_river_bottom_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Unique three river bottom with bar3 volume above 21-day average."""
    pat = _unique_three_river_bottom_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


# --- Group G (038-041): Homing Pigeon & Concealing Baby Swallow ---

def rev_ext_038_homing_pigeon_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: homing pigeon — large bear bar, smaller bear bar fully inside larger (dual-bear harami)."""
    return _homing_pigeon_flag(open, close, high, low).astype(float)


def rev_ext_039_homing_pigeon_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Homing pigeon at/near the 21-day closing low."""
    pat = _homing_pigeon_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_040_concealing_baby_swallow_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: concealing baby swallow — two marubozu bears, small wick-bar, then bull recovery."""
    return _concealing_baby_swallow_flag(open, close, high, low).astype(float)


def rev_ext_041_concealing_baby_swallow_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Concealing baby swallow within 10% of 252-day closing low."""
    pat = _concealing_baby_swallow_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


# --- Group H (042-047): Descending Hawk (confirming bar) & Two-Bar Reversal ---

def rev_ext_042_descending_hawk_confirm_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: descending hawk exhaustion confirmed — waning bull momentum followed by bull recovery."""
    return _descending_hawk_flag(open, close, high, low).astype(float)


def rev_ext_043_descending_hawk_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Descending hawk confirming bar at/near the 21-day closing low."""
    pat = _descending_hawk_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_044_two_bar_reversal_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: two-bar reversal / pivot-low — large bear bar followed by large bull bar (V-reversal)."""
    return _two_bar_reversal_flag(open, close, high, low).astype(float)


def rev_ext_045_two_bar_reversal_near_low_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Two-bar reversal at/near the 21-day closing low."""
    pat = _two_bar_reversal_flag(open, close, high, low)
    near = _near_low(close, low, _TD_MON)
    return (pat & near).astype(float)


def rev_ext_046_two_bar_reversal_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Two-bar reversal within 10% of 252-day closing low."""
    pat = _two_bar_reversal_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_047_two_bar_reversal_vol_spike(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Two-bar reversal where today's volume >= 150% of 21-day average (high conviction)."""
    pat = _two_bar_reversal_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume >= avg_vol * 1.5)).astype(float)


# --- Group I (048-053): Bullish Breakaway & Tower Bottom ---

def rev_ext_048_bullish_breakaway_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: bullish breakaway — 5-bar: large bear, 3 small bears drifting lower, large bull recovery."""
    return _bullish_breakaway_flag(open, close, high, low).astype(float)


def rev_ext_049_bullish_breakaway_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Bullish breakaway completing within 10% of 252-day closing low."""
    pat = _bullish_breakaway_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_050_bullish_breakaway_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Bullish breakaway where bar5 volume exceeds 21-day average."""
    pat = _bullish_breakaway_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


def rev_ext_051_tower_bottom_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: tower bottom — large bear towers, small congestion bars, large bull tower recovery."""
    return _tower_bottom_flag(open, close, high, low).astype(float)


def rev_ext_052_tower_bottom_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Tower bottom within 10% of 252-day closing low."""
    pat = _tower_bottom_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_053_tower_bottom_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent tower bottom pattern."""
    flag = rev_ext_051_tower_bottom_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group J (054-058): Fry-Pan Bottom ---

def rev_ext_054_frypan_bottom_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: fry-pan / rounded bottom — gradual curved low, then gap-up breakout."""
    return _frypan_bottom_flag(open, close, high, low).astype(float)


def rev_ext_055_frypan_bottom_near_52wk_low(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Fry-pan bottom completing within 10% of 252-day closing low."""
    pat = _frypan_bottom_flag(open, close, high, low)
    return (pat & _near_52wk_low(close)).astype(float)


def rev_ext_056_frypan_bottom_vol_confirm(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Fry-pan bottom where breakout day volume exceeds 21-day average."""
    pat = _frypan_bottom_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume > avg_vol)).astype(float)


def rev_ext_057_frypan_bottom_count_252d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of fry-pan bottom patterns completing in trailing 252 days."""
    return _rolling_sum(rev_ext_054_frypan_bottom_flag(open, close, high, low), _TD_YEAR)


def rev_ext_058_frypan_bottom_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since most recent fry-pan bottom breakout."""
    flag = rev_ext_054_frypan_bottom_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group K (059-064): Composite Extended Pattern Flags & Counts ---

def rev_ext_059_any_extended_pattern_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: any of the 13 net-new extended patterns fires on the current bar."""
    return _all_extended_flag(open, close, high, low)


def rev_ext_060_any_extended_pattern_count_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bars showing any extended pattern in trailing 21 days."""
    return _rolling_sum(rev_ext_059_any_extended_pattern_flag(open, close, high, low), _TD_MON)


def rev_ext_061_any_extended_pattern_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of bars showing any extended pattern in trailing 63 days."""
    return _rolling_sum(rev_ext_059_any_extended_pattern_flag(open, close, high, low), _TD_QTR)


def rev_ext_062_simultaneous_extended_pattern_count(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Number of distinct extended patterns simultaneously firing on today's bar."""
    return (
        _stick_sandwich_flag(open, close, high, low).astype(float)
        + _ladder_bottom_flag(open, close, high, low).astype(float)
        + _matching_low_flag(open, close, high, low).astype(float)
        + _bullish_counterattack_flag(open, close, high, low).astype(float)
        + _separating_lines_bull_flag(open, close, high, low).astype(float)
        + _unique_three_river_bottom_flag(open, close, high, low).astype(float)
        + _concealing_baby_swallow_flag(open, close, high, low).astype(float)
        + _homing_pigeon_flag(open, close, high, low).astype(float)
        + _descending_hawk_flag(open, close, high, low).astype(float)
        + _two_bar_reversal_flag(open, close, high, low).astype(float)
        + _bullish_breakaway_flag(open, close, high, low).astype(float)
        + _tower_bottom_flag(open, close, high, low).astype(float)
        + _frypan_bottom_flag(open, close, high, low).astype(float)
    )


def rev_ext_063_extended_pattern_cluster_21d_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Flag: 3 or more extended pattern bars within the last 21 days (cluster signal)."""
    count21 = rev_ext_060_any_extended_pattern_count_21d(open, close, high, low)
    return (count21 >= 3).astype(float)


def rev_ext_064_extended_pattern_days_since(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Days since the most recent bar with any extended pattern."""
    flag = rev_ext_059_any_extended_pattern_flag(open, close, high, low).astype(bool)
    return _days_since(flag)


# --- Group L (065-069): Pattern-Confluence and After-Drawdown Context ---

def rev_ext_065_extended_pattern_at_deep_drawdown_flag(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Extended pattern firing during deep drawdown (>= 20% below 63-day high)."""
    pat = rev_ext_059_any_extended_pattern_flag(open, close, high, low).astype(bool)
    dd = _deep_drawdown(close, lookback=_TD_QTR, threshold=0.20)
    return (pat & dd).astype(float)


def rev_ext_066_extended_pattern_after_5d_decline(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Extended pattern firing after 5 consecutive declining closes."""
    pat = rev_ext_059_any_extended_pattern_flag(open, close, high, low).astype(bool)
    five_d_decline = close.shift(1) < close.shift(6)
    return (pat & five_d_decline).astype(float)


def rev_ext_067_extended_pattern_vol_expansion(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Extended pattern with volume >= 2x 21-day average (high-conviction capitulation reversal)."""
    pat = rev_ext_059_any_extended_pattern_flag(open, close, high, low).astype(bool)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (pat & (volume >= avg_vol * 2.0)).astype(float)


def rev_ext_068_two_bar_reversal_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of two-bar reversal patterns in trailing 63 days."""
    return _rolling_sum(rev_ext_044_two_bar_reversal_flag(open, close, high, low), _TD_QTR)


def rev_ext_069_homing_pigeon_count_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Count of homing pigeon patterns in trailing 63 days."""
    return _rolling_sum(rev_ext_038_homing_pigeon_flag(open, close, high, low), _TD_QTR)


# --- Group M (070-075): ROC and Acceleration of Extended Pattern Frequency ---

def rev_ext_070_extended_pattern_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day extended pattern count (velocity of extended pattern activity)."""
    count = rev_ext_060_any_extended_pattern_count_21d(open, close, high, low)
    return count.diff(_TD_WEEK)


def rev_ext_071_extended_pattern_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day extended pattern count (monthly velocity)."""
    count = rev_ext_061_any_extended_pattern_count_63d(open, close, high, low)
    return count.diff(_TD_MON)


def rev_ext_072_extended_pattern_recency_ewm_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Exponentially decayed (21-day span) signal of any extended pattern (recency score)."""
    flag = rev_ext_059_any_extended_pattern_flag(open, close, high, low)
    return flag.ewm(span=_TD_MON, min_periods=1).mean()


def rev_ext_073_extended_pattern_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of the 21-day EWM extended pattern recency score (velocity of recency)."""
    ewm_score = rev_ext_072_extended_pattern_recency_ewm_21d(open, close, high, low)
    return ewm_score.diff(_TD_WEEK)


def rev_ext_074_extended_pattern_count_21d_accel(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day extended pattern count (acceleration of activity)."""
    count = rev_ext_060_any_extended_pattern_count_21d(open, close, high, low)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_ext_075_extended_pattern_composite_distress_index(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Composite distress index for extended patterns:
    EWM recency score * vol-norm * (1 + deep-drawdown flag).
    Captures capitulation quality of extended reversal signals.
    """
    recency = rev_ext_072_extended_pattern_recency_ewm_21d(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    dd_boost = 1.0 + _deep_drawdown(close, lookback=_TD_QTR, threshold=0.20).astype(float)
    return recency * vol_norm * dd_boost


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_EXTENDED_REGISTRY_001_075 = {
    "rev_ext_001_stick_sandwich_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_001_stick_sandwich_flag},
    "rev_ext_002_stick_sandwich_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_002_stick_sandwich_near_low_flag},
    "rev_ext_003_stick_sandwich_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_003_stick_sandwich_near_52wk_low},
    "rev_ext_004_stick_sandwich_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_004_stick_sandwich_vol_confirm},
    "rev_ext_005_stick_sandwich_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_005_stick_sandwich_count_63d},
    "rev_ext_006_stick_sandwich_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_006_stick_sandwich_days_since},
    "rev_ext_007_ladder_bottom_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_007_ladder_bottom_flag},
    "rev_ext_008_ladder_bottom_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_008_ladder_bottom_near_low_flag},
    "rev_ext_009_ladder_bottom_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_009_ladder_bottom_near_52wk_low},
    "rev_ext_010_ladder_bottom_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_010_ladder_bottom_vol_confirm},
    "rev_ext_011_ladder_bottom_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_011_ladder_bottom_count_252d},
    "rev_ext_012_ladder_bottom_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_012_ladder_bottom_days_since},
    "rev_ext_013_matching_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_013_matching_low_flag},
    "rev_ext_014_matching_low_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_014_matching_low_near_low_flag},
    "rev_ext_015_matching_low_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_015_matching_low_near_52wk_low},
    "rev_ext_016_matching_low_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_016_matching_low_count_63d},
    "rev_ext_017_matching_low_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_017_matching_low_vol_confirm},
    "rev_ext_018_matching_low_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_018_matching_low_days_since},
    "rev_ext_019_bullish_counterattack_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_019_bullish_counterattack_flag},
    "rev_ext_020_bullish_counterattack_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_020_bullish_counterattack_near_low_flag},
    "rev_ext_021_bullish_counterattack_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_021_bullish_counterattack_near_52wk_low},
    "rev_ext_022_bullish_counterattack_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_022_bullish_counterattack_vol_confirm},
    "rev_ext_023_bullish_counterattack_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_023_bullish_counterattack_count_63d},
    "rev_ext_024_bullish_counterattack_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_024_bullish_counterattack_days_since},
    "rev_ext_025_bullish_counterattack_body_strength": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_025_bullish_counterattack_body_strength},
    "rev_ext_026_separating_lines_bull_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_026_separating_lines_bull_flag},
    "rev_ext_027_separating_lines_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_027_separating_lines_near_low_flag},
    "rev_ext_028_separating_lines_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_028_separating_lines_near_52wk_low},
    "rev_ext_029_separating_lines_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_029_separating_lines_vol_confirm},
    "rev_ext_030_separating_lines_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_030_separating_lines_count_63d},
    "rev_ext_031_separating_lines_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_031_separating_lines_days_since},
    "rev_ext_032_unique_three_river_bottom_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_032_unique_three_river_bottom_flag},
    "rev_ext_033_unique_three_river_bottom_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_033_unique_three_river_bottom_near_low_flag},
    "rev_ext_034_unique_three_river_bottom_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_034_unique_three_river_bottom_near_52wk_low},
    "rev_ext_035_unique_three_river_bottom_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_035_unique_three_river_bottom_count_252d},
    "rev_ext_036_unique_three_river_bottom_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_036_unique_three_river_bottom_days_since},
    "rev_ext_037_unique_three_river_bottom_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_037_unique_three_river_bottom_vol_confirm},
    "rev_ext_038_homing_pigeon_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_038_homing_pigeon_flag},
    "rev_ext_039_homing_pigeon_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_039_homing_pigeon_near_low_flag},
    "rev_ext_040_concealing_baby_swallow_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_040_concealing_baby_swallow_flag},
    "rev_ext_041_concealing_baby_swallow_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_041_concealing_baby_swallow_near_52wk_low},
    "rev_ext_042_descending_hawk_confirm_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_042_descending_hawk_confirm_flag},
    "rev_ext_043_descending_hawk_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_043_descending_hawk_near_low_flag},
    "rev_ext_044_two_bar_reversal_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_044_two_bar_reversal_flag},
    "rev_ext_045_two_bar_reversal_near_low_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_045_two_bar_reversal_near_low_flag},
    "rev_ext_046_two_bar_reversal_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_046_two_bar_reversal_near_52wk_low},
    "rev_ext_047_two_bar_reversal_vol_spike": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_047_two_bar_reversal_vol_spike},
    "rev_ext_048_bullish_breakaway_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_048_bullish_breakaway_flag},
    "rev_ext_049_bullish_breakaway_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_049_bullish_breakaway_near_52wk_low},
    "rev_ext_050_bullish_breakaway_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_050_bullish_breakaway_vol_confirm},
    "rev_ext_051_tower_bottom_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_051_tower_bottom_flag},
    "rev_ext_052_tower_bottom_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_052_tower_bottom_near_52wk_low},
    "rev_ext_053_tower_bottom_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_053_tower_bottom_days_since},
    "rev_ext_054_frypan_bottom_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_054_frypan_bottom_flag},
    "rev_ext_055_frypan_bottom_near_52wk_low": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_055_frypan_bottom_near_52wk_low},
    "rev_ext_056_frypan_bottom_vol_confirm": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_056_frypan_bottom_vol_confirm},
    "rev_ext_057_frypan_bottom_count_252d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_057_frypan_bottom_count_252d},
    "rev_ext_058_frypan_bottom_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_058_frypan_bottom_days_since},
    "rev_ext_059_any_extended_pattern_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_059_any_extended_pattern_flag},
    "rev_ext_060_any_extended_pattern_count_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_060_any_extended_pattern_count_21d},
    "rev_ext_061_any_extended_pattern_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_061_any_extended_pattern_count_63d},
    "rev_ext_062_simultaneous_extended_pattern_count": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_062_simultaneous_extended_pattern_count},
    "rev_ext_063_extended_pattern_cluster_21d_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_063_extended_pattern_cluster_21d_flag},
    "rev_ext_064_extended_pattern_days_since": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_064_extended_pattern_days_since},
    "rev_ext_065_extended_pattern_at_deep_drawdown_flag": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_065_extended_pattern_at_deep_drawdown_flag},
    "rev_ext_066_extended_pattern_after_5d_decline": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_066_extended_pattern_after_5d_decline},
    "rev_ext_067_extended_pattern_vol_expansion": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_067_extended_pattern_vol_expansion},
    "rev_ext_068_two_bar_reversal_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_068_two_bar_reversal_count_63d},
    "rev_ext_069_homing_pigeon_count_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_069_homing_pigeon_count_63d},
    "rev_ext_070_extended_pattern_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_070_extended_pattern_count_21d_5d_diff},
    "rev_ext_071_extended_pattern_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_071_extended_pattern_count_63d_21d_diff},
    "rev_ext_072_extended_pattern_recency_ewm_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_072_extended_pattern_recency_ewm_21d},
    "rev_ext_073_extended_pattern_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_073_extended_pattern_recency_ewm_5d_diff},
    "rev_ext_074_extended_pattern_count_21d_accel": {"inputs": ["open", "close", "high", "low"], "func": rev_ext_074_extended_pattern_count_21d_accel},
    "rev_ext_075_extended_pattern_composite_distress_index": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_ext_075_extended_pattern_composite_distress_index},
}
