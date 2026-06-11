"""
49_reversal_patterns — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative reversal-pattern features — acceleration of velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Includes acceleration features for all patterns including the six new ones:
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def rev_drv3_001_engulfing_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day engulfing count (acceleration of engulfing velocity)."""
    count = _rolling_sum(_eng_flag(open, close, high, low), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_002_any_pattern_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day any-pattern count (jerk in pattern activity)."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_003_any_pattern_count_63d_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 63-day pattern count."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_QTR)
    vel21 = count.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rev_drv3_004_krd_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day key-reversal-day count."""
    count = _rolling_sum(_krd_flag(open, close, high, low), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_005_reversal_density_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day reversal density (acceleration of pattern density)."""
    density = _rolling_mean(_any_pattern_flag(open, close, high, low), _TD_MON)
    vel = density.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_006_three_white_soldiers_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM three white soldiers signal (acceleration of tws recency)."""
    ewm_score = _three_white_soldiers_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_007_engulfing_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM engulfing signal (acceleration of recency decay velocity)."""
    ewm_score = _eng_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_008_kicker_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM bullish kicker signal."""
    ewm_score = _kicker_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_009_any_pattern_ewm_5d_diff_slope_21d(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of the 63d EWM pattern signal."""
    ewm_score = _any_pattern_flag(open, close, high, low).ewm(span=_TD_QTR, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rev_drv3_010_belt_hold_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM belt hold signal."""
    ewm_score = _belt_hold_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_011_three_inside_up_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM three inside up signal."""
    ewm_score = _three_inside_up_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_012_three_outside_up_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM three outside up signal."""
    ewm_score = _three_outside_up_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_013_any_pattern_density_21d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 21-day pattern density over 21 days."""
    density = _rolling_mean(_any_pattern_flag(open, close, high, low), _TD_MON)
    slp = _linslope(density, _TD_MON)
    return slp.diff(_TD_WEEK)


def rev_drv3_014_abandoned_baby_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of EWM abandoned baby signal (acceleration of rare pattern recency)."""
    ewm_score = _abandoned_baby_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    vel = ewm_score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_015_vol_weighted_reversal_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day volume-weighted reversal score."""
    flag = _any_pattern_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_MON)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_016_reversal_near_low_density_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 63-day near-low reversal density."""
    flag = _any_pattern_flag(open, close, high, low).astype(bool)
    near = _near_low(close, low, _TD_MON)
    density = _rolling_mean((flag & near).astype(float), _TD_QTR)
    vel = density.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_017_new_patterns_composite_ewm_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of composite EWM score across all 6 new patterns."""
    tws = _three_white_soldiers_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    ab = _abandoned_baby_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    kicker = _kicker_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    bh = _belt_hold_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    tiu = _three_inside_up_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    tou = _three_outside_up_flag(open, close, high, low).ewm(span=_TD_MON, min_periods=1).mean()
    composite = (tws + ab + kicker + bh + tiu + tou) / 6.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_018_reversal_cluster_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of the 21-day cluster flag (>=3 patterns)."""
    count21 = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_MON)
    cluster = (count21 >= 3).astype(float)
    vel = cluster.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_019_vol_weighted_reversal_63d_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 63-day vol-weighted reversal score."""
    flag = _any_pattern_flag(open, close, high, low)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    score = _rolling_sum(flag * vol_norm, _TD_QTR)
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rev_drv3_020_any_pattern_slope_63d_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 63-day pattern count (rate of slope change)."""
    count = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_QTR)
    slp = _linslope(count, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rev_drv3_021_reversal_density_252d_21d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of 21-day change in 252-day reversal density."""
    density = _rolling_mean(_any_pattern_flag(open, close, high, low), _TD_YEAR)
    vel21 = density.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rev_drv3_022_krd_count_21d_slope_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """5-day diff of OLS slope of 21-day krd count over 63 days."""
    count = _rolling_sum(_krd_flag(open, close, high, low), _TD_MON)
    slp = _linslope(count, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rev_drv3_023_new_patterns_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day new-patterns count (acceleration of new pattern activity)."""
    count = _rolling_sum(_new_patterns_flag(open, close, high, low), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_024_hammer_count_21d_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of 21-day hammer count (jerk in hammer frequency)."""
    flag = _hammer_flag(open, close, high, low) + _inv_hammer_flag(open, close, high, low)
    count = _rolling_sum((flag > 0).astype(float), _TD_MON)
    vel = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rev_drv3_025_any_pattern_zscore_5d_diff_5d_diff(
    open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """Second 5-day diff of z-score of 21-day pattern count (acceleration of extremity)."""
    count21 = _rolling_sum(_any_pattern_flag(open, close, high, low), _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    z = _safe_div(count21 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

REVERSAL_PATTERNS_REGISTRY_3RD_DERIVATIVES = {
    "rev_drv3_001_engulfing_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_001_engulfing_count_21d_5d_diff_5d_diff},
    "rev_drv3_002_any_pattern_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_002_any_pattern_count_21d_5d_diff_5d_diff},
    "rev_drv3_003_any_pattern_count_63d_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_003_any_pattern_count_63d_21d_diff_5d_diff},
    "rev_drv3_004_krd_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_004_krd_count_21d_5d_diff_5d_diff},
    "rev_drv3_005_reversal_density_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_005_reversal_density_21d_5d_diff_5d_diff},
    "rev_drv3_006_three_white_soldiers_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_006_three_white_soldiers_ewm_5d_diff_5d_diff},
    "rev_drv3_007_engulfing_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_007_engulfing_ewm_5d_diff_5d_diff},
    "rev_drv3_008_kicker_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_008_kicker_ewm_5d_diff_5d_diff},
    "rev_drv3_009_any_pattern_ewm_5d_diff_slope_21d": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_009_any_pattern_ewm_5d_diff_slope_21d},
    "rev_drv3_010_belt_hold_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_010_belt_hold_ewm_5d_diff_5d_diff},
    "rev_drv3_011_three_inside_up_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_011_three_inside_up_ewm_5d_diff_5d_diff},
    "rev_drv3_012_three_outside_up_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_012_three_outside_up_ewm_5d_diff_5d_diff},
    "rev_drv3_013_any_pattern_density_21d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_013_any_pattern_density_21d_slope_5d_diff},
    "rev_drv3_014_abandoned_baby_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_014_abandoned_baby_ewm_5d_diff_5d_diff},
    "rev_drv3_015_vol_weighted_reversal_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_drv3_015_vol_weighted_reversal_21d_5d_diff_5d_diff},
    "rev_drv3_016_reversal_near_low_density_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_016_reversal_near_low_density_5d_diff_5d_diff},
    "rev_drv3_017_new_patterns_composite_ewm_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_017_new_patterns_composite_ewm_5d_diff_5d_diff},
    "rev_drv3_018_reversal_cluster_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_018_reversal_cluster_21d_5d_diff_5d_diff},
    "rev_drv3_019_vol_weighted_reversal_63d_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low", "volume"], "func": rev_drv3_019_vol_weighted_reversal_63d_21d_diff_5d_diff},
    "rev_drv3_020_any_pattern_slope_63d_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_020_any_pattern_slope_63d_5d_diff},
    "rev_drv3_021_reversal_density_252d_21d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_021_reversal_density_252d_21d_diff_5d_diff},
    "rev_drv3_022_krd_count_21d_slope_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_022_krd_count_21d_slope_5d_diff},
    "rev_drv3_023_new_patterns_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_023_new_patterns_count_21d_5d_diff_5d_diff},
    "rev_drv3_024_hammer_count_21d_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_024_hammer_count_21d_5d_diff_5d_diff},
    "rev_drv3_025_any_pattern_zscore_5d_diff_5d_diff": {"inputs": ["open", "close", "high", "low"], "func": rev_drv3_025_any_pattern_zscore_5d_diff_5d_diff},
}
