"""
49_reversal_patterns — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base reversal-pattern features — velocity / acceleration
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Includes velocity/diff features for all patterns including the six new ones:
three white soldiers, abandoned baby, kicker, belt hold, three inside up, three outside up.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _body_abs(o: pd.Series, c: pd.Series) -> pd.Series:
    return (c - o).abs()


def _range(h: pd.Series, l: pd.Series) -> pd.Series:
    return (h - l).replace(0, np.nan)


def _upper_wick(o: pd.Series, c: pd.Series, h: pd.Series) -> pd.Series:
    return h - pd.concat([o, c], axis=1).max(axis=1)


def _lower_wick(o: pd.Series, c: pd.Series, l: pd.Series) -> pd.Series:
    return pd.concat([o, c], axis=1).min(axis=1) - l


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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
    pos = (c - lo) / rng
    return pos <= 0.10


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


# ── Pattern base helpers ──────────────────────────────────────────────────────

def _eng_flag(o, c, h, l):
    prev_bear = c.shift(1) < o.shift(1)
    today_bull = c > o
    engulfs = (o <= c.shift(1)) & (c >= o.shift(1))
    return (prev_bear & today_bull & engulfs).astype(float)


def _hammer_flag(o, c, h, l):
    rng = _range(h, l)
    body = _body_abs(o, c)
    lw = _lower_wick(o, c, l)
    uw = _upper_wick(o, c, h)
    small_body = body <= rng * 0.33
    long_lower = lw >= body * 2.0
    short_upper = uw <= body * 0.5
    body_upper_half = pd.concat([o, c], axis=1).min(axis=1) >= l + rng * 0.5
    return (small_body & long_lower & short_upper & body_upper_half).astype(float)


def _inv_hammer_flag(o, c, h, l):
    rng = _range(h, l)
    body = _body_abs(o, c)
    lw = _lower_wick(o, c, l)
    uw = _upper_wick(o, c, h)
    small_body = body <= rng * 0.33
    long_upper = uw >= body * 2.0
    short_lower = lw <= body * 0.5
    body_lower_half = pd.concat([o, c], axis=1).max(axis=1) <= l + rng * 0.5
    return (small_body & long_upper & short_lower & body_lower_half).astype(float)


def _morning_star_flag(o, c, h, l):
    bar1_bear = c.shift(2) < o.shift(2)
    bar1_body = _body_abs(o.shift(2), c.shift(2))
    bar2_small = _body_abs(o.shift(1), c.shift(1)) <= bar1_body * 0.35
    bar3_bull = c > o
    bar3_recovers = c > (o.shift(2) + c.shift(2)) / 2.0
    return (bar1_bear & bar2_small & bar3_bull & bar3_recovers).astype(float)


def _krd_flag(o, c, h, l):
    new_low = l < _rolling_min(l.shift(1), _TD_MON)
    closes_up = c > c.shift(1)
    return (new_low & closes_up).astype(float)


def _three_white_soldiers_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    b3_bull = c > o
    b2_bull = c.shift(1) > o.shift(1)
    b1_bull = c.shift(2) > o.shift(2)
    b3_long = _body_abs(o, c) > atr14 * 0.5
    b2_long = _body_abs(o.shift(1), c.shift(1)) > atr14 * 0.5
    b1_long = _body_abs(o.shift(2), c.shift(2)) > atr14 * 0.5
    b3_opens_in_b2 = (o >= o.shift(1)) & (o <= c.shift(1))
    b2_opens_in_b1 = (o.shift(1) >= o.shift(2)) & (o.shift(1) <= c.shift(2))
    b3_higher = c > c.shift(1)
    b2_higher = c.shift(1) > c.shift(2)
    b3_near_high = _upper_wick(o, c, h) <= _body_abs(o, c) * 0.20
    b2_near_high = _upper_wick(o.shift(1), c.shift(1), h.shift(1)) <= _body_abs(o.shift(1), c.shift(1)) * 0.20
    return (b3_bull & b2_bull & b1_bull & b3_long & b2_long & b1_long
            & b3_opens_in_b2 & b2_opens_in_b1 & b3_higher & b2_higher
            & b3_near_high & b2_near_high).astype(float)


def _abandoned_baby_flag(o, c, h, l):
    rng2 = _range(h.shift(1), l.shift(1))
    body2 = _body_abs(o.shift(1), c.shift(1))
    is_doji_mid = body2 <= rng2 * 0.10
    gap_down_in = l.shift(2) > h.shift(1)
    gap_up_out = l > h.shift(1)
    bar3_bull = c > o
    return (gap_down_in & is_doji_mid & gap_up_out & bar3_bull).astype(float)


def _kicker_flag(o, c, h, l):
    bar1_bear = c.shift(1) < o.shift(1)
    gap_up_open = o > o.shift(1)
    bar2_bull = c > o
    return (bar1_bear & gap_up_open & bar2_bull).astype(float)


def _belt_hold_flag(o, c, h, l):
    atr14 = _atr(c, h, l, 14)
    lw = _lower_wick(o, c, l)
    body = _body_abs(o, c)
    bar_bull = c > o
    tiny_lw = lw <= atr14 * 0.05
    long_body = body >= atr14 * 0.7
    prior_down = c.shift(1) < c.shift(3)
    return (bar_bull & tiny_lw & long_body & prior_down).astype(float)


def _three_inside_up_flag(o, c, h, l):
    b1_bear = c.shift(2) < o.shift(2)
    b2_inside = (o.shift(1) > c.shift(2)) & (o.shift(1) < o.shift(2)) & (c.shift(1) > c.shift(2)) & (c.shift(1) < o.shift(2))
    b3_bull = c > o
    b3_higher = c > c.shift(1)
    return (b1_bear & b2_inside & b3_bull & b3_higher).astype(float)


def _three_outside_up_flag(o, c, h, l):
    b1_bear = c.shift(2) < o.shift(2)
    b2_bull = c.shift(1) > o.shift(1)
    b2_engulfs = (o.shift(1) <= c.shift(2)) & (c.shift(1) >= o.shift(2))
    b3_bull = c > o
    b3_higher = c > c.shift(1)
    return (b1_bear & b2_bull & b2_engulfs & b3_bull & b3_higher).astype(float)


def _any_pattern_flag(o, c, h, l):
    harami = (
        (c.shift(1) < o.shift(1)) & (c > o)
        & (o > c.shift(1)) & (o < o.shift(1))
        & (c > c.shift(1)) & (c < o.shift(1))
    ).astype(float)
    tweezer = (
        ((l - l.shift(1)).abs() <= _atr(c, h, l, 14) * 0.10)
        & (c.shift(1) < c.shift(2))
    ).astype(float)
    piercing = (
        (c.shift(1) < o.shift(1)) & (o < l.shift(1))
        & (c > (o.shift(1) + c.shift(1)) / 2.0) & (c > o)
    ).astype(float)
    outside_up = (
        (h > h.shift(1)) & (l < l.shift(1)) & (c > o)
        & (c >= (l + (h - l) * 0.60))
    ).astype(float)
    total = (
        _eng_flag(o, c, h, l) + _hammer_flag(o, c, h, l) + _inv_hammer_flag(o, c, h, l)
        + _morning_star_flag(o, c, h, l) + harami + tweezer + piercing + outside_up
        + _three_white_soldiers_flag(o, c, h, l) + _abandoned_baby_flag(o, c, h, l)
        + _kicker_flag(o, c, h, l) + _belt_hold_flag(o, c, h, l)
        + _three_inside_up_flag(o, c, h, l) + _three_outside_up_flag(o, c, h, l)
    )
    return (total > 0).astype(float)


def _new_patterns_flag(o, c, h, l):
    total = (
        _three_white_soldiers_flag(o, c, h, l)
        + _abandoned_baby_flag(o, c, h, l)
        + _kicker_flag(o, c, h, l)
        + _belt_hold_flag(o, c, h, l)
        + _three_inside_up_flag(o, c, h, l)
        + _three_outside_up_flag(o, c, h, l)
    )
    return (total > 0).astype(float)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

# --- Group A (drv2_001-008): 5-day diffs of base pattern counts ---

def rev_drv2_001_engulfing_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day bullish-engulfing count (velocity of engulfing frequency)."""
    count = _rolling_sum(_eng_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_drv2_002_hammer_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day hammer count (velocity of hammer frequency)."""
    flag = _hammer_flag(open, close, high, low) + _inv_hammer_flag(open, close, high, low)
    count = _rolling_sum((flag > 0).astype(float), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_drv2_003_any_pattern_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day any-pattern count."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_drv2_004_any_pattern_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day any-pattern count (monthly velocity of pattern activity)."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_QTR)
    return count.diff(_TD_MON)


def rev_drv2_005_krd_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day key-reversal-day count."""
    count = _rolling_sum(_krd_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_drv2_006_three_white_soldiers_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day three white soldiers count (velocity of tws frequency)."""
    count = _rolling_sum(_three_white_soldiers_flag(open, close, high, low), _TD_QTR)
    return count.diff(_TD_MON)


def rev_drv2_007_kicker_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day bullish kicker count (velocity of kicker frequency)."""
    count = _rolling_sum(_kicker_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_drv2_008_new_patterns_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day count of the 6 new candlestick patterns."""
    count = _rolling_sum(_new_patterns_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


# --- Group B (drv2_009-016): Slopes and trend of pattern signals ---

def rev_drv2_009_any_pattern_count_21d_slope_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 21-day pattern count over trailing 21 days."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_MON)
    return _linslope(count, _TD_MON)


def rev_drv2_010_krd_count_21d_slope_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 21-day krd count over trailing 63 days."""
    count = _rolling_sum(_krd_flag(open, close, high, low), _TD_MON)
    return _linslope(count, _TD_QTR)


def rev_drv2_011_engulfing_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of EWM-decayed engulfing signal."""
    ewm_score = _eng_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_drv2_012_three_white_soldiers_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of EWM-decayed three white soldiers signal."""
    ewm_score = _three_white_soldiers_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_drv2_013_any_pattern_ewm_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day EWM-decayed any-pattern signal."""
    ewm_score = _any_pattern_flag(open, close, high, low).ewm(span=_TD_QTR, min_periods=1).mean()
    return ewm_score.diff(_TD_MON)


def rev_drv2_014_kicker_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of EWM-decayed bullish kicker signal."""
    ewm_score = _kicker_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_drv2_015_reversal_density_252d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 252-day reversal-pattern density."""
    density = _rolling_mean(_any_pattern_flag(open, close, high, low), _TD_YEAR)
    return density.diff(_TD_MON)


def rev_drv2_016_reversal_zscore_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of z-score of 21-day pattern count."""
    count21 = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    z = _safe_div(count21 - m, s)
    return z.diff(_TD_WEEK)


# --- Group C (drv2_017-025): Volume-pattern and new-pattern velocity ---

def rev_drv2_017_vol_weighted_reversal_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day volume-weighted reversal score."""
    flag = _any_pattern_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_MON)
    return score.diff(_TD_WEEK)


def rev_drv2_018_reversal_near_low_density_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 63-day reversal-at-near-low density."""
    flag = _any_pattern_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    density = _rolling_mean((flag & near).astype(float), _TD_QTR)
    return density.diff(_TD_WEEK)


def rev_drv2_019_belt_hold_count_21d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day belt hold count (velocity of belt hold frequency)."""
    count = _rolling_sum(_belt_hold_flag(open, close, high, low), _TD_MON)
    return count.diff(_TD_WEEK)


def rev_drv2_020_three_inside_up_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day three inside up count."""
    count = _rolling_sum(_three_inside_up_flag(open, close, high, low), _TD_QTR)
    return count.diff(_TD_MON)


def rev_drv2_021_three_outside_up_count_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """21-day diff of 63-day three outside up count."""
    count = _rolling_sum(_three_outside_up_flag(open, close, high, low), _TD_QTR)
    return count.diff(_TD_MON)


def rev_drv2_022_new_patterns_recency_ewm_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of EWM-decayed signal for all 6 new candlestick patterns combined."""
    ewm_score = _new_patterns_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    return ewm_score.diff(_TD_WEEK)


def rev_drv2_023_vol_weighted_reversal_63d_21d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """21-day diff of 63-day volume-weighted reversal score."""
    flag = _any_pattern_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_QTR)
    return score.diff(_TD_MON)


def rev_drv2_024_any_pattern_slope_63d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope of 63-day pattern count over trailing 63 days."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_QTR)
    return _linslope(count, _TD_QTR)


def rev_drv2_025_composite_new_pattern_recency_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of average EWM score across all 6 new candlestick patterns."""
    tws = _three_white_soldiers_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    ab = _abandoned_baby_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    kicker = _kicker_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    bh = _belt_hold_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    tiu = _three_inside_up_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    tou = _three_outside_up_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    composite = (tws + ab + kicker + bh + tiu + tou) / 6.0
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_REGISTRY_2ND_DERIVATIVES = {
    "rev_drv2_001_engulfing_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_001_engulfing_count_21d_5d_diff},
    "rev_drv2_002_hammer_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_002_hammer_count_21d_5d_diff},
    "rev_drv2_003_any_pattern_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_003_any_pattern_count_21d_5d_diff},
    "rev_drv2_004_any_pattern_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_004_any_pattern_count_63d_21d_diff},
    "rev_drv2_005_krd_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_005_krd_count_21d_5d_diff},
    "rev_drv2_006_three_white_soldiers_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_006_three_white_soldiers_count_63d_21d_diff},
    "rev_drv2_007_kicker_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_007_kicker_count_21d_5d_diff},
    "rev_drv2_008_new_patterns_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_008_new_patterns_count_21d_5d_diff},
    "rev_drv2_009_any_pattern_count_21d_slope_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_009_any_pattern_count_21d_slope_21d},
    "rev_drv2_010_krd_count_21d_slope_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_010_krd_count_21d_slope_63d},
    "rev_drv2_011_engulfing_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_011_engulfing_recency_ewm_5d_diff},
    "rev_drv2_012_three_white_soldiers_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_012_three_white_soldiers_recency_ewm_5d_diff},
    "rev_drv2_013_any_pattern_ewm_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_013_any_pattern_ewm_21d_diff},
    "rev_drv2_014_kicker_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_014_kicker_recency_ewm_5d_diff},
    "rev_drv2_015_reversal_density_252d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_015_reversal_density_252d_21d_diff},
    "rev_drv2_016_reversal_zscore_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_016_reversal_zscore_21d_5d_diff},
    "rev_drv2_017_vol_weighted_reversal_21d_5d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_drv2_017_vol_weighted_reversal_21d_5d_diff},
    "rev_drv2_018_reversal_near_low_density_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_018_reversal_near_low_density_5d_diff},
    "rev_drv2_019_belt_hold_count_21d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_019_belt_hold_count_21d_5d_diff},
    "rev_drv2_020_three_inside_up_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_020_three_inside_up_count_63d_21d_diff},
    "rev_drv2_021_three_outside_up_count_63d_21d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_021_three_outside_up_count_63d_21d_diff},
    "rev_drv2_022_new_patterns_recency_ewm_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_022_new_patterns_recency_ewm_5d_diff},
    "rev_drv2_023_vol_weighted_reversal_63d_21d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_drv2_023_vol_weighted_reversal_63d_21d_diff},
    "rev_drv2_024_any_pattern_slope_63d": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_024_any_pattern_slope_63d},
    "rev_drv2_025_composite_new_pattern_recency_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv2_025_composite_new_pattern_recency_5d_diff},
}
