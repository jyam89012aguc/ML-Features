"""
49_reversal_patterns — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended-2nd-derivative features — acceleration of extended pattern velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Each function is a second diff / slope-of-slope / diff-of-slope of an extended-2nd-derivative
concept. The underlying extended-pattern logic is re-implemented inline (self-contained).
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
        + _matching_low_flag(o, c, h, l).astype(float)
        + _bullish_counterattack_flag(o, c, h, l).astype(float)
        + _separating_lines_bull_flag(o, c, h, l).astype(float)
        + _unique_three_river_bottom_flag(o, c, h, l).astype(float)
        + _homing_pigeon_flag(o, c, h, l).astype(float)
        + _two_bar_reversal_flag(o, c, h, l).astype(float)
        + _bullish_breakaway_flag(o, c, h, l).astype(float)
        + _tower_bottom_flag(o, c, h, l).astype(float)
        + _frypan_bottom_flag(o, c, h, l).astype(float)
    )
    return (total > 0).astype(float)


# ── Extended 3rd-Derivative Feature Functions extdrv3_001-025 ────────────────

# --- Group A (extdrv3_001-006): Second 5-day diffs of extended pattern counts ---

def rev_extdrv3_001_stick_sandwich_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day stick sandwich count (acceleration of sandwich frequency)."""
    count = _rolling_sum(_stick_sandwich_flag(open, close, high, low).astype(float), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_002_matching_low_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day matching low count (jerk in matching low frequency)."""
    count = _rolling_sum(_matching_low_flag(open, close, high, low).astype(float), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_003_homing_pigeon_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day homing pigeon count (acceleration of homing pigeon frequency)."""
    count = _rolling_sum(_homing_pigeon_flag(open, close, high, low).astype(float), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_004_two_bar_reversal_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day two-bar reversal count (acceleration of pivot-low frequency)."""
    count = _rolling_sum(_two_bar_reversal_flag(open, close, high, low).astype(float), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_005_any_extended_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day any-extended-pattern count (jerk in extended activity)."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_006_any_extended_count_63d_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 63-day any-extended count (cross-horizon acceleration)."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_QTR)
    vel21 = count.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- Group B (extdrv3_007-012): EWM signal second diffs (acceleration of recency) ---

def rev_extdrv3_007_stick_sandwich_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM stick sandwich signal (acceleration of recency velocity)."""
    ewm_score = _stick_sandwich_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_008_two_bar_reversal_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM two-bar reversal signal (acceleration of two-bar recency)."""
    ewm_score = _two_bar_reversal_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_009_any_extended_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day EWM any-extended-pattern signal (acceleration of recency)."""
    ewm_score = _all_extended_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_010_frypan_bottom_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM fry-pan bottom signal (acceleration of rounded-bottom recency)."""
    ewm_score = _frypan_bottom_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_011_homing_pigeon_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM homing pigeon signal (acceleration of dual-bear-harami recency)."""
    ewm_score = _homing_pigeon_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_012_bullish_counterattack_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM bullish counterattack signal (acceleration of meeting-line recency)."""
    ewm_score = _bullish_counterattack_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group C (extdrv3_013-018): Slope-of-slope and diff-of-slope features ---

def rev_extdrv3_013_any_extended_count_21d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 21-day extended count (rate of slope change)."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    slp = _linslope(count, _TD_MON)
    return slp.diff(_TD_WEEK)


def rev_extdrv3_014_any_extended_count_63d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 63-day extended count (quarterly slope velocity)."""
    count = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_QTR)
    slp = _linslope(count, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rev_extdrv3_015_two_bar_reversal_count_63d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 63-day two-bar reversal count."""
    count = _rolling_sum(_two_bar_reversal_flag(open, close, high, low).astype(float), _TD_QTR)
    slp = _linslope(count, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rev_extdrv3_016_tower_bottom_count_63d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 63-day tower bottom count."""
    count = _rolling_sum(_tower_bottom_flag(open, close, high, low).astype(float), _TD_QTR)
    slp = _linslope(count, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rev_extdrv3_017_any_extended_ewm_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 63-day EWM any-extended signal (cross-speed acceleration)."""
    ewm_score = _all_extended_flag(open, close, high, low).ewm(span=_TD_QTR, min_periods=1).mean()
    vel21 = ewm_score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rev_extdrv3_018_extended_density_21d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 21-day extended pattern density (slope-of-density velocity)."""
    density = _rolling_mean(_all_extended_flag(open, close, high, low), _TD_MON)
    slp = _linslope(density, _TD_MON)
    return slp.diff(_TD_WEEK)


# --- Group D (extdrv3_019-025): Volume-adjusted and composite 3rd derivatives ---

def rev_extdrv3_019_extended_vol_weighted_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day vol-weighted extended pattern score (jerk in quality)."""
    flag = _all_extended_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_MON)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_020_extended_vol_weighted_count_63d_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 63-day vol-weighted extended score (cross-horizon quality jerk)."""
    flag = _all_extended_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_QTR)
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rev_extdrv3_021_extended_near_low_density_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 63-day near-low extended pattern density (jerk in distress density)."""
    near = _near_low(close, low, _TD_MON)
    flag = _all_extended_flag(open, close, high, low).astype(bool)
    density = _rolling_mean((flag & near).astype(float), _TD_QTR)
    vel = density.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_022_extended_zscore_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of z-score of 21-day extended count (acceleration of extremity)."""
    count21 = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    z = _safe_div(count21 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_023_extended_density_252d_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 252-day extended pattern density (long-run jerk)."""
    density = _rolling_mean(_all_extended_flag(open, close, high, low), _TD_YEAR)
    vel21 = density.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rev_extdrv3_024_composite_ext_recency_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of composite EWM score across 6 core extended patterns (jerk of composite)."""
    ss = _stick_sandwich_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    ml = _matching_low_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    hp = _homing_pigeon_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    tbr = _two_bar_reversal_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    tb = _tower_bottom_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    fp = _frypan_bottom_flag(open, close, high, low).astype(float).ewm(span=_TD_MON, min_periods=1).mean()
    composite = (ss + ml + hp + tbr + tb + fp) / 6.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_extdrv3_025_extended_cluster_21d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 21-day extended cluster flag (jerk of cluster slope)."""
    count21 = _rolling_sum(_all_extended_flag(open, close, high, low), _TD_MON)
    cluster = (count21 >= 3).astype(float)
    slp = _linslope(cluster, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "rev_extdrv3_001_stick_sandwich_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_001_stick_sandwich_count_21d_5d_diff_5d_diff},
    "rev_extdrv3_002_matching_low_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_002_matching_low_count_21d_5d_diff_5d_diff},
    "rev_extdrv3_003_homing_pigeon_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_003_homing_pigeon_count_21d_5d_diff_5d_diff},
    "rev_extdrv3_004_two_bar_reversal_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_004_two_bar_reversal_count_21d_5d_diff_5d_diff},
    "rev_extdrv3_005_any_extended_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_005_any_extended_count_21d_5d_diff_5d_diff},
    "rev_extdrv3_006_any_extended_count_63d_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_006_any_extended_count_63d_21d_diff_5d_diff},
    "rev_extdrv3_007_stick_sandwich_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_007_stick_sandwich_ewm_5d_diff_5d_diff},
    "rev_extdrv3_008_two_bar_reversal_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_008_two_bar_reversal_ewm_5d_diff_5d_diff},
    "rev_extdrv3_009_any_extended_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_009_any_extended_ewm_5d_diff_5d_diff},
    "rev_extdrv3_010_frypan_bottom_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_010_frypan_bottom_ewm_5d_diff_5d_diff},
    "rev_extdrv3_011_homing_pigeon_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_011_homing_pigeon_ewm_5d_diff_5d_diff},
    "rev_extdrv3_012_bullish_counterattack_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_012_bullish_counterattack_ewm_5d_diff_5d_diff},
    "rev_extdrv3_013_any_extended_count_21d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_013_any_extended_count_21d_slope_5d_diff},
    "rev_extdrv3_014_any_extended_count_63d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_014_any_extended_count_63d_slope_5d_diff},
    "rev_extdrv3_015_two_bar_reversal_count_63d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_015_two_bar_reversal_count_63d_slope_5d_diff},
    "rev_extdrv3_016_tower_bottom_count_63d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_016_tower_bottom_count_63d_slope_5d_diff},
    "rev_extdrv3_017_any_extended_ewm_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_017_any_extended_ewm_21d_diff_5d_diff},
    "rev_extdrv3_018_extended_density_21d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_018_extended_density_21d_slope_5d_diff},
    "rev_extdrv3_019_extended_vol_weighted_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_extdrv3_019_extended_vol_weighted_count_21d_5d_diff_5d_diff},
    "rev_extdrv3_020_extended_vol_weighted_count_63d_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_extdrv3_020_extended_vol_weighted_count_63d_21d_diff_5d_diff},
    "rev_extdrv3_021_extended_near_low_density_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_021_extended_near_low_density_5d_diff_5d_diff},
    "rev_extdrv3_022_extended_zscore_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_022_extended_zscore_21d_5d_diff_5d_diff},
    "rev_extdrv3_023_extended_density_252d_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_023_extended_density_252d_21d_diff_5d_diff},
    "rev_extdrv3_024_composite_ext_recency_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_024_composite_ext_recency_5d_diff_5d_diff},
    "rev_extdrv3_025_extended_cluster_21d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_extdrv3_025_extended_cluster_21d_slope_5d_diff},
}
