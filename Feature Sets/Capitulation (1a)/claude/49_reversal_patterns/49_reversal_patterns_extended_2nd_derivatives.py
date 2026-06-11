"""
49_reversal_patterns — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended-base reversal-pattern features — velocity of extended patterns
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Each function is a 5-day diff, 21-day diff, pct_change, or rolling OLS slope of an
extended-base concept from 49_reversal_patterns_extended_001_075.py.
The underlying extended-base pattern logic is re-implemented inline (self-contained).
New extended patterns: stick sandwich, ladder bottom, matching low, bullish counterattack /
meeting line, bullish separating lines, unique three river bottom, concealing baby swallow,
homing pigeon, descending hawk, two-bar reversal / pivot-low, bullish breakaway, tower bottom,
fry-pan bottom (rounded bottom).
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _body_abs(o: pd.Series, c: pd.Series) -> pd.Series:
    return (c - o).abs()


def _range(h: pd.Series, l: pd.Series) -> pd.Series:
    return (h - l).replace(0, np.nan)


def _upper_wick(o: pd.Series, c: pd.Series, h: pd.Series) -> pd.Series:
    return h - pd.concat([o, c], axis=1).max(axis=1)


def _lower_wick(o: pd.Series, c: pd.Series, l: pd.Series) -> pd.Series:
    return pd.concat([o, c], axis=1).min(axis=1) - l


def _atr(c: pd.Series, h: pd.Series, l: pd.Series, w: int = 14) -> pd.Series:
    tr = pd.concat([
        h - l,
        (h - c.shift(1)).abs(),
        (l - c.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _near_low(c: pd.Series, l: pd.Series, lookback: int = 21) -> pd.Series:
    lo = _rolling_min(l, lookback)
    hi = _rolling_max(c, lookback)
    rng = (hi - lo).replace(0, np.nan)
    return (c - lo) / rng <= 0.10


def _near_52wk_low(c: pd.Series) -> pd.Series:
    low52 = _rolling_min(c, _TD_YEAR)
    return c <= low52 * 1.10


def _deep_drawdown(c: pd.Series, lookback: int = 63, threshold: float = 0.20) -> pd.Series:
    peak = _rolling_max(c, lookback)
    return c <= peak * (1.0 - threshold)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended-pattern base helpers (inline, self-contained) ────────────────────

def _stick_sandwich_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(2) < o.shift(2)
    bar2_bull = c.shift(1) > o.shift(1)
    bar2_above_bar1_close = c.shift(1) > c.shift(2)
    bar3_bear = c < o
    bar3_matches_bar1 = (c - c.shift(2)).abs() <= tol
    return (bar1_bear & bar2_bull & bar2_above_bar1_close & bar3_bear & bar3_matches_bar1)


def _ladder_bottom_flag(o, c, h, l):
    b1_bear = c.shift(4) < o.shift(4)
    b2_bear = c.shift(3) < o.shift(3)
    b3_bear = c.shift(2) < o.shift(2)
    b2_lower = c.shift(3) < c.shift(4)
    b3_lower = c.shift(2) < c.shift(3)
    atr14 = _atr(c, h, l, 14)
    b4_bear = c.shift(1) < o.shift(1)
    b4_upper_wick = _upper_wick(o.shift(1), c.shift(1), h.shift(1)) >= atr14 * 0.3
    b5_bull = c > o
    b5_gap_or_higher = o > o.shift(1)
    return (b1_bear & b2_bear & b3_bear & b2_lower & b3_lower
            & b4_bear & b4_upper_wick & b5_bull & b5_gap_or_higher)


def _matching_low_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(1) < o.shift(1)
    bar2_bear = c < o
    lows_match = (c - c.shift(1)).abs() <= tol
    both_declining = c.shift(1) < c.shift(2)
    return (bar1_bear & bar2_bear & lows_match & both_declining)


def _bullish_counterattack_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(1) < o.shift(1)
    bar1_large = _body_abs(o.shift(1), c.shift(1)) >= atr14 * 0.5
    bar2_bull = c > o
    bar2_opens_lower = o < c.shift(1)
    bar2_closes_at_bar1 = (c - c.shift(1)).abs() <= tol
    return (bar1_bear & bar1_large & bar2_bull & bar2_opens_lower & bar2_closes_at_bar1)


def _separating_lines_bull_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    tol = atr14 * 0.05
    bar1_bear = c.shift(1) < o.shift(1)
    bar2_bull = c > o
    opens_match = (o - o.shift(1)).abs() <= tol
    bar2_strong = _body_abs(o, c) >= atr14 * 0.6
    return (bar1_bear & bar2_bull & opens_match & bar2_strong)


def _unique_three_river_bottom_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    bar1_bear = c.shift(2) < o.shift(2)
    bar1_large = _body_abs(o.shift(2), c.shift(2)) >= atr14 * 0.5
    bar2_lower_low = l.shift(1) < l.shift(2)
    lw2 = _lower_wick(o.shift(1), c.shift(1), l.shift(1))
    body2 = _body_abs(o.shift(1), c.shift(1))
    bar2_has_lw = lw2 >= body2 * 1.5
    bar3_bull = c > o
    bar3_small = _body_abs(o, c) <= atr14 * 0.4
    bar3_inside_bar2 = (c <= pd.concat([o.shift(1), c.shift(1)], axis=1).max(axis=1))
    return (bar1_bear & bar1_large & bar2_lower_low & bar2_has_lw
            & bar3_bull & bar3_small & bar3_inside_bar2)


def _concealing_baby_swallow_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    tiny = atr14 * 0.05
    b1_bear = c.shift(3) < o.shift(3)
    b1_tiny_lw = _lower_wick(o.shift(3), c.shift(3), l.shift(3)) <= tiny
    b1_tiny_uw = _upper_wick(o.shift(3), c.shift(3), h.shift(3)) <= tiny
    b2_bear = c.shift(2) < o.shift(2)
    b2_tiny_lw = _lower_wick(o.shift(2), c.shift(2), l.shift(2)) <= tiny
    b2_tiny_uw = _upper_wick(o.shift(2), c.shift(2), h.shift(2)) <= tiny
    b3_bear = c.shift(1) < o.shift(1)
    b3_uw = _upper_wick(o.shift(1), c.shift(1), h.shift(1))
    b3_has_uw = b3_uw >= tiny * 2
    b4_bull = c > o
    b4_higher = c > o.shift(1)
    return (b1_bear & b1_tiny_lw & b1_tiny_uw
            & b2_bear & b2_tiny_lw & b2_tiny_uw
            & b3_bear & b3_has_uw
            & b4_bull & b4_higher)


def _homing_pigeon_flag(o, c, h, l):
    bar1_bear = c.shift(1) < o.shift(1)
    bar2_bear = c < o
    body1_top = o.shift(1)
    body1_bot = c.shift(1)
    b2_inside = (o < body1_top) & (o > body1_bot) & (c > body1_bot) & (c < body1_top)
    bar2_smaller = _body_abs(o, c) < _body_abs(o.shift(1), c.shift(1))
    return (bar1_bear & bar2_bear & b2_inside & bar2_smaller)


def _two_bar_reversal_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    bar1_bear = c.shift(1) < o.shift(1)
    bar1_large = _body_abs(o.shift(1), c.shift(1)) >= atr14 * 0.7
    bar2_bull = c > o
    bar2_large = _body_abs(o, c) >= atr14 * 0.7
    bar2_recovers = c >= (o.shift(1) + c.shift(1)) / 2.0
    return (bar1_bear & bar1_large & bar2_bull & bar2_large & bar2_recovers)


def _bullish_breakaway_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    b1_bear = c.shift(4) < o.shift(4)
    b1_large = _body_abs(o.shift(4), c.shift(4)) >= atr14 * 0.6
    b2_bear = c.shift(3) < o.shift(3)
    b3_bear = c.shift(2) < o.shift(2)
    b4_bear = c.shift(1) < o.shift(1)
    declining = (c.shift(3) < c.shift(4)) & (c.shift(2) < c.shift(3))
    b5_bull = c > o
    b5_large = _body_abs(o, c) >= atr14 * 0.6
    b5_recovers = c > c.shift(2)
    return (b1_bear & b1_large & b2_bear & b3_bear & b4_bear & declining
            & b5_bull & b5_large & b5_recovers)


def _tower_bottom_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    threshold = atr14 * 0.6
    b_minus4_large_bear = (_body_abs(o.shift(4), c.shift(4)) >= threshold) & (c.shift(4) < o.shift(4))
    b_minus3_large_bear = (_body_abs(o.shift(3), c.shift(3)) >= threshold) & (c.shift(3) < o.shift(3))
    b_minus2_small = _body_abs(o.shift(2), c.shift(2)) <= threshold * 0.5
    b_minus1_small = _body_abs(o.shift(1), c.shift(1)) <= threshold * 0.5
    today_large_bull = (c > o) & (_body_abs(o, c) >= threshold)
    return (b_minus4_large_bear & b_minus3_large_bear
            & b_minus2_small & b_minus1_small
            & today_large_bull)


def _frypan_bottom_flag(o, c, h, l):
    close_5_ago = c.shift(5)
    close_10_ago = c.shift(10)
    first_half_down = close_5_ago < close_10_ago
    second_half_up = c > close_5_ago
    win = 10
    min_10 = _rolling_min(c, win)
    midpoint_is_min = (c.shift(5) - min_10).abs() <= (c - min_10) * 0.5
    gap_up = o > c.shift(1)
    return (first_half_down & second_half_up & midpoint_is_min & gap_up)


def _all_extended_flag(o, c, h, l):
    total = (
        _stick_sandwich_flag(o, c, h, l).astype(float)
        + _ladder_bottom_flag(o, c, h, l).astype(float)
        + _matching_low_flag(o, c, h, l).astype(float)
        + _bullish_counterattack_flag(o, c, h, l).astype(float)
        + _separating_lines_bull_flag(o, c, h, l).astype(float)
        + _unique_three_river_bottom_flag(o, c, h, l).astype(float)
        + _concealing_baby_swallow_flag(o, c, h, l).astype(float)
        + _homing_pigeon_flag(o, c, h, l).astype(float)
        + _two_bar_reversal_flag(o, c, h, l).astype(float)
        + _bullish_breakaway_flag(o, c, h, l).astype(float)
        + _tower_bottom_flag(o, c, h, l).astype(float)
        + _frypan_bottom_flag(o, c, h, l).astype(float)
    )
    return (total > 0).astype(float)


# ── Extended 2nd-Derivative Feature Functions extdrv2_001-025 ────────────────

# --- Group A (extdrv2_001-006): 5-day diffs of extended pattern counts ---

def rev_extdrv2_001_stick_sandwich_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day stick sandwich count (velocity of stick sandwich frequency)."""
    count = _rolling_sum(_stick_sandwich_flag(open, close, high, low).astype(float), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_extdrv2_002_matching_low_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day matching low count (velocity of matching low frequency)."""
    count = _rolling_sum(_matching_low_flag(open, close, high, low).astype(float), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_extdrv2_003_homing_pigeon_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day homing pigeon count (velocity of homing pigeon frequency)."""
    count = _rolling_sum(_homing_pigeon_flag(open, close, high, low).astype(float), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_extdrv2_004_two_bar_reversal_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day two-bar reversal count (velocity of two-bar pivot-low frequency)."""
    count = _rolling_sum(_two_bar_reversal_flag(open, close, high, low).astype(float), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_extdrv2_005_any_extended_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day any-extended-pattern count (velocity of extended pattern activity)."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_extdrv2_006_any_extended_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day any-extended-pattern count (monthly velocity of extended patterns)."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_QTR)
    return count.diff(_TD_MON)


# --- Group B (extdrv2_007-012): OLS slopes of extended pattern counts ---

def rev_extdrv2_007_any_extended_count_21d_slope_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 21-day extended pattern count over trailing 21 days."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    return _linslope(count, _TD_MON)


def rev_extdrv2_008_any_extended_count_63d_slope_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 63-day extended pattern count over trailing 63 days."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_QTR)
    return _linslope(count, _TD_QTR)


def rev_extdrv2_009_two_bar_reversal_count_63d_slope_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 63-day two-bar reversal count over trailing 63 days."""
    count = _rolling_sum(_two_bar_reversal_flag(open, close, high, low).astype(float), _TD_QTR)
    return _linslope(count, _TD_QTR)


def rev_extdrv2_010_tower_bottom_count_63d_slope_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 63-day tower bottom count over trailing 63 days."""
    count = _rolling_sum(_tower_bottom_flag(open, close, high, low).astype(float), _TD_QTR)
    return _linslope(count, _TD_QTR)


def rev_extdrv2_011_bullish_counterattack_count_21d_slope_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 21-day bullish counterattack count over trailing 21 days."""
    count = _rolling_sum(_bullish_counterattack_flag(open, close, high, low).astype(float), _TD_MON)
    return _linslope(count, _TD_MON)


def rev_extdrv2_012_separating_lines_count_21d_slope_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 21-day separating lines count over trailing 21 days."""
    count = _rolling_sum(_separating_lines_bull_flag(open, close, high, low).astype(float), _TD_MON)
    return _linslope(count, _TD_MON)


# --- Group C (extdrv2_013-018): EWM recency diffs of extended patterns ---

def rev_extdrv2_013_stick_sandwich_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day EWM-decayed stick sandwich signal (velocity of recency)."""
    ewm_score = _stick_sandwich_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_extdrv2_014_two_bar_reversal_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day EWM-decayed two-bar reversal signal."""
    ewm_score = _two_bar_reversal_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_extdrv2_015_any_extended_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day EWM-decayed any-extended-pattern signal."""
    ewm_score = _all_extended_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_extdrv2_016_any_extended_recency_ewm_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day EWM-decayed any-extended-pattern signal."""
    ewm_score = _all_extended_flag(open, close, high, low).ewm(span=_TD_QTR, min_periods=1).mean()
    return ewm_score.diff(_TD_MON)


def rev_extdrv2_017_frypan_bottom_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day EWM-decayed fry-pan bottom signal."""
    ewm_score = _frypan_bottom_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_extdrv2_018_homing_pigeon_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day EWM-decayed homing pigeon signal."""
    ewm_score = _homing_pigeon_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


# --- Group D (extdrv2_019-025): Volume-adjusted and composite diffs ---

def rev_extdrv2_019_extended_vol_weighted_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day volume-weighted extended pattern score (velocity of quality)."""
    flag = _all_extended_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_MON)
    return score.diff(_TD_WEEK)


def rev_extdrv2_020_extended_vol_weighted_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of 63-day volume-weighted extended pattern score."""
    flag = _all_extended_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_QTR)
    return score.diff(_TD_MON)


def rev_extdrv2_021_extended_near_low_density_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 63-day density of extended patterns firing near the 21-day low."""
    near = _near_low(close, low, _TD_MON)
    flag = _all_extended_flag(open, close, high, low).astype(bool)
    density = _rolling_mean((flag & near).astype(float), _TD_QTR)
    return density.diff(_TD_WEEK)


def rev_extdrv2_022_extended_zscore_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of z-score of 21-day extended pattern count (velocity of extremity)."""
    count21 = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    z = _safe_div(count21 - m, s)
    return z.diff(_TD_WEEK)


def rev_extdrv2_023_extended_density_252d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 252-day extended pattern density (long-run trend velocity)."""
    density = _rolling_mean(_all_extended_flag(open, close, high, low), _TD_YEAR)
    return density.diff(_TD_MON)


def rev_extdrv2_024_composite_ext_recency_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of composite EWM score across 6 core extended patterns (velocity of composite)."""
    ss = _stick_sandwich_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    ml = _matching_low_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    hp = _homing_pigeon_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    tbr = _two_bar_reversal_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    tb = _tower_bottom_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    fp = _frypan_bottom_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    composite = (ss + ml + hp + tbr + tb + fp) / 6.0
    return composite.diff(_TD_WEEK)


def rev_extdrv2_025_extended_cluster_21d_density_slope_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 21-day extended-pattern cluster flag density over trailing 21 days."""
    count21 = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    cluster = (count21 >= 3).astype(float)
    return _linslope(cluster, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "rev_extdrv2_001_stick_sandwich_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_001_stick_sandwich_count_21d_5d_diff},
    "rev_extdrv2_002_matching_low_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_002_matching_low_count_21d_5d_diff},
    "rev_extdrv2_003_homing_pigeon_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_003_homing_pigeon_count_21d_5d_diff},
    "rev_extdrv2_004_two_bar_reversal_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_004_two_bar_reversal_count_21d_5d_diff},
    "rev_extdrv2_005_any_extended_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_005_any_extended_count_21d_5d_diff},
    "rev_extdrv2_006_any_extended_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_006_any_extended_count_63d_21d_diff},
    "rev_extdrv2_007_any_extended_count_21d_slope_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_007_any_extended_count_21d_slope_21d},
    "rev_extdrv2_008_any_extended_count_63d_slope_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_008_any_extended_count_63d_slope_63d},
    "rev_extdrv2_009_two_bar_reversal_count_63d_slope_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_009_two_bar_reversal_count_63d_slope_63d},
    "rev_extdrv2_010_tower_bottom_count_63d_slope_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_010_tower_bottom_count_63d_slope_63d},
    "rev_extdrv2_011_bullish_counterattack_count_21d_slope_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_011_bullish_counterattack_count_21d_slope_21d},
    "rev_extdrv2_012_separating_lines_count_21d_slope_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_012_separating_lines_count_21d_slope_21d},
    "rev_extdrv2_013_stick_sandwich_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_013_stick_sandwich_recency_ewm_5d_diff},
    "rev_extdrv2_014_two_bar_reversal_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_014_two_bar_reversal_recency_ewm_5d_diff},
    "rev_extdrv2_015_any_extended_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_015_any_extended_recency_ewm_5d_diff},
    "rev_extdrv2_016_any_extended_recency_ewm_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_016_any_extended_recency_ewm_21d_diff},
    "rev_extdrv2_017_frypan_bottom_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_017_frypan_bottom_recency_ewm_5d_diff},
    "rev_extdrv2_018_homing_pigeon_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_018_homing_pigeon_recency_ewm_5d_diff},
    "rev_extdrv2_019_extended_vol_weighted_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_extdrv2_019_extended_vol_weighted_count_21d_5d_diff},
    "rev_extdrv2_020_extended_vol_weighted_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_extdrv2_020_extended_vol_weighted_count_63d_21d_diff},
    "rev_extdrv2_021_extended_near_low_density_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_021_extended_near_low_density_5d_diff},
    "rev_extdrv2_022_extended_zscore_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_022_extended_zscore_21d_5d_diff},
    "rev_extdrv2_023_extended_density_252d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_023_extended_density_252d_21d_diff},
    "rev_extdrv2_024_composite_ext_recency_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_024_composite_ext_recency_5d_diff},
    "rev_extdrv2_025_extended_cluster_21d_density_slope_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv2_025_extended_cluster_21d_density_slope_21d},
}
